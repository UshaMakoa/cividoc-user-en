# CiviDocRewriteByAI.py
# Prompt‑based rewriting of CiviCRM documentation using multiple AI models with persistent model memory
#
# you must install the modules 
# and set the environment variables OPENAI_API_KEY and PERPLEXITY_API_KEY
# you can create api keys on https://platform.openai.com/ and https://perplexity.ai/api
#
# If you set include_section environment variable, only that section will be processed (even if you fill the exclude list)
#
# TODO: handle rate limits and errors more gracefully
# 
# @alain.benbassat, @davem, @usha.makoa
# CiviCamp 2025 - Lunteren, Netherlands

 
import os
import re
import time
import random
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm
from openai import OpenAI

# === CONFIGURATION ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-yourkeyhere")
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_NAME", "pplx-yourkeyhere")

BASE_URL = "https://docs.civicrm.org/user/en/latest/"
OUTPUT_DIR = "sonarprogenerated-docs"

# 🔧 Par défaut, on n’exclut rien et on n’inclut rien de spécifique
EXCLUDE_SECTIONS = os.getenv("EXCLUDE_SECTIONS", "")
INCLUDE_SECTION = os.getenv("INCLUDE_SECTION", "")

# Transformation pour les rendre exploitables sous forme de liste / chaîne
EXCLUDE_SECTIONS = [s.strip() for s in EXCLUDE_SECTIONS.split(",") if s.strip()]
INCLUDE_SECTION = INCLUDE_SECTION.strip() or None

#🎯 Seulement EVENTS
#setx INCLUDE_SECTION "events"
#python 01CiviDocRewriteByAI.py
#🚫 Exclure certaines sections
#setx EXCLUDE_SECTIONS "membership,email"
#python 01CiviDocRewriteByAI.py

# === Clients API ===
client_openai = OpenAI(api_key=OPENAI_API_KEY)
client_pplx = OpenAI(api_key=PERPLEXITY_API_KEY, base_url="https://api.perplexity.ai")

# === Rotation multi‑modèles (2025 generation) ===
MODELS = [
    ("perplexity", "sonar-pro"),    # modèle raisonnement web
    ("perplexity", "sonar"),        # modèle de base
    #("perplexity", "llama-3.1-sonar-large-128k-online"), # modèle étendu
    ("openai", "gpt-4.1-mini"),          # standard lightweight
    ("openai", "gpt-4.1"),               # plus robuste
    ("openai", "gpt-4o-mini"),           # plus rapide
    ("openai", "gpt-5-mini"),            # nouvelle génération compacte
    ("openai", "gpt-5-nano"),            # nouvelle génération compacte
    ("openai", "gpt-5"),                 # modèle principal GPT‑5
    ("openai", "o3-mini"),               # modèle reasoning alternatif
]

# === PROMPT Diataxis CiviCRM ===
PROMPT = """
Rewrite the content of https://docs.civicrm.org/some/page/ for an audience of non-profit users of CiviCRM who are not experts and are learning to perform specific tasks.

Structure the new documentation according to the Diátaxis framework (https://diataxis.fr/start-here/):

Determine if this page is a Tutorial (step-by-step for first-time use), Guide (problem-oriented how-to), Reference (systematic, factual), or Explanation (background, “why”, architecture)—add your reasoning as a comment at the end if unsure.

Assign a categories value: one of "Tutorial", "Guide", "Reference", or "Explanation".

Suggest an appropriate level: Basic, Intermediate, or Advanced.

Write a clear, one-sentence summary tailored for a non-expert CiviCRM audience.

Specify the section in which this page logically belongs (based on its topic).

Use this template at the very top of the output, with no intro or lead-in, and do not include any content before the front matter (You often put content before the front matter like '# Source: https://docs.civicrm.org/user/en/latest/introduction/what-is-civicrm/", don't do that this time.)
:

...
text
---
categories:
level:
summary:
section:
---

# <Title>
## <Section 1>

your text here...

# comment: Source: https://docs.civicrm.org/some/page/
# comment: Suggestion: https://docs.civicrm.org/some/page/

...

Diátaxis guidelines for writing:

For a Tutorial: Provide a hands-on, step-by-step lesson with clear, sequential instructions; use an encouraging and supportive tone; pre-empt user confusion and call out pitfalls.

For a How-to Guide: Address a specific goal or problem; phrase each step as an action for users to perform; no background, no explanation—focus on "how" not "why".

For a Reference: Be concise and precise; list facts, API details, configuration, or exhaustive options; no procedural or motivational text.

For an Explanation: Clarify difficult concepts, context, or relationships in CiviCRM; address “why” and broader understanding, often using examples.

Split the content into several pages using “=== NEW PAGE ===” if this will help non-experts, and label each page appropriately and write a front.matter also for this new page and write (as a title) this is a 'Suggestion''

Additional style requirements:

Write in plain, inclusive, and professional English.

Use sentence case for all titles/headings and keep titles short and direct.

Avoid links, footnotes, or horizontal lines in the body (no <hr>).

Emphasize approachability: prefer “you” and “your organisation”, conversational explanations, and encouragement.

Directly format the output as Markdown; do not output HTML or any annotation.

Do not duplicate material across split pages; group similar topics together for clarity.

If you believe the page overlaps multiple Diátaxis types (for example, both Guide and Reference), suggest in a comment at the end which parts should be split off for best clarity and learning.

I repeat : Use plain, inclusive English.

"""

visited = set()
current_model_index = 0  # On garde en mémoire le dernier modèle utilisé avec succès

# === UTILS ===
from pathlib import Path
from urllib.parse import urlparse

def ensure_folder(url, base_folder):
    """Recreate original folder structure from civicrm.org URLs."""
    relative = url.replace(BASE_URL, "").strip("/")
    relative = relative.split("#")[0]  # remove anchors if any
    folder = Path(base_folder) / Path(os.path.dirname(relative))
    folder.mkdir(parents=True, exist_ok=True)
    return str(folder), os.path.basename(relative) or "index"

def file_already_exists(url):
    folder, name = ensure_folder(url, OUTPUT_DIR)
    safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", name)
    return os.path.exists(os.path.join(folder, f"{safe_name}.md"))

def get_links(url):
    global INCLUDE_SECTION, EXCLUDE_SECTIONS

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except Exception:
        return []

    soup = BeautifulSoup(r.text, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        link = urljoin(url, a["href"])

        # ❌ S’assure que le lien est bien dans la doc CiviCRM
        if not link.startswith(BASE_URL):
            continue

        # 🎯 Si INCLUDE_SECTION est spécifié : inclure uniquement cette section
        if INCLUDE_SECTION:
            if f"/{INCLUDE_SECTION.strip('/')}/" not in link:
                continue

        # 🚫 Sinon, appliquer exclure uniquement si EXCLUDE_SECTIONS n’est pas vide
        elif any(ex.strip('/') in link for ex in EXCLUDE_SECTIONS):
            continue

        if link not in visited and "#" not in link:
            links.append(link)

    return links


# === API LOGIC — Garde le dernier modèle qui marche ===
def ai_rewrite(content):
    global current_model_index
    full_prompt = f"{PROMPT}\n\n{content}"
    max_retries = 6
    attempts = 0

    while attempts < max_retries:
        provider, model = MODELS[current_model_index]
        print(f"\n🧠 Using {provider}:{model} (attempt {attempts+1}/{max_retries})")

        try:
            if provider == "openai":
                resp = client_openai.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": full_prompt}],
                    temperature=0.4,
                )
            else:
                resp = client_pplx.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": full_prompt}],
                    temperature=0.4,
                )

            print(f"✅ Success with {provider}:{model}")
            return resp.choices[0].message.content

        except Exception as e:
            print(f"❌ Error ({provider}:{model}): {e}")
            attempts += 1
            wait_time = 2 * (2 ** attempts) + random.uniform(0, 2)

            # Change de modèle seulement en cas d’erreur
            current_model_index = (current_model_index + 1) % len(MODELS)
            new_provider, new_model = MODELS[current_model_index]
            print(f"🔄 Switching to {new_provider}:{new_model} after {wait_time:.1f}s...")
            time.sleep(wait_time)
            continue

    print("🚫 All models failed after several retries.")
    return ""

# === NORMALIZE HEADERS ===
def normalize_markdown_headers(content):
    """
    Normalize markdown headers: preserve existing capitalization exactly as written.
    Ensure the spacing and '#' syntax are consistent.
    """
    lines = content.splitlines()
    normalized = []
    for line in lines:
        # Match Markdown headers (H1 to H6)
        match = re.match(r"^(#{1,6})\s*(.*)", line)
        if match:
            hashes, text = match.groups()
            text = text.strip()  # Clean space
            # Do NOT modify capitalization, just ensure proper spacing
            normalized.append(f"{hashes} {text}")
        else:
            normalized.append(line)
    return "\n".join(normalized)

# === SAVE FILES ===
from pathlib import Path

def save_markdown(url, content, base_folder, index=None):
    """Save each rewritten or split Markdown file into the docs structure."""
    folder, name = ensure_folder(url, base_folder)
    safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", name)
    suffix = f"-part{index}" if index else ""
    path = Path(folder) / f"{safe_name}{suffix}.md"
    path.parent.mkdir(parents=True, exist_ok=True)

    # 🧩 Apply header normalization before writing
    clean_content = normalize_markdown_headers(content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(clean_content)

    print(f"💾 Saved → {path}")


# === PAGE PROCESSING ===
def process_page(url):
    if url in visited:
        return
    visited.add(url)

    if file_already_exists(url):
        print(f"⏭️ Already exists: {url}")
        return

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"❌ Fetch failed {url}: {e}")
        return

    text = BeautifulSoup(r.text, "html.parser").get_text()
    ai_md = ai_rewrite(text)
    if not ai_md:
        return

    # 🧩 All output now goes to OUTPUT_DIR
    if "=== NEW PAGE ===" in ai_md:
        parts = [p.strip() for p in ai_md.split("=== NEW PAGE ===") if p.strip()]
        for i, part in enumerate(parts, 1):
            save_markdown(url, part, OUTPUT_DIR, i)
    else:
        save_markdown(url, ai_md, OUTPUT_DIR)
    time.sleep(1)

# === CRAWLER ===
def crawl(start_url):
    queue = [start_url]
    while queue:
        current = queue.pop()
        process_page(current)
        for link in get_links(current):
            if link not in visited:
                queue.append(link)

if __name__ == "__main__":
    print("🚀 Launching CiviCRM generator with persistent model memory...")
    print(f"🧩 Model pool size: {len(MODELS)}")
    crawl(BASE_URL)
    print(f"🎉 Done. Content saved in '{OUTPUT_DIR}' — all files, including splits, are now structured under docs/")
if INCLUDE_SECTION:
    print(f"🎯 Mode INCLUDE → uniquement la section '{INCLUDE_SECTION}'")
elif EXCLUDE_SECTIONS:
    print(f"🚫 Mode EXCLUDE → exclus les sections {EXCLUDE_SECTIONS}")
else:
    print("✅ Mode FULL → aucune exclusion, toutes les sections incluses")

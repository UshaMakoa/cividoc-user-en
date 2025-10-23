# CiviDocRewriteByAI.py
# Prompt‑based rewriting of CiviCRM documentation using multiple AI models with persistent model memory
#
# you must set the environment variables OPENAI_API_KEY and PERPLEXITY_API_KEY
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
PERPLEXITY_API_KEY = os.getenv("civicrm doc", "pplx-yourkeyhere")

BASE_URL = "https://docs.civicrm.org/user/en/latest/"
OUTPUT_DIR = "ai_generated_docs"
SPLIT_DIR = "split_docs"
EXCLUDE_SECTIONS = ["membership", "email", "events"]

# === Clients API ===
client_openai = OpenAI(api_key=OPENAI_API_KEY)
client_pplx = OpenAI(api_key=PERPLEXITY_API_KEY, base_url="https://api.perplexity.ai")

# === Rotation multi‑modèles (2025 generation) ===
MODELS = [
    ("perplexity", "gpt-5-mini"),            # nouvelle génération compacte
    ("perplexity", "gpt-5-nano"),            # nouvelle génération compacte
    ("perplexity", "sonar"),        # modèle de base
    ("perplexity", "sonar-pro"),    # modèle raisonnement web
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
I want to re-write [https://docs.civicrm.org/some/page/](https://docs.civicrm.org/some/page/) 
for an audience of non-profit users of CiviCRM who are not experts and are learning how to undertake specific tasks on the system.
We’re building our documentation using the Diataxis framework (https://diataxis.fr/start-here/) 
so mark the document as one of: Tutorial, Guide, Reference or Explanation labelled as “categories”. 
Suggest the level as Basic, Intermediate or Advanced.
Provide a one sentence summary of the page and use this format for the top of the page.

---
categories:
level:
summary:
section:
---

# <Title>
## <Section 1>
...

The title of the page should be H1 and the output should be in markdown.
The language should be inclusive and encouraging with a professional but approachable tone.
Use plain English and sentence case for titles, following the style guide at:
https://docs.google.com/document/d/1CQQW9gVTytipP7s-RgbddF_oSCX3t9yUnJ4Bl-Yu_1A
Suggest splitting into multiple pages if appropriate based on simpler or more complex subjects.
Avoid links or separators like <hr>. Use plain, inclusive English.
If the content should be split into multiple pages, separate each with the line:
=== NEW PAGE ===
"""

visited = set()
current_model_index = 0  # On garde en mémoire le dernier modèle utilisé avec succès

# === UTILS ===
def ensure_folder(url, base_folder):
    relative = url.replace(BASE_URL, "").strip("/")
    folder = os.path.join(base_folder, os.path.dirname(relative))
    os.makedirs(folder, exist_ok=True)
    return folder, os.path.basename(relative) or "index"

def file_already_exists(url):
    folder, name = ensure_folder(url, OUTPUT_DIR)
    safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", name)
    return os.path.exists(os.path.join(folder, f"{safe_name}.md"))

def get_links(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except Exception:
        return []
    soup = BeautifulSoup(r.text, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        link = urljoin(url, a["href"])
        if not link.startswith(BASE_URL): continue
        if any(x in link for x in EXCLUDE_SECTIONS): continue
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

# === SAUVEGARDE ===
def save_markdown(url, content, base_folder, index=None):
    folder, name = ensure_folder(url, base_folder)
    safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", name)
    suffix = f"-part{index}" if index else ""
    path = os.path.join(folder, f"{safe_name}{suffix}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Source: {url}\n\n{content}")
    print(f"💾 Saved {path}")

# === TRAITEMENT DE PAGE ===
def process_page(url):
    if url in visited: return
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

    if "=== NEW PAGE ===" in ai_md:
        parts = [p.strip() for p in ai_md.split("=== NEW PAGE ===") if p.strip()]
        for i, part in enumerate(parts, 1):
            save_markdown(url, part, SPLIT_DIR, i)
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
    print(f"🎉 Done. Content in '{OUTPUT_DIR}' and '{SPLIT_DIR}'.")

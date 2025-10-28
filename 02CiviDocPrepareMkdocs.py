# 02CiviDocPrepareMkdocs.py
#
# Prepare MkDocs site for CiviCRM User Documentation
# --------------------------------------------------
# ✓ Merge sonarprogenerated-docs/ into docs/
# ✓ Clean YAML, comments, and lists (safe for markdown)
# ✓ Fix orphan comment tags (--> / <!--)
# ✓ Generate mkdocs.yml using official nav from mkdocs_nav_template.yml
# ✓ Append extra generated pages (part1, part2…) to correct sections
# ✓ Include mkdocs-categories plugin
#
# Usage: python 02CiviDocPrepareMkdocs.py
# Requires: pip install pyyaml
# Optional: provide a file mkdocs_nav_template.yml from official repo
#
# @alain.benbassat, @davem, @usha.makoa, CiviCamp 2025


import os, re, shutil, yaml
from pathlib import Path


SOURCE_DIRS = ["sonarprogenerated-docs"]
TARGET_DIR = "docs"
MKDOCS_YML = "mkdocs.yml"
MKDOCS_NAV_TEMPLATE = "mkdocs_nav_template.yml"


# === 1️⃣ LOAD OFFICIAL NAV TEMPLATE ===
def load_official_nav(template_path):
    if not os.path.exists(template_path):
        raise FileNotFoundError(
            f"❌ Missing navigation template file: {template_path}. "
            "Provide your original mkdocs_nav_template.yml from https://docs.civicrm.org/user/en/latest/"
        )
    with open(template_path, encoding="utf-8") as f:
        nav_yaml = yaml.safe_load(f)
        return nav_yaml["nav"] if "nav" in nav_yaml else nav_yaml


# === 2️⃣ MERGE SOURCE FILES INTO DOCS ===
def merge_to_docs(sources, target):
    if os.path.exists(target):
        print(f"🧹 Cleaning {target}/ …")
        shutil.rmtree(target)
    os.makedirs(target, exist_ok=True)
    for src in sources:
        if not os.path.exists(src):
            continue
        print(f"📂 Copying from {src}/ …")
        for root, _, files in os.walk(src):
            for file in files:
                if not file.endswith(".md"):
                    continue
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, src)
                dest_path = os.path.join(target, rel_path)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy2(src_path, dest_path)
    print(f"✅ Markdown copied into {target}/")


# === 3️⃣ CLEAN MARKDOWN: FRONTMATTER, COMMENTS, LISTS ===

def normalize_lists_and_comments(text):
    """Remet en forme commentaires, listes et évite les tags orphelins."""
    # 1. Remplace les # comment: ... par <!-- ... -->
    text = re.sub(r"(?m)^#\s*comment:\s*(.*)$", r"<!-- \1 -->", text)

    # 2. Nettoie les balises orphelines :
    # Supprime tout <!-- sans fermeture
    text = re.sub(r"<\!--\s*$", "", text, flags=re.M)
    # Supprime tout --> sans ouverture
    text = re.sub(r"^\s*-->", "", text, flags=re.M)

    # 3. Forcer un saut de ligne après <!-- ... -->
    text = re.sub(r"(<!--.*?-->)", r"\1\n", text, flags=re.DOTALL)

    # 4. Correction des "listes" flattées :
    text = re.sub(
        r"(\d+\.)\s+([A-Z0-9].*?)(?=\s*\d+\.|$)",
        lambda m: f"\n{m.group(1)} {m.group(2).strip()}\n",
        text, flags=re.S,
    )
    text = re.sub(
        r"(-)\s+([A-Z0-9].*?)(?=\s*-|$)",
        lambda m: f"\n{m.group(1)} {m.group(2).strip()}\n",
        text, flags=re.S,
    )
    # 5. Nettoie les [¶](...) et espaces fin de ligne
    text = re.sub(r"\[¶\]\([^)]+\)", "", text)
    text = re.sub(r"[ \t]+$", "", text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def clean_markdown_files(folder):
    print("🧽 Cleaning frontmatter & fixing Markdown syntax …")
    for root, _, files in os.walk(folder):
        for f in files:
            if not f.endswith(".md"):
                continue
            path = Path(root, f)
            text = path.read_text(encoding="utf-8")

            # keep after valid front matter start
            text = re.sub(r"^[\s\S]*?(?=---\s*\n)", "", text, count=1)
            text = normalize_lists_and_comments(text)

            # Ensure valid categories block
            if "categories:" not in text:
                text = re.sub(
                    r"^(---\s*\n)", r"\1categories:\n  - Uncategorized\n", text
                )
            else:
                text = re.sub(
                    r'(?m)^categories:\s*"?([\w\s\-|]+)"?$',
                    r'categories:\n  - \1',
                    text,
                )

            # Remove leftover comment lines after YAML
            lines = text.splitlines()
            last_hr = None
            for i, line in enumerate(lines):
                if line.strip() == "---":
                    last_hr = i
            if last_hr is not None:
                retained = lines[:last_hr + 1]
                for line in lines[last_hr + 1:]:
                    if not re.match(r"^\s*<\!--", line):
                        retained.append(line)
                text = "\n".join(retained).strip() + "\n"

            path.write_text(text, encoding="utf-8")
    print("✅ Markdown normalized successfully.")


# === 4️⃣ NAVIGATION MERGE: ADD NEW FILES (part1, part2...) ===
def all_md_files(base):
    for root, _, files in os.walk(base):
        for f in files:
            if f.endswith(".md"):
                yield os.path.relpath(os.path.join(root, f), base).replace("\\", "/")


def add_missing_md(nav_section, base, known_paths):
    """Recursively add new .md files (parts) into corresponding section."""
    if not isinstance(nav_section, list):
        return nav_section
    for i, entry in enumerate(nav_section):
        if isinstance(entry, dict):
            for key, value in entry.items():
                nav_section[i][key] = add_missing_md(value, base, known_paths)
    # detect directory for insertion
    for md_path in all_md_files(base):
        if md_path not in known_paths:
            base_dir = os.path.dirname(md_path)
            for i, entry in enumerate(nav_section):
                if isinstance(entry, dict):
                    for key, _ in entry.items():
                        key_dir = key.lower().replace(" ", "-")
                        if key_dir in base_dir and not any(md_path in str(v) for v in nav_section):
                            print(f"➕ Adding extra file: {md_path}")
                            entry[key].append({os.path.basename(md_path): md_path})
                            known_paths.add(md_path)
                            break
    return nav_section


# === 5️⃣ MAIN ===
if __name__ == "__main__":
    print("🚀 Preparing CiviCRM MkDocs structure…")
    merge_to_docs(SOURCE_DIRS, TARGET_DIR)
    clean_markdown_files(TARGET_DIR)

    if not os.path.exists(MKDOCS_NAV_TEMPLATE):
        raise SystemExit("❌ Provide 'mkdocs_nav_template.yml' from official CiviCRM docs.")

    with open(MKDOCS_NAV_TEMPLATE, "r", encoding="utf-8") as f:
        official_config = yaml.safe_load(f)

    nav = official_config["nav"]
    known_paths = set()
    for item in nav:
        for v in item.values() if isinstance(item, dict) else []:
            for sub in v if isinstance(v, list) else []:
                if isinstance(sub, dict):
                    for _, path_val in sub.items():
                        if isinstance(path_val, str) and path_val.endswith(".md"):
                            known_paths.add(path_val)

    updated_nav = add_missing_md(nav, TARGET_DIR, known_paths)

    official_config["nav"] = updated_nav
    with open(MKDOCS_YML, "w", encoding="utf-8") as f:
        yaml.dump(official_config, f, sort_keys=False, allow_unicode=True, width=160)

    print("🎉 mkdocs.yml successfully updated with official nav order and extra part files!")

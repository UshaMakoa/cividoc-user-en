# 02CiviDocPrepareMkdocs.py
#
# Prepare MkDocs site for CiviCRM User documentation
# --------------------------------------------------
# ✓ Merge ai_generated_docs/ and split_docs/ into docs/
# ✓ Clean YAML front matter & comments
# ✓ Generate mkdocs.yml (navigation respecting official order)
# ✓ Include categories-plugin configuration
#
# Usage: python 02CiviDocPrepareMkdocs.py
# Requires: pip install pyyaml
#
# @alain.benbassat, @davem, @usha.makoa

import os, re, shutil, yaml
from pathlib import Path

SOURCE_DIRS = ["ai_generated_docs", "split_docs"]
TARGET_DIR = "docs"
MKDOCS_YML = "mkdocs.yml"

# === CONFIG MkDocs === #
mkdocs_config = {
    "site_name": "CiviCRM User Guide",
    "site_url": "https://docs.civicrm.org/user/en/latest/",
    "repo_url": "https://lab.civicrm.org/documentation/docs/user-en/",
    "edit_uri": "https://lab.civicrm.org/documentation/docs/user-en/-/edit/master/docs/",
    "site_description": "A guide for CiviCRM users.",
    "site_author": "The CiviCRM community",
    "theme": {
        "name": "material",
        "icon": {"repo": "fontawesome/brands/gitlab"}
    },
    "markdown_extensions": [
        "attr_list", "admonition", "def_list",
        {"toc": {"permalink": True}},
        {"pymdownx.highlight": {"guess_lang": True}},
        {"pymdownx.superfences": {"css_class": "codehilite"}},
        {"pymdownx.inlinehilite": {"css_class": "codehilite"}},
        "pymdownx.tilde", "pymdownx.betterem", "pymdownx.mark"
    ],
    "plugins": [
        {"search": {"lang": "en"}},
        {"categories": {
            "generate_index": True,
            "verbose": True,
            "base_name": "categories",
            "section_title": "Categories",
            "no_nav": False,
            "category_separator": "|"
        }}
    ]
}

# === Original CiviCRM navigation order === #
ORDER = [
    "introduction",
    "organising-your-data",
    "contacts",
    "mailings",
    "contributions",
    "membership",
    "events",
    "searching",
    "reports",
    "customizing",
    "system-administration",
    "troubleshooting",
]

# === STEP 1 - merge source folders === #
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


# === STEP 2 - clean YAML and stray comments === #
def clean_markdown_files(folder):
    print("🧽 Cleaning Markdown files & YAML front matter …")
    for root, _, files in os.walk(folder):
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            content = open(path, encoding="utf-8").read()

            # keep only first YAML block & content after it
            content = re.sub(r'^[\s\S]*?(?=---\s*\n)', '', content, count=1)

            # ensure categories are in list
            content = re.sub(r'(?m)^categories:\s*"?([\w\s\-|]+)"?$', r'categories:\n  - \1', content)

            # ensure there is a valid categories block
            if "categories:" not in content:
                content = re.sub(r'^(---\s*\n)', r'\1categories:\n  - Uncategorized\n', content)

            # strip HTML comments below last delimiter
            lines = content.splitlines()
            last_hr = None
            for i, l in enumerate(lines):
                if l.strip() == "---":
                    last_hr = i
            if last_hr is not None:
                retained = lines[:last_hr + 1]
                for l in lines[last_hr + 1:]:
                    if not l.strip().startswith("<!--"):
                        retained.append(l)
                content = "\n".join(retained).strip() + "\n"

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
    print("✅ YAML cleaned and safe for mkdocs-categories")


# === STEP 3 - build navigation === #
def sort_key(path):
    """Sort by CiviCRM section priority."""
    path = path.lower()
    for i, seg in enumerate(ORDER):
        if f"/{seg}/" in f"/{path}/" or path.endswith(seg):
            return i
    return len(ORDER)

def build_nav(folder):
    sections = {}
    for root, _, files in os.walk(folder):
        md_files = sorted([f for f in files if f.endswith(".md")])
        if not md_files:
            continue
        section = os.path.relpath(root, folder)
        sections[section] = []
        for f in md_files:
            rel_path = os.path.relpath(os.path.join(root, f), folder)
            title = os.path.splitext(f)[0].replace("-", " ").replace("_", " ").title()
            sections[section].append({title: rel_path.replace("\\", "/")})

    # follow official doc order
    sorted_sections = sorted(sections.items(), key=lambda kv: sort_key(kv[0]))

    nav = []
    for section, items in sorted_sections:
        if section == ".":
            nav.extend(items)
        else:
            nav.append({section.replace("-", " ").title(): items})
    return nav


# === PIPELINE === #
if __name__ == "__main__":
    merge_to_docs(SOURCE_DIRS, TARGET_DIR)
    clean_markdown_files(TARGET_DIR)

    mkdocs_config["nav"] = build_nav(TARGET_DIR)
    with open(MKDOCS_YML, "w", encoding="utf-8") as f:
        yaml.dump(mkdocs_config, f, sort_keys=False, allow_unicode=True, width=160)

    print("🎉 mkdocs.yml generated successfully.")
    print("📚 Navigation follows the original structure of docs.civicrm.org/user/en/")

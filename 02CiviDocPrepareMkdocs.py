# 02CiviDocPrepareMkdocs.py
# 
# Preparation script for MkDocs documentation site for CiviCRM user docs
#
# What it does:
# - Merge ai_generated_docs/ and split_docs/ into docs/
# - Prepare mkdocs.yml with proper navigation
# - clean YAML front matter
# - delete comments at end of files
# - Generate mkdocs.yml including 'categories' plugin configuration - to be verified
# 
# Requires PyYAML: pip install pyyaml
#
# @alain.benbassat, @davem, @usha.makoa
# CiviCamp 2025 - Lunteren, Netherlands

 
import os
import re
import shutil
import yaml

SOURCE_DIRS = ["ai_generated_docs", "split_docs"]
TARGET_DIR = "docs"
MKDOCS_YML = "mkdocs.yml"

# ===== CONFIGURATION MkDocs ===== #
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
        "attr_list",
        "admonition",
        "def_list",
        {"toc": {"permalink": True}},
        {"pymdownx.highlight": {"guess_lang": True}},
        {"pymdownx.superfences": {"css_class": "codehilite"}},
        {"pymdownx.inlinehilite": {"css_class": "codehilite"}},
        "pymdownx.tilde",
        "pymdownx.betterem",
        "pymdownx.mark"
    ],
    "plugins": [
        {"search": {"lang": "en"}},
        {
            "categories": {           # Option 3 : configuration complète
                "generate_index": True,
                "verbose": True,
                "base_name": "categories",
                "section_title": "Categories",
                "no_nav": False,
                "category_separator": "|"
            }
        }
    ]
}

# ===== Étape 1 : fusion vers /docs ===== #
def merge_to_docs(sources, target):
    if os.path.exists(target):
        print(f"🧹 Nettoyage de {target}/ existant…")
        shutil.rmtree(target)
    os.makedirs(target, exist_ok=True)

    for src in sources:
        if not os.path.exists(src):
            continue
        print(f"📁 Copie depuis {src}/ …")
        for root, dirs, files in os.walk(src):
            for file in files:
                if not file.endswith(".md"):
                    continue
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, src)
                dest_path = os.path.join(target, rel_path)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy2(src_path, dest_path)
    print(f"✅ Markdown copié dans {target}/")

# ===== Étape 2 : nettoyage et réparation YAML ===== #
def clean_markdown_files(folder):
    print("🧽 Nettoyage et correction YAML front matter…")
    for root, _, files in os.walk(folder):
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()

            # Conserver texte entre 1er et 2e '---'
            if "---" in content:
                parts = content.split("---")
                if len(parts) >= 3:
                    cleaned = "---" + parts[1] + "---" + parts[2]
                else:
                    cleaned = content
            else:
                cleaned = content

            # Corriger categories: si c’est une chaîne → YAML liste
            cleaned = re.sub(
                r'(?m)^categories:\s*"?([\w\s\-|]+)"?$',
                r'categories:\n  - \1',
                cleaned
            )

            # Supprimer les commentaires après la dernière ligne ---
            lines = cleaned.splitlines()
            last_hr = None
            for i, l in enumerate(lines):
                if l.strip() == "---":
                    last_hr = i
            if last_hr is not None:
                retained = lines[:last_hr + 1]
                for l in lines[last_hr + 1:]:
                    if not l.strip().startswith("<!--"):
                        retained.append(l)
                cleaned = "\n".join(retained).strip() + "\n"

            with open(path, "w", encoding="utf-8") as file:
                file.write(cleaned)
    print("✅ Fichiers nettoyés et YAML corrigé")

# ===== Étape 3 : création navigation ===== #
def build_nav(folder):
    nav = []
    for root, dirs, files in os.walk(folder):
        dirs.sort()
        files = [f for f in files if f.endswith(".md")]
        files.sort()
        if not files:
            continue
        section = os.path.relpath(root, folder)
        items = []
        for f in files:
            rel_path = os.path.relpath(os.path.join(root, f), folder)
            title = os.path.splitext(f)[0].replace("-", " ").replace("_", " ").title()
            items.append({title: rel_path.replace("\\", "/")})
        if section != ".":
            nav.append({section.replace("-", " ").title(): items})
        else:
            nav.extend(items)
    return nav

# ===== PIPELINE COMPLET ===== #
merge_to_docs(SOURCE_DIRS, TARGET_DIR)
clean_markdown_files(TARGET_DIR)
mkdocs_config["nav"] = build_nav(TARGET_DIR)

with open(MKDOCS_YML, "w", encoding="utf-8") as f:
    yaml.dump(mkdocs_config, f, sort_keys=False, allow_unicode=True, width=160)

print(f"🎉 mkdocs.yml généré + correction YAML pour compatibilité plugin 'categories'")

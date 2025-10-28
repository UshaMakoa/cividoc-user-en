# 02CiviDocPrepareMkdocs.py
#
# Prepare MkDocs site for CiviCRM User documentation
# --------------------------------------------------
# ✓ Merge sonarprogenerated-docs/ into docs/
# ✓ Clean YAML front matter & comments
# ✓ Normalize lists and Markdown spacing
# ✓ Generate mkdocs.yml respecting official CiviCRM nav order
# ✓ Include categories-plugin configuration
#
# Usage: python 02CiviDocPrepareMkdocs.py
# Requires: pip install pyyaml
#
# @alain.benbassat, @davem, @usha.makoa, CiviCamp 2025


import os, re, shutil, yaml
from pathlib import Path


SOURCE_DIRS = ["sonarprogenerated-docs"]
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
    "theme": {"name": "material", "icon": {"repo": "fontawesome/brands/gitlab"}},
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
            "generate_index": True, "verbose": True,
            "base_name": "categories",
            "section_title": "Categories",
            "no_nav": False, "category_separator": "|"
        }}
    ]
}

# === Official nav order (docs.civicrm.org/user/en) === #
ORDER = [
    "introduction", "organising-your-data", "contacts", "mailings",
    "contributions", "membership", "events", "searching",
    "reports", "customizing", "system-administration",
    "troubleshooting", "appendix"
]


# --- STEP 1: Merge all Markdown into /docs ---
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


# --- STEP 2: Normalize lists, comments, and YAML ---
def normalize_lists_and_comments(md_content):
    """Convert flat lists to Markdown, fix comment syntax and remove orphans."""
    # Convert "# comment:" ➜ "<!-- ... -->"
    md_content = re.sub(r"(?m)^#\s*comment:\s*(.*)$", r"<!-- \1 -->", md_content)
    # Remove orphan "<!-- -->" artifacts
    md_content = re.sub(r'<\!--\s*-->', '', md_content)
    md_content = re.sub(r'(-->\s*<\!--)', '', md_content)

    # Fix inline numbered lists (e.g. 1. ... 2. ...)
    md_content = re.sub(
        r"(\d+\.)\s+([A-Z0-9].*?)(?=\s+\d+\.|$)",
        lambda m: f"\n{m.group(1)} {m.group(2).strip()}\n",
        md_content, flags=re.S)

    # Fix inline unordered lists (- item - item)
    md_content = re.sub(
        r"(-)\s+([A-Z0-9].*?)(?=\s+-|$)",
        lambda m: f"\n{m.group(1)} {m.group(2).strip()}\n",
        md_content, flags=re.S)

    # Remove leftover [¶](URL) markers
    md_content = re.sub(r"\[¶\]\([^)]+\)", "", md_content)

    # Normalize whitespace
    md_content = re.sub(r"\n{3,}", "\n\n", md_content)
    md_content = re.sub(r"[ \t]+$", "", md_content, flags=re.M)
    return md_content.strip() + "\n"


def clean_markdown_files(folder):
    print("🧽 Cleaning Markdown YAML & formatting lists/comments …")
    for root, _, files in os.walk(folder):
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            content = Path(path).read_text(encoding="utf-8")

            # Keep content from first frontmatter onward
            content = re.sub(r'^[\s\S]*?(?=---\s*\n)', '', content, count=1)
            content = normalize_lists_and_comments(content)

            # Convert categories to YAML list
            content = re.sub(r'(?m)^categories:\s*"?([\w\s\-|]+)"?$', r'categories:\n  - \1', content)
            if "categories:" not in content:
                content = re.sub(r'^(---\s*\n)', r'\1categories:\n  - Uncategorized\n', content)

            # Remove HTML comments beyond YAML block
            lines = content.splitlines()
            last_hr = None
            for i, l in enumerate(lines):
                if l.strip() == "---":
                    last_hr = i
            if last_hr is not None:
                retained = lines[:last_hr + 1]
                for l in lines[last_hr + 1:]:
                    if not re.match(r"^\s*<\!--", l):
                        retained.append(l)
                content = "\n".join(retained).strip() + "\n"

            Path(path).write_text(content, encoding="utf-8")
    print("✅ Markdown normalized successfully for mkdocs.")


# --- STEP 3: Build navigation in official order ---
def sort_key(path):
    path = path.lower()
    for i, seg in enumerate(ORDER):
        if f"/{seg}/" in f"/{path}/" or path.endswith(seg):
            return i
    return len(ORDER)


def build_nav(folder):
    """Recreate original navigation order with correct case."""
    sections = {}
    for root, _, files in os.walk(folder):
        md_files = sorted([f for f in files if f.endswith(".md")])
        if not md_files:
            continue
        section = os.path.relpath(root, folder)
        items = []
        for f in md_files:
            rel_path = os.path.relpath(os.path.join(root, f), folder)
            file_title = os.path.splitext(f)[0]
            file_title = file_title[:1].upper() + file_title[1:]
            items.append({file_title: rel_path.replace("\\", "/")})
        sections[section] = items

    sorted_sections = sorted(sections.items(), key=lambda kv: sort_key(kv[0]))

    nav = []
    for section, items in sorted_sections:
        if section == ".":
            nav.extend(items)
        else:
            display = section.replace("-", " ").capitalize()
            nav.append({display: items})
    return nav


# --- PIPELINE ---
if __name__ == "__main__":
    merge_to_docs(SOURCE_DIRS, TARGET_DIR)
    clean_markdown_files(TARGET_DIR)
    mkdocs_config["nav"] = build_nav(TARGET_DIR)
    with open(MKDOCS_YML, "w", encoding="utf-8") as f:
        yaml.dump(mkdocs_config, f, sort_keys=False, allow_unicode=True, width=160)
    print("🎉 mkdocs.yml generated with official navigation order from docs.civicrm.org/user/en")

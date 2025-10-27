# importcsv-frontmatter-ai.py
# 
# Import CSV data to update YAML front matter in Markdown files
#
# What it does:
# - Reads a CSV file with columns "URL" and "yaml front matter"
# - For each row, finds the corresponding Markdown file under 'docs/' based on "URL"
# - Replaces the YAML front matter in that Markdown file with the provided "yaml front matter"
# - If the file does not exist, logs a message indicating the missing file
# Prerequisites:
# - CSV file must be UTF-8 encoded
# - Markdown files are located under the 'docs/' directory
#
# @alain.benbassat, @usha.makoa
# CiviCamp 2025 - Lunteren, Netherlands

 

import csv
import os

BASE_PATH = r'docs'  # dossier racine des md
CSV_FILE = '20251021 CiviCRM - Doc - User Guide - EN - Tags Diataxis - Developer Guide.csv'

def sanitize_filename(path):
    # Nettoie le path fourni (sans slash de début, ni slash final inutiles)
    path = path.strip().lstrip('/').rstrip('/')
    if not path.endswith('.md'):
        path += '.md'
    return path

def find_md(base, relpath):
    # Compose le chemin absolu attendu, puis vérifie son existence
    abs_path = os.path.join(base, relpath)
    if os.path.exists(abs_path):
        return abs_path
    return None

with open(CSV_FILE, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rel_filename = sanitize_filename(row['URL'])
        yaml_block = row['yaml front matter'].strip()
        file_path = find_md(BASE_PATH, rel_filename)
        if file_path:
            with open(file_path, encoding='utf-8') as f:
                content = f.read()
            # Supprimer l'ancien front matter s'il existe
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) == 3:
                    content = parts[2].lstrip()
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"{yaml_block}\n\n{content}")
            print(f"Front matter updated in: {file_path}")
        else:
            print(f"File missing: {rel_filename}")

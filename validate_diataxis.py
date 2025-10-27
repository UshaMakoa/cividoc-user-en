import os
import re
import yaml
import frontmatter

DOCS_DIR = "docs"
REPORT_TXT = "diataxis_report.txt"
REPORT_MD = "diataxis_audit.md"

CATEGORIES = {"tutorial", "guide", "reference", "explanation"}
LEVELS = {"basic", "intermediate", "advanced"}

def load_front_matter(path):
    """Robust front matter parser using python-frontmatter."""
    try:
        post = frontmatter.load(path)
        return dict(post.metadata) if post.metadata else {}
    except Exception as e:
        print(f"⚠️  YAML parsing error in {path}: {e}")
        return {}

def analyze_file(path):
    """Analyze a .md file, return (issues, score)."""
    meta = load_front_matter(path)
    issues = []

    # --- Diátaxis front matter checks
    for key in ["categories", "level", "summary", "section"]:
        if key not in meta or not meta[key]:
            issues.append(f"❌ Missing or empty field: '{key}'")

    cats = meta.get("categories", [])
    if isinstance(cats, str):
        cats = [cats]
    invalid = [c for c in cats if c.lower() not in CATEGORIES]
    if invalid:
        issues.append(f"⚠️ Invalid category: {invalid} (expected: {CATEGORIES})")

    level = str(meta.get("level", "")).lower()
    if level and level not in LEVELS:
        issues.append(f"⚠️ Invalid level '{level}' (expected: {LEVELS})")

    summary = str(meta.get("summary", ""))
    if len(summary.split()) < 5:
        issues.append("🔸 Summary is too short (<5 words).")

    # --- Content checks
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # --- Structure: H1/H2 required
    if not re.search(r"^# ", content, flags=re.MULTILINE):
        issues.append("⚠️ Missing H1 title.")
    elif not re.search(r"^## ", content, flags=re.MULTILINE):
        issues.append("🔸 No sections (## headers) detected.")

    # --- External links
    for link in re.findall(r"\[.*?\]\((https?://[^\)]+)\)", content):
        if not any(domain in link for domain in ["docs.civicrm.org", "civicrm.org"]):
            issues.append(f"🔗 External link found: {link}")

    # --- Text density/length
    words = len(re.findall(r"\w+", content))
    if words < 120:
        issues.append("🪶 Too short (<120 words): likely incomplete.")
    elif words > 3000:
        issues.append("📚 Very long document (>3000 words): consider a Diátaxis split.")

    # --- Contradictions between Diátaxis types
    if cats:
        cat = cats[0].lower()
        if cat in ["tutorial", "guide"] and "why" in content.lower():
            issues.append("⚠️ Found 'explanation' concepts inside tutorial/guide (should be separated).")
        if cat == "reference" and "how to" in content.lower():
            issues.append("🔸 Reference with 'how-to': should be split into guides.")

    # --- Readability / Deep quality: sentence length
    sentences = re.split(r"[.!?]", content)
    avg_len = sum(len(s.split()) for s in sentences if s.strip()) / max(len(sentences), 1)
    if avg_len > 25:
        issues.append("⚠️ Very long sentences – consider breaking them (deep quality).")
    elif avg_len < 7:
        issues.append("🔸 Sentences too short; rhythm could be improved (flow).")

    # --- "Flow breaking" patterns
    if re.search(r"In conclusion|Summary|To recap|Wrapping up", content, flags=re.IGNORECASE):
        issues.append("⚠️ Ending section (e.g. 'In conclusion') detected – not idiomatic Diátaxis.")

    # --- "Anticipation": Prerequisites in tutorials
    if "prerequisite" not in content.lower() and cats and cats[0].lower() == "tutorial":
        issues.append("🔸 Tutorial lacks a 'Prerequisites' section – anticipate user needs.")

    # --- Functional quality score
    fun_quality = 100
    fun_quality -= sum([
        any(x in line for x in ["❌", "⚠️"]) for line in issues
    ]) * 5
    fun_quality = max(fun_quality, 0)

    # --- Deep quality score (proxy)
    deep_quality = 100
    for hint in ["flow", "anticipate", "clear", "simple", "friendly"]:
        if hint not in content.lower():
            deep_quality -= 4
    deep_quality = max(deep_quality, 0)

    # --- Global score (weighted mix)
    global_score = int((fun_quality * 0.7) + (deep_quality * 0.3))
    return issues, global_score

def main():
    report_lines = []
    total, clean = 0, 0
    total_score = 0

    for root, _, files in os.walk(DOCS_DIR):
        for f in files:
            if not f.endswith(".md"):
                continue
            path = os.path.join(root, f)
            rel_path = os.path.relpath(path, DOCS_DIR)
            total += 1
            issues, score = analyze_file(path)
            total_score += score

            if issues:
                report_lines.append(f"\n🔍 {rel_path}  (score {score}/100)")
                for issue in issues:
                    report_lines.append("   " + issue)
            else:
                clean += 1
                report_lines.append(f"✅ {rel_path}  (score {score}/100)")

    avg_score = int(total_score / total) if total else 0

    # Plaintext report
    with open(REPORT_TXT, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
        f.write(f"\n\n📊 Summary: {clean}/{total} fully compliant, average score {avg_score}/100.\n")

    # Markdown audit report
    with open(REPORT_MD, "w", encoding="utf-8") as md:
        md.write("# 🧾 Diátaxis Validation Report\n\n")
        md.write("| File | Score | Status | Details |\n|---------|--------|---------|----------|\n")
        for line in report_lines:
            if line.startswith("✅") or line.startswith("🔍"):
                path_part = line.split()[1]
                score_part = re.findall(r"\d+\/100", line)
                score_val = score_part[0] if score_part else "–"
                status = "✅" if line.startswith("✅") else "❌"
                md.write(f"| {path_part} | {score_val} | {status} | |\n")
        md.write(f"\n\n**Average score**: {avg_score}/100\n")

    print(f"✅ Diátaxis validation finished → {REPORT_TXT} and {REPORT_MD}")
    print(f"📊 Global average: {avg_score}/100")

if __name__ == "__main__":
    main()

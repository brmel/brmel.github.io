#!/usr/bin/env python3
"""A page nobody can navigate to may as well not be published.

PariData built, rendered and passed every other gate while its card was the only
way to reach it — so this asserts the reverse direction: every page in a listed
section is linked from that section's index, in the language it lives in.
"""
import glob, os, re, sys

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
PUB = os.path.join(ROOT, "public")
CONFIG = open(os.path.join(ROOT, "config.toml"), encoding="utf-8").read()

m = re.search(r"^\s*mainSections\s*=\s*\[([^\]]*)\]", CONFIG, re.M)
SECTIONS = re.findall(r'"([^"]+)"', m.group(1)) if m else []
LANGS = ("", "fr/", "ar/")

fails, checked = [], 0

def is_redirect(html):
    return "http-equiv=refresh" in html[:800]

for lang in LANGS:
    for section in SECTIONS:
        index_path = os.path.join(PUB, lang, section, "index.html")
        if not os.path.isfile(index_path):
            continue
        index_html = open(index_path, encoding="utf-8", errors="ignore").read()

        pattern = os.path.join(PUB, lang, section, "*", "index.html")
        for page in sorted(glob.glob(pattern)):
            html = open(page, encoding="utf-8", errors="ignore").read()
            if is_redirect(html):
                continue
            slug = os.path.basename(os.path.dirname(page))
            url = f"/{lang}{section}/{slug}/"
            checked += 1
            # section indexes link either relatively or by absolute permalink
            linked = re.search(
                r'href=["\']?(?:https?://[^/"\'\s>]+)?' + re.escape(url) + r'(?=["\'\s>])',
                index_html)
            if not linked:
                fails.append(f"/{lang}{section}/ does not link {url} — the page is published but unreachable from its index")

print(f"checked {checked} section page(s) against their index")
if fails:
    print(f"\n❌ {len(fails)} unreachable page(s):")
    for f in fails:
        print("  " + f)
    sys.exit(1)
print("✅ every published page is linked from the index of its section")

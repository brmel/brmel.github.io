#!/usr/bin/env python3
"""check-chrome.py — every content page ends the same way.

Each layout used to assemble its own ending, and they had drifted: an article
got tags + a mailto + share + section nav; a project got a different subset; the
standalone report and the resume got nothing at all — no breadcrumb, no way
back, no contribute. A reader learned one page's affordances and lost them on
the next.

partials/content-footer.html is now the single composition. This asserts every
content page actually renders it, so a new layout cannot quietly opt out.

A page may opt out deliberately with `hideContentFooter: true` in front matter;
list that page in OPT_OUT below so the exemption is visible rather than silent.
"""
import os, re, sys, glob

ROOT = os.path.join(os.path.dirname(__file__), "..")
PUB = os.path.join(ROOT, "public")

# Sections whose single pages are "content" — the ones a reader reads and may
# want to leave, improve or discuss.
CONTENT = ("tech/", "projects/", "thoughts/", "adventures/")
OPT_OUT = set()          # none today; add a path + a reason if that changes

REQUIRED = {
    "way back":  re.compile(r"section-nav__back|sa-nav__link|breadcrumbs"),
    "contribute": re.compile(r"content-actions"),
}

fails, checked = [], 0
for f in sorted(glob.glob(os.path.join(PUB, "**", "*.html"), recursive=True)):
    rel = os.path.relpath(f, PUB)
    url = "/" + rel.replace("index.html", "")
    if rel.startswith("reports" + os.sep):
        continue                                    # embedded artefact, not a page
    body = open(f, encoding="utf-8", errors="ignore").read()
    if "http-equiv=refresh" in body:
        continue                                    # alias redirect
    # a single page inside a content section, not the section index itself
    stripped = url.lstrip("/")
    if not stripped.startswith(CONTENT):
        continue
    depth = stripped.rstrip("/").count("/")
    lang_prefixed = stripped[:3] in ("fr/", "ar/")
    if depth < (2 if lang_prefixed else 1):
        continue                                    # section index
    if url in OPT_OUT:
        continue
    checked += 1
    for name, pat in REQUIRED.items():
        if not pat.search(body):
            fails.append(f"{url}: no {name}")

print(f"checked {checked} content pages")
if fails:
    print(f"\n❌ {len(fails)} page(s) missing shared chrome:")
    for x in fails:
        print("  " + x)
    sys.exit(1)
print("✅ every content page carries the same footer: a way back and a way to contribute")

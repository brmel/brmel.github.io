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

Three more rules apply to EVERY page, not just content pages, each of them a
defect the August 2026 screen audit found shipped:

  one h1        the report had none across 13,000px of scroll; one article had
                two because it repeated its title as a body heading
  skip link     no page had one, so keyboard users walked the nav every time
  image sizing  the resume's nine video thumbnails carried no width/height and
                the page reflowed as they loaded
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

# The lightbox placeholder has no dimensions until JS opens an image into it.
DIM_EXEMPT = re.compile(r'id="?lightbox-img"?')

IMG = re.compile(r"<img\b[^>]*>", re.I)

def img_without_dimensions(html):
    out = []
    for tag in IMG.findall(html):
        if DIM_EXEMPT.search(tag):
            continue
        if not re.search(r"\bwidth=", tag) or not re.search(r"\bheight=", tag):
            out.append(re.sub(r"\s+", " ", tag)[:90])
    return out

fails, checked, pages = [], 0, 0
for f in sorted(glob.glob(os.path.join(PUB, "**", "*.html"), recursive=True)):
    rel = os.path.relpath(f, PUB)
    url = "/" + rel.replace("index.html", "")
    if rel.startswith("reports" + os.sep):
        continue                                    # embedded artefact, not a page
    body = open(f, encoding="utf-8", errors="ignore").read()
    if "http-equiv=refresh" in body:
        continue                                    # alias redirect

    # ---- rules that apply to every page ----
    pages += 1
    n_h1 = len(re.findall(r"<h1[ >]", body))
    if n_h1 != 1:
        fails.append(f"{url}: {n_h1} h1 (want exactly 1)")
    if "skip-link" not in body:
        fails.append(f"{url}: no skip link")
    for tag in img_without_dimensions(body):
        fails.append(f"{url}: img without width/height — {tag}")

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

print(f"checked {pages} pages, {checked} of them content pages")
if fails:
    print(f"\n❌ {len(fails)} problem(s):")
    for x in fails:
        print("  " + x)
    sys.exit(1)
print("✅ one h1, a skip link and sized images on every page; "
      "every content page carries the same footer")

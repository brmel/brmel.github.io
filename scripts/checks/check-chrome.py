#!/usr/bin/env python3
import os, re, sys, glob

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
PUB = os.path.join(ROOT, "public")

CONTENT = ("tech/", "projects/", "thoughts/", "adventures/")

REQUIRED = {
    "way back":  re.compile(r"section-nav__link|breadcrumbs"),
    "contribute": re.compile(r"content-actions"),
}

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
        continue
    body = open(f, encoding="utf-8", errors="ignore").read()
    if "http-equiv=refresh" in body:
        continue

    pages += 1
    n_h1 = len(re.findall(r"<h1[ >]", body))
    if n_h1 != 1:
        fails.append(f"{url}: {n_h1} h1 (want exactly 1)")
    if "skip-link" not in body:
        fails.append(f"{url}: no skip link")
    for tag in img_without_dimensions(body):
        fails.append(f"{url}: img without width/height — {tag}")

    stripped = url.lstrip("/")
    if not stripped.startswith(CONTENT):
        continue
    depth = stripped.rstrip("/").count("/")
    lang_prefixed = stripped[:3] in ("fr/", "ar/")
    if depth < (2 if lang_prefixed else 1):
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

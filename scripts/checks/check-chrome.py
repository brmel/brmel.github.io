#!/usr/bin/env python3
import re
from gate import LANGS, SECTIONS, finish, pages, url_of

REQUIRED = {"way back": re.compile(r"section-nav__link|breadcrumbs"), "contribute": re.compile(r"content-actions")}
IMG = re.compile(r"<img\b[^>]*>", re.I)

fails, checked, total = [], 0, 0
for rel, html in pages():
    url = url_of(rel)
    total += 1
    h1 = len(re.findall(r"<h1[ >]", html))
    if h1 != 1:
        fails.append(f"{url}: {h1} h1 (want exactly 1)")
    if "skip-link" not in html:
        fails.append(f"{url}: no skip link")
    for tag in IMG.findall(html):
        if not re.search(r"\bwidth=", tag) or not re.search(r"\bheight=", tag):
            fails.append(f"{url}: img without width/height — {re.sub(r'\s+', ' ', tag)[:90]}")
    parts = [p for p in url.strip("/").split("/") if p]
    if parts and parts[0] in LANGS:
        parts = parts[1:]
    if len(parts) != 2 or parts[0] not in SECTIONS:
        continue
    checked += 1
    for name, pattern in REQUIRED.items():
        if not pattern.search(html):
            fails.append(f"{url}: no {name}")

print(f"checked {total} pages, {checked} of them content pages")
finish(fails, "one h1, a skip link and sized images on every page; every content page carries the same footer")

#!/usr/bin/env python3
import re
from gate import finish, pages, url_of

IMG = re.compile(r"<img\b[^>]*>", re.I)

fails, total = [], 0
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

print(f"checked {total} pages")
finish(fails, "one h1, a skip link and sized images on every page")

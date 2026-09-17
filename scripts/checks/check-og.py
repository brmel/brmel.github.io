#!/usr/bin/env python3
import os, re
from urllib.parse import urlparse
from gate import PUB, finish, pages

def meta(html, key):
    return re.search(rf'<meta property={key}[^>]*content="([^"]*)"', html) or re.search(
        rf'<meta property="{key}"[^>]*content="([^"]*)"', html)

fails, checked = [], 0
for rel, html in pages():
    checked += 1
    image = meta(html, "og:image")
    if not image:
        fails.append(f"{rel}: no og:image")
        continue
    url = image.group(1)
    if not url.startswith("http"):
        fails.append(f"{rel}: og:image is relative -> {url}")
    elif not os.path.exists(os.path.join(PUB, urlparse(url).path.lstrip("/"))):
        fails.append(f"{rel}: og:image does not resolve -> {url}")
    alt = meta(html, "og:image:alt")
    if not alt or not alt.group(1).strip():
        fails.append(f"{rel}: og:image:alt missing or empty")

print(f"checked {checked} pages")
finish(fails, "every page has a resolvable, absolute og:image with alt text")

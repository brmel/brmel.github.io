#!/usr/bin/env python3
import re
from gate import SECTIONS, clean_parts, finish, pages, url_of

built = {url_of(rel): html for rel, html in pages()}
fails, checked = [], 0
for url in built:
    parts = clean_parts(url)
    if len(parts) != 2 or parts[0] not in SECTIONS:
        continue
    index = url.rsplit("/", 2)[0] + "/"
    checked += 1
    if not re.search(r'href=["\']?(?:https?://[^/"\'\s>]+)?' + re.escape(url) + r'(?=["\'\s>])', built.get(index, "")):
        fails.append(f"{index} does not link {url} — the page is published but unreachable from its index")

print(f"checked {checked} section page(s) against their index")
finish(fails, "every published page is linked from the index of its section")

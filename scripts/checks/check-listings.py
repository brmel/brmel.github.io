#!/usr/bin/env python3
import glob, os, re
from gate import LANGS, PUB, SECTIONS, finish

fails, checked = [], 0
for lang in [""] + [f"{l}/" for l in LANGS]:
    for section in SECTIONS:
        index = os.path.join(PUB, lang, section, "index.html")
        if not os.path.isfile(index):
            continue
        index_html = open(index, encoding="utf-8", errors="ignore").read()
        for page in sorted(glob.glob(os.path.join(PUB, lang, section, "*", "index.html"))):
            if "http-equiv=refresh" in open(page, encoding="utf-8", errors="ignore").read(800):
                continue
            url = f"/{lang}{section}/{os.path.basename(os.path.dirname(page))}/"
            checked += 1
            if not re.search(r'href=["\']?(?:https?://[^/"\'\s>]+)?' + re.escape(url) + r'(?=["\'\s>])', index_html):
                fails.append(f"/{lang}{section}/ does not link {url} — the page is published but unreachable from its index")

print(f"checked {checked} section page(s) against their index")
finish(fails, "every published page is linked from the index of its section")

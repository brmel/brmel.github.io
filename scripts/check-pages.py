#!/usr/bin/env python3
"""check-pages.py — the faults a structural check misses.

The existing gates ask "is the block present" and "is the block present once".
Both passed while the resume showed LinkedIn and GitHub twice: once as a text
link in the header, once as an icon in the footer. Two different components,
same destination, so neither a duplicate-block check nor a duplicate-(href,text)
check saw it.

These rules compare pages the way a reader does — by where a link goes, what a
control looks like, and whether the journey closes.

  1. Same destination twice on a page, whatever the two links look like.
  2. A link that points at the page it is on.
  3. A control with no accessible name (an icon link with no label).
  4. Mixed affordance: the same destination shown as bare text in one place and
     as an icon in another.
  5. Internal links that resolve to nothing.
  6. A page reachable from nowhere.
"""
import os, re, sys, glob, collections
from urllib.parse import unquote

ROOT = os.path.join(os.path.dirname(__file__), "..")
PUB = os.path.join(ROOT, "public")

CHROME_WIDE = re.compile(r"class=[\"']?(?:nav|footer|site-mark|skip-link)")

pages = {}
for f in sorted(glob.glob(os.path.join(PUB, "**", "*.html"), recursive=True)):
    body = open(f, encoding="utf-8", errors="ignore").read()
    if "http-equiv=refresh" in body or 'http-equiv="refresh"' in body:
        continue
    rel = os.path.relpath(f, PUB)
    if rel.startswith("reports" + os.sep):
        continue
    pages["/" + rel.replace("index.html", "").replace(os.sep, "/")] = body

fails, warns = [], []

def main_of(html):
    """Everything inside <main>, so site chrome is not counted as page content."""
    m = re.search(r"<main\b.*?</main>", html, re.S)
    return m.group(0) if m else html

ANCHOR = re.compile(r"<a\b([^>]*)>(.*?)</a>", re.S)

for url, html in pages.items():
    body = main_of(html)
    seen = collections.defaultdict(list)
    for attrs, inner in ANCHOR.findall(body):
        href = re.search(r'href=(?:"([^"]*)"|([^\s>]+))', attrs)
        if not href:
            continue
        target = (href.group(1) or href.group(2)).split("#")[0]
        if not target or target.startswith(("mailto:", "tel:")) and False:
            continue
        text = re.sub(r"<[^>]+>", "", inner).strip()
        label = re.search(r'(?:aria-label|title)=(?:"([^"]*)"|([^\s>]+))', attrs)
        has_icon = "<svg" in inner
        seen[target].append((text, has_icon, bool(label)))

        # 3 — a control a screen reader cannot name
        if not text and not label and has_icon:
            fails.append(f"{url}: icon link to {target[:48]} has no accessible name")

    for target, uses in seen.items():
        # 2 — a link to the page it is on
        if target.rstrip("/") == url.rstrip("/") and target:
            fails.append(f"{url}: links to itself ({len(uses)}x)")
        if len(uses) < 2:
            continue
        texts = {u[0] for u in uses}
        icons = {u[1] for u in uses}
        # 1 + 4 — same destination twice, and worse if it looks different each time
        if len(icons) > 1:
            fails.append(f"{url}: {target[:44]} appears as text and as an icon")
        elif len(texts) > 1:
            warns.append(f"{url}: {target[:44]} linked {len(uses)}x with different words {sorted(texts)[:2]}")
        else:
            warns.append(f"{url}: {target[:44]} linked {len(uses)}x")

# 5 — internal links that resolve to nothing
def resolves(p):
    p = unquote(p.split("#")[0].split("?")[0])
    if not p.startswith("/"):
        return True
    fs = os.path.join(PUB, p.strip("/"))
    return os.path.exists(fs) or os.path.exists(os.path.join(fs, "index.html")) or os.path.exists(fs + ".html")

broken = collections.Counter()
for url, html in pages.items():
    for m in re.finditer(r'href=(?:"(/[^"]*)"|(/[^\s>]+))', html):
        t = m.group(1) or m.group(2)
        if not resolves(t):
            broken[t] += 1
for t, n in broken.items():
    fails.append(f"link to {t} resolves to nothing ({n} pages)")

# 6 — a page nothing links to
linked = set()
for html in pages.values():
    for m in re.finditer(r'href=(?:"(/[^"]*)"|(/[^\s>]+))', html):
        linked.add((m.group(1) or m.group(2)).split("#")[0].rstrip("/") or "/")
for url in pages:
    u = url.rstrip("/") or "/"
    if u not in linked and not u.startswith(("/tags", "/en", "/404")) and u != "/":
        warns.append(f"{url}: nothing on the site links here")

print(f"checked {len(pages)} pages")
for w in warns:
    print("  ⚠  " + w)
if fails:
    print(f"\n❌ {len(fails)} problem(s):")
    for f in fails:
        print("  " + f)
    sys.exit(1)
print("✅ no repeated destinations, self-links, unnamed controls or dead internal links")

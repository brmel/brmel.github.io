#!/usr/bin/env python3
import collections, os, re
from urllib.parse import unquote
from gate import BASE, PUB, finish, pages as built, url_of

SELF_HOST = re.compile(r"^https?://(?:www\.)?" + re.escape(BASE.split("//", 1)[-1]), re.I)
HREF = re.compile(r'href=(?:"([^"]*)"|([^\s>]+))')

def internal_targets(html):
    for m in HREF.finditer(html):
        t = SELF_HOST.sub("", m.group(1) or m.group(2), count=1) or "/"
        if t.startswith("/"):
            yield t

pages = {url_of(rel): html for rel, html in built()}

fails = []

def main_of(html):
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
        if not target:
            continue
        text = re.sub(r"<[^>]+>", "", inner).strip()
        label = re.search(r'(?:aria-label|title)=(?:"([^"]*)"|([^\s>]+))', attrs)
        has_icon = "<svg" in inner
        seen[target].append((text, has_icon, bool(label)))

        if not text and not label and has_icon:
            fails.append(f"{url}: icon link to {target[:48]} has no accessible name")

    for target, uses in seen.items():
        if target.rstrip("/") == url.rstrip("/") and target:
            fails.append(f"{url}: links to itself ({len(uses)}x)")
        if len(uses) < 2:
            continue
        texts = {u[0] for u in uses}
        icons = {u[1] for u in uses}
        if len(icons) > 1:
            fails.append(f"{url}: {target[:44]} appears as text and as an icon")

def resolves(p):
    p = unquote(p.split("#")[0].split("?")[0])
    if not p.startswith("/"):
        return True
    fs = os.path.join(PUB, p.strip("/"))
    return os.path.exists(fs) or os.path.exists(os.path.join(fs, "index.html")) or os.path.exists(fs + ".html")

broken = collections.Counter()
for url, html in pages.items():
    for t in internal_targets(html):
        if not resolves(t):
            broken[t] += 1
for t, n in broken.items():
    fails.append(f"link to {t} resolves to nothing ({n} pages)")

linked = set()
for html in pages.values():
    for t in internal_targets(html):
        linked.add(unquote(t.split("#")[0]).rstrip("/") or "/")
for url in pages:
    u = url.rstrip("/") or "/"
    if u not in linked and not u.startswith(("/en", "/404")) and u != "/":
        fails.append(f"{url}: nothing on the site links here")

print(f"checked {len(pages)} pages")
finish(fails, "no mixed text/icon duplicates, self-links, unnamed controls, dead internal links or unlinked pages")

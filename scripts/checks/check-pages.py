#!/usr/bin/env python3
import collections, os, re
from urllib.parse import unquote
from gate import BASE, PUB, finish, pages as built, url_of

SELF_HOST = re.compile(r"^https?://(?:www\.)?" + re.escape(BASE.split("//", 1)[-1]), re.I)
HREF = re.compile(r'href=(?:"([^"]*)"|([^\s>]+))')
ANCHOR = re.compile(r"<a\b([^>]*)>(.*?)</a>", re.S)

def internal_targets(html):
    for m in HREF.finditer(html):
        t = SELF_HOST.sub("", m.group(1) or m.group(2), count=1) or "/"
        if t.startswith("/"): yield t

def resolves(p):
    p = unquote(p.split("#")[0].split("?")[0])
    if not p.startswith("/"): return True
    fs = os.path.join(PUB, p.strip("/"))
    return os.path.exists(fs) or os.path.exists(os.path.join(fs, "index.html")) or os.path.exists(fs + ".html")

pages = {url_of(rel): html for rel, html in built()}
fails = []
broken = collections.Counter()
linked = set()

for url, html in pages.items():
    body = re.search(r"<main\b.*?</main>", html, re.S)
    body_text = body.group(0) if body else html
    seen = collections.defaultdict(list)

    for attrs, inner in ANCHOR.findall(body_text):
        href = HREF.search(attrs)
        if not href: continue
        target = (href.group(1) or href.group(2)).split("#")[0]
        if not target: continue
        text = re.sub(r"<[^>]+>", "", inner).strip()
        label = re.search(r'(?:aria-label|title)=(?:"([^"]*)"|([^\s>]+))', attrs)
        has_icon = "<svg" in inner
        seen[target].append((text, has_icon, bool(label)))
        if not text and not label and has_icon:
            fails.append(f"{url}: icon link to {target[:48]} has no accessible name")

    for target, uses in seen.items():
        if target.rstrip("/") == url.rstrip("/") and target:
            fails.append(f"{url}: links to itself ({len(uses)}x)")
        if len(uses) >= 2 and len({u[1] for u in uses}) > 1:
            fails.append(f"{url}: {target[:44]} appears as text and as an icon")

    for t in internal_targets(html):
        if not resolves(t): broken[t] += 1
        linked.add(unquote(t.split("#")[0]).rstrip("/") or "/")

for t, n in broken.items():
    fails.append(f"link to {t} resolves to nothing ({n} pages)")
for url in pages:
    u = url.rstrip("/") or "/"
    if u not in linked and not u.startswith(("/en", "/404")) and u != "/":
        fails.append(f"{url}: nothing on the site links here")

print(f"checked {len(pages)} pages")
finish(fails, "no mixed text/icon duplicates, self-links, unnamed controls, dead internal links or unlinked pages")


#!/usr/bin/env python3
import os, re, sys, glob, collections
from urllib.parse import unquote

ROOT = os.path.join(os.path.dirname(__file__), "..")
PUB = os.path.join(ROOT, "public")

CHROME_WIDE = re.compile(r"class=[\"']?(?:nav|footer|site-mark|skip-link)")

BASE_URL = re.search(
    r'^\s*baseURL\s*=\s*["\']([^"\']+)', open(os.path.join(ROOT, "config.toml"),
    encoding="utf-8").read(), re.M).group(1)
SELF_HOST = re.compile(
    r"^https?://(?:www\.)?" + re.escape(BASE_URL.split("//", 1)[-1].strip("/")), re.I)
HREF = re.compile(r'href=(?:"([^"]*)"|([^\s>]+))')

def internal_targets(html):
    """Every href that lands on this site, as a site-relative path.

    Hugo emits absolute permalinks, so a pattern anchored on "/" sees none of
    them: broken absolute links went unchecked and pages linked only that way
    looked orphaned.
    """
    for m in HREF.finditer(html):
        t = SELF_HOST.sub("", m.group(1) or m.group(2), count=1) or "/"
        if t.startswith("/"):
            yield t

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
        elif len(texts) > 1:
            warns.append(f"{url}: {target[:44]} linked {len(uses)}x with different words {sorted(texts)[:2]}")
        else:
            warns.append(f"{url}: {target[:44]} linked {len(uses)}x")

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

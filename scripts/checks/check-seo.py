#!/usr/bin/env python3
import collections, glob, html, json, os, re
from urllib.parse import unquote
from gate import BASE, LANGS, PUB, finish

TYPES = {"tech": "TechArticle", "thoughts": "BlogPosting", "adventures": "BlogPosting",
         "projects": "SoftwareSourceCode"}

fails, indexable = [], set()
titles, descriptions = collections.defaultdict(list), collections.defaultdict(list)

for f in sorted(glob.glob(os.path.join(PUB, "**", "index.html"), recursive=True)):
    h = open(f, encoding="utf-8", errors="ignore").read()
    if "http-equiv=refresh" in h[:800] or re.search(r'name=robots content=["\']?noindex', h):
        continue
    rel = os.path.relpath(os.path.dirname(f), PUB).replace(os.sep, "/")
    url = "/" if rel == "." else f"/{rel}/"
    indexable.add(BASE + url)
    lang = re.search(r"<html lang=([\w-]+)", h).group(1)
    title = html.unescape(re.search(r"<title>(.*?)</title>", h, re.S).group(1))
    m = re.search(r'<meta name=description content=(?:"([^"]*)"|\'([^\']*)\')', h)
    desc = html.unescape((m.group(1) or m.group(2)) if m else "")
    titles[(lang, title)].append(url)
    descriptions[(lang, desc)].append(url)
    if not 50 <= len(desc) <= 160:
        fails.append(f"{url}: description is {len(desc)} characters (want 50–160)")
    if "rel=canonical" not in h:
        fails.append(f"{url}: no canonical link")
    if "hreflang=x-default" not in h:
        fails.append(f"{url}: no hreflang x-default")
    parts = [p for p in url.strip("/").split("/") if p]
    if parts and parts[0] in LANGS:
        parts = parts[1:]
    if len(parts) == 2 and parts[0] in TYPES:
        types = {n.get("@type") for ld in re.findall(r"<script type=application/ld\+json>(.*?)</script>", h, re.S)
                 for n in json.loads(ld).get("@graph", [])}
        if TYPES[parts[0]] not in types:
            fails.append(f"{url}: JSON-LD has {sorted(t for t in types if t)}, want {TYPES[parts[0]]}")

for (lang, text), urls in list(titles.items()) + list(descriptions.items()):
    if len(urls) > 1:
        fails.append(f"{lang}: {len(urls)} pages share \"{text[:50]}\": {', '.join(urls)}")

listed = {unquote(loc) for f in glob.glob(os.path.join(PUB, "**", "sitemap.xml"), recursive=True)
          for loc in re.findall(r"<loc>([^<]+)</loc>", open(f, encoding="utf-8").read())
          if not loc.endswith("sitemap.xml")}
fails += [f"sitemap is missing {u}" for u in sorted(indexable - listed)]
fails += [f"sitemap lists {u}, which is not an indexable page" for u in sorted(listed - indexable)]

print(f"checked {len(indexable)} indexable pages and {len(listed)} sitemap URLs")
finish(fails, "descriptions sized and unique, canonical and x-default everywhere, JSON-LD per section, sitemap exact")

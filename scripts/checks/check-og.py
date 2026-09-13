#!/usr/bin/env python3
import os, re, sys
from urllib.parse import urlparse

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
PUB = os.path.join(ROOT, "public")
BASE = re.search(
    r'^\s*baseURL\s*=\s*["\']([^"\']+)',
    open(os.path.join(ROOT, "config.toml"), encoding="utf-8").read(),
    re.M).group(1).rstrip("/")

meta = lambda h, k, a="property": re.search(
    rf'<meta {a}={k}[^>]*content="([^"]*)"', h) or re.search(
    rf'<meta {a}="{k}"[^>]*content="([^"]*)"', h)

fails, checked = [], 0
for root, _, files in os.walk(PUB):
    for f in files:
        if not f.endswith(".html"):
            continue
        p = os.path.join(root, f)
        h = open(p, encoding="utf-8", errors="ignore").read()
        if "http-equiv=refresh" in h or 'http-equiv="refresh"' in h:
            continue
        if os.path.relpath(p, PUB).startswith("reports" + os.sep):
            continue
        rel = os.path.relpath(p, PUB)
        checked += 1

        m = meta(h, "og:image")
        if not m:
            fails.append(f"{rel}: no og:image"); continue
        url = m.group(1)
        if not url.startswith("http"):
            fails.append(f"{rel}: og:image is relative -> {url}"); continue
        local = os.path.join(PUB, urlparse(url).path.lstrip("/"))
        if not os.path.exists(local):
            fails.append(f"{rel}: og:image does not resolve -> {url}")

        alt = meta(h, "og:image:alt")
        if not alt or not alt.group(1).strip():
            fails.append(f"{rel}: og:image:alt missing or empty")

print(f"checked {checked} pages")
if fails:
    print(f"\n❌ {len(fails)} problem(s):")
    for x in fails[:40]:
        print("  ", x)
    sys.exit(1)
print("✅ every page has a resolvable, absolute og:image with alt text")

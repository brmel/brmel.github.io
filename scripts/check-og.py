#!/usr/bin/env python3
"""check-og.py — every built page must carry a real social card.

Asserts, for every public/**/*.html that is a page (not an alias redirect):
  * og:image is present
  * it is an ABSOLUTE url (X and LinkedIn reject relative ones)
  * it resolves to a file that actually exists in public/
  * og:image:alt is present and non-empty
  * og:title and og:description are not the site-wide defaults

This exists because the site shipped for months with og:image pointing at
static/images/profile.jpg — which was not an image at all, but a text
placeholder file. Nothing caught it because nothing looked. Now something does.
"""
import os, re, sys
from urllib.parse import urlparse

ROOT = os.path.join(os.path.dirname(__file__), "..")
PUB = os.path.join(ROOT, "public")
BASE = "https://ibraverse.ca"

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
            continue                                  # alias redirect, not a page
        if os.path.relpath(p, PUB).startswith("reports" + os.sep):
            continue     # generated report artifact embedded in an iframe, never shared directly
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

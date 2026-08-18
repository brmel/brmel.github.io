#!/usr/bin/env python3
"""check-js.py — every selector a script reaches for exists in the page.

The scripts here are small and defensive: they return early when an element is
missing. That is the right behaviour and it is also why a renamed class fails
silently — the feature simply stops, with no console error and no build error.
The timeline lightbox and the comments loader both hang off exactly this.

Rule: for each script, the pages that load it must contain every id and class
it queries.
"""
import re, sys, glob, os, collections

ROOT = os.path.join(os.path.dirname(__file__), "..")
PUB = os.path.join(ROOT, "public")

SEL = re.compile(r"""(?:getElementById\(['"]([\w-]+)['"]\)|querySelector(?:All)?\(['"]([^'"]+)['"]\))""")

pages = {}
for f in glob.glob(os.path.join(PUB, "**", "*.html"), recursive=True):
    pages[f] = open(f, encoding="utf-8", errors="ignore").read()

fails = []
for js in sorted(glob.glob(os.path.join(ROOT, "assets/js/*.js"))):
    name = os.path.basename(js)
    stem = name.replace(".js", "")
    src = open(js, encoding="utf-8").read()
    users = [h for h in pages.values() if re.search(stem + r"\.[0-9a-f]{8,}\.js", h)]
    if not users:
        continue
    wanted = set()
    for gid, qs in SEL.findall(src):
        if gid:
            wanted.add(("id", gid))
        for token in re.findall(r"\.([a-zA-Z][\w-]*)", qs or ""):
            wanted.add(("class", token))
        for token in re.findall(r"#([a-zA-Z][\w-]*)", qs or ""):
            wanted.add(("id", token))
    for kind, val in sorted(wanted):
        needle = f'id="{val}"' if kind == "id" else val
        alt = f"id={val}" if kind == "id" else val
        if not any(needle in h or alt in h for h in users):
            fails.append(f"{name}: {kind} '{val}' is queried but appears on none of the {len(users)} pages that load it")

print(f"checked {len(glob.glob(os.path.join(ROOT, 'assets/js/*.js')))} scripts against the pages that load them")
if fails:
    print(f"\n❌ {len(fails)} dangling selector(s):")
    for f in fails:
        print("  " + f)
    sys.exit(1)
print("✅ every selector a script reaches for exists where it runs")

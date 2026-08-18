#!/usr/bin/env python3
"""check-rtl.py — the layout mirrors without per-direction overrides.

Arabic is a first-class language here, not a translation bolted on. A physical
property (margin-left, border-right, left:) pins a thing to one side of the
screen and stays pinned when the page flips, so an accent bar meant for the
leading edge ends up on the trailing one.

Logical properties do the mirroring for free. This fails the build on a
physical one outside an explicit [dir=] override, where the physical value is
the whole point.
"""
import re, sys, glob, os

ROOT = os.path.join(os.path.dirname(__file__), "..")
PHYS = re.compile(r'(?<![-\w])(margin-left|margin-right|padding-left|padding-right|'
                  r'border-left|border-right|text-align\s*:\s*(?:left|right)|(?<![\w-])left|(?<![\w-])right)\s*:')

fails = []
for f in sorted(glob.glob(os.path.join(ROOT, "assets/css/**/*.css"), recursive=True)):
    src = re.sub(r"/\*.*?\*/", "", open(f, encoding="utf-8").read(), flags=re.S)
    for i, line in enumerate(src.split("\n"), 1):
        if "[dir=" in line:
            continue
        m = PHYS.search(line)
        if m:
            fails.append(f"{os.path.basename(f)}:{i}: {m.group(1)} — use the logical property")

print(f"checked {len(glob.glob(os.path.join(ROOT, 'assets/css/**/*.css'), recursive=True))} stylesheets for direction-safety")
if fails:
    print(f"\n❌ {len(fails)} physical propert(ies):")
    for f in fails:
        print("  " + f)
    sys.exit(1)
print("✅ layout mirrors from logical properties alone")

#!/usr/bin/env python3
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

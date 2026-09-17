#!/usr/bin/env python3
import glob, os, re
from gate import ROOT, finish

PHYS = re.compile(r'(?<![-\w])(margin-left|margin-right|padding-left|padding-right|'
                  r'border-left|border-right|text-align\s*:\s*(?:left|right)|(?<![\w-])left|(?<![\w-])right)\s*:')

sheets = sorted(glob.glob(os.path.join(ROOT, "assets/css/**/*.css"), recursive=True))
fails = []
for f in sheets:
    src = re.sub(r"/\*.*?\*/", "", open(f, encoding="utf-8").read(), flags=re.S)
    for i, line in enumerate(src.split("\n"), 1):
        m = PHYS.search(line)
        if m and "[dir=" not in line:
            fails.append(f"{os.path.basename(f)}:{i}: {m.group(1)} — use the logical property")

print(f"checked {len(sheets)} stylesheets for direction-safety")
finish(fails, "layout mirrors from logical properties alone")

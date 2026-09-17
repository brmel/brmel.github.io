#!/usr/bin/env python3
import os, re, glob
from gate import PUB, ROOT, finish

EXT = os.path.join(ROOT, "assets", "css", "extended")
MAX_LINES = 260
TOKENS = "00-tokens.css"
COMPONENTS = "20-components.css"

PRIMITIVES = {
    "card surface": re.compile(r"background:var\(--bg-alt\);\s*\n?\s*border:var\(--hairline\) solid var\(--rule\)"),
    "hover lift": re.compile(r"transform:translateY\(-2px\)"),
}

fails = []
files = sorted(glob.glob(os.path.join(EXT, "*.css")))

for f in files:
    b = os.path.basename(f)
    if not re.match(r"^\d{2}-[a-z0-9-]+\.css$", b):
        fails.append(f"{b}: must be NN-name.css so the cascade order is explicit")

for f in files:
    b = os.path.basename(f)
    if b == TOKENS:
        continue
    src = open(f).read()
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    for m in re.findall(r"#[0-9a-fA-F]{3,8}\b", src):
        fails.append(f"{b}: colour {m} defined outside {TOKENS}")

for f in files:
    n = sum(1 for _ in open(f))
    if n > MAX_LINES:
        fails.append(f"{os.path.basename(f)}: {n} lines (max {MAX_LINES}) — split it by concern")

for f in files:
    b = os.path.basename(f)
    if b in (TOKENS, COMPONENTS):
        continue
    src = open(f).read()
    for name, pat in PRIMITIVES.items():
        if pat.search(src):
            fails.append(f"{b}: redeclares the '{name}' primitive — compose {COMPONENTS} instead")

markup = "".join(open(f, encoding="utf-8", errors="ignore").read()
                 for pattern in ("**/*.html", "**/*.js") for f in glob.glob(os.path.join(PUB, pattern), recursive=True))
markup += "".join(open(f, encoding="utf-8", errors="ignore").read()
                  for pattern in ("assets/js/*.js", "layouts/**/*.html", "themes/PaperMod/assets/css/includes/chroma-styles.css")
                  for f in glob.glob(os.path.join(ROOT, pattern), recursive=True))

declared = set()
for f in files:
    src = re.sub(r"/\*.*?\*/", "", open(f).read(), flags=re.S)
    declared |= set(re.findall(r"\.([a-z][a-z0-9_-]*(?:__[a-z0-9-]+)?(?:--[a-z0-9-]+)?)", src))

for c in sorted(c for c in declared if c not in markup):
    fails.append(f"class .{c} is declared in CSS but appears on no published page or script")

print(f"checked {len(files)} stylesheets, {len(declared)} classes")
finish(fails, "cascade explicit · colours in tokens only · no oversized files · no duplicated primitives · no dead classes")

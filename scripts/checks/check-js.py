#!/usr/bin/env python3
import re, sys, glob, os, collections

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
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
    users = [h for h in pages.values() if re.search(re.escape(stem) + r"(?:\.min)?\.[0-9a-f]{8,}\.js", h)]
    if not users:
        fails.append(f"{name}: no page loads it")
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
        if kind == "id":
            pat = re.compile(r'\bid=["\']?' + re.escape(val) + r'(?=["\'\s>])')
        else:
            pat = re.compile(r'\bclass=["\']?[^"\'>]*(?<![\w-])' + re.escape(val) + r'(?![\w-])')
        if not any(pat.search(h) for h in users):
            fails.append(f"{name}: {kind} '{val}' is queried but appears on none of the {len(users)} pages that load it")

print(f"checked {len(glob.glob(os.path.join(ROOT, 'assets/js/*.js')))} scripts against the pages that load them")
if fails:
    print(f"\n❌ {len(fails)} dangling selector(s):")
    for f in fails:
        print("  " + f)
    sys.exit(1)
print("✅ every selector a script reaches for exists where it runs")

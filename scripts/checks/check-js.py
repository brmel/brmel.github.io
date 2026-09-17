#!/usr/bin/env python3
import glob, os, re
from gate import ROOT, finish, pages

SEL = re.compile(r"""(?:getElementById\(['"]([\w-]+)['"]\)|querySelector(?:All)?\(['"]([^'"]+)['"]\))""")
built = [html for _, html in pages()]
scripts = sorted(glob.glob(os.path.join(ROOT, "assets/js/*.js")))

fails = []
for js in scripts:
    name = os.path.basename(js)
    users = [h for h in built if re.search(re.escape(name[:-3]) + r"(?:\.min)?\.[0-9a-f]{8,}\.js", h)]
    if not users:
        fails.append(f"{name}: no page loads it")
        continue
    wanted = set()
    for gid, query in SEL.findall(open(js, encoding="utf-8").read()):
        if gid:
            wanted.add(("id", gid))
        wanted |= {("class", t) for t in re.findall(r"\.([a-zA-Z][\w-]*)", query)}
        wanted |= {("id", t) for t in re.findall(r"#([a-zA-Z][\w-]*)", query)}
    for kind, value in sorted(wanted):
        if kind == "id":
            pattern = re.compile(r'\bid=["\']?' + re.escape(value) + r'(?=["\'\s>])')
        else:
            pattern = re.compile(r'\bclass=["\']?[^"\'>]*(?<![\w-])' + re.escape(value) + r'(?![\w-])')
        if not any(pattern.search(h) for h in users):
            fails.append(f"{name}: {kind} '{value}' is queried but appears on none of the {len(users)} pages that load it")

print(f"checked {len(scripts)} scripts against the pages that load them")
finish(fails, "every selector a script reaches for exists where it runs")

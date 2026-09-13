#!/usr/bin/env python3
import re, sys, glob, os

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
def r(p): return open(os.path.join(ROOT, p), encoding="utf-8").read()

sa_tpl = r("layouts/_default/standalone.html")
bundle = re.search(r"range \(slice ([^)]*)\)", sa_tpl).group(1)
sa_css = "".join(r("assets/" + f) for f in re.findall(r'"([^"]+)"', bundle)
                 if os.path.exists(os.path.join(ROOT, "assets", f)))
all_css = "".join(r(f) for f in sorted(glob.glob(os.path.join(ROOT, "assets/css/extended/*.css"))))

reachable = sa_tpl
for f in glob.glob(os.path.join(ROOT, "layouts/shortcodes/*.html")):
    reachable += r(os.path.relpath(f, ROOT))
seen, queue = set(), re.findall(r'partial(?:Cached)? "([^"]+)"', reachable)
while queue:
    p = queue.pop()
    f = f"layouts/partials/{p}"
    if p in seen or not os.path.exists(os.path.join(ROOT, f)):
        continue
    seen.add(p)
    src = r(f)
    reachable += src
    queue += re.findall(r'partial(?:Cached)? "([^"]+)"', src)

classes = set()
for group in re.findall(r'class="([^"{}]+)"', reachable):
    classes.update(group.split())

missing = [c for c in sorted(classes)
           if c and not c.startswith("{") and f".{c}" not in sa_css and f".{c}" in all_css]

print(f"checked {len(classes)} classes reachable from the standalone layout")
if missing:
    print(f"\n❌ {len(missing)} styled outside the standalone bundle:")
    for m in missing:
        print(f"  .{m}")
    sys.exit(1)
print("✅ every class the standalone layout renders is styled by a file it loads")

#!/usr/bin/env python3
"""check-bundles.py — every rule reaches every layout that needs it.

Two layouts assemble two different CSS bundles. PaperMod pages load all of
assets/css/extended/*.css; the standalone layout hand-picks four files. A class
rendered by a shared partial but styled in a file only one bundle loads is
invisible in the other, and it fails silently: the markup is there, the page
looks wrong, and no build error appears.

This has shipped twice. `.report-frame` collapsed to a 300px iframe when its
rules moved to 50-content.css, and `.related-project` rendered unstyled on the
report page for the same reason.

Rule: a class used by a template the standalone layout renders must be defined
in a stylesheet the standalone bundle loads.
"""
import re, sys, glob, os

ROOT = os.path.join(os.path.dirname(__file__), "..")
def r(p): return open(os.path.join(ROOT, p), encoding="utf-8").read()

sa_tpl = r("layouts/_default/standalone.html")
bundle = re.search(r"range \(slice ([^)]*)\)", sa_tpl).group(1)
sa_css = "".join(r("assets/" + f) for f in re.findall(r'"([^"]+)"', bundle)
                 if os.path.exists(os.path.join(ROOT, "assets", f)))
all_css = "".join(r(f) for f in sorted(glob.glob(os.path.join(ROOT, "assets/css/extended/*.css"))))

# what the standalone layout can render: itself, every shortcode, and the
# partials its content footer composes
reachable = sa_tpl
for f in glob.glob(os.path.join(ROOT, "layouts/shortcodes/*.html")):
    reachable += r(os.path.relpath(f, ROOT))
for p in ("content-footer", "content-actions", "share_icons", "section-nav",
          "comments", "brand-mark", "author-card", "related-project"):
    f = f"layouts/partials/{p}.html"
    if os.path.exists(os.path.join(ROOT, f)):
        reachable += r(f)

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

#!/usr/bin/env python3
"""check-contrast.py — every text token must be readable on every surface.

The original gate only checked ACCENTS against --bg. That let --ink-mute ship
at 3.15:1 on --bg-alt, failing WCAG AA for normal text across every eyebrow,
date and caption on the site. This checks the whole matrix instead.

Rules: body/label text needs 4.5:1. Accents are also used for links in running
text, so they are held to the same bar.
"""
import re, sys, os

TOKENS = os.path.join(os.path.dirname(__file__), "..",
                      "assets", "css", "extended", "00-tokens.css")
AA = 4.5

def lum(h):
    h = h.lstrip("#")
    r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def ratio(a, b):
    l1, l2 = sorted((lum(a), lum(b)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)

css = open(TOKENS).read()
# :root block = light, .dark block = dark
light_block = css.split(":root{")[1].split("}")[0]
dark_block = css.split(".dark{")[1].split("}")[0]

def tokens(block):
    return dict(re.findall(r"--([\w-]+)\s*:\s*(#[0-9a-fA-F]{6})", block))

fails = []
checked = 0
for theme, block, base in (("light", light_block, None), ("dark", dark_block, None)):
    t = tokens(block)
    if theme == "dark":                       # dark only redefines some tokens
        merged = tokens(light_block); merged.update(t); t = merged
    bgs = [("--bg", t["bg"]), ("--bg-alt", t["bg-alt"])]
    fgs = [k for k in t if k.startswith("ink") or k == "accent"
           or k.startswith("cat-") and not k.endswith("-soft")]
    for fg in sorted(fgs):
        for bgname, bg in bgs:
            r = ratio(t[fg], bg)
            checked += 1
            if r < AA:
                fails.append(f"{theme}: --{fg} ({t[fg]}) on {bgname} ({bg}) = {r:.2f}:1")

print(f"checked {checked} token/background pairs against {AA}:1")
if fails:
    print(f"\n\u274c {len(fails)} below AA for normal text:")
    for f in fails:
        print("  ", f)
    sys.exit(1)
print("\u2705 every text token clears AA on every surface, both themes")

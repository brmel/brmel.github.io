#!/usr/bin/env python3
import glob, re, os
from gate import ROOT, finish

TOKENS = os.path.join(ROOT, "assets", "css", "extended", "00-tokens.css")
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
light_block = css.split(":root{")[1].split("}")[0]
dark_block = css.split(".dark{")[1].split("}")[0]

def tokens(block):
    return dict(re.findall(r"--([\w-]+)\s*:\s*(#[0-9a-fA-F]{6})", block))

fails = []
checked = 0
for theme, block in (("light", light_block), ("dark", dark_block)):
    t = tokens(block)
    if theme == "dark":
        merged = tokens(light_block); merged.update(t); t = merged
    bgs = [("--bg", t["bg"]), ("--bg-alt", t["bg-alt"])]
    fgs = [k for k in t if k.startswith("ink") or k == "accent"]
    for fg in sorted(fgs):
        for bgname, bg in bgs:
            r = ratio(t[fg], bg)
            checked += 1
            if r < AA:
                fails.append(f"{theme}: --{fg} ({t[fg]}) on {bgname} ({bg}) = {r:.2f}:1")

THEME = os.path.join(ROOT, "themes", "PaperMod", "assets", "css")
EXT = os.path.join(ROOT, "assets", "css", "extended")
light_tokens = tokens(light_block)
syntax = {cls: col for cls, col in re.findall(
    r"\.chroma \.([\w-]+)\s*\{[^}]*?(?<![-\w])color:\s*(#[0-9a-fA-F]{6})",
    open(os.path.join(THEME, "includes", "chroma-styles.css")).read())
    if cls not in ("ln", "lnt", "hl")}
for f in glob.glob(os.path.join(EXT, "*.css")):
    for classes, token in re.findall(r"\.chroma\s*:is\(([^)]*)\)\s*\{[^}]*?color:\s*var\(--([\w-]+)\)", open(f).read()):
        for cls in re.findall(r"\.([\w-]+)", classes):
            syntax[cls] = light_tokens[token]
theme_vars = open(os.path.join(THEME, "core", "theme-vars.css")).read()
code_bgs = ["#%02x%02x%02x" % tuple(map(int, m))
            for m in re.findall(r"--code-block-bg:\s*rgb\((\d+),\s*(\d+),\s*(\d+)\)", theme_vars)]
for cls, col in sorted(syntax.items()):
    for theme, bg in zip(("light", "dark"), code_bgs):
        checked += 1
        if ratio(col, bg) < AA:
            fails.append(f"{theme}: syntax .{cls} ({col}) on code background ({bg}) = {ratio(col, bg):.2f}:1")

print(f"checked {checked} token/background pairs against {AA}:1")
finish(fails, "every text token and syntax colour clears AA on its surface, both themes")

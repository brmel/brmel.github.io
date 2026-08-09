#!/usr/bin/env python3
"""check-css.py — keep the stylesheet layer modular.

The CSS started as one 541-line file that accumulated eight unrelated concerns,
plus a 208-line legacy file where more than half styled a feature that had been
deleted. Nothing noticed either. These rules make that shape fail the build
instead of accumulating quietly.

Rules
  1. Explicit cascade. Every file in css/extended/ is NN-name.css. Hugo
     concatenates by lexical order, so the number IS the architecture — without
     it, tokens.css sorted last, after everything that consumes it.
  2. Tokens are the only place a colour is defined.
  3. No file over MAX_LINES. A file that large is doing more than one job.
  4. The shared primitives live in one file. If a card, accent bar or eyebrow
     is redeclared in a section file, that is duplication returning.
  5. No dead selectors: every class in the CSS must appear somewhere in
     layouts/, content/ or assets/js/.
"""
import os, re, sys, glob

ROOT = os.path.join(os.path.dirname(__file__), "..")
EXT = os.path.join(ROOT, "assets", "css", "extended")
MAX_LINES = 260
TOKENS = "00-tokens.css"
COMPONENTS = "20-components.css"

# Patterns that belong to the primitives layer and nowhere else.
PRIMITIVES = {
    "card surface": re.compile(r"background:var\(--bg-alt\);\s*\n?\s*border:var\(--hairline\) solid var\(--rule\)"),
    "hover lift": re.compile(r"transform:translateY\(-2px\)"),
}

fails, warns = [], []
files = sorted(glob.glob(os.path.join(EXT, "*.css")))

# 1 — naming / cascade order
for f in files:
    b = os.path.basename(f)
    if not re.match(r"^\d{2}-[a-z0-9-]+\.css$", b):
        fails.append(f"{b}: must be NN-name.css so the cascade order is explicit")

# 2 — colours only in tokens
for f in files:
    b = os.path.basename(f)
    if b == TOKENS:
        continue
    src = open(f).read()
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)          # ignore comments
    for m in re.findall(r"#[0-9a-fA-F]{3,8}\b", src):
        if m.lower() in ("#fff", "#ffffff", "#000", "#000000"):
            warns.append(f"{b}: raw {m} — acceptable only for a fixed ground (iframe, print)")
        else:
            fails.append(f"{b}: colour {m} defined outside {TOKENS}")

# 3 — file size
for f in files:
    n = sum(1 for _ in open(f))
    if n > MAX_LINES:
        fails.append(f"{os.path.basename(f)}: {n} lines (max {MAX_LINES}) — split it by concern")

# 4 — primitives not redeclared
for f in files:
    b = os.path.basename(f)
    if b in (TOKENS, COMPONENTS):
        continue
    src = open(f).read()
    for name, pat in PRIMITIVES.items():
        if pat.search(src):
            fails.append(f"{b}: redeclares the '{name}' primitive — compose {COMPONENTS} instead")

# 5 — dead selectors
markup = ""
for pat in ("layouts/**/*.html", "content/**/*.md", "assets/js/*.js"):
    for f in glob.glob(os.path.join(ROOT, pat), recursive=True):
        markup += open(f, encoding="utf-8", errors="ignore").read()
# theme templates can use our classes too
for f in glob.glob(os.path.join(ROOT, "themes/PaperMod/layouts/**/*.html"), recursive=True):
    markup += open(f, encoding="utf-8", errors="ignore").read()

declared = set()
for f in files:
    src = re.sub(r"/\*.*?\*/", "", open(f).read(), flags=re.S)
    declared |= set(re.findall(r"\.([a-z][a-z0-9_-]*(?:__[a-z0-9-]+)?(?:--[a-z0-9-]+)?)", src))

# classes the theme owns, or that JS/markdown generate
IGNORE = {"dark", "active", "highlight", "post-content", "post-single", "post-header",
          "post-footer", "post-tags", "post-title", "post-description", "post-meta",
          "entry-header", "entry-content", "entry-footer", "entry-link", "entry-hint",
          "entry-hint-parent", "first-entry", "page-header", "pagination", "prev", "next",
          "share-buttons", "social-icons", "logo", "logo-switches", "lang-switch", "nav",
          "main", "footer", "header", "profile", "profile_inner", "buttons", "button",
          "button-inner", "top-link", "breadcrumbs", "terms-tags", "archive-month",
          "paginav", "toc", "adventures", "align-center", "video-js", "vjs-tech"}
dead = sorted(c for c in declared if c not in IGNORE and c not in markup)
for c in dead:
    warns.append(f"class .{c} is declared in CSS but appears in no template or content")

print(f"checked {len(files)} stylesheets, {len(declared)} classes")
for w in warns:
    print("  ⚠  " + w)
if fails:
    print(f"\n❌ {len(fails)} problem(s):")
    for f in fails:
        print("  " + f)
    sys.exit(1)
print("✅ cascade explicit · colours in tokens only · no oversized files · no duplicated primitives")

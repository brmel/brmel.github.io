#!/usr/bin/env python3
import glob, os, re
from urllib.parse import unquote
from gate import ROOT, finish

DOCS = ["AGENTS.md", "README.md", "ARCHITECTURE.md",
        *glob.glob("docs/**/*.md", root_dir=ROOT, recursive=True),
        *glob.glob(".claude/skills/**/SKILL.md", root_dir=ROOT, recursive=True)]
FENCE = re.compile(r"^(```|~~~).*?^\1", re.S | re.M)
CODE = re.compile(r"`([^`\n]+)`")
LINK = re.compile(r"\]\(([^)\s]+)")
PLACEHOLDER = re.compile(r"[<>{}…]|\.\.\.")
TOP = set(os.listdir(ROOT))

fails, checked = [], 0
for doc in sorted(DOCS):
    text = FENCE.sub("", open(os.path.join(ROOT, doc), encoding="utf-8").read())
    words = (w.removeprefix("./") for span in CODE.findall(text) for w in span.split())
    refs = [w for w in words if w.split("/")[0] in TOP and not PLACEHOLDER.search(w)]
    refs += [os.path.join(os.path.dirname(doc), unquote(l.split("#")[0]))
             for l in LINK.findall(CODE.sub("", text)) if not re.match(r"[a-z]+:|#|/", l)]
    for ref in refs:
        checked += 1
        if not glob.glob(os.path.join(ROOT, ref), recursive=True):
            fails.append(f"{doc}: {ref} does not exist")

print(f"checked {checked} paths and links in {len(DOCS)} docs")
finish(fails, "every repo path and relative link in the docs exists")

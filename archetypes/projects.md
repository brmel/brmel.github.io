---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true

# --- brand chrome: everything below renders automatically, see
# --- docs/projects-playbook.md. Do not hand-write the eyebrow or the chips.
projectNo:                     # stable, never reused, never renumbered
domain: "saas"                 # saas | mobile | data | infra  -> sets the accent
status: "active"               # shipped | active | prototype | archived
pitch: ""                      # ONE line a non-engineer understands
stack: []                      # ["Flutter", "Firebase", …] — first 4 show on the card
links:
  live: ""
  repo: ""
takeaway: ""                   # one sentence, feeds the learning block on /projects/

lessons:                       # 3–5 bullets. At least one must be a real failure.
  - ""
  - ""
  - ""

tags: []
---

## The story

Why this existed. What problem, for whom, and why you decided to build it rather
than use something that already worked. Not the README — the reader has never
heard of this project.

## The product

What it actually became. Screens, flows, the one or two decisions that made it
work. Concrete numbers where you have them.

<!--
GALLERY: drop images in this page bundle under gallery/ — e.g.
    content/projects/<slug>/gallery/01-board.png
They render automatically, resized and fingerprinted, in filename order.
Compress before committing, and check every image for private data first.
-->

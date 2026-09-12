---
title: "{{ replace .File.ContentBaseName `-` ` ` | title }}"
date: {{ .Date }}
draft: true

projectNo:                     # stable, never reused, never renumbered
domain: "saas"                 # saas | mobile | data | infra  -> eyebrow label
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

Why this existed. What problem, for whom, and why you decided to build it rather
than use something that already worked. Not the README — the reader has never
heard of this project.

What it actually became. Screens, flows, the one or two decisions that made it
work. Concrete numbers where you have them.


---
title: "{{ replace .File.ContentBaseName `-` ` ` | title }}"
date: {{ .Date }}
draft: true

summary: ""
description: ""

tags: []                       # existing terms first, see /tags/
cover:
    image: "cover.jpg"         # in this folder; the figure shortcode resizes it
    alt: ""                    # required — check-og.py fails the build without it
    relative: true

# series: "Windows Memory Management"
# seriesPart: 1
# relatedProject: "meteodata"
# canonicalOriginal: "https://www.linkedin.com/pulse/…"
# canonicalOriginalName: "LinkedIn"
---

Open with the concrete thing, not a preamble. One or two sentences.

{{</* figure src="01-something.jpg" alt="" caption="" */>}}

Images are capped at their own pixel width, so a 400px screenshot renders at
400px rather than being stretched. Capture at 900px or wider to fill the column.

- [Title](https://example.com)

---
title: "{{ replace .File.ContentBaseName `-` ` ` | title }}"
date: {{ .Date }}
draft: true

# Both are used. summary is the card text on /tech/ and the RSS blurb;
# description is the meta description, and is what search engines show.
# Keep description under 160 characters — check-og.py does not police it.
summary: ""
description: ""

tags: []                       # existing terms first, see /tags/
cover:
    image: "cover.jpg"         # in this folder; the figure shortcode resizes it
    alt: ""                    # required — check-og.py fails the build without it
    relative: true

# --- optional, delete what you do not use -------------------------------------
# Part of a multi-article series; both keys are needed for the series card.
# series: "Windows Memory Management"
# seriesPart: 1
#
# Links the article to the project page it came out of.
# relatedProject: "meteodata"
#
# Published elsewhere first. Renders "Originally published on …" and does NOT
# change the canonical URL, which stays on this site.
# canonicalOriginal: "https://www.linkedin.com/pulse/…"
# canonicalOriginalName: "LinkedIn"
---

Open with the concrete thing, not a preamble. One or two sentences.

## First section

{{</* figure src="01-something.jpg" alt="" caption="" */>}}

Images are capped at their own pixel width, so a 400px screenshot renders at
400px rather than being stretched. Capture at 900px or wider to fill the column.

## Sources

- [Title](https://example.com)

---
title: "{{ replace .File.ContentBaseName `-` ` ` | title }}"
date: {{ .Date }}
draft: true

summary: ""
description: ""

tags: []
cover:
    image: "cover.jpg"
    alt: ""
    relative: true
---

Open with the concrete thing, not a preamble. One or two sentences.

{{</* figure src="01-something.jpg" alt="" caption="" */>}}

Images are capped at their own pixel width, so a 400px screenshot renders at
400px rather than being stretched. Capture at 900px or wider to fill the column.

- [Title](https://example.com)

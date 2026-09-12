---
title: "{{ replace .File.ContentBaseName `-` ` ` | title }}"
date: {{ .Date }}
draft: true
summary: ""
tags: ["Montreal", "Adventure"]
cover:
    image: "cover.jpg"
    alt: ""
    relative: true
category: "restaurant"   # restaurant | hike | spa | event | city → eyebrow label + badge icon
fieldNote: 0             # → № 000 in the eyebrow
place: ""                # → eyebrow place, e.g. "Old Montréal"
rating: 0                # → verdict, out of 5
goBack: ""               # verdict: would you go back?
bestFor: ""              # verdict: who it's for
con: ""                  # verdict: the one honest con
---

One or two sentences that hook the reader and say where we are.

{{</* figure src="photo-1.jpg" alt="" caption="" */>}}

Set the scene — what it is, why you went, the vibe.

Walk through the experience. Keep it personal and specific.

{{</* figure src="photo-2.jpg" alt="" caption="" */>}}

{{</* gmap q="PLACE NAME, Montreal" title="PLACE NAME" */>}}

- **Go for:** what this place is best at
- **Order / try:** the specific thing to get
- **Skip:** what wasn't worth it
- **Budget:** rough price per person
- **Best time:** when to go to avoid crowds
- **Getting there:** metro/parking notes


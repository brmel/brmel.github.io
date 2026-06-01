---
title: "{{ replace .File.ContentBaseName `-` ` ` | title }}"
date: {{ .Date }}
draft: true
summary: ""
tags: ["Montreal", "Adventure"]
categories: ["Adventures"]
cover:
    image: "cover.jpg"
    alt: ""
    relative: true
# --- field note: drives the eyebrow, accent, verdict, and reels ---
category: "restaurant"   # restaurant | hike | spa | event | city → sets the accent
fieldNote: 0             # → № 000 in the eyebrow
place: ""                # → eyebrow place, e.g. "Old Montréal"
rating: 0                # → verdict, out of 5
goBack: ""               # verdict: would you go back?
bestFor: ""              # verdict: who it's for
con: ""                  # verdict: the one honest con
reels:                   # one row of reviews at the foot; drop any platform you skipped
  - { platform: "youtube",   id: "VIDEO_ID", meta: "" }
  - { platform: "instagram", url: "https://www.instagram.com/reel/CODE/", thumb: "ig-thumb.jpg", meta: "@ibraverse" }
  - { platform: "tiktok",    url: "https://www.tiktok.com/@you/video/ID", thumb: "tt-thumb.jpg", meta: "" }
---

One or two sentences that hook the reader and say where we are.

## The place

{{</* figure src="photo-1.jpg" alt="" caption="" */>}}

Set the scene — what it is, why you went, the vibe.

## What I did

Walk through the experience. Keep it personal and specific.

{{</* figure src="photo-2.jpg" alt="" caption="" */>}}

## Map

{{</* gmap q="PLACE NAME, Montreal" title="PLACE NAME" */>}}

## Recommendations

- **Go for:** what this place is best at
- **Order / try:** the specific thing to get
- **Skip:** what wasn't worth it
- **Budget:** rough price per person
- **Best time:** when to go to avoid crowds
- **Getting there:** metro/parking notes

<!-- The Verdict block and the Watch reels row render automatically from the
     field-note front matter above — no headings needed here. -->

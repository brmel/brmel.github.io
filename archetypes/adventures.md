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

## Verdict

Would you go back? One honest line.

## Watch

{{</* reels
    youtube="VIDEO_ID"
    instagram="https://www.instagram.com/reel/CODE/" instagram_thumb="ig-thumb.jpg"
    tiktok="https://www.tiktok.com/@you/video/ID"     tiktok_thumb="tt-thumb.jpg" */>}}

---
title: "{{ replace .File.ContentBaseName `-` ` ` | title }}"
date: {{ .Date }}
draft: true
description: ""
tags: []
cover:
    image: "cover.jpg"
    alt: ""
category: "restaurant"
place: ""
rating: 0
goBack: ""
bestFor: ""
con: ""
---

One or two sentences that hook the reader and say where we are.

{{</* figure src="photo-1.jpg" alt="" caption="" */>}}

## The place

Set the scene — what it is, why you went, the vibe.

## What I did

Walk through the experience. Keep it personal and specific.

{{</* figure src="photo-2.jpg" alt="" caption="" */>}}

## Recommendations

- **Go for:** what this place is best at
- **Order / try:** the specific thing to get
- **Skip:** what wasn't worth it
- **Budget:** rough price per person
- **Best time:** when to go to avoid crowds
- **Getting there:** metro/parking notes

{{</* gmap q="PLACE NAME, Montreal" title="PLACE NAME" */>}}

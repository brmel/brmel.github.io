---
title: "Standalone Article Template"
date: 2026-06-01
draft: true
layout: "standalone"
summary: "Scaffold for a full-page, self-contained tech article. Duplicate this folder, drop in your HTML/markdown body, and set draft: false."
tags: ["Template"]
# cover: { image: "cover.jpg", alt: "", relative: true }   # optional → og:image
# customCSS: ["css/standalone-template.css"]                # optional per-article styles
# customJS:  ["js/standalone-template.js"]                  # optional per-article scripts
# hideAutoHeader: true                                      # hide the auto title if your HTML has its own hero
---

<!--
  HOW TO USE
  1. Duplicate this folder → content/tech/<your-slug>/index.md
  2. Paste your article BODY below (HTML and/or markdown). Do NOT paste a full
     <html>…</html> document — the `standalone` layout already provides the
     <head> (SEO + Google Analytics + brand fonts/tokens), the top nav, and the
     footer. Inline <style>/<script> are fine here.
  3. Put any images in the same folder; reference them relatively (e.g. src="pic.jpg").
  4. Heavy styling/scripts → put them in assets/ and list them in customCSS / customJS.
  5. Set draft: false to publish. The page routes to /tech/<your-slug>/.
-->

This is a **standalone** tech article: a full HTML page that bypasses the
PaperMod chrome but still gets the site brand, working navigation, and Google
Analytics.

## Things to verify

- The top bar links back to [Tech](/tech/) and [Home](/) and the theme toggle works.
- An external link opens correctly: [Hugo docs](https://gohugo.io/).
- Code renders in the brand mono font:

```cpp
int answer = 42;  // standalone body content
```

> Replace everything below the front matter with your real article body.

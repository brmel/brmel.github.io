# Adventures Playbook — Montreal articles with video reviews

How to publish an Adventures article: a short **video review** up top (YouTube
Short + Instagram Reel + TikTok side by side), then pictures, a **map**, and
honest **recommendations**.

This is the repeatable recipe. Tools are already wired up: a `reels` shortcode,
a `gmap` shortcode, the existing `figure` shortcode, and an `adventures`
archetype that scaffolds the whole structure.

---

## 0. Mental model

- **Adventures** = places & experiences (Montreal and travel). Each article opens
  with a short vertical video review to pull views from YouTube/IG/TikTok back to
  the site.
- **Lifestyle** = health/training/protocols (e.g. *The Operating Protocol*). Not
  the same thing — don't mix them.
- One article = one **page bundle**: a folder under `content/adventures/<slug>/`
  with `index.md` plus all its images living next to it.

---

## 1. Shoot & publish the reel first

1. Record one vertical (9:16) clip reviewing the place — voice + b-roll, ~15–45s.
2. Post the SAME clip to all three platforms (more reach, one shoot):
   - **YouTube** → upload as a *Short*.
   - **Instagram** → post as a *Reel*.
   - **TikTok** → post the video.
3. Grab the links/IDs you'll paste into the article:
   - **YouTube**: the 11-char video ID (the part after `/shorts/` or `v=`), or
     just paste the full URL — the shortcode extracts it.
   - **Instagram**: the reel URL, e.g. `https://www.instagram.com/reel/CXXXXXX/`.
   - **TikTok**: the video URL, e.g. `https://www.tiktok.com/@you/video/7300000000000000000`.
4. **Thumbnails:** YouTube provides one automatically. Instagram and TikTok don't
   expose one publicly, so export a single frame from your clip and drop it in the
   article folder (`ig-thumb.jpg`, `tt-thumb.jpg`). Keep them small (≤1080px wide).

The reels load **on click** (the visitor sees your thumbnail with a play button),
so three embeds won't slow the page.

---

## 2. Create the article

From the repo root:

```bash
hugo new adventures/old-port-walk/index.md
```

This uses `archetypes/adventures.md` and gives you a ready-made skeleton
(`draft: true`, reels block, figures, map, recommendations). Put every photo for
the article in that same `content/adventures/old-port-walk/` folder.

> No CLI? Copy an existing folder under `content/adventures/`, rename it, and edit.

---

## 3. Fill it in

### Front matter

```yaml
---
title: "A Walk Through the Old Port"
date: 2026-06-01
draft: true
summary: "One-line teaser shown in the Adventures list and on social cards."
tags: ["Montreal", "Old Port", "Walking"]
categories: ["Adventures"]
cover:
    image: "cover.jpg"     # a photo in this folder
    alt: "Old Port of Montreal at sunset"
    relative: true
---
```

### The reel block (top of the article)

```text
{{< reels
    youtube="dQw4w9WgXcQ"
    instagram="https://www.instagram.com/reel/CXXXXXX/" instagram_thumb="ig-thumb.jpg"
    tiktok="https://www.tiktok.com/@you/video/7300000000000000000" tiktok_thumb="tt-thumb.jpg" >}}
```

- Omit any platform you didn't post to — only the ones you pass are shown.
- `*_thumb` names refer to images in the article folder.

### Pictures

Use the existing `figure` shortcode (auto-resolves images in the bundle, lazy-loads):

```text
{{< figure src="photo-1.jpg" alt="Cobblestone street" caption="Rue de la Commune" >}}
```

Optimize before committing: resize to ~1600px max width, compress (JPEG/WebP).
Big unoptimized photos are the #1 thing that slows the site.

### Map

Pick one:

```text
{{< gmap q="Old Port of Montreal" title="Old Port" >}}
```

or, for a styled map / custom pin, in Google Maps → **Share → Embed a map**, copy
the `src="..."` and use:

```text
{{< gmap src="https://www.google.com/maps/embed?pb=..." title="Old Port" >}}
```

For a multi-stop route, build a **Google My Maps**, then embed its `src`.

### Recommendations

Keep the scannable list from the archetype: *Go for / Order-try / Skip / Budget /
Best time / Getting there*, then a one-line **Verdict**.

---

## 4. Preview, then publish

```bash
hugo server -D        # -D renders drafts; open http://localhost:1313/adventures/
```

When happy, set `draft: false` (or delete the line) and commit. The article then
appears in the Adventures section, the home feed, and the RSS feed.

---

## 5. Translations (optional but consistent with the site)

The site is trilingual (en/fr/ar). Tech articles ship all three. To translate an
adventure, add siblings in the same folder:

```
content/adventures/old-port-walk/
  index.md        # English (default)
  index.fr.md     # Français
  index.ar.md     # العربية  (RTL is handled automatically)
```

Shortcodes (`reels`, `gmap`, `figure`) and images are shared — only the prose
changes per language.

---

## 6. Checklist

- [ ] Vertical clip posted to YouTube / Instagram / TikTok
- [ ] `hugo new adventures/<slug>/index.md`
- [ ] `reels` block at the top with correct IDs/URLs + IG/TikTok thumbs
- [ ] `cover.image` set; photos optimized and in the folder
- [ ] `gmap` added
- [ ] Recommendations + Verdict written
- [ ] Previewed with `hugo server -D`
- [ ] `draft: false`, commit, push

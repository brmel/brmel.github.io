# Adventures Playbook — Montreal articles with a voice/face video review

How to publish an Adventures article that **goes viral and stays on-brand**:
a written article with photos, a map, and honest recommendations, closing with a
short **face + voice video review** at the bottom (you on camera explaining the
place) shown as a single row of YouTube / Instagram / TikTok thumbnails.

The whole point is a **repeatable pattern**: every article looks the same, every
reel follows the same beats, so the audience learns your format and the work gets
faster each time. Treat this file as the single source of truth — follow it
article-by-article and don't improvise the structure.

**Photographs must be yours and must be of the place.** The two field notes
published in August 2026 shipped as drafts carrying one stock file reused as the
hero of both a Rawdon spa and an Adirondack summit; they went live without
images rather than with borrowed ones. Same rule for the reels row — it links
your own clips or it stays empty.

`gmap` takes a real embed URL from Google Maps → Share → "Embed a map". The
`q="place name"` form renders a link, not an iframe: Google refuses to frame the
legacy `maps.google.com/maps?output=embed` URL and it came out as a blank box.

Tools are already wired: a `reels` shortcode, a `gmap` shortcode, the `figure`
shortcode, and an `adventures` archetype that scaffolds the structure.

---

## 0. The format in one picture

```
┌───────────────────────────────────────┐
│  FIELD NOTE № 004 · CATEGORY · PLACE   │  ← eyebrow + compass accent (auto)
│  Big serif title                       │
│  One-line hook sentence                │
│  ## The place        + photo           │
│  ## What I did       + photo           │
│  ## Map              (gmap)            │
│  ## Recommendations  (scannable list)  │
├───────────────────────────────────────┤
│  VERDICT  (goBack / bestFor / con / ★) │  ← structured, from front matter (auto)
├───────────────────────────────────────┤
│  WATCH — reel row (YT + IG + TikTok)   │  ← one row, from front matter (auto)
└───────────────────────────────────────┘
```

The **header eyebrow, Verdict block, and Watch reel row all render
automatically** from front matter (`category`, `fieldNote`, `place`, `rating`,
`goBack`, `bestFor`, `con`, `reels`). You write only the prose body — the brand
chrome is layout-driven, so every article is consistent by construction.
`category` (restaurant / hike / spa / event / city) sets the accent color.

- **Adventures** = places & experiences (Montreal + travel). Reel pulls views
  from YouTube/IG/TikTok back to the site.
- **Lifestyle** = health/training/protocols. Different section — don't mix.
- One article = one **page bundle**: `content/adventures/<slug>/index.md` + all
  its images in the same folder.

---

## 1. The VIDEO — record voice (and face) for the article

This is the growth engine. The video is filmed *as if* narrating the article:
you talk through the place, the article is the written version of the same script.

### 1.1 Format & specs (all platforms, one shoot)

| Thing | Spec |
|-------|------|
| Aspect ratio | **9:16 vertical** (1080×1920) |
| Length | **15–45s** (sweet spot 22–30s). Shorts/Reels/TikTok all favor short + replays |
| Frame rate | 30fps (60fps if lots of motion) |
| Face | Yes if comfortable — a face in the first frame lifts watch-time. Talking-head + b-roll cutaways beats voice-over-only |
| Voice | Clear, close mic. Phone earbuds mic > built-in. Record in a quiet spot or add it as voice-over later |
| Captions | **Always burn in subtitles** — most people watch muted. Auto-captions in CapCut/IG/TikTok, then fix typos |
| Orientation | Lock phone, never switch landscape |

### 1.2 The viral structure — same beats every time

Reproducibility = the audience recognizes your pattern. Use these 5 beats in
**every** reel:

1. **Hook (0–3s)** — the make-or-break. Say the payoff first, on camera.
   - Templates: *"This is the best [thing] in Montreal and almost nobody knows it."*
     / *"Don't go to [place] before you watch this."* / *"I found a [X] in Montreal
     that costs [Y]."*
   - Show the most striking shot in frame 1. No slow intros, no "hey guys".
2. **Context (3–8s)** — what it is, where, why it matters. One sentence.
3. **Payoff / proof (8–20s)** — the actual experience: the food, the view, the
   thing. Fast cuts, 1.5–3s per shot. This is the substance.
4. **Honest take (20–30s)** — one real opinion (a pro AND a con). Honesty =
   trust = shares.
5. **CTA (last 2–3s)** — drive to the site + loop.
   - *"Full guide, map, and prices on ibraverse.ca"* / *"Save this for your next
     trip."* / *"Follow for more Montreal spots."*
   - End on a frame that loops back to the hook (boosts replays = algorithm gold).

### 1.3 Shooting guidelines

- **B-roll, lots of it.** Film 5–10 short clips per spot: wide establishing,
  medium, close-up detail, a moving shot (walk-in / pan), your reaction. Variety
  lets you cut fast.
- **Stabilize.** Both hands, elbows tucked, or a small gimbal. Shaky = unwatchable.
- **Light.** Shoot toward the light on your face; golden hour (1h after sunrise /
  before sunset) for exteriors. Avoid harsh noon overhead.
- **Audio first.** Bad video survives, bad audio doesn't. Re-record voice-over
  indoors if the location was noisy.
- **Get the establishing shot + a signage shot** (name of the place) — anchors
  the viewer.
- **Vertical safe zone:** keep faces/text in the **center 80%** — platform UI
  (captions, buttons) covers top ~10% and bottom ~20%.

### 1.4 Editing guidelines (CapCut / InShot / Premiere)

- **Cut on motion / on the beat.** No dead air. First cut within 1.5s.
- **Pacing:** 1.5–3s per shot. Speed-ramp boring transitions (walking → 2×).
- **Music:** use a **trending** audio (TikTok/IG surface trending-audio videos
  more). Keep it low under your voice (-18 to -12 dB).
- **Text overlay:** put the hook as on-screen text too (people read before they
  hear). Big, high-contrast, center-safe.
- **Branding:** same intro font, same caption style, same end-card every time
  (see §4). Consistency = recognizable brand.
- **Export:** 1080×1920, H.264, ~10–15 Mbps. Same export preset each time.

### 1.5 Post to all 3 platforms (more reach, one file)

- **YouTube** → upload as a **Short** (≤60s, vertical). Grab the 11-char video ID.
- **Instagram** → post as a **Reel**. Copy the reel URL.
- **TikTok** → post. Copy the video URL.
- Write platform captions with 1 hook line + 3–5 hashtags (`#montreal #mtlfood
  #montreallife` + 1 niche tag). Same hook wording across platforms.
- **Cross-link:** caption says "full guide on ibraverse.ca"; site embeds the reels.

### 1.6 Thumbnails / covers

YouTube auto-generates one; **override it** for consistency. IG/TikTok have no
public auto-thumbnail, so you supply one (the site needs it too — see §3).

Thumbnail rules (same template every time):
- One **clear subject** + **3–5 word** bold text (e.g. "BEST BAGEL IN MTL").
- High contrast, readable at tiny size. Face with expression if possible.
- Same font + same color accent as your brand (§4).
- Export ~1080px wide JPG. Name it `cover.jpg` (article hero) and
  `ig-thumb.jpg` / `tt-thumb.jpg` (reel cards).

---

## 2. The WRITTEN article — text, photos, map, visuals

The article is the SEO + reference layer: it ranks on Google, holds the map and
prices the reel can't, and gives the reel somewhere to send people.

### 2.1 Text guidelines

- **Voice:** first person, conversational, the way you talked in the reel. Short
  sentences. No travel-brochure fluff.
- **Lead with the hook** — the first sentence mirrors the reel's hook. Don't
  warm up.
- **Length:** 300–700 words. Enough for Google, short enough to read on a phone.
- **Scannable:** `##` headings, short paragraphs (2–3 sentences), bold the key
  noun in a line. People skim.
- **Be specific & honest:** name the dish, the price, the street, the metro. One
  genuine con builds more trust than five pros.
- **One idea per section.** Keep the fixed structure (The place / What I did /
  Map / Recommendations / Verdict) so every article reads the same.
- **SEO:** put the place name + city in the title, the first sentence, and one
  heading. Fill `summary` (used on Google + social cards) with the hook.

### 2.2 Photos & images

- **Hero/cover:** one strong horizontal-ish photo → `cover.jpg`, set in front
  matter `cover.image`. Shows in the list, on Google, on social shares.
- **In-body:** 3–6 photos via the `figure` shortcode. Alternate wide (scene) and
  close (detail). Every photo earns its place — cut filler.
- **Optimize before commit (mandatory — repo is public + must stay fast):**
  - Resize to **≤1600px** wide.
  - Compress: JPEG quality ~80, or WebP. Target **<300KB** per photo.
  - Strip EXIF (removes GPS/personal metadata — privacy + size).
  - Tool: `sips` (mac), `squoosh.app`, or ImageMagick:
    `magick in.jpg -resize 1600x -strip -quality 80 out.jpg`
- **Always set `alt`** — accessibility + SEO.
- **Captions** add context and are scannable — use them.

```text
{{< figure src="photo-1.jpg" alt="Cobblestone street in the Old Port" caption="Rue de la Commune at golden hour" >}}
```

### 2.3 Map

Every adventure gets a map — it's the reason people save the article.

```text
{{< gmap q="Schwartz's Deli, Montreal" title="Schwartz's Deli" >}}
```

- Quick pin: `q="Place Name, Montreal"`.
- Styled map / exact pin: Google Maps → **Share → Embed a map** → copy `src=`:
  `{{< gmap src="https://www.google.com/maps/embed?pb=..." title="..." >}}`
- Multi-stop route/day: build a **Google My Maps**, embed its `src`. Great for
  "a day in [neighborhood]" articles.

### 2.4 Other visuals (optional, on-brand)

- A simple **at-a-glance box** at the top (cost, time, metro) helps skimmers.
- Keep any custom styling in a scoped CSS asset via `customCSS` front matter —
  **never inline `<style>`** (see the layer-separation rule the codebase enforces).

---

## 3. Build an article — step by step

```bash
hugo new adventures/old-port-walk/index.md
```

Uses `archetypes/adventures.md`, scaffolds `draft: true` + reels + figures + map
+ recommendations. Put every photo in the same `content/adventures/old-port-walk/`
folder.

### Front matter

```yaml
---
title: "A Walk Through the Old Port"
date: 2026-06-01
draft: true
summary: "One-line teaser = the reel's hook. Shown in the list + Google + social."
tags: ["Montreal", "Old Port", "Walking"]
categories: ["Adventures"]
cover:
    image: "cover.jpg"
    alt: "Old Port of Montreal at sunset"
    relative: true
# --- field note (drives the brand chrome) ---
category: "city"          # restaurant | hike | spa | event | city → accent
fieldNote: 5              # → № 005 in the eyebrow
place: "Old Port, Montréal"
rating: 4.2               # verdict, out of 5
goBack: "Yes — first-evening material."
bestFor: "A free sunset walk after the crowds thin."
con: "Touristy — skip the terraces on the square."
reels:                    # one row of reviews at the foot; drop any platform you skipped
  - { platform: "youtube",   id: "VIDEO_ID", meta: "2:14" }
  - { platform: "instagram", url: "https://www.instagram.com/reel/CODE/", thumb: "ig-thumb.jpg", meta: "@ibraverse" }
  - { platform: "tiktok",    url: "https://www.tiktok.com/@you/video/ID", thumb: "tt-thumb.jpg", meta: "0:38" }
---
```

### Body order: hook sentence → photos → map → recommendations. Stop there.

The Verdict and Watch reel row are **not** written in the body — they render
from the front matter above (`rating`/`goBack`/`bestFor`/`con` → Verdict;
`reels` → the Watch row). This keeps every article identical in structure.

### Reels (front matter, not a shortcode)

Each entry in `reels:` is one card in the bottom row:

- `platform`: `youtube` | `instagram` | `tiktok`.
- YouTube uses `id` (the 11-char video ID) and auto-pulls its thumbnail.
- Instagram/TikTok use `url` + a `thumb` image in the article folder
  (`ig-thumb.jpg` / `tt-thumb.jpg`) — they have no public auto-thumbnail.
- `meta`: short caption shown on the card (duration or `@handle`).
- Drop any platform you didn't post to. Omit `reels` entirely → no row.

Recommendations block (keep this exact shape every article):

```markdown
- **Go for:** what it's best at
- **Order / try:** the specific thing
- **Skip:** what's not worth it
- **Budget:** $ per person
- **Best time:** when to avoid crowds
- **Getting there:** metro / parking
```

---

## 4. Theme & branding — make it recognizable

Consistency is what makes content "reproducible" and builds a brand. Lock these
once and reuse forever:

| Element | Lock it |
|---------|---------|
| **Name/handle** | Same on YouTube / IG / TikTok (e.g. @ibraverse). Link all to ibraverse.ca |
| **Colors** | Reuse the site palette (PaperMod CSS vars: `--primary`, accent). Same accent in thumbnails + text overlays |
| **Font** | One display font for thumbnails/overlays; one body font (site default) |
| **Intro** | Same 1–2s opener (logo flash or signature line) on every reel |
| **End card** | Same CTA frame: "ibraverse.ca" + follow prompt |
| **Caption style** | Same subtitle font/position/animation every reel |
| **Tone** | Honest, curious, specific. Same persona on camera and in text |
| **Naming** | Files always `cover.jpg`, `ig-thumb.jpg`, `tt-thumb.jpg`, `photo-N.jpg` |

A viewer should know it's yours from the first frame and the article should feel
like the same series every time.

---

## 5. Preview → publish

```bash
hugo server -D      # -D shows drafts → http://localhost:1313/adventures/
```

When happy: `draft: false`, commit, push. Article then appears in Adventures, the
home feed, and RSS.

---

## 6. Translations (optional, matches the rest of the site)

Site is trilingual (en/fr/ar). To translate an adventure, add siblings in the
same folder — shortcodes/images are shared, only prose changes:

```
content/adventures/old-port-walk/
  index.md      # English (default)
  index.fr.md   # Français
  index.ar.md   # العربية (RTL handled automatically)
```

---

## 7. Per-article checklist

**Video**
- [ ] 9:16, 15–45s, hook in first 3s, face in frame 1
- [ ] 5 beats: hook → context → payoff → honest take → CTA
- [ ] Burned-in captions, trending audio low under voice
- [ ] Posted to YouTube Short + IG Reel + TikTok, same hook caption
- [ ] Thumbnail made (on-brand font + accent)

**Article**
- [ ] `hugo new adventures/<slug>/index.md`
- [ ] `reels` block with correct IDs/URLs + IG/TikTok thumbs
- [ ] First sentence = reel hook; 300–700 words; scannable headings
- [ ] `cover.jpg` set; 3–6 photos, all ≤1600px / <300KB / EXIF-stripped / `alt` set
- [ ] `gmap` added
- [ ] Recommendations + Verdict in the fixed shape
- [ ] Previewed `hugo server -D`
- [ ] `draft: false`, commit, push

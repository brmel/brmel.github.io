# Ibraverse — Field Guide Brand System

The single source of truth for the **visual brand** of Ibraverse content: the
Adventures articles (hikes, restaurants, stays, events, city walks) and the
Operating Protocol. One identity, flexed per content type by a single accent.

> Feed this file to **Claude Design** (and paste it alongside any design prompt)
> so every asset — covers, thumbnails, reel end-cards, decks — comes out on-brand.
> The values below are extracted from the live site (`assets/css/protocol.css`,
> `protocol-fonts.html`, the protocol logomark), not invented.

---

## 1. Brand idea

**Editorial field notes.** Honest, first-person reviews of places and
experiences, laid out like a quietly confident print magazine — warm paper,
ink-black type, one rust accent, a compass mark. Calm, not loud. The same series
every time, whatever the subject.

Voice: honest, curious, specific. One real con builds more trust than five pros.

---

## 2. The hook (signature, reproducible motif)

Three elements appear on **every** asset. They are the brand — reproducible by
rule, recognizable in one frame:

1. **The compass-aperture mark** — concentric circles + 4 ticks (N/S/E/W). The
   exact SVG already lives in the Operating Protocol hero; reuse it verbatim as
   the universal Ibraverse mark.
   ```svg
   <svg viewBox="0 0 40 40" fill="none" aria-hidden="true">
     <circle cx="20" cy="20" r="18" stroke="currentColor" stroke-width="1.5"/>
     <circle cx="20" cy="20" r="11" stroke="currentColor" stroke-width="1.5"/>
     <circle cx="20" cy="20" r="3"  fill="currentColor"/>
     <line x1="20" y1="2"  x2="20" y2="8"  stroke="currentColor" stroke-width="1.5"/>
     <line x1="20" y1="32" x2="20" y2="38" stroke="currentColor" stroke-width="1.5"/>
     <line x1="2"  y1="20" x2="8"  y2="20" stroke="currentColor" stroke-width="1.5"/>
     <line x1="32" y1="20" x2="38" y2="20" stroke="currentColor" stroke-width="1.5"/>
   </svg>
   ```
2. **The eyebrow label** — letterspaced mono caps, always the same grammar:
   `FIELD NOTE № 004 · HIKE · ADIRONDACKS`
   (`FIELD NOTE № {nn} · {CATEGORY} · {PLACE/REGION}`).
3. **The rust accent** (`#a8431a`) — one accent, used sparingly: the mark, the
   eyebrow `·` dots, the category bar, links.

Lay them out the same way each time: mark top-left, eyebrow beside it, big serif
title under, photo fills the rest. Recognizable from the first frame.

---

## 3. Color

Warm-editorial. Paper + ink + a single accent. Light is the home theme.

| Token | Light | Dark | Use |
|-------|-------|------|-----|
| `--bg` (paper) | `#faf9f6` | `#14130f` | page background |
| `--bg-alt` | `#f2f0e9` | `#1c1b16` | cards, wells |
| `--ink` | `#181715` | `#ece8dc` | headings, body |
| `--ink-soft` | `#4a4843` | `#b8b3a2` | secondary text |
| `--ink-mute` | `#8a877f` | `#807c70` | captions, eyebrows |
| `--rule` | `#d9d6cb` | `#2c2a23` | hairlines, borders |
| `--accent` | `#a8431a` | `#d97757` | mark, links, dots |
| `--accent-soft` | `#c96b3e` | `#e89878` | hovers, fills |

### Category accent system (the "any type" flex)

Coherence = everything keeps **paper + ink + the type system**; only the accent
hue swaps per content type. Same saturation/role every time, so it always reads
as one brand. Rust stays the master/home accent.

| Category | Accent (light) | Accent (dark) |
|----------|----------------|----------------|
| **Restaurant / Food** | `#a8431a` rust (master) | `#d97757` |
| **Hike / Trail** | `#3f6b3a` forest | `#5d8a52` |
| **Spa / Stay / Getaway** | `#2f6b6b` teal | `#4f9a9a` |
| **Event** | `#6b3a5d` plum | `#9a5d86` |
| **City / Walk** | `#3a5a6b` slate | `#5d86a0` |

Add a new category = pick one mid-saturation hue at the same value, done.

---

## 4. Type

Already loaded site-side via Google Fonts — reuse, don't add new families.

| Role | Font | Notes |
|------|------|-------|
| **Display / titles** | **Instrument Serif** | editorial headline serif; large, tight |
| **Body / UI** | **Inter Tight** | 400/500/600 |
| **Eyebrows / labels / data** | **JetBrains Mono** | uppercase, letterspaced ~0.12em |

Scale: oversized serif title, small mono eyebrow above it, comfortable Inter Tight
body. Generous line-height, lots of paper.

---

## 5. Asset templates (same template, swap photo + category color + words)

**Article cover / hero — `cover.jpg`** (horizontal, ~1600px)
- Photo full-bleed; paper band with mark + eyebrow + serif title overlaid or below.

**Social cover & reel thumbnails — `ig-thumb.jpg` / `tt-thumb.jpg`** (9:16, 1080×1920)
- Paper background, photo in a rounded frame, compass mark top-left, eyebrow,
  3–5 word title in Instrument Serif, a thin category-color bar at the bottom.
- Text in the **center 80%** safe zone (platform UI covers top 10% / bottom 20%).

**Reel end-card** (9:16)
- Paper, big compass mark centered, `ibraverse.ca`, `@ibraverse`, category bar.

**Reels row (on-site)** — `reels` shortcode renders YouTube + Instagram + TikTok
as one row of click-to-load vertical thumbnails at the **bottom** of the article
(under `## Watch`). Platform badge colors are the only non-brand colors allowed,
and only on those badges.

---

## 6. Locked elements (never improvise)

| Element | Lock |
|---------|------|
| Mark | the compass-aperture SVG above, in accent or ink |
| Handle | `@ibraverse` on YouTube / IG / TikTok → all link to ibraverse.ca |
| Eyebrow grammar | `FIELD NOTE № {nn} · {CATEGORY} · {PLACE}` |
| Fonts | Instrument Serif / Inter Tight / JetBrains Mono only |
| Accent rule | one accent per asset, chosen by category (§3) |
| File names | `cover.jpg`, `ig-thumb.jpg`, `tt-thumb.jpg`, `photo-N.jpg` |
| Tone | honest, curious, specific — one genuine con per piece |

---

## 7. Generating assets with Claude Design

Claude Design (Anthropic Labs) builds a reusable **design system** from your
real inputs, then applies it to every asset. It writes **SVG/HTML/CSS** (true
vector) — it does **not** render raster photos, so it produces layouts, marks,
thumbnail templates, and end-cards into which you drop your own photos.

Setup once:
1. New design system → feed it **this file + the repo/live URL** (`ibraverse.ca`).
   Real code/URL beats a bare palette — minimal inputs give hit-or-miss results.
2. Confirm it extracted the tokens in §3–4 and the mark in §2.
3. Generate the templates in §5; export SVG, refine in Figma/Illustrator only if
   going to print.

The master prompt lives with the team notes; keep this file as the brand input.

# Ibraverse — Brand Kit

Templates and guides for everything made **outside** the site: social posts, video covers, channel
art. The site's own colours, type and components are defined in code and documented in
[`../brand-guidelines.md`](../brand-guidelines.md); where this kit and that file disagree, that file
wins.

All artwork is SVG, sRGB, and uses the live palette: paper `#faf9f6`, ink `#181715`, ink-soft
`#4a4843`, ink-mute `#6e6c65`, rule `#d9d6cb`, one accent `#a8431a`. `‹PHOTO›` slots are placeholders,
never faked.

## The hook, on every asset

1. **Compass-aperture mark** — concentric circles r18 / r11 / r3-filled + 4 N/S/E/W ticks, 1.6 stroke, round caps.
2. **Eyebrow** — `FIELD NOTE № {nnn} · {CATEGORY} · {PLACE}` · JetBrains Mono, uppercase, 0.12em · dots in the accent.
3. **One accent** — only on the mark, the `·` dots, the bottom bar, and links. Category is carried by the eyebrow text, not by colour.
4. **Layout** — mark top-left → eyebrow → oversized serif title → photo fills the rest → thin accent bar.

Fonts: Instrument Serif (display) · Inter Tight 400/500/600 (body) · JetBrains Mono 400/500 (data).

## What's inside

| Folder | Files |
|---|---|
| `01-guides/` | `photography.md` (look, crops, frame, grade) · `voice-tone.md` (persona, eyebrow grammar, captions, 5-beat reel, headlines, verdict) |
| `02-logo/` | `mark.svg` · `mark-circle.svg` · `wordmark-horizontal.svg` · `lockup-stacked.svg` · `favicon-16.svg` · `favicon-32.svg` · `app-icon-180.svg` · `app-icon-512.svg` · `mark-mono-ink.svg` · `mark-mono-paper.svg` · `clearspace-minsize.svg` · `misuse.svg` |
| `03-components/` | `cover-1600x900.svg` · `cover-1600x2000.svg` · `social-9x16.svg` · `ig-4x5.svg` · `ig-1x1.svg` · `story-9x16.svg` · `reel-endcard.svg` · `og-1200x630.svg` · `carousel-1.svg` … `carousel-3.svg` |
| `04-channels/` | `avatar.svg` (reads at 32px) · `youtube-banner-2560x1440.svg` (title-safe 1546×423) |

Clear space around the mark = its outer ring radius. Minimum size: 24px (full mark), 16px (favicon,
no inner ring).

## Export specs

| Asset | Size (px) | Notes |
|---|---|---|
| Article cover (wide / tall) | 1600×900 · 1600×2000 | replace `‹PHOTO›` with the graded photo |
| Social / reel thumb | 1080×1920 | centre-80% safe |
| IG post | 1080×1350 · 1080×1080 | 64px safe |
| Story | 1080×1920 | UI-safe 250 top / 320 bottom |
| Reel end-card | 1080×1920 | — |
| Carousel | 1080×1350 ×3 | hook · proof · verdict + CTA |
| Avatar | 512 → 180 / 32 | bold mark |
| YouTube banner | 2560×1440 | title-safe 1546×423 |

Rasterize at 2× the target size. The SVGs name the fonts but don't embed them — install the three
families before exporting. The site's Open Graph cards are not made here: they come from
`scripts/og-cards.html` via `scripts/gen-og-cards.py`.

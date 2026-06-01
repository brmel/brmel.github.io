# Ibraverse — Brand Package

**Editorial field notes.** A quietly confident print magazine for honest, first-person reviews —
hikes, restaurants, spas & stays, events, city walks — plus the daily *Operating Protocol*.
Warm paper, ink-black type, **one rust accent**, a compass mark. This package establishes the
Operating Protocol look across every surface, vector-only and production-ready.

**Version 1.0** · All SVG / HTML / CSS · sRGB · `‹PHOTO›` slots are placeholders, never faked.

---

## The hook (on every asset, reproducible by rule)

1. **Compass-aperture mark** — concentric circles r18 / r11 / r3-filled + 4 N/S/E/W ticks, 1.6 stroke, round caps.
2. **Eyebrow** — `FIELD NOTE № {nnn} · {CATEGORY} · {PLACE}` · JetBrains Mono, uppercase, 0.12em · dots = accent.
3. **One accent per asset**, chosen by category — used only on the mark, the `·` dots, the category bar, and links.
4. **Layout DNA** — mark top-left → eyebrow → oversized serif title → photo fills the rest → thin category bar.

---

## Quick start

1. **Tokens** → drop `06-web/tokens.css` into the repo (variable names already match `protocol.css`:
   `--bg`, `--ink`, `--accent`, …). Or import `03-color/design-tokens.json` (W3C format) into your tool.
2. **Theme** → `:root` is light; add `data-theme="dark"` for dark. Both are first-class.
3. **Category** → add `data-category="restaurant|hike|spa|event|city"` to `<html>` or an `<article>`.
   Only the accent changes.
4. **Fonts** → Instrument Serif (display) · Inter Tight 400/500/600 (body/UI) · JetBrains Mono 400/500 (data).
5. **See it all** → open `07-proofs/contact-sheet.html` (every component, 5 categories, light + dark).

---

## What's inside

### `01-foundations/`
| File | What |
|---|---|
| `brand-guidelines.md` | The idea, the hook, the quality bar, how the system extends |
| `color.md` · `swatches.svg` | Full palette, hex/RGB/HSL, computed WCAG pairings, new-hue rule |
| `type.md` · `specimen.html` | Type scale (desktop/tablet/mobile), the eyebrow, live specimen |
| `spacing-grid.md` | 8pt scale, containers, 12-col grid, safe-zones, radii, shadows |
| `voice-tone.md` | Persona, do/don't, eyebrow grammar, 5-beat reel, headlines per category |
| `photography.md` | Natural-light direction, crops, the 14px frame, treatment, `‹PHOTO›` |
| `motion.md` | Duration/easing tokens, link/play-button/reveal micro-interactions |

### `02-logo/`
`mark.svg` · `mark-circle.svg` · `wordmark-horizontal.svg` · `lockup-stacked.svg` ·
`favicon-16.svg` · `favicon-32.svg` · `app-icon-180.svg` · `app-icon-512.svg` ·
`mark-mono-ink.svg` · `mark-mono-paper.svg` · `clearspace-minsize.svg` · `misuse.svg`
> Clear space **= the outer ring radius (X)**. Min size: 24px digital (full mark), 16px favicon
> (simplified, no inner ring). Recolor only by swapping the single accent.

### `03-color/`
`tokens.css` (color + category system, protocol var names) · `design-tokens.json` (W3C) ·
`category-accents.svg` (the 5 hues + line icons — trail, fork, steam, ticket, pin).

### `04-components/`  *(canonical = restaurant master, light)*
`cover-1600x900.svg` · `cover-1600x2000.svg` · `social-9x16.svg` · `ig-4x5.svg` · `ig-1x1.svg` ·
`story-9x16.svg` · `reel-endcard.svg` · `og-1200x630.svg` · `carousel-1/2/3.svg` ·
**`web-ui-kit.html`** (live: theme + category switch — header, eyebrow, badge, recs, verdict, buttons, links, tags, footer).

### `05-channels/`
`avatar.svg` (accent disc + knockout mark; reads at 32px) · `youtube-banner-2560x1440.svg` (title-safe 1546×423).

### `06-web/`
`tokens.css` (full repo drop-in: color + space + type + motion) · `adventures-brand.css`
(PaperMod single.html extensions) · `reels.css` (the one-row click-to-load reels shortcode) ·
`hugo-partial.html` (front-matter + header/verdict/icon partials + `reels` shortcode + JS).

### `07-proofs/`
`contact-sheet.html` — **the master board**, every component × 5 categories × light/dark, plus safe-zones.
`proof-restaurant.svg` · `proof-hike.svg` · `proof-spa.svg` · `proof-event.svg` · `proof-city.svg`
(cover + social + end-card, light & dark — proving only accent + eyebrow + photo change).

---

## Color & accessibility (computed WCAG 2.1)

| | Light | Dark |
|---|---|---|
| Paper / bg | `#faf9f6` | `#14130f` |
| Ink (AAA) | `#181715` · 17.0:1 | `#ece8dc` · 15.2:1 |
| Ink-soft (AAA) | `#4a4843` · 8.68:1 | `#b8b3a2` · 8.86:1 |
| Rule | `#d9d6cb` | `#2c2a23` |

**Category accents** (light on paper · dark on bg): Restaurant `#a8431a` 5.73 / `#d97757` 5.95 ·
Hike `#3f6b3a` 5.91 / `#5d8a52` 4.62 · Spa `#2f6b6b` 5.80 / `#4f9a9a` 5.68 ·
Event `#6b3a5d` 8.35 / `#9a5d86` **3.79** · City `#3a5a6b` 6.99 / `#5d86a0` 4.76.

> **Two flags, both fixed.** ① `ink-mute` (3.41/4.46:1) is for **captions/meta only**, never body —
> use `ink-soft`/`ink` for copy. ② **Event's dark accent (3.79:1)** passes for large text / the
> category bar / dots, but not normal inline links on dark — so **links on dark are always underlined**
> (the underline is the affordance). All five *light* accents clear AA on paper without caveat.

---

## Export specs

| Asset | Size (px) | Format | Notes |
|---|---|---|---|
| Article cover (wide / tall) | 1600×900 · 1600×2000 | SVG → PNG/JPG | sRGB · replace `‹PHOTO›` with graded photo at 14px frame |
| Social / reel thumb | 1080×1920 | SVG → PNG | center-80% safe |
| IG post | 1080×1350 · 1080×1080 | SVG → PNG/JPG | 64px safe |
| Story | 1080×1920 | SVG → PNG | UI-safe 250 top / 320 bottom |
| Reel end-card | 1080×1920 | SVG → PNG | — |
| OG / share | 1200×630 | SVG → PNG | 64px safe |
| Carousel | 1080×1350 ×3 | SVG → PNG | hook · proof · verdict+CTA |
| Avatar | 512 → 180/32 | SVG → PNG | bold mark, reads tiny |
| YouTube banner | 2560×1440 | SVG → PNG | title-safe 1546×423 |
| Favicon / app icon | 16 · 32 · 180 · 512 | SVG → ICO/PNG | 16 = simplified mark |

All artwork is vector and resolution-independent; rasterize at **2× the target** for crisp social.
Standalone SVGs reference the three families by name — install them (or embed) for exact type;
the HTML files (`contact-sheet`, `web-ui-kit`, `specimen`) load the webfonts and render pixel-true.

---

## Figma import structure

Create a page **“Ibraverse / Brand”** with frames named to match the files, grouped:
`Logo / mark`, `Logo / wordmark-horizontal`, `Logo / lockup-stacked`, `Logo / clearspace`, `Logo / misuse`;
`Color / swatches`, `Color / category-accents`;
`Type / specimen`;
`Component / cover-1600x900`, `…/cover-1600x2000`, `…/social-9x16`, `…/ig-4x5`, `…/ig-1x1`, `…/story-9x16`,
`…/reel-endcard`, `…/og-1200x630`, `…/carousel-1..3`;
`Channel / avatar`, `Channel / youtube-banner`;
`Proof / restaurant`, `…/hike`, `…/spa`, `…/event`, `…/city`.
Drop each SVG into its frame, set fonts to Instrument Serif / Inter Tight / JetBrains Mono, and
turn the accent into a Figma variable with a mode per category.

---

## The rules, condensed

- One accent per asset. Accent only on mark · `·` dots · category bar · links.
- No font or color outside the tokens. Two surface levels max (paper→alt / bg→alt).
- Everything on the 8pt grid. Optically center the mark. Balance the serif title (3–7 words).
- Body text ≥ AA on its background. Photos are real; `‹PHOTO›` is a placeholder.
- Every review carries **one genuine con**. The same recognizable series, whatever the subject.

*Built on the Operating Protocol · ibraverse.ca · @ibraverse · © 2026 Ibraverse*

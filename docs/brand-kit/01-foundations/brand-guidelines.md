# Ibraverse — Brand Guidelines

*Editorial field notes. A quietly confident print magazine for honest, first-person reviews.*

**Version 1.0 · Establishes the Operating Protocol look across every surface.**

---

## 1. The idea

Ibraverse is a personal series of honest, first-person **field reviews** — hikes, restaurants,
spas & stays, events, city walks — plus a daily **Operating Protocol**. The brand is built to feel
like a quietly confident print magazine: **warm paper, ink-black type, one rust accent, a compass
mark.** Calm, not loud. Honest, curious, specific. Every review carries exactly **one genuine con**.

The promise to the reader: *the same recognizable series every time, whatever the subject.* A hike
and a tasting menu should look like siblings — same mark, same spacing, same type — separated only
by a single accent hue and the photo.

---

## 2. The hook — appears on every asset, reproducible by rule

Three elements make any Ibraverse asset recognizable in a feed at a glance. They are not decoration;
they are the signature. **If an asset is missing one, it is off-brand.**

### 2.1 Compass-aperture mark
Concentric circles — outer **r18**, inner **r11**, filled center **r3** — plus four **N / S / E / W**
ticks crossing the outer ring. Drawn on a 48-unit grid, center (24, 24), stroke **1.5**, round caps.
Always top-left. Optically centered, never mechanically. See `02-logo/`.

### 2.2 Eyebrow label
JetBrains Mono, uppercase, **0.12em** tracking. Fixed grammar:

```
FIELD NOTE № {nnn} · {CATEGORY} · {PLACE / REGION}
```

The number is **zero-padded to three digits** (`№ 004`). The middle dots are `·` (U+00B7) and they
carry the accent color. Example: `FIELD NOTE № 012 · HIKE · GATINEAU PARK`.

### 2.3 The accent — one per asset
Exactly **one accent** per asset, chosen by category, used **sparingly**: the mark, the `·` dots, the
category bar, and links. Never fills, never backgrounds. The rest of the asset is paper + ink.

### 2.4 Fixed layout DNA
> Mark top-left → eyebrow beside or beneath it → oversized Instrument Serif title → photo fills the
> rest → thin category bar. This skeleton never changes; only content and accent do.

---

## 3. Foundations at a glance

| System | Source of truth | File |
|---|---|---|
| Color | Paper + ink + one rust master, five category hues, full dark theme | `color.md`, `03-color/tokens.css` |
| Type | Instrument Serif · Inter Tight · JetBrains Mono | `type.md`, `specimen.html` |
| Spacing & grid | 8pt scale, 12-col web grid, 9:16 safe-zones | `spacing-grid.md` |
| Logo | Compass mark + wordmark system | `02-logo/` |
| Voice | Honest, curious, specific — one con per review | `voice-tone.md` |
| Photography | Natural light, honest not stock, 14px rounded frame | `photography.md` |
| Motion | Web micro-interactions, durations & easings as tokens | `motion.md` |

---

## 4. Color, in one breath

Warm **paper `#faf9f6`**, ink-black **`#181715`**, one hairline **rule `#d9d6cb`**, and a single
**accent** chosen by category. The master accent is Restaurant rust **`#a8431a`** (the default when a
category is ambiguous). Category changes swap **only the accent** — paper, ink, rule, and type stay put.

| Category | Light accent | Dark accent |
|---|---|---|
| Restaurant *(master)* | `#a8431a` | `#d97757` |
| Hike | `#3f6b3a` | `#5d8a52` |
| Spa / Stay | `#2f6b6b` | `#4f9a9a` |
| Event | `#6b3a5d` | `#9a5d86` |
| City / Walk | `#3a5a6b` | `#5d86a0` |

Full hex / RGB / HSL, WCAG pairings, dark theme, and the rule for adding a new hue: `color.md`.

---

## 5. Type, in one breath

- **Instrument Serif** — display titles only. Large, set tight, optically balanced.
- **Inter Tight** (400 / 500 / 600) — body, UI, captions.
- **JetBrains Mono** (400 / 500) — eyebrows, labels, data, the wordmark's metadata.

No other families, ever. Scale, line-heights, tracking, and responsive values: `type.md`.

---

## 6. Voice, in one breath

First person. Specific over general. **One genuine con per review** — always. No hype, no "hidden
gem," no stock enthusiasm. The reel follows a fixed **5-beat structure**: Hook → Place → Proof →
The Con → Verdict. Full persona, do/don't, and per-category example headlines: `voice-tone.md`.

---

## 7. Non-negotiables (the quality bar)

1. **Vector only.** SVG / HTML / CSS. Photos are clearly-labeled `<PHOTO>` slots — never faked.
2. **No font or color outside the tokens.** One accent per asset.
3. **Pixel-perfect.** Exact px for every size, margin, and safe-zone; everything aligns to the 8pt grid.
4. **Accessibility.** Body text meets WCAG AA on its background; any failing pair is flagged and fixed.
5. **Internally consistent.** The same mark, spacing, and type rules across every file.

---

## 8. How the system extends

Adding a new category = pick a hue that meets the contrast rule in `color.md` (≥ 4.5:1 on paper for the
light accent, ≥ 4.5:1 on dark bg for the dark accent), give it a category icon in the mark's stroke
style (`04-components` / iconography), and register both light + dark values as a token pair. Nothing
else changes. That discipline is the brand.

*Next: `color.md`.*

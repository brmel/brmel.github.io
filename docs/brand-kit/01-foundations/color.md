# Ibraverse — Color

One warm paper, one ink-black, one hairline rule, and **one accent chosen by category**. Changing
category swaps **only the accent**. Everything else holds still. That restraint is the whole point.

All contrast ratios below are computed (WCAG 2.1 relative-luminance). Targets: **AA normal ≥ 4.5:1**,
**AA large / UI ≥ 3:1**, **AAA normal ≥ 7:1**.

---

## 1. Neutrals — Light theme (primary)

| Token | Role | HEX | RGB | HSL | On paper |
|---|---|---|---|---|---|
| `--paper` | Page background | `#faf9f6` | 250, 249, 246 | 45° 29% 97% | — |
| `--paper-alt` | Raised band / card | `#f2f0e9` | 242, 240, 233 | 47° 26% 93% | 1.08:1 *(surface)* |
| `--ink` | Primary text, titles | `#181715` | 24, 23, 21 | 45° 30% 9% | **17.02:1** ✓ AAA |
| `--ink-soft` | Secondary text | `#4a4843` | 74, 72, 67 | 47° 5% 28% | **8.68:1** ✓ AAA |
| `--ink-mute` | Captions, metadata | `#8a877f` | 138, 135, 127 | 45° 4% 52% | 3.41:1 ⚠︎ large/UI only |
| `--rule` | Hairlines, dividers | `#d9d6cb` | 217, 214, 203 | 45° 19% 82% | 1.38:1 *(non-text)* |

## 2. Neutrals — Dark theme

| Token | Role | HEX | RGB | HSL | On bg `#14130f` |
|---|---|---|---|---|---|
| `--bg` | Page background | `#14130f` | 20, 19, 15 | 48° 14% 7% | — |
| `--bg-alt` | Raised band / card | `#1c1b16` | 28, 27, 22 | 50° 12% 10% | 1.08:1 *(surface)* |
| `--ink` | Primary text, titles | `#ece8dc` | 236, 232, 220 | 45° 30% 89% | **15.17:1** ✓ AAA |
| `--ink-soft` | Secondary text | `#b8b3a2` | 184, 179, 162 | 46° 13% 68% | **8.86:1** ✓ AAA |
| `--ink-mute` | Captions, metadata | `#807c70` | 128, 124, 112 | 45° 7% 47% | 4.46:1 ⚠︎ AA large; ~AA normal |
| `--rule` | Hairlines, dividers | `#2c2a23` | 44, 42, 35 | 47° 11% 15% | 1.29:1 *(non-text)* |

> **Flag — `ink-mute`.** Light `#8a877f` (3.41:1) and dark `#807c70` (4.46:1) are reserved for
> **metadata, captions, and timestamps at ≥ 16px**, never long-form body copy. For body text use
> `ink-soft` or `ink` — both clear AAA.

---

## 3. Accent — master + five category hues

The **master accent is Restaurant rust `#a8431a`** (light) / `#d97757` (dark). It is the default when a
category is ambiguous. Each category provides a **light/dark pair**; you only ever swap this one value.

| Category | Light HEX | RGB · HSL | On paper | On paper-alt | Dark HEX | On bg | On bg-alt |
|---|---|---|---|---|---|---|---|
| **Restaurant** *(master)* | `#a8431a` | 168,67,26 · 17° 73% 38% | **5.73** ✓ | 5.29 ✓ | `#d97757` | **5.95** ✓ | 5.52 ✓ |
| **Hike** | `#3f6b3a` | 63,107,58 · 114° 30% 32% | **5.91** ✓ | 5.46 ✓ | `#5d8a52` | 4.62 ✓ | 4.29 ✓ large |
| **Spa / Stay** | `#2f6b6b` | 47,107,107 · 180° 39% 30% | **5.80** ✓ | 5.36 ✓ | `#4f9a9a` | 5.68 ✓ | 5.27 ✓ |
| **Event** | `#6b3a5d` | 107,58,93 · 317° 30% 32% | **8.35** ✓ AAA | 7.71 ✓ | `#9a5d86` | 3.79 ⚠︎ | 3.52 ⚠︎ |
| **City / Walk** | `#3a5a6b` | 58,90,107 · 201° 30% 32% | **6.99** ✓ | 6.45 ✓ | `#5d86a0` | 4.76 ✓ | 4.42 ✓ large |

**Accent-soft (master):** light `#c96b3e` (3.53:1 on paper — ⚠︎ large/UI only) · dark `#e89878`
(8.14:1 on bg — ✓ AAA). Soft is a hover/secondary tone for the accent, never body text on light.

> **Flag — Event dark accent `#9a5d86` (3.79:1).** Passes AA for **large text (≥ 24px), the category
> bar, the `·` dots, and the mark** — all of which is how the accent is used. It **fails AA for normal
> inline links on dark.** Fix: on dark, render Event links at the body size **with an underline** (the
> underline is the affordance, not the color), or step links to `ink` and reserve the hue for the
> underline + large type. The same underline-on-dark rule is applied site-wide for safety.

All five **light** accents clear **AA normal (≥ 4.5)** on both paper and paper-alt — links, dots, and
bars are safe in the primary light theme without caveat.

---

## 4. Usage rules

- **One accent per asset.** Pick by category. Never mix two category hues in one composition.
- Accent appears only on: **the mark, the `·` dots, the category bar, and links/active states.**
  Never as a fill, never as a page background, never behind text.
- Ink is for type and the mark's mono variants. Rule is for hairlines only (1px).
- Surfaces step paper → paper-alt (light) / bg → bg-alt (dark). Never more than two surface levels.
- Dark theme is a true sibling, not an inversion: warm near-blacks, never pure `#000`.

---

## 5. The rule for adding a new category hue

1. Choose a hue at roughly **L 30–32% / S 28–40%** for the light value and **L 43–50% / S 25–32%**
   for the dark value (mirrors the existing five — muted, magazine-ink, never neon).
2. **Verify contrast:** light value **≥ 4.5:1 on `#faf9f6` and `#f2f0e9`**; dark value **≥ 4.5:1 on
   `#14130f`**. If the dark value lands 3.0–4.5, it is **large/UI-only** and links must be underlined
   (the Event exception).
3. Register both as a token pair in `03-color/tokens.css` (`--accent` / `--accent-soft`, themed) and
   add an `accent-soft` ~12–14% lighter (light) or lighter still (dark).
4. Give the category a line icon in the mark's 1.5px round-cap style.
5. Nothing else in the system changes.

*Swatch sheet: `swatches.svg`. Tokens: `../03-color/tokens.css`. Next: `type.md`.*

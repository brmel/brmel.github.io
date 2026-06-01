# Ibraverse — Type

Three families, no exceptions. A serif that does the talking, a neutral sans that gets out of the
way, and a mono that timestamps everything.

| Role | Family | Weights | Where |
|---|---|---|---|
| **Display** | Instrument Serif | 400 (+ italic) | Titles, oversized headlines — display only |
| **Body / UI** | Inter Tight | 400 · 500 · 600 | Paragraphs, UI, captions, buttons |
| **Mono / data** | JetBrains Mono | 400 · 500 | Eyebrows, labels, metadata, the wordmark's data line |

Load (Google Fonts):
```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

---

## 1. Type scale — desktop (≥ 1024px)

Base = 16px = 1rem. Display uses **Instrument Serif**; everything else as noted.

| Token | Use | Font | px / rem | Line-height | Weight | Tracking |
|---|---|---|---|---|---|---|
| `display-xl` | Hero title | Instrument Serif | **88 / 5.5** | 0.98 (86) | 400 | −0.02em |
| `display-l` | Cover title | Instrument Serif | **64 / 4.0** | 1.00 (64) | 400 | −0.015em |
| `display-m` | Article title | Instrument Serif | **48 / 3.0** | 1.04 (50) | 400 | −0.01em |
| `display-s` | Card / section title | Instrument Serif | **34 / 2.125** | 1.08 (37) | 400 | −0.005em |
| `heading` | UI heading | Inter Tight | **24 / 1.5** | 1.25 (30) | 600 | −0.01em |
| `subhead` | Sub-heading / lede | Inter Tight | **20 / 1.25** | 1.40 (28) | 500 | 0 |
| `body-l` | Long-form body | Inter Tight | **18 / 1.125** | 1.62 (29) | 400 | 0 |
| `body` | Default body / UI | Inter Tight | **16 / 1.0** | 1.60 (26) | 400 | 0 |
| `caption` | Captions, footnotes | Inter Tight | **13 / 0.8125** | 1.45 (19) | 400 | 0.005em |
| `eyebrow` | The eyebrow label | JetBrains Mono | **12 / 0.75** | 1.30 (16) | 500 | **0.12em**, UPPERCASE |
| `data` | Meta, timestamps, tags | JetBrains Mono | **13 / 0.8125** | 1.40 (18) | 400 | 0.04em |
| `micro` | Legal, fine print | JetBrains Mono | **11 / 0.6875** | 1.40 (15) | 400 | 0.06em |

## 2. Responsive — tablet (640–1023px) & mobile (< 640px)

Display steps down with a fluid clamp; body holds. Eyebrow never goes below **11px** or its 0.12em
tracking collapses.

| Token | Desktop | Tablet | Mobile | Fluid `clamp()` |
|---|---|---|---|---|
| `display-xl` | 88 | 64 | 44 | `clamp(2.75rem, 1.6rem + 5.8vw, 5.5rem)` |
| `display-l` | 64 | 48 | 36 | `clamp(2.25rem, 1.5rem + 3.8vw, 4rem)` |
| `display-m` | 48 | 38 | 30 | `clamp(1.875rem, 1.35rem + 2.6vw, 3rem)` |
| `display-s` | 34 | 30 | 26 | `clamp(1.625rem, 1.35rem + 1.4vw, 2.125rem)` |
| `heading` | 24 | 22 | 20 | `clamp(1.25rem, 1.1rem + 0.8vw, 1.5rem)` |
| `subhead` | 20 | 19 | 18 | `clamp(1.125rem, 1.05rem + 0.4vw, 1.25rem)` |
| `body-l` | 18 | 18 | 17 | `clamp(1.0625rem, 1rem + 0.3vw, 1.125rem)` |
| `body` | 16 | 16 | 16 | `1rem` |
| `eyebrow` | 12 | 12 | 11 | fixed (don't fluid the tracking) |

> **Minimums.** Slide / cover renders never below **24px** of rendered type. Print never below **12pt**.
> Mobile body never below **16px** (prevents iOS zoom-on-focus).

---

## 3. Setting rules

**Instrument Serif (display).**
- Set **tight**: negative tracking as in the table, line-height ≤ 1.08.
- **Optically balance** multi-line titles — break for sense, hang no orphan, keep the last line ≥ 2 words.
- Use the **italic** only for a single emphasized word or a place name inside a title, never whole lines.
- Titles are 3–7 words. If it needs more, it's a subhead, not a title.

**Inter Tight (body/UI).**
- Measure **60–75 characters** for long-form (`body-l`, ~`--container-text` 720px).
- 600 for UI emphasis and buttons; 500 for ledes and labels; 400 for running text.
- `text-wrap: pretty` on paragraphs; `text-wrap: balance` on headings.

**JetBrains Mono (eyebrow/data).**
- The eyebrow is **always uppercase, 0.12em** tracking. The `·` separators carry the **accent**.
- Numbers are tabular by default (Mono is monospaced) — good for the `№ 004` field-note index.
- Never set body copy in Mono. It is signage and data only.

---

## 4. The eyebrow, exactly

```
FIELD NOTE № 004 · RESTAURANT · OLD MONTREAL
└──────────┘ └─┘   └────────┘   └──────────┘
 fixed lead   idx    CATEGORY      PLACE/REGION
 ink-soft    ink     ink           ink-mute
              the · dots are ACCENT, 12px, 0.12em, uppercase
```

- `FIELD NOTE №` and the title-case structure are fixed; only `idx / CATEGORY / PLACE` change.
- Index zero-padded to **3 digits**. Dots are U+00B7 with one space either side.
- Color split: lead + index + category in `ink` (or `ink-soft` on busy photos), place in `ink-mute`,
  the `·` dots in `accent`. On a photo, set the whole eyebrow in paper/ink-on-band, never over the image.

*Live specimen: `specimen.html`. Next: `spacing-grid.md`.*

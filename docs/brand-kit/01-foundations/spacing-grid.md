# Ibraverse — Spacing, Grid & Tokens

Everything aligns to an **8-point grid**. Type, margins, gaps, component padding, and safe-zones are
all multiples of 8 (with a 4px half-step for tight optical work). If a number isn't on the scale,
it's a mistake.

---

## 1. Spacing scale (8pt)

| Token | px | rem | Typical use |
|---|---|---|---|
| `space-0` | 0 | 0 | reset |
| `space-1` | 4 | 0.25 | icon ↔ label, hairline insets (half-step) |
| `space-2` | 8 | 0.5 | tight stacks, chip padding |
| `space-3` | 12 | 0.75 | eyebrow ↔ title, list gaps |
| `space-4` | 16 | 1.0 | default gap, card padding (mobile) |
| `space-5` | 24 | 1.5 | block spacing, card padding |
| `space-6` | 32 | 2.0 | section sub-gaps |
| `space-7` | 48 | 3.0 | section spacing, band padding |
| `space-8` | 64 | 4.0 | major sections |
| `space-9` | 96 | 6.0 | hero band, page top/bottom |
| `space-10` | 128 | 8.0 | full-bleed breathing room |

---

## 2. Containers

| Token | Max-width | Use |
|---|---|---|
| `container-text` | **720px** | Long-form article body (60–75ch at 18px) |
| `container-content` | **960px** | Article header, recommendation lists, default page |
| `container-wide` | **1200px** | Galleries, contact sheet, dashboards |
| `container-full` | **1440px** | Edge-to-edge layouts, banners |

Gutters: **24px** mobile · **48px** tablet · **96px** desktop (all on-grid).

## 3. Web grid — 12 columns

- **12 columns**, 24px gutter, max content 1200px.
- Tablet collapses to **8 columns**, mobile to **4 columns**.
- Article = text centered in `container-text`; media may break out to `container-content`.
- Reels row = 3 equal columns (1fr each), 16px gap, at the article foot.

```css
.grid-12{display:grid;grid-template-columns:repeat(12,1fr);gap:24px;
  max-width:1200px;margin-inline:auto;padding-inline:clamp(24px,6vw,96px)}
@media (max-width:1023px){.grid-12{grid-template-columns:repeat(8,1fr)}}
@media (max-width:639px){.grid-12{grid-template-columns:repeat(4,1fr);gap:16px}}
```

---

## 4. Social & print safe-zones

All vertical social is **1080×1920 (9:16)**. Keep all type and the mark inside the **center 80%**.

| Frame | Size | Safe margin (each side) | Safe box |
|---|---|---|---|
| 9:16 vertical | 1080×1920 | **108px** L/R (10%), **120px** top, **160px** bottom | 864×1640 |
| 4:5 post | 1080×1350 | 64px all sides | 952×1222 |
| 1:1 post | 1080×1080 | 64px all sides | 952×952 |
| Story UI-safe | 1080×1920 | **250px top** (clock/handle), **320px bottom** (caption/CTA UI) | center band |
| OG / share | 1200×630 | 64px all sides | 1072×502 |
| YouTube banner | 2560×1440 | **title-safe 1546×423**, centered | see `05-channels` |

- The **mark** sits at the **top-left of the safe box**, not the frame edge.
- The **category bar** spans the safe-box width (or full-bleed bottom on covers — see component specs).
- Never place readable type outside the safe box; photos may bleed to the frame edge.

---

## 5. Radii

| Token | px | Use |
|---|---|---|
| `radius-xs` | 4 | tags, inline chips |
| `radius-sm` | 8 | buttons, badges, small cards |
| `radius-md` | **14** | **the photo frame** (canonical), large cards |
| `radius-lg` | 20 | feature panels, modals |
| `radius-pill` | 999 | pills, the play button |

## 6. Hairlines & borders

| Token | Value | Use |
|---|---|---|
| `hairline` | 1px solid `--rule` | dividers, card edges, table rules |
| `hairline-strong` | 1.5px solid `--ink` | the mark stroke, emphasis underlines |
| `category-bar` | **4px** solid `--accent` | the category bar (the one accent rule) |
| `focus-ring` | 2px solid `--accent`, 2px offset | keyboard focus |

## 7. Shadows (used sparingly — this is a paper brand)

| Token | Value | Use |
|---|---|---|
| `shadow-none` | none | default (flat, print-like) |
| `shadow-card` | `0 1px 2px rgba(24,23,21,.04), 0 2px 8px rgba(24,23,21,.06)` | raised card on paper |
| `shadow-pop` | `0 4px 12px rgba(24,23,21,.10), 0 12px 32px rgba(24,23,21,.10)` | menus, the play button hover |
| `shadow-photo` | `0 2px 8px rgba(24,23,21,.08)` | the 14px photo frame |

Dark theme shadows use `rgba(0,0,0,.4)` at the same offsets. Prefer **rule borders over shadows** —
shadows are the exception, not the texture.

## 8. Texture tokens (optional, from the protocol)

- `--grain`: a 2% opacity paper-grain PNG/SVG noise, multiply-blended on `--paper`. Off by default.
- `--hairline-grid`: a 32px × 32px 1px `--rule` grid at 6% opacity, for contact sheets and editorial
  backgrounds only. Never behind body copy.

*Tokens in code: `../03-color/tokens.css` and `../06-web/tokens.css`. Next: `voice-tone.md`.*

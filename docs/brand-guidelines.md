# Brand

The visual brand of the whole site: Home, Resume, Projects, Tech, Adventures. Values come from
`assets/css/extended/00-tokens.css` and `layouts/partials/brand/mark.html`; where this file and the
code disagree, the code is right and this file gets fixed. How the copy sounds is in
[voice.md](voice.md); the reasons behind these rules are in [decisions.md](decisions.md).

## 1. Idea

An engineer who ships, documents honestly, and explores. Every page shows work one person built,
ran and measured, says what didn't work, and is laid out like a calm print magazine: warm paper,
ink-black type, one accent, a compass mark. The idea describes the person, so a machine-vision
article, an Algerian transit app and a hike all sit on the same site.

## 2. Signature

Three elements appear on every asset.

1. **The compass-aperture mark**: concentric circles and four N/S/E/W ticks. One implementation,
   `layouts/partials/brand/mark.html`; never inline or redraw it.

   | Placement | Size | Colour |
   |---|---|---|
   | Nav logo, every page | 22px | `--accent` |
   | Site footer, every page | 18px | `--ink-mute` at 70% |
   | Social cards, end-cards | large, centred | `--accent` |

   Never inside body copy, as a bullet or spinner, twice on one screen, or in another colour.

2. **The eyebrow**: letterspaced mono caps with accent `·` separators, from
   `layouts/partials/func/eyebrow.html`.

   | Where | Grammar | Example |
   |---|---|---|
   | Field note | `FIELD NOTE № {nnn} · {CATEGORY} · {PLACE}` | `FIELD NOTE № 004 · HIKE · ADIRONDACKS` |
   | Project page | `PROJECT № {nn} · {DOMAIN} · {STATUS}` | `PROJECT № 01 · SAAS · SHIPPED` |
   | Project index card | `№ {nn} · {YEAR} · {DOMAIN} · {STATUS}` | `№ 11 · 2026 · DATA · IN PROGRESS` |
   | Article page, list card | `{DATE} · {READ LENGTH}` | `1 JUNE 2026 · 6 MIN` |
   | Resume | `{LOCATION}` | `MONTRÉAL, QUÉBEC` |
   | Career period | `{YEARS}` | `2024 — PRESENT` |

   Every label is translated (`№` is `رقم` in Arabic). Dates render through `time.Format
   ":date_long"`, so month names follow the language. Read length shows only from 2 minutes.

3. **One accent**: the mark, the eyebrow dots, the category bar and links. Never a filled
   background, never plain text that is not a link.

## 3. Colour

Paper, ink and one accent. Light is the default theme.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--bg` | `#faf9f6` | `#14130f` | page background |
| `--bg-alt` | `#f2f0e9` | `#1c1b16` | cards, wells |
| `--ink` | `#181715` | `#ece8dc` | headings, body |
| `--ink-soft` | `#4a4843` | `#b8b3a2` | secondary text |
| `--ink-mute` | `#6e6c65` | `#888477` | captions, eyebrows |
| `--rule` | `#d9d6cb` | `#2c2a23` | hairlines, borders |
| `--accent` | `#a8431a` | `#d97757` | mark, links, dots |
| `--accent-soft` | `#c96b3e` | `#e89878` | hovers |
| `--ink-gain` / `--ink-loss` | `#0a4fd0` / `#c1121f` | `#58a9ff` / `#ff5c5c` | PariData results only |

- Browser chrome (`theme_color`) is paper, `#faf9f6`.
- Gain and loss colours encode a result, so they may tint the surface that carries it (a ledger row,
  a result card, the area under a curve). They never paint a heading, link, rule or the mark.
  Secondary text on a tint uses `--ink-soft`; `--ink-mute` drops below AA there.
- Every text colour clears 4.5:1 on both backgrounds in both themes, syntax colours included.
  `scripts/checks/check-contrast.py` enforces it.

## 4. Type

Loaded once from `layouts/partials/head/fonts.html`. Never add a family.

| Role | Face | Notes |
|---|---|---|
| Titles | Instrument Serif | large and tight |
| Body and UI | Inter Tight 400/500/600 | |
| Eyebrows, labels, data, code | JetBrains Mono | uppercase, `0.12em` tracking on labels |
| Arabic script | IBM Plex Sans Arabic 400/600 | downloads only for Arabic characters; labels switch to it with normal tracking |

| Token | Size | Use |
|---|---|---|
| `--fl-display-m` | 30–48px, fluid | every page title |
| `--t-display-s` | 34px | big numbers: project metrics, field-note rating |
| `--t-heading` | 24px | card, feed and search-result titles |
| `--t-subhead` | 20px | page descriptions, names in author and resume cards |
| `--prose-size` | 18–21px, fluid | article body |
| `--t-body-l` | 18px | body text outside articles |
| `--t-body` | 16px | card descriptions, UI text |
| `--t-caption` | 14px | captions, breadcrumbs, secondary lines |
| `--t-eyebrow` | 12px (14px in Arabic) | eyebrows, chips, stack lines, labels: the floor |

Every size is in `rem`, so a reader's browser font size scales the whole page. Nothing renders under
12px.

## 5. Sections

| Section | Exists to | Chrome |
|---|---|---|
| Home | say who this is, show the career, route into the work | profile, career strip, "Start here", section cards, latest |
| Resume | the career on one page | career timeline, skills, certifications |
| Projects | things built end to end, with what went wrong | eyebrow, stack chips, status, metrics, gallery, lessons |
| Tech | explain something learned by doing it | article layout, figures, series box |
| Adventures | honest first-person notes on places | eyebrow, verdict block |
| Topics | every page on one subject | grouped topic list, topic chips on each page |

A page that fits none of these has no home yet. The nav skips a section with no published pages.

## 6. Locked elements

| Element | Rule |
|---|---|
| Mark | `layouts/partials/brand/mark.html` only, in `--accent` or `--ink-mute` |
| Handle | `@ibraverse` on YouTube, Instagram and TikTok, all linking to ibraverse.ca |
| Eyebrow | the grammar in §2 |
| Fonts | the four faces in §4 |
| Colour | defined in `00-tokens.css` only; one accent |
| Images | in the page bundle: `cover.jpg`, `gallery/NN-name.jpg`, `NN-name.jpg` for figures |

## 7. Languages

| Tier | Pages | Languages |
|---|---|---|
| Structural | home, resume, section indexes, search, nav, UI strings | English, French, Arabic, always |
| Long-form | projects, articles, field notes | English; translated one page at a time |

A reader never sees less because of their language: lists merge untranslated English pages in,
labelled "in English" / "en anglais" / «بالإنجليزية». Arabic is RTL and is checked on screen, not
assumed. The mechanics are in [ARCHITECTURE.md](../ARCHITECTURE.md#languages).

## 8. Social cards and assets

- **Article cover** (`cover.jpg`, horizontal, about 1200px): one clear subject, no text in the image.
  It is the list thumbnail and the page's social card.
- **Open Graph cards** (`static/og/<section>.jpg`, 1200×630) come from one template,
  `scripts/generate/og-cards.html`, cut by `scripts/generate/gen-og-cards.py`. A page shares its
  cover, else its first gallery image, else its section card, else the home card
  (`layouts/partials/func/og-image.html`); `scripts/checks/check-og.py` fails a page without one.
- **Social formats** (thumbnails, reels, carousels, channel art) are in [brand-kit/](brand-kit/00-README.md).

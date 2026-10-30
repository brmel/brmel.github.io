# Brand

The visual brand of the whole site: Home, Resume, Projects, Tech, Adventures. Values come from
`assets/css/00-tokens.css` and `layouts/_partials/brand/mark.html`; where this file and the
code disagree, the code is right and this file gets fixed. How the copy sounds is in
[voice.md](voice.md); the reasons behind these rules are in [decisions.md](decisions.md).

## 1. Idea

A developer who ships, documents honestly, and explores. Every page shows work one person built,
ran and measured, says what didn't work, and is laid out calmly in the manner of Google's own
products: white and neutral grey surfaces, one sans-serif face, large borderless cards, few lines, generous space,
one accent, a compass mark. The idea describes the person, so a machine-vision
article, an Algerian transit app and a hike all sit on the same site.

## 2. Signature

Three elements appear on every asset.

1. **The compass-aperture mark**: concentric circles and four N/S/E/W ticks. One implementation,
   `layouts/_partials/brand/mark.html`; never inline or redraw it (the standalone generator pages in
   `scripts/generate/` are the one exception).

   | Placement | Size | Colour |
   |---|---|---|
   | Nav logo, every page | 22px | `--accent` |
   | List card with no image | 64px, centred on a `--bg-alt` thumbnail | `--accent` |
   | Social cards | large, centred | `--accent` |

   Never inside body copy, as a bullet or spinner, or in another colour.

2. **The eyebrow**: one short sentence-case line above a title, in `--ink-mute`, with `·`
   separators, from `layouts/_partials/func/eyebrow.html` and `article/meta.html`.

   | Where | Grammar | Example |
   |---|---|---|
   | Field note | `{Category} · {Place} · {Date} · {Read length}` | `Hike · Adirondacks · June 1, 2026 · 6 min` |
   | Project page and card | `{Year} · {Status}` | `2026 · In progress` |
   | Article page and card | `{Date} · {Read length}` | `June 1, 2026 · 6 min` |
   | Career period | `{Month Year} — {Month Year}`; years alone for a degree | `Aug 2026 — Present` |

   Every label is translated. Dates render through `time.Format ":date_long"`, so month names
   follow the language. Read length shows only from 2 minutes.

3. **One accent**: the mark, links, buttons and the card placeholder tint. Never plain text that is
   not a link.

## 3. Colour

Neutral surfaces, near-black ink and one accent. Light is the default theme.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--bg` | `#ffffff` | `#131314` | page and card background |
| `--bg-alt` | `#f1f3f4` | `#1e1f20` | wells, table heads, thumbnails |
| `--ink` | `#1f1f1f` | `#e3e3e3` | headings, body |
| `--ink-soft` | `#444746` | `#c4c7c5` | secondary text |
| `--ink-mute` | `#5f6368` | `#9aa0a6` | captions, eyebrows |
| `--rule` | `#dadce0` | `#3c4043` | hairlines, card outlines |
| `--accent` | `#a8431a` | `#e2876a` | mark, links, buttons |
| `--ink-gain` / `--ink-loss` | `#0a4fd0` / `#c1121f` | `#58a9ff` / `#ff5c5c` | PariData results only |

- Browser chrome (`theme_color`) is white, `#ffffff`.
- Gain and loss colours encode a result, so they may tint the surface that carries it (a ledger row,
  a result card, the area under a curve). They never paint a heading, link, rule or the mark.
  Secondary text on a tint uses `--ink-soft`; `--ink-mute` drops below AA there.
- Every text colour clears 4.5:1 on both backgrounds in both themes, syntax colours included.
  `scripts/checks/check-contrast.py` enforces it.

## 4. Type

Loaded once from `layouts/_partials/head/fonts.html`. Never add a family.

| Role | Face | Notes |
|---|---|---|
| Titles, body, labels, data | Inter Tight 400/500/600 | titles 500 with tight tracking; labels in sentence case |
| Code | JetBrains Mono | code blocks and inline code only |
| Arabic script | IBM Plex Sans Arabic 400/600 | downloads only for Arabic characters |

| Token | Size | Use |
|---|---|---|
| `--fl-display-l` | 36–64px, fluid | the owner's name on the home page |
| `--fl-display-m` | 30–48px, fluid | every other page title |
| `--t-display-s` | 34px | big numbers: project metrics, field-note rating |
| `--t-heading` | 24px | section headings, career roles |
| `--t-subhead` | 20px | page descriptions and card titles |
| `--prose-size` | 18–21px, fluid | article body |
| `--t-body-l` | 18px | body text outside articles |
| `--t-body` | 16px | card descriptions, UI text |
| `--t-caption` | 14px | eyebrows, captions, chips, secondary lines |
| `--t-eyebrow` | 12px (14px in Arabic) | dense data labels in PariData: the floor |

Every size is in `rem`, so a reader's browser font size scales the whole page. Nothing renders under
12px.

## 5. Sections

Every list (section index, project index, home) uses the same card.

| Section | Exists to | Chrome |
|---|---|---|
| Home | say who this is, route into the work | one profile card (name, role, intro, photo), "Start here" cards |
| Resume | the career on one page | career timeline, skills, certifications |
| Projects | things built end to end, with what went wrong | eyebrow, stack chips, status, metrics, gallery |
| Tech | explain something learned by doing it | article layout, figures, series box |
| Adventures | honest first-person notes on places | eyebrow, verdict block |

A page that fits none of these has no home yet. The nav skips a section with no published pages.

## 6. Locked elements

| Element | Rule |
|---|---|
| Mark | `layouts/_partials/brand/mark.html` only, in `--accent` |
| Eyebrow | the grammar in §2 |
| Fonts | the faces in §4 |
| Colour | defined in `00-tokens.css` only; one accent |
| Images | in the page bundle: `cover.jpg`, `gallery/NN-name.jpg`, `NN-name.jpg` for figures |

## 7. Languages

| Tier | Pages | Languages |
|---|---|---|
| Structural | home, resume, section indexes, nav, UI strings | English, French, Arabic, always |
| Long-form | projects, articles, field notes | English; translated one page at a time |

A reader never sees less because of their language: lists merge untranslated English pages in,
labelled "in English" / "en anglais" / «بالإنجليزية». Arabic is RTL and is checked on screen, not
assumed. The mechanics are in [ARCHITECTURE.md](../ARCHITECTURE.md#languages).

## 8. Social cards and assets

- **Article cover** (`cover.jpg`, horizontal, about 1200px): one clear subject, no text in the image.
  It is the list thumbnail and the page's social card. A page with no photo of its own gets a flat
  illustration of its subject: a neutral or muted ground, the accent for the one thing that matters,
  no text, and an `alt` that starts with "Illustration:".
- **Open Graph cards** (`static/og/<section>.jpg`, 1200×630) come from one template,
  `scripts/generate/og-cards.html`, cut by `scripts/generate/gen-og-cards.py`. A page shares its
  cover, else its first gallery image, else its section card, else the home card
  (`layouts/_partials/func/og-image.html`); `scripts/checks/check-og.py` fails a page without one.

# Ibraverse — Brand System

The single source of truth for the **visual and verbal brand of the whole site**:
Home, Resume, Projects, Tech, Adventures, Thoughts. One identity, flexed per
content type by a single accent.

> Feed this file to a design tool alongside any prompt so every asset — covers,
> thumbnails, social cards, decks — comes out on-brand. Every value below is
> **extracted from the live code**, specifically
> [`assets/css/extended/tokens.css`](../assets/css/extended/tokens.css) and
> [`layouts/partials/brand-mark.html`](../layouts/partials/brand-mark.html) —
> not invented. Where this document and the CSS ever disagree, **the CSS wins
> and this file is wrong**.

---

## 1. Brand idea

> **An engineer who ships, documents honestly, and explores.**

Three things are always true, whatever the page is about:

- **Built, not described.** Everything here was made, run, and measured by one
  person. Numbers come from data that was actually collected.
- **Honest about the parts that didn't work.** One real con builds more trust
  than five pros. A project page with no scars is marketing.
- **Editorial, not corporate.** Laid out like a quietly confident print
  magazine: warm paper, ink-black type, one accent, a compass mark. Calm, not
  loud.

That idea has to cover a machine-vision article, an Algerian transit app, and a
hike in the Adirondacks without any of them feeling like a different website.
It does, because it describes the *person*, not the subject.

> **Status:** proposed by the #8 rewrite and in use across the site. Change the
> sentence here and every section register below has to be re-checked against it.

---

## 2. The hook (signature, reproducible motif)

Three elements appear on **every** asset. They are the brand — reproducible by
rule, recognisable in one frame:

1. **The compass-aperture mark** — concentric circles + 4 ticks (N/S/E/W). One
   implementation only:
   [`layouts/partials/brand-mark.html`](../layouts/partials/brand-mark.html).
   Never inline a second copy; never redraw it.

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

2. **The eyebrow label** — letterspaced mono caps, always the same grammar, with
   accent-coloured `·` separators:

   | Section | Grammar | Example |
   |---|---|---|
   | Adventures | `FIELD NOTE № {nn} · {CATEGORY} · {PLACE}` | `FIELD NOTE № 004 · HIKE · ADIRONDACKS` |
   | Projects | `PROJECT № {nn} · {DOMAIN} · {STATUS}` | `PROJECT № 01 · SAAS · SHIPPED` |
   | Any list card | `{DATE} · {READ LENGTH}` | `1 JUNE 2026 · 6 MIN` |
   | Career period | `{YEARS}` | `2024 — PRESENT` |

   Two rules the eyebrow follows everywhere:

   - **The date is localised.** It renders through `time.Format` with
     `:date_long`, never Go's `.Format`, which prints English month names
     on every language.
   - **Read length appears only when it is true.** Hugo counts words in the
     markdown, so a page whose body is one embedded artefact reported
     "1 MIN" for 13,000px of report. Under two minutes it is the date alone.

   On a project *index* card the word `PROJECT` is dropped: the page is the
   project index, so it would repeat on every card. It stays on the project
   page itself, where it is the only thing naming the section.

3. **One accent, used sparingly** — the mark, the eyebrow dots, the category
   bar, links. Never a filled background.

Layout is the same every time: mark top-left, eyebrow beside it, big serif title
under, image fills the rest.

### Where the mark appears

| Placement | Size | Colour |
|---|---|---|
| Nav logo (every page) | 22px | `--accent` |
| Site footer (every page) | 18px | `--ink-mute` at 70% opacity |
| Social cards / end-cards | large, centred | `--accent` |

**Never**: inside body copy, as a bullet, as a loading spinner, more than once
on one screen, or in any colour that is not `--accent` or `--ink-mute`. The home
hero used to carry a 40px mark directly under the nav's 22px one — the same
signature twice within one screen height, which reads as a logo stacked on a
logo rather than as a mark. The nav carries it there now.

---

## 3. Colour

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

Browser chrome (`theme_color`, `msapplication_TileColor`) is `#faf9f6` — paper,
not PaperMod's default slate.

### The category accent system

Coherence = everything keeps **paper + ink + the type system**; only the accent
hue swaps per content type, at the same saturation and value every time. Rust
stays the master/home accent. The mechanism is a single CSS rule in
`tokens.css` — `[data-category="…"]` reassigns `--accent` and nothing else.
There is no second colour system anywhere on this site.

**Adventures**

| Category | Light | Dark |
|----------|-------|------|
| Restaurant / Food | `#a8431a` rust (master) | `#d97757` |
| Hike / Trail | `#3f6b3a` forest | `#5d8a52` |
| Spa / Stay | `#2f6b6b` teal | `#4f9a9a` |
| Event | `#6b3a5d` plum | `#a76e95` |
| City / Walk | `#3a5a6b` slate | `#5d86a0` |

**Projects** — `domain:` in front matter sets these.

| Domain | Light | Dark | Use for |
|--------|-------|------|---------|
| `saas` | `#3a3f6b` indigo | `#7d84c4` | products with customers, admin portals, licensing |
| `mobile` | `#8a5a12` ochre | `#d0a05a` | phone-first apps |
| `data` | `#5a6b2f` olive | `#9ab562` | collection, analysis, reporting |
| `infra` | `#6b2f3a` burgundy | `#c47d8a` | backends, pipelines, control planes |

Adding a category = pick one mid-saturation hue at the same value, add both
theme variants and the `[data-category]` rule, **and check contrast** (below).

### Contrast is a gate, not a preference

Every accent must clear **4.5:1** against `--bg` in the theme it ships in. All
nine currently do; the dark plum was lightened from `#9a5d86` (3.79:1) to
`#a76e95` (4.70:1) for exactly this reason. Check before committing a hue:

```python
def lum(h):
    h = h.lstrip('#'); r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def ratio(a, b):
    l1, l2 = sorted((lum(a), lum(b)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)

ratio('#a76e95', '#14130f')   # 4.70 -> passes
```

---

## 4. Type

Loaded once site-wide — `extend_head.html` for PaperMod pages,
`brand-fonts.html` for the standalone layout. Reuse; never add a family.

| Role | Font | Notes |
|------|------|-------|
| Display / titles | **Instrument Serif** | editorial headline serif; large, tight |
| Body / UI | **Inter Tight** | 400/500/600 |
| Eyebrows / labels / data / code | **JetBrains Mono** | uppercase, letterspaced `0.12em` |

Scale: oversized serif title, small mono eyebrow above it, comfortable Inter
Tight body. Generous line-height, lots of paper. Tokens: `--t-display-*`,
`--t-body*`, `--t-eyebrow`, `--t-micro`, `--fl-display-*` for fluid sizes.

**One rank, one size.** Every single page — article, project, field note,
resume — opens at `--fl-display-m`; a section index opens one step down. This
was three sizes until the audit: an article title was 64px because
`44-adventures.css` styled `.post-single .post-title`, which is every single
page on the site, from a file scoped to one section.

**`--t-micro` is the floor.** Chips, stack lines and language markers were
written as raw 9, 10, 10.5 and 11px across six stylesheets — four sizes doing
one job, two of them below the size the contrast audit was run at.

---

## 5. Section register

What each section is for, and which brand elements it uses. A new page that
doesn't fit one of these rows doesn't have a home yet — decide before building.

| Section | It exists to | Accent | Chrome |
|---|---|---|---|
| **Home** | Say who this is, show the career, then route into the work | rust (master) | hero band, career strip, section cards, latest posts |
| **Resume** | The career, in one page | rust | career timeline, skills, certifications |
| **Projects** | Show things built end-to-end, with the lessons | per `domain:` | eyebrow, stack chips, status, gallery |
| **Tech** | Explain something learned by doing it | rust | article layout, figures |
| **Adventures** | Honest first-person reviews of places | per `category:` | eyebrow, verdict block, reel row |
| **Thoughts** | Reflection — shorter, no artefact required | rust | plain article, no cover |

**Layout-driven chrome is the rule.** In Adventures and Projects the eyebrow,
verdict, chips, status and reel row all render from front matter. You write only
prose. That is why those sections stay consistent — consistency is
constructed, not remembered. Any new section follows the same rule.

**Empty sections hide themselves.** `layouts/partials/header.html` skips a menu
entry whose section has no published pages, so the nav can never point at an
empty-state card.

---

## 6. Voice

Honest, curious, specific. First person. Short paragraphs. No hedging, no
throat-clearing, no words that would not survive being read aloud.

| Section | Voice notes |
|---|---|
| Projects | What problem, for whom, why you built it, what it became. Never copy README prose — a README is written for contributors, a project page for someone who has never heard of it. Lessons include at least one real failure. |
| Tech | Teach one thing properly. Show the real image, the real measurement, the real code. |
| Adventures | One genuine con per piece. A recommendation nobody could disagree with is not a recommendation. |
| Thoughts | Reflection earned from something you actually did. No general advice. |
| Resume | Facts, verifiable, no adjectives you would not defend in an interview. |

---

## 7. Locked elements (never improvise)

| Element | Lock |
|---------|------|
| Mark | `partials/brand-mark.html` only, in `--accent` or `--ink-mute` |
| Handle | `@ibraverse` on YouTube / IG / TikTok → all link to ibraverse.ca |
| Eyebrow grammar | per §2 table |
| Fonts | Instrument Serif / Inter Tight / JetBrains Mono only |
| Accent rule | one accent per page, chosen by `category:` / `domain:` (§3) |
| Colour source | `tokens.css`. No hex outside it, ever |
| Contrast | ≥ 4.5:1 accent-on-background, checked before commit |
| File names | `cover.jpg`, `ig-thumb.jpg`, `tt-thumb.jpg`, `photo-N.jpg` |
| Tone | honest, curious, specific — one genuine con per piece |

---

## 8. Language

The site ships English, French and Arabic (RTL) under a **tiered policy**:

| Tier | What | Languages |
|---|---|---|
| **Structural** | Home, Resume, section indexes, nav, all UI strings | **all three, always** |
| **Long-form** | Project write-ups, tech articles, field notes, Thoughts | **English by default**; translate individually when it earns it |

The rule that makes this honest: **a reader never sees less because of their
language.** Section listings *merge* rather than filter —
`partials/func/section-pages.html` returns this language's pages plus any
default-language pages that have no translation here, and the untranslated ones
are labelled *in English* / *en anglais* / *بالإنجليزية* on the card.

So `/fr/tech/` lists all three tech articles: the one translated into French, in
French, and the two English-only ones, marked. Filtering instead of merging is
what made `/fr/projects/` empty, which then hid Projects from the French nav
entirely — the French site silently contained less than the English one.

Consequences worth knowing:

- A page listed from the fallback links to its **English URL**. That is
  deliberate: it is an English page, and pretending otherwise by minting a
  French URL for English content is worse.
- New UI strings go in `i18n/{en,fr,ar}.yaml` in all three at once. Hugo
  resolves the flat `key: value` form here — the nested go-i18n `other:` form
  silently returns empty and falls through to the English default.
- Translating a long-form page means adding `index.fr.md` beside `index.md` in
  the same page bundle. The merge notices and stops showing the English one.

Two rules that predate the policy and still hold:

- The language switcher must never offer a language that does not exist for the
  current page. PaperMod's nav switcher points at each language's **home**, so
  it cannot dead-end; `partials/translation_list.html` only renders when a
  translation actually exists.
- Arabic is RTL and must be **checked**, not assumed: nav, breadcrumbs,
  eyebrows, galleries and timelines all have to mirror. Numeric ranges need
  isolating (`dir="ltr"`) or they render backwards.

---

## 9. Asset templates

Same template every time — swap photo, accent, and words.

**Article cover / hero — `cover.jpg`** (horizontal, ~1600px)
Photo full-bleed; paper band with mark + eyebrow + serif title overlaid or below.

**Social / reel thumbnails — `ig-thumb.jpg` / `tt-thumb.jpg`** (9:16, 1080×1920)
Paper background, photo in a rounded frame, compass mark top-left, eyebrow, 3–5
word title in Instrument Serif, thin accent bar at the bottom. Text in the
**centre 80%** safe zone — platform UI covers the top 10% and bottom 20%.

**Reel end-card** (9:16)
Paper, large compass mark centred, `ibraverse.ca`, `@ibraverse`, accent bar.

**Reels row (on-site)** — the `reels` shortcode renders YouTube + Instagram +
TikTok as one row of click-to-load vertical thumbnails at the bottom of an
Adventures article. Platform badge colours are the only non-brand colours
allowed anywhere on the site, and only on those badges.

**Open Graph cards** — `static/og/<section>.jpg`, 1200×630, six sections from
**one** template (`scripts/og-cards.html`, cut by `scripts/gen-og-cards.py`).
Six hand-designed cards would drift; one template cannot. Adding a section means
editing the template and the `SECTIONS` list, not drawing an image.

Which card a page shares is resolved in one place,
`layouts/partials/func/og-image.html`, first hit wins:

1. the page's own `cover.image`
2. a project's first `gallery/` screenshot — a real product shot beats a
   generated card
3. the section card
4. the home card

`og:` and `twitter:` read the same resolver, so they cannot disagree — upstream
PaperMod let them fall back differently. `scripts/check-og.py` runs locally and
in CI and fails the build if any page ships an og:image that is missing,
relative, unresolvable, or has no alt text.

The built kit lives in [`docs/brand-kit/`](brand-kit/) — proofs, channel assets,
and exported tokens. Regenerate rather than hand-editing.

---

## 10. Related documents

| File | Covers |
|---|---|
| [`adventures-playbook.md`](adventures-playbook.md) | How to publish an Adventures field note end-to-end |
| [`projects-playbook.md`](projects-playbook.md) | How to publish a Project page end-to-end |
| [`standalone-layout.md`](standalone-layout.md) | The full-page layout for self-contained articles |
| [`brand-kit/`](brand-kit/) | Generated proofs, channel assets, exported tokens |

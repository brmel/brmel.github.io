# Ibraverse — Brand System

The single source of truth for the **visual and verbal brand of the whole site**:
Home, Resume, Projects, Tech, Adventures, Thoughts. One identity, flexed per
content type by a single accent.

> Feed this file to a design tool alongside any prompt so every asset — covers,
> thumbnails, social cards, decks — comes out on-brand. Every value below is
> **extracted from the live code**, specifically
> [`assets/css/extended/00-tokens.css`](../assets/css/extended/00-tokens.css) and
> [`layouts/partials/brand/mark.html`](../layouts/partials/brand/mark.html) —
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
   [`layouts/partials/brand/mark.html`](../layouts/partials/brand/mark.html).
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
   | Project index card | `№ {nn} · {YEAR} · {DOMAIN} · {STATUS}` | `№ 11 · 2026 · DATA · IN PROGRESS` |
   | Article page, any list card | `{DATE} · {READ LENGTH}` | `1 JUNE 2026 · 6 MIN` |
   | Resume | `{LOCATION}` | `MONTRÉAL, QUÉBEC` |
   | Career period | `{YEARS}` | `2024 — PRESENT` |

   Every label is translated (`FIELD NOTE`, `PROJECT`, the domain and status words, and
   `№`, which is `رقم` in Arabic). The eyebrow sits between the breadcrumbs and the
   title in the one page header (`partials/page-head/header.html`); a field note puts
   its date line under the description.

   Two rules the eyebrow follows everywhere:

   - **The date is localised.** It renders through `time.Format` with
     `:date_long`, never Go's `.Format`, which prints English month names
     on every language.
   - **Read length appears only when it is true.** Hugo counts words in the
     markdown, so a page whose body is one embedded artefact reported
     "1 MIN" for 13,000px of report. Under two minutes it is the date alone.

   On a project *index* card the word `PROJECT` is dropped: the page is the
   project index, so it would repeat on every card. It stays on the project
   page itself, where it is the only thing naming the section. The year is on
   the card because the index is one grid, not a timeline of year groups.

3. **One accent, used sparingly** — the mark, the eyebrow dots, the category
   bar, links. Never a filled background, and never plain text that is not a
   link: metric values, skill labels and verdict answers are ink.

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
logo rather than as a mark. The resume head and the project eyebrow did the same
until the page headers were unified. The nav carries it there now.

---

## 3. Colour

Warm-editorial. Paper + ink + a single accent. Light is the home theme.

| Token | Light | Dark | Use |
|-------|-------|------|-----|
| `--bg` (paper) | `#faf9f6` | `#14130f` | page background |
| `--bg-alt` | `#f2f0e9` | `#1c1b16` | cards, wells |
| `--ink` | `#181715` | `#ece8dc` | headings, body |
| `--ink-soft` | `#4a4843` | `#b8b3a2` | secondary text |
| `--ink-mute` | `#6e6c65` | `#888477` | captions, eyebrows |
| `--rule` | `#d9d6cb` | `#2c2a23` | hairlines, borders |
| `--accent` | `#a8431a` | `#d97757` | mark, links, dots |
| `--accent-soft` | `#c96b3e` | `#e89878` | hovers, fills |

Browser chrome (`theme_color`, `msapplication_TileColor`) is `#faf9f6` — paper,
not PaperMod's default slate.

### One accent, everywhere

`--accent` is rust — `#a8431a` light, `#d97757` dark — on every page of the
site, in both themes. There is no second colour system and no per-page hue.

**This replaced a category accent system** (removed September 2026). Nine hues
used to reassign `--accent` from a `[data-category="…"]` rule: five for
Adventures categories, four for project `domain:` values. Each page was
internally coherent and the set was contrast-checked, but the site as a whole
had nine accents, so a visitor moving from one project to the next saw the brand
colour change under them. Recognition across pages is worth more than
wayfinding within one, and category is already stated in words by the eyebrow
(`№ 05 · DATA · SHIPPED`), which survives colour-blindness and greyscale print
as colour does not.

If a future section genuinely needs to be told apart by colour, scope the hue to
a small badge — never to `--accent`, which paints headings, links, rules and
bars across the whole page.

**Data colour is not accent.** `--ink-gain` (blue) and `--ink-loss` (red) encode
a result, so they may tint the surface that carries it — a ledger row, a result
card, the area under a curve — in PariData. They never paint a heading, a link,
a rule or the mark, and secondary text on a tinted surface uses `--ink-soft`:
`--ink-mute` drops below AA on every tint.

### Contrast is a gate, not a preference

Every colour must clear **4.5:1** against `--bg` in the theme it ships in, and
`check-contrast.py` fails the build if one does not. Check before committing a
hue:

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

Loaded once site-wide from `head/fonts.html`. Reuse; never add a family.

| Role | Font | Notes |
|------|------|-------|
| Display / titles | **Instrument Serif** | editorial headline serif; large, tight |
| Body / UI | **Inter Tight** | 400/500/600 |
| Eyebrows / labels / data / code | **JetBrains Mono** | uppercase, letterspaced `0.12em` |

Scale: oversized serif title, small mono eyebrow above it, comfortable Inter
Tight body. Generous line-height, lots of paper. Tokens: `--t-display-*`,
`--t-body*`, `--t-eyebrow`, `--t-micro`, `--fl-display-*` for fluid sizes.

**One rank, one size.** Every page header — section index, article, project,
field note, resume — opens at `--fl-display-m`. This
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
| **Projects** | Show things built end-to-end, with the lessons | rust | eyebrow, stack chips, status, gallery |
| **Tech** | Explain something learned by doing it | rust | article layout, figures |
| **Adventures** | Honest first-person reviews of places | rust | eyebrow, verdict block |
| **Thoughts** | Reflection — shorter, no artefact required | rust | plain article, no cover |

**Layout-driven chrome is the rule.** In Adventures and Projects the eyebrow,
verdict, chips and status all render from front matter. You write only
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
| Mark | `partials/brand/mark.html` only, in `--accent` or `--ink-mute` |
| Handle | `@ibraverse` on YouTube / IG / TikTok → all link to ibraverse.ca |
| Eyebrow grammar | per §2 table |
| Fonts | Instrument Serif / Inter Tight / JetBrains Mono; IBM Plex Sans Arabic for Arabic script only (the three Latin faces have no Arabic glyphs) |
| Accent rule | one accent, site-wide: `--accent` (§3) |
| Colour source | `00-tokens.css`. No hex outside it, ever |
| Contrast | ≥ 4.5:1 accent-on-background, checked before commit |
| File names | `cover.jpg`, `photo-N.jpg` |
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

- The language switcher must never dead-end. It goes to the current page's
  translation when one exists and to that language's home otherwise.
- Arabic is RTL and must be **checked**, not assumed: nav, breadcrumbs,
  eyebrows, galleries and timelines all have to mirror. Numbers and amounts are
  isolated left-to-right; anything with words in it (a period like
  `2024 — الآن`, a long date) uses a plain `<bdi>`, which picks its own
  direction — forcing `dir="ltr"` on it renders it backwards.

---

## 9. Asset templates

Same template every time — swap photo, accent, and words.

**Article cover — `cover.jpg`** (horizontal, ~1200px)
The list thumbnail (shown at 100px) and the page's social card. One clear subject, no text in
the image: the title is rendered beside it.

**Social / reel thumbnails — `ig-thumb.jpg` / `tt-thumb.jpg`** (9:16, 1080×1920)
Paper background, photo in a rounded frame, compass mark top-left, eyebrow, 3–5
word title in Instrument Serif, thin accent bar at the bottom. Text in the
**centre 80%** safe zone — platform UI covers the top 10% and bottom 20%.

**Reel end-card** (9:16)
Paper, large compass mark centred, `ibraverse.ca`, `@ibraverse`, accent bar.

**Open Graph cards** — `static/og/<section>.jpg`, 1200×630, six sections from
**one** template (`scripts/generate/og-cards.html`, cut by `scripts/generate/gen-og-cards.py`).
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
PaperMod let them fall back differently. `scripts/checks/check-og.py` runs locally and
in CI and fails the build if any page ships an og:image that is missing,
relative, unresolvable, or has no alt text.

Social templates, logo files and channel art live in [`docs/brand-kit/`](brand-kit/).

---

## 10. Related documents

| File | Covers |
|---|---|
| [`adventures-playbook.md`](adventures-playbook.md) | How to publish an Adventures field note end-to-end |
| [`projects-playbook.md`](projects-playbook.md) | How to publish a Project page end-to-end |
| [`brand-kit/`](brand-kit/) | Logo, social templates, channel art, photo and voice guides |

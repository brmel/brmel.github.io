# Screen audit — August 2026

> **Resolved 2026-08-09.** Every defect below is fixed and the fixes are gated.
> Final sweep: 23 screens × 2 viewports × 3 languages, zero violations of the
> checklist. Four rules — one `h1`, a skip link, sized images, no image under
> `static/` — are now enforced by `scripts/`, each verified by seeding the
> defect and watching the gate fail. This file is kept as the record of what
> was wrong and why; see the commit log from `Fix D1` onward for each change.

Every route in the built site, checked screen by screen against one checklist.
97 real pages (aliases and paginator stubs excluded), 12 screen archetypes,
3 languages, 2 themes, 2 viewports.

Method: structural pass over `public/**/index.html` for chrome, metadata and
heading structure; Playwright pass at 1440×900 and 390×844, light and dark, for
layout, journeys and computed accessibility properties.

---

## 1. The checklist

Applied to every screen. A screen passes a row or it appears in §3.

### Branding, theme, design, language

- [ ] Brand mark in the header, single implementation, `currentColor`
- [ ] Type scale from tokens — serif display, sans body, mono eyebrow
- [ ] Every colour resolves to `00-tokens.css`; no local hex
- [ ] Accent follows `[data-category]`, never hard-coded per page
- [ ] Light and dark both legible; no element defined only in one theme
- [ ] Eyebrow grammar consistent (`№ NN · DOMAIN · STATUS`)
- [ ] Casing consistent — chrome is uppercase mono, prose is sentence case
- [ ] `lang` and `dir` correct on `<html>`; RTL mirrors through logical properties
- [ ] Every visible string comes from `i18n/`, not the template
- [ ] Voice matches `docs/brand-guidelines.md` — first person, specific, no filler

### Layout

- [ ] Content column and rhythm identical to sibling screens
- [ ] Grids fill their rows or degrade to a deliberate shape
- [ ] No orphan card, no letterboxed image, no visible dead space
- [ ] Images carry `width`/`height`; nothing shifts on load
- [ ] 390 px: no horizontal scroll, no clipped chip row
- [ ] Long content reflows rather than truncating mid-word

### Buttons and controls

- [ ] Every control has an accessible name
- [ ] Hit target ≥ 24×24 CSS px (WCAG 2.5.8)
- [ ] Focus ring visible on every focusable element
- [ ] External links carry `rel="noopener noreferrer"`
- [ ] Hover and active states defined once, in `20-components.css`

### Return / back

- [ ] Breadcrumb from any page deeper than root
- [ ] "Back to {Section}" in the content footer
- [ ] Previous/next siblings where a section has more than one page
- [ ] Back-to-top present and reachable by keyboard
- [ ] No screen that can only be left with the browser's back button

### Contribute

- [ ] "Improve this page" → GitHub edit view on the right branch and path
- [ ] "Found a problem?" → prefilled issue carrying title and URL
- [ ] Comments block present or deliberately inert
- [ ] Share row on anything worth sharing

### Scrolling

- [ ] No horizontal overflow at any breakpoint
- [ ] Sticky elements do not cover the scroll target
- [ ] Below-fold images lazy, above-fold images eager
- [ ] Long pages carry in-page navigation or a back-to-top

### UI / UX journeys

- [ ] Entry from nav, from search engine, and from a shared link all land coherently
- [ ] Nav offers nothing the destination cannot deliver
- [ ] Every published route is reachable from at least one link
- [ ] No published route is empty
- [ ] The recruiter path — home → resume → projects → project → back — never dead-ends

### Files, folders, architecture

- [ ] One page bundle per article or project; assets travel with their page
- [ ] Images in `assets/` or a bundle, never `static/`
- [ ] Chrome renders from front matter, not hand-written markup
- [ ] No partial, shortcode, stylesheet or asset without a live consumer
- [ ] Cascade order explicit; section files compose primitives, never redeclare
- [ ] Every rule that matters is enforced by a script in `scripts/`

---

## 2. Screen inventory and verdict

| # | Screen | Routes | Brand | Layout | Buttons | Back | Contribute | Scroll | Journey |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Home | `/`, `/fr/`, `/ar/` | pass | **fail** | warn | n/a | n/a | pass | **fail** |
| 2 | Resume | `/resume/` ×3 | pass | warn | warn | pass | pass | pass | pass |
| 3 | Projects index | `/projects/` ×3 | pass | pass | pass | pass | n/a | pass | pass |
| 4 | Project single | 6 pages | pass | pass | warn | pass | pass | pass | pass |
| 5 | Tech index | `/tech/` ×3 | pass | warn | pass | pass | n/a | pass | pass |
| 6 | Article single | 9 pages | pass | pass | pass | pass | pass | pass | **fail** |
| 7 | Thoughts index | `/thoughts/` ×3 | pass | pass | pass | pass | n/a | pass | pass |
| 8 | Thought single | 1 page | pass | pass | pass | pass | pass | pass | pass |
| 9 | Adventures index | `/adventures/` ×3 | pass | pass | pass | pass | n/a | pass | **fail** |
| 10 | Standalone report | 1 page | **fail** | pass | warn | warn | pass | pass | **fail** |
| 11 | Tags | index ×3 + 58 terms | pass | pass | pass | warn | n/a | pass | warn |
| 12 | 404 | 1 page | warn | **fail** | n/a | **fail** | n/a | pass | **fail** |

Clean across every screen: `lang`/`dir`, `<title>`, meta description, canonical,
`og:image` with alt text, `header`/`nav`/`main`/`footer` landmarks, zero images
without `alt`, zero `target="_blank"` without `rel="noopener"`, zero console
errors, zero horizontal overflow at 390 px, and both themes legible.

---

## 3. Defects

### D1 — French and Arabic home pages advertise a site that isn't there

`/fr/` and `/ar/` render **two** section cards (Tech, CV) where `/` renders four,
and **one** latest entry where `/` renders five. The nav on those same pages
links to Projects and Thoughts. A French visitor sees a nav promising four
sections and a home page that knows about two.

This is the bug already fixed once for section listings. `partials/func/section-pages.html`
merges this language's pages with untranslated default-language ones;
`home-sections.html` and `home-latest.html` never adopted it and still filter.

**Fix:** route both partials through `func/section-pages.html`.

### D2 — 404 is a dead end

No `h1`, no message, no links out — a 72 px numeral on an empty page. Anyone
arriving from a stale link, and every crawler, hits a screen with nothing to do.
The site has one dead end and this is it.

**Fix:** heading, one sentence, links to Home / Projects / Tech.

### D3 — The report page leaves the site

`/tech/hydro-quebec-outage-analysis/` is the standalone layout: no site nav, no
brand mark, no site footer, no back-to-top, and **no `h1` at all** — 13,653 px of
scroll with zero headings in the document outline. Its content footer renders,
but from a CSS bundle that omits the chrome rules, so "← Back to Tech" and
"Improve this page" appear in sentence case where every other screen shows them
uppercase mono.

It is also the single best artefact on the site for a recruiter, and the only
page that looks like it belongs to a different project.

**Fix:** give it an `h1`, add the chrome rules to `standalone-bundle`, and put
the brand mark and site nav in its top bar.

### D4 — Adventures is published, empty and orphaned

`/adventures/` renders "No Adventures Published Yet." in three languages. It is
in no nav, linked only from its own translations, and its two posts are drafts.
Cost of keeping it: 2.8 MB of content, 12 photos, `44-adventures.css` (169 lines),
`45-reels.css` (122 lines), the `reels` shortcode and partial (49 lines) — all
serving zero published pages. The `reels` shortcode has **zero uses** in
published content.

**Fix:** publish the two drafts, or drop the section and its stylesheets.

### D5 — Every article shows its tags twice

Header renders `· tagged: C++, Windows, Memory Management, Sysinternals, Systems`
and the content footer renders the same five as chips. Both are layout-driven, so
this repeats on all nine articles.

**Fix:** drop tags from `post_meta.html`; the content footer already owns them.

### D6 — Two `h1` on one article

`/tech/image-histograms/` repeats its title as a body heading. `h1=2` there,
`h1=0` on the report; every other content page is exactly one.

**Fix:** demote the body heading; add the count to `check-chrome.py`.

### D7 — Breadcrumbs are inconsistent

Present on projects, tech, thoughts, adventures and tag terms. Absent on Resume
and on the Tags index — both of which are one level below root, like the pages
that have them.

### D8 — Tag pages leak section headings into summaries

`/tags/flutter/` shows *"The story The moment matters more than the mechanism…"*.
Hugo's auto-summary swallows the first `##`. Affects every project on every tag
page it appears on.

**Fix:** a `summary` in project front matter, or `.Description` in the entry template.

### D9 — Home grid leaves an orphan

Four section cards in a three-column grid: three across, Resume alone underneath.
Resume's card also carries the eyebrow "THE SHORT VERSION" where the other three
carry "N ENTRIES" — two different card grammars in one row. In the Latest list,
the first row shows a summary and the remaining four show title only.

### D10 — No skip link anywhere

Zero pages carry a skip-to-content link. Keyboard and screen-reader users
traverse the full nav on every page (WCAG 2.4.1).

### D11 — Touch targets below 24 px

18 focusable elements under 24×24 on a project page, 12 on the resume, 5 on home
— the share icons, social row and language switcher. WCAG 2.5.8, and it is felt
on a phone.

### D12 — Smaller items

| | |
|---|---|
| Resume | one image with no `width`/`height` → CLS; heading order jumps `h1 → h3` |
| Resume | no share row, on the page most likely to be shared |
| Tech index | thumbnails are 100×100 `object-fit: contain` — mixed sources letterbox |
| Tags | 36 of 50 tags have exactly one post; each is a page linking to one thing |
| `<html>` | `dir="auto"` on en/fr where `ltr` is meant |
| Agentic SEO | `llms.txt` and `llms-full.txt` still missing — flagged in `site-audit-2026-08.md`, never built |

---

## 4. Files, folders, architecture

Clean, and verified rather than assumed:

- No unused partial. Every one of the 26 has a live consumer.
- `i18n` parity exact — 37 keys in each of en, fr, ar, no extras, no gaps.
- Numbered cascade holds; no colour outside `00-tokens.css`.
- Every asset is referenced; `check-orphans.sh` passes.
- One page bundle per article and project.

Four things that are not clean:

1. **`static/images/timeline/` — 9 files, 212 KB.** README states images live in
   `assets/` or a bundle, never `static/`, so they pass through the pipeline.
   These bypass it: no WebP, no `srcset`, no fingerprint. The convention is
   documented and unenforced.
2. **`assets/reports/hydro-quebec-outage.html` — 1.4 MB, one file.** 24 % of
   `assets/`, and it is a build artefact under version control.
3. **`content/` is 6.1 MB, 2.8 MB of it drafts** (D4).
4. **`reels` shortcode, partial and stylesheet — 171 lines, zero published uses** (D4).

---

## 5. Order of work

| | Item | Why first |
|---|---|---|
| 1 | **Deploy** | 25 commits sit unpushed; ibraverse.ca still serves the old site, so nothing below is visible either way |
| 2 | D1 French/Arabic home | Two of three languages misrepresent the site |
| 3 | D2 404 | The only dead end |
| 4 | D3 report chrome | Best artefact, worst-integrated screen |
| 5 | D5, D6, D7, D8 | Consistency defects, each a small edit |
| 6 | D10, D11, D12 CLS | Accessibility, and each is enforceable by a gate |
| 7 | D4 Adventures | Decide: publish or delete |
| 8 | D12 `llms.txt` | Agentic SEO, still outstanding |

Gates to add so these cannot recur: `h1 == 1` per content page, skip link
present, no image without dimensions, no image under `static/`.

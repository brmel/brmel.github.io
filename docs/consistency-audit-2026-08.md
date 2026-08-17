# Consistency audit — August 2026

A second pass over the whole site, after the career-timeline rebuild. Where
`screen-audit-2026-08.md` asked *"does every screen work"*, this one asks
*"does every screen agree with the others"* — language, type, spacing, chrome,
and the code behind them.

Method: a structural scan over all 72 built pages (headings, eyebrow strings,
titles, dates, link targets, `lang`/`dir`, raw CSS values, i18n parity), then a
screen-by-screen pass at 1280×900 and 390×844 in both themes and all three
languages.

Everything in §1 is fixed. §2 is open, with a recommendation each.

---

## 1. Fixed

### Language

| | |
|---|---|
| **Dates were English in every language.** `/fr/` and `/ar/` printed "August 4, 2026" on every card, article and the learning block — the one string on those pages that never translated. `DateFormat` was a Go layout (`January 2, 2006`), which hard-codes English month names, and two call sites used `.Format` instead of `time.Format`. | `DateFormat = ":date_long"`, called through `time.Format`. Now *4 août 2026* · *٤ أغسطس ٢٠٢٦*. |
| **"How I Fixed an IA Algorithm in Scikit-Learn."** `IA` is the French acronym; the article is in English. | → `AI`. |
| **Montreal / Montréal, Quebec / Québec.** Eight unaccented spellings in Adventures and one Tech article, against accented ones everywhere else including the resume and the home subtitle. | Normalised to `Montréal` / `Québec`. |
| **Empty-state text was written in the template.** `_default/list.html` said "No {section} published yet." in English on all three language sites, and promised "new field notes" whatever the section was. | Through `i18n`, generic wording. |
| **The verdict block's four labels** were hard-coded English. | Through `i18n`. |

### Type and spacing

| | |
|---|---|
| **One rank, three sizes.** An article title rendered at 64px, a project title at 48px, a section index at 40px. The 64px came from `44-adventures.css` styling `.post-single .post-title` — a section file setting the type of every single page on the site. | Rules moved to `50-content.css`; every single page opens at `--fl-display-m`. |
| **Four sizes for the smallest type** — raw `9px`, `10px`, `10.5px`, `11px` in six stylesheets, two of them below the size the contrast audit was run at. | One `--t-micro` token. |
| **Five chip declarations for one component** — paddings of 1×8, 2×9, 3×10, 4×9 and 5×12px, three font sizes, two border treatments, in four files. | One `.u-chip` primitive in `20-components.css`; the section files add only what differs. |

### Layout

| | |
|---|---|
| **The date on a list card moved depending on how long the text was.** `.entry-cover` was floated, so an entry whose text ran taller than the 100px thumbnail dropped its meta line back to the left margin — two alignments in one list, decided by prose length. | The entry is two boxes now, a thumbnail column and a text column. |
| **The longest description was cut mid-word** ("…the data pipeline behind i…") while its neighbours showed theirs in full, from the theme's two-line clamp. | Clamp removed: these are authored descriptions, not machine summaries. |
| **Six nav items needed 403px inside a 375px scroller,** so *Thoughts* sat off-screen on a phone and only a sideways swipe found it. | Tighter gaps and a 14px label at ≤520px: all six fit. Wrapping was the other option and made the header 196px tall. |
| **The home hero was one full viewport** (PaperMod sizes `.profile` at `100vh` because upstream it is the only thing on the page) — 732px before a reader saw any work. | A band: photo one side, name the other. |

### Chrome and code

| | |
|---|---|
| **The projects index was the only section index with no feed link**, though it publishes `index.xml` like the others. | RSS link added. |
| **The standalone report's `<title>` used an em dash** where all 71 other pages use a pipe. | `\|`. |
| **`.report-frame` had two homes** — an inline `<style>` in the shortcode and `50-content.css`. | One home. |
| **A dead lightbox.** The image half of the resume lightbox — markup, CSS and a JS branch — became unreachable when the timeline stopped carrying plain images. | Removed. |
| **`.section-nav` was dropped site-wide.** `30-chrome.css:73` had lost the `/*` opening its section header, so the stray `*/` swallowed the next rule: no rule above "Back to…" on any content page. | Comment repaired. |
| **`.home-intro` had lost its selector**, so the home intro ran full width and left-aligned under a centred name. | Selector restored. |
| **A truncated reduced-motion block** in `42-timeline.css` (`.video-thumb,.video-thumb:hover,}`). | Repaired. |
| **`.profile__photo` was declared twice**, identically, in two files. | Once. |

---

### Content

**"What I am learning now" removed.** The continuous-learning block had two
halves: what each project taught (generated from `takeaway` front matter) and a
hand-maintained list of work in progress (`data/learning.yaml`). The second was
the only list on the site that could rot, needed a staleness warning in the
build to police it, and put unfinished work next to finished work on the page
that exists to show finished work. The block is now one list, under its own
heading, and `data/` is gone.

The six takeaways were rewritten at the same time: plain first person, no
project-internal vocabulary ("pillar", "web property"), and no two built on the
same sentence pattern.

---

## 2. Open

**Article title casing.** Eight of ten titles are Title Case, two are sentence
case ("How an image-processing feature saved my flight", "Five percent"). Both
are defensible; the mix is not. An editorial brand usually picks sentence case.
*Left alone: these are authored titles and the choice is the author's.*

**The report page is a different design system.** `/tech/hydro-quebec-outage-analysis/`
embeds a generated 1.4MB artefact with a white ground, a blue accent and a bold
sans — none of which exist anywhere else on this site. It is deliberately
iframed and documented as such, and it is also the best artefact here for a
recruiter. *Recommendation: regenerate the report with the site's tokens; the
palette is ~20 values in the generator.*

**Project pages show `stack` and `tags` on the same screen** — "TypeScript" and
"Firebase" appear in both rows. *Recommendation: drop tags from project pages;
`stack` is the honest list and the taxonomy still works from the tag pages.*

**Thumbnails on list cards are `object-fit: contain` at 100×100,** so a
wide diagram and a tall screenshot letterbox differently. Carried over from the
August audit. *Recommendation: crop to a square at build time, or accept it —
`contain` is right for diagrams, which must stay readable.*

**The 404's `<title>` is untranslated** on `/fr/` and `/ar/` (the body is
translated). It comes from Hugo's synthetic 404 page and PaperMod's `head.html`;
fixing it means forking that partial for one string. *Recommendation: leave it —
a 404 title is not indexed.*

**Three project galleries hold three screenshots in a two-column layout,**
which leaves a hole at the bottom right. *Recommendation: a fourth screenshot,
or accept the ragged edge that column layout gives.*

# Architecture

How the templates, stylesheets, content and scripts fit together. Rules for changing them are in
[AGENTS.md](AGENTS.md); the reasons behind them are in [docs/decisions.md](docs/decisions.md).

Chrome renders from front matter and from a page's place in the site: eyebrows, stack chips, status,
gallery, lessons, verdict, series box, original-source credit, page header and page ending. Authors
write prose; consistency comes from the templates.

## Repository

| Path | Holds |
|---|---|
| `content/` | one page bundle (markdown plus its images) per project, article and field note; `content/resume.md` and `content/search.md` with `.fr.md`/`.ar.md` twins; topic pages in `content/tags/` |
| `data/` | `data/paridata/` (PariData tickets, matches, profile) and `data/topics.yaml` (topic groups) |
| `archetypes/` | scaffolds for `hugo new`: projects, tech, adventures, default |
| `layouts/` | templates (below) |
| `assets/` | everything that goes through Hugo Pipes: `assets/css/extended/`, `assets/js/` (`timeline.js` resume video dialog, `paridata.js` ledger controls), `assets/images/` (profile photo, resume video posters named by YouTube ID), `assets/paridata/flags/`, `assets/reports/` (generated report pages) |
| `i18n/` | UI strings in `i18n/en.yaml`, `i18n/fr.yaml`, `i18n/ar.yaml` |
| `static/` | files served verbatim: favicons, `static/fonts/`, social cards in `static/og/`, `static/robots.txt`, `static/CNAME` |
| `scripts/` | build entry points, gates, audit and generators (below) |
| `themes/PaperMod/` | the vendored theme, unmodified |
| `.github/workflows/site.yml` | CI and deployment |
| `docs/` | brand, voice, playbooks, decisions, backlog, brand kit |
| `.claude/skills/` | agent skills; see [AGENTS.md](AGENTS.md) |

## Templates

| Path | Renders |
|---|---|
| `layouts/_default/baseof.html` | the page shell; a layout widens `<main>` to the frame with `{{ define "main-width" }} main--wide{{ end }}` |
| `layouts/_default/list.html` | the home page (profile, intro, career, featured, section cards, latest) and section indexes (featured, then every page) |
| `layouts/_default/single.html` | Tech articles and field notes |
| `layouts/_default/term.html` | one topic: every page carrying the tag, newest first, with its section named |
| `layouts/_default/terms.html` | `/tags/`: topics in the groups and order of `data/topics.yaml`, with page counts; tags in no group land in a trailing "More" group sorted by count |
| `layouts/_default/resume.html` | the resume, from front matter |
| `layouts/_default/search.html`, `layouts/_default/index.json` | the search page and its index |
| `layouts/_default/rss.xml` | feeds |
| `layouts/_default/single.markdown.md` | the markdown twin of every Tech and Adventures page |
| `layouts/_default/_markup/render-link.html` | external links open in a new tab |
| `layouts/projects/list.html` | the project index: one grid, highest `projectNo` first |
| `layouts/projects/single.html` | a project page |
| `layouts/projects/tracker.html` | PariData, from `data/paridata/` |
| `layouts/404.html` | the only 404 GitHub Pages serves, so it links the French and Arabic homes |
| `layouts/sitemap.xml` | indexable pages only, with `hreflang` and `x-default` |
| `layouts/index.llms.txt`, `layouts/index.llmsfull.txt` | `/llms.txt` and `/llms-full.txt` |
| `layouts/shortcodes/` | `figure` (a bundle image through the pipeline, with `srcset` and dimensions; a missing file fails the build), `gmap` (a link to a Google Maps search for `q`), `reportframe` (a report from `assets/reports/` rendered in place); the `*.markdown.md` files render these and `youtube` as links in the markdown output |

### Partials

A partial at the root of `layouts/partials/` has a name PaperMod or Hugo calls; everything written
for this site lives in the folder for its domain.

| Path | Holds |
|---|---|
| `layouts/partials/` (root) | `header.html` (menu skips sections with no pages; language switcher goes to the translation, else that language's home), `footer.html`, `index_profile.html`, `post_meta.html` (date, and read length from 2 minutes), `social_icons.html`; `extend_head.html` (CSP, `x-default`, fonts, JSON-LD), `extend_footer.html` (footer mark), `google_analytics.html` (GA4 after idle) |
| `layouts/partials/templates/` | Open Graph, Twitter card and `schema_json` (breadcrumb JSON-LD) |
| `layouts/partials/func/` | partials that `return` a value; call with `partial` and use the result |
| `layouts/partials/page-head/` | `header.html`, every page header: breadcrumbs, eyebrow, title, one description line (`pitch`, `role` or `description`), date line on field notes, optional `extra` block; called with `(dict "page" . "title" … "extra" …)` |
| `layouts/partials/page-end/` | `footer.html`, the one page ending: topic chips, "discuss this page" link, social icons, author card, section navigation |
| `layouts/partials/article/` | `entry.html` (a list card; takes `(dict "page" . "showSection" true)`), `cover.html` (list thumbnail; a missing cover fails the build), `origin.html` (series box), `original.html` (first-published credit), `related-project.html` |
| `layouts/partials/home/` | `career.html`, `sections.html`, and `featured.html` / `latest.html`, which take a list of pages |
| `layouts/partials/project/meta.html` | project links and stack chips |
| `layouts/partials/adventures/verdict.html` | the verdict block, rendered when `rating` is set |
| `layouts/partials/resume/` | `timeline.html`, `contact.html` (an icon shows only when the URL is also in `socialIcons`), `video-thumb.html` |
| `layouts/partials/paridata/` | dashboard, curve, ledger, amount, about |
| `layouts/partials/head/` | `fonts.html` (preloads), `schema.html` (JSON-LD per section) |
| `layouts/partials/brand/` | `mark.html` (the compass mark, the only implementation), `social-icon.html` |
| `layouts/partials/lang/en-only.html` | the "in English" label on an untranslated page listed in French or Arabic |

| `layouts/partials/func/` | Returns |
|---|---|
| `section-pages.html` | the pages a section or topic lists: this language's pages plus default-language pages with no translation here, matched by `.Path` |
| `main-pages.html` | `section-pages.html` over every section in `mainSections`, for the home page |
| `eyebrow.html` | a page's eyebrow line, by section |
| `dots.html` | a slice joined into one escaped string with the accent dot, each item in its own `<bdi>` so mixed-direction lists keep their order |
| `lang-attrs.html` | `lang`/`dir` attributes for a page listed in another language |
| `og-image.html`, `og-src.html` | the social card a page shares (cover, else first gallery image, else `static/og/<section>.jpg`, else the home card) and its file |
| `paridata-ledger.html` | the PariData tickets settled from match results; bad data fails the build |

### Theme forks

Fifteen files are forks of PaperMod, each with a one-line header naming the upstream path and commit
(`@2d2f2c6`): `layouts/404.html`, `layouts/_default/` `baseof.html` `list.html` `single.html`
`search.html` `index.json` `rss.xml`, `layouts/partials/` `header.html` `footer.html`
`index_profile.html` `post_meta.html` `social_icons.html`, and the three files in
`layouts/partials/templates/`. Diff each against the theme before upgrading it.

These share a theme or Hugo name, are written here from scratch, and carry no header:
`extend_head.html`, `extend_footer.html`, `google_analytics.html`, `shortcodes/figure.html`,
`_default/terms.html`, `_markup/render-link.html`, `sitemap.xml`.

## Stylesheets

PaperMod concatenates `assets/css/extended/*.css` in lexical order, so the number prefix is the
cascade. Every page loads the one bundle.

| File | Holds |
|---|---|
| `00-tokens` | design tokens, the only place a colour is defined; dark values under `.dark`; print and phone overrides |
| `05-fonts` | self-hosted `@font-face` declarations |
| `10-base` | theme variable remap, page frame and measure, page header, type, links, tables, code |
| `20-components` | shared primitives (`.u-card`, `.u-bar`, `.u-tile`, `.u-eyebrow`, `.u-meta`, `.u-dot`, `.u-link`, `.u-rule-link`, `.u-chip`, `.u-rows`, `.u-label-row`, `.u-rule-heading`, `.u-frame`, `.u-sr-only`) and anything a shared partial or shortcode renders |
| `30-chrome` | nav, mark, footers, section nav, page end |
| `31-toc`, `32-search` | table of contents, search box |
| `40-home` … `47-topics` | one section each: home, resume, timeline and video dialog, projects, adventures, PariData, project page, topics |
| `50-content` | article body: figures, diagrams, embedded reports |
| `60-print` | print, last in the cascade |

Section files compose the primitives and never redeclare them. `scripts/checks/check-css.py` fails
on a colour outside tokens, a redeclared primitive, a file over 260 lines, a file not named
`NN-name.css`, or a class no page, template or script uses. `scripts/checks/check-rtl.py` fails on a
physical property (`left`, `margin-right`, …).

### Page frame

Header, footer and `<main>` share the 1200px frame (`--container-content`). Every block inside a page
sits at that page's measure:

- by default the text measure, 900px (`--container-text`); grids reflow to it with `auto-fit`/`minmax`.
- the 1200px frame on pages whose body is a grid or a table, set with `main--wide`: the project index,
  the resume and PariData.

No block sets its own `max-width` or `margin-inline:auto`, nothing is sized from `100vw`, and space
between blocks is `margin-block` from `--flow-tight`, `--flow-block` and `--flow-section`. Rules sit
under section headings (`.u-rule-heading`) and at the page end, never in a page header.

## Content

One page bundle per project, article or field note, so images travel with the page and go through
Hugo's image pipeline. Section front matter is documented in the playbooks:
[projects](docs/projects-playbook.md), [field notes](docs/adventures-playbook.md),
[PariData](docs/paridata-playbook.md). Any project, article or field note can take `featured: N`, which
lists it under "Start here" on the home page (and on the Tech or Adventures index), lowest number
first.

A Tech or Adventures article declares `title`, `description`, `tags` and a `cover` (`image`, a file in
the bundle, and `alt`). `description` is the one line a reader sees on the list card, the home feed,
search, the meta description and JSON-LD. Optional fields:

| Field | Renders, in |
|---|---|
| `series`, `seriesPart` | the series box listing every part (`article/origin.html`) |
| `canonicalOriginal`, `canonicalOriginalName` | the "first published on" credit (`article/original.html`), inside the series box when there is one |
| `relatedProject` | a project card at the foot (`article/related-project.html`), by project slug |

The resume is front matter: `role`, `location`, `contact`, then `experience:` periods (`period`,
`role`, `org`, `url`, `note`, `kind: education` for degrees, `work` items with `title`, `url`, `text`,
`video`, `videoAlt`, then `built`, `stack`, `tools` and a markdown `learned` list), `skills` and
`certifications`. `layouts/partials/resume/timeline.html` renders the periods; the home career strip
and `llms.txt` read the same data.

A report is a Tech article: prose with every figure, then
`{{< reportframe src="reports/<file>.html" title="…" >}}`. The frame loads lazily; on load its
script maps the page's tokens onto the report's CSS variables (both themes), loads the site fonts,
hides the report's own nav and title, and patches its accessibility gaps. Report files and their
generators stay untouched.

### Topics

Each tag is a topic page at `/tags/<tag>/`, rendered by `layouts/_default/term.html` from
`layouts/partials/func/section-pages.html`. `content/tags/<tag>/_index.md` gives it a title and a
description (and `url:` where the tag is not URL-safe: `C++` is `/tags/cpp/`). `/tags/` groups topics
by `data/topics.yaml`: the order of `groups` is the order on the page, each group's heading is the i18n
key `topics_group_<key>`, and any tag not listed falls into the trailing "More" group automatically.
Topic chips at the foot of each page link the topic pages.

## Languages

English lives at the root, French under `/fr/`, Arabic (RTL) under `/ar/`. Structural pages (home,
resume, section indexes, search, UI strings) exist in all three; long-form pages are English unless
translated, by adding `index.fr.md` or `index.ar.md` to the bundle.

- Lists merge: `func/section-pages.html` returns this language's pages plus untranslated English
  ones, which keep their English URL, carry `lang="en"` and their own direction, and show the "in
  English" label. Section indexes, home feeds, section feeds, search, topic pages and `llms.txt` all
  use it.
- UI strings exist in all three `i18n/*.yaml` files at once. Plain strings are flat `key: "value"`;
  counted strings use plural forms (`one`/`other`, plus `zero`/`two`/`few`/`many` in Arabic).
- Numbers, currency placement and plurals come from i18n (`number_locale`, `currency_pattern`), and
  dates from `time.Format ":date_long"`.
- Arabic text renders in IBM Plex Sans Arabic. Text that mixes words and numbers (a period like
  `2024 — الآن`, a date) sits in a plain `<bdi>`; forcing `dir="ltr"` on it renders it backwards.

## Agents and search engines

- `static/robots.txt` allows everything except `/reports/`, whose content is in the article prose.
- `/llms.txt` lists the career, project facts and every section page; `/llms-full.txt` holds every
  page as plain text. Both are English-only.
- Tech and Adventures pages also publish `index.md` (cascade in `config.toml`), linked with
  `rel="alternate" type="text/markdown"`.
- JSON-LD by section: `TechArticle` (Tech), `BlogPosting` with `contentLocation` (Adventures),
  `SoftwareSourceCode` (Projects), plus the `Person` from the resume on every page.

## Configuration

`config.toml` holds languages, menus, `mainSections` (the sections the nav, home page, `llms.txt` and
gates treat as content), `socialIcons`, GA4, output formats and the markdown cascade. `socialIcons`
and every other plain `[params]` key stay above the first `[params.*]` sub-table: TOML assigns keys
written after a sub-table header to that sub-table.

## Scripts

| Path | Does |
|---|---|
| `scripts/check.sh` | builds into `public/` and runs `scripts/gates.sh` |
| `scripts/gates.sh` | the list of gates; each prints what it asserts |
| `scripts/checks/` | `gate.py` (paths, `config.toml`, page iterator, pass/fail) and one file per gate |
| `scripts/audit.py` | Lighthouse (11 pages, mobile and desktop) and a link crawl against a live or local site; fails under budget |
| `scripts/generate/gen-favicons.py` | favicons and `apple-touch-icon.png` from a 512px screenshot of `scripts/generate/favicon-src.html` |
| `scripts/generate/gen-og-cards.py` | `static/og/*.jpg` from a full-page screenshot of `scripts/generate/og-cards.html` at width 1200, one card per entry in its `SECTIONS` |

Generators run by hand and need Pillow; serve the HTML templates from the site root so they load
`/fonts`. Commit what they write.

## Deployment

`.github/workflows/site.yml` pins Hugo 0.148.0 extended, runs `scripts/check.sh` and an internal link
crawl on every pull request (plus an advisory external crawl), and on a push to `main` does the same,
then publishes `public/` to GitHub Pages.

# Architecture

How the templates, stylesheets, content and scripts fit together. Rules for changing them are in
[AGENTS.md](AGENTS.md); the reasons behind them are in [docs/decisions.md](docs/decisions.md).

Chrome renders from front matter and from a page's place in the site: eyebrows, stack chips, status,
gallery, lessons, verdict, series box, page header and list cards. Pages end with their content: no
author card, topic chips, social links or previous/next. Authors write prose; consistency comes from
the templates.

## Repository

| Path | Holds |
|---|---|
| `content/` | one page bundle (markdown plus its images) per project, article and field note; `content/resume.md` and `content/search.md` with `.fr.md`/`.ar.md` twins; topic pages in `content/tags/` |
| `data/` | `data/paridata/` (PariData tickets, matches, profile) and `data/topics.yaml` (topic groups) |
| `archetypes/` | scaffolds for `hugo new`: projects, tech, adventures, default |
| `layouts/` | templates (below) |
| `assets/` | everything that goes through Hugo Pipes: `assets/css/`, `assets/js/` (`search.js` search, `timeline.js` resume video dialog, `paridata.js` ledger controls), `assets/images/` (profile photo, resume video posters named by YouTube ID), `assets/paridata/flags/`, `assets/reports/` (generated report pages) |
| `i18n/` | UI strings in `i18n/en.yaml`, `i18n/fr.yaml`, `i18n/ar.yaml` |
| `static/` | files served verbatim: favicons, `static/fonts/`, social cards in `static/og/`, `static/robots.txt`, `static/CNAME` |
| `scripts/` | build entry points, gates, audit and generators (below) |
| `.github/workflows/site.yml` | CI and deployment |
| `docs/` | brand, voice, playbooks, decisions, backlog, brand kit |
| `.claude/skills/` | agent skills; see [AGENTS.md](AGENTS.md) |

## Templates

Hugo's current layout, with no theme: page templates at the root of `layouts/`, partials in
`layouts/_partials/`, shortcodes in `layouts/_shortcodes/`, render hooks in `layouts/_markup/`.

| Path | Renders |
|---|---|
| `layouts/baseof.html` | the page shell; a layout widens `<main>` to the frame with `{{ define "main-width" }} main--wide{{ end }}` |
| `layouts/list.html` | the home page (profile, intro, the `featured` cards), section indexes and topic pages: a card grid of every page, newest first (projects by highest `projectNo`; topic cards name their section) |
| `layouts/single.html` | Tech articles and field notes; punctuation right after an inline formula stays on the formula's line |
| `layouts/taxonomy.html` | `/tags/`: topics in the groups and order of `data/topics.yaml`, with page counts, each linking to its page in the reader's language when one exists; tags in no group land in a trailing "More" group sorted by count |
| `layouts/resume.html` | the resume, from front matter |
| `layouts/search.html`, `layouts/home.json` | the search page (`assets/js/search.js`) and its index: title, description, section, date and the first 2,000 characters of each page |
| `layouts/rss.xml` | feeds |
| `layouts/single.markdown.md` | the markdown twin of every Tech and Adventures page |
| `layouts/_markup/render-link.html` | external links open in a new tab |
| `layouts/_markup/render-passthrough.html` | LaTeX between `$$ … $$` (block) or `\( … \)` (inline) becomes MathML at build time through `transform.ToMath`; the markdown twin keeps the LaTeX |
| `layouts/projects/single.html` | a project page |
| `layouts/projects/tracker.html` | PariData, from `data/paridata/` |
| `layouts/404.html` | the only 404 GitHub Pages serves: a title and one sentence; the header's language switch links the French and Arabic homes |
| `layouts/sitemap.xml` | indexable pages only, with `hreflang` and `x-default` |
| `layouts/home.llms.txt`, `layouts/home.llmsfull.txt` | `/llms.txt` and `/llms-full.txt` |
| `layouts/_shortcodes/` | `figure` (a bundle image through the pipeline, with `srcset` and dimensions; a missing file fails the build), `gmap` (a link to a Google Maps search for `q`), `reportframe` (a report from `assets/reports/` rendered in place), `youtube` (a self-hosted poster from the bundle linking to the video, so nothing loads from YouTube until the reader clicks; takes `id`, `poster`, `title`); the `*.markdown.md` files render these as links in the markdown output |

### Partials

`head.html`, `header.html` and `footer.html` sit at the root of `layouts/_partials/` because
`baseof.html` calls them; everything else lives in the folder for its domain.

| Path | Holds |
|---|---|
| `layouts/_partials/head.html` | the CSP (first, since a meta CSP only covers what follows it), the dark-theme switch before first paint, title, description, canonical, the stylesheet bundle, icons, feeds, `hreflang` and Speculation Rules (prefetch same-site links on hover, except `/reports/`) |
| `layouts/_partials/head/` | `fonts.html` (preloads), `social.html` (Open Graph and the X card), `schema.html` (one JSON-LD `@graph` per page: the full `Person` on home and resume, a reference elsewhere, the page's own type and its breadcrumb), `analytics.html` (GA4 after idle, production only) |
| `layouts/_partials/header.html`, `footer.html` | the nav (theme toggle, shown only once its script runs; menu marks the current page and section with `aria-current` and skips sections with no pages; the language switch goes to the translation, else that language's index of the same section, else its home) and the footer, whose scripts drive the toggle and the browser-chrome colour and add the code copy button |
| `layouts/_partials/func/` | partials that `return` a value; call with `partial` and use the result |
| `layouts/_partials/page-head/` | `header.html`, every page header: one meta line (eyebrow, plus the date on Tech and Adventures pages), title, one description line (`pitch`, `role` or `description`), optional `extra` block; called with `(dict "page" . "title" … "extra" …)` |
| `layouts/_partials/article/` | `grid.html` (the card grid every list uses; takes `(dict "pages" … "showSection" true "level" 3 "eager" true)`, `level` the card heading level (2 by default), `eager` loading the first thumbnail with high priority), `entry.html` (one card, the same for articles, field notes and projects; an untranslated English page listed in French or Arabic keeps `lang`/`dir` and shows the "in English" label), `cover.html` (the 16:9 thumbnail from `func/cover.html`, else the compass mark), `meta.html` (date, and read length from 2 minutes), `toc.html` (the table of contents from 5 minutes, a `<details>` card), `series.html` (series box) |
| `layouts/_partials/home/` | `profile.html` (photo as AVIF with a WebP fallback, name, role line), `cards.html` (a headed card grid; takes `(dict "id" … "title" … "pages" …)`) |
| `layouts/_partials/project/meta.html` | project links and stack chips |
| `layouts/_partials/adventures/verdict.html` | the verdict block above the body, rendered when `rating` is set |
| `layouts/_partials/topic/related.html` | a topic page's header line: its page count and the four other topics its pages share most, translated when a translation exists |
| `layouts/_partials/resume/` | `timeline.html`, `video-thumb.html` |
| `layouts/_partials/paridata/` | dashboard, curve, ledger, amount, about |
| `layouts/_partials/brand/` | `mark.html` (the compass mark, the only implementation) |

| `layouts/_partials/func/` | Returns |
|---|---|
| `section-pages.html` | the pages a section or topic lists: this language's pages plus default-language pages with no translation here, matched by `.Path` |
| `main-pages.html` | `section-pages.html` over every section in `mainSections`, for the home page |
| `eyebrow.html` | a page's eyebrow line, by section |
| `title.html` | a page's display title: the owner's name on the home page, the not-found title on the 404, else the page title; used by `<title>`, `og:title` and the social image's alt |
| `dots.html` | a slice joined into one escaped string with the accent dot, each item in its own `<bdi>` so mixed-direction lists keep their order |
| `cover.html` | a page's picture and its alt text: the cover (a missing file fails the build), else the first gallery image ("<title> screenshot"), else nothing |
| `og-image.html` | the social card a page shares, with its real size: `cover.html` resized to at most 1200px, else `static/og/<section>.jpg`, else the home card |
| `paridata-ledger.html` | the PariData tickets settled from match results; bad data fails the build |

## Stylesheets

`layouts/_partials/head.html` concatenates the syntax colours (generated at build by
`css.ChromaStyles`, Catppuccin Macchiato) and `assets/css/*.css` in lexical order, so the number
prefix is the cascade, then minifies and fingerprints one bundle that every page loads.

| File | Holds |
|---|---|
| `00-tokens` | design tokens, the only place a colour is defined; dark values under `.dark`; print and phone overrides |
| `05-fonts` | self-hosted `@font-face` declarations |
| `10-base` | reset, page frame and measure, page header, type, links, code |
| `20-components` | shared primitives (`.u-card`, `.u-eyebrow`, `.u-dot`, `.u-heading`, `.u-link`, `.u-chip`, `.u-label-row`, `.u-frame`, `.u-sr-only`) and anything a shared partial or shortcode renders, including the list card and its grid |
| `30-chrome` | nav, mark, footer, series box, table of contents |
| `32-search` | search box |
| `40-home` … `47-topics` | one section each: home, resume, timeline and video dialog, adventures, PariData, project page, topics |
| `50-content` | article body: type scale, figures, diagrams, code |
| `60-print` | print, last in the cascade |

Section files compose the primitives and never redeclare them. `scripts/checks/check-css.py` fails
on a colour outside tokens, a redeclared primitive, a file over 260 lines, a file not named
`NN-name.css`, or a class no page, template or script uses. `scripts/checks/check-rtl.py` fails on a
physical property (`left`, `margin-right`, …).

### Page frame

Header, footer and `<main>` share the 1200px frame (`--container-content`). Every block inside a page
sits at that page's measure:

- by default the text measure, 900px (`--container-text`); grids reflow to it with `auto-fit`/`minmax`.
- the 1200px frame on pages whose body is a table or a timeline, set with `main--wide`: the resume
  and PariData. Card grids stay at the text measure, two cards a row.

No block sets its own `max-width` or `margin-inline:auto` (a single paragraph may cap its line length in `ch`), nothing is sized from `100vw`, and space
between blocks is `margin-block` from `--flow-tight`, `--flow-block` and `--flow-section`. Rules sit
inside cards and tables, never under a heading or in a page header.

## Content

One page bundle per project, article or field note, so images travel with the page and go through
Hugo's image pipeline. Section front matter is documented in the playbooks:
[projects](docs/projects-playbook.md), [field notes](docs/adventures-playbook.md),
[PariData](docs/paridata-playbook.md). Any project, article or field note can take `featured: N`, which
lists it under "Start here" on the home page, lowest number first.

A Tech or Adventures article declares `title`, `description`, `tags` and a `cover` (`image`, a file in
the bundle, and `alt`). `description` is the one line a reader sees on the list card, the home feed,
search, the meta description and JSON-LD. Optional fields:

| Field | Renders, in |
|---|---|
| `series`, `seriesPart` | the series box listing every part (`article/series.html`) |
| `findings`, `methods` | a report article's key findings (a list) and its data and method (markdown), rendered after the report under their own headings and in the markdown twin, so the report's facts are crawlable text |
| `lastmod` | The date of the latest real revision (sitemap, `dateModified`, `article:modified_time`). Without it a page counts as unchanged since `date`. |

The resume is front matter: `role`, `location`, `sameAs` (profile URLs, read only by the JSON-LD
`Person`), then `experience:` periods (`period`,
`role`, `org`, `url`, `note`, `kind: education` for degrees, `work` items with `title`, `url`, `text`,
`video`, `videoAlt`, then `stack` and a markdown `learned` list), `skills` and
`certifications`. `layouts/_partials/resume/timeline.html` renders the periods; `llms.txt` reads the same
data. The page header is the name, the "Save as PDF" button, the `role` line and "As of <month year>" from `lastmod` (printed too); the markdown body, a short list of what the work involves, opens the page in two columns.

A report is a Tech article whose body is the report alone:
`{{< reportframe src="reports/<file>.html" title="…" >}}`, with no introduction above it. The
frame loads lazily and has no border, so the report reads as the article; on load its script sizes
the frame to the report, maps the page's tokens onto the report's CSS variables (both themes), loads
the site font, hides the report's own nav and header, drops its side padding so it sits on the text
column, and patches its accessibility gaps. Report files and their
generators stay untouched.

### Topics

Each tag is a topic page at `/tags/<tag>/`, rendered by `layouts/list.html` from
`layouts/_partials/func/section-pages.html`. `content/tags/<tag>/_index.md` gives it a title and a
description (and `url:` where the tag is not URL-safe: `C++` is `/tags/cpp/`). `/tags/` groups topics
by `data/topics.yaml`: the order of `groups` is the order on the page, each group's heading is the i18n
key `topics_group_<key>`, and any tag not listed falls into the trailing "More" group automatically.

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
gates treat as content), GA4, output formats and the markdown cascade. Every plain `[params]` key
stays above the first `[params.*]` sub-table: TOML assigns keys
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

`.github/workflows/site.yml` pins Hugo 0.168.0 extended, runs `scripts/check.sh` and an internal link
crawl on every pull request (plus an advisory external crawl), and on a push to `main` does the same,
then publishes `public/` to GitHub Pages.

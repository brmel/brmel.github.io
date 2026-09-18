# Architecture

How the templates and stylesheets fit together, and the rules that keep them
that way.

## Principle

**Chrome is layout-driven; authors write prose.** Every repeating structure —
a page's header and eyebrow, a project's stack chips, an article's contribute link, a
section's back navigation — renders from front matter or from the page's
position in the site. An author adding a project writes markdown; the page is
consistent because it cannot be otherwise.

Where that principle was not applied, the site drifted: four layouts each
assembled their own page ending, and two of them ended up with none at all.
Every gate in `scripts/checks/` exists to catch a class of drift that had already
happened.

## Templates

```
layouts/
  404.html · sitemap.xml · index.llms.txt · index.llmsfull.txt
  _default/
    baseof.html · list.html · single.html · search.html · index.json · rss.xml   PaperMod forks
    resume.html        the resume, rendered from front matter
    single.markdown.md the markdown twin of an article, for agents
    _markup/render-link.html   external links open in a new tab
  projects/
    list.html          the project index: one grid, newest first
    single.html        project pages
    tracker.html       PariData, rendered from data/paridata
  partials/
    header.html · footer.html · index_profile.html · post_meta.html · social_icons.html
    templates/         PaperMod forks (Open Graph, Twitter cards, schema)
    extend_head.html · extend_footer.html · google_analytics.html   hooks the theme calls by name
    func/              return values, not markup: call with `partial` and use the result
      section-pages.html   which pages a section lists, across languages
      eyebrow.html         a single page's eyebrow line, by section
      dots.html            a slice joined into one dot-separated, escaped string
      lang-attrs.html      lang/dir attributes for an English page listed on a FR/AR index
      og-image.html · og-src.html   which social card a page shares, and its file
      paridata-ledger.html          the PariData tickets, settled
    page-head/
      header.html          every page header: breadcrumbs, eyebrow, title, description, date line
      crumbs.html
    page-end/          the common page ending
      footer.html          actions, social icons, author card, section nav
      actions.html · author-card.html · section-nav.html
    article/           origin.html (series box) · original.html · related-project.html · cover.html
    adventures/        verdict.html
    home/              career.html · sections.html · latest.html
    project/           meta.html (links + stack) · learning.html
    resume/            timeline.html · contact.html · video-thumb.html
    paridata/          dashboard · curve · ledger · amount · about
    lang/              en-only.html, the "in English" label
    brand/             mark.html (the compass mark, one implementation) · social-icon.html
    head/              fonts.html (preloads) · schema.html (JSON-LD)
  shortcodes/
    figure.html        images through the pipeline, with srcset and dimensions
    gmap.html
    reportframe.html   the branded report frame, rendered in place
    *.markdown.md      the same shortcodes in the markdown output
```

A partial at the root of `partials/` is one PaperMod or Hugo calls by name. Everything written for
this site lives in the folder for its domain.

### `partials/func/`

Partials that `return` a value instead of emitting markup. Keeping them in their
own directory makes the distinction visible at the call site: anything in
`func/` is used as an expression.

```go-html-template
{{- $pages := partial "func/section-pages.html" . }}
{{- $og := partial "func/og-image.html" . }}
```

`dots.html` is the separator. Five templates used to write ` <b aria-hidden="true">·</b> ` and
walk the index themselves, and one of them had drifted to a `<span>` that never got the accent.
The glyph, the element, the `aria-hidden` and the escaping now live in one partial, and the dot
carries `.u-dot` so it styles itself instead of depending on which ancestor it lands in.
Breadcrumbs keep their own, deliberately muted, separator.

### Theme forks

`themes/PaperMod/` is vendored. Fifteen templates are forked into `layouts/`;
each carries a one-line header naming the upstream path and the commit it was
taken from, so a future theme upgrade can be diffed rather than guessed. Nothing
else in the theme is modified.

Four more files in `layouts/` share a name the theme calls without being
forks — `extend_head.html`, `extend_footer.html`, `google_analytics.html` and
`shortcodes/figure.html` are written here from scratch, and the theme's (or
Hugo's) versions are empty extension points or unrelated. They carry no fork header
because there is nothing upstream to diff them against: the header is the
signal, and its absence means "written here, ignore the theme's copy".

## Stylesheets

PaperMod concatenates `assets/css/extended/*.css` in lexical order, so **the
numeric prefix is the cascade**. Without it `tokens.css` sorted last, after
everything that consumes it.

| | |
|---|---|
| `00-tokens` | design tokens; the only file that defines a colour. Spacing is `--flow-tight` / `--flow-block` / `--flow-section` |
| `05-fonts` | self-hosted `@font-face` declarations |
| `10-base` | theme variable remap, the page frame, page headers, type, links, tables, code |
| `20-components` | shared primitives — `.u-card`, `.u-bar`, `.u-tile`, `.u-eyebrow`, `.u-meta`, `.u-dot`, `.u-link`, `.u-rule-link`, `.u-chip`, `.u-rows`, `.u-label-row`, `.u-rule-heading`, `.u-frame` — and what shared partials and shortcodes render |
| `30-chrome` | nav, mark, footers, section nav, content footer |
| `31-toc` `32-search` | table of contents, search box |
| `40-home` `41-resume` `42-timeline` `43-projects` `44-adventures` `45-tracker` `46-project-page` | one section each |
| | `42-timeline` is the career timeline and the resume video dialog |
| `50-content` | article body: figures, diagrams, embedded artefacts |
| `60-print` | print: hides chrome, flattens cards; print spacing and type come from tokens |

Section files **compose** the primitives; they never redeclare them.
`scripts/checks/check-css.py` fails the build if they do, if a colour appears outside
tokens, if a file exceeds 260 lines, or if a class appears on no published page, site template or
script.

Every page loads the same stylesheet. Anything a shared partial or a shortcode renders belongs in
`20-components.css`.

### Page frame

Two widths, one rule in `10-base.css`. The header, footer and `<main>` share the 1200px frame
(`--container-content`), so the logo, the menu's end and the page edges line up. **Every block
inside a page sits at that page's measure — there is no per-block opt-out.** A page picks its
measure once:

- by default it is the text measure (900px, `--container-text`). Home section cards, project
  galleries and report frames sit on the same two edges as the prose beside them; a grid reflows
  to the measure (`auto-fit` + `minmax`) rather than escaping it.
- a page whose body is itself a grid or a table sets the whole page to the 1200px frame with
  `{{ define "main-width" }} main--wide{{ end }}`: the project index, the resume and PariData.
  Headers, section rules and the page end then share the grid's edges, so nothing exceeds anything
  else there either.

Nothing is sized from `100vw`, and no block sets its own `max-width` or `margin-inline:auto` —
spacing between blocks is `margin-block` only.

The measure rule names `.post-content` twice. That is deliberate: PaperMod margins `h3`–`h6`,
`blockquote` and `iframe` by element, which outranks a single class and would left-align them out
of the measure. A block escaping the text column was the whole class of bug this replaced, so the
rule has to win.

There used to be a `.u-wide` opt-out. Every block that carried it — the home section cards, the
project galleries, the report frames — read as a bulge against the text it sat next to, so the
class is gone rather than reapplied more carefully.

Every page header — list, article, field note, project, PariData, resume, search — is
`partials/page-head/header.html`: breadcrumbs, an eyebrow from `func/eyebrow.html`, the title, one
description line (pitch, role or description), and on field notes the date line, `--flow-tight`
apart and `--flow-block` above the content. Articles use `date · N min` as their eyebrow, the same
grammar as their list card. Rules belong to section headings (`.u-rule-heading`) and the page end,
never to a header.

`scripts/checks/check-pages.py` covers what a structural check cannot see: one
destination linked both as text and as an icon on the same page, a link pointing
at its own page, an icon control with no accessible name, internal links that
resolve to nothing, and pages nothing links to. It exists because every other
gate passed while the resume showed LinkedIn and GitHub twice — once as text in
the header, once as an icon in the footer. The gates share `scripts/checks/gate.py`
(paths, config through `tomllib`, the page iterator, pass/fail output).

## Content model

One page bundle per article or project — markdown plus its images — so a page's
assets travel with it and pass through Hugo's image pipeline.

Front matter drives the chrome. A project declares:

```yaml
projectNo: 1                 # stable, orders the index
domain: "saas"               # the eyebrow label; the accent is site-wide
status: "shipped"
pitch: "One line a non-engineer understands."
lede: |                      # three sentences: problem, what it does, what changed
stack: ["Electron", "TypeScript"]
links: { live: "https://…" }
takeaway: "One sentence."    # feeds the learning block on the index
lessons: ["…"]               # at least one real failure
```

`docs/projects-playbook.md` documents each field.

The resume is the same rule applied to a career. Each period is an entry under
`experience:` — `period`, `role`, `org`, the `work` done, then `built`, `stack`,
`tools` and one `learned` sentence — and `layouts/partials/resume/timeline.html`
renders it. It was prose in shortcodes until the three languages drifted: English
listed three periods where French and Arabic listed two, and no gate could see
it. Education is not a separate section; both degrees are periods, so a year, a
degree and a school are written once.

An article in Tech or Adventures declares `title`, `description`, `tags` and a
`cover` (a file in the bundle) with `alt` — `check-og.py` fails the build without the alt.
`description` is the one line the reader sees: on the section card, in the home feed, in the
search index, the meta tag and the JSON-LD. Articles used to carry a `summary` as well, saying
the same thing in different words; it was rendered nowhere, so it is gone. Tags are
not a taxonomy: there are no tag pages; they feed the keywords meta tag and JSON-LD.
Optional fields, each rendered by one partial:

| Field | Renders |
|---|---|
| `series`, `seriesPart` | the series box listing every part, in `article/origin.html` |
| `canonicalOriginal`, `canonicalOriginalName` | the "first published on" credit, in `article/original.html`, inside the series box when there is one |
| `relatedProject` | the project card at the foot, in `article/related-project.html` |

Adventures add the field-note fields documented in `docs/adventures-playbook.md`.

PariData is the one page rendered from `data/` rather than front matter: tickets live in
`data/paridata/tickets/`, documented in `docs/paridata-playbook.md`.

A report is an ordinary Tech article: prose in the text column, then the generated HTML from
`assets/reports/` embedded with `{{< reportframe src="reports/<file>.html" title="…" >}}`. The
article page **is** the report — one URL, reached in one click from the Tech list, with the site
header on it. The shortcode renders the frame in place, `loading="lazy"`, so the report's megabytes
arrive as the reader reaches them rather than behind a button. There is no preview card and no
second route to the same content: a reader who wants the report is already looking at it.

On load the frame script sets the report's own CSS variables from the page's live tokens (so both
themes follow the site), loads the site fonts, hides the report's nav and duplicate title and
patches its accessibility gaps. The report files and their generators stay untouched, so a
regenerated report keeps working.

## Languages

English is the default and lives at the root; French and Arabic live under
`/fr/` and `/ar/`. Structural pages are translated; long-form writing is English
unless someone translates it.

Section listings **merge** rather than filter — `partials/func/section-pages.html`
returns this language's pages plus any default-language pages with no
translation here, and callers label those. Filtering left `/fr/projects/` empty,
which removed Projects from the French nav entirely. Every list follows it: section
indexes, the home feed and section feeds, the search index, the learning list.
An English page on a French or Arabic list carries `lang="en"` and its own direction
(`func/lang-attrs.html`) and the "in English" label (`lang/en-only.html`).

The language switcher goes to the current page's translation when one exists, and to
that language's home otherwise. Numbers, currency placement and plurals come from
i18n (`number_format`, `currency_pattern`, plural forms), not from the templates.
Arabic text renders in IBM Plex Sans Arabic, which downloads only for Arabic
characters. The root `404.html` is the only one GitHub Pages serves, so it links the
French and Arabic homes.

## Deployment

One workflow, `.github/workflows/site.yml`, pins Hugo 0.148.0 extended and runs
`scripts/check.sh` plus an internal link crawl. On a pull request that is all it does
(with an advisory external link crawl); on a push to `main` it then publishes
`public/` to GitHub Pages.

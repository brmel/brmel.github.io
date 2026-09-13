# Architecture

How the templates and stylesheets fit together, and the rules that keep them
that way.

## Principle

**Chrome is layout-driven; authors write prose.** Every repeating structure —
a project's eyebrow and stack chips, an article's tags and contribute links, a
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
    baseof.html        page shell (fork)
    single.html        articles, thoughts, adventures (fork)
    list.html          home + section indexes (fork)
    terms.html         tag index (fork)
    resume.html        the resume, rendered from front matter
    _markup/render-link.html   external links open in a new tab
  projects/
    single.html        project pages
    list.html          the project index
  partials/
    header.html · footer.html · index_profile.html · post_meta.html · share_icons.html
    social_icons.html · translation_list.html · templates/   PaperMod forks
    extend_head.html · extend_footer.html                   PaperMod hooks
    func/              return values, not markup — call with `partial` and use the result
      section-pages.html   which pages a section lists, across languages
      og-image.html        which social card a page shares
      og-src.html          the image file behind it
    page-end/          the common page ending, on every content layout
      footer.html          composes the three below and share_icons.html
      actions.html         improve · discuss
      section-nav.html     back + previous/next
      author-card.html
    article/
      origin.html          series navigation + original-publication credit
      related-project.html the project card at the foot
    adventures/
      header.html · verdict.html · category-icon.html
    home/
      career.html          the experience data, one line per period
      sections.html        section cards
      latest.html          latest across sections
    project/
      header.html          eyebrow, title, pitch, stack, links
      learning.html        what each project taught, at the foot of the index
    resume/
      timeline.html        the resume's periods, from `experience:` front matter
      video-thumb.html     a poster frame that opens in the timeline lightbox
    brand/
      mark.html            the compass mark, single implementation
      social-icon.html
    head/
      fonts.html           font preloads
      schema.html          JSON-LD
  shortcodes/
    figure.html        images through the pipeline, with srcset and dimensions
    gmap.html · reportframe.html
```

A partial at the root of `partials/` is one PaperMod calls by name. Everything written for this site
lives in the folder for its domain.

### `partials/func/`

Partials that `return` a value instead of emitting markup. Keeping them in their
own directory makes the distinction visible at the call site: anything in
`func/` is used as an expression.

```go-html-template
{{- $pages := partial "func/section-pages.html" . }}
{{- $og := partial "func/og-image.html" . }}
```

### Theme forks

`themes/PaperMod/` is vendored. Fifteen templates are forked into `layouts/`;
each carries a one-line header naming the upstream path and the commit it was
taken from, so a future theme upgrade can be diffed rather than guessed. Nothing
else in the theme is modified.

Three more files in `layouts/` share a name with a theme file without being
forks — `extend_head.html`, `extend_footer.html` and
`shortcodes/figure.html` are written here from scratch, and the theme's
versions are empty extension points or unrelated. They carry no fork header
because there is nothing upstream to diff them against: the header is the
signal, and its absence means "written here, ignore the theme's copy".

## Stylesheets

PaperMod concatenates `assets/css/extended/*.css` in lexical order, so **the
numeric prefix is the cascade**. Without it `tokens.css` sorted last, after
everything that consumes it.

| | |
|---|---|
| `00-tokens` | design tokens; the only file that defines a colour |
| `05-fonts` | self-hosted `@font-face` declarations |
| `10-base` | theme variable remap, type, links, tables, code |
| `20-components` | shared primitives — `.u-card`, `.u-bar`, `.u-eyebrow`, `.u-chip`, `.u-rule-heading`, `.u-frame` |
| `30-chrome` | nav, mark, footers, section nav, content footer |
| `31-toc` `32-search` | table of contents, search box |
| `40-home` `41-resume` `42-timeline` `43-projects` `44-adventures` `46-project-page` | one section each |
| | `42-timeline` is the career timeline; the project index draws the same rail from the same tokens |
| `50-content` | article body: figures, diagrams, embedded artefacts |

Section files **compose** the primitives; they never redeclare them.
`scripts/checks/check-css.py` fails the build if they do, if a colour appears outside
tokens, if a file exceeds 260 lines, or if a class is declared but never used.

Every page loads the same stylesheet. Anything a shared partial or a shortcode renders belongs in
`20-components.css`; `.u-breakout` widens a block from the text column to the content width.

`scripts/checks/check-pages.py` covers what a structural check cannot see: the same
destination linked twice on one page however differently the two links are
dressed, a link pointing at its own page, an icon control with no accessible
name, and internal links that resolve to nothing. It exists because every other
gate passed while the resume showed LinkedIn and GitHub twice — once as text in
the header, once as an icon in the footer.

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

An article in Tech, Thoughts or Adventures declares `title`, `summary`, `description`, `tags`
(reuse existing terms) and a `cover` with `alt` — `check-og.py` fails the build without the alt.
Optional fields, each rendered by one partial:

| Field | Renders |
|---|---|
| `series`, `seriesPart` | the series box listing every part, in `article/origin.html` |
| `canonicalOriginal`, `canonicalOriginalName` | the "first published on" credit, same partial |
| `relatedProject` | the project card at the foot, in `article/related-project.html` |

Adventures add the field-note fields documented in `docs/adventures-playbook.md`.

A report is an ordinary Tech article: prose in the text column, then the generated HTML from
`assets/reports/` embedded with `{{< reportframe src="reports/<file>.html" >}}`, which widens to the
content width and sizes the frame to its content.

## Languages

English is the default and lives at the root; French and Arabic live under
`/fr/` and `/ar/`. Structural pages are translated; long-form writing is English
unless someone translates it.

Section listings **merge** rather than filter — `partials/func/section-pages.html`
returns this language's pages plus any default-language pages with no
translation here, and callers label those. Filtering left `/fr/projects/` empty,
which removed Projects from the French nav entirely.

## Deployment

Push to `main` → `.github/workflows/hugo.yml` builds and publishes to GitHub
Pages. Pull requests run `.github/workflows/check.yml`, which is `check.sh` plus
a link crawl. Both pin Hugo 0.148.0 extended.

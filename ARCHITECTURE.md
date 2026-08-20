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
Every gate in `scripts/` exists to catch a class of drift that had already
happened.

## Templates

```
layouts/
  _default/
    single.html        articles, thoughts, adventures
    list.html          home + section indexes
    resume.html        the resume, rendered from front matter
    standalone.html    full-bleed pages that own their <head> (the report)
  projects/
    single.html        project pages
    list.html          the project index
  partials/
    func/              return values, not markup — call with `partial` and use the result
      section-pages.html   which pages a section lists, across languages
      og-image.html        which social card a page shares
    content-footer.html    the common page ending — composes the four below
      content-actions.html   improve · discuss
      share_icons.html
      section-nav.html       back + previous/next
      comments.html          giscus, inert until configured
    brand-mark.html      the compass mark, single implementation
    project-header.html  eyebrow, title, pitch, stack, links
    article-origin.html  series navigation + original-publication credit
    career-timeline.html the resume's periods, from `experience:` front matter
    video-thumb.html     a poster frame that opens in the timeline lightbox
    home-career.html     the same experience data, one line per period
    home-sections.html   section cards
    home-latest.html     latest across sections
    projects-learning.html  what each project taught, at the foot of the index
  shortcodes/
    figure.html        images through the pipeline, with srcset and dimensions
    gmap.html · reportframe.html
```

### `partials/func/`

Partials that `return` a value instead of emitting markup. Keeping them in their
own directory makes the distinction visible at the call site: anything in
`func/` is used as an expression.

```go-html-template
{{- $pages := partial "func/section-pages.html" . }}
{{- $og := partial "func/og-image.html" . }}
```

### Theme forks

`themes/PaperMod/` is vendored. Sixteen templates are forked into `layouts/`;
each carries a one-line header naming the upstream path and the commit it was
taken from, so a future theme upgrade can be diffed rather than guessed. Nothing
else in the theme is modified.

Four more files in `layouts/` share a name with a theme file without being
forks — `comments.html`, `extend_head.html`, `extend_footer.html` and
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
| `10-base` | theme variable remap, type, links, tables, code |
| `20-components` | shared primitives — `.u-card`, `.u-bar`, `.u-eyebrow`, `.u-chip`, `.u-rule-heading`, `.u-frame` |
| `30-chrome` | nav, mark, footers, section nav, content footer |
| `40-home` `41-resume` `42-timeline` `43-projects` `44-adventures` `46-project-page` | one section each |
| | `42-timeline` is the career timeline; the project index draws the same rail from the same tokens |
| `50-content` | article body: figures, diagrams, embedded artefacts |

Section files **compose** the primitives; they never redeclare them.
`scripts/check-css.py` fails the build if they do, if a colour appears outside
tokens, if a file exceeds 260 lines, or if a class is declared but never used.

`scripts/check-bundles.py` covers the fault that shipped twice: two layouts
assemble two different CSS bundles, and a class rendered by a shared partial but
styled in a file only one bundle loads is invisible in the other, silently.
`.report-frame` collapsed to a 300px iframe that way; `.related-project`
rendered unstyled on the same page for the same reason. Anything a shared
partial or a shortcode renders belongs in `20-components.css`.

`scripts/check-pages.py` covers what a structural check cannot see: the same
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
domain: "saas"               # selects the accent via [data-category]
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
`tools` and one `learned` sentence — and `layouts/partials/career-timeline.html`
renders it. It was prose in shortcodes until the three languages drifted: English
listed three periods where French and Arabic listed two, and no gate could see
it. Education is not a separate section; both degrees are periods, so a year, a
degree and a school are written once.

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

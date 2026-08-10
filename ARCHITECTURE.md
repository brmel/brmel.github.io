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
    home-sections.html   section cards
    home-latest.html     latest across sections
    projects-learning.html  continuous-learning block
  shortcodes/
    figure.html        images through the pipeline, with srcset and dimensions
    timeline.html · timeline_item.html   the resume career timeline
    reels.html · gmap.html · reportframe.html · rawhtml.html
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

`themes/PaperMod/` is vendored. Thirteen templates are forked into `layouts/`;
each carries a one-line header naming the upstream path and the commit it was
taken from, so a future theme upgrade can be diffed rather than guessed. Nothing
else in the theme is modified.

## Stylesheets

PaperMod concatenates `assets/css/extended/*.css` in lexical order, so **the
numeric prefix is the cascade**. Without it `tokens.css` sorted last, after
everything that consumes it.

| | |
|---|---|
| `00-tokens` | design tokens; the only file that defines a colour |
| `10-base` | theme variable remap, type, links, tables, code |
| `20-components` | shared primitives — `.u-card`, `.u-bar`, `.u-eyebrow`, `.u-rule-heading`, `.u-frame` |
| `30-chrome` | nav, mark, footers, section nav, content footer |
| `40-home` `41-resume` `42-timeline` `43-projects` `44-adventures` `45-reels` | one section each |
| `50-content` | article body: figures, diagrams, embedded artefacts |

Section files **compose** the primitives; they never redeclare them.
`scripts/check-css.py` fails the build if they do, if a colour appears outside
tokens, if a file exceeds 260 lines, or if a class is declared but never used.

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

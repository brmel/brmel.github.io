# Ibraverse

Personal site of Brahim Redouane Mellah — machine vision and image processing
engineer. Live at **[ibraverse.ca](https://ibraverse.ca)**.

Hugo static site, PaperMod theme (vendored and partially forked), deployed to
GitHub Pages. Three languages: English, French, Arabic (RTL).

## Run it

```bash
hugo server            # http://localhost:1313
./scripts/check.sh     # everything CI runs, locally
```

Requires Hugo **0.148.0 extended** — pinned in both workflows. The gates need
Python 3 and nothing else; the generators also need Pillow.

## Layout

```
content/          markdown, one page bundle per article or project
  projects/       what was built, with galleries
  tech/           long-form technical writing
  thoughts/       shorter reflection
  adventures/     field notes
  resume.md       + .fr.md / .ar.md
  search.md       + .fr.md / .ar.md
archetypes/       one scaffold per section
layouts/          templates; see ARCHITECTURE.md
assets/
  css/extended/   NN-name.css — the number is the cascade order
  js/             timeline.js, the resume video lightbox
  reports/        generated report pages, embedded by the reportframe shortcode
i18n/             en, fr, ar strings
static/og/        generated social cards
scripts/          check.sh and gates.sh; checks/ holds the gates, generate/ the asset generators
docs/             brand system, brand kit, playbooks, improvement plan
themes/PaperMod/  vendored theme; forked files carry a provenance header
```

## Gates

`scripts/gates.sh` holds the list of gates in `scripts/checks/`; `./scripts/check.sh` builds and runs it, and
both workflows run the same script — on every pull request, and again before a
deploy, plus a link crawl on top. They exist because each one caught a defect
that had already shipped.

| Check | Asserts |
|---|---|
| build | Hugo builds clean with `--cleanDestinationDir` |
| `check-orphans.sh` | no asset is referenced by nothing; no image under `static/` |
| `check-og.py` | every page has a resolvable, absolute `og:image` with alt text |
| `check-contrast.py` | every text token clears WCAG AA on every surface, both themes |
| `check-css.py` | explicit cascade order, colours only in tokens, no duplicated primitives, no dead classes |
| `check-chrome.py` | one `h1`, a skip link and sized images on every page; every content page has a way back and a way to contribute |
| `check-pages.py` | no destination linked twice, no self-link, no unnamed control; every internal link resolves and every page is reachable |
| `check-bundles.py` | every class the standalone layout renders is styled by a file it loads |
| `check-rtl.py` | layout mirrors from logical properties alone — no physical `left`/`right` |
| `check-js.py` | every selector a script reaches for exists on the pages that load it |

## Generators

Run by hand, not by the build. Each writes into the repo; commit the result.

| Script | Writes | How |
|---|---|---|
| `scripts/generate/gen-favicons.py` | `static/favicon.{ico,16,32,192,512}`, `apple-touch-icon.png` | serve `scripts/generate/favicon-src.html`, screenshot the mark to `mark-512.png`, then `python3 scripts/generate/gen-favicons.py mark-512.png` |
| `scripts/generate/gen-og-cards.py` | `static/og/*.jpg` | open `scripts/generate/og-cards.html` at width 1200, full-page screenshot to `og-strip.png`, then `python3 scripts/generate/gen-og-cards.py og-strip.png` |

Both need Pillow. The card template uses the self-hosted faces from `/fonts`, so
serve it from the site root rather than opening the file directly.

## Conventions

- **Colours live in `assets/css/extended/00-tokens.css` and nowhere else.** The
  CSS gate fails the build on a hex anywhere else.
- **Chrome renders from front matter.** Project eyebrows, stack chips, status,
  gallery, lessons, series links and the origin credit are all layout-driven, so
  an author writes prose and the page stays consistent by construction.
- **Sections merge across languages.** A section lists this language's pages plus
  untranslated default-language ones, marked. See `docs/brand-guidelines.md` §8.
- **Images go in `assets/` or a page bundle**, never `static/`, so they pass
  through the image pipeline. `static/` is for files served verbatim.

## Docs

| | |
|---|---|
| [ARCHITECTURE.md](ARCHITECTURE.md) | how the templates and stylesheets fit together |
| [docs/brand-guidelines.md](docs/brand-guidelines.md) | the design system, tokens, voice |
| [docs/projects-playbook.md](docs/projects-playbook.md) | how to publish a project page |
| [docs/adventures-playbook.md](docs/adventures-playbook.md) | how to publish a field note |
| [docs/brand-kit/](docs/brand-kit/00-README.md) | logo, social templates, channel art |
| [docs/improvement-plan.md](docs/improvement-plan.md) | the working list for the current branch |

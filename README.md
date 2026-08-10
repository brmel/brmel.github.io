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

Requires Hugo **0.148.0 extended** — pinned in both workflows. Python 3 and
Pillow for the asset and audit scripts.

## Layout

```
content/          markdown, one page bundle per article or project
  projects/       what was built, with galleries
  tech/           long-form technical writing
  thoughts/       shorter reflection
  adventures/     field notes (currently all drafts)
  resume.md       + .fr.md / .ar.md
layouts/          templates; see ARCHITECTURE.md
  partials/func/  partials that return a value rather than markup
assets/
  css/extended/   NN-name.css — the number is the cascade order
  js/             two files, ~80 lines total
static/og/        generated social cards
scripts/          build gates and asset generators
docs/             brand system, playbooks, audit
themes/PaperMod/  vendored theme; forked files carry a provenance header
```

## Gates

`./scripts/check.sh` runs six checks; CI runs the same six plus a link crawl on
every pull request. They exist because each one caught a defect that had already
shipped.

| Check | Asserts |
|---|---|
| build | Hugo builds clean with `--cleanDestinationDir` |
| `check-orphans.sh` | no asset is referenced by nothing; no image under `static/` |
| `check-og.py` | every page has a resolvable, absolute `og:image` with alt text |
| `check-contrast.py` | every text token clears WCAG AA on every surface, both themes |
| `check-css.py` | explicit cascade order, colours only in tokens, no duplicated primitives, no dead classes |
| `check-chrome.py` | one `h1`, a skip link and sized images on every page; every content page has a way back and a way to contribute |

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
| [docs/comments.md](docs/comments.md) | enabling giscus comments |
| [docs/site-audit-2026-08.md](docs/site-audit-2026-08.md) | measured performance, SEO and a11y audit |

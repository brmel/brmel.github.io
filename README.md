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

Requires Hugo **0.148.0 extended** — pinned in `.github/workflows/site.yml`. The gates need
Python 3 and Java; the generators also need Pillow.

## Layout

```
content/          markdown, one page bundle per article or project
  projects/       what was built, with galleries
  tech/           long-form technical writing
  adventures/     field notes
  resume.md       + .fr.md / .ar.md
  search.md       + .fr.md / .ar.md
data/paridata/    PariData tickets, matches and profile; see docs/paridata-playbook.md
archetypes/       one scaffold per section
layouts/          templates; see ARCHITECTURE.md
assets/           everything that passes through Hugo Pipes
  css/extended/   NN-name.css — the number is the cascade order
  js/             timeline.js (resume video dialog), paridata.js (ledger controls)
  images/         profile photo and resume video posters
  paridata/       competition flags
  reports/        generated report pages; the reportframe shortcode renders one in place
i18n/             en, fr, ar strings
static/           copied as-is: favicons, fonts (Latin faces + IBM Plex Sans Arabic), social cards (og/), CNAME, robots.txt
scripts/          check.sh builds and runs gates.sh; checks/ holds the gates, generate/ the asset generators
.github/          site.yml: check every pull request; check, then deploy, on push to main
docs/             brand system, brand kit, playbooks, improvement plan
themes/PaperMod/  vendored theme; forked files carry a provenance header
```

## Gates

`scripts/gates.sh` is the list of gates in `scripts/checks/`, and `./scripts/check.sh` builds the
site and runs it. CI runs the same script on every pull request and again before every deploy,
then crawls every internal link. Each gate prints what it asserts when it passes; each exists
because it caught a defect that had already shipped.

## Audit

`python3 scripts/audit.py [base-url]` runs Lighthouse (12 pages, mobile and desktop) and a
full link crawl against the live site or a local server, and fails when a score is under the
budget in `docs/improvement-plan.md`. It needs Node for `npx` and Chrome; nothing is installed
into the repo.

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

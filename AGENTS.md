# Ibraverse — Agent Guide

`CLAUDE.md` is a symlink to this file, the single source of truth for every coding agent in this repo.

## The site

Personal site of Brahim Redouane Mellah, senior C++ engineer in Montréal: resume, projects, technical
articles, field notes and the PariData ledger, in English, French and Arabic (RTL). Hugo 0.148.0
extended on the vendored PaperMod theme, deployed to GitHub Pages at https://ibraverse.ca.

## Commands

| Command | Does |
|---|---|
| `hugo server -M` | local site on http://localhost:1313; `-M` renders to memory so `public/` keeps the real build, `-D` adds drafts |
| `./scripts/check.sh` | build and every gate, exactly what CI runs; needs Python 3 and Java |
| `./scripts/gates.sh` | the gates alone, on an existing `public/` |
| `python3 scripts/checks/check-css.py` | one gate (each file in `scripts/checks/` is one) |
| `python3 scripts/audit.py [base-url]` | Lighthouse on 11 pages, mobile and desktop, plus a link crawl, against the budgets below; defaults to the live site; needs Node and Chrome |
| `node .claude/skills/verify-site/responsive.mjs` | page overflow across pages × viewports × themes; see the `verify-site` skill |

## Hard rules

Each rule names the gate that enforces it; the rest are enforced in review.

**Code**
- Less code is the goal: a change that removes more than it adds and still works is the better change.
- No comments in templates, CSS, JS or scripts. Exceptions: the one-line header on PaperMod forks and
  the `# vN` tag on SHA-pinned actions.
- No dead code. Every partial, token, i18n key and front-matter field has a reader; unused classes
  (`check-css`), unloaded scripts and missing selectors (`check-js`) and unreferenced assets
  (`check-orphans`) fail the build.
- Hugo features and plain CSS first. JavaScript only where a page cannot work without it: theme
  toggle, search, resume video dialog, PariData controls, report frame, code copy button, analytics.
- No third-party runtime requests except Google Analytics 4. Fonts, scripts and images are
  self-hosted; the CSP in `layouts/partials/extend_head.html` blocks the rest.
- No new dependencies. Tools run from `npx` or are pinned inside the script that uses them.

**CSS**
- Colours exist only in `assets/css/extended/00-tokens.css` (`check-css`); every text token clears
  4.5:1 on both backgrounds in both themes, syntax colours included (`check-contrast`).
- Files are `NN-name.css`, the number is the cascade, 260 lines at most; shared primitives live in
  `20-components.css` and are never redeclared (`check-css`).
- Logical properties only, never `left`/`right` (`check-rtl`).
- Breakpoints are 600px and 768px (960px for the PariData ledger); a grid that can size itself uses
  `auto-fit`/`minmax`. No block sets its own `max-width` or uses `100vw`; a page widens with `main--wide`.

**Templates**
- Chrome renders from front matter; content files never carry layout markup.
- PaperMod forks keep the upstream name and the fork header. Site templates live in a domain folder
  and never take a theme name. Partials that return a value live in `layouts/partials/func/`.
- Every page has one `h1`, a skip link and sized images; every section page ends with
  `layouts/partials/page-end/footer.html` (`check-chrome`) and is linked from its index (`check-listings`).

**Content and images**
- One page bundle per page. Images live in the bundle or `assets/`, never `static/` (`check-orphans`).
- File names are kebab-case and describe the content (`02-vmmap-snapshot.jpg`).
- Every image has `alt`, `width`, `height` (`check-chrome`), a WebP rendition and `sizes` that match
  its displayed width. The likely LCP image loads eagerly with `fetchpriority="high"`, the rest lazily.
- A cover or figure file missing from the bundle fails the build; a cover without `alt` fails `check-og`.
- Copy follows [docs/voice.md](docs/voice.md). Facts, numbers and links are never changed in an edit.

**Languages**
- Structural pages (home, resume, section indexes, search) exist in EN, FR and AR, each with its own
  title and description. A new UI string goes into all three `i18n/*.yaml` files at once.
- Lists merge through `layouts/partials/func/section-pages.html`; nothing filters by language.
- Arabic is checked on screen: mirroring, `‎C++‎` with direction marks, `<bdi>` around mixed text.

**Accessibility**: WCAG 2.2 AA. Targets at least 24px, scrollable regions keyboard-focusable, named
controls (`check-pages`), valid HTML (`check-html`).

**SEO**: descriptions 50–160 characters, titles and descriptions unique per language, canonical and
`x-default` on every page, JSON-LD type per section, sitemap equal to the indexable pages
(`check-seo`); no dead internal links, self-links, unlinked pages or text-and-icon duplicates
(`check-pages`); every page has an absolute `og:image` with alt (`check-og`).

**Agents**: `static/robots.txt`, `/llms.txt` and `/llms-full.txt` describe the real site and block
only `/reports/`. Every Tech and Adventures page has an `index.md` twin.

**Performance** (mobile, Lighthouse simulated throttling; `scripts/audit.py` fails on the scores)

| Performance | A11y, best practices, SEO | LCP | CLS | TBT | HTML gzip | CSS gzip | Images above the fold |
|---|---|---|---|---|---|---|---|
| ≥ 98 | 100 | ≤ 1.5 s | ≤ 0.01 | 0 ms | ≤ 20 KB | ≤ 15 KB | ≤ 60 KB |

## Where things live

| Path | |
|---|---|
| `content/` | page bundles; `content/tags/` topic pages |
| `layouts/` | templates; `layouts/partials/<domain>/`, theme names at the partials root |
| `assets/css/extended/` | the stylesheet, cascade by file number |
| `i18n/`, `data/` | UI strings; PariData and topic groups |
| `scripts/` | `check.sh`, `gates.sh`, `scripts/checks/`, `audit.py`, `scripts/generate/` |
| `docs/` | brand, voice, playbooks, `docs/decisions.md`, `docs/backlog.md` |

The full map, every template and partial, the stylesheet table and the content model are in
[ARCHITECTURE.md](ARCHITECTURE.md).

## Workflow

1. Work on a branch; a push to `main` deploys.
2. Read every file the change touches and its callers; confirm the problem on the current build.
3. Make the smallest change that does the job. A second defect found on the way goes into
   [docs/backlog.md](docs/backlog.md).
4. `./scripts/check.sh` passes.
5. Any change to layouts, CSS, content or i18n is checked on screen with the `verify-site` skill.
6. Docs change in the same commit: ARCHITECTURE.md for structure, a playbook for front matter,
   `docs/decisions.md` for a decision, `docs/backlog.md` for open work, this file for commands and
   rules. `check-docs` fails on a path that no longer exists.
7. Commit subject: one plain sentence saying what changed for the reader, capitalised, no prefix, no
   period ("Take the pull-quote out of every project story"). Body: why, and what was measured, in
   short paragraphs wrapped near 72 columns.

## Skills

Repo skills in `.claude/skills/`; read the `SKILL.md` before relying on it.

| Skill | Load when |
|---|---|
| `verify-site` | any change to layouts, CSS, content or i18n, before calling it done |
| `publish-content` | adding a project, Tech article, field note, PariData ticket or result, topic, or translation |
| `voice` | writing or editing any user-facing copy in EN, FR or AR |

Global skills: `karpathy-guidelines` before writing code; `diagnosing-bugs` before fixing a bug whose
cause is unknown; `playwright-cli` for ad-hoc browser automation.

## MCP

Playwright is the only MCP server this repo uses (`verify-site`). The dart, artemis and mobile-mcp
servers are Flutter and Android tools; disable them for this project with `/mcp`.

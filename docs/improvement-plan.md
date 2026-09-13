# Improvement plan

Working list for the `ImprovePerformance` branch: speed, SEO, agent readiness, accessibility,
correctness and structure. Items run in the order of §5a, one at a time, and each one must leave the
site measurably better or it is reverted.

When every item is done or dropped, fold §2 and §3 into `ARCHITECTURE.md` and `README.md`, then
delete this file. Git keeps the history.

---

## 1. The loop — every item, no exceptions

1. **Read.** Open every file the item touches and every caller of it. Confirm the problem still
   exists on the current build before changing anything.
2. **Measure before.** Run the checks named in the item's *Verify* column and write the numbers
   in the done log (§7).
3. **Design the smallest change.** Prefer Hugo and browser features over new code. If the change
   needs a new dependency, a second code path, or a workaround for the theme, drop the item and
   log why.
4. **Change.** Code only: no comments, no dead code, no half-wired options. Docs change in the same
   commit when behaviour or structure changes.
5. **Verify.**
   - `./scripts/check.sh` passes: every gate.
   - Playwright on the affected pages: EN/FR/AR × light/dark × 390px/768px/1440px, with
     screenshots viewed and the DOM checked.
   - The item's own measure (Lighthouse, axe, validator, crawler) shows the gain. No regression on
     any other score in §4.
6. **Commit.** One item per commit, message says what and why, pushed to `ImprovePerformance`.
7. **Log.** Tick the box, fill the done log: commit, before, after.
8. **Ship.** At the end of each phase, merge to `main`, confirm the deploy run for that exact
   commit succeeded, and re-measure the live site.

---

## 2. Standing rules

### Code

- Less code is the goal. A change that removes more than it adds and still does the job wins.
- No comments. The only exceptions are the one-line fork headers on PaperMod forks and the `# vN`
  tags on SHA-pinned actions.
- No dead code: every partial, class, token, i18n key, script and front-matter field has a reader.
- Build with native, stable features: Hugo pipes, image processing, output formats, i18n; plain
  CSS; no JavaScript unless a page cannot work without it.
- No third-party runtime requests. Fonts, scripts and images are self-hosted.

### CSS

- Colours exist only in `00-tokens.css`. Every token is used.
- The file number is the cascade. Shared primitives live in `20-components.css`, and section files
  compose them without redeclaring.
- Logical properties only (`inline-start`, never `left`), so Arabic mirrors for free.
- Two breakpoints: 600px and 768px. Files stay under 260 lines.

### Templates

- Chrome renders from front matter. Authors write prose, never layout.
- PaperMod forks keep their upstream name and a fork header. Project-owned templates never shadow
  a theme name.
- Partials that return values live in `partials/func/`.

### Content and images

- One page bundle per article or project. Images go through the pipeline: never `static/`.
- File names are kebab-case and describe the content (`02-vmmap-snapshot.jpg`).
- Every image has `alt`, width, height, a WebP rendition, and a `sizes` that matches its real
  displayed width.
- The image likely to be the LCP loads eagerly with `fetchpriority="high"`. Everything else is lazy.
- Plain English. No filler, no AI phrasing.

### Languages

- Structural pages exist in EN/FR/AR. Each translated page has its own title and description, not
  the English one.
- Every page emits `hreflang` for its translations plus `x-default`.

### Accessibility

- WCAG 2.2 AA: text contrast ≥ 4.5:1, including syntax highlighting. Targets ≥ 24px.
- Anything scrollable is keyboard-focusable.
- One `h1`, a skip link, and named controls on every page.

### SEO

- `<title>` is 60 characters or fewer; description is 70–160 characters; both are unique per page
  and language.
- The sitemap lists only indexable pages.
- Each section's JSON-LD type matches its content: `TechArticle` for tech, `BlogPosting` for
  thoughts, `BlogPosting` + `Review` for adventures, `SoftwareSourceCode` for projects.

### Agents

- `robots.txt`, `llms.txt` and `llms-full.txt` describe the real site. Nothing an agent should
  read is blocked.
- Every article has a clean text rendition an agent can fetch without parsing HTML.

### Performance budgets (mobile, Lighthouse simulated throttling)

| Metric | Budget |
|---|---|
| Performance score | ≥ 98 on every page |
| LCP | ≤ 1.5 s |
| CLS | ≤ 0.01 |
| TBT | 0 ms |
| HTML (gzip) | ≤ 20 KB |
| CSS (gzip) | ≤ 15 KB |
| JavaScript | none, except search and resume |
| Image bytes above the fold | ≤ 60 KB |

### Quality gates (targets)

| Check | Target |
|---|---|
| Lighthouse accessibility, best practices | 100 |
| Lighthouse SEO | 100 on indexable pages |
| axe-core WCAG 2.2 AA, 15 pages × 2 widths × 2 themes | 0 violations |
| Nu HTML Checker, site pages | 0 errors |
| Link crawl | 0 broken |

---

## 3. Target structure

Only the changes are marked. Everything else stays where it is.

```
.github/workflows/      check.yml (pull requests) · hugo.yml (deploy on main)
archetypes/             one per section: adventures, projects, tech, thoughts, default
assets/
  css/extended/         NN-name.css, cascade by number
  css/standalone.css
  images/               profile photo; timeline/ posters named by video ID  ← R3
  js/                   timeline.js
  reports/              generated report HTML, embedded by reportframe
content/                page bundles per section; resume.{md,fr.md,ar.md}; search.*
docs/
  brand-guidelines.md · projects-playbook.md · adventures-playbook.md · standalone-layout.md
  brand-kit/            logo, social templates, channel art, photo and voice guides
  improvement-plan.md   this file, deleted when the branch closes
i18n/                   en · fr · ar
layouts/
  _default/             theme-level layouts and forks
  projects/             project index and page
  partials/
    <theme names>       forks and theme hooks only, at the root     ← R2
    func/               partials that return values
    article/            origin, content footer and actions, section nav, author card, verdict
    home/               profile blocks, career line, sections, latest
    project/            header, learning, related project
    resume/             career timeline, video thumb
    brand/              mark, fonts, category icon, social icon
  shortcodes/           figure · gmap · reportframe
  index.llms.txt · index.llmsfull.txt · sitemap.xml
scripts/
  check.sh · gates.sh   entry points
  checks/               one gate per file                           ← R1
  generate/             favicon and OG generators, with their HTML templates  ← R1
  audit.sh              local Lighthouse, axe, validator, crawler run  ← M1
static/                 verbatim files only: favicons, fonts, og, robots.txt, CNAME
themes/PaperMod/        vendored, untouched
```

Placement rules:
- A file sits in the folder named for its domain. The root of `partials/` means "PaperMod calls
  this by name".
- A generator's HTML template sits next to the generator.
- A gate is added to `gates.sh` in the same commit that adds the check.

---

## 4. Baseline — 2026-09-12, `main` at `e304831`, live site

Lighthouse 12, 12 pages × mobile/desktop:

| Page | Perf mobile / desktop | A11y | BP | SEO | LCP mobile |
|---|---|---|---|---|---|
| Home EN | 99 / 100 | 100 | 100 | 100 | 2.2 s |
| Home FR · AR | 100 / 100 | 100 | 100 | 100 | 1.2 s |
| Resume | 98 / 100 | 100 | 100 | 100 | 1.8 s |
| Projects index | 99 / 100 | 100 | 100 | 100 | 1.8 s |
| Project · Tech index · Adventure · Thought · Report | 100 / 100 | 100 | 100 | 100 | 1.2–1.6 s |
| Windows memory deep dive | 97 / 100 | 96 | 100 | 100 | 2.2 s |
| Search (noindex by design) | 100 / 100 | 100 | 100 | 66 | 1.5 s |

- **axe-core, 60 runs:** 2 rules fail, both on deep-dive code blocks: 136 contrast nodes and
  4 scrollable regions with no keyboard access.
- **Nu HTML Checker:** 4 errors in the verdict `<dl>`, about 15 duplicate `srcset` widths, and
  11 in generated reports (mostly validator gaps).
- **Link crawl:** 398 links, 0 broken.
- **AI crawlers** (GPTBot, ClaudeBot, PerplexityBot, Google-Extended): 200 everywhere.
- **Headers:** `max-age=600` on every file, gzip only, no HSTS/CSP/nosniff/referrer policy.

---

## 5. Backlog

Columns: **Where** is the starting point, **Done when** is the acceptance test, **Verify** is the
measure logged in §7.

### 5a. Order

K1 → K2 → R1 → R2 → R3 → R4 → C4 → M1 → C1 → C2 → M2 → C3 → M3 → C5 → P1 → P2 → P3 → P4 → P5 →
S1 → S2 → S3 → S4 → S5 → S6 → S7 → A1 → A2 → A3 → H1 → close (re-audit live, merge, fold rules into
ARCHITECTURE.md and README.md, delete this file).

Structure moves come first so later changes land in their final place. A fix lands before the gate
that locks it, so `main` stays green.

### Cleaning

- [x] **K1 · `.gitignore`.** Only patterns this repo produces; no comments, no entries covered by
  broader ones.
- [x] **K2 · Archetypes without comments.** The inline hints move into the playbooks, which already
  document each field.
  - *Done when:* `hugo new` on every archetype gives front matter with no `#`, and every hinted
    value is in a playbook.

### Phase 0 — Measure in the repo

So every later item can prove its gain with one command.

- [ ] **M1 · Local audit script.** `scripts/audit.sh [base-url]` runs Lighthouse (mobile and
  desktop, pages from §4), axe-core through Playwright (15 pages × 2 widths × 2 themes), the Nu
  HTML Checker on `public/`, and a link crawl. It prints one summary table. Tools come from `npx`
  and a pinned `vnu.jar`; nothing is added to the repo's dependencies.
  - *Done when:* one command reproduces §4 within noise.
- [ ] **M2 · HTML validity gate.** Add `checks/check-html.sh` running the pinned Nu checker on
  site pages (generated `assets/reports/` excluded), wired into `gates.sh` and CI. Java is
  already on GitHub runners.
  - *Done when:* the gate fails on today's `<dl>` and `srcset` errors. It lands together with C1
    and C2 so `main` stays green.
- [ ] **M3 · Syntax colours in the contrast gate.** `check-contrast.py` also reads the Chroma
  highlight colours against the code-block background, in both themes.
  - *Done when:* it fails on today's comment colour, 3.6:1. Lands with C3.

### Phase 1 — Structure

Moves first, so every later change lands in its final place.

- [x] **R1 · Split `scripts/`.** Gates into `scripts/checks/`. Generators and their HTML templates
  into `scripts/generate/`. `check.sh` and `gates.sh` stay as entry points.
  - *Where:* `gates.sh`, both workflows, README, ARCHITECTURE, and the relative paths inside the
    scripts.
  - *Done when:* check.sh and CI pass, and both generators run from their new location.
- [ ] **R2 · Group project-owned partials by domain** (layout in §3). Theme names stay at the root.
  - *Where:* every `partial "…"` call; `check-bundles.py` if it names paths.
  - *Done when:* the build is byte-identical, and no partial at the root lacks
    a theme counterpart.
- [ ] **R3 · Profile photo name.** `assets/images/MyPhoto.jpg` becomes `profile.jpg`. The
  timeline images keep their names: they are YouTube video IDs, and `video-thumb.html` looks them
  up by ID.
  - *Where:* `config.toml` (four references).
  - *Done when:* the build is identical apart from the file name, and no asset is left orphaned.
- [ ] **R4 · Evaluate Hugo's current template layout** (`_partials/`, `_shortcodes/`, no
  `_default/`). Adopt only if every PaperMod lookup still resolves with a byte-identical build.
  Otherwise log "dropped: theme depends on legacy lookup" and stop.

### Phase 2 — Correctness and cleaning

- [ ] **C1 · Verdict markup.** Wrap every `dt`/`dd` pair in a `div`, not just the last two.
  - *Where:* `partials/verdict.html`, `44-adventures.css`.
  - *Done when:* 0 validator errors, and the verdict looks pixel-identical in the Playwright matrix.
- [ ] **C2 · `srcset` without duplicate widths.** When the image is smaller than the large
  rendition, emit a single candidate.
  - *Where:* `shortcodes/figure.html`.
  - *Done when:* 0 duplicate-width errors, and figure widths are unchanged.
- [ ] **C3 · Code blocks.** Comment colour ≥ 4.5:1 in both themes, and `tabindex="0"` on
  scrollable `pre` through the code-block render hook.
  - *Where:* `10-base.css` or tokens, `_markup/render-codeblock.html` only if Hugo cannot do it
    natively.
  - *Done when:* axe 0 violations on the deep dive, and the deep dive's a11y score is 100.
- [ ] **C4 · Docs match the code.**
  - ARCHITECTURE: the partials tree is missing 12 partials, it says "Sixteen templates" where
    there are 15, and the stylesheet table is missing `05-fonts`, `31-toc`, `32-search`.
  - README: "adventures (currently all drafts)" (both are published), "two files, ~80 lines"
    (one file, 71 lines), and "docs: … audit" (removed).
  - *Done when:* every path and count in both files matches `find` output.
- [ ] **C5 · Phone navigation.** EN/FR menus overflow by 5–52px at 360–390px since Search was
  added. Choose one of: keep the native scroll, a two-row wrap, or tighter spacing (§6, D3).
  - *Done when:* the chosen option is implemented, screenshots are taken at 360/375/390/414 in all
    three languages, and nothing is clipped without a visible way to reach it.

### Phase 3 — Speed

- [ ] **P1 · Profile photo.** `sizes` matches the displayed width (153–200px); renditions at 200w,
  400w and 600w.
  - *Where:* `partials/index_profile.html`.
  - *Done when:* home image bytes drop from 131 KB to ≤ 20 KB on a 3× phone, and home LCP ≤ 1.5 s.
- [ ] **P2 · Index covers.** List-page covers render at card width in WebP with a correct `sizes`.
  - *Where:* PaperMod's `partials/cover.html` (fork it) or a list-only partial.
  - *Done when:* Lighthouse "properly size images" and "next-gen formats" pass on `/tech/`, saving
    about 426 KB.
- [ ] **P3 · LCP image priority.** On article pages, the cover or the first figure above the fold
  loads eagerly with `fetchpriority="high"`; every other image stays lazy.
  - *Done when:* the deep dive's mobile LCP ≤ 1.5 s and its perf ≥ 99.
- [ ] **P4 · Fonts.** Audit which faces each page actually uses. Preload only the ones used above
  the fold, and drop any face never rendered.
  - *Done when:* no unused font request in any Lighthouse run, and FCP is not worse.
- [ ] **P5 · Unused CSS (evaluate).** About 10 KB unused on search and list pages. Split bundles
  only if it adds no second code path. Otherwise log "dropped: one bundle is simpler, 12 KB gzip
  is within budget".

### Phase 4 — SEO

- [ ] **S1 · Sitemap lists only indexable pages.** Skip pages with `robotsNoIndex`.
  - *Where:* `layouts/sitemap.xml`.
  - *Done when:* the 35 tag pages and `/search/` are gone from the sitemap, and every URL left
    returns 200 without `noindex`.
- [ ] **S2 · JSON-LD per section** (types in §2). Adventures carry a `Review` with `itemReviewed`
  and `reviewRating` taken from `rating`.
  - *Where:* `partials/schema.html`, `templates/schema_json.html`.
  - *Done when:* each type is parsed and checked for required properties by M1, on every section.
- [ ] **S3 · Titles ≤ 60 characters.** 13 pages are over, worst 99 (FR barcode). Shorten the
  titles themselves; don't add a second title field.
  - *Done when:* 0 titles over 60, H1s still read naturally, and 0 duplicate titles (home EN/FR
    differ).
- [ ] **S4 · Descriptions 70–160 characters.** FR/AR section indexes and the AR barcode page.
  - *Done when:* 0 out of range, and each is written in its own language.
- [ ] **S5 · `hreflang` `x-default`** on every translated page and in the sitemap.
- [ ] **S6 · Report pages.** The standalone layout emits `hreflang`, canonical and `TechArticle`
  JSON-LD like every other article.

- [ ] **S7 · SEO gate.** `checks/check-seo.py` asserts the §2 SEO rules on the build: title and
  description length and uniqueness, sitemap only indexable, `hreflang` with `x-default`, JSON-LD
  type per section. Lands once S1–S6 pass.

### Phase 5 — Agent readiness

- [ ] **A1 · Report content reachable.** Today `robots.txt` blocks `/reports/`, so crawlers index
  only the ~600-word wrapper. Choose between allowing `/reports/` and moving the key findings into
  the wrapper as text (§6, D2).
- [ ] **A2 · Markdown rendition per article.** A Hugo output format serves `index.md` beside each
  page, linked with `rel="alternate" type="text/markdown"` and from `llms.txt`.
  - *Done when:* every article's `.md` returns 200 as `text/markdown` or `text/plain` and matches
    its HTML body.
- [ ] **A3 · `llms.txt` headings.** Short section names as `##`, with the one-line description on
  the next line; the longest heading today is 148 characters.
  - *Done when:* it parses cleanly with the `llms-txt` reference parser.

### Phase 6 — Hosting

Needs decision D1 before starting.

- [ ] **H1 · Headers GitHub Pages cannot set.** Year-long `immutable` cache on fingerprinted files
  and fonts, brotli, HSTS, a CSP, `X-Content-Type-Options`, `Referrer-Policy`. Options: a
  Cloudflare proxy in front of Pages (DNS change only), or Cloudflare Pages with a `_headers` file.
  - *Done when:* Lighthouse cache audits pass on every page, and the Mozilla Observatory grade is
    A or better.

---

## 6. Decisions needed

| ID | Question | Blocks |
|---|---|---|
| D1 | Keep GitHub Pages as is, or put Cloudflare in front? | H1 |
| D2 | Reports: allow crawling `/reports/`, or move the findings into the wrapper page? | A1 |
| D3 | Phone menu: native sideways scroll, two-row wrap, or tighter spacing? | C5 |

---

## 7. Done log

| Item | Commit | Before | After | Notes |
|---|---|---|---|---|
| K1 | `e28e720` | 22 lines, 9 comments | 11 lines | same ignored set |
| K2 | `70ed507` | 22 comment lines in 3 archetypes | 0; field docs in ARCHITECTURE.md and projects-playbook.md | all 4 archetypes scaffold and build |
| R1 | this commit | 15 files flat in `scripts/` | entry points + `checks/` (9) + `generate/` (4) | gates pass; gates resolve the repo from any cwd; OG generator output byte-identical |

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
  brand-guidelines.md · projects-playbook.md · adventures-playbook.md
  brand-kit/            logo, social templates, channel art, photo and voice guides
  improvement-plan.md   this file, deleted when the branch closes
i18n/                   en · fr · ar
layouts/
  _default/             theme-level layouts and forks
  projects/             project index and page
  partials/
    <theme names>       forks and theme hooks only, at the root     ← R2
    func/               partials that return values
    page-end/           footer, actions, section nav, author card
    article/            origin, related project
    adventures/         header, verdict, category icon
    home/               career, sections, latest
    project/            header, learning
    resume/             timeline, video thumb
    brand/              mark, social icon
    head/               fonts, schema
  shortcodes/           figure · gmap · reportframe
  index.llms.txt · index.llmsfull.txt · sitemap.xml
scripts/
  check.sh · gates.sh   entry points
  checks/               one gate per file                           ← R1
  generate/             favicon and OG generators, with their HTML templates  ← R1
  audit.py              Lighthouse and link crawl against budgets  ← M1
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

K1 → K2 → R1 → R2 → R3 → R4 → K3 → K4 → K5 → K6 → K7 → K8 → C4 → M1 → C1 → C2 → M2 → C3 → M3 → C5 → C6 → P1 → P2 → C7 → P3 → P4 → P5 →
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

- [x] **K3 · Redundant RTL script.** `extend_head.html` set `dir="rtl"` from JavaScript on pages
  whose `<html>` already carries it from `baseof.html` and `standalone.html`.
- [x] **K4 · Unused `customCSS` / `customJS`.** Read by two templates, set by no page. Per-article
  CSS would also escape the CSS gate; styling belongs in the section stylesheet.
- [x] **K5 · Stale standalone scaffold.** `docs/standalone-layout.md` is a draft content file, not
  a doc: comments, Google Analytics (removed), inline `<style>` advice. Delete it and document
  the standalone front matter (`hideAutoHeader`, `fullBleed`) in ARCHITECTURE.md.

- [x] **K6 · Comments left in inline scripts and styles.** The first sweep covered template and
  CSS comments; `//` and `/* */` inside `<script>` and `<style>` blocks in templates were missed
  (`reportframe.html` has one).
  - *Done when:* no comment in any template's inline script or style, and the build is identical
    apart from minified output that already stripped them.

- [x] **K7 · Comments and dead code in the gates.** Trailing `#` comments in four gate scripts,
  and `OPT_OUT`, a set that was always empty in `check-chrome.py`.
- [x] **K8 · CSS gate warnings become failures.** Raw `#fff`/`#000` in `20-components.css` and
  `42-timeline.css` move to tokens; after that, a raw colour or a declared-but-unused class fails
  the build (both only warn today, though the README says the gate enforces them).

### Phase 0 — Measure in the repo

So every later item can prove its gain with one command.

- [x] **M1 · Local audit script.** `scripts/audit.py [base-url]` runs Lighthouse (mobile and
  desktop, pages from §4) and a link crawl against budgets. HTML validity lives in the M2 gate;
  the axe matrix stays a Playwright step in the loop. It prints one summary table. Tools come from `npx`
  and a pinned `vnu.jar`; nothing is added to the repo's dependencies.
  - *Done when:* one command reproduces §4 within noise.
- [x] **M2 · HTML validity gate.** Add `checks/check-html.py` running the pinned Nu checker on
  site pages (generated `assets/reports/` excluded), wired into `gates.sh` and CI. Java is
  already on GitHub runners.
  - *Done when:* the gate fails on today's `<dl>` and `srcset` errors. It lands together with C1
    and C2 so `main` stays green.
- [x] **M3 · Syntax colours in the contrast gate.** `check-contrast.py` also reads the Chroma
  highlight colours against the code-block background, in both themes.
  - *Done when:* it fails on today's comment colour, 3.6:1. Lands with C3.

### Phase 1 — Structure

Moves first, so every later change lands in its final place.

- [x] **R1 · Split `scripts/`.** Gates into `scripts/checks/`. Generators and their HTML templates
  into `scripts/generate/`. `check.sh` and `gates.sh` stay as entry points.
  - *Where:* `gates.sh`, both workflows, README, ARCHITECTURE, and the relative paths inside the
    scripts.
  - *Done when:* check.sh and CI pass, and both generators run from their new location.
- [x] **R2 · Group project-owned partials by domain** (layout in §3). Theme names stay at the root.
  - *Where:* every `partial "…"` call; `check-bundles.py` if it names paths.
  - *Done when:* the build is byte-identical, and no partial at the root lacks
    a theme counterpart.
- [x] **R3 · Profile photo name.** `assets/images/MyPhoto.jpg` becomes `profile.jpg`. The
  timeline images keep their names: they are YouTube video IDs, and `video-thumb.html` looks them
  up by ID.
  - *Where:* `config.toml` (four references).
  - *Done when:* the build is identical apart from the file name, and no asset is left orphaned.
- [x] **R4 · Hugo's current template layout — dropped.** Moving to `_partials/`, `_shortcodes/`,
  `_markup/` and a flat `layouts/` built identically except the tag indexes: the vendored theme's
  `_default/terms.html` wins over the project fork under both `terms.html` and `taxonomy.html`.
  Keeping it would need a theme workaround, so the legacy layout stays until PaperMod moves.

### Phase 2 — Correctness and cleaning

- [x] **C1 · Verdict markup.** Wrap every `dt`/`dd` pair in a `div`, not just the last two.
  - *Where:* `partials/verdict.html`, `44-adventures.css`.
  - *Done when:* 0 validator errors, and the verdict looks pixel-identical in the Playwright matrix.
- [x] **C2 · `srcset` without duplicate widths.** When the image is smaller than the large
  rendition, emit a single candidate.
  - *Where:* `shortcodes/figure.html`.
  - *Done when:* 0 duplicate-width errors, and figure widths are unchanged.
- [x] **C3 · Code blocks.** Comment colour ≥ 4.5:1 in both themes, and `tabindex="0"` on
  scrollable `pre` through the code-block render hook.
  - *Where:* `10-base.css` or tokens, `_markup/render-codeblock.html` only if Hugo cannot do it
    natively.
  - *Done when:* axe 0 violations on the deep dive, and the deep dive's a11y score is 100.
- [x] **C4 · Docs match the code.**
  - ARCHITECTURE: the partials tree is missing 12 partials, it says "Sixteen templates" where
    there are 15, and the stylesheet table is missing `05-fonts`, `31-toc`, `32-search`.
  - README: "adventures (currently all drafts)" (both are published), "two files, ~80 lines"
    (one file, 71 lines), and "docs: … audit" (removed).
  - *Done when:* every path and count in both files matches `find` output.
- [x] **C5 · Phone navigation.** EN/FR menus overflow by 5–52px at 360–390px since Search was
  added. Choose one of: keep the native scroll, a two-row wrap, or tighter spacing (§6, D3).
  - *Done when:* the chosen option is implemented, screenshots are taken at 360/375/390/414 in all
    three languages, and nothing is clipped without a visible way to reach it.

- [x] **C6 · Back-to-top link outside a landmark.** Once a page scrolls, `#top-link` becomes visible
  outside `header`/`main`/`footer` (axe `region`), on every long page. The first axe matrix never
  scrolled, so it missed it.
  - *Done when:* axe run after scrolling reports 0 violations on the deep dive, home and resume.

- [x] **R5 · Reports use the article layout (bug: report text ran edge to edge).** Both report
  articles used `standalone.html`, a second page shell with its own top bar (no theme toggle,
  languages or menu), footer, type and a 560px breakpoint. `fullBleed` removed the text column once
  the reports gained prose, so paragraphs ran 0px from the right edge at every width. Reports are now
  ordinary Tech articles; the frame widens with a shared `.u-breakout`, also used by the project
  gallery. Removes `standalone.html`, `standalone.css`, `check-bundles.py`, three front-matter
  params, one token and one i18n key. Also satisfies S6.

### Phase 3 — Speed

- [x] **P1 · Profile photo.** `sizes` matches the displayed width (153–200px); renditions at 200w,
  400w and 600w.
  - *Where:* `partials/index_profile.html`.
  - *Done when:* home image bytes drop from 131 KB to ≤ 20 KB on a 3× phone, and home LCP ≤ 1.5 s.
- [x] **P2 · Index covers.** List-page covers render at card width in WebP with a correct `sizes`.
  - *Where:* PaperMod's `partials/cover.html` (fork it) or a list-only partial.
  - *Done when:* Lighthouse "properly size images" and "next-gen formats" pass on `/tech/`, saving
    about 426 KB.
- [x] **C7 · List eyebrow wraps mid-phrase on phones.** "AUGUST 20, 2026 · 3 MIN" breaks between
  "3" and "MIN" at 390px on list pages (live too).
  - *Done when:* date and reading time never split inside a unit at 360–414px in EN/FR/AR.

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
- [x] **S6 · Report pages.** The standalone layout emits `hreflang`, canonical and `TechArticle`
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
| D3 | Phone menu — decided: compact two-row wrap (measured: +5px header at 360–390, no overflow; scroll clipped Search; tighter spacing needed 13px text) | C5 |

---

## 7. Done log

| Item | Commit | Before | After | Notes |
|---|---|---|---|---|
| K1 | `e28e720` | 22 lines, 9 comments | 11 lines | same ignored set |
| K2 | `70ed507` | 22 comment lines in 3 archetypes | 0; field docs in ARCHITECTURE.md and projects-playbook.md | all 4 archetypes scaffold and build |
| R1 | `18bd70c` | 15 files flat in `scripts/` | entry points + `checks/` (9) + `generate/` (4) | gates pass; gates resolve the repo from any cwd; OG generator output byte-identical |
| R2 | `985449d` | 31 partials, 20 project-owned mixed with theme names at the root | root = PaperMod names only; 8 domain folders | build byte-identical (386 files); bundle gate now follows partial calls instead of a list that skipped missing files |
| R3 | `ecec54e` | `MyPhoto.jpg` | `profile.jpg` | build identical apart from the name (diffed) |
| R4 | dropped | — | — | trial diffed: 3 tag indexes fell back to the theme template |
| K3 | `81d75b2` | inline script on 12 Arabic pages | none | only AR pages changed; dir=rtl, mirrored nav, no errors at 390/1440 × light/dark |
| K4 | `39dfa6c` | 2 unused hooks, 17 template lines | 0 | build byte-identical; playbook points styling at 44-adventures.css |
| K5 | `d064cd7` | scaffold draft in docs/, `disableShare: false` ×2 | deleted; reports documented in ARCHITECTURE.md | build byte-identical |
| K6 | `2236d13` | 16 comment lines in inline JS and timeline.js; 2 stale DRAFT notes on published reports | 0 | build byte-identical; all 46 report figures checked against the generated reports first |
| K7 | `380c70b` | 9 comments, 1 always-empty opt-out | 0 | every gate passes with the same counts |
| K8 | `9a6c9ba` | 3 raw colours warned; dead classes only warned; 29-name ignore list; dead `cat-` branch in contrast gate | 3 tokens; both fail the build; no ignore list | computed colours unchanged (#fff frame, #fff icon, #000 lightbox); negative test fails as expected |
| C4 | `6bb8b76` | fork count 16, 3 stylesheets and 12 partials undocumented, stale README lines | counts, tree, tables and docs index match the repo | every backticked path and relative link in both files resolves |
| C1 | `122dbe6` | 4 validator errors; phone labels one letter per line, verdict 1038px tall at 390px; physical `text-align:right` | 0 errors; labels on one line, 504px; logical properties | desktop pixel-identical (antialiasing only), tablet dividers continuous, phone stacks label over value; 2 pages × 3 widths × 2 themes |
| C2 | `83589a4` | ~15 duplicate-width srcsets; `sizes` at 760px (breakpoint is 768); gallery sized 310px (renders 389px); figure shortcode 43 lines with 9 unused params and an unreachable branch; 8 ignored `width`/`align` in content; duplicated media rule | 0 validator errors on site pages; sizes match layout; shortcode 21 lines, fails the build on a missing image | figure fig-w/src/width/height identical on all 9 pages; images checked at 390/1440 |
| M1 | `6ecaad4` | manual tool runs | one command, exit 1 when under budget | live run matched §4 within noise; flags article a11y 96 (C3); resume mobile CLS 0.088 this run (look at in P4) |
| M2 | `0c59735` | no HTML validation | gate on 130 pages, 2 s | fails on a reintroduced `<dl>` error; jar pinned by sha512; ran green in CI (run 34757852355) |
| C3 | `5439011` | comments 3.61:1 (light) / 2.89:1 (dark); code element scrolls without focus | `--code-comment` 5.97:1 / 4.79:1; `pre` (tabindex=0) scrolls | axe 0 contrast / scrollable violations on 3 code pages × 2 widths × 2 themes; block sizes identical |
| C3 fix | `59e22d4` | C3 pushed with the CSS gate failing on `.cm`/`.cpf` | gate counts the highlighter's class vocabulary as rendered | all gates pass; lesson: the commit chain now runs check.sh first |
| M3 | `0b77a5e` | 16 token pairs | 142 pairs: tokens + every syntax colour after site overrides, on both code backgrounds | removing the comment override fails the gate |
| C5 | `d092b08` | EN/FR menu overflowed 5–52px at 360–390, Search clipped, scrollbar visible | wraps to a centred second row, 40px taps | 5 pages × 10 widths (360–1440): 0 overflow, 0 clipped, no horizontal scroll; header 135→140px at 360–390, 135→100px at 414–600 |
| C6 | `0915391` | back-to-top outside a landmark once scrolled; no focus ring (theme `outline:0` beat the global rule); focus rule duplicated in 44-adventures.css | inside `<footer>`; 2px focus ring; one global focus rule | axe 0 after scroll on 4 pages × 2 widths × 2 themes; button position, size, colour identical to live |
| C6b | `ed3e8cf` | theme toggle and TOC summary had no keyboard focus ring (theme `outline:0`) | both use the global accent ring | tab walk on article (light/dark) and search: every focusable control shows a ring; the search input keeps the theme's border highlight |
| P1 | `ab5e6fb` | `sizes=380px`, 380w/760w q72–q58: 131 KB on 2×/3× screens | `sizes` 180px/200px, 200w/400w q60: 12 KB at 1×, 44 KB at 2–3× | chosen file verified at 390@2x/3x, 768@2x, 1440@1x/2x; q60 vs q72 indistinguishable at 400px; LCP re-measured live at phase end |
| P2 | `fbd2fb8` | list thumbnails served original JPEG/PNG + JPEG resizes with `sizes` 720px: 517 KB on /tech/ | site-owned `article/cover.html`, 100/200/300w WebP, `sizes=100px`: 39 KB at 3×, 23 KB at 2×; tag pages no longer ship hidden covers; theme cover path, the unused adventures hero and 3 config params removed | thumbnails pixel-equivalent at 390@3×; og gate passes |
| C7 | `376294e` | "3 / MIN" and dates split across lines on EN/FR lists at 360–390px | each eyebrow unit is unbreakable | 4 list pages × 4 widths (320–414) × EN/FR/AR: 0 split units, no overflow |
| R5 | `ad7a63a` | report prose 26px left / 0px right at every width; separate shell without toggle, languages, menu, hreflang | text column like every article (278/275px at 1440, 31/28px at 390); frame 1200px centred; site header and SEO head | gallery geometry identical at 390–1920; frame height stable within 1s, no inner scrollbar, EN light/dark 390/768/1440 |
| U3 | `c9f87f7` | resume ended with "Back to Ibraverse" and a lone "Next: Search" card; prev/next were grey cards unlike the accent back link | section nav only inside a section; previous/next use the accent arrow link style with the title below | article (EN/AR), project 390, first-in-series; AR arrows mirror; resume has no section nav; gates pass |
| U4 | `3a46ccc` | "Save as PDF" printed 6 pages: screen cards, accent bars, rail, screen type; dark theme would print light text on white; first date digit clipped | 3 pages EN/FR, 2 AR (A4 and Letter): flat, compact, always light ink; print spacing/type are token values; print rules in one last-in-cascade `60-print.css` | PDFs rendered and inspected EN/FR/AR; screen light/dark unchanged; gates pass |
| U4b | `d0ec351` | Chromium ignored break-after:avoid, stranding an entry header at the foot of Arabic A4 page 1 | each timeline entry prints whole | 6 PDFs (EN/FR/AR × A4/Letter) checked: no stranded headers; EN/FR 3 pages, AR 2–3 |
| U5 | `ce9cc91` | "Start here" block on /projects/ | removed with its CSS, `startHere`/`startHereWhy` front matter (4 files) and i18n key (3 languages) | /projects/ EN/FR/AR × 390/1440 × light/dark render without it, no overflow |
| U2b | this commit | gutters 14px at ≤768px (jump from 53px at 769); light list pages on `bg-alt`, articles on paper | 16px ≤600, 24px 601–1024, centred column above; one background on every page | 14 page types × 11 widths (320–1440): symmetric gutters, no overflow, menu fits |

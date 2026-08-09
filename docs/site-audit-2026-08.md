# Site audit — August 2026

Measured against the `site-overhaul` branch, built with
`hugo --gc --minify --baseURL https://ibraverse.ca/` and served from `public/`.
Lighthouse 12, headless Chrome. Every number below was produced by running
something, not estimated.

**Read the caveats in §1 before acting on the Lighthouse output** — two of its
loudest complaints are artifacts of the local test server and are already
handled in production.

---

## 1. Scores

| Page | Preset | Perf | A11y | Best practices | SEO |
|---|---|---:|---:|---:|---:|
| Home | desktop | **97** | 92 | 100 | 100 |
| Home | mobile | **85** | 92 | 100 | 100 |
| `/projects/tikipro/` | desktop | **97** | 96 | 100 | 100 |

### Core Web Vitals

| Metric | Home desktop | Home mobile | Project page | Target |
|---|---:|---:|---:|---:|
| LCP | 1.1 s | **3.8 s** | 1.1 s | < 2.5 s |
| FCP | 0.8 s | 2.5 s | 0.9 s | < 1.8 s |
| TBT | 0 ms | 10 ms | 0 ms | < 200 ms |
| CLS | 0.057 | 0.003 | 0.002 | < 0.1 |
| Total transferred | — | **649 KiB** | 396 KiB | < 500 KiB |

### Two Lighthouse findings that are NOT real

- *"Enable text compression — 51 KiB"*. The local `python -m http.server` does
  not gzip. GitHub Pages does: `content-encoding: gzip` confirmed on
  `https://ibraverse.ca/`.
- *"Use efficient cache lifetimes — 349 KiB"*. Partly real, but not fixable
  here: GitHub Pages sends `cache-control: max-age=600` for everything and does
  not accept custom headers. Assets are already content-hashed, so they *could*
  be cached for a year on a host that allows it. This is an argument for a CDN
  in front, not a code change.

---

## 2. Performance — what actually costs time

### 2.1 The profile photo is the whole mobile problem

```
static/images/MyPhoto.jpg   760 × 960 px   324 KB   displayed at 380 px wide
```

It is the **LCP element** on the home page and the single heaviest resource on
the site. It ships raw: no resize, no WebP, no `srcset`.

**Root cause, and it is structural.** Files in `static/` are copied verbatim;
only `assets/` goes through Hugo Pipes. `index_profile.html` calls
`resources.Get` on `images/MyPhoto.jpg`, gets `nil` because it lives in
`static/`, and silently falls through to the raw `absURL` branch. The image
pipeline exists and this file simply never enters it — the same pipeline that
correctly produces WebP + `srcset` for every project gallery.

### 2.2 Google Fonts blocks first render for 851 ms

One render-blocking stylesheet, then three font files (43 + 30 + 15 KiB) from a
second origin. Three DNS lookups and TLS handshakes before any text paints.

### 2.3 Google Analytics is the largest script on every page

`gtag/js` is **165 KiB** — larger than the CSS bundle, the HTML, and all our own
JavaScript combined. Our own JS is 1 KB.

### 2.4 Weight breakdown

| | Size |
|---|---:|
| `public/` total | 6.6 MB |
| — the Hydro-Québec report artifact alone | **1.4 MB** |
| — all other images | 3.2 MB |
| — all HTML | 2.4 MB |
| CSS bundle (one file, fingerprinted) | 51 KB |
| Our JavaScript | 1 KB |

The report is a generated Plotly document in an iframe. It is lazy-loaded and
only affects one page, but it is 21% of the site.

---

## 3. Accessibility — three real defects

### 3.1 `--ink-mute` fails contrast for normal text, in both themes

The contrast gate added in #8 checked **accents against `--bg`** and stopped
there. It never checked the text tokens. Running the full matrix:

| Theme | Token | on `--bg` | on `--bg-alt` | Verdict |
|---|---|---:|---:|---|
| light | `--ink` | 17.02 | 15.71 | OK |
| light | `--ink-soft` | 8.68 | 8.01 | OK |
| light | **`--ink-mute`** | **3.41** | **3.15** | **fails 4.5:1** |
| light | `--accent` | 5.73 | 5.29 | OK |
| dark | `--ink-mute` | **4.46** | **4.13** | **fails 4.5:1** |

`--ink-mute` is the eyebrow / meta / caption colour, so this affects the mono
labels everywhere: `LATEST`, post dates, section counts, stack chips, the
footer. It passes the 3:1 bar for large text but is used at 11–13 px.

### 3.2 Body links are distinguishable by colour alone

`.post-content a` sets colour and a faint `text-decoration-color`, giving
**1.51:1 against the surrounding text** — below the 3:1 required when colour is
the only signal.

### 3.3 The language switcher's accessible name does not match its label

`<a aria-label="العربية">Ar</a>` — a speech-input user saying "Ar" cannot
activate it. Same for `Fr`.

---

## 4. SEO

Lighthouse SEO is **100/100** on every page tested. The gaps are the ones
Lighthouse does not check.

### 4.1 `robots.txt` points at the wrong domain — real bug

```
Sitemap: https://brmel.github.io/sitemap.xml
```

The site is `ibraverse.ca`. This has been wrong the whole time.

### 4.2 Structured data

| Type | Pages |
|---|---:|
| `BreadcrumbList` | 25 |
| `BlogPosting` | 13 |
| `Organization` | 3 |
| **none** | **50** |

The 50 are tag and category term pages. More usefully: **project pages emit
`BlogPosting`**, which is wrong — they describe software, not articles.
`SoftwareApplication` or `CreativeWork` would let a search engine (or an agent)
understand what they are. There is no `Person` schema anywhere, which is the
single most valuable one for a portfolio.

### 4.3 Smaller items

- `hreflang` has no `x-default`.
- `tech/image-histograms` emits **two `<h1>`** — the markdown body repeats the
  title.
- The Hydro-Québec standalone page emits **no `<h1>`** (`hideAutoHeader: true`).
- 404 pages have no `<h1>`.

---

## 5. Agentic SEO — nothing exists yet

This is the largest gap, and the cheapest to close.

| Signal | Status |
|---|---|
| `llms.txt` | **missing** |
| `llms-full.txt` | **missing** |
| Markdown endpoints (`/page.md`) | **0** |
| AI-crawler rules in `robots.txt` | **0 directives** |
| `Person` / `SoftwareApplication` schema | **missing** |

What is already right: **every page renders its full text in static HTML** — 652
words on `/projects/tikipro/` with no JavaScript required. Nothing is hidden
behind hydration, so any crawler that fetches the page gets the content. That is
the hard part, and it is done.

What is missing is the part that makes an agent *choose* this site: a single
entry point describing what is here, and a clean text representation it can
quote without stripping tags.

### Why `llms.txt` matters here specifically

An agent asked *"who has built transit software for Algeria"* or *"show me
someone who ships Flutter and machine vision"* needs to answer from a summary,
not by crawling 134 pages. `llms.txt` is that summary, and the convention is
being adopted by the crawlers that matter.

### Thin pages worth noting

The thinnest real pages are the taxonomy indexes (22–27 words). They are
indexable and say almost nothing.

---

## 6. Architecture

### 6.1 Shape

| | Files | Lines |
|---|---:|---:|
| `layouts/` (ours) | 37 | 1,670 |
| `assets/css/` | 8 | 1,547 |
| `assets/js/` | 2 | 82 |
| `themes/PaperMod/` (vendored) | 120 | — |

Healthy for a Hugo site. The token system holds: **three hardcoded hex values
outside `tokens.css`**, all defensible (`#000` shadow, `#fff` iframe ground,
`#999` print rule).

### 6.2 The real scaling risk: 13 forked theme files

| Fork | Upstream | Ours |
|---|---:|---:|
| `partials/header.html` | 149 | 156 |
| `_default/list.html` | 121 | 156 |
| `_default/single.html` | 65 | 82 |
| `partials/share_icons.html` | 95 | 55 |
| `partials/templates/opengraph.html` | 86 | 55 |
| `partials/extend_head.html` | 4 | 47 |
| …and 7 more | | |

Each fork is justified in its own header comment, and each one silently stops
receiving upstream fixes. There is **no record of which upstream version they
were forked from**, so a future PaperMod update cannot be merged — only
re-forked by hand, file by file.

### 6.3 What scales well

- Adding a project is one markdown file. Layout, accent, eyebrow, gallery,
  learning-block row all derive automatically. Asserted, not assumed.
- Adding a section adds a nav entry, a home card, and a slot in `mainSections`.
- Language fallback means new English content appears in `fr` and `ar` the same
  day, labelled.
- The gates catch real defects: `check-orphans.sh`, `check-og.py` (which found
  three live bugs), the stale-data warning.

### 6.4 What does not scale

- **No test of rendered output beyond the three gates.** No check that a page's
  `<h1>` count is 1, that headings nest, or that images have dimensions.
- **`static/` bypasses the image pipeline** — §2.1. Any image put there ships
  raw. Nothing warns.
- **The report artifact is committed at 1.4 MB.** A second one doubles it.

---

## 7. The plan

Ordered by measured impact per unit of work. Each item names what it fixes and
how to verify it.

### Wave A — correctness bugs (do first, all small)

| # | Fix | Verify |
|---|---|---|
| A1 | `robots.txt` sitemap → `https://ibraverse.ca/sitemap.xml` | `curl` it, expect 200 |
| A2 | Move `MyPhoto.jpg` to `assets/`, render through Hugo Pipes with `srcset` + WebP | mobile LCP < 2.5 s, home payload < 400 KiB |
| A3 | Fix `height="auto"` on the profile img (invalid HTML, contributes CLS) | desktop CLS < 0.01 |
| A4 | Language switcher: accessible name must contain the visible text | axe rule passes |
| A5 | Remove the duplicate `<h1>` in `tech/image-histograms` | 0 pages with h1 ≠ 1 |

### Wave B — accessibility (token-level, affects every page)

| # | Fix | Verify |
|---|---|---|
| B1 | Darken `--ink-mute` until it clears 4.5:1 on both `--bg` and `--bg-alt`, both themes | contrast matrix, all cells ≥ 4.5 |
| B2 | Give body links a visible underline, not colour alone | axe link-in-text-block passes |
| B3 | **Extend the contrast gate to every text token**, not just accents, and run it in CI | script fails on a regression |

B3 is the one that matters. B1 fixes today's defect; B3 stops the next one.

### Wave C — agentic SEO (largest gap, cheapest close)

| # | Fix |
|---|---|
| C1 | `llms.txt` — who this is, what each section holds, links to the canonical pages |
| C2 | `llms-full.txt` — full text of every project page and article, concatenated |
| C3 | Markdown endpoints via a Hugo output format, so `/projects/tikipro/index.md` returns clean source |
| C4 | `robots.txt`: explicit rules for `GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`, `CCBot` — an explicit allow is a stronger signal than silence |
| C5 | `Person` schema on the resume; `SoftwareApplication` on project pages instead of `BlogPosting` |

C1–C4 are generated from content that already exists. No new writing.

### Wave D — performance

| # | Fix | Expected |
|---|---|---|
| D1 | Self-host the three font families, `preload` the two used above the fold | −851 ms render block, −3 third-party connections |
| D2 | Load GA on interaction/idle instead of in `<head>`, or drop it for a privacy-friendly counter | −165 KiB per page |
| D3 | Explicit `width`/`height` on every remaining raw `<img>` | CLS → ~0 |
| D4 | Move the Hydro report out of the repo (release asset or object storage), keep the iframe | −1.4 MB, −21% repo |

### Wave E — architecture hardening

| # | Fix |
|---|---|
| E1 | Record the PaperMod commit each fork was taken from, in each fork's header comment, so an upstream update is mergeable |
| E2 | Pin the theme as a submodule/module at a known version rather than a vendored copy |
| E3 | Extend CI: one `<h1>` per page, heading nesting, every `<img>` has dimensions, no raw `static/` images over 100 KB |
| E4 | Add `x-default` hreflang |

### Sequencing

**A → B → C** first: they are small, they fix live defects, and C is the item
with no equivalent anywhere else on the site.
**D** next — real gains but each item is a judgement call (analytics, fonts).
**E** last — it protects future work rather than improving the current site.

### What not to do

- Do not chase the Lighthouse cache-lifetime warning on GitHub Pages. It is a
  host limitation; the answer is a CDN, and the site is not big enough to need
  one.
- Do not optimise the project gallery images. They already go through Hugo
  Pipes, ship as WebP with `srcset`, and total 585 KB for 15 screenshots.

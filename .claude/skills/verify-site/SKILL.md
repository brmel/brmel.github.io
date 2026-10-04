---
name: verify-site
description: Verify a change to the Ibraverse site on screen before calling it done. Use after any change to layouts, CSS, content, front matter, data or i18n strings: runs the build and every gate, then the page × viewport × theme × language overflow matrix with responsive.mjs, then a screenshot review of RTL mirroring, dark theme, phone header, cards and code blocks.
---

# Verify the site

Gates prove structure; this skill proves what a reader sees. Run all three steps for every change to
`layouts/`, `assets/css/`, `content/`, `data/` or `i18n/`.

## 1. Build and gates

```bash
./scripts/check.sh
```

Every gate must pass. A gate failing on a file outside the change is reported as such, never skipped.

## 2. Overflow matrix

Start a server that renders to memory, so `public/` keeps the real build (run it in the background):

```bash
hugo server -M --port 1320 --bind 127.0.0.1
```

Then:

```bash
BASE=http://127.0.0.1:1320 node .claude/skills/verify-site/responsive.mjs
```

| Variable | Default | |
|---|---|---|
| `BASE` | `http://127.0.0.1:1313` | server root |
| `PAGES` | 20 pages: home, resume, project, PariData, Tech, report, field note, topics, search, 404, in EN/FR/AR | comma-separated paths; add every page the change touches |
| `VIEWPORTS` | `320,360,390,768,1024,1440` | widths, or `WxH` |
| `THEMES` | `light,dark` | |
| `SHOOT` | none | widths to screenshot full-page, e.g. `390,1440` |
| `OUT` | `$TMPDIR/ibraverse-responsive` | screenshot folder, outside the repo |

It exits 1 on any HTTP error, horizontal page overflow or element escaping the viewport outside a
scroll container. Text under 12px and targets under 24×24px are listed as warnings: inline links in
prose are exempt; anything else is a finding. Playwright comes from the project or from the global
`@playwright/cli` install; it uses system Chrome and falls back to bundled Chromium.

## 3. Screenshots

Run again with `SHOOT=390,1440` on the affected pages and open the PNGs. For interaction (theme
toggle, phone menu, resume video dialog, PariData stake controls, search), use the Playwright MCP:
`browser_snapshot` for structure, `browser_evaluate` for computed values, `browser_take_screenshot`
for pixels. Look at:

| Area | Correct when |
|---|---|
| Arabic (RTL) | `<html dir="rtl">`; nav, breadcrumbs, eyebrows, card bars, timeline rail and previous/next arrows mirror; `C++` reads "C++"; numbers and dates read left to right inside Arabic text |
| Dark theme | every surface is the dark paper, text and code legible, the report frame follows the theme, no light flash on load |
| Phone header (320–390) | the menu wraps into balanced rows with nothing clipped; logo, theme toggle and language switch fit on one line |
| Cards | project tiles, list cards, home section cards and the PariData dashboard sit on the same two edges as the text; no stranded single card |
| Code blocks | long lines scroll inside the `pre`, which takes keyboard focus; the copy button sits inside the block; the page itself does not scroll sideways |
| Page frame | headings, figures, galleries and report frames align with the text column (1200px on project index, resume, PariData) |

## Done when

- `./scripts/check.sh` passes.
- `responsive.mjs` exits 0 on the default pages plus every page the change touches.
- Screenshots at 390 and 1440 of each affected page type, EN and AR, light and dark, have been opened
  and match the table above.
- The report back names the pages, viewports and themes checked and any warning left open.

Stop the server afterwards.

# Decisions

Why the site is the way it is. One row per decision that still holds; reversed decisions are removed.
Add a row in the same change that makes a decision.

## Structure and build

| Date | Decision | Why |
|---|---|---|
| 2026-08-17 | The resume renders from `experience:` front matter. Degrees are periods with `kind: education`. | As shortcode prose the three languages drifted (EN listed three periods, FR/AR two) and no gate could see it. A degree written as a period states the year, school and title once. |
| 2026-09-13 | Keep Hugo's legacy template folders (`layouts/_default/`, `partials/`, `shortcodes/`). | Under the newer `_partials/` layout the vendored theme's `_default/terms.html` outranks the site's own terms template. |
| 2026-09-13 | Forked theme files carry a one-line header naming the upstream path and commit; files written here that share a theme name carry none. | A theme upgrade can be diffed file by file, and a missing header says "ignore the theme's copy". |
| 2026-09-13 | Reports are ordinary Tech articles. | The separate report shell had no theme toggle, menu, language switch or `hreflang`, and its text ran edge to edge. |
| 2026-09-13 | One stylesheet bundle for every page. | 11 KB gzip, under the 15 KB budget, cached after the first page. Per-page bundles would add a second build path to save about 10 KB once. |
| 2026-09-13 | Audit tools run from `npx` and a pinned `vnu.jar`. | Nothing is added to the repo's dependencies. |
| 2026-09-16 | One page header partial and one page-ending partial for every layout. | Four layouts each built their own header and ending; two ended with none. |
| 2026-09-18 | `layouts/partials/func/dots.html` is the only list separator. | Eleven hand-written copies drifted, one to an element that never got the accent. |
| 2026-09-18 | Every block sits at its page's measure; there is no per-block wide opt-out. | Home cards, galleries and report frames that escaped the text column read as bulges. The measure rule names `.post-content` twice because PaperMod margins `h3`–`h6`, `blockquote` and `iframe` by element, which outranks one class. |
| 2026-09-22 | Tags are topic pages under `/tags/`, grouped by `data/topics.yaml`. | The site had no way to answer "show me the C++ work". |
| — | Duplication kept on purpose: PariData validated both in `layouts/partials/func/paridata-ledger.html` and `scripts/checks/check-paridata.py`; the compass mark inlined in the generator templates; the figure shortcode and the project gallery each building their own responsive image. | The build-time check fails the build where the page is rendered, the gate explains the data. Generator templates are standalone pages. One image partial for both cases would be a parameter bag. |

## Content

| Date | Decision | Why |
|---|---|---|
| 2026-09-13 | Field notes are `BlogPosting` with `contentLocation`, not `Review`. | No front-matter field names the reviewed venue. |
| 2026-09-13 | Titles may run past 60 characters. | The ` \| Ibraverse` suffix comes from PaperMod's `head.html`; making it conditional means forking the whole file. |
| 2026-09-18 | `description` is the only summary line of a page. | Articles also carried a `summary` that said the same thing in other words and rendered nowhere. |
| 2026-09-18 | A report article is the report: prose, then the frame rendered in place, lazy-loaded, themed from the page's tokens. `/reports/` stays disallowed in `static/robots.txt`. | One URL and one click instead of a preview and a second route. Every figure is in the crawlable prose, so the raw report files would only be indexed as duplicates. |
| 2026-09-21 | No pull-quote in project stories. | All nine pages had one in the same slot, so it read as a template. |
| 2026-09-21 | No one-line `takeaway` per project and no aggregated learning list. | Read together the takeaways were one formula; lessons stay on each project, where they can be specific. |
| 2026-09-22 | British/Canadian spelling (colour, behaviour, optimise). | The English was mixed while titles already said Colour. |
| — | Read length shows only from 2 minutes, and never on a page with a report frame. | Hugo counts markdown words, so an embedded report reported "1 MIN" for a page 13,000px tall. |
| — | The project index card drops the word "Project" from its eyebrow and adds the year. | The page is the project index, so the word would repeat on every card; the index is one grid, not year groups. |

## Brand and interface

| Date | Decision | Why |
|---|---|---|
| 2026-09-11 | One accent on every page, in both themes. | Nine category hues changed the brand colour from page to page. The eyebrow names the category in words, which survives greyscale and colour-blindness. |
| 2026-09-13 | The phone menu wraps to balanced rows. | Horizontal scroll clipped Search; tighter spacing needed 13px text. |
| 2026-09-13 | The print stylesheet comes last and always prints light ink. | The dark theme printed light text on white, and screen cards and bars cost pages. |
| 2026-09-16 | Arabic text renders in IBM Plex Sans Arabic. | The three Latin faces have no Arabic glyphs; the face downloads only for Arabic characters. |
| 2026-09-16 | Six social links: GitHub, LinkedIn, X, Email, Facebook, Instagram. | Owner's choice. |
| — | The compass mark appears once per screen, in the nav. | The home hero, resume head and project eyebrow each repeated it under the nav's copy. |
| — | Social cards come from one HTML template; a page shares its cover, else its first gallery image, else its section card, else the home card. | Hand-drawn cards drift. A real product screenshot says more than a generated card. `og:` and `twitter:` read the same resolver so they cannot disagree. |

## Hosting and privacy

| Date | Decision | Why |
|---|---|---|
| 2026-09-13 | The Content-Security-Policy is a `<meta>` tag. | GitHub Pages cannot set response headers; the meta policy still blocks third-party requests in the browser. |
| 2026-09-16 | Google Analytics 4 (`G-CHFGS2DHF6`) is the one third-party runtime request, loaded after the page is idle, with no consent banner. | The owner asked for it back. Loading after idle keeps it off the critical path. Consent is open in [backlog](backlog.md). |
| 2026-09-16 | PariData is anonymous: no links, handles, account names or screenshots of the tipster. | The repository is public. |

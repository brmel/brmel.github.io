# Decisions

Why the site is the way it is. One row per decision that still holds; reversed decisions are removed.
Add a row in the same change that makes a decision.

## Structure and build

| Date | Decision | Why |
|---|---|---|
| 2026-08-17 | The resume renders from `experience:` front matter. Degrees are periods with `kind: education`. | As shortcode prose the three languages drifted (EN listed three periods, FR/AR two) and no gate could see it. A degree written as a period states the year, school and title once. |
| 2026-10-20 | No theme: the site owns every template, its stylesheet (syntax colours generated at build by `css.ChromaStyles`) and a 40-line search script, in Hugo's current layout (`_partials/`, `_shortcodes/`, `_markup/`). | The site already overrode most of PaperMod; the rest was 120 files, about 40% dead CSS, a 15 KB search library and fork headers to maintain. The move was checked byte for byte against the previous build. |
| 2026-10-20 | Search matches every word of the query in the title, description and first 2,000 characters of each page, accents and Arabic marks ignored, title matches first; results render as list cards and the query stays in the URL. | Fuse.js's fuzzy scoring added 15 KB for 90 pages; Pagefind would cost about 115 KB and split French and Arabic search away from the untranslated English pages. |
| 2026-09-13 | Reports are ordinary Tech articles. | The separate report shell had no theme toggle, menu, language switch or `hreflang`, and its text ran edge to edge. |
| 2026-09-13 | One stylesheet bundle for every page. | 11 KB gzip, under the 15 KB budget, cached after the first page. Per-page bundles would add a second build path to save about 10 KB once. |
| 2026-09-13 | Audit tools run from `npx` and a pinned `vnu.jar`. | Nothing is added to the repo's dependencies. |
| 2026-09-16 | One page header partial for every layout. | Four layouts each built their own header. |
| 2026-10-20 | A page ends with its content. No topic chips, issue link, social icons, author card, related project or previous/next; the site footer is the copyright line. | The owner found the ending noisy: it repeated the resume, the nav and the social links on every page. |
| 2026-10-20 | No breadcrumbs; the nav marks the section the page belongs to. | Breadcrumbs repeated the nav as one more row above every title. |
| 2026-10-20 | The home page is the profile, the intro, four featured cards and four latest cards. | The career strip repeated the resume, the section cards repeated the nav, and a fifth card sat alone on a row. |
| 2026-09-18 | `layouts/_partials/func/dots.html` is the only list separator. | Eleven hand-written copies drifted, one to an element that never got the accent. |
| 2026-09-18 | Every block sits at its page's measure; there is no per-block wide opt-out. | Home cards, galleries and report frames that escaped the text column read as bulges. The measure rule names `.post-content` twice so that no element rule inside an article can override it. |
| 2026-09-22 | Tags are topic pages under `/tags/`, grouped by `data/topics.yaml`. | The site had no way to answer "show me the C++ work". |
| — | Duplication kept on purpose: PariData validated both in `layouts/_partials/func/paridata-ledger.html` and `scripts/checks/check-paridata.py`; the compass mark inlined in the generator templates; the figure shortcode and the project gallery each building their own responsive image. | The build-time check fails the build where the page is rendered, the gate explains the data. Generator templates are standalone pages. One image partial for both cases would be a parameter bag. |

## Content

| Date | Decision | Why |
|---|---|---|
| 2026-09-13 | Field notes are `BlogPosting` with `contentLocation`, not `Review`. | No front-matter field names the reviewed venue. |
| 2026-10-20 | Every title is "<page> \| Ibraverse"; the home page's is the owner's name. Titles may run past 60 characters. | One rule for every page; the home title was "Ibraverse" alone in every language. |
| 2026-10-21 | A page's modified date comes from `lastmod` in front matter, never from git. Pages carry no notes about earlier versions, corrections or old URLs. | Git dates moved on every typo fix and rename, so `dateModified` said nothing. The site has no returning readers who need a change history, so it shows only the current version. |
| 2026-09-18 | `description` is the only summary line of a page. | Articles also carried a `summary` that said the same thing in other words and rendered nowhere. |
| 2026-10-20 | A report article is the report alone: no introduction above it, no border or shadow around the frame, the report's own header hidden and its side padding removed so it sits on the text column. `/reports/` stays disallowed in `static/robots.txt`. | An introduction that repeated the report's numbers, then a boxed report with its own title, read as two articles. The cost: the crawlable text of those pages is the title and the description. |
| 2026-10-11 | Maths is LaTeX in the markdown, rendered to MathML at build time, with no script or maths font. | Hugo ships KaTeX, so the page gets real equations with no third-party request and no JavaScript; browsers render MathML natively. A thin space follows `\cos` and `\sin` because Chrome drops the function-application gap. |
| 2026-09-21 | No pull-quote in project stories. | All nine pages had one in the same slot, so it read as a template. |
| 2026-09-21 | No one-line `takeaway` per project and no aggregated learning list. | Read together the takeaways were one formula; lessons stay on each project, where they can be specific. |
| 2026-09-22 | British/Canadian spelling (colour, behaviour, optimise). | The English was mixed while titles already said Colour. |
| 2026-10-20 | The site gives Brahim his job title, Senior Software Developer (« développeur logiciel senior », «مطور برمجيات أول»), and never calls him an engineer. Degree names such as « Ingénieur d'État » stay. | Québec's Engineers Act reserves the title "engineer" for members of the Ordre des ingénieurs du Québec. |
| 2026-10-20 | Matrox-era work names the product as it is sold today ("the Matrox Imaging Library, today Zebra's Aurora Imaging Library"), and the Matrox Imaging period links to it. | Matrox Imaging's own site and product names are gone since Zebra's acquisition. |
| 2026-10-20 | A resume period carries its work items, `stack` and `learned`; no `built` or `tools` list. | Both repeated the work titles above them and the Skills section below. |
| 2026-10-20 | The home intro and resume say what a product is in plain words before the detail ("the Aurora Imaging Library, Zebra's machine vision SDK"). | A recruiter or a reader outside machine vision reads the first sentence of each entry and stops. |
| — | Read length shows only from 2 minutes, and never on a page with a report frame. | Hugo counts markdown words, so an embedded report reported "1 MIN" for a page 13,000px tall. |
| 2026-10-20 | One list card everywhere (section indexes, projects, topics, home): a 16:9 thumbnail, a meta line, the title and one line of text. The thumbnail is the cover, else the first gallery image, else the compass mark. Projects and field notes carry no number. | Four card designs made every list look different, and a card without an image broke its grid. |

## Brand and interface

| Date | Decision | Why |
|---|---|---|
| 2026-09-11 | One accent on every page, in both themes. | Nine category hues changed the brand colour from page to page. The eyebrow names the category in words, which survives greyscale and colour-blindness. |
| 2026-10-20 | The menu has no Home item. | The logo already links home, and six items fit the phone menu in two even rows. |
| 2026-10-20 | A field note's verdict sits above the body. | Readers come for the answer first (The Infatuation, Wirecutter); the practical list at the end keeps the details. |
| 2026-10-20 | A report article lists its key findings and its data and method after the report, from front matter. | The report frame is invisible to search engines and screen readers; the facts belong in text (The Pudding, Our World in Data). This does not bring back an introduction above the report. |
| 2026-10-20 | A video in an article is a self-hosted poster linking to YouTube, never an embedded player. | An embed loads YouTube's scripts and cookies for every reader; the poster costs one local image. |
| 2026-10-20 | No back-to-top button. | It needed a scroll listener outside the allowed JavaScript, and pages end with their content. |
| 2026-09-13 | The phone menu wraps to balanced rows. | Horizontal scroll clipped Search; tighter spacing needed 13px text. |
| 2026-09-13 | The print stylesheet comes last and always prints light ink. | The dark theme printed light text on white, and screen cards and bars cost pages. |
| 2026-09-16 | Arabic text renders in IBM Plex Sans Arabic. | The three Latin faces have no Arabic glyphs; the face downloads only for Arabic characters. |
| 2026-10-20 | No social, contact or "first published on" links anywhere on the site. Profile URLs stay only in the JSON-LD `sameAs`. | Owner's choice: they repeated on every page. |
| 2026-10-20 | A Google-like interface: white and neutral grey surfaces, Inter Tight for every heading, sentence-case labels, list cards with no outline (a rounded 16:9 picture over the text), filled grey panels instead of borders and dividers, one 16px radius. The accent and the mark stay. | The owner asked for a calmer, uniform look; serif titles and mono uppercase labels read as a magazine and added noise. |
| 2026-10-20 | The resume header is one row (the name and "Save as PDF") over the role line. | Location, contact links and breadcrumbs made four rows above the career; the location stays in the JSON-LD. |
| 2026-10-20 | The compass mark is the nav logo and the thumbnail of a card with no image, nowhere else. | A card needs a picture; the mark is the brand rather than a stock image. |
| 2026-10-21 | One size for every section heading: article `h2`s and the `.u-heading` sections ("Experience", "Gallery", "Start here") share `--t-section`, 1.3 × the prose size. Sections sit 48px apart (40px on phones). | A project page mixed 36px and 24px headings for the same level, and article `h2`s were as big as the page title on phones. The owner found the gaps between sections too large. |
| 2026-10-21 | A project's eyebrow is year · status; there is no domain. | Several domains were wrong (TikiPro as SaaS, three different projects as Infrastructure), and the stack chips already say what a project is. |
| 2026-10-21 | No two topics list the same pages. | Five pairs of topic pages were identical. |
| 2026-10-21 | The 404 page is its title and one sentence. | It repeated the header's menu and language links. |
| — | Social cards come from one HTML template; a page shares its cover, else its first gallery image, else its section card, else the home card. | Hand-drawn cards drift. A real product screenshot says more than a generated card. `og:` and `twitter:` read the same resolver so they cannot disagree. |

## Hosting and privacy

| Date | Decision | Why |
|---|---|---|
| 2026-09-13 | The Content-Security-Policy is a `<meta>` tag. | GitHub Pages cannot set response headers; the meta policy still blocks third-party requests in the browser. |
| 2026-09-16 | Google Analytics 4 (`G-CHFGS2DHF6`) is the one third-party runtime request, loaded after the page is idle, with no consent banner. | The owner asked for it back. Loading after idle keeps it off the critical path. Consent is open in [backlog](backlog.md). |
| 2026-09-16 | PariData is anonymous: no links, handles, account names or screenshots of the tipster. | The repository is public. |
| 2026-10-20 | The Hydro-Québec report maps have no basemap: the regions are drawn on the page background. | CARTO's free tiles now print "API key required" across the map, and the tiles were one more third-party request. |

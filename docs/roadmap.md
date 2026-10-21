# Roadmap

Small steps that move the site forward, one change each. Each comes from what comparable sites do
well or from a measured gap in this repo. Ship a step, run `./scripts/check.sh` and the
`verify-site` skill, record any decision in [decisions](decisions.md), and move it to Shipped.

## What comparable sites teach

Read on 2026-10-20: Karpathy, LeCun, Lilian Weng (Hugo + PaperMod, as this site was until October 2026), Chris Olah,
Chip Huyen, Sebastian Raschka, Jay Alammar, Simon Willison, Eugene Yan, Distill, Gwern, Ciechanowski;
Bruce Dawson, Raymond Chen, Fabien Sanglard, Julia Evans, Dan Luu, Eli Bendersky, Jeff Preshing, Aras
Pranckevičius, Inigo Quilez, Matt Godbolt, Arthur O'Dwyer, Herb Sutter, Daniel Lemire, Ash Vardanian
(also Hugo + PaperMod); portfolios, case studies, data stories, field notes and trilingual sites listed
under each step.

| Pattern on the best sites | Here before 2026-10-20 |
|---|---|
| Who they are in one first-person line, then the work | a name, a role line and a five-paragraph intro before the first card |
| Every page dated; revisions and corrections dated and visible ("Update, April 26, 2025: …") | publish date only; `dateModified` comes from git, so a typo fix counts as an update |
| Evidence on the page: machine, versions, tables, the code in a repo, the outcome (PR merged, still open) | strong in places, uneven across articles |
| Articles end with references or further reading; asides in footnotes | Sources on some articles; footnotes unstyled |
| Case studies lead with a result against a baseline, name what was rejected, give the regret a heading | metrics often describe scope ("1 command", "Sandboxed") |
| Data stories put key findings and "Data and methods" in text beside the charts | the two report articles are a frame only: no crawlable text |
| Field notes use fixed slots (distance, climb, cost, month visited) and a published rating scale | verdict at the end, facts in prose, rating undefined |
| A feed link a reader can see | feeds exist (per section and per topic) but no page links them |
| No share buttons, comments, pop-ups, hero images or related-post widgets | already true after the 2026-10-20 redesign |

## Shipped on 2026-10-20

Hugo 0.168 with Node 24 actions; the deprecated keys and the language-relative aliases fixed; i18n
and deprecation warnings fail the build. Arabic headings without letter-spacing at weight 600;
native controls follow dark mode; the profile photo in AVIF. Dated `updates` lines and `lastmod`
from front matter, with the B15 corrections in both Windows articles. The site's own head, one
JSON-LD graph per page, its own stylesheet and a 40-line search; PaperMod removed and the templates
in Hugo's current layout, byte-identical output. Key findings and data and methods after both
reports; the K-means article ends with the fix that shipped; field-note verdicts first; a shorter
home, the "in practice" list on the resume and a dated resume. The language switch keeps the
section on untranslated pages; topic pages name their related topics; prefetch and view
transitions.

## Shipped on 2026-10-21

A six-point resume summary and a home intro that name machine learning from prototype to production,
deep learning evaluation and constrained camera hardware. Tighter, uniform spacing and one
section-heading size; a shorter phone header; each project fact in one place; five duplicate topics
merged; a one-sentence 404; French and Arabic wording made consistent.

## Still open (owner)

1. **Projects as results.** One metric per project against a baseline, one "considered and
   rejected" line, a year range, and a sentence defining `active` (B13). Sources:
   [Discord](https://discord.com/blog/how-discord-stores-trillions-of-messages),
   [Notion](https://www.notion.com/blog/sharding-postgres-at-notion),
   [MacWright](https://macwright.com/projects/).
2. **Tech articles as evidence.** A "measured on" sentence (machine, OS build, tool versions) where
   there are numbers; references on the articles that have none; one companion code repo with a
   folder per article; Compiler Explorer links under the C++ snippets. Footnote styles land with the
   first article that uses a footnote. Sources: Daniel Lemire, Fabien Sanglard, Arthur O'Dwyer.
3. **A rating scale** on the Adventures index: what 3, 4 and 5 mean. Source:
   [The Infatuation](https://www.theinfatuation.com/ratings-explainer).

## Open choices for the owner

| Choice | Trade-off |
|---|---|
| One quiet way to reach you (email on the resume, or an issue link) | every site above has one; without it nobody can report an error |
| A visible feed link (footer or Tech index) | the one subscription channel that needs no social account |
| Tech as a dated title list instead of cards, once it passes about 20 articles | how Karpathy, Sanglard, Luu and Aras list writing |
| A licence line for code snippets | the copy button invites copying; say whether readers may |
| An AI-assistance note on pages an LLM helped edit | Matt Godbolt's one-line form |
| Cite-this lines on reference articles (ellipse, edge measurement) | Lemire, Lilian Weng, Eugene Yan |

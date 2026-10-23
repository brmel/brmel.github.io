---
name: publish-content
description: Add or change content on the Ibraverse site — a new project page, Tech article, report article, Adventures field note, PariData ticket or result, or a French/Arabic translation. Routes to the right playbook, lists the front matter the layouts read, and names the gate that catches each mistake.
---

# Publish content

Every section renders its chrome from front matter, so publishing is: scaffold, fill the fields the
layouts read, write prose in the voice, verify. Read the playbook for the section before writing.

| Adding | Scaffold | Read first |
|---|---|---|
| Project | `hugo new projects/<slug>/index.md` | [docs/projects-playbook.md](../../../docs/projects-playbook.md) |
| Field note | `hugo new adventures/<slug>/index.md` | [docs/adventures-playbook.md](../../../docs/adventures-playbook.md) |
| Tech article | `hugo new tech/<slug>/index.md` | the Content section of [ARCHITECTURE.md](../../../ARCHITECTURE.md) |
| Report article | a Tech article, then `{{< reportframe src="reports/<file>.html" title="…" >}}` with the file in `assets/reports/` | the report paragraph in ARCHITECTURE.md |
| PariData ticket or result | edit `data/paridata/` | [docs/paridata-playbook.md](../../../docs/paridata-playbook.md) |
| Translation | `index.fr.md` or `index.ar.md` beside `index.md` in the same bundle | the Languages section of ARCHITECTURE.md |

New pages start as `draft: true`; preview with `hugo server -M -D`, and remove `draft` to publish.

## Rules every page follows

- One page bundle: markdown plus its images. Covers and figures live in the bundle, never in `static/`.
  File names are kebab-case and numbered in reading order (`02-vmmap-snapshot.jpg`).
- Images go through `{{< figure src="…" alt="…" caption="…" >}}`, never raw `<img>` or Markdown images.
- `description` is 50–160 characters, unique per language, and is the line the reader sees on cards
  and in the meta tag. A project's `pitch` and `description` are the same sentence.
- Tech and Adventures pages need `cover.image` (a file in the bundle) and `cover.alt`.
- Copy follows the `voice` skill. A translated page has its own title and description, written in
  that language, and every `C++` in Arabic is written `‎C++‎` (U+200E on both sides).

## What fails, and where

| Mistake | Caught by |
|---|---|
| cover without `alt`, or no resolvable social image | `check-og` |
| figure or cover file missing from the bundle | the Hugo build |
| page not linked from its section index | `check-listings` |
| description too short, too long or duplicated; missing `hreflang`/canonical | `check-seo` |
| missing `h1`, unsized image, no skip link | `check-chrome` |
| dead internal link, link to itself, unlinked page | `check-pages` |
| invalid HTML from raw markup in Markdown | `check-html` |
| PariData coupon pointing at an unknown or undated match, incoherent odds | `check-paridata` and the build |

Then run the `verify-site` skill on the new page in EN, FR and AR, light and dark.

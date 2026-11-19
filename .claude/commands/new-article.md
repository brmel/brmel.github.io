---
description: Scaffold a new Tech article in EN, FR and AR with the SEO fields pre-wired
argument-hint: <slug> "<pillar>"
allowed-tools: Bash(hugo *), Read, Write, Edit
---

Scaffold a new Tech article from $ARGUMENTS: a kebab-case slug and one pillar —
Machine Vision Up Close, Engineering Judgment, Field Notes, or Built in Public.

1. Run `hugo new tech/<slug>/index.md`. The archetype starts the page as a
   draft with its cover fields.
2. Create `index.fr.md` and `index.ar.md` beside it in the same bundle, with
   the same front matter. Each language gets its own title and its own
   description of 50–160 characters, written in that language — never a
   machine copy of the English. In Arabic, every `C++` is written `‎C++‎`
   (U+200E on both sides).
3. Pre-wire the SEO fields in all three files before any prose: `title`,
   `description`, `cover.image` (a file that will live in the bundle) and
   `cover.alt`, `date`. `check-seo` and `check-og` fail on anything missing.
4. Open on the concrete thing, in the voice skill's register. The piece must
   land an engineering lesson and end on a measurable claim — a metric, a bug
   found, a budget met (the Bridge Rule in AGENTS.md). If the package in
   `docs/content-packages/` names the claim, use that claim.
5. Leave `draft: true` in all three files. Publishing is the owner's step:
   drop the draft flag, run `./scripts/check.sh`, then the `verify-site`
   skill on the page in EN, FR and AR, light and dark.

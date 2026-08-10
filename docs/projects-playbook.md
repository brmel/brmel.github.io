# Projects Playbook

How to publish a project page. Follow it page by page and don't improvise the
structure — the point is that every project looks the same, so the reader learns
the format once and the work gets faster each time.

Companion to [`brand-guidelines.md`](brand-guidelines.md) (the identity) and
[`adventures-playbook.md`](adventures-playbook.md) (the same discipline applied
to field notes).

---

## 0. The format in one picture

```
┌──────────────────────────────────────────┐
│ ⊙ PROJECT № 01 · SAAS · SHIPPED          │ ← eyebrow: mark + mono caps (auto)
│ TikiPro                                  │ ← serif display title (auto)
│ One line a non-engineer understands.     │ ← pitch (auto)
│ [Electron][TypeScript][Firebase]  LIVE ↗ │ ← stack chips + links (auto)
├──────────────────────────────────────────┤
│ GALLERY  — screenshots from gallery/     │ ← auto, from the page bundle
├──────────────────────────────────────────┤
│ ## The story      ← you write this       │
│ ## The product    ← and this             │
├──────────────────────────────────────────┤
│ WHAT IT TAUGHT ME — lessons (auto)       │ ← from front matter
└──────────────────────────────────────────┘
```

**Everything marked (auto) renders from front matter or the page bundle.** You
write two prose sections and a list of lessons. That is the whole job. If you
find yourself hand-writing an eyebrow, a chip row, or a gallery, stop — the
layout already does it and hand-rolling it is how sections drift apart.

---

## 1. Scaffold

```bash
hugo new projects/<slug>/index.md
```

That copies [`archetypes/projects.md`](../archetypes/projects.md), which contains
every field below with a comment. It starts `draft: true`.

---

## 2. Front matter

```yaml
projectNo: 1                 # stable. Never reused, never renumbered.
domain: "saas"               # saas | mobile | data | infra  → sets the accent
status: "shipped"            # shipped | active | prototype | archived
pitch: "Clinic ticketing that runs on one PC."
stack: ["Electron", "TypeScript", "Firebase", "Ed25519"]
links:
  live: "https://tikipro.web.app"
  repo: ""
takeaway: "One sentence."    # feeds the learning block on /projects/
lessons:
  - "**Bold lead.** Then the detail."
```

| Field | Rule |
|---|---|
| `projectNo` | Manual and permanent. Sorts the index. Renumbering a published project breaks its identity. |
| `domain` | Picks the accent from the register in [`tokens.css`](../assets/css/extended/tokens.css). Adding a domain means adding a hue **and** checking contrast — see brand-guidelines §3. |
| `status` | Localised via `i18n/*.yaml` (`project_status_*`). Don't type a free-text status. |
| `pitch` | One sentence. If a non-engineer can't parse it, rewrite it. Not the tagline from the README. |
| `stack` | The index card shows the **first four**, so order them by what matters. |
| `links` | Keys are localised via `project_link_*`. An empty value is skipped, so leave unused keys blank rather than deleting them. |
| `lessons` | 3–5 bullets, markdown allowed. **At least one must be a real failure.** |
| `takeaway` | One sentence for the learning block. Not a summary of the lessons — the single thing you'd tell someone starting the same project. |

---

## 3. The prose

Two sections, in this order. Both are for a reader who has never heard of the
project.

**`## The story`** — why it existed. What problem, for whom, and why you built it
instead of using something that already worked. Lead with the human situation,
not the architecture.

**`## The product`** — what it actually became. Screens, flows, the one or two
decisions that made it work. Concrete numbers wherever you have them.

> **Never copy README prose.** A README is written for a contributor who has
> already decided to care. A project page is written for someone deciding whether
> to. They are different documents with different jobs.

---

## 4. The gallery

Drop images into the page bundle under `gallery/`, numbered so they order
predictably:

```
content/projects/<slug>/
├── index.md
└── gallery/
    ├── 01-waiting-room-board.png
    ├── 02-marketing-site.png
    └── 03-release-feed.png
```

They render automatically — resized, converted to WebP, fingerprinted, and
served with `srcset`. Nothing to write in the markdown.

**Before committing any image:**

- [ ] **No private data.** Real names, phone numbers, emails, addresses, real
      user records. Use the app's demo or seed data. QA-evidence folders are
      full of real runs — check every frame, not just the first.
- [ ] **No secrets.** API keys, tokens, project IDs, signed URLs in a visible
      address bar.
- [ ] **Compressed.** Cap the long edge around 1400px; Hugo handles the rest.
      Report the added weight in the PR.
- [ ] Capture from the **live public surface** where one exists — it is current,
      correctly sized, and cannot leak anything that isn't already public.

Aim for three to six. A gallery of one looks like a placeholder.

---

## 5. Lessons

The section that makes the page worth reading, and the one most likely to come
out as marketing.

- **At least one real failure.** A lessons list with no scars reads as a
  brochure. The site's voice rule is that one genuine con builds more trust than
  five pros — that applies here more than anywhere.
- **Specific over general.** "Rate limits need names" with the actual limits
  beats "monitoring is important".
- **Bold lead, then the detail.** Scannable first, readable second.
- Write them when the project is fresh. Reconstructed lessons are always
  flatter than remembered ones.

---

## 6. Publish

```bash
./scripts/check.sh          # build + orphaned assets
hugo server                 # then read the page at 1440px and 390px
```

- [ ] `draft: false`
- [ ] Page renders in **en / fr / ar**; Arabic mirrors (eyebrow, chips, gallery,
      lesson ticks all use logical properties, so this should be free — verify
      anyway)
- [ ] Every external link resolves
- [ ] `projectNo` doesn't collide with a published project
- [ ] The card on `/projects/` still reads as the same design system as the
      others — screenshot the grid, not just the page
- [ ] Changing `domain:` changes the accent and **nothing else**; that is the
      test that you used the mechanism rather than working around it

---

## 7. Registry

| № | Project | Domain | Status |
|---|---|---|---|
| 01 | TikiPro | saas | shipped |
| 02 | Wingo | mobile | active |
| 03 | Rekba | infra | active |
| 04 | Farkad | mobile | active |
| 05 | HydroData | data | shipped |
| 06 | Leorra | mobile | archived |

Keep this table current — it is the fastest way to check the next free number.

# Projects playbook

How to publish a project page. Every project page has the same structure, rendered by
`layouts/projects/single.html`; the author writes front matter and two prose sections.

## The page

```
┌──────────────────────────────────────────┐
│ 2025 · Shipped                            │ eyebrow from date and status (auto)
│ TikiPro                                   │ title
│ One line a non-engineer understands.      │ pitch
│ Live ↗  Repo ↗  [Electron][TypeScript]    │ links and stack chips (auto)
│ lede                                      │ three sentences
│ 1 PC · … · …                              │ metrics row
├──────────────────────────────────────────┤
│ ## The story                              │ prose
│ ## The product                            │ prose
├──────────────────────────────────────────┤
│ Gallery                                   │ gallery/ images (auto)
└──────────────────────────────────────────┘
```

The project index card is the same card as every list on the site: the `cover`, else the first gallery image, as a 16:9
thumbnail (the compass mark when there is none), `{year} · {status}`, the title and the
pitch.

## 1. Scaffold

```bash
hugo new projects/<slug>/index.md
```

This copies `archetypes/projects.md` with `draft: true`. Pick the next free number:

```bash
grep -h '^projectNo:' content/projects/*/index.md | sort -n -k2 | tail -1
```

## 2. Front matter

| Field | Rule |
|---|---|
| `title`, `date` | The year of `date` shows on the index card. |
| `projectNo` | Unique and permanent. The index lists the highest first. |
| `status` | `shipped`, `active` (shown as "In progress") or `archived`, through `project_status_<status>`. |
| `pitch` | One sentence a non-engineer can parse. It is the header line, the index card text and the JSON-LD abstract. |
| `description` | 50–160 characters, unique per language; the meta description and `llms.txt`. Usually identical to `pitch`. |
| `lede` | Markdown, three sentences: the problem, what the project does, what changed. It must add to the pitch, not restate it. |
| `stack` | Chips under the page header, in order of importance. |
| `links` | `live` and `repo`, each rendered through the `project_link_<key>` string in the three `i18n/*.yaml` files; a new key needs that string first. A link that starts with `/` points at a page on this site: it shows as "Write-up" (`project_link_writeup`) and opens in the same tab. Empty values are skipped. |
| `metrics` | Up to three `value` + `label` pairs above the body; a value is a number, never a word ("Offline", "Cited"). Every figure also appears, sourced, in the body. They feed the "Project facts" in `llms.txt`. A project with no honest numbers has no metrics. |
| `featured` | Optional. `featured: N` lists the project under "Start here" on the home page, lowest number first. |
| `cover` | Optional `image` (a file in the bundle) and `alt` (starting "Illustration:" for a drawing): the card thumbnail and social card when the project has no screenshot worth leading with. |
| `resources` | Optional `params.caption` per gallery image. Alt text is "<title> screenshot"; the first image is the index-card thumbnail. |

## 3. The prose

Two sections, both for a reader who has never heard of the project. Aim for about 220 words: the lede and
metrics carry the rest. Never reuse README prose.

- `## The story`: why it existed. The problem, for whom, and why it was built instead of using
  something that already worked. Lead with the situation.
- `## The product`: what it became; left out when the lede already says it. Screens, flows, the one or two decisions that made it work,
  numbers where they exist.

Voice: [voice.md](voice.md).

## 4. The gallery

Images in `gallery/` inside the bundle, numbered so they sort:

```
content/projects/<slug>/
├── index.md
└── gallery/
    ├── 01-waiting-room-board.png
    └── 02-marketing-site.png
```

They render after the body at 640px and 1280px in WebP: a landscape shot takes the full column, portrait
shots sit three to a row. Without a `cover`, the first one is the page's social card.
Their alt text is "<title> screenshot"; describe the image in `params.caption`.

```yaml
resources:
  - src: "gallery/01-waiting-room-board.png"
    params:
      caption: "The board in the clinic's waiting room."
```

Before committing an image:

- [ ] No private data: real names, phone numbers, emails, addresses, user records. Use demo or seed data.
- [ ] No secrets: API keys, tokens, project IDs, signed URLs in an address bar.
- [ ] Long edge around 1400px.
- [ ] Captured from the live public surface where there is one.

Three to six images.

## 5. Publish

- [ ] `draft` removed
- [ ] `./scripts/check.sh` passes.
- [ ] The page and the `/projects/` grid checked with the `verify-site` skill, in EN, FR and AR.
- [ ] Every external link resolves.

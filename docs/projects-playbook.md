# Projects playbook

How to publish a project page. Every project page has the same structure, rendered by
`layouts/projects/single.html`; the author writes front matter, two prose sections and the lessons.

## The page

```
┌──────────────────────────────────────────┐
│ Home · Projects                           │ breadcrumbs (auto)
│ PROJECT № 01 · SAAS · SHIPPED             │ eyebrow from projectNo, domain, status (auto)
│ TikiPro                                   │ title
│ One line a non-engineer understands.      │ pitch
│ LIVE ↗  REPO ↗  [Electron][TypeScript]    │ links and stack chips (auto)
│ lede                                      │ three sentences
│ 1 PC · … · …                              │ metrics row
├──────────────────────────────────────────┤
│ ## The story                              │ prose
│ ## The product                            │ prose
├──────────────────────────────────────────┤
│ GALLERY                                   │ gallery/ images (auto)
│ LESSONS                                   │ lessons (auto)
│ topics · discuss · author · back/next     │ page end (auto)
└──────────────────────────────────────────┘
```

The project index card shows `№ {nn} · {year} · {domain} · {status}`, the title, the pitch, a "Live"
marker when `links.live` is set, and the first four `stack` entries.

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
| `projectNo` | Unique and permanent. The index lists the highest first; previous/next follow the number. |
| `domain` | `saas`, `data`, `infra` or `mobile`, shown through `project_domain_<domain>` in `i18n/*.yaml`. A new domain needs that key in all three files. |
| `status` | `shipped`, `active` (shown as "In progress") or `archived`, through `project_status_<status>`. |
| `pitch` | One sentence a non-engineer can parse. It is the header line, the index card text, the related-project card and the JSON-LD abstract. |
| `description` | 50–160 characters, unique per language; the meta description, search and `llms.txt`. Usually identical to `pitch`. |
| `lede` | Markdown, three sentences: the problem, what the project does, what changed. |
| `stack` | Chips on the page; the index card shows the first four, so order by importance. |
| `links` | `live` renders as a localised "Live ↗"; any other key (`repo`) renders title-cased. Empty values are skipped. |
| `metrics` | Three `value` + `label` pairs above the body. Every figure also appears, sourced, in the body. They feed the "Project facts" in `llms.txt`. A project with no honest numbers has no metrics. |
| `lessons` | Three to five markdown strings, each with a bold lead, at least one a real failure. |
| `tags` | Topic pages; see [publishing a new tag](#new-tags). |
| `featured` | Optional. `featured: N` lists the project under "Start here" on the home page, lowest number first. |
| `resources` | Optional `title` (alt text) and `params.caption` per gallery image. |

## 3. The prose

Two sections, both for a reader who has never heard of the project. Aim for about 220 words: the lede,
metrics and lessons carry the rest. Never reuse README prose.

- `## The story`: why it existed. The problem, for whom, and why it was built instead of using
  something that already worked. Lead with the situation.
- `## The product`: what it became. Screens, flows, the one or two decisions that made it work,
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

They render after the body at 640px and 1280px in WebP, and the first one is the page's social card.
Give each a `title` under `resources:`; it becomes the alt text, and without it the alt is the file
path.

```yaml
resources:
  - src: "gallery/01-waiting-room-board.png"
    title: "The waiting-room board showing three called tickets"
    params:
      caption: "The board in the clinic's waiting room."
```

Before committing an image:

- [ ] No private data: real names, phone numbers, emails, addresses, user records. Use demo or seed data.
- [ ] No secrets: API keys, tokens, project IDs, signed URLs in an address bar.
- [ ] Long edge around 1400px.
- [ ] Captured from the live public surface where there is one.

Three to six images.

## 5. New tags

A tag is a topic page. A tag no page used before needs `content/tags/<tag>/_index.md` with a `title`
and a 50–160 character `description`, and a place in a group in `data/topics.yaml` (otherwise it is
listed under "More"). A French or Arabic page carrying the tag needs `_index.fr.md` / `_index.ar.md`
there too.

## 6. Publish

- [ ] `draft: false`
- [ ] `./scripts/check.sh` passes.
- [ ] The page and the `/projects/` grid checked with the `verify-site` skill, in EN, FR and AR.
- [ ] Every external link resolves.

# Adventures playbook

How to publish a field note: a written review of a place with photos, a map link and a verdict.
Every field note has the same structure so readers learn the format once.

## The page

```
┌───────────────────────────────────────┐
│ Hike · Adirondacks · date · N min      │ category, place, date (auto)
│ Title                                  │
│ description                            │
│ VERDICT  go back · best for · con · ★  │ from front matter (auto)
│ hook sentence                          │
│ ## The place          + photo          │
│ ## What I did         + photo          │
│ ## Recommendations    fixed list       │
│ map link (gmap)                        │
└───────────────────────────────────────┘
```

## 1. Scaffold

```bash
hugo new adventures/<slug>/index.md
```

This copies `archetypes/adventures.md` (front matter, figures, map, recommendations) with
`draft: true`. Every photo goes in the same bundle, `content/adventures/<slug>/`.

## 2. Front matter

```yaml
title: "A Walk Through the Old Port"
date: 2026-06-01
draft: true
description: "The reel's hook in one line: list card, home feed, search, Google and social cards."
tags: ["Montréal", "Walking"]
cover:
  image: "cover.jpg"
  alt: "Old Port of Montréal at sunset"
category: "city"
place: "Old Port, Montréal"
rating: 4.2
goBack: "Yes, on a first evening in town."
bestFor: "A free sunset walk after the crowds thin."
con: "Touristy: skip the terraces on the square."
```

| Field | Rule |
|---|---|
| `description` | 50–160 characters, unique per language. |
| `cover` | `image` must be a file in the bundle (the build fails otherwise); `alt` is required (`check-og.py`). It is the list thumbnail and the social card. |
| `category` | `restaurant`, `hike`, `spa`, `event` or `city`; printed capitalised as the eyebrow label. |
| `place` | A real, locatable place; the eyebrow's last part and the JSON-LD `contentLocation`. |
| `rating` | Out of 5, one decimal, consistent with the prose. The verdict block renders only when it is set. |
| `goBack`, `bestFor`, `con` | The verdict rows. `con` is one genuine drawback. |
| `tags` | Topic pages; a new tag needs a topic page, as in the [projects playbook](projects-playbook.md#5-new-tags). |

## 3. The text

- First person, the way the reel talks. The first sentence is the reel's hook.
- 300–700 words, `##` headings, paragraphs of two or three sentences.
- Name the dish, the price, the street, the trail junction, the metro. One genuine con.
- Place name and city in the title, the first sentence and one heading.
- The verdict is never written in the body; it renders from front matter.

Recommendations, same shape every time:

```markdown
- **Go for:** what it's best at
- **Order / try:** the specific thing
- **Skip:** what's not worth it
- **Budget:** $ per person
- **Best time:** when to avoid crowds
- **Getting there:** metro / parking
```

Voice: [voice.md](voice.md).

## 4. Photos and map

Photos are your own and show the place.

- `cover.jpg` plus three to six in-body photos, alternating wide scene and close detail.
- Before committing: long edge ≤ 1600px, about 300 KB or less, EXIF stripped
  (`magick in.jpg -resize 1600x -strip -quality 80 out.jpg`).
- In the body: `{{< figure src="photo-1.jpg" alt="…" caption="…" >}}`. Captions name the moment and
  the time. The first figure loads with high priority, the rest lazily.
- Map: `{{< gmap q="Place name, City" title="…" >}}` renders a link to a Google Maps search.
- Styling goes in `assets/css/44-adventures.css` from tokens; no inline `<style>`.

## 5. Translations

`index.fr.md` and `index.ar.md` in the same bundle share its images; only the prose and the
front-matter strings change. Each needs its own `title` and `description`.

## 6. Checklist

- [ ] Front matter complete; `rating`, `goBack`, `bestFor`, `con` agree with the prose.
- [ ] `cover.jpg` and three to six photos, resized, stripped, with `alt`.
- [ ] Map link and recommendations in the fixed shape.
- [ ] `draft` removed, `./scripts/check.sh` passes, and the page is checked with the `verify-site` skill.

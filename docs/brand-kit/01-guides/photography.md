# Photography

Photos are the one part of the brand that is not drawn. They are first-person, taken by the author at
the place, and never stock or generated. Templates in this kit mark the photo area with a `‹PHOTO›`
placeholder.

## Look

- Natural light: golden hour and the hour after, window light indoors. No flash or strobes.
- Real scenes: a plate with a bite taken, a muddy trail, steam on the glass.
- Eye level or slightly above a table, the trail as seen walking it. Hands welcome; faces optional.
- Warm, slightly desaturated colour. Nothing neon, nothing crushed to black.
- One clear subject with negative space around it.

Avoid over-styling, obvious filters, heavy HDR, vignettes, flat midday glare, mixed white balance,
people used as props, unintended logos and licence plates, and anything that contradicts the written
con.

## Crops

| Ratio | Pixels | Used in |
|---|---|---|
| 16:9 | 1600×900 | wide cover |
| 4:5 | 1080×1350 | Instagram post, carousel, tall cover |
| 1:1 | 1080×1080 | Instagram square, thumbnails |
| 9:16 | 1080×1920 | reel, story, social cover |
| 3:2 | 1500×1000 | in-article images |

Shoot wider than the tightest crop so one frame serves both 16:9 and 9:16.

## Placement

- **Site**: in-article images sit in the 900px text column, never upscaled, with an 8px radius
  (`--radius-sm`) and the caption beneath; the `figure` shortcode does this.
- **Social**: covers, posts, carousels and reels frame the photo with a 14px radius (`--radius-md`)
  and `--shadow-photo`. Text sits on a paper band, never directly on the photo. Keep at least 24px
  between the photo and the mark or eyebrow.

## Grade

1. **None** (default): accurate and warm.
2. **Subtle warm**, for a mixed set: +150–250 K, slightly lifted shadows, −4 to −8 saturation. No LUTs,
   duotone or rust tint; the rust belongs to the accent.

Keep skin tones true; drop the grade if it fights the food or the landscape.

## The `‹PHOTO›` placeholder

A `--bg-alt` fill at the exact crop with a 14px radius and a centred tag: `‹PHOTO›`, the ratio and a
one-line art direction ("golden hour, the dining room, 16:9"), with a corner tick and the mark at 6%
opacity. A real asset replaces it at the same frame and radius.

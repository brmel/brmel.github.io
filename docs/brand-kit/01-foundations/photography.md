# Ibraverse — Photography Direction

Photos are the only thing in the system we don't draw. They must feel **honest, first-person, and
present** — like you were there, not like a catalog. Every render in this kit uses a clearly-labeled
`<PHOTO>` placeholder; **never fake or AI-generate the final imagery.**

---

## 1. The look

- **Natural light, always.** Golden hour and the soft hour after are the house style. Window light
  indoors. No on-camera flash, no studio strobes.
- **Honest, not stock.** Real plates with a bite taken, trails with mud, steam on the glass, a seat
  that's actually yours. A little imperfection reads as truth.
- **Present-tense, first person.** Eye-level or slightly above a table; the trail as you'd see it
  walking it. Hands in frame are welcome. Faces optional and incidental.
- **Quiet color.** Warm, slightly desaturated, paper-friendly. Nothing neon; nothing crushed to black.
- **One subject.** Compose for a single clear thing — the dish, the ridline, the doorway. Negative
  space is good; it's where the eyebrow and title breathe.

## 2. What to avoid

- Stock-y over-styling, fake "lifestyle," obvious filters, heavy HDR, vignette gimmicks.
- Flat midday glare, mixed white balance, dirty-sensor skies.
- People as props. Logos and license plates you didn't mean to feature.
- Anything that contradicts the written con — the photo must tell the same truth as the words.

---

## 3. Crop ratios (match the components)

| Ratio | Pixels | Used in |
|---|---|---|
| **16:9** | 1600×900 | Article hero (wide cover) |
| **4:5** | 1080×1350 | Instagram post, carousel, tall cover detail |
| **1:1** | 1080×1080 | IG square, avatars-of-place, thumbnails |
| **9:16** | 1080×1920 | Reel / story / social cover (photo fills, paper band overlays) |
| **3:2** | 1500×1000 | In-article inline images |

Always shoot wider than the tightest crop you need, so the same frame can ride 16:9 and 9:16.

## 4. How photos sit in the templates

- **Framed:** photos live in a **14px rounded frame** (`--radius-md`) with `shadow-photo`
  (`0 2px 8px rgba(24,23,21,.08)`). The frame is the canonical treatment — social covers, posts,
  carousels, reels.
- **Full-bleed:** article heroes may bleed a photo to the edge with a **paper band** carrying the mark,
  eyebrow, and title over solid paper (never text directly on the photo unless inside a scrim).
- **Inset:** in-article images sit in `container-content` (960px) with the 14px frame, captioned beneath.
- The photo never touches the mark or the eyebrow — keep `space-5` (24px) clearance minimum.

```css
.photo-frame{border-radius:14px;overflow:hidden;box-shadow:0 2px 8px rgba(24,23,21,.08);
  background:var(--paper-alt)} /* placeholder fill while empty */
```

## 5. Treatment (grade)

Two grades only:

1. **None (default).** Accurate, warm, true. Let the natural light do the work.
2. **Subtle warm.** A whisper of warmth for cohesion when a set is mixed: temp +150–250K, a touch of
   lifted shadows, −4 to −8 saturation. Never a heavy or stylized LUT. No duotone, no rust-tint —
   the rust lives in the accent, not the photo.

Keep skin tones honest. If a grade fights the food or the landscape, drop it.

## 6. The `<PHOTO>` placeholder (in this kit)

Every render marks the image area with a labeled placeholder so nothing is faked:

- A `--paper-alt` (or `--bg-alt`) fill at the exact crop, **14px rounded**, with a centered tag:
  `‹PHOTO›` plus the intended ratio and a one-line art-direction note (e.g. *"golden hour, the
  dining room, 16:9"*). A faint corner-tick and the compass mark watermark sit at 6% opacity.
- When producing a real asset, replace the placeholder with the graded photo at the same frame and
  radius — nothing else moves.

*Next: `motion.md`.*

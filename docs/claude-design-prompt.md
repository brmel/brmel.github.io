# Claude Design — Master Prompt (Ibraverse Brand System)

Paste the block below into **Claude Design** with `docs/brand-guidelines.md`
attached and the repo / `ibraverse.ca` connected. It asks for a complete,
production-ready brand package — files, folders, every element, every state.

If Claude Design truncates (it's one large brief), run it in the 6 phases listed
at the very bottom, pasting "Continue with Phase N — same constraints" each time.

---

```
ROLE
You are the lead brand + design-systems designer building the COMPLETE visual identity for "Ibraverse" — a personal site of honest, first-person field reviews (hikes, restaurants, spas/stays, events, city walks) plus a daily "Operating Protocol". I want a finished, production-ready brand package: real files in a real folder structure, every element, every state, visually perfect. Not a moodboard, not a sketch.

SOURCE OF TRUTH (extract, never invent)
- The attached brand-guidelines.md.
- The connected repo / live site ibraverse.ca. Read assets/css/protocol.css, layouts/partials/protocol-fonts.html, the protocol logomark SVG, and assets/css/extended/reels.css. Match what already exists — this brand EXTENDS the Operating Protocol look to everything; it does not replace it.
If any value below conflicts with the repo, the repo wins and you flag it.

BRAND IDEA
Editorial field notes. A quietly confident print magazine: warm paper, ink-black type, ONE rust accent, a compass mark. Calm, not loud. Honest, curious, specific — one genuine con per review. The same recognizable series every time, whatever the subject.

THE HOOK (must appear on EVERY asset, reproducible by rule)
1. Compass-aperture mark — concentric circles (r18, r11, r3-filled) + 4 N/S/E/W ticks. Reuse the exact SVG from the repo; build variants (see below).
2. Eyebrow label — JetBrains Mono, uppercase, ~0.12em tracking, grammar: "FIELD NOTE № {nn} · {CATEGORY} · {PLACE/REGION}".
3. The accent — one accent per asset, used sparingly (mark, the · dots, category bar, links). Chosen by category.
Fixed layout DNA: mark top-left, eyebrow beside/under it, oversized serif title, photo fills the rest, thin category bar.

================ FOUNDATIONS (specify all, exactly) ================

COLOR — full system, light + dark, with hex + role + WCAG contrast pairing:
  Paper #faf9f6 / paper-alt #f2f0e9 ; Ink #181715 / ink-soft #4a4843 / ink-mute #8a877f ; Rule #d9d6cb ; Accent (master, Restaurant) #a8431a, accent-soft #c96b3e ; Dark theme: bg #14130f, bg-alt #1c1b16, ink #ece8dc, ink-soft #b8b3a2, ink-mute #807c70, rule #2c2a23, accent #d97757, accent-soft #e89878.
  Category accents (swap ONLY this, keep everything else): Restaurant #a8431a(dark #d97757) · Hike #3f6b3a(#5d8a52) · Spa/Stay #2f6b6b(#4f9a9a) · Event #6b3a5d(#9a5d86) · City/Walk #3a5a6b(#5d86a0).
  Deliver: swatch sheet, each with hex/RGB/HSL, light+dark, AA/AAA contrast on paper and on ink, and the rule for adding a new category hue.

TYPE — full scale, no new families: Instrument Serif (display titles), Inter Tight 400/500/600 (body/UI), JetBrains Mono 400/500 (eyebrows/labels/data). Deliver a type-scale table (display XL→body→caption→eyebrow) with px/rem, line-height, weight, letter-spacing, and responsive (desktop/tablet/mobile) values. Show a styled specimen page.

SPACING & GRID — an 8pt spacing scale, container widths, a 12-col web grid, and the print/social safe-zones (center 80% for 9:16). Define radii, hairline weights, shadow tokens.

THE MARK — deliver: primary mark, mark-in-circle, mark + "Ibraverse" wordmark (horizontal), stacked lockup, favicon/app-icon (16/32/180/512), monochrome ink, monochrome paper (knockout), and each in accent. Specify clear-space (= ring radius), minimum sizes, and a misuse sheet (don't stretch / recolor outside palette / add effects / rotate).

ICONOGRAPHY & MOTIF — a small set of line icons (trail, fork, sauna/steam, ticket, pin) in the mark's stroke style (1.5px, round caps) for category tagging. Optional: a subtle paper-grain / hairline-grid texture token reused from the protocol.

PHOTOGRAPHY DIRECTION — one page: how photos should look (natural light, golden hour, honest not stock), crop ratios, how they sit inside templates (rounded 14px frame), and treatment (none / subtle warm). Use clearly-labeled <PHOTO> placeholders in all renders.

MOTION — micro-interaction specs for web: link/hover, the reel card play-button, page-load reveal. Durations/easings as tokens.

VOICE & TONE — one page: persona, do/don't lines, the eyebrow grammar, caption style, the 5-beat reel structure, and example headlines per category.

================ COMPONENTS (build all, with exact pixel specs) ================
For EACH: full layout, real code, light + dark, and the safe-zone overlay.
1. Article cover / hero — 1600×900 and 1600×2000. Full-bleed photo + paper band (mark, eyebrow, oversized serif title, category bar).
2. Social cover / reel thumbnail — 1080×1920 (9:16). Paper bg, rounded photo frame, mark top-left, eyebrow, 3–5-word serif title, category bar bottom, center-80% safe text.
3. Instagram post — 1080×1350 (4:5) and 1080×1080 (1:1).
4. Instagram/TikTok Story — 1080×1920 with UI-safe overlay.
5. Reel end-card — 1080×1920: paper, centered mark, ibraverse.ca, @ibraverse, category bar, CTA.
6. Open Graph / share card — 1200×630.
7. Carousel template — 3 slides (hook / proof / verdict+CTA), 1080×1350.
8. On-site reels row — the existing `reels` shortcode look: 1 row, YouTube+IG+TikTok vertical click-to-load thumbnails at the article bottom under "## Watch". Show its on-brand styling.
9. Web UI kit — article header, eyebrow, category badge, recommendations list, verdict block, buttons, links, tags, footer — as HTML/CSS using the tokens, matching PaperMod + the protocol chrome.
10. Avatar / channel banners — profile avatar (mark) + YouTube banner 2560×1440 (title-safe) + channel art for IG/TikTok.

================ WEB / CODE DELIVERABLES ================
- design-tokens.json (W3C design-tokens format) and a tokens.css (:root + [data-theme="dark"]) using the EXACT variable names already in protocol.css (--bg, --ink, --accent, …) so it drops into the repo.
- A Hugo-ready partial or CSS for the Adventures articles that applies Instrument Serif titles + the eyebrow + category accent, consistent with layouts/_default/single.html and assets/css/extended/.
- An updated, on-brand version of the `reels` shortcode styling (one row).
- A Figma-importable structure note (frames named per component).

================ OUTPUT: FILE & FOLDER STRUCTURE ================
Return a real, downloadable package laid out exactly like this (create every file with real content/code, not placeholders):

ibraverse-brand/
  00-README.md                  ← how to use the kit, index of everything
  01-foundations/
    brand-guidelines.md         ← polished, final
    color.md  +  swatches.svg
    type.md   +  specimen.html
    spacing-grid.md
    voice-tone.md
    photography.md
    motion.md
  02-logo/
    mark.svg  mark-circle.svg  wordmark-horizontal.svg  lockup-stacked.svg
    favicon-16.svg favicon-32.svg app-icon-180.svg app-icon-512.svg
    mark-mono-ink.svg  mark-mono-paper.svg
    clearspace-minsize.svg  misuse.svg
  03-color/
    tokens.css  design-tokens.json  category-accents.svg
  04-components/
    cover-1600x900.svg  cover-1600x2000.svg
    social-9x16.svg  ig-4x5.svg  ig-1x1.svg  story-9x16.svg
    reel-endcard.svg  og-1200x630.svg  carousel-{1,2,3}.svg
    web-ui-kit.html
  05-channels/
    avatar.svg  youtube-banner-2560x1440.svg
  06-web/
    tokens.css  adventures-brand.css  reels.css  hugo-partial.html
  07-proofs/
    contact-sheet.html          ← every component, all 5 categories, light+dark, on one page
    proof-hike.svg proof-restaurant.svg proof-spa.svg proof-event.svg proof-city.svg

================ PROOFS (prove reproducibility) ================
Render the cover + social thumbnail + end-card FIVE times — once per category (hike, restaurant, spa, event, city) — so the ONLY difference is the accent + eyebrow + photo. Show light AND dark. Assemble all of it into 07-proofs/contact-sheet.html as one scrollable board.

================ CONSTRAINTS / QUALITY BAR (visually perfect) ================
- Vector only (SVG/HTML/CSS). Leave clearly-labeled <PHOTO> slots — do not fake photos.
- No font or color outside the tokens. One accent per asset.
- Pixel-perfect: state exact px for every size, margin, and safe-zone; align to the 8pt grid; optically center the mark; balance the serif title.
- Accessibility: body text ≥ WCAG AA on its background; note any pairing that fails and fix it.
- Export specs for each asset (dimensions, format, color space).
- Everything internally consistent: the same mark, spacing, and type rules across every file.

PROCESS
First restate the extracted tokens (color + type + mark) so I can confirm you read the repo correctly. Then build foundations, then components, then proofs. Output each file with its path as a heading and full copy-paste code beneath. End with 00-README.md indexing the whole package.

If you must stop, stop at a file boundary and tell me the next file.
```

---

## Run it in 6 phases if it truncates

1. **Extract + foundations** — tokens, color, type, spacing, voice, photography, motion (`01-foundations/`, `03-color/`).
2. **Logo system** — every lockup, favicon, clear-space, misuse (`02-logo/`).
3. **Core components** — cover, social 9:16, end-card, OG (`04-components/` part 1).
4. **Extended components** — IG post/story, carousel, web UI kit, channel art (`04-components/` part 2, `05-channels/`).
5. **Web/code** — tokens.css, design-tokens.json, adventures-brand.css, reels.css, hugo partial (`06-web/`).
6. **Proofs + README** — 5-category × light/dark contact sheet, `00-README.md`.

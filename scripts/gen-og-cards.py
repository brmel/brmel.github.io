#!/usr/bin/env python3
"""Regenerate the per-section social cards in static/og/.

Six sections, ONE template — scripts/og-cards.html — so the cards cannot drift
apart the way six hand-designed images would. Edit the card list in that file,
not the images.

There is no SVG/HTML rasteriser on this machine, so the template is rendered in
a real browser and screenshotted as one 1200x3780 strip, then cut into six
1200x630 cards here.

    python3 -m http.server 8899 --directory scripts/
    # drive a headless browser: open /og-cards.html at width 1200,
    # full-page screenshot -> og-strip.png
    python3 scripts/gen-og-cards.py og-strip.png

Requires Pillow. Adding a section means adding it to og-cards.html AND to
SECTIONS below, in the same order.
"""
import sys, os
from PIL import Image

SECTIONS = ["home", "resume", "projects", "tech", "adventures", "thoughts"]
W, H = 1200, 630

src = sys.argv[1] if len(sys.argv) > 1 else "og-strip.png"
strip = Image.open(src).convert("RGB")
if strip.size != (W, H * len(SECTIONS)):
    sys.exit(f"expected {W}x{H*len(SECTIONS)}, got {strip.size} — "
             f"does og-cards.html still have exactly {len(SECTIONS)} cards?")

os.makedirs("static/og", exist_ok=True)
for i, name in enumerate(SECTIONS):
    card = strip.crop((0, i * H, W, (i + 1) * H))
    out = f"static/og/{name}.jpg"
    card.save(out, "JPEG", quality=86, optimize=True, progressive=True)
    print(f"  {out}  {os.path.getsize(out)//1024} KB")

#!/usr/bin/env python3
"""Regenerate the favicon set from the Ibraverse compass mark.

The mark has one source of truth — layouts/partials/brand-mark.html — and the
tab icon must be the same shape. This script rasterises it and writes every
file declared under [params.assets] in config.toml.

There is no SVG rasteriser on this machine, so the mark is rendered in a real
browser and screenshotted. Run:

    python3 -m http.server 8899 --directory scripts/           # serve favicon-src.html
    # drive a headless browser to screenshot it at 512x512 -> mark-512.png
    python3 scripts/gen-favicons.py mark-512.png

Requires Pillow. safari-pinned-tab.svg is hand-maintained (monochrome mask,
different stroke weights) and is NOT written by this script.
"""
import sys
from PIL import Image

SRC = sys.argv[1] if len(sys.argv) > 1 else "mark-512.png"
src = Image.open(SRC).convert("RGBA")
if src.size != (512, 512):
    sys.exit(f"expected a 512x512 source, got {src.size}")

# Opaque paper background: iOS composites a transparent apple-touch-icon onto
# black, which would invert the mark.
src.resize((180, 180), Image.LANCZOS).convert("RGB").save("static/apple-touch-icon.png")

for n in (16, 32, 192, 512):
    src.resize((n, n), Image.LANCZOS).save(f"static/favicon-{n}x{n}.png")

src.resize((256, 256), Image.LANCZOS).save(
    "static/favicon.ico",
    sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
)
print("wrote static/favicon.ico, favicon-{16,32,192,512}, apple-touch-icon.png")

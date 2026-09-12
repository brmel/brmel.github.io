#!/usr/bin/env python3
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

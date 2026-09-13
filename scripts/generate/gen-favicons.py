#!/usr/bin/env python3
import sys
from PIL import Image

SRC = sys.argv[1] if len(sys.argv) > 1 else "mark-512.png"
src = Image.open(SRC).convert("RGBA")
if src.size != (512, 512):
    sys.exit(f"expected a 512x512 source, got {src.size}")

src.resize((180, 180), Image.LANCZOS).convert("RGB").save("static/apple-touch-icon.png")

for n in (16, 32, 192, 512):
    src.resize((n, n), Image.LANCZOS).save(f"static/favicon-{n}x{n}.png")

src.resize((256, 256), Image.LANCZOS).save(
    "static/favicon.ico",
    sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
)
print("wrote static/favicon.ico, favicon-{16,32,192,512}, apple-touch-icon.png")

#!/usr/bin/env python3
"""Generate compressed .webp versions next to the heavy source images.

Originals are never modified or deleted; templates reference the .webp
copies. Re-run after adding or replacing any image below (idempotent:
skips webp files newer than their source). Requires Pillow with webp.
"""
import glob
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUALITY = 80

SOURCES = (
    "assets/img/redesign/*.png",
    "assets/img/blog/*.png",
    "assets/img/blog/blog-1/*.png",
)

def main():
    total_in = total_out = 0
    for pattern in SOURCES:
        for src in sorted(glob.glob(os.path.join(ROOT, pattern))):
            dst = os.path.splitext(src)[0] + ".webp"
            if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
                continue
            Image.open(src).save(dst, "WEBP", quality=QUALITY, method=6)
            kin, kout = os.path.getsize(src) // 1024, os.path.getsize(dst) // 1024
            total_in += kin
            total_out += kout
            print(f"{os.path.relpath(src, ROOT)}  {kin}KB -> {kout}KB")

    # Smaller PNG copy of the structured-data logo (stays PNG for crawlers).
    logo = os.path.join(ROOT, "assets/img/brand/abitaresmart-logo-icon.png")
    logo_out = os.path.join(ROOT, "assets/img/brand/abitaresmart-logo-icon-512.png")
    if not os.path.exists(logo_out):
        im = Image.open(logo).resize((512, 512), Image.LANCZOS)
        im.save(logo_out, "PNG", optimize=True)
        print(f"logo 512px copy: {os.path.getsize(logo_out) // 1024}KB")

    if total_in:
        print(f"total: {total_in / 1024:.1f}MB -> {total_out / 1024:.1f}MB")

if __name__ == "__main__":
    main()

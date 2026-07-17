#!/usr/bin/env python3
"""Export AbitareSmart browser and PWA icons from the premium 1024 px master."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[2]
MASTER = ROOT / "assets" / "img" / "brand" / "abitaresmart-premium-icon.png"
FAVICONS = ROOT / "assets" / "img" / "favicons"

PNG_EXPORTS = {
    "favicon-96x96.png": 96,
    "apple-touch-icon.png": 180,
    "web-app-manifest-192x192.png": 192,
    "web-app-manifest-512x512.png": 512,
}


def resized(master: Image.Image, size: int) -> Image.Image:
    return master.resize((size, size), Image.Resampling.LANCZOS)


def main() -> None:
    master = Image.open(MASTER).convert("RGB")
    if master.size != (1024, 1024):
        raise ValueError(f"Expected a 1024x1024 icon master, got {master.size}")

    FAVICONS.mkdir(parents=True, exist_ok=True)
    for filename, size in PNG_EXPORTS.items():
        output = FAVICONS / filename
        resized(master, size).save(output, "PNG", optimize=True)
        print(f"  {output.relative_to(ROOT)}  {size}x{size}")

    ico = FAVICONS / "favicon.ico"
    master.save(ico, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"  {ico.relative_to(ROOT)}  16/32/48")


if __name__ == "__main__":
    main()

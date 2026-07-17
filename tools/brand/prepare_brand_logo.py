#!/usr/bin/env python3
"""Build the AbitareSmart navbar logo icon and browser/PWA exports."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageOps


ROOT = Path(__file__).resolve().parents[2]
ARTWORK = ROOT / "assets" / "img" / "brand" / "abitaresmart-logo-artwork.png"
MASTER = ROOT / "assets" / "img" / "brand" / "abitaresmart-logo-icon.png"
NAVBAR = ROOT / "assets" / "img" / "brand" / "abitaresmart-logo-icon-96.png"
FAVICONS = ROOT / "assets" / "img" / "favicons"

MASTER_SIZE = 1024
MASK_INSET = 16
MASK_RADIUS = 224
CANVAS = (247, 244, 236)

PNG_EXPORTS = {
    "favicon-96x96.png": (96, False),
    "apple-touch-icon.png": (180, True),
    "web-app-manifest-192x192.png": (192, True),
    "web-app-manifest-512x512.png": (512, True),
}


def rounded_mask() -> Image.Image:
    scale = 4
    size = MASTER_SIZE * scale
    inset = MASK_INSET * scale
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        (inset, inset, size - inset, size - inset),
        radius=MASK_RADIUS * scale,
        fill=255,
    )
    return mask.resize((MASTER_SIZE, MASTER_SIZE), Image.Resampling.LANCZOS)


def build_master(artwork: Image.Image) -> Image.Image:
    fitted = ImageOps.fit(
        artwork.convert("RGB"),
        (MASTER_SIZE, MASTER_SIZE),
        method=Image.Resampling.LANCZOS,
    ).convert("RGBA")
    master = Image.new("RGBA", fitted.size, (0, 0, 0, 0))
    master.paste(fitted, (0, 0), rounded_mask())
    return master


def resized(master: Image.Image, size: int, opaque: bool) -> Image.Image:
    icon = master.resize((size, size), Image.Resampling.LANCZOS)
    if not opaque:
        return icon

    background = Image.new("RGBA", icon.size, (*CANVAS, 255))
    return Image.alpha_composite(background, icon).convert("RGB")


def main() -> None:
    artwork = Image.open(ARTWORK)
    if artwork.width != artwork.height or artwork.width < MASTER_SIZE:
        raise ValueError(
            f"Expected square source artwork at least {MASTER_SIZE}px, got {artwork.size}"
        )

    master = build_master(artwork)
    master.save(MASTER, "PNG", optimize=True)
    resized(master, 96, False).save(NAVBAR, "PNG", optimize=True)
    print(f"  {MASTER.relative_to(ROOT)}  {MASTER_SIZE}x{MASTER_SIZE} rounded RGBA")
    print(f"  {NAVBAR.relative_to(ROOT)}  96x96 navbar")

    FAVICONS.mkdir(parents=True, exist_ok=True)
    for filename, (size, opaque) in PNG_EXPORTS.items():
        output = FAVICONS / filename
        resized(master, size, opaque).save(output, "PNG", optimize=True)
        print(f"  {output.relative_to(ROOT)}  {size}x{size}")

    ico = FAVICONS / "favicon.ico"
    master.save(ico, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"  {ico.relative_to(ROOT)}  16/32/48")


if __name__ == "__main__":
    main()

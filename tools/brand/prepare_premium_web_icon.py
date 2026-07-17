#!/usr/bin/env python3
"""Build the rounded AbitareSmart icon and export its browser/PWA sizes."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageOps


ROOT = Path(__file__).resolve().parents[2]
ARTWORK = ROOT / "assets" / "img" / "brand" / "abitaresmart-smart-home-artwork.png"
MASTER = ROOT / "assets" / "img" / "brand" / "abitaresmart-premium-icon.png"
FAVICONS = ROOT / "assets" / "img" / "favicons"

MASTER_SIZE = 1024
CARD_INSET = 28
CARD_RADIUS = 212
CANVAS = (247, 244, 236)

PNG_EXPORTS = {
    "favicon-96x96.png": (96, False),
    "apple-touch-icon.png": (180, True),
    "web-app-manifest-192x192.png": (192, True),
    "web-app-manifest-512x512.png": (512, True),
}


def rounded_mask(size: int, inset: int, radius: int) -> Image.Image:
    scale = 4
    mask = Image.new("L", (size * scale, size * scale), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle(
        (
            inset * scale,
            inset * scale,
            (size - inset) * scale,
            (size - inset) * scale,
        ),
        radius=radius * scale,
        fill=255,
    )
    return mask.resize((size, size), Image.Resampling.LANCZOS)


def build_master(artwork: Image.Image) -> Image.Image:
    inner_size = MASTER_SIZE - (CARD_INSET * 2)
    card = ImageOps.fit(
        artwork.convert("RGB"),
        (inner_size, inner_size),
        method=Image.Resampling.LANCZOS,
    ).convert("RGBA")

    mask = rounded_mask(MASTER_SIZE, CARD_INSET, CARD_RADIUS)
    master = Image.new("RGBA", (MASTER_SIZE, MASTER_SIZE), (0, 0, 0, 0))

    shadow_alpha = mask.filter(ImageFilter.GaussianBlur(14))
    shadow = Image.new("RGBA", master.size, (11, 33, 31, 0))
    shadow.putalpha(shadow_alpha.point(lambda alpha: round(alpha * 0.28)))
    master.alpha_composite(shadow, dest=(0, 8))

    card_layer = Image.new("RGBA", master.size, (0, 0, 0, 0))
    card_layer.paste(card, (CARD_INSET, CARD_INSET))
    master.paste(card_layer, (0, 0), mask)
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
    print(f"  {MASTER.relative_to(ROOT)}  {MASTER_SIZE}x{MASTER_SIZE} rounded RGBA")

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

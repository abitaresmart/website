#!/usr/bin/env python3
"""Render the AbitareSmart Signal Portal master logo and QA sheet."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
ASSET_DIR = ROOT / "assets" / "img"
QA_PATH = Path("/tmp/abitaresmart-logo-qa.png")

COLORS = {
    "ink": "#0B211F",
    "tile": "#17302D",
    "paper": "#FFFDF8",
    "signal": "#DDF86A",
    "node": "#FF735C",
}

MASTER_SIZE = 2048
RENDER_SCALE = 4


def scaled(value: int) -> int:
    return value * RENDER_SCALE


def render_master() -> Image.Image:
    """Draw at 4x and downsample once for clean, vector-like edges."""
    canvas = Image.new(
        "RGB",
        (scaled(MASTER_SIZE), scaled(MASTER_SIZE)),
        COLORS["tile"],
    )
    draw = ImageDraw.Draw(canvas)

    # The portal is deliberately wider than it is tall: stable in a social
    # avatar, architectural in the website navigation, and clear at 24 px.
    outer_house = [
        (scaled(430), scaled(1575)),
        (scaled(430), scaled(930)),
        (scaled(1024), scaled(408)),
        (scaled(1618), scaled(930)),
        (scaled(1618), scaled(1575)),
    ]
    draw.polygon(outer_house, fill=COLORS["paper"])

    # One arched opening cuts the building into a continuous portal. Its
    # radius and wall width are matched optically, not mathematically.
    draw.ellipse(
        (scaled(692), scaled(742), scaled(1356), scaled(1406)),
        fill=COLORS["tile"],
    )
    draw.rectangle(
        (scaled(692), scaled(1074), scaled(1356), scaled(1576)),
        fill=COLORS["tile"],
    )

    # A single broad wireless wave avoids the generic three-arc Wi-Fi glyph.
    draw.ellipse(
        (scaled(758), scaled(844), scaled(1290), scaled(1376)),
        fill=COLORS["signal"],
    )
    draw.rectangle(
        (scaled(758), scaled(1110), scaled(1290), scaled(1376)),
        fill=COLORS["tile"],
    )
    draw.ellipse(
        (scaled(880), scaled(966), scaled(1168), scaled(1254)),
        fill=COLORS["tile"],
    )

    # The coral source is the system hub and the mark's visual punctuation.
    draw.ellipse(
        (scaled(916), scaled(1230), scaled(1132), scaled(1446)),
        fill=COLORS["node"],
    )

    return canvas.resize(
        (MASTER_SIZE, MASTER_SIZE),
        Image.Resampling.LANCZOS,
        reducing_gap=3.0,
    )


def export_assets(master: Image.Image) -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    exports = {
        "abitaresmart-social-avatar.png": 2048,
        "abitaresmart-portal-logo.png": 1024,
        "icon.png": 1024,
    }
    for filename, size in exports.items():
        image = master if size == MASTER_SIZE else master.resize(
            (size, size), Image.Resampling.LANCZOS
        )
        image.save(ASSET_DIR / filename, format="PNG", optimize=True)


def circle_crop(image: Image.Image, size: int) -> Image.Image:
    avatar = image.resize((size, size), Image.Resampling.LANCZOS).convert("RGBA")
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
    avatar.putalpha(mask)
    return avatar


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def render_qa_sheet(master: Image.Image) -> None:
    """Build a disposable sheet to inspect crop safety and small-size clarity."""
    sheet = Image.new("RGB", (1500, 940), COLORS["paper"])
    draw = ImageDraw.Draw(sheet)
    draw.text((72, 56), "ABITARESMART — SIGNAL PORTAL", fill=COLORS["ink"], font=font(40, True))
    draw.text(
        (72, 112),
        "Square master · circular crops · 48 px navigation · 24 px minimum",
        fill="#66736F",
        font=font(22),
    )

    large = master.resize((560, 560), Image.Resampling.LANCZOS)
    sheet.paste(large, (72, 210))

    labels = [
        (180, "SOCIAL / 180 PX", 230),
        (48, "NAV / 48 PX", 500),
        (24, "MIN / 24 PX", 700),
    ]
    for size, label, y in labels:
        draw.text((760, y), label, fill=COLORS["ink"], font=font(20, True))
        preview_size = max(size, 120)
        avatar = circle_crop(master, size)
        if size < preview_size:
            avatar = avatar.resize((preview_size, preview_size), Image.Resampling.NEAREST)
        sheet.paste(avatar, (760, y + 42), avatar)

    # Footer context: the Ink/Ink-soft distinction keeps the tile visible.
    draw.rounded_rectangle((1010, 250, 1418, 454), radius=28, fill=COLORS["ink"])
    footer_mark = master.resize((112, 112), Image.Resampling.LANCZOS)
    sheet.paste(footer_mark, (1048, 296))
    draw.text((1182, 320), "Abitare", fill=COLORS["paper"], font=font(25, True))
    draw.text((1282, 320), "Smart", fill=COLORS["node"], font=font(25, True))
    draw.text((1048, 426), "DARK FOOTER", fill="#AEECCF", font=font(16, True))

    sheet.save(QA_PATH, format="PNG", optimize=True)


def validate(master: Image.Image) -> None:
    assert master.size == (MASTER_SIZE, MASTER_SIZE)
    probes = {
        (16, 16): COLORS["tile"],
        (1024, 500): COLORS["paper"],
        (1024, 900): COLORS["signal"],
        (1024, 1338): COLORS["node"],
    }
    for point, expected in probes.items():
        assert master.getpixel(point) == tuple(bytes.fromhex(expected[1:])), (point, expected)


def main() -> None:
    master = render_master()
    validate(master)
    export_assets(master)
    render_qa_sheet(master)


if __name__ == "__main__":
    main()

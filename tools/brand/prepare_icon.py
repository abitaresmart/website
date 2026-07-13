#!/usr/bin/env python3
"""Prepare website, favicon, and social exports from the 3D icon master."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[2]
ASSET_DIR = ROOT / "assets" / "img"
MASTER_PATH = ASSET_DIR / "brand" / "abitaresmart-dimensional-master.png"
QA_PATH = Path("/tmp/abitaresmart-dimensional-icon-qa.png")

INK = "#0B211F"
INK_SOFT = "#17302D"
CANVAS = "#F7F4EC"
SURFACE = "#EFEADF"
WHITE = "#FFFDF8"
LIME = "#DDF86A"
CORAL = "#FF735C"


def crop_master() -> Image.Image:
    master = Image.open(MASTER_PATH).convert("RGBA")
    alpha_box = master.getchannel("A").getbbox()
    if alpha_box is None:
        raise ValueError("The dimensional master contains no opaque pixels")
    left, top, right, bottom = alpha_box
    padding = 18
    box = (
        max(0, left - padding),
        max(0, top - padding),
        min(master.width, right + padding),
        min(master.height, bottom + padding),
    )
    return master.crop(box)


def contain(subject: Image.Image, size: int, coverage: float) -> Image.Image:
    target = int(size * coverage)
    scale = min(target / subject.width, target / subject.height)
    dimensions = (
        max(1, round(subject.width * scale)),
        max(1, round(subject.height * scale)),
    )
    return subject.resize(dimensions, Image.Resampling.LANCZOS)


def centered(canvas: Image.Image, subject: Image.Image, y_offset: int = 0) -> None:
    position = (
        (canvas.width - subject.width) // 2,
        (canvas.height - subject.height) // 2 + y_offset,
    )
    canvas.alpha_composite(subject, position)


def primary_icon(subject: Image.Image, size: int = 1400) -> Image.Image:
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    centered(canvas, contain(subject, size, 0.84), y_offset=10)
    return canvas


def paper_disc(size: int) -> Image.Image:
    # The subtle radial shift belongs to the social presentation, not the mark.
    gradient = Image.radial_gradient("L").resize((size, size), Image.Resampling.BICUBIC)
    disc = ImageOps.colorize(gradient, black=WHITE, white=SURFACE).convert("RGBA")
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((4, 4, size - 5, size - 5), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(max(1, size / 700)))
    disc.putalpha(mask)
    return disc


def social_avatar(subject: Image.Image, size: int = 2048) -> Image.Image:
    canvas = paper_disc(size)
    icon = contain(subject, size, 0.69)

    # A small ambient shadow keeps the freestanding object dimensional after a
    # social platform downsamples it. It remains inside the circular backdrop.
    shadow = Image.new("RGBA", icon.size, (0, 0, 0, 0))
    shadow.putalpha(icon.getchannel("A"))
    shadow_color = Image.new("RGBA", icon.size, (11, 33, 31, 72))
    shadow_color.putalpha(shadow.getchannel("A").filter(ImageFilter.GaussianBlur(size / 90)))
    centered(canvas, shadow_color, y_offset=round(size * 0.026))
    centered(canvas, icon, y_offset=round(size * 0.006))
    return canvas


def export_assets(subject: Image.Image) -> tuple[Image.Image, Image.Image]:
    primary = primary_icon(subject)
    social = social_avatar(subject)

    primary.save(ASSET_DIR / "abitaresmart-dimensional-icon.png", optimize=True)
    primary.resize((512, 512), Image.Resampling.LANCZOS).save(
        ASSET_DIR / "abitaresmart-dimensional-icon-web.png", optimize=True
    )
    social.save(ASSET_DIR / "abitaresmart-social-avatar.png", optimize=True)
    social.resize((512, 512), Image.Resampling.LANCZOS).save(
        ASSET_DIR / "icon.png", optimize=True
    )
    return primary, social


def get_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    filename = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    try:
        return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{filename}", size)
    except OSError:
        return ImageFont.load_default()


def qa_sheet(primary: Image.Image, social: Image.Image) -> None:
    sheet = Image.new("RGB", (1600, 1000), CANVAS)
    draw = ImageDraw.Draw(sheet)
    draw.text((68, 48), "ABITARESMART — DIMENSIONAL SIGNAL", fill=INK, font=get_font(38, True))
    draw.text(
        (68, 101),
        "Transparent mark · circular social crop · navigation · favicon",
        fill="#66736F",
        font=get_font(21),
    )

    large = primary.resize((560, 560), Image.Resampling.LANCZOS)
    sheet.paste(large, (50, 190), large)
    draw.text((70, 790), "PRIMARY / LIGHT SURFACE", fill=INK, font=get_font(18, True))

    social_preview = social.resize((300, 300), Image.Resampling.LANCZOS)
    sheet.paste(social_preview, (690, 200), social_preview)
    draw.text((690, 530), "SOCIAL AVATAR / CIRCLE SAFE", fill=INK, font=get_font(18, True))

    footer = Image.new("RGB", (500, 210), INK)
    footer_icon = social.resize((112, 112), Image.Resampling.LANCZOS)
    footer.paste(footer_icon, (34, 42), footer_icon)
    footer_draw = ImageDraw.Draw(footer)
    footer_draw.text((170, 65), "Abitare", fill=WHITE, font=get_font(26, True))
    footer_draw.text((273, 65), "Smart", fill=CORAL, font=get_font(26, True))
    footer_draw.text((170, 111), "DARK SURFACE", fill="#AEECCF", font=get_font(15, True))
    sheet.paste(footer, (1040, 200))

    for x, size, label in [(720, 48, "48 PX"), (930, 24, "24 PX")]:
        sample = primary.resize((size, size), Image.Resampling.LANCZOS)
        preview = sample.resize((144, 144), Image.Resampling.NEAREST)
        sheet.paste(preview, (x, 650), preview)
        draw.text((x, 815), label, fill=INK, font=get_font(17, True))

    sheet.save(QA_PATH, optimize=True)


def validate(primary: Image.Image, social: Image.Image) -> None:
    assert primary.size == (1400, 1400) and primary.mode == "RGBA"
    assert social.size == (2048, 2048) and social.mode == "RGBA"
    for image in (primary, social):
        alpha = image.getchannel("A")
        assert alpha.getextrema() == (0, 255)
        assert alpha.getpixel((0, 0)) == 0
        assert alpha.getbbox() is not None


def main() -> None:
    subject = crop_master()
    primary, social = export_assets(subject)
    validate(primary, social)
    qa_sheet(primary, social)


if __name__ == "__main__":
    main()

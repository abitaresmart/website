#!/usr/bin/env python3
"""Generate the AbitareSmart "warm core" mark and every web export from scratch.

Concept: a solid botanical-ink house opened by a warm arched doorway — an
Italian portale. A lime lunetta (fanlight window) glows at the top of the
arch; the coral hub floats in the doorway below it. Solid mass + luminous
portal — designed PNG-first with restrained material lighting, composited
at 2048 px and supersampled down.

Palette (Signal design system):
  - Ink #0B211F      solid architectural shell
  - White #FFFDF8    interior plate seen through the aperture
  - Lime #DDF86A     energy ring circulating around the hub
  - Coral #FF735C    the intelligent hub itself
  - Canvas #F7F4EC / Surface #EFEADF  circular presentation field

Outputs (all paths relative to repo root):
  assets/img/brand/abitaresmart-mark.svg      512 master geometry, transparent
  assets/img/abitaresmart-mark.png            1400x1400 transparent (structured data)
  assets/img/abitaresmart-mark-web.png        512x512 transparent (navigation)
  assets/img/abitaresmart-mark-disc.svg       circular presentation (SVG favicon)
  assets/img/abitaresmart-mark-disc.png       512x512 circular (favicon + footer)
  assets/img/abitaresmart-mark-avatar.png     2048x2048 circular (touch icon + social)
"""

import io
import math
from pathlib import Path

import cairosvg
from PIL import Image, ImageChops, ImageFilter

ROOT = Path(__file__).resolve().parents[2]
IMG = ROOT / "assets" / "img"

INK = "#0B211F"
WHITE = "#FFFDF8"
LIME = "#DDF86A"
CORAL = "#FF735C"
CANVAS = "#F7F4EC"
SURFACE = "#EFEADF"

SS = 2048          # supersampling canvas
K = SS / 512       # 512-grid -> supersample scale

# --- geometry (512 viewBox) -------------------------------------------------
# Solid house: filled pentagon whose corners are rounded by stroking the same
# path with a round-joined stroke (radius = CORNER / 2).
APEX = (256, 66)
EAVE_Y, BASE_Y = 218, 444
X_L, X_R = 96, 416
CORNER = 44

ARCH = (256, 276)    # doorway arch centre
R_ARCH = 80
DOOR_L, DOOR_R = 176, 336
DOOR_BOTTOM = 470    # past the shell edge; clipped to the silhouette
R_LUNETTA = 58       # lime fanlight (lunetta) filling the top of the arch
HUB = (256, 368)     # coral hub floating in the doorway
R_CORE = 32

HOUSE_D = (f"M {X_L} {BASE_Y} L {X_L} {EAVE_Y} L {APEX[0]} {APEX[1]} "
           f"L {X_R} {EAVE_Y} L {X_R} {BASE_Y} Z")
DOOR_D = (f"M {DOOR_L} {DOOR_BOTTOM} L {DOOR_L} {ARCH[1]} "
          f"A {R_ARCH} {R_ARCH} 0 0 1 {DOOR_R} {ARCH[1]} L {DOOR_R} {DOOR_BOTTOM} Z")

# Optical bounds: x 74-438, y 44-466 -> centre (256, 255).
OPT_CY = 255


def lunetta_path() -> str:
    x1, x2 = ARCH[0] - R_LUNETTA, ARCH[0] + R_LUNETTA
    return f"M {x1} {ARCH[1]} A {R_LUNETTA} {R_LUNETTA} 0 0 1 {x2} {ARCH[1]} Z"


def house_shape(paint: str) -> str:
    return (f'<path d="{HOUSE_D}" fill="{paint}" stroke="{paint}" '
            f'stroke-width="{CORNER}" stroke-linejoin="round"/>')


# --- flat vector masters ----------------------------------------------------

def flat_group() -> str:
    return f"""  <defs>
    <clipPath id="shell"><path d="{HOUSE_D}"/></clipPath>
  </defs>
  {house_shape(INK)}
  <path d="{DOOR_D}" fill="{WHITE}" clip-path="url(#shell)"/>
  <path d="{lunetta_path()}" fill="{LIME}"/>
  <circle cx="{HUB[0]}" cy="{HUB[1]}" r="{R_CORE}" fill="{CORAL}"/>"""


def wrap(body: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">\n'
            f'{body}\n</svg>\n')


def disc_svg() -> str:
    scale = 0.72
    tx = 256 - scale * 256
    ty = 256 - scale * OPT_CY
    return wrap(f"""  <defs>
    <linearGradient id="field" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{CANVAS}"/>
      <stop offset="1" stop-color="{SURFACE}"/>
    </linearGradient>
  </defs>
  <circle cx="256" cy="256" r="256" fill="url(#field)"/>
  <g transform="translate({tx:.2f} {ty:.2f}) scale({scale})">
{flat_group()}
  </g>""")


# --- material PNG pipeline ---------------------------------------------------

def render(body: str, size: int = SS) -> Image.Image:
    png = cairosvg.svg2png(bytestring=wrap(body).encode(),
                           output_width=size, output_height=size)
    return Image.open(io.BytesIO(png)).convert("RGBA")


def cast_shadow(layer: Image.Image, blur: float, dy: int,
                opacity: float, color=(5, 14, 13)) -> Image.Image:
    alpha = layer.split()[3]
    moved = Image.new("L", layer.size, 0)
    moved.paste(alpha, (0, dy))
    moved = moved.filter(ImageFilter.GaussianBlur(blur))
    moved = moved.point(lambda p: int(p * opacity))
    shadow = Image.new("RGBA", layer.size, color + (255,))
    shadow.putalpha(moved)
    return shadow


def shell_mask() -> Image.Image:
    return render(house_shape("#fff")).split()[3]


def body_layer() -> Image.Image:
    """Satin ink shell with a quiet top-light and occlusion around the arch."""
    svg = f"""  <defs>
    <linearGradient id="satin" gradientUnits="userSpaceOnUse" x1="0" y1="44" x2="0" y2="466">
      <stop offset="0" stop-color="#1B3A34"/>
      <stop offset="0.5" stop-color="#0C2320"/>
      <stop offset="1" stop-color="#071815"/>
    </linearGradient>
  </defs>
  {house_shape("url(#satin)")}
  <path d="M {DOOR_L} 466 L {DOOR_L} {ARCH[1]} A {R_ARCH} {R_ARCH} 0 0 1 {DOOR_R} {ARCH[1]} L {DOOR_R} 466"
        fill="none" stroke="#04100E" stroke-width="10" stroke-opacity="0.4"/>"""
    img = render(svg)
    mask = shell_mask()
    img.putalpha(ImageChops.multiply(img.split()[3], mask))
    # top-light: a smooth vertical sheen built in PIL so the rounding stroke
    # cannot double-paint it into a band along the roofline
    y0, y1, peak = int(44 * K), int(210 * K), 0.11
    ramp = Image.new("L", (1, SS), 0)
    ramp.putdata([int(255 * peak * max(0.0, 1 - (y - y0) / (y1 - y0)))
                  if y >= y0 else int(255 * peak) for y in range(SS)])
    sheen_a = ImageChops.multiply(ramp.resize((SS, SS)), mask)
    sheen = Image.new("RGBA", img.size, (255, 253, 248, 255))
    sheen.putalpha(sheen_a)
    img.alpha_composite(sheen)
    return img


def plate_layer() -> Image.Image:
    """Warm-white doorway, recessed: rim shadow under the arch."""
    plate = render(f'<path d="{DOOR_D}" fill="{WHITE}"/>')
    plate.putalpha(ImageChops.multiply(plate.split()[3], shell_mask()))
    mask = plate.split()[3]
    shift = int(9 * K)
    moved = Image.new("L", plate.size, 0)
    moved.paste(mask, (0, shift))
    crescent = ImageChops.subtract(mask, moved)
    crescent = crescent.filter(ImageFilter.GaussianBlur(10 * K))
    crescent = ImageChops.multiply(crescent, mask)
    crescent = crescent.point(lambda p: int(p * 0.30))
    inner = Image.new("RGBA", plate.size, (35, 48, 44, 255))
    inner.putalpha(crescent)
    plate.alpha_composite(inner)
    return plate


def ring_layer() -> Image.Image:
    top = ARCH[1] - R_LUNETTA
    return render(f"""  <defs>
    <linearGradient id="limeg" gradientUnits="userSpaceOnUse"
        x1="0" y1="{top}" x2="0" y2="{ARCH[1]}">
      <stop offset="0" stop-color="#EDFF9E"/>
      <stop offset="1" stop-color="#D5F158"/>
    </linearGradient>
  </defs>
  <path d="{lunetta_path()}" fill="url(#limeg)"/>""")


def core_layer() -> Image.Image:
    return render(f"""  <defs>
    <radialGradient id="enamel" cx="0.40" cy="0.34" r="0.92">
      <stop offset="0" stop-color="#FF8F76"/>
      <stop offset="0.55" stop-color="#FF735C"/>
      <stop offset="1" stop-color="#E9563E"/>
    </radialGradient>
    <radialGradient id="spec" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#FFFDF8" stop-opacity="0.42"/>
      <stop offset="1" stop-color="#FFFDF8" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="{HUB[0]}" cy="{HUB[1]}" r="{R_CORE}" fill="url(#enamel)"/>
  <ellipse cx="{HUB[0] - 10}" cy="{HUB[1] - 11}" rx="8" ry="6.5" fill="url(#spec)"/>""")


def material_mark() -> Image.Image:
    body = body_layer()
    plate = plate_layer()
    ring = ring_layer()
    core = core_layer()

    out = Image.new("RGBA", (SS, SS), (0, 0, 0, 0))
    out.alpha_composite(body)
    out.alpha_composite(plate)
    out.alpha_composite(cast_shadow(ring, blur=5 * K, dy=int(4 * K), opacity=0.16))
    out.alpha_composite(cast_shadow(core, blur=4 * K, dy=int(4 * K), opacity=0.20))
    out.alpha_composite(ring)
    out.alpha_composite(core)
    return out


def material_disc(mark: Image.Image) -> Image.Image:
    disc = render(f"""  <defs>
    <linearGradient id="field" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{CANVAS}"/>
      <stop offset="1" stop-color="{SURFACE}"/>
    </linearGradient>
  </defs>
  <circle cx="256" cy="256" r="256" fill="url(#field)"/>""")

    scale = 0.72
    small = mark.resize((int(SS * scale),) * 2, Image.LANCZOS)
    ox = round(SS / 2 - scale * SS * (256 / 512))
    oy = round(SS / 2 - scale * SS * (OPT_CY / 512))
    placed = Image.new("RGBA", (SS, SS), (0, 0, 0, 0))
    placed.alpha_composite(small, (ox, oy))

    disc.alpha_composite(cast_shadow(placed, blur=44, dy=34, opacity=0.16))
    disc.alpha_composite(placed)
    mask = render('  <circle cx="256" cy="256" r="256" fill="#fff"/>').split()[3]
    disc.putalpha(mask)
    return disc


def save(img: Image.Image, out: Path, size: int) -> None:
    img.resize((size, size), Image.LANCZOS).save(out)
    print(f"  {out.relative_to(ROOT)}  {size}x{size}")


def main() -> None:
    (IMG / "brand" / "abitaresmart-mark.svg").write_text(wrap(flat_group()))
    (IMG / "abitaresmart-mark-disc.svg").write_text(disc_svg())
    print("  assets/img/brand/abitaresmart-mark.svg")
    print("  assets/img/abitaresmart-mark-disc.svg")

    mark = material_mark()
    disc = material_disc(mark)
    save(mark, IMG / "abitaresmart-mark.png", 1400)
    save(mark, IMG / "abitaresmart-mark-web.png", 512)
    save(disc, IMG / "abitaresmart-mark-disc.png", 512)
    save(disc, IMG / "abitaresmart-mark-avatar.png", 2048)


if __name__ == "__main__":
    main()

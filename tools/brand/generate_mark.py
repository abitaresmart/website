#!/usr/bin/env python3
"""Generate the AbitareSmart Signal mark and every web export from scratch.

The geometry is pure vector, built on the Signal palette:
  - Ink #0B211F      architectural portal (open house silhouette)
  - Lime #DDF86A     precision signal channel (single arc, not generic Wi-Fi)
  - Coral #FF735C    source node (the intelligent hub)
  - Canvas #F7F4EC / Surface #EFEADF  circular presentation field

The PNG exports add restrained material lighting: a satin vertical gradient
on the ink portal, a top-light sheen, an enamel node with a specular
highlight, and soft contact shadows. Everything is composited at 2048 px
and supersampled down, so edges stay clean at every size.

Outputs (all paths relative to repo root):
  assets/img/brand/abitaresmart-mark.svg      512 master geometry, transparent
  assets/img/abitaresmart-mark.png            1400x1400 transparent (structured data)
  assets/img/abitaresmart-mark-web.png        512x512 transparent (navigation)
  assets/img/abitaresmart-mark-disc.svg       circular presentation (SVG favicon)
  assets/img/abitaresmart-mark-disc.png       512x512 circular (favicon + footer)
  assets/img/abitaresmart-mark-avatar.png     2048x2048 circular (touch icon + social)
"""

import math
from pathlib import Path

import cairosvg
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[2]
IMG = ROOT / "assets" / "img"

INK = "#0B211F"
LIME = "#DDF86A"
CORAL = "#FF735C"
CANVAS = "#F7F4EC"
SURFACE = "#EFEADF"

SS = 2048  # supersampling canvas

# --- geometry (512 viewBox) -------------------------------------------------
# Open-portal pentagon: two walls and a gabled roof drawn as one continuous
# round-capped stroke. The open base keeps the doorway/portal brand story.
WALL_L, WALL_R = 84, 428
BASE_Y, EAVE_Y, APEX_Y = 442, 232, 84
STROKE = 58

# Signal: one wide arc hugging the node, centred on the hub.
NODE = (256, 348)
NODE_R = 38
ARC_R = 98
ARC_W = 36
ARC_DEG = 20  # arc runs from 180-ARC_DEG to ARC_DEG degrees, over the top

HOUSE_D = f"M {WALL_L} {BASE_Y} V {EAVE_Y} L 256 {APEX_Y} L {WALL_R} {EAVE_Y} V {BASE_Y}"


def arc_path() -> str:
    a = math.radians(ARC_DEG)
    dx, dy = ARC_R * math.cos(a), ARC_R * math.sin(a)
    x1, x2 = NODE[0] - dx, NODE[0] + dx
    y = NODE[1] - dy
    return f"M {x1:.2f} {y:.2f} A {ARC_R} {ARC_R} 0 0 1 {x2:.2f} {y:.2f}"


# --- flat vector masters ----------------------------------------------------

def flat_group(house=INK, lime=LIME, coral=CORAL) -> str:
    return f"""  <path d="{HOUSE_D}"
        fill="none" stroke="{house}" stroke-width="{STROKE}"
        stroke-linecap="round" stroke-linejoin="round"/>
  <path d="{arc_path()}" fill="none" stroke="{lime}"
        stroke-width="{ARC_W}" stroke-linecap="round"/>
  <circle cx="{NODE[0]}" cy="{NODE[1]}" r="{NODE_R}" fill="{coral}"/>"""


def wrap(body: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">\n'
            f'{body}\n</svg>\n')


def mark_svg() -> str:
    return wrap(flat_group())


def disc_svg() -> str:
    # Optical bounds of the mark: x 55-457, y 55-471 -> centre (256, 263).
    scale = 0.72
    tx = 256 - scale * 256
    ty = 256 - scale * 263
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
    import io
    return Image.open(io.BytesIO(png)).convert("RGBA")


def cast_shadow(layer: Image.Image, blur: float, dy: int,
                opacity: float, color=(6, 16, 15)) -> Image.Image:
    """Soft shadow built from a layer's silhouette."""
    alpha = layer.split()[3]
    moved = Image.new("L", layer.size, 0)
    moved.paste(alpha, (0, dy))
    moved = moved.filter(ImageFilter.GaussianBlur(blur))
    moved = moved.point(lambda p: int(p * opacity))
    shadow = Image.new("RGBA", layer.size, color + (255,))
    shadow.putalpha(moved)
    return shadow


def house_layers() -> str:
    """Satin ink portal: vertical tonal gradient plus a top-light sheen."""
    return f"""  <defs>
    <linearGradient id="satin" gradientUnits="userSpaceOnUse"
        x1="0" y1="{APEX_Y - 30}" x2="0" y2="{BASE_Y + 30}">
      <stop offset="0" stop-color="#173430"/>
      <stop offset="0.55" stop-color="#0B211F"/>
      <stop offset="1" stop-color="#091C1A"/>
    </linearGradient>
    <linearGradient id="sheen" gradientUnits="userSpaceOnUse"
        x1="0" y1="{APEX_Y - 30}" x2="0" y2="{EAVE_Y}">
      <stop offset="0" stop-color="#FFFDF8" stop-opacity="0.10"/>
      <stop offset="1" stop-color="#FFFDF8" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <path d="{HOUSE_D}" fill="none" stroke="url(#satin)" stroke-width="{STROKE}"
        stroke-linecap="round" stroke-linejoin="round"/>
  <path d="{HOUSE_D}" fill="none" stroke="url(#sheen)" stroke-width="{STROKE}"
        stroke-linecap="round" stroke-linejoin="round"/>"""


def arc_layer() -> str:
    top = NODE[1] - ARC_R - ARC_W / 2
    return f"""  <defs>
    <linearGradient id="limeg" gradientUnits="userSpaceOnUse"
        x1="0" y1="{top}" x2="0" y2="{NODE[1]}">
      <stop offset="0" stop-color="#E9FD90"/>
      <stop offset="1" stop-color="#D6F25E"/>
    </linearGradient>
  </defs>
  <path d="{arc_path()}" fill="none" stroke="url(#limeg)"
        stroke-width="{ARC_W}" stroke-linecap="round"/>"""


def node_layer() -> str:
    """Enamel hub: warm radial body with a small specular highlight."""
    return f"""  <defs>
    <radialGradient id="enamel" cx="0.40" cy="0.34" r="0.92">
      <stop offset="0" stop-color="#FF8B72"/>
      <stop offset="0.55" stop-color="#FF735C"/>
      <stop offset="1" stop-color="#EF5D45"/>
    </radialGradient>
    <radialGradient id="spec" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#FFFDF8" stop-opacity="0.45"/>
      <stop offset="1" stop-color="#FFFDF8" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="{NODE[0]}" cy="{NODE[1]}" r="{NODE_R}" fill="url(#enamel)"/>
  <ellipse cx="{NODE[0] - 12}" cy="{NODE[1] - 14}" rx="10" ry="8" fill="url(#spec)"/>"""


def material_mark() -> Image.Image:
    house = render(house_layers())
    arc = render(arc_layer())
    node = render(node_layer())

    out = Image.new("RGBA", (SS, SS), (0, 0, 0, 0))
    out.alpha_composite(house)
    out.alpha_composite(cast_shadow(arc, blur=26, dy=28, opacity=0.15))
    out.alpha_composite(cast_shadow(node, blur=16, dy=18, opacity=0.20))
    out.alpha_composite(arc)
    out.alpha_composite(node)
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
    # Optical centre of the mark sits at (256, 263) in the 512 grid.
    ox = round(SS / 2 - scale * SS * (256 / 512))
    oy = round(SS / 2 - scale * SS * (263 / 512))
    placed = Image.new("RGBA", (SS, SS), (0, 0, 0, 0))
    placed.alpha_composite(small, (ox, oy))

    disc.alpha_composite(cast_shadow(placed, blur=44, dy=34, opacity=0.16))
    disc.alpha_composite(placed)
    # keep the presentation strictly circular after the shadow pass
    mask = render('  <circle cx="256" cy="256" r="256" fill="#fff"/>').split()[3]
    disc.putalpha(mask)
    return disc


def save(img: Image.Image, out: Path, size: int) -> None:
    img.resize((size, size), Image.LANCZOS).save(out)
    print(f"  {out.relative_to(ROOT)}  {size}x{size}")


def main() -> None:
    (IMG / "brand" / "abitaresmart-mark.svg").write_text(mark_svg())
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

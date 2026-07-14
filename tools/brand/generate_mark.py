#!/usr/bin/env python3
"""Generate the AbitareSmart Signal mark and every web export from scratch.

The mark is pure vector geometry built on the Signal palette:
  - Ink #0B211F      architectural portal (open house silhouette)
  - Lime #DDF86A     precision signal channel (single arc, not generic Wi-Fi)
  - Coral #FF735C    source node (the intelligent hub)
  - Canvas #F7F4EC / Surface #EFEADF  circular presentation field

Outputs (all paths relative to repo root):
  assets/img/brand/abitaresmart-mark.svg      512 master, transparent
  assets/img/abitaresmart-mark.png            1400x1400 transparent (structured data)
  assets/img/abitaresmart-mark-web.png        512x512 transparent (navigation)
  assets/img/abitaresmart-mark-disc.svg       circular presentation (SVG favicon)
  assets/img/abitaresmart-mark-disc.png       512x512 circular (favicon + footer)
  assets/img/abitaresmart-mark-avatar.png     2048x2048 circular (touch icon + social)
"""

import math
from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parents[2]
IMG = ROOT / "assets" / "img"

INK = "#0B211F"
LIME = "#DDF86A"
CORAL = "#FF735C"
CANVAS = "#F7F4EC"
SURFACE = "#EFEADF"

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


def arc_path() -> str:
    a = math.radians(ARC_DEG)
    dx, dy = ARC_R * math.cos(a), ARC_R * math.sin(a)
    x1, x2 = NODE[0] - dx, NODE[0] + dx
    y = NODE[1] - dy
    return f"M {x1:.2f} {y:.2f} A {ARC_R} {ARC_R} 0 0 1 {x2:.2f} {y:.2f}"


def mark_group() -> str:
    return f"""  <path d="M {WALL_L} {BASE_Y} V {EAVE_Y} L 256 {APEX_Y} L {WALL_R} {EAVE_Y} V {BASE_Y}"
        fill="none" stroke="{INK}" stroke-width="{STROKE}"
        stroke-linecap="round" stroke-linejoin="round"/>
  <path d="{arc_path()}" fill="none" stroke="{LIME}"
        stroke-width="{ARC_W}" stroke-linecap="round"/>
  <circle cx="{NODE[0]}" cy="{NODE[1]}" r="{NODE_R}" fill="{CORAL}"/>"""


def mark_svg() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
{mark_group()}
</svg>
"""


def disc_svg() -> str:
    # Optical bounds of the mark: x 55-457, y 55-471 -> centre (256, 263).
    scale = 0.72
    tx = 256 - scale * 256
    ty = 256 - scale * 263
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="field" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{CANVAS}"/>
      <stop offset="1" stop-color="{SURFACE}"/>
    </linearGradient>
  </defs>
  <circle cx="256" cy="256" r="256" fill="url(#field)"/>
  <g transform="translate({tx:.2f} {ty:.2f}) scale({scale})">
{mark_group()}
  </g>
</svg>
"""


def render(svg: str, out: Path, size: int) -> None:
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(out),
                     output_width=size, output_height=size)
    print(f"  {out.relative_to(ROOT)}  {size}x{size}")


def main() -> None:
    mark = mark_svg()
    disc = disc_svg()

    (IMG / "brand" / "abitaresmart-mark.svg").write_text(mark)
    (IMG / "abitaresmart-mark-disc.svg").write_text(disc)
    print("  assets/img/brand/abitaresmart-mark.svg")
    print("  assets/img/abitaresmart-mark-disc.svg")

    render(mark, IMG / "abitaresmart-mark.png", 1400)
    render(mark, IMG / "abitaresmart-mark-web.png", 512)
    render(disc, IMG / "abitaresmart-mark-disc.png", 512)
    render(disc, IMG / "abitaresmart-mark-avatar.png", 2048)


if __name__ == "__main__":
    main()

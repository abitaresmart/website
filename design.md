# AbitareSmart Design Guidelines

Version: Signal 1.2

Applies to: `redesign-original-brand`

Primary implementation: `assets/css/abitaresmart-signal.css`

## 1. Brand direction

AbitareSmart should feel calm, intelligent, architectural, and human. The identity balances the confidence of a technology company with the warmth expected from a brand that works inside people's homes.

The system follows five principles:

1. **Clarity before decoration.** Every element should communicate purpose quickly.
2. **Confident energy.** Use strong hierarchy, generous space, and vivid color with discipline.
3. **Technology made human.** Technical details may appear, but the experience should never feel clinical.
4. **One coherent system.** The website, logo, interface states, imagery, and localized pages use the same visual language.
5. **Accessible by default.** Contrast, focus states, motion preferences, and semantic HTML are design requirements.

## 2. Color system

The Signal palette restores the original neon character of the redesign: botanical ink and warm paper provide a grounded base, while electric lime, mint, coral, and sky communicate intelligent energy. Saturated colors are accents, not page backgrounds.

### Core palette

| Family | Token | Hex | Role |
| --- | --- | --- | --- |
| Botanical | Ink | `#0B211F` | Primary text, dark sections, footer, dark buttons |
| Botanical | Ink soft | `#17302D` | Secondary dark text and elevated dark surfaces |
| Warm neutral | Canvas | `#F7F4EC` | Page background and editorial negative space |
| Warm neutral | Surface | `#EFEADF` | Alternate sections, panels, inactive surfaces |
| Warm neutral | White | `#FFFDF8` | Cards, overlays, and inverse copy |
| Electric | Primary | `#DDF86A` | Primary actions, energy cards, active diagrams |
| Electric | Primary hover | `#EBFF98` | Hover and pressed states |
| Mint | Primary pale | `#D8F7E8` | Informational and connected surfaces |
| Mint | Secondary soft | `#AEECCF` | Supporting feature surfaces and dark-button hover |
| Sky | Secondary | `#76C7F2` | Restrained supporting graphic details |
| Coral | Accent | `#FF735C` | Large highlights, nodes, and graphic emphasis |
| Coral | Accent strong | `#B93A31` | Accessible small accent text and focus rings |
| Slate | Muted text | `#66736F` | Secondary copy and metadata |
| Positive | Status | `#38A36D` | Connected state only, never decorative |
| Positive | Status strong | `#2E7D59` | Connected labels and check icons |

### Semantic CSS tokens

```css
:root {
  --color-ink: #0b211f;
  --color-ink-soft: #17302d;
  --color-canvas: #f7f4ec;
  --color-surface: #efeadf;
  --color-white: #fffdf8;
  --color-primary: #ddf86a;
  --color-primary-hover: #ebff98;
  --color-primary-soft: #ddf86a;
  --color-primary-pale: #d8f7e8;
  --color-secondary: #76c7f2;
  --color-secondary-soft: #aeeccf;
  --color-accent: #ff735c;
  --color-accent-strong: #b93a31;
  --color-text-muted: #66736f;
  --color-positive: #38a36d;
  --color-positive-strong: #2e7d59;
  --color-line: rgba(11, 33, 31, 0.14);
  --color-line-inverse: rgba(255, 255, 255, 0.16);
}
```

### Color usage rules

- Use **Canvas + Ink** as the default page pairing.
- Use **Ink + White/Canvas** for dark editorial sections.
- Use **Primary + Ink** for the main call to action.
- Use bright **Accent** for large display text and graphic nodes; use **Accent strong** for small text, links, and focus rings.
- Use **Primary**, **Primary pale**, and **Secondary soft** for feature cards and diagrams.
- Use no more than one saturated color as the focal point in a component.
- Coral and status green must never become general-purpose body-text colors.
- Do not use Primary, Primary pale, Secondary, or Secondary soft for body text.

### Verified contrast pairs

| Foreground | Background | Ratio | Use |
| --- | --- | ---: | --- |
| `#0B211F` | `#F7F4EC` | 15.27:1 | Body and display text |
| `#0B211F` | `#DDF86A` | 14.15:1 | Primary buttons |
| `#0B211F` | `#AEECCF` | 12.54:1 | Soft feature surfaces |
| `#B93A31` | `#F7F4EC` | 5.15:1 | Small accent text and links |
| `#66736F` | `#F7F4EC` | 4.50:1 | Muted body copy |
| `#FFFDF8` | `#0B211F` | 16.51:1 | Dark sections |

## 3. Logo

The AbitareSmart **Portale mark** is a freestanding smart-home icon, not a badge or app tile. Four elements create the meaning:

- the solid botanical-ink **architectural shell** — a softly rounded gabled silhouette — gives the mark confident, protective mass;
- the warm-white **arched doorway** (the *portale*) opens the shell to the ground, welcoming you into the inhabited home;
- the electric-lime **lunetta** — the fanlight window glowing at the top of the arch — communicates live intelligent energy without any Wi-Fi cliché;
- the coral **hub** floats in the doorway: the intelligent heart of the home.

The composition is solid mass plus luminous portal: you look through the wall of a secure home into its warm, connected centre. The geometry is pure vector, so it stays crisp from a 16 px favicon to full-bleed print. The PNG exports add restrained material lighting — a satin vertical tone with a quiet top-light on the shell, a recessed rim shadow under the arch, an enamel hub with a small specular, and soft contact shadows — composited at 2048 px and supersampled down. The materials stay quiet; the geometry carries the mark. There is no square container in the primary mark.

### Source assets

All assets are generated from a single script; never edit the exports by hand.

- Vector master: `assets/img/brand/abitaresmart-mark.svg` — 512 viewBox, transparent
- Primary website mark: `assets/img/abitaresmart-mark.png` — 1400 × 1400 transparent PNG
- Web-optimized mark: `assets/img/abitaresmart-mark-web.png` — 512 × 512 transparent PNG
- Circular presentation (vector): `assets/img/abitaresmart-mark-disc.svg` — SVG favicon
- Circular presentation (raster): `assets/img/abitaresmart-mark-disc.png` — 512 × 512 PNG favicon fallback and footer mark
- Social avatar: `assets/img/abitaresmart-mark-avatar.png` — 2048 × 2048 circular PNG
- Generator: `tools/brand/generate_mark.py` (requires `cairosvg`)

The transparent high-resolution mark is used in structured organization metadata; its optimized export is used in navigation. The circular presentation remains the footer treatment, and its 2048 px version remains available as a clean logo-first social avatar. Browser, touch, and PWA icon surfaces use the premium website presentation described below.

### Primary brand icon

The navbar pairs a dedicated minimal image mark with the live HTML wordmark **AbitareSmart**. The mark uses one Ink rounded-square field, one warm-white architectural ribbon, one electric smart-energy arc, one coral hub, and one restrained mint connection. Its low shape count and bold negative space keep it recognizable from the 48 px navbar presentation down to a 16 px favicon.

- Generated source: `assets/img/brand/abitaresmart-logo-artwork.png` — full-resolution RGB artwork
- Rounded master: `assets/img/brand/abitaresmart-logo-icon.png` — 1024 × 1024 RGBA
- Navbar export: `assets/img/brand/abitaresmart-logo-icon-96.png` — 96 × 96 RGBA
- Browser favicon: `assets/img/favicons/favicon.ico` — 16, 32, and 48 px
- High-resolution favicon: `assets/img/favicons/favicon-96x96.png`
- Apple touch icon: `assets/img/favicons/apple-touch-icon.png` — 180 × 180
- PWA icons: `assets/img/favicons/web-app-manifest-192x192.png` and `web-app-manifest-512x512.png`
- Exporter: `tools/brand/prepare_brand_logo.py` (requires Pillow)

The exporter creates transparent rounded corners for the navbar and browser assets, plus Canvas-backed Apple/PWA variants. The lettering remains HTML text rather than being embedded in the generated image.

### Detailed smart-home artwork

The detailed **smart-home illustration generated from scratch** remains available as a separate campaign-quality asset. A warm contemporary Italian home, connected energy paths, and a coral control hub communicate the product category directly without altering or imitating the canonical Portale logo.

- Source artwork: `assets/img/brand/abitaresmart-smart-home-artwork.png` — full-bleed generated RGB artwork
- Rounded master: `assets/img/brand/abitaresmart-premium-icon.png` — 1024 × 1024 RGBA
- Exporter: `tools/brand/prepare_smart_home_artwork.py` (requires Pillow)

The source artwork uses the complete site palette: Ink and Ink soft for structure, Canvas/Surface/White for architecture and atmosphere, Electric and Mint for connected energy, Sky for restrained system details, and Coral for the central hub. Its exporter applies a rounded-square crop and subtle Ink shadow without touching any active logo or favicon files.

### Logo rules

- Minimum digital size: **16 × 16 px** (favicon); prefer **42 px or larger** in layouts.
- Recommended navigation size: **42–48 px**.
- Keep external clear space equal to at least **12.5% of the primary mark width** on every side.
- Scale proportionally; never stretch, skew, rotate, crop, outline, recolor, or retrace the geometry.
- Do not add external shadows, glows, gradients, badges, borders, or square containers.
- Use the transparent primary mark on Canvas, Surface, White, or quiet light imagery.
- Use the circular presentation on Ink or other dark surfaces; do not place the ink portal directly on Ink.
- For social profiles, upload the 2048 px circular asset directly. The meaningful geometry is centred inside the circular crop-safe area.
- Keep the wordmark separate and editable as HTML text. Do not bake “AbitareSmart” into the image.

### Construction and color

The logo is anchored to four palette colors: Ink `#0B211F` for the solid architectural shell, White `#FFFDF8` for the arched doorway, Primary `#DDF86A` for the lunetta fanlight, and Accent `#FF735C` for the hub. The shell is a filled gabled pentagon with rounded corners; the doorway is a half-circle arch cut to the base of the silhouette; the lunetta is a filled half-disc concentric with the arch; the hub is a circle floating in the doorway. The material lighting in the exports uses only shaded derivatives of these colors and may not introduce a new decorative hue; no further colors, strokes, or effects may be added to the mark.

The primary mark has a transparent background. The circular presentation adds a Canvas-to-Surface tonal field so the mark survives dark browser chrome, platform downsampling, and Ink surfaces. This field must never be baked into the transparent website mark.

## 4. Typography

### Families

- **Manrope** is the primary family for navigation, headings, body text, buttons, and forms.
- **DM Mono** is the technical accent for eyebrows, labels, metadata, counters, and system details.
- Fallbacks: `Helvetica Neue`, Arial, sans-serif for Manrope; monospace for DM Mono.

### Type hierarchy

| Style | Implementation | Guidance |
| --- | --- | --- |
| Hero H1 | `clamp(4rem, 7.2vw, 7.25rem)` | One clear idea, short line lengths |
| Section H2 | `clamp(2.75rem, 5vw, 5.2rem)` | Editorial section statement |
| H3 | `1.65rem` | Card or subsection title |
| Body | `1rem / 1.65` | Default long-form reading |
| Label | `0.62–0.72rem`, DM Mono | Uppercase, tracked, concise |

Headings use tight tracking (`-0.045em`) and compact line-height (`1.04`). Body copy should remain relaxed and readable.

### Copy rules

- Prefer sentence case.
- Use uppercase only for short technical labels.
- Avoid jargon unless it helps the customer make a decision.
- Italian and English copy should sound native, not mechanically mirrored.
- Do not place essential text inside images.

## 5. Layout and spacing

- Maximum content width: **1240 px**.
- Default desktop gutter: **24 px per side**.
- Standard section spacing: `clamp(88px, 10vw, 152px)`.
- Desktop layouts may use a 12-column grid.
- Major compositions collapse to one column below **900 px**.
- Mobile gutters reduce below **680 px**.
- Keep paragraph measure near **60–72 characters** where possible.

Use asymmetric editorial grids for energy, but maintain consistent alignment between headings, copy, media, and controls.

## 6. Shape, borders, and depth

| Token | Value | Use |
| --- | ---: | --- |
| Small radius | `14px` | Compact controls and small cards |
| Default radius | `24px` | Cards and media |
| Large radius | `38px` | Hero media and CTA containers |
| Pill radius | `999px` | Buttons, language switchers, statuses |

Depth should remain quiet:

- Small shadow: `0 12px 35px rgba(11, 33, 31, 0.08)`.
- Large shadow: `0 32px 90px rgba(11, 33, 31, 0.18)`.
- Prefer borders and surface contrast over extra shadows.
- Never stack multiple heavy shadows on one component.

## 7. Components

### Buttons

- **Primary:** Electric-lime Primary background, Ink text, pale-lime hover background.
- **Dark:** Ink background, Canvas text; may invert to Secondary soft on hover.
- Minimum height: **44 px**; preferred primary height: **54 px**.
- Buttons use pill geometry and a subtle `translateY(-2px)` hover response.
- Every icon-only control must have an accessible name.

### Cards

- Default cards use White on Canvas with a low-contrast Ink border.
- Informational cards use Primary pale.
- Secondary feature cards use Primary soft or Secondary soft.
- Dark technical cards use Ink with White copy and electric-lime details.
- Avoid mixing Primary soft and Secondary soft inside the same small card.

### Navigation

- Sticky header uses a translucent Canvas surface with blur.
- The active experience relies on spacing and contrast rather than a heavy container.
- Language switching must remain visible and keyboard accessible.
- Mobile navigation must lock page scroll only while open.

### Status and focus

- Connected states use Positive, Positive strong, and Primary pale.
- Energy/active diagrams use Primary; supporting feature states use Secondary soft.
- Focus rings use a 3 px Accent strong outline with a 3 px offset.
- Never communicate state through color alone; retain iconography or text.

## 8. Imagery and illustration

- Favor calm, believable interiors with natural light and authentic materials.
- UI mockups should use the same semantic palette as the website.
- Avoid heavy neon filters over photography; saturated color belongs to the interface layer.
- Keep technical diagrams sparse, using Ink, Primary soft, and Accent as the center node.
- Generated imagery must not include text, third-party logos, or imaginary product branding.

## 9. Motion

- Standard interaction duration: **160–220 ms**.
- Large image transitions may use **500–700 ms**.
- Use motion to explain hierarchy or state, not as decoration.
- Keep transforms small: 2 px lift, slight icon rotation, or restrained image zoom.
- Respect `prefers-reduced-motion: reduce`; remove nonessential animation and smooth scrolling.

## 10. Localization

- Italian remains the root experience; English lives under `/en/`.
- Every translated page must preserve `lang`, `hreflang`, and `translation_url` relationships.
- Navigation order and component hierarchy remain consistent between languages.
- Allow text containers to expand; never rely on fixed heights for localized copy.
- Validate both languages after any navigation, footer, CTA, or metadata change.

## 11. Accessibility

- Target WCAG 2.2 AA for text and interactive elements.
- Preserve the skip link and visible keyboard focus.
- Use semantic headings in order and descriptive link text.
- Decorative images use empty alt text; meaningful images require localized alt text.
- Interactive targets should be at least **44 × 44 px**.
- Never rely on hover as the only way to reveal essential information.
- Test at 200% zoom and with reduced motion enabled.

## 12. Implementation checklist

Before merging a visual change:

1. Use existing semantic color tokens; do not add isolated hex values without documenting a new role.
2. Check contrast for any new text/background pair.
3. Verify Italian and English routes.
4. Test desktop, tablet, and mobile breakpoints.
5. Test keyboard navigation and visible focus.
6. Confirm reduced-motion behavior.
7. Run `jekyll build` and `git diff --check`.
8. Use a new versioned filename for cache-sensitive CSS or primary brand assets.

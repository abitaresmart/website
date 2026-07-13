# AbitareSmart Design Guidelines

Version: Signal 1.1

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

The AbitareSmart **Signal Portal** is one compact smart-home symbol built from three locked elements:

- the continuous warm-white **architectural portal** makes the home unmistakable;
- the single electric-lime **broadcast arch** communicates an active connected system without falling back to the generic three-wave Wi-Fi symbol;
- the coral **source node** represents the intelligent hub at the centre of the home.

The deliberately broad, low architecture feels stable and professional. The one-wave signal and node stay legible when the mark is reduced to a browser favicon or cropped into a circular social avatar. The dark Ink-soft tile is part of the logo, not an optional container.

### Source assets

- Primary website mark: `assets/img/abitaresmart-portal-logo.png` — 1024 × 1024 PNG
- Social avatar master: `assets/img/abitaresmart-social-avatar.png` — 2048 × 2048 PNG
- Compatibility/canonical icon: `assets/img/icon.png` — 1024 × 1024 PNG
- Reproducible rendering source: `tools/brand/render_logo.py`

The website mark is used by navigation, footer, favicon, touch icon, and structured organization metadata. The 2048 px master is the upload-ready asset for Instagram, Facebook, LinkedIn, X, TikTok, YouTube, and other social profiles.

### Logo rules

- Minimum digital size: **24 × 24 px**; prefer **32 px or larger** when space allows.
- Recommended navigation size: **42–48 px**.
- Keep external clear space equal to at least **12.5% of the tile width** on every side.
- Scale proportionally; never stretch, skew, rotate, crop, outline, recolor, or remove the Ink-soft tile.
- Do not add external shadows, gradients, badges, borders, or secondary containers.
- Do not place the mark over detailed photography unless the full square tile remains intact.
- For social profiles, upload the 2048 px master directly. Essential geometry is centred for both circular and rounded-square platform crops.
- Keep the wordmark separate and editable as HTML text. Do not bake “AbitareSmart” into the image.

### Construction and color

The logo uses only four brand colors: Ink soft `#17302D` for the tile, White `#FFFDF8` for the portal, Primary `#DDF86A` for the signal, and Accent `#FF735C` for the node. No gradients, shading, transparency, texture, or off-palette effects are permitted. Antialiasing at geometric edges is the only color interpolation allowed.

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

# AbitareSmart Design Guidelines

Version: Lumen 1.0

Applies to: `redesign-original-brand`

Primary implementation: `assets/css/abitaresmart-lumen.css`

## 1. Brand direction

AbitareSmart should feel calm, intelligent, architectural, and human. The identity balances the confidence of a technology company with the warmth expected from a brand that works inside people's homes.

The system follows five principles:

1. **Clarity before decoration.** Every element should communicate purpose quickly.
2. **Quiet confidence.** Use strong hierarchy, generous space, and restrained color.
3. **Technology made human.** Technical details may appear, but the experience should never feel clinical.
4. **One coherent system.** The website, logo, interface states, imagery, and localized pages use the same visual language.
5. **Accessible by default.** Contrast, focus states, motion preferences, and semantic HTML are design requirements.

## 2. Color system

The Lumen palette replaces the previous teal and orange identity. It is built from midnight navy, cobalt, iris, porcelain, and cool neutral surfaces.

### Core palette

| Family | Token | Hex | Role |
| --- | --- | --- | --- |
| Midnight | Ink | `#12192B` | Primary text, dark sections, footer, dark buttons |
| Midnight | Ink soft | `#1D2842` | Secondary dark text and elevated dark surfaces |
| Porcelain | Canvas | `#F7F7F2` | Page background and warm negative space |
| Neutral | Surface | `#E9ECF4` | Alternate sections, panels, inactive surfaces |
| Neutral | White | `#FFFFFF` | Cards, overlays, and text on primary color |
| Cobalt | Primary | `#4265E8` | Primary actions, active states, connectivity |
| Cobalt | Primary hover | `#304FC7` | Hover and pressed states |
| Cobalt | Primary soft | `#AFC0FF` | Feature surfaces, diagrams, icon backgrounds |
| Cobalt | Primary pale | `#DDE4FF` | Subtle status and informational surfaces |
| Iris | Secondary | `#8B78E6` | Supporting graphic details only |
| Iris | Secondary soft | `#D9D1FA` | Secondary surfaces and secure states |
| Iris | Accent | `#6654C7` | Highlighted words, links, focus, brand emphasis |
| Slate | Muted text | `#657086` | Secondary copy and metadata |

### Semantic CSS tokens

```css
:root {
  --color-ink: #12192b;
  --color-ink-soft: #1d2842;
  --color-canvas: #f7f7f2;
  --color-surface: #e9ecf4;
  --color-white: #ffffff;
  --color-primary: #4265e8;
  --color-primary-hover: #304fc7;
  --color-primary-soft: #afc0ff;
  --color-primary-pale: #dde4ff;
  --color-secondary: #8b78e6;
  --color-secondary-soft: #d9d1fa;
  --color-accent: #6654c7;
  --color-text-muted: #657086;
  --color-line: rgba(18, 25, 43, 0.14);
  --color-line-inverse: rgba(255, 255, 255, 0.16);
}
```

### Color usage rules

- Use **Canvas + Ink** as the default page pairing.
- Use **Ink + White/Canvas** for dark editorial sections.
- Use **Primary + White** for the main call to action.
- Use **Accent** for highlighted display text, links, and focus rings—not for large background areas.
- Use **Primary soft** and **Secondary soft** for feature cards and diagrams.
- Use no more than one saturated color as the focal point in a component.
- Do not introduce teal, orange, red, or green as brand colors. Semantic error/success colors may be added only when the interface genuinely requires those states.
- Do not use Primary soft, Primary pale, or Secondary soft for body text.

### Verified contrast pairs

| Foreground | Background | Ratio | Use |
| --- | --- | ---: | --- |
| `#12192B` | `#F7F7F2` | 16.29:1 | Body and display text |
| `#FFFFFF` | `#4265E8` | 4.93:1 | Primary buttons |
| `#6654C7` | `#F7F7F2` | 5.34:1 | Accent text and links |
| `#657086` | `#F7F7F2` | 4.64:1 | Muted body copy |
| `#FFFFFF` | `#12192B` | 17.51:1 | Dark sections |

## 3. Logo

The AbitareSmart mark combines three signals:

- the **house** communicates the physical home;
- the **wireless arcs** communicate connected technology;
- the **iris hub** communicates a central intelligent control point.

### Source assets

- Primary raster mark: `assets/img/abitaresmart-lumen.png`
- Compatibility/canonical icon: `assets/img/icon.png`

Both files contain the same transparent-background mark. The primary asset is used by navigation, footer, favicon, touch icon, and structured organization metadata.

### Logo rules

- Minimum digital size: **24 × 24 px**.
- Recommended navigation size: **42–48 px**.
- Keep clear space equal to at least **12.5% of the mark width** on every side.
- Scale proportionally; never stretch, skew, rotate, crop, outline, or recolor the mark.
- Do not add external drop shadows, badges, borders, or containers.
- Do not place the mark over detailed photography.
- Use the full-color mark on Canvas, White, Surface, or Ink backgrounds.
- Keep the wordmark separate and editable as HTML text. Do not bake “AbitareSmart” into the image.

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

- Small shadow: `0 12px 35px rgba(18, 25, 43, 0.08)`.
- Large shadow: `0 32px 90px rgba(18, 25, 43, 0.18)`.
- Prefer borders and surface contrast over extra shadows.
- Never stack multiple heavy shadows on one component.

## 7. Components

### Buttons

- **Primary:** Primary background, White text, Primary hover background.
- **Dark:** Ink background, Canvas text; may invert to Secondary soft on hover.
- Minimum height: **44 px**; preferred primary height: **54 px**.
- Buttons use pill geometry and a subtle `translateY(-2px)` hover response.
- Every icon-only control must have an accessible name.

### Cards

- Default cards use White on Canvas with a low-contrast Ink border.
- Informational cards use Primary pale.
- Secondary feature cards use Primary soft or Secondary soft.
- Dark technical cards use Ink with White copy and soft cobalt details.
- Avoid mixing Primary soft and Secondary soft inside the same small card.

### Navigation

- Sticky header uses a translucent Canvas surface with blur.
- The active experience relies on spacing and contrast rather than a heavy container.
- Language switching must remain visible and keyboard accessible.
- Mobile navigation must lock page scroll only while open.

### Status and focus

- Connected/active states use Primary and Primary pale.
- Secure/supporting states use Secondary and Secondary soft.
- Focus rings use a 3 px Accent outline with a 3 px offset.
- Never communicate state through color alone; retain iconography or text.

## 8. Imagery and illustration

- Favor calm, believable interiors with natural light and authentic materials.
- UI mockups should use the same semantic palette as the website.
- Avoid heavy blue or violet filters over photography.
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

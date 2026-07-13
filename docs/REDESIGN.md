# AbitareSmart — 2026 redesign direction

## Positioning

AbitareSmart should feel like a calm, design-conscious home consultancy that happens to be deeply technical. The new experience replaces generic smart-home tropes with a warmer promise: technology that recedes into the background and makes everyday living simpler, safer, and more considered.

**Italian promise:** La tecnologia si fa casa.

**English promise:** Technology, made at home.

## Visual concept — “Quiet intelligence”

- **Canvas:** warm ivory surfaces instead of clinical white.
- **Ink:** a very dark green-black for depth, confidence, and high contrast.
- **Signals:** mint for connected/active states, coral for warmth and human moments, electric lime for small moments of emphasis.
- **Shape:** generous radii, architectural grids, thin keylines, tactile switches, and soft ambient glows.
- **Imagery:** editorial Italian interiors with technology integrated discreetly. No floating gadgets, neon circuitry, stock-office scenes, or visible brand logos.
- **Motion:** restrained entrance reveals, tactile hover states, a live home-status panel, and reduced-motion support.

## Type

- A bold geometric sans for statements and navigation.
- A highly readable sans for long-form content.
- Oversized display type with compact tracking; sentence case rather than tech-industry uppercase everywhere.
- Small mono-like labels and numeric counters create a subtle systems layer.

## Information architecture

1. **Hero:** value proposition, consultation CTA, editorial home image, and compact live-status controls.
2. **Proof strip:** privacy-first, Matter/Thread ready, existing-device friendly, designed in Italy.
3. **Value bento:** security, simplicity, energy, and interoperability.
4. **Services:** consultation, system design, installation, and ongoing care.
5. **Method:** listen → design → connect → refine.
6. **Selected solutions:** three visual project stories instead of generic feature cards.
7. **Journal:** practical guidance that supports trust and organic discovery.
8. **FAQ:** concise native disclosure components.
9. **Consultation CTA + footer:** clear next step and full legal/navigation context.

## Localization model

- Italian remains the root locale (`/`); English lives at `/en/`.
- Localized page chrome, metadata, calls to action, form labels, service content, FAQs, legal pages, and journal index.
- Italian articles remain canonical source content; English article routes contain carefully translated editions.
- Every localized page exposes an obvious language switch and `hreflang` metadata.
- Locale is structural and server-rendered—no flash of untranslated content and no browser-translation dependency.

## Accessibility and responsive behavior

- WCAG-friendly contrast and visible keyboard focus.
- Semantic headings, landmarks, native `details`, descriptive image alternatives, and a skip link.
- Minimum 44px interactive targets.
- Mobile-first composition: the hero control panel becomes a compact card; project cards become a horizontal snap rail; navigation becomes a lightweight drawer.
- All animation respects `prefers-reduced-motion`.

## Asset system

- A new custom SVG monogram combines a house outline with a connected-node path.
- Interface icons are redrawn as a consistent 24px rounded-stroke SVG sprite.
- New PNG photography is generated specifically for the hero and project stories, then optimized for web delivery.
- Decorative glows, grids, and signal rings are CSS/SVG so they stay sharp at every density.


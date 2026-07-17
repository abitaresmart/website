# Artwork provenance

The smart-home source artwork at `assets/img/brand/abitaresmart-smart-home-artwork.png` was generated from scratch with Codex's built-in image-generation tool. It did not use the Portale logo or either previous website icon as an image reference.

`tools/brand/prepare_smart_home_artwork.py` applies the rounded-square layout separately and creates the preserved 1024 px campaign master at `assets/img/brand/abitaresmart-premium-icon.png`. It does not modify the active navbar or favicon assets.

## Final generation prompt

> Use case: stylized-concept
>
> Asset type: original premium smart-home website icon artwork, square master image before rounded-square layout treatment
>
> Primary request: From scratch, create a gorgeous, richly detailed hero illustration that instantly communicates “beautiful intelligent home.” Show one charming compact modern Italian home brought to life by elegant connected-home energy: softly glowing automated windows, a coral central control hub, and graceful luminous paths linking the house systems. The result should feel warm, aspirational, sustainable, clever, and premium—not like a corporate logo and not like a generic stock smart-home symbol.
>
> Scene/backdrop: A vivid, full-bleed miniature world at a magical warm sunrise. The smart home sits slightly elevated among sculpted botanical leaves and soft architectural terrain. Sweeping energy ribbons, tiny connected nodes, atmospheric brush streaks, and restrained sky shapes wrap around the home and create motion, depth, and a sense that the entire house is intelligently connected. The environment must remain readable and uncluttered at icon size.
>
> Subject: One distinctive contemporary home in a friendly three-quarter view, with deep botanical-ink roof and structure, warm canvas and white walls, softly illuminated electric-lime windows and doorway accents, mint connected-energy paths, a single polished coral hub at the heart of the composition, and a few restrained sky-blue system details. The home should feel inhabitable, welcoming, and architecturally refined, with clear roof, doorway, windows, terraces, and subtle smart-home control details. No people.
>
> Style/medium: Exceptionally polished hand-crafted 2.5D illustrated icon artwork with the richness of a flagship mobile-game icon. Dense sculpted painterly facets, tactile enamel-like surfaces, visible but refined brushwork, crisp silhouettes, layered atmospheric depth, premium editorial charm, sophisticated European design, beautiful micro-detail, and excellent readability. Not photorealism, not flat vector art, not a smooth generic 3D render.
>
> Composition/framing: Bold close-up square composition with the home filling about 68 percent of the canvas. Dynamic three-quarter perspective and a gentle upward visual flow. Keep all critical architecture, the coral hub, and the main energy connections inside the central 72 percent so a rounded-square crop can be applied later without losing content. Corners may contain only soft atmosphere, energy trails, leaves, or light. Strong recognizable silhouette at 32, 60, and 180 pixels. No border and no baked-in rounded corners.
>
> Lighting/mood: Cinematic warm sunrise rim light from upper left, luminous electric-lime interior glow, deep controlled botanical shadows, soft mint bounce light, subtle coral reflections, optimistic, welcoming, intelligent, secure, sustainable, playful, and luxurious.
>
> Color palette: Use only this AbitareSmart palette and natural mixtures/shading derived from it: Botanical Ink #0B211F for deepest structure and shadows; Botanical Ink soft #17302D for dimensional dark surfaces; Warm Canvas #F7F4EC for the atmospheric foundation; Warm Surface #EFEADF for terrain and secondary architecture; Warm White #FFFDF8 for walls and highlights; Electric Primary #DDF86A for intelligent lighting and energy accents; Electric Primary hover #EBFF98 for hot highlights; Mint Primary pale #D8F7E8 for luminous atmospheric surfaces; Mint Secondary soft #AEECCF for connected pathways and foliage; Sky Secondary #76C7F2 for restrained system details and sky accents; Coral Accent #FF735C for the central smart-home hub and major focal accent; Coral Accent strong #B93A31 for small coral shadows; Slate Muted #66736F only for subtle neutral detail; Positive #38A36D and #2E7D59 only as tiny connected-state signals. Do not introduce purple, magenta, bright red, royal blue, black, gray, brown, or colors outside this palette.
>
> Materials/textures: Hand-painted tile-like micro-facets, warm ceramic walls, satin dark roof, translucent luminous windows, polished coral enamel hub, softly textured paper-grain atmosphere, layered foliage, crisp rim highlights, tiny light particles, and finely controlled energy trails.
>
> Smart-home storytelling: Communicate intelligence through the house itself and the elegant relationships between its lights, windows, energy, climate, security, and central coral hub. The connected paths should feel organically integrated into the architecture and landscape, never like a pasted-on diagram.
>
> Constraints: Completely original composition generated from scratch. Full-bleed square artwork with no transparency. No text, letters, numbers, wordmark, existing logo, watermark, UI, screenshot frame, device mockup, external rounded-corner mask, app-store frame, giant Wi-Fi glyph, padlock glyph, robot, human character, floating phone, generic circuit-board house outline, or multiple houses. No cropped roof or doorway. Preserve clear breathing room for the later rounded-square layout.
>
> Avoid: minimal logo, flat icon, sparse beige background, generic plastic render, stock illustration, sterile corporate infographic, photorealistic real-estate image, excessive tiny gadgets, visual clutter, dark horror mood, childish toy-house proportions.

## Premium illustrated brand icon

The navbar/favicon source at `assets/img/brand/abitaresmart-logo-artwork.png` was generated with the same built-in image-generation tool. The Skybound App Store icon was supplied only as the rendering-quality, lighting, texture, and craftsmanship reference; its subject and composition were explicitly excluded. The wordmark is intentionally absent from the image and rendered as live HTML beside the mark. `tools/brand/prepare_brand_logo.py` produces the rounded navbar, favicon, Apple touch, and PWA assets.

### Final generation prompt

> Use case: stylized-concept
>
> Asset type: premium illustrated brand icon for the AbitareSmart website navbar, favicon, Apple touch icon, and PWA icon
>
> Primary request: Create a completely new, studio-quality illustrated brand icon for AbitareSmart, a premium Italian smart-home company. Design a distinctive “Living Portal”: one compact sculpted architectural object that feels like the intelligent heart of a beautiful home. It must be richer, more memorable, and more art-directed than a conventional flat logo, while remaining readable beside the separate HTML wordmark “AbitareSmart” at 48 pixels.
>
> Input images: Image 1 is the exact benchmark for rendering quality, craftsmanship, material richness, lighting discipline, painterly micro-facets, energy, depth, silhouette clarity, and premium finish. Match its top-tier illustrated-icon quality and hand-crafted confidence. Do not copy its bird, scarf, clouds, composition, or colors.
>
> Subject: One heroic house-shaped architectural artifact in a subtle three-quarter view. Build it from layered Botanical Ink and Ink-soft sculpted panels with a beautiful warm-white portal cut into its center. A luminous electric-lime energy ribbon emerges from the portal, sweeps upward in one elegant diagonal gesture, curls around part of the architecture, and reconnects to a polished coral hub jewel near the threshold. Add only two or three tiny mint/sky nodes embedded into the object to suggest lighting, climate, energy, and security working together. The portal should glow warmly from within and feel inhabited, intelligent, secure, sustainable, and welcoming. The object must have a unique silhouette—not a generic house outline.
>
> Scene/backdrop: Full-bleed atmospheric Botanical Ink and Ink-soft field with layered mint, pale mint, and restrained sky brushwork. Use a few sweeping energy streaks, tiny geometric particles, and a warm Canvas/White light bloom behind the object to create separation and movement. Keep the environment abstract and subordinate, not a literal room, garden, landscape, or infographic. Do not bake in rounded corners; the rounded-square layout will be applied afterward.
>
> Style/medium: Premium hand-crafted 2.5D illustrated brand icon with the same exceptional finish as Image 1: dense sculpted painterly facets, tactile enamel and ceramic materials, crisp silhouettes, beautiful microtexture, layered atmospheric depth, carefully controlled reflected light, small hand-painted imperfections, and sophisticated European editorial character. It should feel commissioned from a world-class illustration and identity studio. Not a flat vector logo, not smooth generic 3D, not clip art.
>
> Composition/framing: Bold close-up focal object filling approximately 70 percent of the square canvas, centered with a subtle dynamic diagonal ascent. Keep the complete object, portal, lime ribbon, and coral hub inside the central 72 percent so a rounded-square crop can be applied safely. Strong massing and clear large shapes at 16 and 48 pixels; reward larger viewing sizes with refined surface detail. No border, no external frame, no tiny hairlines.
>
> Lighting/mood: Warm sunrise rim light from upper left, luminous portal glow, deep controlled Botanical shadows, lime and coral reflected highlights, dimensional contact shadows, optimistic, calm, intelligent, luxurious, secure, human, and quietly magical. Match Image 1’s strong edge lighting and disciplined glow rather than using flat ambient illumination.
>
> Color palette: Use only the AbitareSmart palette and natural tonal mixtures derived from it: Botanical Ink #0B211F and Ink soft #17302D for structure, background, and shadows; Canvas #F7F4EC, Surface #EFEADF, and White #FFFDF8 for the portal and warm light; Electric Primary #DDF86A and Primary hover #EBFF98 for the main energy ribbon and hot highlights; Primary pale #D8F7E8 and Secondary soft #AEECCF for atmospheric layers and connected details; Sky #76C7F2 for very restrained system accents; Coral Accent #FF735C and Accent strong #B93A31 for the hub jewel and reflected depth; Slate #66736F only for subtle neutral surface variation; Positive #38A36D and #2E7D59 only as tiny connected-state accents. Do not introduce purple, magenta, royal blue, black, brown, or colors outside this palette.
>
> Materials/textures: Satin Botanical architectural panels, warm ceramic portal, translucent lime energy ribbon, polished coral enamel hub, hand-painted tile-like micro-facets, subtle paper grain, luminous edge paint, and restrained atmospheric brush streaks.
>
> Brand character: Italian warmth, architectural intelligence, sustainable technology, premium craftsmanship, calm confidence. The image must feel ownable and distinctive rather than assembled from common smart-home symbols.
>
> Constraints: One object only; no text, letters, initials, numbers, wordmark, watermark, existing AbitareSmart logo, generic house-outline icon, Wi-Fi glyph, toggle switch, circuit-board pattern, padlock, shield, key, plug, lightbulb, robot, phone, people, furniture, realistic house, multiple buildings, UI, logo presentation sheet, app-store badge, device mockup, or baked rounded-corner mask. No disconnected decorative symbols. Keep every accent integrated with the architecture.
>
> Avoid: childish simplicity, stock icon geometry, sparse empty field, cheap plastic, flat corporate logo, generic home-automation glyph, random arc-and-dot composition, excessive realism, clutter, illegibility, or a literal miniature-house scene.

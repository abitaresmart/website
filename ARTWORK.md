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

## Minimal brand-logo icon

The navbar/favicon source at `assets/img/brand/abitaresmart-logo-artwork.png` was generated independently with the same built-in image-generation tool. The wordmark is intentionally excluded from the image and rendered as live HTML beside the mark. `tools/brand/prepare_brand_logo.py` produces the rounded navbar, favicon, Apple touch, and PWA assets.

### Final generation prompt

> Use case: logo-brand
>
> Asset type: premium minimal brand icon for the AbitareSmart website navbar, favicon, Apple touch icon, and PWA icon
>
> Primary request: Create one original, exceptionally polished minimal logo icon for AbitareSmart, a premium Italian smart-home brand. The image will sit immediately to the left of the separately rendered wordmark “AbitareSmart,” so the icon itself must contain no text. It must communicate home, intelligence, warmth, connectivity, and refined sustainable living with a tiny number of bold shapes and remain instantly recognizable at 16 pixels.
>
> Concept: A deep Botanical Ink rounded-square field containing one elegant warm-white architectural ribbon that forms both a simple pitched roof and an open doorway/portal in a single coherent symbol. Inside the architecture, add one short electric-lime energy arc and one small coral circular hub connected by a restrained mint detail. The relationship between roof, portal, arc, and hub should imply an intelligent connected home without using a Wi-Fi glyph, circuit-board pattern, padlock, plug, lightbulb, or letter.
>
> Scene/background: One logo only, centered straight-on. The Botanical Ink rounded square fills approximately 94 percent of the canvas, with a corner radius around 22 percent and only tiny warm Canvas corner areas outside it. No scenery, landscape, room, garden, sky, decorative background objects, or presentation mockup.
>
> Style/medium: Premium minimal brand design with crisp, deliberate geometry and superb optical balance. Mostly flat graphic forms with restrained tactile finish: subtle satin depth in the Ink field, warm ceramic character in the white symbol, a tiny enamel highlight on the lime arc and coral hub, and extremely subtle paper grain. Sophisticated contemporary European identity design. Clean enough to reproduce as a simple vector later, but rendered as a beautiful finished image now.
>
> Composition/framing: One symmetrical or near-symmetrical symbol centered in the rounded square. The interior mark occupies about 58 percent of the canvas and uses thick, favicon-safe forms with generous negative space. No thin hairlines. All essential details remain legible at 16, 32, 42, and 48 pixels. Strong silhouette, even margins, front-on orthographic view, no perspective.
>
> Lighting/mood: Restrained soft top-left highlight, calm, intelligent, welcoming, secure, premium, quietly optimistic. No cinematic scene lighting, glow clouds, lens flare, or dramatic shadows.
>
> Color palette: Use only Botanical Ink #0B211F, Ink soft #17302D, Canvas #F7F4EC, White #FFFDF8, Electric Primary #DDF86A, Electric hover #EBFF98, Mint pale #D8F7E8, Mint soft #AEECCF, Coral #FF735C, and Coral strong #B93A31.
>
> Shape budget: One rounded-square field, one unified architectural symbol, one lime arc, one coral hub, and at most one tiny mint connector. Every element must earn its place. Reduce rather than decorate.
>
> Constraints: One icon only. No text, letters, initials, numbers, wordmark, watermark, existing logo, multiple options, logo sheet, grid, border frame, app-store badge, device mockup, shadows outside the rounded square, transparent checkerboard, house illustration, multiple windows, roof tiles, chimney, furniture, people, plants, landscape, tiny devices, generic Wi-Fi symbol, circuit traces, lock, shield, key, plug, robot, or excessive detail.
>
> Avoid: complex illustration, realistic house, mobile-game scene, stock smart-home icon, generic clip art, overly cute style, glossy plastic 3D, thick bevels, neon glow, clutter, gradients that muddy the palette, thin lines, small illegible details, letter A, letter S.

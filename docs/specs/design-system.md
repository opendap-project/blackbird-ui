# OpenDAP design system

- **Status:** Draft. This is the maintainers' design direction (2026-10-22). Values are starting points: colours, sizes and timings are to be validated on the first prototype's display and hardware.
- **Date:** 2026-10-22
- **Scope:** visual language, interaction patterns and design tokens for the OpenDAP OS interface, OpenDAP Desktop, documentation and product renders. The physical product's materials and geometry are summarised here and specified in the [case industrial-design spec](https://github.com/opendap-project/case/blob/main/docs/specs/industrial-design.md); the body buttons in the [controls and status LED spec](https://github.com/opendap-project/t1/blob/main/docs/specs/controls-and-status-led.md).
- **Tokens:** [`tokens/opendap.tokens.json`](../../tokens/opendap.tokens.json) is the canonical source of every value below.
- **Requirements:** DS-001, DS-006 to DS-013 in this repository; SYS-009, SYS-021 to SYS-030, SYS-033 to SYS-037 in [`system`](https://github.com/opendap-project/system/blob/main/docs/requirements/README.md); T1-014, T1-015, T1-022, T1-056, T1-057, T1-059 in [`t1`](https://github.com/opendap-project/t1/blob/main/docs/requirements/README.md).

**Design principle: engineering excellence, made approachable.**

The OpenDAP T1 is a digital audio player first. Every rule here serves that: playback, volume and the current track come before anything else on screen, and nothing visual may cost a frame of the interface or a sample of the audio.

## Contents

1. [Philosophy and principles](#1-philosophy-and-principles)
2. [Identity](#2-identity)
3. [Colour](#3-colour)
4. [Plasma gradients](#4-plasma-gradients)
5. [Thermal refraction](#5-thermal-refraction)
6. [Materials and geometry (summary)](#6-materials-and-geometry-summary)
7. [Physical controls (summary)](#7-physical-controls-summary)
8. [Interaction](#8-interaction)
9. [Typography](#9-typography)
10. [Spacing, radii, borders and elevation](#10-spacing-radii-borders-and-elevation)
11. [Motion](#11-motion)
12. [Lighting and effects](#12-lighting-and-effects)
13. [Accessibility](#13-accessibility)
14. [Design tokens](#14-design-tokens)
15. [Components](#15-components)
16. [Product renders](#16-product-renders)
17. [Performance](#17-performance)
18. [Alignment with OpenDAP requirements](#18-alignment-with-opendap-requirements)
19. [Review checklist](#19-review-checklist)
20. [Decisions and open questions](#20-decisions-and-open-questions)

## 1. Philosophy and principles

OpenDAP combines the precision of aerospace instrumentation with the ergonomics and approachability of contemporary consumer electronics. The product should feel like a carefully engineered instrument, not a gaming accessory or a generic smartphone.

The design language draws on:

- **Aerospace instrumentation:** functional surfaces, material discipline and purposeful indicators.
- **Material restraint:** restrained geometry, graphite surfaces, low-reflectivity finishes and subtle structural details.
- **Contemporary consumer electronics:** rounded corners, tactile controls, visual clarity and intuitive interactions.
- **Thermal and plasma physics:** controlled luminous gradients, heat distortion and energetic colour transitions, used as a distinctive and occasional visual signature.
- **Human-centred industrial design:** ergonomic controls, predictable interactions, accessible contrast and minimal cognitive load.

### Principles

1. **Function before decoration.** Every visible detail communicates function, improves interaction or reinforces product identity.
2. **Approachable engineering.** The device feels sophisticated without intimidating non-technical users.
3. **Material authenticity.** Surfaces suggest plausible manufactured materials, not artificial science-fiction textures.
4. **Controlled energy.** Plasma and thermal effects give identity; they are never continuous visual noise.
5. **Tactility matters.** Physical and digital controls communicate their purpose through shape, position, feedback and consistency.
6. **Quiet by default.** Most of the interface is neutral; colour and motion are reserved for meaningful states.
7. **Open by design.** The visual language never implies a sealed enclosure, needless complexity or inaccessible technology.

## 2. Identity

### 2.1 Attributes

| Attribute | Expression |
|---|---|
| Technical | Precise geometry, consistent alignment, functional details |
| Human | Rounded shapes, comfortable proportions, clear labels |
| Open | Transparent hierarchy, understandable controls, minimal ornament |
| Refined | Restrained colours, subtle textures, deliberate spacing |
| Energetic | Plasma gradients and thermal refraction in selected places |
| Durable | Matte finishes, robust shapes, realistic materials |

### 2.2 What the design is not

- Aggressive or hostile aesthetics, or overly sharp geometry.
- Cyberpunk or neon styling.
- Decorative circuit-board patterns.
- Exposed screws, vents or machined parts that have no function.
- Full-metal construction as the default visual assumption.
- Excessive glow, bloom, lens flares or animated backgrounds.
- Dense instrumentation where ordinary playback controls are enough.
- Smartphone interfaces copied without adapting them to a dedicated audio device.

The target: precision without aggression, sophistication without complexity, technology without intimidation.

## 3. Colour

The palette is graphite, white and one restrained orange accent. Plasma colours add a wider spectrum only where they serve a specific purpose (§4).

### 3.1 Core palette

| Token | Value | Purpose |
|---|---|---|
| `color.graphite.950` | `#111315` | Primary dark background |
| `color.graphite.900` | `#191C1F` | Main surfaces |
| `color.graphite.850` | `#202428` | Raised panels |
| `color.graphite.800` | `#292E33` | Secondary controls |
| `color.graphite.700` | `#3A4148` | Separators |
| `color.graphite.500` | `#737C85` | Muted icons and large labels (see §3.4) |
| `color.white` | `#F5F6F4` | Primary text, high-contrast details |
| `color.white-muted` | `#C6CBD0` | Secondary text |
| `color.orange.500` | `#FF6A2A` | Brand accent |
| `color.orange.400` | `#FF874D` | Hover, active highlight, focus |
| `color.orange.700` | `#C84719` | Pressed, gradient transitions |

The orange is to be validated against the physical accent part (§7) under the same light, and every pair is to be checked for contrast before production.

### 3.2 Semantic colours

Semantic colours communicate state, never decoration, and keep one meaning everywhere.

| Token | Value | Meaning | Status LED equivalent (IEC 60073) |
|---|---|---|---|
| `color.state.error` | `#FF5D65` | Error, fault or critical state | Red: danger, fault |
| `color.state.warning` | `#F3C66B` | Warning, attention required | Amber: abnormal or warning |
| `color.state.success` | `#64D6A1` | Successful operation, normal | Green: normal |
| `color.state.info` | `#69BFFF` | Information that asks for attention or an action; system activity | Blue: action required |
| `color.state.processing` | `#A995FF` | Processing or computational activity | none (see §18.4) |

Neutral information uses the neutral text colours, as the status LED uses white.

### 3.3 Distribution

As a starting guideline, not a pixel quota: 75–90 % graphite surfaces; 5–15 % white and muted content; 2–5 % orange; plasma and semantic colours only in localised areas.

### 3.4 Measured contrast

WCAG 2 contrast ratios computed from the token values (sRGB relative luminance):

| Foreground | on `graphite.950` | on `graphite.900` | on `graphite.850` | on `graphite.800` |
|---|---|---|---|---|
| `text` `#F5F6F4` | 17.2 | 15.8 | 14.4 | 12.6 |
| `text-secondary` `#C6CBD0` | 11.4 | 10.5 | 9.6 | 8.4 |
| `text-muted` `#939BA3` | 6.6 | 6.1 | 5.6 | 4.9 |
| `graphite.500` `#737C85` | 4.4 | 4.0 | 3.7 | 3.2 |
| `brand` `#FF6A2A` | 6.5 | 6.0 | 5.5 | 4.8 |
| `error` `#FF5D65` | 6.2 | 5.7 | 5.2 | 4.6 |
| `border` `#343A40` | 1.6 | 1.5 | 1.4 | 1.2 |
| `border-strong` `#515A63` | 2.7 | 2.4 | 2.2 | 2.0 |

Consequences:

- `graphite.500` fails AA (4.5:1) for body text on every surface. Use it only for icons and large text (3:1), or use `text-muted`.
- On an orange fill, the foreground is dark: `graphite.950` on `brand` is 6.5:1; `white` on `brand` is 2.6:1 and is not allowed for text or icons.
- `border` and `border-strong` are below 3:1. They may separate surfaces, but a control whose boundary is needed to find it carries a 3:1 cue another way (fill contrast, label or icon), per WCAG 1.4.11.

## 4. Plasma gradients

Plasma is OpenDAP's occasional visual signature: concentrated energy and heat, without depicting a literal source in every component. It is a **special visual mode, never the default surface treatment** (DS-009).

### 4.1 Character

- A concentrated white or near-white core.
- A transition through warm orange and amber.
- Localised violet or magenta transitions; occasional cyan dispersal at the outer edge.
- Soft volumetric halos with organic, asymmetric contours, not perfect concentric rings.
- Strong contrast against graphite, and a sense of energy moving through space.

The result is luminous, layered and physically plausible, not a multicolour wallpaper. Violet and cyan are secondary transitions, never competing brand colours.

### 4.2 Reference recipe

Tokens: `plasma.*` in the token file. The CSS below is a reference recipe for web, documentation and OpenDAP Desktop; the device renders with Slint (§18.1).

```css
.plasma-gradient {
  background: radial-gradient(
    ellipse at 46% 54%,
    rgba(255, 253, 249, 0.98) 0%,
    rgba(255, 177, 92, 0.92) 7%,
    rgba(255, 106, 42, 0.82) 19%,
    rgba(220, 107, 255, 0.43) 39%,
    rgba(119, 92, 255, 0.23) 54%,
    rgba(91, 220, 255, 0.12) 68%,
    transparent 78%
  );
}
```

Glow is built from several layers rather than one large blur:

```css
.plasma-glow {
  position: relative;
  isolation: isolate;
  background: var(--color-bg);
}
.plasma-glow::before {
  content: "";
  position: absolute;
  inset: 8%;
  z-index: -1;
  border-radius: 50%;
  background: radial-gradient(
    ellipse at 48% 50%,
    rgba(255, 247, 237, 0.95) 0%,
    rgba(255, 106, 42, 0.72) 15%,
    rgba(220, 107, 255, 0.28) 38%,
    rgba(91, 220, 255, 0.12) 58%,
    transparent 75%
  );
  filter: blur(22px);
  opacity: 0.82;
  pointer-events: none;
}
```

These are recipes, not mandatory gradients: tune the balance, blur and opacity for the surface, the display and the intended intensity.

### 4.3 Where plasma belongs

**Use for:** a dedicated visualiser or now-playing background; boot and selected transition moments; audio-reactive visualisation; processing indicators where a luminous metaphor fits; a restrained signature in documentation and renders; selected status and experimental screens.

**Never use for:** buttons in general; text backgrounds; routine lists and settings screens; warnings that already have a semantic colour; small icons that a glow would make illegible.

## 5. Thermal refraction

Thermal refraction is the distortion heat produces around an energetic source: subtle optical deformation, not smoke, fire or a plain blur. It stays subordinate to content: nobody ever has to read a distorted label or icon.

### 5.1 Character

Slightly displaced contours; layered translucent waves; low-amplitude irregular distortion; softly shifting gradients; localised luminance changes; organic asymmetry; minimal interference with text and controls.

### 5.2 Layers

1. **Source:** a localised plasma or warm light source.
2. **Refraction:** subtle wave-like distortion of the source or background.
3. **Atmosphere:** a very low-opacity colour haze that gives depth.

The layers are independent, so each can be reduced, disabled or replaced without changing the layout.

### 5.3 Reference recipe (atmosphere only)

```css
.thermal-field {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  background: var(--color-bg);
}
.thermal-field::before {
  content: "";
  position: absolute;
  inset: -12%;
  z-index: -1;
  background:
    radial-gradient(ellipse at 35% 55%, rgba(255, 106, 42, 0.19), transparent 43%),
    radial-gradient(ellipse at 67% 38%, rgba(119, 92, 255, 0.13), transparent 48%),
    radial-gradient(ellipse at 60% 72%, rgba(91, 220, 255, 0.08), transparent 42%);
  filter: blur(24px);
  pointer-events: none;
}
```

This is the atmospheric field, not optical refraction. Real displacement needs a tested displacement filter, a shader or a pre-rendered texture; `backdrop-filter: blur()` alone does not produce heat distortion.

### 5.4 Rules

- Prefer a static atmospheric field over continuous animation.
- Use real displacement only where the platform renders it within the frame budget (§17).
- Avoid large filter regions that force expensive repaints.
- Keep important text on a stable, undistorted layer.
- No continuous shader work on the battery-powered device unless it is measured within budget.
- Honour the reduced-effects mode (§12.4).
- Test contrast against every background the effect can produce.

## 6. Materials and geometry (summary)

The physical product is specified in the [case industrial-design spec](https://github.com/opendap-project/case/blob/main/docs/specs/industrial-design.md). In short:

- A predominantly synthetic palette: matte graphite polymer for the body (CASE-020, CASE-021), with satin or anodised details, translucent light guides and elastomer only where they have a function.
- Three geometry families, shared by hardware and interface: **primary** (rounded rectangles, broad radii: enclosure, panels, cards), **control** (circles, capsules, segmented capsules, soft concavity: buttons, button groups and their on-screen counterparts) and **instrumentation** (fine lines, arcs, restrained markings: secondary information). Instrumentation never overpowers the primary geometry.
- Edges are softened by geometry, highlights and material transitions, never by bright outlines or exaggerated chamfers.

Digital radii (§10.2) are interface tokens; physical radii are set by industrial design and manufacturing (CASE-028).

## 7. Physical controls (summary)

Specified in the [controls and status LED spec](https://github.com/opendap-project/t1/blob/main/docs/specs/controls-and-status-led.md) (§ Physical control design). The button design in the [T1 concept art](https://github.com/opendap-project/t1/tree/main/docs/concept-art) governs (T1-059); this spec describes it. Other details in that concept art are stale (480 × 800 screen, 1.27 mm pins, earlier dimensions) and are not a source.

Seen from the front:

- **Left edge, top: Action** (T1-014, T1-022). A round disc, subtly concave, with deeper travel and a clearer click. It is the main action button and the only control in the orange brand accent.
- **Left edge, below Action: Volume + and Volume −.** Two half-capsules: together they form one capsule split across the middle, each half with a rounded outer end and a flat inner edge at the split, operated as two separate buttons. Not a rocker. This pair is the reference instance of the **button group** pattern (§15.1).
- **Right edge: Main (power)** (T1-015). A taller capsule with horizontal ribs, so it is identified by touch.
- Everything is graphite except Action.

On screen, the same hierarchy holds: one primary action per screen carries the orange emphasis, and button groups use the same segmented capsule (§15).

## 8. Interaction

### 8.1 A dedicated device

The T1 is an audio player, not a general-purpose smartphone. The interface puts first:

1. immediate playback control;
2. fast access to the current track or source;
3. clear volume and output status;
4. reliable navigation through the library, at any size (T1-046, SYS-033);
5. readable metadata;
6. settings and diagnostics when needed.

Do not add a conventional app launcher, dashboards or complex navigation only because they are familiar from smartphones.

### 8.2 Hierarchy

Every screen has a **primary** level (the current task or the most important information), a **secondary** level (supporting controls and metadata) and a **tertiary** level (technical detail, diagnostics, optional configuration). Technical detail is available on demand, never permanently in the way.

### 8.3 Touch targets

Sized in millimetres on the real panel, then converted to pixels (§18.2):

| Target | Minimum | On the T1 panel (166 ppi) |
|---|---|---|
| Any touch target | 6.7 mm | 44 × 44 px |
| Primary and frequent actions | larger than the minimum; value set on the prototype | — |
| Gap between destructive or mutually exclusive actions | 1.2 mm | 8 px (`space.2`) |
| On-screen keyboard keys (documented exception) | 4.9 mm wide, 7.0 mm tall | 32 × 46 px, with long-press alternates and hit-target correction |

For physical controls, evaluate actual size, finger clearance, reach and tactile discrimination rather than applying pixel targets.

### 8.4 Feedback

Every interaction gets immediate, unambiguous feedback within the [experience budgets](https://github.com/opendap-project/t1/blob/main/docs/specs/experience-budgets.md) (touch to visual response ≤ 50 ms ideal; T1-057):

- a volume change shows a visible value or level change;
- the playback state has a clear icon, and a label where it helps;
- connection errors look different from buffering or loading;
- long operations show progress and allow cancelling where possible;
- destructive actions ask for proportionate confirmation;
- what the screen shows always matches what the device is doing (T1-057).

Animation clarifies a change of state; it never decorates every interaction.

## 9. Typography

Type communicates precision and stays comfortable for everyday reading.

### 9.1 Roles

| Role | Family | Use |
|---|---|---|
| Interface | IBM Plex Sans (and its script companions, §9.4) | All interface text |
| Technical | IBM Plex Mono | Values, timestamps, identifiers, formats and sample rates, diagnostics, tabular data |
| Fallback | System sans-serif and monospace | Web and Desktop only, when Plex is not available |

The technical face is for values that benefit from fixed-width comparison, not for every paragraph.

### 9.2 Hierarchy

| Role | Treatment |
|---|---|
| Screen title | Clear, medium or semibold |
| Primary value | Prominent, highly legible |
| Section label | Compact and restrained |
| Body text | Comfortable regular weight |
| Technical metadata | Monospaced where it improves comparison |
| Auxiliary label | Muted but readable (`text-muted`, never `graphite.500` for small text) |

Avoid wide tracking, tiny uppercase labels and condensed futuristic faces. Uppercase never applies to scripts without case, and is never forced by a template (DS-006).

### 9.3 Legibility

Consistent line height; no long uppercase passages; a clear difference between primary and secondary text; no small text over plasma or thermal effects; the minimum type size is tested on the target display. The type scale (sizes and line heights) is not defined yet: it is set on the prototype panel and added to the tokens.

### 9.4 Script coverage

The UI ships with English, Mandarin Chinese, Hindi, Spanish and Arabic (SYS-028, DS-011). IBM Plex has a companion family for each launch script, all under the SIL Open Font License 1.1, checked in the [IBM/plex repository](https://github.com/IBM/plex) on 2026-10-22:

| Script | Languages | Family | Package version | Regular OTF size |
|---|---|---|---|---|
| Latin | English, Spanish | IBM Plex Sans; IBM Plex Mono | 1.1.0; 2.5.0 | — |
| Han (Simplified) | Mandarin Chinese | IBM Plex Sans SC | 1.1.0 | 6.98 MB (hinted) |
| Han (Traditional) | not a launch locale | IBM Plex Sans TC | 1.1.1 | — |
| Devanagari | Hindi | IBM Plex Sans Devanagari | 1.1.0 | 0.18 MB |
| Arabic | Arabic | IBM Plex Sans Arabic | 1.1.0 | 0.17 MB |

Each family ships eight weights (Thin to Bold, plus Text). **UNVERIFIED:** glyph coverage of Plex Sans SC against the characters Chinese library metadata needs; shaping quality of Plex Sans Devanagari conjuncts and Plex Sans Arabic joining through parley and HarfRust; whether Plex Mono's Latin-only coverage needs a per-script fallback for technical values in Arabic or Hindi locales (for example Arabic-Indic digits); and the storage budget against the alternative in the [i18n research](https://github.com/opendap-project/system/blob/main/docs/research/2026-10-text-input-and-i18n.md) (Noto Sans SC subset, 8.33 MB). The per-script font packs and the CJK subset for first boot follow that research.

### 9.5 Right-to-left

Arabic makes right-to-left a launch requirement (SYS-025). Layouts mirror: leading and trailing swap, horizontal sequences reverse, directional icons (back, forward, chevrons, progress direction) flip. Media transport controls (previous, play/pause, next) and the seek bar's time direction do not mirror, following platform practice (the exact rule set is **UNVERIFIED**). Slint does not mirror layouts yet ([#2294](https://github.com/slint-ui/slint/issues/2294)), so the mirroring comes from OpenDAP's `.slint` generator. Tokens are written in logical terms (start, end), never left and right.

## 10. Spacing, radii, borders and elevation

### 10.1 Spacing

A 4 px base: `space.1` 4, `space.2` 8, `space.3` 12, `space.4` 16, `space.5` 20, `space.6` 24, `space.8` 32, `space.10` 40, `space.12` 48 (px). Adapt density to the display, but never compress important controls to fit more content. Layouts leave room for text expansion between languages (DS-006).

### 10.2 Radii

`radius.control` 10 px · `radius.card` 16 px · `radius.panel` 20 px · `radius.device` 28 px · `radius.pill` 999 px · `radius.round` 50 % · `radius.group-outer` (outer ends of a button group, = `radius.pill`; §15.1). These are digital tokens; physical radii are decided by industrial design and manufacturing.

### 10.3 Borders

Low-contrast graphite borders; brighter borders for active or focused elements; not every component outlined; orange borders are not a general emphasis mechanism.

### 10.4 Elevation

Prefer tonal contrast between surfaces (`graphite.950` → `900` → `850` → `800`) over large shadows. A raised surface differs from its background by its treatment, not by floating dramatically above it.

## 11. Motion

Motion is deliberate, controlled and physically motivated.

### 11.1 Principles

Short transitions for direct interactions; smooth, restrained easing; no bounce; no perpetual decorative movement; no sudden full-screen flashes; no animation that delays access to primary controls. Every animation runs at the display's full frame rate (T1-056).

| Token | Value | Use |
|---|---|---|
| `motion.duration.fast` | 120 ms | Press states, small toggles |
| `motion.duration.standard` | 200 ms | Most transitions |
| `motion.duration.slow` | 320 ms | Large surface changes |
| `motion.easing.standard` | `cubic-bezier(0.2, 0, 0, 1)` | Default easing |

An animation never stands between an input and its effect: the state changes at once, and the animation shows it.

### 11.2 Plasma motion

When used, plasma movement suggests energy flow, not a looping screensaver: slow movement of the core, slight changes in the outer gradient, audio-reactive amplitude or intensity, a brief activation when playback starts, gentle settling when a process ends. No rapidly cycling colours and no high-frequency brightness changes.

### 11.3 Thermal motion

Extremely subtle and slow; atmospheric detail, never a source of information.

### 11.4 Reduced motion

OpenDAP OS has a system **reduce motion** setting, and web surfaces honour `prefers-reduced-motion` (DS-012). Reduced motion replaces animation with a static state; it never removes the feedback the animation carried.

## 12. Lighting and effects

### 12.1 Lighting model

Soft diffuse light; localised luminous sources; subtle edge highlights; controlled reflections; deep but readable shadows; occasional plasma bloom. Lighting supports material perception and hierarchy.

### 12.2 Glow

Only on elements that are actually luminous, or in selected energetic visualisations. Never on every icon, border, title or control.

### 12.3 Transparency

Translucency for light guides, overlays and selected atmospheric layers. Text and controls sit on surfaces opaque enough to stay legible.

### 12.4 Effects budget and reduced-effects mode

Every effect costs attention, rendering time and battery. Before adding one, answer:

1. What does it communicate?
2. Why is a static colour or shape not enough?
3. Can it be reduced or disabled?
4. Does it stay within the frame and power budgets on the target hardware (§17)?
5. Does it interfere with reading?

If any answer is unclear, remove the effect.

OpenDAP OS has a **reduced-effects** mode that replaces plasma and thermal effects with their static or flat equivalents (DS-009). The interface is complete and correct with every effect off.

## 13. Accessibility

Accessibility is part of engineering quality (DS-010):

- Text meets WCAG 2 AA contrast: 4.5:1 for normal text, 3:1 for large text and for the visual cues needed to identify a control (§3.4).
- Critical state is never shown by colour alone: a label, an icon, a shape or a pattern carries it too.
- Active, disabled, loading and error states are distinguishable.
- Reduced motion and reduced effects are supported (§11.4, §12.4).
- Text stays legible at the smallest supported size on the real panel.
- Every control has a clear accessible name.
- Primary actions never need fine motor precision; physical controls have spacing and tactile distinction.
- Plasma effects never cover important information.
- Keyboard and non-touch input reach every control (SYS-021 to SYS-026; non-touch faceplates send HID navigation).

The display and physical controls are also evaluated under realistic light and viewing angles.

## 14. Design tokens

The tokens live in one platform-neutral file, [`tokens/opendap.tokens.json`](../../tokens/opendap.tokens.json), in the W3C Design Tokens Community Group format ([2025.10](https://www.designtokens.org/tr/2025.10/format/)). Slint globals for the device and CSS custom properties for web, documentation and OpenDAP Desktop are generated from it; neither is edited by hand (§18.1).

Groups: `color` (primitives), `semantic` (surfaces, text, brand, state, border, focus), `size` (strokes such as the button-group divider), `plasma` (spectrum and reference gradients, kept apart so it can be disabled as one group), `font`, `space`, `radius`, `motion`, `effect`.

The CSS names generated from the semantic tokens follow the draft's names, for example:

```css
:root {
  --color-bg: #111315;
  --color-surface: #191c1f;
  --color-surface-raised: #202428;
  --color-surface-active: #292e33;
  --color-text: #f5f6f4;
  --color-text-secondary: #c6cbd0;
  --color-text-muted: #939ba3;
  --color-brand: #ff6a2a;
  --color-brand-hover: #ff874d;
  --color-brand-pressed: #c84719;
  --color-border: #343a40;
  --color-border-strong: #515a63;
  --color-focus: #ff874d;
  --font-ui: "IBM Plex Sans", system-ui, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, monospace;
  --duration-standard: 200ms;
  --ease-standard: cubic-bezier(0.2, 0, 0, 1);
}
```

No colour, radius or timing is written outside the tokens without a recorded reason.

## 15. Components

- **Primary action:** round or near-round; the only orange emphasis on the screen; dark foreground on the orange fill (§3.4); a clearly visible pressed state (`brand-pressed`); no persistent glow; an accessible name and state.
- **Secondary action:** graphite surface; neutral border or tonal separation; white label or icon; orange only for selected or active states.
- **Button groups and segmented controls:** see §15.1.
- **Playback controls:** play and pause immediately distinguishable; skip controls subordinate to the primary action; volume easy to reach; the playback state never shown by animation alone; output and format settings reachable without cluttering the playback screen. Transport controls do not mirror in right-to-left layouts (§9.5).
- **Status indicators:** stable semantic colours with a label, icon or other non-colour cue; animated luminous indicators only for active processing; no permanent decorative blinking. Where the screen shows the same state as the status LED, it uses the same colour family (§18.4).
- **Panels and cards:** graphite tonal surfaces; consistent radii; minimal borders; clear internal spacing; no deep nesting; no plasma background on ordinary cards.
- **Diagnostics and technical information:** IBM Plex Mono for values that need fixed-width alignment; advanced information on demand; expert use supported without turning every screen into a diagnostic dashboard. Under "100 % of the hardware" (T1-045), everything the hardware does is reachable; the hierarchy decides where, not whether.
- **On-screen keyboard:** follows these tokens and the keyboard sizes in §8.3; its layout mirrors for right-to-left languages.

### 15.1 Button groups: the segmented capsule

Button groups, physical and digital, use one pattern (DS-013): **one capsule split into segments**. The outer ends are rounded; the inner edges at each split are flat; every segment is its own button; splits are marked by a consistent gap or divider. The T1's Volume + / Volume − pair is the reference instance (§7).

On screen this covers button groups and segmented controls, for example gain, filter, output or mode selectors:

| Part | Rule | Token |
|---|---|---|
| Outer ends | Full capsule radius on the first and last segment's outer side; square inner corners | `radius.group-outer` (= `radius.pill`) |
| Splits | One divider style per group, gap or line, never mixed | `size.group-divider` (1 px, proposal) with `semantic.border.group-divider`, or `space.group-gap` (2 px, proposal) |
| Segments | Equal height; equal width unless the labels are of very different lengths; each meets the touch minimum (§8.3) | — |
| Selected segment | Tonal fill (`surface-active`) with a non-colour cue (weight, icon or indicator); orange only when the group is the screen's primary action | — |
| Right-to-left | Segment order mirrors with the layout, except groups that stand for a physical order (volume, transport) | — |
| Accessibility | Each segment has its own accessible name; a single-choice group is announced as one group with a selected item | — |

A group of two to five segments fits the 320 px width at the touch minimum; more options go to a list or a picker.

## 16. Product renders

Renders, previews and concept art follow the same language as the interface. The rules for the physical product are in the [case industrial-design spec](https://github.com/opendap-project/case/blob/main/docs/specs/industrial-design.md) (§ Rendering rules); renders are built from components' `export/` and the [Blender library](https://github.com/opendap-project/blender-lib). In short: matte synthetic enclosure by default; soft, controlled studio light; orange only on the Action button and sparingly elsewhere; plasma confined to display content or a conceptual visualisation; accurate proportions; the hardware stays credible as a manufacturable object.

## 17. Performance

The interface runs at the display's refresh rate under any load (60 fps; T1-056, SYS-036; [experience budgets](https://github.com/opendap-project/t1/blob/main/docs/specs/experience-budgets.md)), and nothing visual may take time from the audio path.

- Static gradients are the default; animated effects are the exception and isolated from frequently redrawn content.
- Gradients drawn by the renderer before raster images, where they fit; pre-rendered textures for effects the renderer cannot draw cheaply.
- No stacked blur filters and no large displacement regions.
- No core function depends on GPU-intensive rendering; the interface is complete with every effect off.
- Every effect is measured on the target hardware (frame time and energy) before it ships; an effect that drops a frame, or moves the playback autonomy towards its warning value, is removed or reduced.
- Visual fidelity never costs responsiveness, legibility or battery life.

## 18. Alignment with OpenDAP requirements

How this design direction fits the decisions already taken.

### 18.1 Rendering: Slint on the device, tokens as the single source

- The device UI is rendered by **Slint** ([system ADR 0006](https://github.com/opendap-project/system/blob/main/docs/adr/0006-slint-as-host-renderer.md)), not by a browser. The CSS in this document is a **reference recipe** for web, documentation and OpenDAP Desktop, and a visual description for the device.
- Tokens are canonical in `tokens/opendap.tokens.json` and generated into Slint globals and CSS custom properties (DS-008). The generator is not written yet.
- Slint 1.18.1 draws linear, conic and **circular** radial gradients only ("only circular gradients are supported", [Slint reference](https://github.com/slint-ui/slint/blob/v1.18.1/docs/astro/src/content/docs/reference/property-types/colors-and-brushes.mdx)), and has no general blur or displacement filter. On the device, the elliptical plasma field is a circular gradient stretched by its element or a pre-rendered image, and blur, glow and thermal displacement are pre-rendered textures or an application-rendered GPU texture. Which of these meets the budgets is **UNVERIFIED** until measured.

### 18.2 The display: 320 × 480 at about 166 ppi

- The touch faceplate's panel is 3.5", 320 × 480 portrait, active area 48.96 × 73.44 mm, about 166 ppi ([faceplate-touch ADR 0001](https://github.com/opendap-project/faceplate-touch/blob/main/docs/adr/0001-focus-lcds-e35gh-display.md); [i18n research](https://github.com/opendap-project/system/blob/main/docs/research/2026-10-text-input-and-i18n.md) §6). One pixel is 0.153 mm, so 44 px ≈ 6.7 mm.
- Token pixels are panel pixels on the T1: one logical pixel per physical pixel (a scale factor of 1; **proposal**). On Desktop and the web, CSS pixels follow the host's scaling, so the same token is physically larger there.
- Minimum targets are defined in millimetres (§8.3). The on-screen keyboard's 32 px keys (4.9 mm) are the documented exception, compensated by 46 px rows, long-press alternates and hit-target correction.
- Faceplates are interchangeable: other panels convert the same millimetre minimums at their own density.

### 18.3 Fluidity, effects and battery

- 60 fps under any load is a must (T1-056); effects never drop frames. Static by default; plasma and thermal only on the screens listed in §4.3; a reduced-effects mode (§12.4).
- The UI never waits on work (SYS-036) and an animation never delays an action's effect (T1-057, SYS-037).
- Effects count against the power budget (playback autonomy > 12 h ideal); an always-on animated effect on the playback screen needs a measurement before it is allowed.

### 18.4 Semantic colours and the status LED

The status LED follows IEC 60073 ([controls and status LED spec](https://github.com/opendap-project/t1/blob/main/docs/specs/controls-and-status-led.md)). The on-screen semantic colours use the same families for the same meanings: red for fault or danger (`error`), amber for warning (`warning`), green for normal (`success`), blue for a state that needs the user's action or patience (`info`, as for pairing, recovery or an update in progress), and neutral white for neutral information. `processing` (violet) has no LED counterpart; see §20. The screen never contradicts the LED.

### 18.5 Languages and scripts

Five launch languages, including Arabic, so right-to-left and four scripts (Latin, Han, Devanagari, Arabic) are launch requirements (SYS-025, SYS-028, DS-006, DS-011). Typography in §9.4 and §9.5; templates have no hard-coded text and leave room for expansion.

### 18.6 Themes

One official theme, defined by these tokens (DS-007, SYS-030). A community theme is a replacement token set (and template layouts), with no code. Themes may change values, never the meaning of semantic colours, the contrast minimums, the target sizes or the reduced-motion and reduced-effects behaviour.

### 18.7 What this supersedes

DS-002 to DS-005 (withdrawn requirements adopted from earlier experiments: Plex with a Serif role, a warm black and ivory palette with per-activity accents, a layout anatomy and a 480 × 800 reference screen) are superseded by this spec.

## 19. Review checklist

### Identity and materials

- [ ] Engineered but approachable; nothing aggressive or gaming-like.
- [ ] Graphite, white and orange remain the vocabulary; orange stays at 2–5 %.
- [ ] Synthetic materials look believable; every detail has a function or an identity purpose.

### Ergonomics

- [ ] The main action is easy to find and operate; the round, concave Action button keeps its geometry and the accent.
- [ ] Volume + / − are two half-capsules of one split capsule; Main is the ribbed capsule; physical controls are distinguishable by touch.
- [ ] Every button group, physical or digital, uses the segmented capsule (§15.1).
- [ ] Touch targets meet the millimetre minimums on the real panel.

### Plasma and thermal

- [ ] Plasma appears only on the screens §4.3 allows; it has a luminous core and controlled transitions; violet and cyan stay secondary.
- [ ] Glow is localised; thermal refraction is subtle and never touches legibility.
- [ ] Effects are static or restrained by default; reduced-motion and reduced-effects alternatives exist and were tested.

### Interface

- [ ] Primary information is understandable at a glance; routine screens are quiet.
- [ ] Every control gives immediate feedback; the screen matches the device state.
- [ ] Contrast meets §3.4; colour is never the only cue.
- [ ] Layout works in all five launch languages, including right-to-left, with no clipped text.

### Engineering

- [ ] Measured at 60 fps on the target hardware under background load; energy measured for any animated effect.
- [ ] Every value comes from the tokens.
- [ ] The interface is complete with all effects off.
- [ ] Real hardware dimensions and the real display were used.

## 20. Decisions and open questions

Decided on 2026-10-22 (under the maintainers' delegation):

- **Processing colour.** Updates and other long system operations use `info` blue on screen, matching the status LED's blue breathing (T1 controls spec). Violet `processing` is reserved for computational visualisations (for example DSP or analysis views), never for system state.
- **Greys.** The token list is canonical: `text-muted` `#939BA3` for muted text (passes AA) and `border` `#343A40` for borders. `graphite.500` `#737C85` is kept only for icons and large text, and `graphite.700` `#3A4148` for separators.
- **Button groups.** Divider 1 px and gap 2 px are the starting values, confirmed on the prototype panel.

Open, to be set on the prototype:

- **Orange validation.** The brand orange against the physical Action button part, measured under the same light.
- **Type scale.** Sizes and line heights for the 166 ppi panel.
- **Primary target size.** The larger size for primary and frequent actions (§8.3).
- **Fonts.** The UNVERIFIED items in §9.4, and Plex Sans SC versus a Noto CJK subset for storage.

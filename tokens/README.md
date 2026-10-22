# Tokens

Design tokens of the official design system: every colour, font, spacing, radius, timing and effect value the UI uses. The rules for using them are in the [design system spec](../docs/specs/design-system.md).

## Files

| File | Contents |
|---|---|
| [`opendap.tokens.json`](opendap.tokens.json) | The **official theme**, in the W3C Design Tokens Community Group format ([2025.10](https://www.designtokens.org/tr/2025.10/format/)). Status: Draft; values are starting points to validate on the prototype display. |

## Structure

| Group | Contents |
|---|---|
| `color` | Primitive palette: graphite, white, orange. Components do not use it directly. |
| `semantic` | Roles: background, surfaces, text, brand, state (success, warning, error, info, processing), borders, focus. Most are aliases of primitives. |
| `font` | Interface and technical families (IBM Plex with its script companions) and weights. |
| `space`, `size`, `radius` | Spacing scale (4 px base), strokes and minimum target, digital radii including the button-group outer radius. |
| `motion` | Durations and easing. |
| `effect` | Shadow and brand glow. |
| `plasma` | The plasma and thermal special mode, kept as one group so the reduced-effects mode can turn it off as a whole. |

Units: on the T1, `px` is one panel pixel (about 0.153 mm at 166 ppi). Values the format cannot express (elliptical radial gradients, layer blur and inset) are in `$extensions` under `org.opendap.*`.

## Generated outputs

The JSON file is the single source. Two outputs are generated from it and never edited by hand:

- **Slint** globals for OpenDAP OS on the device ([system ADR 0006](https://github.com/opendap-project/system/blob/main/docs/adr/0006-slint-as-host-renderer.md)).
- **CSS** custom properties for the web, documentation and OpenDAP Desktop (`--color-bg`, `--space-4`, `--radius-control`…, as listed in the spec).

The generator is **not written yet**, and its tooling is not chosen.

## Themes

There is one official theme (DS-007, SYS-030). A community theme is another token file with the same structure that replaces values, without code. A theme may change values, not the meaning of semantic colours, the contrast minimums, the target sizes or the reduced-motion and reduced-effects behaviour.

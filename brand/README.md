# Brand mark (Draft)

The OpenDAP mark: a lying rhomboid outline with horizontal top and bottom edges and sides rising at 60°, its two acute corners cut, a thick stroke that grows inward (no fill), and a vertical centre line of the same weight. The outline reads as the **O** and, with the line, the **D** of OpenDAP.

## Construction on a 1:1 grid

Grid unit u; major grid every 7 u. Every value is either a grid integer or a simple ratio of the stroke (28 u).

| Element | Value | Why |
|---|---|---|
| Proportions | Stroke : counter : stroke = 4 : 7 : 4 (28 : 49 : 28 u); height 105 u | The stroke is 4/15 of the height: heavy, with open counters |
| Overall | 180 u × 105 u = 12 : 7 | Follows from the triangular counters |
| Angles | 0°, 90° and 60° | Industrial (set-square) angles. The sides rise 7 u per 4 u across (60.26°), the grid-exact approximation of 60° (within 0.3°) |
| 60° sides | 32 u measured horizontally = 8/7 of the stroke (27.8 u perpendicular) | Optically equal to the base stroke, and it keeps the inner contour on the grid |
| Centre line | x = 76–104 u, exactly vertical, centred on the 180 u width | Placed by the triangular counters: it meets each side's inner contour at the counter's tip |
| Counters | Triangles bounded by a horizontal stroke, a 60° side and the centre line, chamfered into six sides | The O and the D read through the outline and the line |
| Counter chamfers | Faces of 8 u (2/7 of the stroke). The 60° and 90° corners are cut symmetrically. The acute corner is cut by a horizontal face, parallel to the strokes, half a stroke (14 u) from the corner | The horizontal cut gives the centre line a square end, so it reads as vertical among the diagonals; 8 u is the face that puts that cut exactly half a stroke from the corner |
| Acute outer corners | Cut vertically at x = 16 u (4/7 of the stroke), the side's grid point one stroke above the corner; each cut is 28 u long | One stroke long; echoes the centre line |
| Outer chamfers | Faces of 16 u (twice the counters', equal to the cut offset) where the outline meets a horizontal edge; none where a vertical cut meets a 60° side | One family of chamfers in a 2 : 1 ratio; a chamfer next to the rising sides would blur them |
| Corner rounding | Every corner, outer and inner, by a true circular arc of 2 u (1/14 of the stroke) | The same small curve at every corner, whatever its angle |

The outer contour and the counters' horizontal and vertical edges fall on the grid; chamfer points on the 60° sides are set by the face lengths.

## Files

- `mark.py`: generates the mark from this construction; `--grid` draws the construction drawing. `STROKE`, `COUNTER` and `CHAMFER` set the construction; the rest is derived from them.
- `opendap-mark.svg`: the mark, light on transparent.
- `opendap-mark-accent.svg`: the mark in the brand orange.
- `opendap-mark-construction.svg`: on the grid, with the construction lines.

Status: Draft. Usage rules (clear space, minimum size, colours) follow once the shape is final. See the [design system](../docs/specs/design-system.md), §2.

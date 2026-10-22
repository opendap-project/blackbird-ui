# Brand mark (Draft)

The OpenDAP mark: a lying rhomboid outline with horizontal top and bottom edges and sides rising at 60°, its two acute corners cut, a thick stroke that grows inward (no fill), and a vertical centre line of the same weight. The outline reads as the **O** and, with the line, the **D** of OpenDAP.

## Construction on a 1:1 grid

| Element | Value (grid units, u) | Why |
|---|---|---|
| Angles | 0°, 90° and 60° | Industrial (set-square) angles. The sides rise 7 u per 4 u across (60.26°), the grid-exact approximation of 60° (within 0.3°) |
| Height | 91 u = 28 + 35 + 28 | Stroke at 30.8 % of the height: heavy, with open counters |
| Horizontal strokes, centre line | 28 u | The base stroke |
| 60° sides | 32 u measured horizontally (27.8 u perpendicular) | Optically equal to the base stroke, and it keeps the inner contour on the grid |
| Counters | Triangles bounded by a horizontal stroke, a 60° side and the centre line, which meets the side's inner contour at the counter's tip | The centre line is placed by this condition |
| Counter chamfers | Every corner of each counter cut so that every cut face is 4 u long: two six-sided counters. A corner of angle t moves 4 / (2 sin(t/2)) u along each edge | Equal cut faces read as one deliberate detail; it repeats the cut corners outside |
| Overall | 164 u × 91 u, about 1.8:1 | Follows from the triangular counters |
| Centre line | x = 68–96 u | The middle of the 164 u width |
| Acute outer corners | Cut vertically at the side's grid point one stroke above the corner, 28 u long | The cut is one stroke and echoes the centre line |
| Outer chamfers | Every corner of the outline chamfered with the same 4 u cut face as the counters | One chamfer length across the whole mark |
| Corner rounding | Outer chamfers only, 2 u (half a cut face); counters sharp | Soft outside for the hand and the eye, precise inside |

Every point of the outer and inner contours falls on the grid.

## Files

- `mark.py`: generates the mark from this construction; `--grid` draws the construction drawing. `STROKE` and `COUNTER` (multiples of 7 u) set the weight, and `CHAMFER` sets the length of every counter cut face.
- `opendap-mark.svg`: the mark, light on transparent.
- `opendap-mark-accent.svg`: the mark in the brand orange.
- `opendap-mark-construction.svg`: on the grid, with the construction lines.

Status: Draft. Usage rules (clear space, minimum size, colours) follow once the shape is final. See the [design system](../docs/specs/design-system.md), §2.

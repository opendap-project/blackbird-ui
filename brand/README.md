# Brand mark (Draft)

The OpenDAP mark: a lying rhomboid outline with horizontal top and bottom edges and sides rising at 60°, its two acute corners cut, a thick stroke that grows inward (no fill), and a vertical centre line of the same weight. The outline reads as the **O** and, with the line, the **D** of OpenDAP.

## Construction on a 1:1 grid

| Element | Value (grid units, u) | Why |
|---|---|---|
| Angles | 0°, 90° and 60° | Industrial (set-square) angles. The sides rise 7 u per 4 u across (60.26°), the grid-exact approximation of 60° (within 0.3°); 60° rather than 45° keeps the mark compact |
| Height | 21 u = 7 + 7 + 7 | The stroke is one third of the height |
| Horizontal strokes, centre line | 7 u | The base stroke: heavy, for presence at small sizes |
| 60° sides | 8 u measured horizontally (6.95 u perpendicular) | Optically equal to the base stroke, and it keeps the inner contour on the grid |
| Horizontal edges | 33 u | Each counter narrows to 3 u at its tip and widens to 7 u (one stroke) at its base |
| Overall | 45 u × 21 u, about 2.1:1 | |
| Centre line | x = 19–26 u | The middle of the 45 u width |
| Acute corners | Cut vertically at the first grid point of the side, 7 u long | The cut is exactly one stroke and echoes the centre line |
| Corner rounding | 0.5 u on every corner, outer and inner | Subtle, almost invisible |

Every point of the outer and inner contours falls on the grid.

## Files

- `mark.py`: generates the mark from this construction (`--grid` draws the construction drawing).
- `opendap-mark.svg`: the mark, light on transparent. `opendap-mark-accent.svg`: in the brand orange.
- `opendap-mark-construction.svg`: on the grid, with the construction lines.

Status: Draft. Usage rules (clear space, minimum size, colours) follow once the shape is final. See the [design system](../docs/specs/design-system.md), §2.

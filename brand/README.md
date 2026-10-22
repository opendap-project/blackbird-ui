# Brand mark (Draft)

The OpenDAP mark: a lying rhomboid outline with horizontal top and bottom edges and sides rising at 60°, its two acute corners cut, a thick stroke that grows inward (no fill), and a vertical centre line of the same weight. The outline reads as the **O** and, with the line, the **D** of OpenDAP.

## Construction on a 1:1 grid

| Element | Value (grid units, u) | Why |
|---|---|---|
| Angles | 0°, 90° and 60° | Industrial (set-square) angles. The sides rise 7 u per 4 u across (60.26°), the grid-exact approximation of 60° (within 0.3°); 60° rather than 45° keeps the mark compact |
| Height | 21 u = 7 + 7 + 7 | The stroke is one third of the height |
| Horizontal strokes, centre line | 7 u | The base stroke: heavy, for presence at small sizes |
| 60° sides | 8 u measured horizontally (6.95 u perpendicular) | Optically equal to the base stroke, and it keeps the inner contour on the grid |
| Counters | Triangles: each is bounded by a horizontal stroke, a 60° side and the centre line, which meets the side's inner contour at the counter's tip | The centre line is placed by this condition, not by a free choice |
| Counter chamfer | 45°, 1 u, at the right-angle corner where the stroke meets the centre line | An inner chamfer like a gusset in a structural joint; it repeats the cut corners outside |
| Horizontal edges, overall | 27 u; 39 u × 21 u, about 1.86:1 | Follow from the triangular counters |
| Centre line | x = 16–23 u | The middle of the 39 u width |
| Acute corners | Cut vertically at the first grid point of the side, 7 u long | The cut is exactly one stroke and echoes the centre line |
| Corner rounding | 0.5 u on every corner, outer and inner | Subtle, almost invisible |

Every point of the outer and inner contours falls on the grid.

## Files

- `mark.py`: generates the mark from this construction (`--grid` draws the construction drawing). `CHAMFER` sets the inner chamfer (1 u; 2 u narrows the counters to slots). `COUNTER` sets the counter height in multiples of 7 u (7 u: stroke at one third of the height; 14 u: a lighter weight); every other dimension follows.
- `opendap-mark.svg`: the mark, light on transparent. `opendap-mark-accent.svg`: in the brand orange.
- `opendap-mark-construction.svg`: on the grid, with the construction lines.

Status: Draft. Usage rules (clear space, minimum size, colours) follow once the shape is final. See the [design system](../docs/specs/design-system.md), §2.

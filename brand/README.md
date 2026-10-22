# Brand mark (Draft)

The OpenDAP mark: a lying rhomboid outline with horizontal top and bottom edges and sides rising at 45°, its two acute corners cut, a thick stroke that grows inward (no fill), and a vertical centre line of the same weight. The outline reads as the **O** and, with the line, the **D** of OpenDAP.

## Construction on a 1:1 grid

| Element | Value (grid units, u) | Why |
|---|---|---|
| Angles | 0°, 90°, 45° only | Industrial (set-square) angles; 45° is the diagonal of the grid square |
| Height | 24 u = 4 + 16 + 4 | Two strokes and the counter |
| Horizontal strokes, centre line | 4 u | The base stroke |
| 45° sides | 6 u measured horizontally (4.24 u perpendicular) | About 6 % heavier than the base stroke: the usual optical compensation for diagonals, and it keeps the inner contour on the grid |
| Horizontal edges | 40 u | Each counter then narrows to exactly one stroke (4 u) at its tip and widens to 20 u at its base |
| Overall | 64 u × 24 u | The 45° sides add the height (24 u) to the edge length |
| Centre line | x = 30–34 u | The middle of the 64 u width |
| Acute corners | Cut vertically, 4 u long, at the first grid point of the side | The cut faces repeat the stroke and echo the centre line |
| Corner rounding | 0.5 u on every corner, outer and inner | Subtle, almost invisible |

Every point of the outer and inner contours falls on the grid.

## Files

- `mark.py`: generates the mark from this construction (`--grid` draws the construction drawing).
- `opendap-mark.svg`: the mark, light on transparent. `opendap-mark-accent.svg`: in the brand orange.
- `opendap-mark-construction.svg`: on the grid, with the construction lines.

Status: Draft. Usage rules (clear space, minimum size, colours) follow once the shape is final. See the [design system](../docs/specs/design-system.md), §2.

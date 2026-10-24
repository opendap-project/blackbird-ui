# UI model

- **Status:** Draft
- **Decided by:** Claude, under the maintainers' delegation (they asked to analyse scope, nesting, inheritance, override and propagation, the layout model, scrolling and motion, from the models that proved themselves, for the best developer and user experience); for their review
- **Builds on:** [ADR 0002](../adr/0002-slint-components-with-a-blueprint-mode.md) (components, blueprint mode), [ADR 0003](../adr/0003-screen-states.md) (screen states), the [design system](design-system.md), system [input events](https://github.com/opendap-project/system/blob/main/docs/specs/input-events.md), system ADR 0006 (Slint)

How OpenDAP's interface is put together, for whoever writes an activity or a component. Each section names the models that proved themselves, what Slint already gives (1.18), and what Blackbird UI adds. Nothing here replaces a standard Slint already implements; Blackbird UI adds only what Slint leaves out.

## 1. Scope and nesting

**Proven:** a tree of components composed, not inherited (React, SwiftUI, Compose, Flutter); children passed in as content (slots, `children`); each component owns its private state; one root per screen.

- **Slint gives:** components, `@children` for content, `inherits` for one base, private properties, `in`/`out`/`in-out` for the public surface.
- **Rules:**
  - **Composition over inheritance.** A component wraps others and takes content through `@children`; `inherits` only from a primitive (`Rectangle`, a layout, `Text`), never to extend another Blackbird UI component's behaviour.
  - **The public surface is the contract.** `in` for what the caller decides, `out` for what the component reports, `in-out` only for a value both sides own (a slider's `value`); callbacks for what happened. Nothing else is reached from outside.
  - **One screen, one root:** `Screen`, then its header, its scroll area, its content. Activities nest screens by navigation, never by drawing one screen inside another.

## 2. Inheritance of context

**Proven:** values that flow down the tree without being passed at every level and that the nearest provider overrides: CSS inherited properties (`color`, `direction`), React context, SwiftUI's environment, Compose's `CompositionLocal`, Flutter's `InheritedWidget`.

- **Slint gives:** globals (one value for the whole window), property bindings.
- **Blackbird UI's context**, as globals read by every component:

  | Context | Holds | Who sets it |
  |---|---|---|
  | `Tokens` | The theme's values (DS-007) | The theme (generated) |
  | `Blueprint` | The debug UI mode (SYS-070) | The application, from the system's flag |
  | `Motion` (to add) | Reduce motion (DS-012), reduced effects (DS-009) | The application, from the system's settings |
  | `Layout` (to add) | The direction (left-to-right or right-to-left, §9.5), the layout class (§18.2), the design-pixel `unit` | The application, from the description and the language |
  | `FocusReveal` | Where the focused element is | The components |

- **Cascading states.** `enabled` cascades down as HTML's `fieldset disabled` and SwiftUI's `.disabled()`: a disabled group disables what it holds, and a child cannot re-enable itself inside it. The same for a reason (ADR 0003): the group's reason is shown once, not on every child.
- **Window-wide, not subtree.** Slint's globals are per window, so a context that must differ inside one subtree (a right-to-left island, a nested blueprint) is passed as an `in` property by the components that need it. This is the one gap against the environment model; it is rarely needed on a 3.5" screen, and it is named here so no one fakes it.

## 3. Override

**Proven:** layered tokens (primitive → semantic → component; the W3C Design Tokens format), theming by replacing a layer, local overrides at the call site, variants instead of ad hoc styling.

- **Order, weakest first:** the theme's primitives → its semantic tokens (`surface-*`, `text-*`, `state-*`) → a component's defaults → its variant (`PrimaryButton` round or capsule by content) → the call site's `in` properties. A community theme replaces the first two layers only (DS-007), and every component follows.
- **What a call site may override:** content, size where the layout needs it, its state and its callbacks. Not colours, radii or type: those come from the semantic layer, so a theme and the blueprint mode reach every element. A need that the tokens cannot express becomes a token or a variant, not a local value.

## 4. Data and propagation

**Proven:** data down, events up (unidirectional flow: Elm, React, Redux, SwiftUI's single source of truth); state lifted to the nearest owner; two-way binding only for a value the user edits in a control.

- **Slint gives:** bindings (`<=>` two-way), callbacks, `changed` handlers.
- **Rules:**
  - **State has one owner.** The activity's model (in Rust, the application core of the crate architecture) owns what the screen shows; components hold only what is theirs (pressed, focused, an animation's progress).
  - **Events go up as callbacks** with the domain payload (input events §6); the owner changes its state; the screen follows by binding. A component never reaches into another.
  - **`<=>` only for a control's value** (a slider, a toggle), and only between the control and its owner.
  - **Input propagation** is the input events' model: the system first, then capture, target and bubble, with directives and implicit defaults (input events §4, §5).
  - **Hardware in flight:** a value sent to the hardware is fire-and-forget, the latest winning; a physical state (a card in its socket) waits for the hardware's confirmation before the control says it changed.

## 5. Interaction states

**Proven:** one fixed set of states, layered in one order (Material's state layers; CSS's `:hover`, `:active`, `:focus-visible`, `:disabled`, `:checked`).

- **Slint gives:** `states [ … when … ]` with `in` and `out` transitions; `TouchArea.has-hover`, `pressed`; `FocusScope.has-focus`.
- **The set, in the order they combine:** disabled (dims everything; nothing else shows) → selected or checked → hovered (a pointer only) → focused (the ring, design system §8.4) → locked for adjustment (a slider) → pressed (live input). Each component uses Slint's `states` for them, so their transitions come from the motion tokens in one place.
- **Every state is visible without colour alone** (DS-010): weight, a ring, an icon, a fill, never a hue only.

## 6. Layout

**Proven:** constraints go down, sizes go up, the parent places (Flutter's and Compose's layout model); one-dimensional flex with gap, alignment and growth (CSS Flexbox, SwiftUI stacks, Compose `Row`/`Column` with weights); a two-dimensional grid for aligned tables (CSS Grid); logical directions (`start`/`end`, not left/right) for right-to-left; layout chosen by the space a component has (container queries), not by the device's name.

- **Slint gives:** `HorizontalLayout` and `VerticalLayout` (one dimension: `spacing`, `padding`, `alignment`, stretch factors, minimum, preferred and maximum sizes), `FlexboxLayout` (CSS Flexbox with wrapping), `GridLayout`; minimum, preferred and maximum sizes propagate up; elements without `x` and `y` are centred in their parent.
- **Rules:**
  - **Stacks for almost everything:** a vertical stack per screen, horizontal stacks for rows. `FlexboxLayout` only where items must wrap (chips, a cover grid that reflows); `GridLayout` only where columns must align (a readout table).
  - **Spacing is proximity** (design system §10.1, DS-017): a stack's spacing is a space token (`space-unit` within a unit, `space-group` within a group, `space-section` between groups); never a number at the call site.
  - **Side margins belong to groups,** so lists run the full width under them (§15.2).
  - **Logical directions:** `start` and `end` in every component's API; the `Layout` context mirrors them for right-to-left (§9.5); transport and physical-order groups do not mirror.
  - **By the space, not the device:** a component that changes shape does it by its own width (a container query), and the screen picks the layout class (§18.2); no component tests for "the T1".
  - **Explicit position only for overlays** (a badge, a focus ring, a toast); always set `x` and `y` there, since Slint centres what has none.

## 7. Scrolling

**Proven:** momentum with deceleration after a fling (iOS `decelerationRate`, Android `OverScroller`); an edge that answers when the content ends (iOS's rubber band, Android 12's stretch); scroll-snapping to items (CSS `scroll-snap`); nested scrolling that hands the motion to the parent at the end (CSS `overscroll-behavior`, Compose's nested scroll); the focused element kept in view; scroll indicators that show only while scrolling; scrolling to the top from the status bar (iOS).

- **Slint gives:** `Flickable` (panning, wheel and touchpad, deceleration after a flick, `content-x`/`content-y`, `flicked`); `ScrollView` adds scroll bars. No edge effect, no snapping, no nested hand-over.
- **Blackbird UI's `Scroll`** (to build on `Flickable`):
  - **Edge effect:** a stretch at the top and the bottom, not a rubber band that moves the content far past its end. The content stretches by at most 3 % along the scroll axis while the finger pulls past the edge, and settles back on release with a spring (`spring(0)`, critically damped: no overshoot). It says "this is the end" without making the screen wobble, which fits a restrained design (§2.2). With reduce motion, no stretch: a hairline at the edge, held 200 ms.
  - **Deceleration:** Slint's, kept.
  - **Snapping:** opt-in, to items (a cover grid, a picker), and to the start of a section after a fling.
  - **Nested:** an inner scroll hands the remaining motion to its parent at its end, horizontal inside vertical included (a row of covers inside a page).
  - **Focus kept in view:** `FocusReveal` (done), with the edge effect not triggered by focus moves.
  - **Indicator:** a 2 px bar at the end edge, shown while scrolling and 1 s after, for screens taller than two pages.
  - **To the top:** a tap on the status bar scrolls the screen on display to its top (iOS's convention).
  - **Buttons:** focus navigation scrolls (§8.4); there is no separate page-scroll binding.

## 8. Motion

**Proven:** durations and easing curves as tokens (Material, the design system's `motion.*`); springs for anything a hand moves, since they carry the gesture's velocity and can be interrupted (SwiftUI, Compose, UIKit dynamics); enter and exit transitions for what appears and disappears (SwiftUI transitions, Framer's presence); layout animation of position changes (FLIP); shared-element transitions between screens; reduce motion that keeps the information and drops the movement.

- **Slint gives:** `animate` on any property (duration, delay, easing), easing curves including `cubic-bezier`, `ease-out-bounce` and `spring(bounce)`; `states` transitions.
- **Rules:**
  - **Timed for what the system starts, springs for what a hand moves.** A screen change, a toast or a state change takes the motion tokens (`fast` 120 ms, `standard` 200 ms, `slow` 320 ms, the standard easing). A drag released, a sheet thrown or a knob let go settles with a critically damped spring from its velocity. `bounce` is never used for a routine screen (§2.2); `ease-out-bounce` is not used at all.
  - **Everything is interruptible:** a new input takes over from wherever the animation is, never waits for it to end.
  - **Enter and exit:** what appears fades and moves at most 8 dp toward its place; what leaves does the reverse, faster (`fast`).
  - **Navigation:** going deeper slides the new screen from the end edge; going back reverses it; the header's title cross-fades. A shared element (a cover to Now Playing) morphs between screens where both show it.
  - **Lists:** an inserted or removed line animates its height and the lines below move into place (layout animation), so nothing jumps.
  - **Reduce motion** (DS-012): durations become zero and springs settle at once; fades remain where they carry information, at `fast`.
  - **Budget:** 60 frames per second on the T1 (§17); only transforms and opacity animate on screens with many elements, never a layout pass per frame.

## 9. What Blackbird UI adds, in order

1. The `Motion` and `Layout` contexts (§2), read by every component.
2. `states` in every component for the interaction states (§5).
3. `Scroll`: edge stretch, snapping, nested hand-over, the indicator, to-the-top (§7).
4. Stack wrappers with spacing by proximity tokens (§6): `Stack`, `Row`, `Group`, so no screen writes a spacing number.
5. Enter, exit and navigation transitions (§8), and layout animation for lists.

Each one shows in the UI primitives activity (system SYS-071) and in the blueprint mode (ADR 0002).

## Open questions

- Subtree context (a right-to-left island, §2): needed only if a screen mixes directions; Slint's globals are per window.
- The edge stretch's amount (3 %) and the indicator's threshold (two pages) are proposals to try on the T1.

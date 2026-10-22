# UI components requirements

Requirements for the official UI components and design system of OpenDAP OS.

| ID | Requirement | Priority | Status |
|---|---|---|---|
| DS-001 | All OpenDAP OS UI shall follow the official design system. | must | Confirmed |
| DS-002 | Typography: IBM Plex (Sans for the interface, Serif italic for reading and notes, Mono for data). | should | Withdrawn |
| DS-003 | Color: warm black #0E0D0C and ivory #F3EFE7, with one accent per activity (Listen #F0A63C, Watch #7DB3E8, Read #A3C98F, Create #EE7E62, Day #6CC4B4, Advanced #B7A4F0). | should | Withdrawn |
| DS-004 | Layout anatomy: status bar, a strip of activities (the active one large, the others peeking) and a 60 px playback thread at the bottom, replacing tabs and icons. | should | Withdrawn |
| DS-005 | Reference screen: 480 × 800 portrait; some views landscape 800 × 480. | should | Withdrawn |
| DS-006 | Components and templates shall be i18n-first: no hard-coded text, room for text expansion, mirrored layouts for right-to-left languages, and script-aware typography (SYS-025). | must | Confirmed |
| DS-007 | The design system shall define one official theme, with its tokens and templates structured so community themes can replace them without code (SYS-030). | must | Confirmed |
| DS-008 | The [design system spec](../specs/design-system.md) shall be the reference for all OpenDAP OS UI, OpenDAP Desktop, documentation visuals and product renders; its tokens file is the single source of design values. | must | Confirmed |
| DS-009 | Plasma and thermal effects shall be a special visual mode, never used on routine screens (lists, settings, ordinary cards), and the UI shall offer a reduced-effects mode that replaces them with static or flat equivalents without losing information. | must | Confirmed |
| DS-010 | Text shall meet WCAG 2 AA contrast against its background in every theme, and no state shall be communicated by colour alone. | must | Confirmed |
| DS-011 | Typography shall define its roles (interface, technical values) and cover the scripts of every shipped language, starting with Latin, Han, Devanagari and Arabic (SYS-028), with right-to-left mirroring. | must | Confirmed |
| DS-012 | Motion shall respect the reduce-motion setting: animation is replaced by a static state, never by the loss of the feedback it carried. | must | Confirmed |
| DS-013 | Button groups, physical and digital, shall use the segmented-capsule pattern: one capsule split into segments with rounded outer ends and flat inner edges. | must | Confirmed |

## Context

- DS-002 to DS-005: Adopted from the earlier experiments on 2026-10-21 as **Draft**: consistent with the decisions already taken and with the product philosophy, pending the maintainers' confirmation. Part availability still has to be checked against the sourcing rule (T1-010).
- Withdrawn on 2026-10-21 after the [experiment review](https://github.com/opendap-project/t1/blob/main/docs/research/2026-10-experiment-review.md): DS-002, DS-003, DS-004, DS-005.
- DS-002 to DS-005 are superseded by the [design system spec](../specs/design-system.md) (2026-10-22), written from the maintainers' design direction: graphite, white and one orange accent; IBM Plex Sans and Mono with script companions; the 320 × 480 touch panel.
- DS-008 to DS-012 (2026-10-22): from the maintainers' design direction, reconciled with the decisions already taken (Slint renderer, 166 ppi panel, 60 fps budget, status LED colours, five launch languages). Draft until the maintainers confirm the wording.
- DS-013 (maintainers, 2026-10-22): the T1's Volume + / Volume − pair (T1-059) is the reference instance; on screen it covers button groups and segmented controls such as gain, filter, output or mode selectors.

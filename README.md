# Blackbird UI

Blackbird UI, the user interface of Blackbird OS: **Engineered Matter**, the OpenDAP design system, with its tokens, OpenDAP Icons, guidelines and components ([spec](docs/specs/design-system.md)), the templates the host renders, and the dynamic components contributed through the registry (including those from HATs).

## Layout

- `tokens/`: the token file and `generate.py`
- `export/`: generated outputs other repositories read (`slint/tokens.slint`, `css/tokens.css`)
- `fonts/`: IBM Plex, vendored (OFL-1.1)
- `icons/`
- `components/`
- `docs/`

## License

This repository follows the [REUSE](https://reuse.software) layout: license texts live in `LICENSES/` and `REUSE.toml` maps each path to its license.

- Default: **Mozilla Public License 2.0** (`MPL-2.0`)
- Markdown files: **Creative Commons Attribution-ShareAlike 4.0** (`CC-BY-SA-4.0`)
- `docs/`: **Creative Commons Attribution-ShareAlike 4.0** (`CC-BY-SA-4.0`)
- `fonts/`: IBM Plex under the **SIL Open Font License 1.1** (`OFL-1.1`), © IBM Corp.

Copyright © 2026 The OpenDAP Project.

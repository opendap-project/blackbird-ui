# Fonts

IBM Plex, the design system's type (design system §9), vendored so that the product host compiles it in and every build draws the same glyphs. The device does not rely on system fonts for its own text.

| File | Family | Source |
|---|---|---|
| `IBMPlexSans-Variable.ttf` | IBM Plex Sans, variable (`wdth`, `wght`) | [google/fonts `ofl/ibmplexsans`](https://github.com/google/fonts/tree/main/ofl/ibmplexsans) (`IBMPlexSans[wdth,wght].ttf`, version 3.201, upstream [googlefonts/plex](https://github.com/googlefonts/plex)) |
| `IBMPlexMono-Regular.ttf`, `IBMPlexMono-Medium.ttf` | IBM Plex Mono | [google/fonts `ofl/ibmplexmono`](https://github.com/google/fonts/tree/main/ofl/ibmplexmono) (upstream [googlefonts/plex](https://github.com/googlefonts/plex)) |

- **Licence:** SIL Open Font License 1.1 ([`LICENSES/OFL-1.1.txt`](../LICENSES/OFL-1.1.txt)), © 2017 IBM Corp., with Reserved Font Name "Plex"; upstream's licence file is kept as [`OFL.txt`](OFL.txt). The files are unmodified, as downloaded on 2026-10-23.
- **Not here yet:** the script companions (Arabic, Devanagari, SC) of §9.4. They come with right-to-left and CJK support.

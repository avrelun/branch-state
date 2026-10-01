# Frontend dependency and template provenance

The BRST-6 lockfile introduces the dependencies below. Package metadata, packaged license/notice files and the versioned generator licenses were inspected on October 1, 2026. The root MIT license covers project-owned code; dependency and template terms remain upstream terms. Generator notices are preserved in [frontend/THIRD_PARTY_NOTICES.md](../../frontend/THIRD_PARTY_NOTICES.md).

## Direct dependencies

Versions below are the installed/locked versions. Source links identify the upstream releases or exact npm metadata; package-owned license and notice files remain in the packages when installed.

| Dependency                                                         | Version          | License    | Use and source                                                                                                                                                                   |
| ------------------------------------------------------------------ | ---------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Angular common, compiler, core, forms, platform-browser and router | 22.2.1           | MIT        | Browser application; [Angular source](https://github.com/angular/angular/tree/22.2.1), Google LLC notice.                                                                        |
| RxJS                                                               | 7.8.2            | Apache-2.0 | Angular HTTP observables; [package](https://registry.npmjs.org/rxjs/7.8.2), `LICENSE.txt` includes Google, Netflix, Microsoft and contributor attribution.                       |
| tslib                                                              | 2.8.1            | 0BSD       | TypeScript runtime helpers; [package](https://registry.npmjs.org/tslib/2.8.1), Microsoft `LICENSE.txt` and `CopyrightNotice.txt`.                                                |
| Zod                                                                | 4.6.5            | MIT        | Validate API responses; [package](https://registry.npmjs.org/zod/4.6.5), Colin McDonnell notice.                                                                                 |
| Angular build, CLI, compiler-cli and language-service              | 22.2.1           | MIT        | Build, tests and editor tooling; [Angular CLI source](https://github.com/angular/angular-cli/tree/22.2.1), [Angular source](https://github.com/angular/angular/tree/22.2.1).     |
| Nx and @nx/angular, devkit, eslint, eslint-plugin, js and web      | 23.2.1           | MIT        | Scaffold, project boundaries and task execution; [source and license](https://github.com/nrwl/nx/tree/23.2.1), Narwhal Technologies Inc.                                         |
| Orval, including its Angular and Zod generators                    | 8.39.0           | MIT        | Generate client/validation code from the project-owned OpenAPI input; [source and license](https://github.com/orval-labs/orval/tree/v8.39.0), Victor Bury.                       |
| TypeScript                                                         | 6.0.3            | Apache-2.0 | Compiler; [package](https://registry.npmjs.org/typescript/6.0.3), Microsoft license and `ThirdPartyNoticeText.txt`.                                                              |
| Vitest                                                             | 4.1.11           | MIT        | Unit tests; [package](https://registry.npmjs.org/vitest/4.1.11).                                                                                                                 |
| jsdom                                                              | 27.4.0           | MIT        | Test DOM; [package](https://registry.npmjs.org/jsdom/27.4.0).                                                                                                                    |
| ESLint / @eslint/js                                                | 10.11.0 / 10.0.1 | MIT        | Lint configuration and execution; [ESLint](https://registry.npmjs.org/eslint/10.11.0), [@eslint/js](https://registry.npmjs.org/%40eslint%2Fjs/10.0.1).                           |
| angular-eslint / typescript-eslint                                 | 22.5.0 / 8.71.0  | MIT        | Angular and TypeScript lint rules; [angular-eslint](https://registry.npmjs.org/angular-eslint/22.5.0), [typescript-eslint](https://registry.npmjs.org/typescript-eslint/8.71.0). |
| Prettier / eslint-config-prettier                                  | 3.9.9 / 10.1.8   | MIT        | Formatting and lint compatibility; [Prettier](https://registry.npmjs.org/prettier/3.9.9), [eslint-config-prettier](https://registry.npmjs.org/eslint-config-prettier/10.1.8).    |
| @types/node                                                        | 26.6.3           | MIT        | Tool configuration types; [package](https://registry.npmjs.org/%40types%2Fnode/26.6.3).                                                                                          |

The production dependency closure has ten package/version records: the nine direct runtime packages above and `@standard-schema/spec` 1.1.0 (MIT, [package](https://registry.npmjs.org/%40standard-schema%2Fspec/1.1.0)). Development tools are not vendored into the repository.

## Transitive review

The application lockfile contains **857 package/version records**. `pnpm licenses list --json` inspected **725 installed records** across 642 package names; exact npm release metadata was read for the remaining **132 optional platform packages**. Those omitted packages declare MIT (122) or MPL-2.0 (10). The separate package-manager bootstrap document has 15 pnpm 12.8.1 records, all declaring MIT. This separates installed file inspection from metadata-only evidence for other platforms.

| License expression                   | Application package/version records |
| ------------------------------------ | ----------------------------------: |
| MIT                                  |                                 743 |
| ISC                                  |                                  35 |
| Apache-2.0                           |                                  26 |
| BSD-2-Clause                         |                                  19 |
| MPL-2.0                              |                                  12 |
| BSD-3-Clause                         |                                  10 |
| BlueOak-1.0.0                        |                                   3 |
| MIT-0                                |                                   2 |
| 0BSD, Python-2.0, CC-BY-4.0, CC0-1.0 |                              1 each |
| Apache-2.0 AND BSD-3-Clause          |                                   1 |
| MIT OR CC0-1.0                       |                                   1 |
| WTFPL OR MIT                         |                                   1 |

These transitive cases require attention when redistributing the tools or their data:

- **Lightning CSS 1.33.0 and its platform binaries:** MPL-2.0. It is build tooling; no Lightning CSS source or binary is copied into the page. Redistributing the tool itself requires retaining its license and meeting the MPL source requirements.
- **caniuse-lite 1.0.30001814:** CC-BY-4.0 browser data; retain its attribution and license when distributing that data. **mdn-data 2.27.1** declares CC0-1.0.
- **@bufbuild/protobuf 2.16.0:** Apache-2.0 **and** BSD-3-Clause, rather than a choice. The installed `dist/esm/clone.js` preserves the Buf Technologies Apache notice; `dist/esm/wire/varint.js` contains the full Google BSD notice. Its metadata does not provide a root license file.
- **argparse 2.0.1:** the packaged `LICENSE` contains the Python/PSF terms. **lru-cache 11.5.3** and **minimatch 10.2.5/10.2.6** use BlueOak-1.0.0. The installed permission texts were checked.
- **union 0.5.0:** pnpm labels its missing package metadata as `Unknown`; its included `LICENSE` is MIT, copyright 2010 Charlie Robbins and the Contributors. It is counted as MIT above from that file evidence.
- **Prettier 3.9.9**, **TypeScript 6.0.3**, **reflect-metadata 0.2.2** and **tslib 2.8.1** have additional bundled/copyright notices. Preserve their `THIRD-PARTY-NOTICES.md`, `ThirdPartyNoticeText.txt` and `CopyrightNotice.txt` files when redistributing those tools. TypeScript's bundled notice includes Unicode, W3C and WHATWG terms beyond its package-level Apache label.

Some published packages omit standalone license files. Their package declarations were checked; Nx and Orval generator terms were additionally read from their pinned upstream repositories and preserved with the generated source. This review does not independently enumerate every library embedded inside native tool binaries, and other platform package contents were not downloaded. Recheck the applicable packages and notices if distributing a toolchain or native binaries.

## Source and browser distributions

Nx's retained application templates and Orval's generated Angular/Zod code are attributed in the frontend notices. The OpenAPI document is project-owned. The page uses the five Gruvbox color values recorded in [branding notices](../branding/THIRD_PARTY_NOTICES.md#gruvbox-palette), with a system font stack and no bundled images, icons or font files. The generated favicon is omitted. For BRST-6, the actual palette definitions, package metadata and README were re-inspected at revision `ef8864bb42bf244f0295d1c5a403b27e3d139695`: all five CSS values match, the package identifies Pavel Pertsev and MIT, and the README declares MIT/X11. Its tree supplies no standalone license file or palette copyright year; that limitation and the attribution remain in the frontend notices.

Keep `frontend/THIRD_PARTY_NOTICES.md` with source and browser distributions. Keep the production Angular build's `3rdpartylicenses.txt` with browser distributions and inspect it whenever bundled dependencies change. That extraction preserves bundled package licenses; it does not replace the template or palette attribution above.

Repeat the installed dependency review after lockfile changes:

```sh
cd frontend
pnpm licenses list --json
pnpm licenses list --prod --json
```

Compare the result with every package record in both lockfile documents; inspect exact release metadata for optional packages absent on the current platform. Publication checks validate their defined file/record scope and do not establish legal clearance. Maintainer review remains separate from this agent-prepared inspection.

## Screenshot font input

Chrome's CDP inspection of the screenshot's text elements reported `NotoSans-Regular`, `NotoSans-Bold`, `NotoSans-Medium` and a `DejaVuSans` fallback glyph in the connection button. All were system fonts, with `isCustomFont=false`. The actual input files' embedded name, version, copyright and license fields were inspected:

| Font input                         | Actual metadata and origin                                                                                                                                                                     | Terms                                                                                                                                                                                                                                                                          |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Noto Sans Regular, Bold and Medium | All three TTF files identify version 2.015 and copyright 2022 The Noto Project Authors. Installed package: `noto-fonts 1:2026.10.01-1`.                                                        | SIL OFL 1.1; embedded declarations match the [Noto Sans 2.015 upstream license](https://github.com/notofonts/latin-greek-cyrillic/blob/NotoSans-v2.015/OFL.txt).                                                                                                               |
| DejaVu Sans                        | `DejaVuSans.ttf` identifies version 2.37, Bitstream copyright 2003, Tavmjong Bah copyright 2006, and DejaVu changes in the public domain. Installed package: `ttf-dejavu 2.37+18+g9b5d1b2f-8`. | Bitstream Vera and Arev permission terms, with public-domain DejaVu changes. The installed license matches the [actual upstream package revision's LICENSE](https://github.com/dejavu-fonts/dejavu-fonts/blob/9b5d1b2ffeec20c7b46aa89c0223d783c02762cf/LICENSE) byte for byte. |

The Noto package's standalone LICENSE contains Apache-2.0, despite its package metadata and these font files declaring OFL. This discrepancy is recorded; the inspected fonts' own embedded declarations and pinned upstream OFL provide the font evidence.

The screenshot is raster output; no font binary is included in the application or image. The [OFL's official FAQ, sections 1.1.1 and 1.13](https://openfontlicense.org/ofl-faq/) permits such output without imposing the font license on the resulting artwork, and [the font-use guidance](https://openfontlicense.org/how-to-use-ofl-fonts/) distinguishes this from redistributing font files. The inspected DejaVu terms permit using the fonts; their font-copy notice conditions remain applicable if font files are redistributed. Font attribution is retained here as input evidence. The screenshot's own provenance record covers the rendered page and existing Gruvbox palette; this font inspection does not establish full clearance or human approval.

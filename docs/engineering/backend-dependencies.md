# Backend dependency provenance

Checked 2026-10-01 against `backend/uv.lock`, installed distribution metadata and packaged license files. The lock contains 29 third-party Python distributions: 27 installed on Linux and two conditional dependencies inspected in their exact upstream wheels. Branchstate 0.1.0 is project-owned and uses the root MIT license.

The repository references these packages through its manifests and lockfile; their implementation files, binaries and license files are not vendored into the repository. Installed Python notices and Pyright's bundled notices remain intact and match their wheel RECORD entries. Source links below identify exact release metadata; license declarations were checked against the installed notices, or upstream archive notices for the conditional/build packages.

## Python distributions

FastAPI, Pydantic, pydantic-settings and Uvicorn are direct runtime dependencies. HTTPX2, Pyright, pytest and Ruff are direct development dependencies. The remaining rows are locked transitive dependencies. Preserve each distribution's complete packaged notices when distributing its artifacts; the holder column is an attribution summary, not a replacement for those notices.

| Distribution / exact source | Version | License | Copyright holder / notice detail |
| --- | --- | --- | --- |
| [annotated-doc](https://pypi.org/pypi/annotated-doc/0.0.5/json) | 0.0.5 | MIT | Sebastián Ramírez; `LICENSE`. |
| [annotated-types](https://pypi.org/pypi/annotated-types/0.8.0/json) | 0.8.0 | MIT | Contributors; `LICENSE`. |
| [AnyIO](https://pypi.org/pypi/anyio/4.15.1/json) | 4.15.1 | MIT | Alex Grönholm; `LICENSE`. |
| [Click](https://pypi.org/pypi/click/8.5.0/json) | 8.5.0 | BSD-3-Clause | Pallets; `LICENSE.txt`. |
| [Colorama](https://pypi.org/pypi/colorama/0.4.6/json) | 0.4.6 | BSD-3-Clause | Jonathan Hartley; upstream `LICENSE.txt` inspected. Windows-only dependency, absent from the Linux environment. |
| [FastAPI](https://pypi.org/pypi/fastapi/0.142.2/json) | 0.142.2 | MIT | Sebastián Ramírez; `LICENSE`. |
| [h11](https://pypi.org/pypi/h11/0.16.0/json) | 0.16.0 | MIT | Nathaniel J. Smith and contributors; `LICENSE.txt`. |
| [HTTPCore2](https://pypi.org/pypi/httpcore2/2.13.0/json) | 2.13.0 | BSD-3-Clause | Pydantic Services Inc., contributors and Encode OSS Ltd; `LICENSE.md`. |
| [HTTPX2](https://pypi.org/pypi/httpx2/2.13.0/json) | 2.13.0 | BSD-3-Clause | Pydantic Services Inc., contributors and Encode OSS Ltd; `LICENSE.md`. |
| [httpx2-jsfetch](https://pypi.org/pypi/httpx2-jsfetch/1.0/json) | 1.0 | BSD-3-Clause | Pydantic Services Inc., contributors and Encode OSS Ltd; upstream `LICENSE.md` inspected. Emscripten-only dependency, absent from the Linux environment. |
| [idna](https://pypi.org/pypi/idna/3.20/json) | 3.20 | BSD-3-Clause | Kim Davies and contributors; `LICENSE.md`. |
| [iniconfig](https://pypi.org/pypi/iniconfig/2.3.0/json) | 2.3.0 | MIT | Holger Krekel and others; `LICENSE`. |
| [nodeenv](https://pypi.org/pypi/nodeenv/1.11.0/json) | 1.11.0 | BSD-3-Clause | Eugene Kalinin; `LICENSE` and `AUTHORS`. Metadata says BSD; the inspected text has three clauses. |
| [OpenTelemetry API](https://pypi.org/pypi/opentelemetry-api/1.45.0/json) | 1.45.0 | Apache-2.0 | OpenTelemetry Authors; `LICENSE`. |
| [packaging](https://pypi.org/pypi/packaging/26.3/json) | 26.3 | Apache-2.0 OR BSD-2-Clause | Donald Stufft and contributors; preserve `LICENSE`, `LICENSE.APACHE` and `LICENSE.BSD`. |
| [Pluggy](https://pypi.org/pypi/pluggy/1.6.0/json) | 1.6.0 | MIT | Holger Krekel; `LICENSE`. |
| [Pydantic](https://pypi.org/pypi/pydantic/2.13.5/json) | 2.13.5 | MIT | Pydantic Services Inc. and contributors; `LICENSE`. |
| [pydantic-core](https://pypi.org/pypi/pydantic-core/2.46.5/json) | 2.46.5 | MIT | Samuel Colvin; `LICENSE`; compiled component scope below. |
| [pydantic-settings](https://pypi.org/pypi/pydantic-settings/2.15.0/json) | 2.15.0 | MIT | Samuel Colvin and contributors; `LICENSE`. |
| [Pygments](https://pypi.org/pypi/pygments/2.21.0/json) | 2.21.0 | BSD-2-Clause | Respective authors; preserve `LICENSE` and `AUTHORS`. |
| [Pyright Python wrapper](https://pypi.org/pypi/pyright/1.1.414/json) | 1.1.414 | MIT | Robert Craigie; `LICENSE`. Microsoft's bundled program has separate provenance below. |
| [pytest](https://pypi.org/pypi/pytest/9.1.1/json) | 9.1.1 | MIT | Holger Krekel and others; `LICENSE`. |
| [python-dotenv](https://pypi.org/pypi/python-dotenv/1.2.4/json) | 1.2.4 | BSD-3-Clause | Saurabh Kumar, Ted Tieken and Jacob Kaplan-Moss; `LICENSE`. |
| [Ruff](https://pypi.org/pypi/ruff/0.16.9/json) | 0.16.9 | MIT | Charles Marsh; preserve its complete `LICENSE`, including the derived-project notices below. |
| [Starlette](https://pypi.org/pypi/starlette/1.7.0/json) | 1.7.0 | BSD-3-Clause | Encode OSS Ltd; `LICENSE.md`. |
| [truststore](https://pypi.org/pypi/truststore/0.10.4/json) | 0.10.4 | MIT | Seth Michael Larson; `LICENSE`. |
| [typing-extensions](https://pypi.org/pypi/typing-extensions/4.16.0/json) | 4.16.0 | PSF-2.0 | Python Software Foundation and historical holders; preserve the complete `LICENSE`, including historical terms. |
| [typing-inspection](https://pypi.org/pypi/typing-inspection/0.4.4/json) | 0.4.4 | MIT | Pydantic Services Inc.; `LICENSE`. |
| [uv_build](https://pypi.org/pypi/uv_build/0.12.21/json) | 0.12.21 | MIT OR Apache-2.0 | Astral Software Inc.; build requirement outside `uv.lock`; upstream `LICENSE-MIT` and `LICENSE-APACHE` inspected. |
| [Uvicorn](https://pypi.org/pypi/uvicorn/0.54.0/json) | 0.54.0 | BSD-3-Clause | Encode OSS Ltd; `LICENSE.md`. |

The pinned build backend is supplied by uv 0.12.21's bundled build implementation and is not an installed runtime distribution. Its exact upstream uv_build wheel and the matching [uv source license](https://github.com/astral-sh/uv/blob/0.12.21/LICENSE-MIT) were inspected.

## Pyright's bundled program

The wrapper installs Microsoft's [Pyright 1.1.414](https://registry.npmjs.org/pyright/1.1.414), MIT, copyright Microsoft Corporation. Its packaged `LICENSE.txt` is present. Bundled typeshed is pinned by `commit.txt` to [289e5d3568961c8bcd33d01eef5b7ec5e1ad33ad](https://github.com/python/typeshed/tree/289e5d3568961c8bcd33d01eef5b7ec5e1ad33ad); its complete `LICENSE` declares Apache-2.0 with MIT parts attributed to Jukka Lehtosalo and contributors. Those notices were inspected and retained.

The installed `vendor.js.map` identifies the following 37 bundled npm packages and exact versions. Each linked release's registry declaration and archive license/notice files were inspected. Yarn's archives omit a standalone license file; the release metadata's `gitHead` identified the exact upstream [fslib license](https://github.com/yarnpkg/berry/blob/a71d42c2ffd6278a202cccb5fb92c3ac0caf9cae/LICENSE.md) and [libzip license](https://github.com/yarnpkg/berry/blob/f4af6c7cf1588f80011ec13060099d96be67127c/LICENSE.md), which were inspected instead.

| Bundled npm packages / exact source and version | License | Copyright holder |
| --- | --- | --- |
| [@yarnpkg/fslib 2.10.4](https://registry.npmjs.org/@yarnpkg/fslib/2.10.4), [@yarnpkg/libzip 2.3.0](https://registry.npmjs.org/@yarnpkg/libzip/2.3.0) | BSD-2-Clause | Yarn contributors. |
| [ansi-styles 4.3.0](https://registry.npmjs.org/ansi-styles/4.3.0), [chalk 4.1.2](https://registry.npmjs.org/chalk/4.1.2), [has-flag 4.0.0](https://registry.npmjs.org/has-flag/4.0.0), [supports-color 7.2.0](https://registry.npmjs.org/supports-color/7.2.0) | MIT | Sindre Sorhus. |
| [binary-extensions 2.3.0](https://registry.npmjs.org/binary-extensions/2.3.0), [is-binary-path 2.1.0](https://registry.npmjs.org/is-binary-path/2.1.0) | MIT | Sindre Sorhus and Paul Miller. |
| [anymatch 3.1.3](https://registry.npmjs.org/anymatch/3.1.3) | ISC | Elan Shanker and Paul Miller. |
| [glob-parent 5.1.2](https://registry.npmjs.org/glob-parent/5.1.2) | ISC | Elan Shanker. |
| [braces 3.0.3](https://registry.npmjs.org/braces/3.0.3), [fill-range 7.1.1](https://registry.npmjs.org/fill-range/7.1.1), [is-extglob 2.1.1](https://registry.npmjs.org/is-extglob/2.1.1), [is-glob 4.0.3](https://registry.npmjs.org/is-glob/4.0.3), [is-number 7.0.0](https://registry.npmjs.org/is-number/7.0.0), [normalize-path 3.0.0](https://registry.npmjs.org/normalize-path/3.0.0), [picomatch 2.3.2](https://registry.npmjs.org/picomatch/2.3.2), [to-regex-range 5.0.1](https://registry.npmjs.org/to-regex-range/5.0.1) | MIT | Jon Schlinkert. |
| [buffer-from 1.1.2](https://registry.npmjs.org/buffer-from/1.1.2) | MIT | Linus Unnebäck. |
| [chokidar 3.6.0](https://registry.npmjs.org/chokidar/3.6.0) | MIT | Paul Miller and Elan Shanker. |
| [color-convert 2.0.1](https://registry.npmjs.org/color-convert/2.0.1) | MIT | Heather Arthur. |
| [color-name 1.1.4](https://registry.npmjs.org/color-name/1.1.4) | MIT | Dmitry Ivanov. |
| [command-line-args 5.2.1](https://registry.npmjs.org/command-line-args/5.2.1) | MIT | Lloyd Brookes. |
| [jsonc-parser 3.3.1](https://registry.npmjs.org/jsonc-parser/3.3.1), [vscode-jsonrpc 9.0.1](https://registry.npmjs.org/vscode-jsonrpc/9.0.1), [vscode-languageserver 10.1.0](https://registry.npmjs.org/vscode-languageserver/10.1.0), [vscode-languageserver-protocol 3.18.2](https://registry.npmjs.org/vscode-languageserver-protocol/3.18.2), [vscode-languageserver-textdocument 1.0.12](https://registry.npmjs.org/vscode-languageserver-textdocument/1.0.12), [vscode-languageserver-types 3.18.0](https://registry.npmjs.org/vscode-languageserver-types/3.18.0), [vscode-uri 3.1.0](https://registry.npmjs.org/vscode-uri/3.1.0) | MIT | Microsoft and contributors; additional protocol attribution below. |
| [lodash.camelcase 4.3.0](https://registry.npmjs.org/lodash.camelcase/4.3.0) | MIT | jQuery Foundation and contributors; Underscore attribution retained upstream. Documentation samples have a separate CC0 waiver. |
| [readdirp 3.6.0](https://registry.npmjs.org/readdirp/3.6.0) | MIT | Thorsten Lorenz and Paul Miller. |
| [smol-toml 1.7.0](https://registry.npmjs.org/smol-toml/1.7.0) | BSD-3-Clause | Squirrel Chat and others. |
| [source-map 0.6.1](https://registry.npmjs.org/source-map/0.6.1) | BSD-3-Clause | Mozilla Foundation and contributors. |
| [source-map-support 0.5.21](https://registry.npmjs.org/source-map-support/0.5.21) | MIT | Evan Wallace. |
| [tmp 0.2.7](https://registry.npmjs.org/tmp/0.2.7) | MIT | KARASZI István. |
| [tslib 1.14.1](https://registry.npmjs.org/tslib/1.14.1) | 0BSD | Microsoft; `LICENSE.txt` and `CopyrightNotice.txt` inspected. |

The Microsoft language-server packages' `thirdpartynotices.txt` files were also inspected. They include TypeFox attribution and DefinitelyTyped 0.0.1 under MIT, with respective contributors retaining copyright.

The installed Pyright bundle includes the Microsoft and typeshed licenses but does not include the individual vendor-package notices above. Their upstream terms remain applicable; a distribution that includes this bundled tool must address that notice gap. Pyright also declares optional external `fsevents~2.3.3`; it is absent from the inspected Linux bundle and its platform-specific resolution was not reviewed.

Node is an external development-tool prerequisite, not a Python lockfile dependency or a binary copied into this repository. The inspected environment used Node 26.10.0. Its complete runtime and bundled native-library notices were not reviewed for redistribution here.

## Other inputs and review limits

Ruff's complete packaged `LICENSE` reproduces MIT notices for derivatives from autoflake, autotyping, Flake8, flake8-eradicate, flake8-pyi, flake8-simplify, isort, pygrep-hooks, pycodestyle, pydocstyle, Pyflakes, Pyright, pyupgrade, rome/tools, RustPython and rust-analyzer/text-size. Those preserved notices were inspected; the file does not identify exact source revisions for those derivatives.

The Serena configuration's field names were checked against the [official project schema template](https://raw.githubusercontent.com/oraios/serena/main/src/serena/resources/project.template.yml). The minimal configuration was authored for Branchstate; template comments and substantive template body were not copied. This is a schema reference, not a vendored Serena implementation.

This inventory covers the locked Python package graph, its packaged notices and the identified Pyright JavaScript bundle. It does not trace every Rust dependency compiled into pydantic-core, Ruff or uv's build implementation, every native/Wasm dependency inside Yarn libzip, or the complete derivation history of packaged data and type stubs. Those limits remain unresolved for redistribution of such binaries; package metadata and passing repository checks do not establish complete license clearance. Recheck this inventory when the lockfile or distributed artifacts change, under the [publication policy](publication-policy.md). Maintainer review remains independent of these agent checks.

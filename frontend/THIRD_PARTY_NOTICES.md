# Frontend third-party notices

The root MIT license covers Branchstate-owned code. The components and generated derivatives below retain their upstream terms. Preserve this file with frontend source and browser distributions. Browser distributions must also include the Angular production build's `3rdpartylicenses.txt`.

## Nx generator templates

Nx 23.2.1 generated the application scaffold and its TypeScript, HTML, CSS and configuration templates; retained and modified template code is covered by the following upstream notice. Source: [Nx application generator](https://github.com/nrwl/nx/tree/23.2.1/packages/angular/src/generators/application), [Nx license](https://github.com/nrwl/nx/blob/23.2.1/LICENSE).

```text
(The MIT License)

Copyright (c) 2017-2026 Narwhal Technologies Inc.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## Orval client and validation generators

Orval 8.39.0, including `@orval/angular` and `@orval/zod`, generates the Angular HTTP client and Zod validation code from the project-owned OpenAPI document. Source: [Angular generator](https://github.com/orval-labs/orval/tree/v8.39.0/packages/angular), [Zod generator](https://github.com/orval-labs/orval/tree/v8.39.0/packages/zod), [Orval license](https://github.com/orval-labs/orval/blob/v8.39.0/LICENSE).

```text
MIT License

Copyright (c) 2022-present Victor Bury

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Angular

Angular 22.2.1 and its build tooling retain this upstream notice. Source: [Angular](https://github.com/angular/angular/tree/22.2.1), [Angular CLI](https://github.com/angular/angular-cli/tree/22.2.1).

```text
The MIT License

Copyright (c) 2010-2026 Google LLC. https://angular.dev/license

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

## Gruvbox palette

The page CSS uses `#282828`, `#ebdbb2`, `#b8bb26`, `#d79921` and `#bdae93` from Gruvbox by **Pavel Pertsev (morhetz)**. This reuse covers the five color values, with no copied theme implementation, fonts, icons or images.

The source revision checked for Branchstate branding and re-inspected for this page is `ef8864bb42bf244f0295d1c5a403b27e3d139695`: [palette definitions](https://github.com/morhetz/gruvbox/blob/ef8864bb42bf244f0295d1c5a403b27e3d139695/colors/gruvbox.vim), [MIT declaration](https://github.com/morhetz/gruvbox/blob/ef8864bb42bf244f0295d1c5a403b27e3d139695/package.json), [MIT/X11 README](https://github.com/morhetz/gruvbox/blob/ef8864bb42bf244f0295d1c5a403b27e3d139695/README.md#license). The reviewed evidence is preserved in [the existing branding notices](../docs/branding/THIRD_PARTY_NOTICES.md#gruvbox-palette).

That revision supplies no standalone LICENSE file or copyright year for the palette. Attribution is preserved above without inventing a year. The standard MIT permission and disclaimer text below is reproduced for the declared terms; it is not a verbatim upstream license file.

```text
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Runtime and build dependencies

Runtime dependencies and their license evidence are recorded in [the frontend dependency review](../docs/engineering/frontend-dependencies.md). This file preserves generator and palette attribution; the production `3rdpartylicenses.txt` carries the licenses for code bundled into the browser application. Tool distributions retain their own packaged LICENSE, CopyrightNotice and third-party notice files.

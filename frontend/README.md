# Branchstate frontend

Angular 22.2.1 in an Nx 23.2.1 workspace. Use Node **26.10.0** and pnpm **12.8.1**; the committed lockfile pins application and tool dependencies. Target desktop Chrome 155 and newer. The page checks the backend `GET /health` endpoint and accepts `{"status":"ok"}` through a generated, runtime-validated client.

Browserslist includes unreleased Chrome versions while excluding versions below 155, so the selected target resolves even while Chrome 155 is beta. Build and test targets first reject empty or incompatible browser lists; an empty target would leave unsupported syntax in the Node-based test bootstrap. [Browserslist query rules](https://github.com/browserslist/browserslist#full-list).

Angular currently warns that these unreleased versions are outside its published browser support list, but retains them as compilation targets. Verify the page in Chrome 155 or newer before treating that browser baseline as runtime-tested.

## Local development

From the repository root:

```sh
cd frontend
pnpm install --frozen-lockfile --strict-peer-dependencies
pnpm start
```

Open `http://127.0.0.1:4200`. The development server proxies `/api/health` to `http://127.0.0.1:8000/health`, so no cross-origin configuration is needed. Start the backend separately; an unavailable backend produces a retryable error on the page. To use a different local backend address, change `target` in `apps/web/proxy.conf.json`. Stop the development server with Ctrl+C.

## Checks and production build

Run from `frontend/`:

```sh
pnpm lint
pnpm test
pnpm format:check
pnpm build
```

Vitest **4.1.11** runs through the official `@angular/build:unit-test` builder. Tests cover loading, valid/invalid responses, HTTP/network errors, retries, cancellation and runtime configuration. ESLint enforces Nx project boundaries and public entry points. The client and platform libraries contain actual shared code; add feature layers and their own tests as needed.

The client-only production output is `dist/apps/web/`. Serve that directory over HTTP, including `config.json`, `THIRD_PARTY_NOTICES.md` and `3rdpartylicenses.txt`. There is no SSR. The production server must route `/api/` to the backend and strip that prefix, or supply an explicit API URL below. Hosting and the complete Docker Compose integration are separate work.

## Deployment configuration

Before Angular starts, it fetches `/config.json` from the page's origin with caching disabled. The default is:

```json
{ "apiBaseUrl": "/api" }
```

Replace the deployed file to use a different API origin without rebuilding JavaScript:

```json
{ "apiBaseUrl": "https://api.example.com" }
```

The value may be a root-relative prefix or an absolute HTTP(S) URL; trailing slashes are normalized. For different frontend/API origins, the backend must allow the frontend origin through CORS. Prefer a same-origin reverse proxy when CORS is unnecessary. Invalid or missing configuration prevents startup. This file is public browser configuration; it must contain no secrets. Serve it with `Cache-Control: no-store` as well to avoid stale intermediary responses.

## API generation

`openapi/health.json` is the FastAPI OpenAPI snapshot for the agreed M0 health endpoint (`operationId: getHealth`). Update it from a running backend when its contract changes:

```sh
curl --fail --silent --show-error http://127.0.0.1:8000/openapi.json -o openapi/health.json
pnpm generate:api
pnpm lint
pnpm test
pnpm build
```

Orval 8.39.0 generates the Angular service, DI base URL provider and Zod 4.6.5 schemas under `libs/api-client/src/lib/generated/`. Runtime response validation is enabled explicitly; do not edit generated files. Review the snapshot and generated changes together. Dependency/template and palette evidence is in [frontend provenance](../docs/engineering/frontend-dependencies.md).

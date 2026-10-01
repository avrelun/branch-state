# Repository Guidelines

## Project Structure & Current Status

This repository contains planning documents, a local PostgreSQL workflow and an Angular frontend under `frontend/`. `branchstate-starter/` preserves the original product Markdown files. Keep new application work within Milestone 0 until its complete development loop is verified.

Read all seven documents before making architectural decisions. Start with `README.md` and `CODEX_START_PROMPT.md`; use `MILESTONES.md` to constrain scope. Architecture notes are suggested defaults, while the required stack is Python, FastAPI, Angular, and PostgreSQL.

For Milestone 0, propose a minimal layout such as `backend/`, `frontend/`, and `docs/`, with root-level Docker Compose configuration and CI under `.github/workflows/`. Keep simulation code independent of FastAPI.

## Build, Test, and Development Commands

Frontend commands are documented in `frontend/README.md`: use pnpm with the lockfile, `pnpm start`, `pnpm lint`, `pnpm test`, `pnpm format:check` and `pnpm build` from `frontend/`. Repository checks and the PostgreSQL workflow are documented in README.md. Do not assume backend or complete-application Compose commands exist until their tooling is introduced.

Milestone 0 must provide a local Docker Compose workflow, one backend endpoint, one frontend page, automated tests, formatting, linting, and CI. Document exact runnable commands and prerequisites in the root README as tooling is introduced.

## Coding Style & Naming Conventions

Until formatter configuration is established, use four-space indentation for Python and two-space indentation for TypeScript, HTML, and configuration files. Use `snake_case` for Python modules and functions, `PascalCase` for classes, and `kebab-case` for Angular filenames.

The frontend uses Prettier and ESLint with Angular rules and Nx boundaries. Keep libraries behind public entry points and retain generated Orval output. Use the same checks locally and in CI. Prefer explicit domain rules and small modules over speculative abstractions.

## Testing Guidelines

The frontend uses Vitest 4.1.11 through the official Angular unit-test builder. Test page behavior with TestBed and HttpTestingController, including malformed successful responses. No coverage threshold has been selected. Introduce simulation behavior tests as domain logic arrives. Suggested naming is `test_*.py` for Python and `*.spec.ts` for Angular.

Verify invariants and reproducibility: identical seeds, simulator versions, configuration, and commands must produce identical outcomes. Test the simulation core without HTTP or PostgreSQL.

## Commit & Pull Request Guidelines

Use concise, imperative commit subjects, such as `Add backend health endpoint`.

Keep pull requests focused on one milestone or coherent change. Describe the resulting behavior, validation performed, and deferred decisions. Link relevant issues when available and include screenshots for UI changes.

## Architecture Boundaries

Start with Milestone 0. Defer AI, branching, event sourcing, and background infrastructure until justified. AI may propose validated commands or explain recorded evidence; deterministic simulation rules govern world state.


## Repository Boundaries and Review

- Keep instructions, documentation, commands and configuration specific to Branchstate and self-contained. Do not reference external coordination notes, personal setup or sibling checkouts.
- Document the necessary rationale and alternatives for product decisions inside this repository.
- Work on a topic branch and submit a PR. Maintainer review is required before merge; agent self-checks are not human approval. Do not push directly to main without explicit integration approval.
- Use CONTRIBUTING.md for contribution and attribution rules and docs/engineering/publication-policy.md for provenance and publication checks.
- Before publishing assets, inspect all inputs, including palettes, fonts and generated derivatives. Record sources, license notices and inspection evidence in docs/engineering/asset-provenance.json; recheck changed assets and notices before updating hashes. Generated geometry and passing checks do not establish originality or legal clearance.
- State what was checked and any unresolved provenance in the PR. Keep unresolved materials out of the publication candidate, and never substitute agent self-checks for maintainer approval.
- Project-owned code and accompanying documentation use the root MIT LICENSE. Preserve third-party terms.

# Repository Guidelines

## Project Structure & Current Status

This repository currently contains planning documents, not an implemented application. `branchstate-starter.zip` is the original bundle; `branchstate-starter/` contains the extracted Markdown files. Research and branding assets exist; application source and application tests do not yet exist.

Read all seven documents before making architectural decisions. Start with `README.md` and `CODEX_START_PROMPT.md`; use `MILESTONES.md` to constrain scope. Architecture notes are suggested defaults, while the required stack is Python, FastAPI, Angular, and PostgreSQL.

For Milestone 0, propose a minimal layout such as `backend/`, `frontend/`, and `docs/`, with root-level Docker Compose configuration and CI under `.github/workflows/`. Keep simulation code independent of FastAPI.

## Build, Test, and Development Commands

Application build, development, test, and lint commands are not configured yet. Repository checks are documented in README.md. Do not assume `npm test`, `pytest`, or `docker compose up --build` works until the corresponding tooling exists.

Milestone 0 must provide a local Docker Compose workflow, one backend endpoint, one frontend page, automated tests, formatting, linting, and CI. Document exact runnable commands and prerequisites in the root README as tooling is introduced.

## Coding Style & Naming Conventions

Until formatter configuration is established, use four-space indentation for Python and two-space indentation for TypeScript, HTML, and configuration files. Use `snake_case` for Python modules and functions, `PascalCase` for classes, and `kebab-case` for Angular filenames.

No formatter or linter is currently configured. Select tools during Milestone 0 and use the same checks locally and in CI. Prefer explicit domain rules and small modules over speculative abstractions.

## Testing Guidelines

No testing framework or coverage threshold has been selected. Add basic checks in Milestone 0; introduce simulation behavior tests as domain logic arrives. Suggested naming is `test_*.py` for Python and `*.spec.ts` for Angular.

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
- Project-owned code and accompanying documentation use the root MIT LICENSE. Preserve third-party terms.

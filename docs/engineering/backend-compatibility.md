# Backend compatibility and implementation prerequisites

Checked 2026-10-01 for M0. The selected backend versions have no conflict in the direct metadata constraints inspected below. This assessment covers upstream release metadata, wheel availability and settings source behavior. Dependency resolution, installation, application tests and database connectivity remain implementation work.

## Runtime and dependency baseline

Use **CPython 3.14.8** and **uv 0.12.21**. Both are stable releases; uv documents Tier 1 support for CPython 3.14. [Python release](https://www.python.org/downloads/release/python-3148/), [uv release](https://github.com/astral-sh/uv/releases/tag/0.12.21), [uv Python support](https://docs.astral.sh/uv/reference/policies/python/).

The selected package releases exist, are not yanked and are current stable releases on the check date; preview/dev releases were excluded. Resolve and commit exact versions in `backend/uv.lock` when introducing the dependencies.

| Distribution | Version | Requires-Python | Relevant compatibility evidence |
| --- | --- | --- | --- |
| [FastAPI](https://pypi.org/pypi/fastapi/0.142.2/json) | 0.142.2 | `>=3.10` | Requires Pydantic `>=2.9.0`, Starlette `>=0.46.0`; declares Python 3.14. |
| [Pydantic](https://pypi.org/pypi/pydantic/2.13.5/json) | 2.13.5 | `>=3.9` | Requires exactly `pydantic-core==2.46.5`; declares Python 3.14. |
| [pydantic-settings](https://pypi.org/pypi/pydantic-settings/2.15.0/json) | 2.15.0 | `>=3.10` | Requires Pydantic `>=2.7.0`, python-dotenv `>=0.21.0`; declares Python 3.14. |
| [Ruff](https://pypi.org/pypi/ruff/0.16.9/json) | 0.16.9 | `>=3.7` | No Python package dependencies; declares Python 3.14. |
| [pytest](https://pypi.org/pypi/pytest/9.1.1/json) | 9.1.1 | `>=3.10` | Requires Pluggy `>=1.5,<2`; declares Python 3.14. |
| [Pyright Python wrapper](https://pypi.org/pypi/pyright/1.1.414/json) | 1.1.414, candidate | `>=3.7` | Matches the [Microsoft release](https://github.com/microsoft/pyright/releases/tag/1.1.414); needs Node. Wrapper metadata admits 3.14 but classifiers stop at 3.12. |
| [SQLAlchemy](https://pypi.org/pypi/SQLAlchemy/2.1.1/json) | 2.1.1 | `>=3.11` | Declares Python 3.14; Greenlet is required only by the `asyncio` extra. |
| [Alembic](https://pypi.org/pypi/alembic/1.20.0/json) | 1.20.0 | `>=3.10` | Requires SQLAlchemy `>=2.0`, admitting 2.1.1; declares Python 3.14. |
| [Psycopg](https://pypi.org/pypi/psycopg/3.3.6/json) | 3.3.6 | `>=3.10` | Declares Python 3.14; upstream supports PostgreSQL 18. |

Pydantic 2.13.5 satisfies both FastAPI and settings bounds. Their shared bounds intersect at `typing-extensions>=4.14.1` and `typing-inspection>=0.4.2`. These checks do not establish that every transitive dependency or optional extra resolves together.

For regular CPython 3.14 on Linux x86_64/glibc, native wheels are published for [pydantic-core 2.46.5](https://pypi.org/pypi/pydantic-core/2.46.5/json), Ruff and SQLAlchemy. [Psycopg-binary 3.3.6](https://pypi.org/pypi/psycopg-binary/3.3.6/json) also has matching `cp314` wheels. The inspected releases publish musllinux wheels as well, but container architecture, libc and ABI need their own checks; regular `cp314` and free-threaded `cp314t` are distinct targets.

## Dependencies needed for a runnable backend

- **ASGI server:** base FastAPI does not include a runner. [Uvicorn 0.54.0](https://pypi.org/pypi/uvicorn/0.54.0/json) is a stable candidate with Python `>=3.10` and a 3.14 classifier. Declare it explicitly when implementing the endpoint. Its base install is sufficient for the proposed command; broader `standard` extras need their own resolution.
- **HTTP tests:** choose and declare a test client against the locked Starlette release. Current [Starlette 1.7.0](https://github.com/Kludex/starlette/blob/1.7.0/starlette/testclient.py) prefers [HTTPX2 2.13.0](https://pypi.org/pypi/httpx2/2.13.0/json), which declares Python 3.14. [HTTPX 0.28.1](https://pypi.org/pypi/httpx/0.28.1/json) remains a deprecated fallback in that Starlette release. FastAPI's tutorial still recommends HTTPX; verify the actual locked combination with an endpoint test rather than inferring behavior from the tutorial alone.
- **Type checking:** add the Pyright wrapper to uv dev dependencies and pin it when resolving. This is a [third-party wrapper](https://pypi.org/project/pyright/1.1.414/) around Microsoft's Node program. The [official package](https://registry.npmjs.org/pyright/1.1.414) requires Node `>=14`. The wrapper can bootstrap Node or use an npm fallback, so verify its executable chain in local development and CI when installed. Keep the pinned version; do not force `latest` through wrapper environment overrides. Configure Python 3.14, `include=["src", "tests"]`, `venvPath="."` and `venv=".venv"` relative to `backend/pyproject.toml`. [Pyright configuration](https://github.com/microsoft/pyright/blob/1.1.414/docs/configuration.md).
- **Persistence:** introduce SQLAlchemy, Alembic and Psycopg when database work starts. Use explicit `postgresql+psycopg://` for Psycopg 3. Synchronous SQLAlchemy does not require Greenlet or a separate pool package. Bare Psycopg needs system libpq. The `binary` extra bundles client libraries; the `c` extra is source-only and needs a compiler, Python/PostgreSQL development headers and `pg_config`. Verify the chosen deployment path and an actual connection to PostgreSQL 18.6 during implementation. [SQLAlchemy 2.1 driver change](https://docs.sqlalchemy.org/en/21/changelog/migration_21.html#default-postgresql-driver-changed-to-psycopg-psycopg-3), [Psycopg 3.3.6 installation source](https://raw.githubusercontent.com/psycopg/psycopg/3.3.6/docs/basic/install.rst).

## Settings and package layout

The agreed package is `backend/src/branchstate/`, with `app.py` and `settings.py`; add domain, simulation and persistence modules only as needed. Declare a build system with src package discovery so `uv sync` installs `branchstate` into `backend/.venv`. A virtual project without a build system will not install this package. Keep Ruff, pytest and Pyright in the uv dev group. [uv package installation and dev groups](https://docs.astral.sh/uv/concepts/projects/sync/).

Use committed `backend/config.toml` for non-secret settings, an ignored `backend/.env` for local secrets/overrides and a committed `.env.example`. With settings 2.15.0:

1. Explicitly register `TomlConfigSettingsSource` through `settings_customise_sources`; `toml_file` alone does not activate TOML loading.
2. Return sources in the order **process environment > local dotenv > TOML**; field defaults follow. Do not retain higher-priority constructor or CLI overrides implicitly. Python 3.14 supplies `tomllib`, so an additional TOML parser is unnecessary.
3. Anchor both file paths to the backend configuration root independently of process cwd. Define how that root is located in the installed package/container; a development-only relative path is insufficient.
4. Validate required settings at startup and fail on invalid input. Missing optional files may be skipped, so required fields or explicit file checks must enforce the application's needs. Use a dedicated dotenv and an explicit unknown-key policy; never provide a default database password.

Source: [settings 2.15.0 documentation](https://github.com/pydantic/pydantic-settings/blob/v2.15.0/docs/index.md), [source ordering](https://github.com/pydantic/pydantic-settings/blob/v2.15.0/pydantic_settings/main.py), [TOML provider](https://github.com/pydantic/pydantic-settings/blob/v2.15.0/pydantic_settings/sources/providers/toml.py). Versioned sources matter: newer documentation describes dotenv options absent from this selected release.

## Commands and checks for implementation

The following is a proposed repository-root command shape, **not a verified startup workflow**. It requires an implemented `branchstate.app:app`, a declared build system and dependencies, a committed current `backend/uv.lock`, and backend tool configuration. Initial lockfile creation belongs to backend implementation; `--locked` rejects a missing or stale lockfile.

```sh
uv sync --project backend --locked --python 3.14.8 --no-python-downloads
uv run --project backend --locked uvicorn branchstate.app:app --reload
uv run --project backend --locked pytest backend/tests
uv run --project backend --locked ruff check backend
uv run --project backend --locked ruff format --check backend
uv run --project backend --locked pyright --project backend/pyproject.toml
```

Backend implementation must verify package import and endpoint behavior, source precedence and invalid/missing settings, and the same configuration from repository/backend/unrelated working directories. Database implementation must verify migrations and a real connection. Review direct/transitive licenses when creating the lockfile under the [publication policy](publication-policy.md). Document startup/shutdown commands in the README only after exercising them from a fresh checkout. No installation, dependency resolution, application execution or container startup was performed for this assessment.

<img src="docs/branding/mark.svg" alt="Branchstate branching mark" width="96" height="96">

# Branchstate

A synthetic retail world whose data comes from a coherent, reproducible simulation history. Start small, inspect consequences, and later compare alternative histories.

## Current state

The repository contains product planning, delivery tooling and a local PostgreSQL workflow. The backend baseline has been checked against published metadata; backend/frontend implementation, locked dependencies and application checks remain pending. Milestone 0 will provide Python/FastAPI, Angular, the complete Docker Compose workflow, tests, formatting, linting, and CI for the application.

## Project map

- [Product overview](branchstate-starter/README.md) and [milestones](branchstate-starter/MILESTONES.md)
- [Contributing](CONTRIBUTING.md) and [publication policy](docs/engineering/publication-policy.md)
- [Contributor guidance](AGENTS.md)
- [Backend compatibility and implementation prerequisites](docs/engineering/backend-compatibility.md)

Historical research, personal branding, operational records, and the original starter archive remain local and are excluded from publication. The extracted product documents are preserved.

## Local PostgreSQL

Requires Python 3, Docker Engine with a reachable daemon and the Docker Compose plugin. Run from the repository root:

```sh
python3 scripts/init_local_env.py
docker compose up --detach --wait --wait-timeout 90 db
```

The setup command generates a password in an untracked, private `.env` and refuses to overwrite an existing file. `.env.example` lists the settings. Adjust `POSTGRES_PORT` if 5432 is occupied; keep real credentials out of Git. Compose passes database settings explicitly to the container and initializes SCRAM authentication for all TCP connections, including container loopback. Changing initialization settings later does not alter an existing database.

PostgreSQL **18.6** is pinned by image digest. Data is stored in the project's `postgres-data` volume mounted at `/var/lib/postgresql`, with the image's default `PGDATA=/var/lib/postgresql/18/docker`. The published port binds to `127.0.0.1`. A host application connects to `127.0.0.1:<POSTGRES_PORT>`; later Compose application containers connect to `db:5432`. The healthcheck waits for readiness; verify authenticated SQL separately:

```sh
docker compose exec db sh -ec 'export PGPASSWORD="$POSTGRES_PASSWORD"; exec psql --host=127.0.0.1 --username="$POSTGRES_USER" --dbname="$POSTGRES_DB" --no-password --command="SELECT 1;"'
```

Stop or remove containers while retaining data:

```sh
docker compose stop
docker compose down
```

**Destructive reset:** `docker compose down --volumes` deletes this project's database data. Use a separate Compose project name (`docker compose --project-name <name> ...`) and a distinct port for each checkout requiring its own database.

Run the integration check from a fresh checkout:

```sh
python3 scripts/verify_postgres.py
```

It starts an isolated database with generated test credentials and an available loopback port, checks version, TCP authentication, rejected credentials, and persistence across restart and container recreation, then destroys only its disposable project data. It requires Docker access and may download the pinned image. Backend/frontend startup and application database integration arrive with their implementation.

## Available checks

Requires Git and Python 3, with no additional packages:

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/check-publication.py --revision HEAD
git diff --check
```

Before the first commit, omit `--revision HEAD` to check staged files. Enable the reviewed local hooks with `git config --local core.hooksPath .githooks`. Pre-commit runs the publication guard and whitespace check; pre-push checks the pushed tips. CI checks the committed tree. The guard requires current [asset provenance records](docs/engineering/asset-provenance.json), including tracked license notices, for supported media and fonts. These records require substantive review; passing checks do not establish legal clearance. These are repository checks; application tests arrive with M0.

## Licensing

Project-owned code and accompanying documentation are licensed under the [MIT License](LICENSE). Third-party materials retain their applicable licenses. The branding uses colors from Gruvbox by Pavel Pertsev (morhetz); see [branding third-party notices](docs/branding/THIRD_PARTY_NOTICES.md). See the publication policy for provenance and third-party material requirements.

Image input: [official PostgreSQL image](https://hub.docker.com/_/postgres), [pinned upstream Dockerfile](https://github.com/docker-library/postgres/blob/e00e1bd34ec5c8a8e7ad89b273b3d42efaf6d5bc/18/trixie/Dockerfile). The inspected image uses Debian trixie-slim and PostgreSQL 18.6. PostgreSQL retains its [PostgreSQL license](https://www.postgresql.org/about/licence/); Docker image tooling uses [MIT](https://github.com/docker-library/postgres/blob/e00e1bd34ec5c8a8e7ad89b273b3d42efaf6d5bc/LICENSE). Bundled Debian packages retain their [individual terms and copyright notices](https://www.debian.org/legal/licenses/). This repository references the upstream image; it does not redistribute its layers or copy its scripts. Image-wide redistribution/license review remains necessary if distribution is introduced.

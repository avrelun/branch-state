<img src="docs/branding/mark.svg" alt="Branchstate branching mark" width="96" height="96">

# Branchstate

A synthetic retail world whose data comes from a coherent, reproducible simulation history. Start small, inspect consequences, and later compare alternative histories.

## Current state

The repository contains product planning and delivery tooling. The application is not implemented yet. Milestone 0 will provide Python/FastAPI, Angular, PostgreSQL, Docker Compose, tests, formatting, linting, and CI for the application. Exact runtime versions remain to be selected.

## Project map

- [Product overview](branchstate-starter/README.md) and [milestones](branchstate-starter/MILESTONES.md)
- [Contributing](CONTRIBUTING.md) and [publication policy](docs/engineering/publication-policy.md)
- [Contributor guidance](AGENTS.md)

Historical research, personal branding, operational records, and the original starter archive remain local and are excluded from publication. The extracted product documents are preserved.

## Available checks

Requires Git and Python 3, with no additional packages:

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/check-publication.py --revision HEAD
git diff --check
```

Before the first commit, omit `--revision HEAD` to check staged files. Enable the reviewed local pre-commit hook with `git config --local core.hooksPath .githooks`. It runs the publication guard and whitespace check. CI checks the committed tree. These are repository checks; application tests arrive with M0.

## Licensing

Project-owned code and accompanying documentation are licensed under the [MIT License](LICENSE). Third-party materials retain their applicable licenses. The branding uses colors from Gruvbox by Pavel Pertsev (morhetz); see [branding third-party notices](docs/branding/THIRD_PARTY_NOTICES.md). See the publication policy for provenance and third-party material requirements.

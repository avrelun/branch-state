# Contributing

Keep changes small and tied to a concrete product outcome. Describe behavior and checks in the PR. Record human and agent implementation, checking, and approval separately; the authenticated account does not establish actual authorship.

All changes require short branches, PRs, and maintainer review. Maintainer approval is required before an agent merges a PR. An agent checking its own work is not independent review. Contributors may claim an activity or request review at line, module, service, or domain level; work may continue on independent authorized tasks.

After inspecting the versioned hook, enable it in your clone:

```sh
git config --local core.hooksPath .githooks
```

The pre-commit hook checks staged blobs, not working-tree copies. Run the committed-tree check with `python3 scripts/check-publication.py --revision HEAD`. Hooks are local and bypassable; CI repeats the publication check. Pattern matching cannot detect every secret or establish legal rights.

Read [publication policy](docs/engineering/publication-policy.md) before adding third-party code, assets, datasets, or dependencies. Do not submit materials you lack permission to contribute. An AI suggestion is not evidence of provenance or permission. No contributor license agreement or mandatory sign-off is imposed at this stage.

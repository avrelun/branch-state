# Contributing

Keep changes small and tied to a concrete product outcome. Describe behavior and checks in the PR. Record human and agent implementation, checking, and approval separately; the authenticated account does not establish actual authorship.

All changes require short branches, PRs, and maintainer review. Maintainer approval is required before an agent merges a PR. An agent checking its own work is not independent review. Contributors may claim an activity or request review at line, module, service, or domain level; work may continue on independent authorized tasks.

For changes tracked in Jira, include the existing work item key in the branch name and PR title. Add `Jira: [BRST-1]` to the PR description, replacing `BRST-1` with the relevant key. The GitHub integration expands this bracketed reference into a Jira link; a key in the title alone does not provide that description link. Link existing work rather than creating duplicate issues just to populate PR metadata.

After inspecting the versioned hook, enable it in your clone:

```sh
git config --local core.hooksPath .githooks
```

The pre-commit hook checks staged blobs, not working-tree copies. Run the committed-tree check with `python3 scripts/check-publication.py --revision HEAD`. Hooks are local and bypassable; CI repeats the publication check. Pattern matching cannot detect every secret or establish legal rights.

Read [publication policy](docs/engineering/publication-policy.md) before adding third-party code, assets, datasets, or dependencies. Do not submit materials you lack permission to contribute. An AI suggestion is not evidence of provenance or permission. No contributor license agreement or mandatory sign-off is imposed at this stage.

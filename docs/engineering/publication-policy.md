# Public repository policy

## License and provenance

The maintainer selected MIT on September 27, 2026. The root LICENSE covers project-owned code and accompanying documentation in this repository. Third-party materials retain their applicable licenses; excluded local materials are not published or relicensed by this decision.

Before importing third-party code, images, fonts, datasets, generated derivatives, or substantial excerpts, record the source URL, version/revision, copyright holder if known, license, required notices, and intended use. Preserve applicable license and NOTICE files. Confirm that the intended redistribution and combination are permitted. Publicly accessible content is not automatically licensed for reuse.

Keep a third-party inventory when actual imports begin. Links in research are references, not permission to copy the referenced implementation. Record unresolved provenance rather than asserting originality. Review AI-generated code and assets under the same rule; generation alone does not prove clearance or copyright ownership.

For dependencies, review direct and transitive licenses when introducing or updating lockfiles. Recheck before releases and distributions. Branding rights and third-party materials must have an explicit scope rather than silently inheriting the code license.

## Privacy and publication

Do not publish personal billing/support records, emails, account audits, credentials, local agent histories, or screenshots containing personal data. Historical local-only materials are ignored and blocked by the publication check. Publish a reviewed summary when project-relevant information is needed.

Review the complete initial tree and subsequent diffs. Use a GitHub noreply address for agent-prepared commits in this repository. If a secret is published, revoke/rotate it first; deleting a file does not remove copies or Git history.

## Checks and limits

The local hook and CI inspect tracked blobs for prohibited paths, common credential signatures, private-key markers, archives, and large files. They are a narrow guard against accidents, not a legal clearance or comprehensive secret scanner. License decisions and provenance require review. Changes to the guard, CI, and publication exclusions require explicit reviewer attention.

References, checked September 27, 2026:

- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
- https://choosealicense.com/no-permission/

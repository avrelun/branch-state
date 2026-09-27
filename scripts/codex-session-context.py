#!/usr/bin/env python3
"""Restore repository rules after session start/resume/compaction; no side effects."""
import json
import sys


def response(event):
    if event.get('hook_event_name') != 'SessionStart':
        return {}
    return {'hookSpecificOutput': {
        'hookEventName': 'SessionStart',
        'additionalContext': (
            'Branchstate: follow AGENTS.md, CONTRIBUTING.md, and '
            'docs/engineering/publication-policy.md. Changes require a PR and '
            'maintainer review before merge. Agent self-checks are not human approval. '
            'Record actual implementer, checker, and approver separately. '
            'Preserve third-party licenses and provenance; do not publish private '
            'records or credentials. Hooks cannot establish legal clearance. '
            'Before adding or publishing assets, inspect actual sources, including '
            'palettes, fonts and generated derivatives; record evidence in '
            'docs/engineering/asset-provenance.json. Do not infer originality from '
            'generated geometry or a passing check. Recheck changed files and '
            'notices before updating provenance hashes. In PRs state the scope '
            'checked and remaining uncertainty; human approval remains separate. '
            'MIT is selected for project-owned code and accompanying documentation.'
        )}}


if __name__ == '__main__':
    print(json.dumps(response(json.load(sys.stdin))))

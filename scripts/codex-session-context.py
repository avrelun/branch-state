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
            'MIT is selected for project-owned code and accompanying documentation.'
        )}}


if __name__ == '__main__':
    print(json.dumps(response(json.load(sys.stdin))))

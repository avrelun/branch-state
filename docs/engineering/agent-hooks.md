# Agent hooks

The project `.codex/hooks.json` configures a SessionStart command hook. It restores the review, provenance, privacy context on startup, resume, clear, and compaction. The handler has no filesystem or network side effects and does not grant permissions or claim legal clearance.

This project hook complements the pre-commit guard and CI; it does not enforce GitHub branch protection.

Activation requires trusting the project config layer and reviewing the hook definition in Codex `/hooks`. New/changed hooks are skipped until trusted. Do not programmatically mark the hook trusted or bypass trust. The handler and JSON config have been checked locally; runtime activation has not been verified in a new session.

Source: https://learn.chatgpt.com/docs/hooks (checked September 27, 2026).

# Prompt for Codex

You are helping build a new project with the working name **Branchstate**.

Read every Markdown file in this repository before making architectural decisions.

## Product

Branchstate is a synthetic business simulator.

The first domain is a small online retail business.

The central idea is that synthetic data should be produced by a coherent history:

```text
initial world
  -> events
  -> business processes
  -> state changes
  -> current world
```

Later the user should be able to inject disruptive events, move through simulated time, rewind, create alternative branches, and compare outcomes.

Examples of future scenarios:

- supplier outage
- warehouse destruction
- logistics disruption
- demand spike
- payment provider failure
- major regional disruption
- deliberately extreme events such as epidemic or meteor impact

These are simulated scenarios, not attempts to predict real-world events.

## Required stack

- Python
- FastAPI
- Angular
- PostgreSQL

An AI subsystem should eventually use a popular contemporary Python AI stack, but do not force AI into Milestone 0 or 1 if it does not improve the product.

## Engineering philosophy

Prefer:

- simple implementations
- strong domain boundaries
- deterministic behavior
- seeded randomness
- reproducibility
- explicit invariants
- tests around simulation behavior
- boring infrastructure
- incremental architecture

Avoid:

- premature microservices
- Kubernetes
- Kafka
- generic plugin systems
- universal workflow engines
- abstract frameworks created for hypothetical future requirements
- event sourcing unless the project actually starts benefiting from it

The simulation core should not depend on FastAPI.

The first few milestones should remain runnable on one developer machine with Docker Compose.

## Immediate task

Start with **Milestone 0** from `MILESTONES.md`.

Before writing implementation code:

1. Inspect the repository.
2. Propose the smallest reasonable repository structure.
3. Write a short implementation plan for Milestone 0.
4. Identify decisions that are safe to defer.
5. Then implement the milestone.

Do not design later milestones in detail.

Do not ask for clarification unless a missing answer blocks implementation. Prefer a reasonable documented assumption.

At the end:

- run the relevant tests / checks
- summarize what was created
- list deferred decisions
- propose the smallest next step toward Milestone 1

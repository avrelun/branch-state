# Branchstate

Working title for a synthetic business simulation project.

Branchstate is a small, self-contained business world that generates coherent data through simulation rather than by filling tables with random values.

The core idea:

> Create a business world, let time pass, inject events, inspect consequences, rewind, branch the timeline, and compare alternative histories.

The first version should be intentionally narrow and easy to run. It does not need to simulate arbitrary companies, integrate with real services, or model an entire economy.

The project should be useful and interesting even with only 2-3 real users.

## Technology constraints

Primary stack:

- Backend: FastAPI
- Frontend: Angular
- Database: PostgreSQL
- AI: use a popular modern Python AI stack where it actually adds value
- Deployment target: ideally <= $20/month
- Up to ~$50/month is acceptable only if the product becomes personally valuable or close to paying for itself

Avoid unnecessary infrastructure early.

The project should run locally with minimal setup.

## Product principles

1. Simulation first, AI second.
2. Events must have deterministic, explainable consequences whenever possible.
3. AI should not invent causes after the fact.
4. Manual setup should be minimal.
5. The system should generate its own interesting data.
6. Time is a first-class concept.
7. Branching / alternative histories should become a core capability.
8. Users should be able to zoom between abstraction levels:
   - whole business
   - subsystem
   - entity
   - event / cause
9. Every early milestone should already produce something usable.
10. Do not design a universal simulation engine before there is evidence it is needed.

Start with `CODEX_START_PROMPT.md`.

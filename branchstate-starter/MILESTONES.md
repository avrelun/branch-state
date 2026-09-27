# Approximate milestone roadmap

This is intentionally provisional.

Do not treat it as a fixed specification.

---

# Milestone 0 — Walking skeleton

Goal:

Have the complete development loop working.

Deliver:

- FastAPI project
- Angular project
- PostgreSQL
- Docker Compose for local development
- one backend endpoint
- one frontend page
- basic automated tests
- formatting / linting
- CI
- README with local run instructions

Avoid domain complexity.

---

# Milestone 1 — Static synthetic business

Goal:

Create a coherent small business state.

The user clicks something like:

> Create World

The system creates a deterministic world from a seed.

Initial scope:

- products
- customers
- one or two warehouses
- inventory
- orders
- payments

Requirements:

- same generator version + same seed => same initial world
- world can be inspected in Angular
- basic navigation between related entities
- JSON/CSV export is useful but optional

No AI is required yet.

Success condition:

The product already works as a small synthetic dataset generator.

---

# Milestone 2 — Time and events

Goal:

The world changes through simulation.

Add:

- simulation clock
- advance one day
- advance N days
- event log
- basic business processes

Possible processes:

- new orders
- stock reservation
- shipping
- restocking
- payment failure
- cancellation

Important:

State changes should originate from recorded events or explicit simulation actions.

Success condition:

The user can inspect why the current state differs from yesterday.

---

# Milestone 3 — External events

Goal:

Allow meaningful interventions.

Start with 3-5 events.

Examples:

- supplier unavailable for N days
- warehouse unavailable
- demand spike
- payment provider outage
- warehouse destroyed

The user should be able to:

1. select an event
2. configure a few parameters
3. inject it
4. advance time
5. observe consequences

Success condition:

Two simulations with different interventions visibly diverge.

---

# Milestone 4 — Historical snapshots / branching

Goal:

Create alternative histories.

Minimal functionality:

- choose a previous point
- fork the world
- apply a different event
- simulate forward
- compare the two outcomes

Do not build Git.

A branch can initially be implemented by copying a small snapshot if that is simpler.

Possible comparison:

- revenue
- cancelled orders
- delayed orders
- inventory losses
- fulfilled orders
- recovery time

Success condition:

The user can answer:

> "What changed because I made this intervention?"

---

# Milestone 5 — First useful AI feature

Goal:

Introduce a real AI stack without making simulation depend on it.

Suggested feature:

Natural-language event creation.

Example:

> "Destroy the main warehouse on day 120 and reduce regional delivery capacity by 50% for two weeks."

Pipeline:

1. LLM receives current world capabilities
2. LLM produces structured event proposal
3. backend validates proposal
4. user can inspect it
5. deterministic simulator applies it

Possible stack:

- Pydantic structured models
- LangGraph or PydanticAI
- LiteLLM if model routing becomes useful
- Langfuse for tracing/evaluation

Do not introduce all components purely to fill a technology checklist.

---

# Milestone 6 — Investigation mode

Goal:

Turn a generated world into an interactive problem.

Example:

> "Paid orders are accumulating but shipments are falling. Investigate."

The user explores the existing data.

Optional AI responsibilities:

- answer questions using available evidence
- provide hints
- critique the investigation after completion
- generate a short debrief

The actual hidden cause should be produced by simulation rules, not invented during the conversation.

---

# Later possibilities

Not commitments:

- reusable scenario definitions
- arbitrary event DSL
- replay
- scenario marketplace
- multiplayer investigations
- business-specific plugins
- synthetic API server
- synthetic data mapped into user schemas
- QA regression worlds
- incident training
- game-like learning
- DevOps / distributed systems simulation
- career learning integration

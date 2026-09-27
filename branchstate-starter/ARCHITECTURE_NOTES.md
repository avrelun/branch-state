# Early architecture notes

These are defaults, not mandatory choices.

## Backend

FastAPI.

Suggested modules:

```text
app/
  api/
  domain/
  simulation/
  worlds/
  events/
  persistence/
  ai/
```

Try to keep simulation logic independent from FastAPI.

A useful direction:

```python
new_state, emitted_events = simulate(state, command)
```

or equivalent domain APIs.

The simulation core should be testable without HTTP or PostgreSQL.

---

# Frontend

Angular.

Initial screens may be:

```text
/worlds
/worlds/:id
/worlds/:id/orders
/worlds/:id/orders/:orderId
/worlds/:id/events
```

Later:

```text
/worlds/:id/timeline
/worlds/:id/branches
/worlds/:id/compare/:branchA/:branchB
```

Do not force the final "zoom" interaction in the first frontend iteration.

First learn what information users actually need to move between.

---

# Database

PostgreSQL.

Potential initial tables:

```text
world
simulation_run
business_event

product
warehouse
inventory_position

customer
order
order_item
payment
shipment
supplier
purchase_order
```

Do not implement event sourcing just because the product has events.

Event sourcing may become useful later, but a regular relational model plus an append-only event log may be enough for early milestones.

---

# Determinism

Prefer seeded randomness.

Store at least:

- simulation seed
- simulator version
- world configuration
- applied commands / external events

A major long-term property should be reproducibility.

---

# Background processing

Do not start with Celery / Kafka / Temporal unless necessary.

Early simulation can run synchronously if it stays fast.

If a job system becomes necessary, introduce the simplest mechanism that solves the actual problem.

---

# AI

Keep a boundary similar to:

```text
Natural language
    ↓
AI interpretation
    ↓
validated structured command
    ↓
simulation engine
```

and:

```text
simulation evidence
    ↓
AI explanation / tutor
```

Avoid:

```text
AI
 ↓
magically invents entire world state
```

for core simulation.

---

# Deployment

Target a simple low-cost setup.

Possible shape:

```text
Cloudflare / static hosting
        |
     Angular

Small VPS / PaaS
        |
     FastAPI
        |
   PostgreSQL
```

A single small server can host FastAPI + PostgreSQL initially if operational simplicity is more valuable than managed services.

Exact provider selection can be made later.

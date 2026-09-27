# Product principles

## 1. A working small world is better than an abstract engine

The first implementation may hard-code many retail concepts.

Generalize only after at least two concrete use cases need the same abstraction.

## 2. Generate history, not random rows

The interesting property is causal consistency.

A customer refund should exist because something happened.

Inventory should change because events changed it.

## 3. The user should not have to prepare the product before using it

Prefer:

> Create world

over:

> Upload schema, define 18 entities, configure probability distributions, describe your company, map fields, and then generate.

Advanced configuration can come later.

## 4. Interactivity matters

The product should encourage:

- acting
- inspecting
- experimenting
- rewinding
- comparing

rather than primarily reading generated reports.

## 5. Every consequence should be inspectable

If the system claims that event X contributed to state Y, the user should be able to inspect the chain.

## 6. Avoid fake precision

A simulation result is the consequence of the model, not a prediction of reality.

The UI should make that distinction clear.

## 7. AI is not the source of truth

Prefer:

- structured outputs
- explicit rules
- deterministic execution
- traceable prompts
- inspectable context

## 8. Keep infrastructure boring at first

Prefer one deployable backend and one database.

Do not introduce:

- Kubernetes
- Kafka
- dedicated vector databases
- distributed workflow engines
- microservices

unless a real milestone requires them.

## 9. Time and branching are product concepts, not implementation tricks

The history should eventually be something users interact with directly.

## 10. The project should remain fun to extend

A good new feature should often be expressible as:

> "What new thing can happen in the world, and what consequences should follow?"

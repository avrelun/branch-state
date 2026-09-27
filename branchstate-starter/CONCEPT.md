# Concept

## What Branchstate is

Branchstate is a synthetic business simulator.

Instead of generating isolated fake rows, it generates a coherent history.

Example:

1. A customer places an order.
2. Stock is reserved.
3. Payment succeeds.
4. Supplier delivery is delayed.
5. Remaining stock becomes insufficient.
6. Some orders are postponed.
7. Customers cancel.
8. Refunds are created.

The final database state is therefore the consequence of previous events.

This distinction matters.

A synthetic dataset answers:

> "What fake data should exist?"

Branchstate should answer:

> "What happened in this world, and why does the data look like this now?"

---

# Initial domain

Start with one fixed domain: a small online retail business.

Possible entities:

- Product
- Warehouse
- InventoryPosition
- Customer
- Order
- OrderItem
- Payment
- Shipment
- Supplier
- PurchaseOrder
- BusinessEvent

Do not add every realistic retail concept.

The goal is not accounting correctness or ERP completeness.

The goal is to have enough interacting systems for interesting consequences to emerge.

---

# Time

Time is a first-class part of the product.

The user should eventually be able to:

- advance one day
- advance N days
- advance until a condition occurs
- inspect the state at a historical point
- create a branch from a historical point
- inject an event at a chosen time
- compare branches

The initial implementation can use a simple discrete simulation clock.

Real-time execution is unnecessary.

---

# Events

There are two broad classes.

## Normal business events

Examples:

- order placed
- payment completed
- payment failed
- stock reserved
- order shipped
- purchase order created
- supplier delivery completed
- customer cancelled order
- return created

## External / disruptive events

Examples:

- supplier unavailable
- warehouse temporarily unavailable
- warehouse destroyed
- logistics capacity reduced
- demand spike
- payment provider outage
- staff availability reduction
- regional disruption
- epidemic scenario
- war-related disruption
- missile attack scenario
- meteor impact

The simulator is not trying to predict real disasters.

A disruptive event is translated into explicit changes to the simulated world.

For example:

```yaml
event: warehouse_destroyed
warehouse: kyiv-main
effects:
  warehouse_status: destroyed
  inventory_loss: 100%
  outbound_capacity: 0
```

Consequences after that point should come from the simulation rules.

---

# AI role

AI should be useful but not be the hidden physics engine.

Potential AI responsibilities:

- convert natural-language scenarios into structured event definitions
- help generate coherent synthetic business descriptions
- explain why a state emerged
- generate investigation tasks
- give hints during interactive exercises
- summarize differences between timeline branches
- later: generate new supported scenarios from a constrained vocabulary

Bad use:

> "The AI decided revenue dropped because customers became sad."

unless the simulator explicitly contains such a mechanism.

Good use:

> User writes: "The primary warehouse was destroyed and regional logistics were disrupted for two weeks."

AI produces a structured draft:

```json
{
  "events": [
    {
      "type": "warehouse_destroyed",
      "target": "warehouse_main"
    },
    {
      "type": "logistics_capacity_change",
      "region": "primary",
      "capacity_multiplier": 0.35,
      "duration_days": 14
    }
  ]
}
```

The user can inspect or confirm the interpretation.

---

# Zoom / abstraction

The UI should eventually support moving between different questions.

## Business level

Questions:

- Is the business healthy?
- What changed recently?
- Where are the major problems?
- What is different between two branches?

## Subsystem level

Examples:

- inventory
- orders
- payments
- suppliers
- logistics

## Entity level

Example:

- this order
- this product
- this warehouse

## Event / causal level

Example:

> Why is Order #481 delayed?

Possible causal chain:

```text
Order #481 delayed
  <- stock unavailable
  <- replacement stock not delivered
  <- supplier B unavailable
  <- disruptive event on day 94
```

"Zoom" does not have to mean a literal infinite canvas.

The important property is preserving context while changing the level of abstraction.

---

# Long-term branches

The same core may later support several products or modes.

## Developer / QA tool

Generate coherent datasets and reproducible scenarios.

Possible uses:

- demo environments
- test fixtures
- edge cases
- regression scenarios
- reproducible bug worlds

## Interactive learning

The system creates a problem inside the synthetic world and asks the user to investigate it.

Examples:

- "Why are paid orders not shipping?"
- "Why did cancellations spike?"
- "Which intervention reduces losses?"
- "Find the first event that made the system fragile."

## Scenario laboratory

Compare decisions or preparation strategies.

Example:

Branch A:
- keep all inventory in one warehouse

Branch B:
- distribute inventory across two warehouses

Then inject the same disruption and compare the outcomes.

## More complex synthetic worlds

Possible later domains:

- SaaS company
- logistics network
- marketplace
- software delivery organization
- small economy

Do not build these early.

# Open questions

These should remain open until implementation or usage provides evidence.

## Product

- What is the first domain exactly?
- Is the first customer a developer, QA engineer, learner, or the author?
- Is export important in Milestone 1?
- What makes the initial world interesting enough to inspect?
- What metrics are worth showing at business level?

## Simulation

- Fixed daily tick, discrete events, or hybrid?
- How much randomness is desirable?
- Which rules must be deterministic?
- How should causality be represented?
- How large can an early world be?

## Time travel

- Full snapshots?
- Event replay?
- Database copy per branch?
- Copy-on-write?
- When is optimization actually needed?

Do the easiest correct thing first.

## UI / zoom

- What is the highest-level screen?
- What transitions feel natural?
- Should a user navigate by entities, events, or questions?
- How do we preserve context during drill-down?

## AI

- Which first feature materially benefits from an LLM?
- Which model provider?
- Is LangGraph actually useful at that stage?
- What should be evaluated?
- How do we keep inference costs bounded?

## Business

- Is this primarily:
  - a developer tool
  - synthetic data product
  - testing product
  - simulation game
  - educational platform

Do not choose prematurely unless product decisions require it.

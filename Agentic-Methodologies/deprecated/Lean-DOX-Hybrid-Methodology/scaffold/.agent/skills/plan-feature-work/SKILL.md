---
name: plan-feature-work
description: Map a broad area of current specs and implementation into a simple direction of coherent likely increments, dependencies, decisions, risks, and deferred concerns. Use for feature planning without creating tasks, IDs, lifecycle states, or detailed execution records.
---

# Skill: Plan Feature Work

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may maintain `.agent-state/task-handoff.md` as temporary
runtime state outside `.agent/`, as defined in root `AGENTS.md`.

Produce enough planning to guide development while keeping the methodology
informal. Do not create candidate tasks or a formal backlog.

## Required Context

Read:

- root `AGENTS.md`;
- `.agent/specs/CONTEXT.md`, spec map, domain language, and relevant specs;
- `../../../docs/normative/architecture.md`;
- `../../../docs/planning.md`;
- enough code, permitted tests, contracts, docs, configuration, and decisions
  to establish the current baseline and material technical capabilities.

## Planning Discipline

- Treat specs as product intent, not as implementation plans. Do not infer that
  a technical impulse in `docs/planning.md` is a requirement.
- Prefer coherent increments with observable outcomes.
- Split by capability, domain boundary, dependency, risk, or independently
  useful result.
- Distinguish established facts, accepted direction, assumptions, and open
  decisions.
- Do not choose dependencies, services, infrastructure, public contracts, or
  architecture changes without following the selected work mode.
- Keep implementation detail only when it affects feasibility, sequencing,
  scope, risk, or verification.
- Draw on `Technical Design Impulses` as non-normative input. Validate them
  against current code and constraints before recommending or implementing
  them.
- Treat records in `docs/normative/decisions/` as accepted technical direction.
  When planning resolves a consequential technical choice, follow the selected
  work mode, record the decision, and prune redundant impulses.
- Treat order as current guidance, not a permanent commitment.

## Procedure

1. Confirm the desired outcome, planning scope, exclusions, and useful horizon.
2. Establish:
   - intended behavior;
   - behavior already implemented;
   - architecture and technical capabilities;
   - constraints and cross-cutting concerns;
   - verification consequences;
   - assumptions and decisions.
3. Identify remaining behavior and required supporting work.
4. Divide it into a small number of coherent likely increments.
5. Show dependencies, useful order, deferrable work, risks, and verification
   focus.
6. Ask for developer decisions where alternatives materially change the plan.
7. If the resulting plan is large, decide whether to execute it as one change
   or split into ordered, independently reviewable items according to the
   selected work mode. Recommend splitting when it improves reliability,
   reviewability, or execution under reduced reasoning effort.
8. In `SUPERVISED` mode, present the plan conversationally and obtain approval
   before implementation when it is significant or architectural. In
   `AUTONOMOUS` mode, record the decision and continue when implementation is
   in scope.
9. If split execution is chosen under the selected work mode, write the
   accepted active plan to `docs/planning.md` before implementation begins.
   Include the outcome, constraints, ordered items, current item, and
   verification focus.
10. Otherwise update `docs/planning.md` with only the short durable remainder:
   current direction, likely next increments, open decisions, and important
   deferred concerns.
11. Remove stale planning notes made obsolete by the new direction.

## Output

A useful plan normally includes:

- outcome and boundaries;
- current baseline;
- likely increments in current order;
- dependencies and cross-cutting concerns;
- decisions, assumptions, risks, and deferred work;
- recommended next increment.

## Guardrails

- Do not create task directories, IDs, statuses, acceptance tables, or history.
- Do not copy the full conversational plan into `docs/planning.md`.
- The exception is an accepted active multi-item plan needed for item-by-item
  execution; remove it when complete rather than archiving it.
- Do not modify specs from this skill; route intent changes through
  `../update-specs/SKILL.md`.
- Do not begin implementation unless the developer also requested execution.

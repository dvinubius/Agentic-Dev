---
name: planning-audit
description: Audit one bounded relationship among current specs, implementation, docs, and docs/planning.md to find forgotten intent, stale notes, contradictions, or missing decisions. Agent-initiated use must stay focused; broad use follows the selected work mode.
---

# Skill: Planning Audit

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may maintain `.agent-state/task-handoff.md` as temporary
runtime state outside `.agent/`, as defined in root `AGENTS.md`.

Diagnosis is the default. This audit evaluates current planning orientation,
not work-item coverage.

## Mandatory Scope Discipline

Agent-selected scope must be one product area, spec section, implementation
increment, or small set of planning notes.

The developer may explicitly request a broad audit. If the agent believes a
wide audit is needed, explain the evidence, proposed scope, cost, and expected
value, then follow the selected work mode.

## Modes

- `intent-vs-implementation`: compare selected specs with current behavior;
- `stale-planning`: find obsolete or contradicted planning notes;
- `forgotten-intent`: find selected intended behavior absent from both current
  implementation and useful near-term orientation;
- `planning-consistency`: find contradictions among selected specs, planning
  notes, docs, and accepted direction.
- `spec-boundary`: find implementation planning or technical design presented
  as product intent, and product intent misplaced as non-normative planning.

Unimplemented specs are allowed. `forgotten-intent` is a prioritization finding,
not automatically a defect.

## Required Context

- selected mode and scope;
- relevant current specs;
- `../../../docs/planning.md`;
- relevant code, permitted tests, contracts, docs, and decisions.

## Procedure

1. State mode, exact scope, and exclusions.
2. Build a small evidence map across the selected sources.
3. Separate confirmed findings, likely findings, and unknowns.
4. For spec content, apply both product-intent tests:
   - would a product owner assert it without choosing how the product is built;
   - would it remain true if the implementation were replaced.
5. Identify the smallest credible repair:
   - update current specs;
   - implement through `work-on-app`;
   - record an accepted durable technical choice in `docs/normative/decisions/`;
   - move useful implementation reasoning to
     `docs/planning.md` > `Technical Design Impulses`;
   - update or prune other `docs/planning.md` content;
   - update technical docs;
   - obtain a developer decision.
6. Do not edit by default. Apply repairs only when requested or clearly
   included in the active work, and follow the selected work mode for
   high-impact decisions.

When a planning impulse has become an accepted durable decision, promote it to
`docs/normative/decisions/` and remove redundant planning detail. When a
decision is no longer accepted, update its status rather than silently treating
planning as the canonical replacement.

## Output

For each finding, report impact, evidence, confidence, minimal action, and any
developer decision required.

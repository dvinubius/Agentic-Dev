---
name: update-specs
description: Add, revise, remove, or reorganize the repository's current product and business specifications while preserving internal consistency, canonical terminology, and awareness of implementation and planning consequences. This skill maintains no historical snapshots.
---

# Skill: Update Specs

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may maintain `.agent-state/task-handoff.md` as temporary
runtime state outside `.agent/`, as defined in root `AGENTS.md`.

`specs/` contains the current form of intended product and business behavior.
Specs may lead implementation. Git, not a methodology snapshot directory,
provides history.

## Product-Intent Boundary

Include a statement in specs only when both tests pass:

1. a product owner would assert it regardless of how the product is built;
2. swapping the implementation would not change the statement.

The tests apply to requirements, examples, acceptance behavior, glossary
definitions, open questions, and explanatory prose. Product-level constraints
are valid when they pass both tests, even if they narrow technical choices.

Implementation ideas are not spec content. Examples include architecture
candidates, frameworks, libraries, module boundaries, internal schemas,
algorithms, migrations, rollout mechanics, engineering sequencing, and test
strategy. Preserve useful technical reasoning according to its maturity:

- an accepted decision with durable rationale and consequences belongs in
  `docs/normative/decisions/`;
- tentative alternatives, unresolved questions, and near-term implementation
  impulses belong under
  `docs/planning.md` > `Technical Design Impulses`.

Do not create a decision record merely to save every idea. Do not treat an
implementation idea discovered during spec work as accepted without developer
approval or autonomous decision where the selected work mode requires it.

## Work Mode

An explicit request to change specs authorizes drafting the requested current
spec edits. Resolve developer-involvement questions through the selected work
mode when:

- intent is ambiguous or contradictory;
- the change has consequential product, security, privacy, compatibility, or
  data-lifecycle implications not already decided;
- coupled requirements admit materially different outcomes;
- the requested wording would silently change established meaning.
- technical reasoning reaches a choice that would define or change architecture
  boundaries, dependencies, public contracts, migrations, security, privacy,
  operations, or another high-impact area without following the selected work
  mode.

An instruction to update specs authorizes product-intent edits. It does not by
itself authorize accepting consequential implementation decisions.

## Required Context

Read:

- `.agent/specs/CONTEXT.md`;
- `../../../specs/README.md`;
- `../../../specs/domain-language.md`;
- affected specs and materially coupled specs;
- relevant technical docs, code, and `../../../docs/planning.md` when needed to
  understand consequences.

Inspect Git history only when prior wording or rationale is materially relevant.
Do not create `spec-history/` or versioned snapshots.

## Procedure

1. State the intended change, affected area, and known exclusions.
2. Inspect current requirements, terminology, and coupled behavior.
3. Classify each proposed statement as:
   - product intent that passes both product-intent tests;
   - a product-level constraint that passes both tests;
   - a technical design impulse or implementation-planning detail;
   - uncertain and requiring developer clarification.
4. Identify contradictions, ambiguities, and decisions.
5. Resolve high-impact intent through the selected work mode.
6. Edit current spec files consistently using only product intent and valid
   product-level constraints.
7. Route useful technical reasoning:
   - when a technical choice is accepted and its rationale or consequences will
     matter later, record it in `docs/normative/decisions/` and update
     `docs/normative/decisions/README.md`;
   - otherwise keep still-useful alternatives, assumptions, tradeoffs, and
     unknowns in `docs/planning.md` under `Technical Design Impulses`.
   Planning detail may be substantial when that prevents useful reasoning from
   being lost, but it remains temporary and non-normative. Prune it when stale,
   implemented, abandoned, or superseded by a decision record.
8. Update the spec map and domain language when needed. Preserve the structure
   defined by `.agent/specs/templates/README.md` and
   `.agent/specs/templates/domain-language.md`.
9. Check relevant implementation and docs for newly visible divergence.
   Unimplemented intent is allowed; contradictory implemented behavior should
   be reported.
10. Report changed files, consequential meaning changes, implementation
    consequences, technical reasoning routed to decisions or planning, and
    unresolved questions.

## Guardrails

- Do not implement runtime behavior as part of this skill unless the developer
  explicitly asks to continue into `work-on-app`.
- Do not edit root `AGENTS.md`, root `CONTEXT.md`, or anything under `.agent/`.
- Do not copy product intent into nested `AGENTS.md` files.
- Do not preserve historical copies in the repository.
- Do not leave known internal contradictions merely to defer a decision.
- Do not make specs more technical merely to retain reasoning already spent;
  route that reasoning to `docs/normative/decisions/` or `docs/planning.md`
  instead.
- Do not treat technical design impulses as approved plans or architecture.
- Do not record a proposed technical direction as accepted without required
  approval or autonomous decision under the selected work mode.
- Do not duplicate a settled decision indefinitely in both an ADR and planning.
- Do not turn `docs/planning.md` into a requirement backlog.

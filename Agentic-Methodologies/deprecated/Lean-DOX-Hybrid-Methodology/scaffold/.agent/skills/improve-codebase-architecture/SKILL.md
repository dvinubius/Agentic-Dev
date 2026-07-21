---
name: improve-codebase-architecture
description: Find focused opportunities to consolidate tightly coupled shallow modules into fewer deep modules with smaller interfaces and better locality. Use for bounded architecture diagnosis and design before accepted refactoring.
---

# Skill: Improve Codebase Architecture

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may maintain `.agent-state/task-handoff.md` as temporary
runtime state outside `.agent/`, as defined in root `AGENTS.md`.

Surface architectural friction and propose deepening opportunities. A
deepening opportunity moves complexity behind a smaller interface, usually by
combining tightly coupled shallow modules into fewer deeper modules.

The default output is diagnosis and design, not runtime changes.

## Scope

Inspect one bounded codebase area selected by the developer or clearly relevant
to current work. Do not turn the skill into a repository-wide architecture
review without following the selected work mode.

## Work Mode

Changing normative architecture boundaries follows the selected work mode.
When developer input is needed, show the current boundary, proposed boundary,
alternatives, migration consequence, and verification approach.

## Required Context

Read:

- [references/language.md](references/language.md);
- `../../../specs/domain-language.md`;
- `../../../docs/normative/architecture.md`;
- relevant specs and decision records;
- bounded source, contracts, and permitted tests;
- root `AGENTS.md`.

## Process

### 1. Explore

Look for evidence such as:

- understanding one concept requires movement among many small modules;
- interfaces expose nearly as much complexity as implementations;
- pass-through modules add names without hiding complexity;
- tightly coupled modules leak knowledge across boundaries;
- verification targets internals because no useful public surface exists;
- related changes and bugs are scattered across callers.

Apply the deletion test from `references/language.md` and classify dependencies
using [references/deepening.md](references/deepening.md).

### 2. Present Candidates

Follow [references/report-format.md](references/report-format.md). For each
candidate include:

- files and modules;
- current friction;
- proposed consolidation;
- expected leverage and locality;
- verification impact;
- before/after diagram;
- dependency category;
- conflict with accepted decisions;
- recommendation strength.

Prefer a small number of evidence-backed candidates and identify the top one.

### 3. Resolve The Selected Design

For a selected candidate, clarify:

- responsibilities inside and outside the module;
- interface and seam placement;
- dependencies and adapters;
- behavior-preservation strategy;
- permitted interface-level verification;
- migration and sequencing constraints.

Use [references/interface-design.md](references/interface-design.md) when
meaningfully different interfaces should be compared.

### 4. Hand Off

If a direction is accepted or selected under the active work mode:

- record a durable decision only when justified;
- add a short current note to `../../../docs/planning.md` only if implementation will
  not begin immediately;
- implement later or continue through `../work-on-app/SKILL.md`;
- once the technical design is accepted, update normative architecture before
  implementation.

## Guardrails

- Do not equate more abstraction with better architecture.
- Do not create seams for hypothetical variation alone.
- Do not expose internals merely to make verification convenient.
- Do not silently contradict accepted decisions.
- Do not refactor runtime code during the diagnostic pass unless implementation
  was explicitly requested.

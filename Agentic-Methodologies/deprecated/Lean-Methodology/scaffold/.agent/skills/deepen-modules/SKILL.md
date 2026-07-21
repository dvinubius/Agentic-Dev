---
name: deepen-modules
description: Find focused opportunities to consolidate tightly coupled shallow modules into fewer deep modules with smaller interfaces and better locality. Use for bounded architecture diagnosis and design before accepted refactoring.
---

# Skill: Deepen Modules

## Scope

Surface architectural friction and propose deepening opportunities. A
deepening opportunity moves complexity behind a smaller interface, usually by
combining tightly coupled shallow modules into fewer deeper modules.

The default output is diagnosis and design, not runtime changes.

Inspect one bounded codebase area selected by the developer or clearly relevant
to current work. Do not turn the skill into a repository-wide architecture
review without confirmation.

## Developer Approval

Changing normative architecture boundaries requires developer approval.
When developer input is needed, show the current boundary, proposed boundary,
alternatives, migration consequence, and verification approach.

## Required Context

Read:

- [references/language.md](references/language.md);
- `../../../docs/domain-language.md`;
- `../../../docs/normative/architecture.md`;
- relevant decision records;
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

If a direction is accepted:

- record a durable decision only when justified;
- implement later or continue through `../work-on-task/SKILL.md`;
- update architecture boundaries when the accepted change is implemented.

## Guardrails

- Do not equate more abstraction with better architecture.
- Do not create seams for hypothetical variation alone.
- Do not expose internals merely to make verification convenient.
- Do not silently contradict accepted decisions.
- Do not refactor runtime code during the diagnostic pass unless implementation
  was explicitly requested.

---
name: improve-codebase-architecture
description: Find opportunities to consolidate tightly coupled shallow modules into fewer deep modules with smaller interfaces and better locality. Use when the engineer wants architectural improvement, fewer pass-through modules, stronger test surfaces, reduced coupling, or refactoring candidates that make the codebase easier to understand and change.
---

# Skill: Improve Codebase Architecture

Surface architectural friction and propose deepening opportunities. A
deepening opportunity moves complexity behind a smaller interface, usually by
combining tightly coupled shallow modules into fewer deeper modules.

The default output is diagnosis and design, not runtime changes. Convert an
approved candidate into a refactoring task before implementation.

## Methodology Context

A **task** is a repository-tracked development work item.
`../../tasks/CURRENT.md` is the active-task lock. If it names a task, use this
skill only in service of that task; otherwise, do not start an unrelated
architecture review.

An approved architecture change is planned under
`agent/tasks/refactoring/NNN-short-description/` and implemented later through
the task-execution workflow in `../../tasks/CONTEXT.md`.

## Engineer Handoffs

Whenever waiting for engineer confirmation, a decision, approval, review, or
candidate selection, end the response with the explicit question the engineer
must answer. Put it in a separate final paragraph and place no text after it.

## Required Language

Read [references/language.md](references/language.md) and use its architecture
terms consistently. Also read `specs/domain-language.md`,
`docs/architecture/boundaries.md`, relevant specs, and relevant decision
records under `docs/decisions/` so candidate names follow project language,
current boundaries remain explicit, and accepted decisions are not casually
re-litigated.

## Process

### 1. Explore

1. Apply the active-task rule above.
2. Identify the bounded codebase area to inspect.
3. Read relevant domain language, specs, decisions, source, tests, and
   contracts.
   When the area includes frontend behavior, read root `AGENTS.md` and do not
   recommend frontend automated tests if its policy excludes them.
4. Explore organically and note friction:
   - understanding one concept requires bouncing among many small modules;
   - interfaces expose nearly as much complexity as implementations;
   - pass-through modules add names and movement without hiding complexity;
   - tightly coupled modules leak knowledge across their seams;
   - tests target internals because no useful public test surface exists;
   - change, bugs, or knowledge are scattered across callers.
5. Apply the deletion test from `references/language.md` to suspected shallow
   modules.
6. Classify dependencies using
   [references/deepening.md](references/deepening.md).

### 2. Present Candidates

Create a concise architecture review. Prefer a self-contained HTML report in
the OS temp directory when the environment can render it; otherwise use
Markdown. Follow [references/report-format.md](references/report-format.md).

For each candidate include:

- files and modules involved;
- current friction;
- proposed consolidation;
- expected leverage and locality;
- testing impact;
- before/after diagram;
- dependency category;
- conflicts with existing decisions;
- recommendation strength: `Strong`, `Worth exploring`, or `Speculative`.

End with the top recommendation. Do not propose a detailed interface yet. Ask
the engineer which candidate, if any, should be explored.

### 3. Grill The Selected Candidate

For the selected candidate, resolve one design decision at a time:

- responsibilities of the deepened module;
- what remains outside;
- seam placement;
- dependencies and adapters;
- behavior-preservation strategy;
- interface-level tests that should survive internal refactoring;
- migration and sequencing constraints.

Use `clarify-with-shared-language` discipline: recommend an answer, ask one
question at a time, and update permitted planning artifacts as decisions
crystallize.

### 4. Explore Interfaces

If alternative interfaces would materially affect the decision, follow
[references/interface-design.md](references/interface-design.md). Produce at
least three meaningfully different designs sequentially, compare their depth,
locality, seam placement, and tradeoffs, then recommend one.

### 5. Hand Off

If the engineer approves a refactor direction:

- create a new refactoring task through `../create-task/SKILL.md`, or update an
  existing task under `../../tasks/refactoring/CONTEXT.md`;
- record the current and intended structure;
- define observable structural and behavior-preservation criteria;
- link the architecture review and relevant decision records;
- do not implement until task execution begins under
  `../../tasks/CONTEXT.md`.

## Guardrails

- Do not equate more abstraction with better architecture.
- Do not create a seam for a single adapter without a concrete reason.
- Do not expose internal seams merely to make tests convenient.
- Do not preserve shallow-module tests after stronger interface-level tests
  replace them.
- Do not silently contradict an accepted decision.
- Do not refactor runtime code as part of the diagnostic pass.

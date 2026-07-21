---
name: ensure-completeness
description: Check whether the current change, a selected area, or an explicitly requested whole-repository baseline fully handles its declared outcome, including affected paths, evidence, cleanup, docs, planning state, and explicit exclusions.
---

# Skill: Ensure Completeness

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may maintain `.agent-state/task-handoff.md` as temporary
runtime state outside `.agent/`, as defined in root `AGENTS.md`.

Completeness is relative to the declared outcome and baseline. Specs may
intentionally remain ahead of implementation.

## Scope Selection

Use exactly one mode:

- **current change**: completeness of the current implementation increment;
- **selected area**: completeness of a named outcome, feature, subsystem,
  contract, path, or spec section;
- **whole repository**: completeness against an explicitly declared
  repository-wide baseline.

If a standalone developer request does not make the mode, boundary, and
completion baseline clear, ask before inspecting. Do not infer that
"completeness" means either the latest diff or implementation of every spec. A
workflow that invokes this skill may supply the scope explicitly; do not ask
again when it does.

Agent-selected use is limited to current-change mode or a tightly bounded
selected outcome. Whole-repository mode follows the selected work mode. Never
silently expand the scope.

## Inputs

- selected mode, outcome, boundary, and completion baseline;
- explicit non-goals, partial-delivery boundaries, and accepted limitations;
- relevant specs, communicated approach, code, permitted tests, contracts,
  docs, and planning notes.

## Procedure

1. State the mode, boundary, exclusions, and what "complete" means for this
   audit.
2. Build the review set:
   - in current-change mode, start from the diff and intended increment;
   - in selected-area mode, inventory the area's entry points, parallel paths,
     specs, contracts, configuration, tests, docs, and planning notes;
   - in whole-repository mode, inventory top-level product areas, executable
     entry points, specs, contracts, migrations, configuration, tests, docs,
     and active planning claims. Divide the audit into bounded passes and track
     coverage against the declared baseline.
3. Map the selected outcome to affected:
   - entry points and callers;
   - states, variants, and failure paths;
   - data, configuration, contracts, and compatibility;
   - cleanup, migration, or removal work;
   - verification;
   - architecture and integration documentation.
4. Check for partially updated parallel paths, stale names, dead compatibility
   branches, missed configuration, or unhandled states.
5. Distinguish:
   - required now;
   - intentionally excluded;
   - deferred but important;
   - unrelated.
6. Repair small in-scope gaps when authorized.
7. Add only important deferred concerns to `docs/planning.md`; do not create a
   backlog or completion history.

## Output

Report the selected mode and baseline, inventory coverage, completed scope,
gaps repaired, intentional omissions, deferred essentials, unverifiable areas,
and any reason the selected scope cannot honestly be called complete.

Do not classify every unimplemented spec as a completeness gap.

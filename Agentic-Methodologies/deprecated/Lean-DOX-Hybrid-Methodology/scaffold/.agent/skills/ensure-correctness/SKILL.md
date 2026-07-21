---
name: ensure-correctness
description: Check whether the current change, a selected area, or an explicitly requested whole-repository audit behaves correctly against current intent, edge cases, contracts, architecture, security rules, and verification evidence.
---

# Skill: Ensure Correctness

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may maintain `.agent-state/task-handoff.md` as temporary
runtime state outside `.agent/`, as defined in root `AGENTS.md`.

Check that behavior is right, not merely that code compiles.

## Scope Selection

Use exactly one mode:

- **current change**: correctness of the current diff or completed increment;
- **selected area**: correctness of a named behavior, feature, subsystem,
  module, contract, path, or spec section;
- **whole repository**: a systematic correctness audit across the repository.

If a standalone developer request does not make the mode and boundary clear,
ask before inspecting. Do not default to the latest change merely because one
exists. A workflow that invokes this skill may supply the scope explicitly; do
not ask again when it does.

Agent-selected use is limited to current-change mode or one tightly bounded
directly affected area. Whole-repository mode follows the selected work mode.
Never silently expand the scope.

## Inputs

- selected mode, behavior, boundary, and exclusions;
- relevant current specs and stated developer intent;
- code, permitted tests, contracts, docs, and architecture rules;
- relevant normative docs and authoritative external references;
- known exclusions or accepted limitations.

## Procedure

1. State the selected mode, exact boundary, exclusions, and evidence standard.
2. Build the review set:
   - in current-change mode, trace the diff through affected call paths and
     contracts;
   - in selected-area mode, inventory the area's entry points, states,
     integrations, contracts, security boundaries, tests, and relevant specs;
   - in whole-repository mode, inventory top-level subsystems, executable entry
     points, public contracts, data stores and migrations, external
     integrations, security boundaries, and verification suites. Divide the
     audit into bounded passes and track coverage and unverified areas.
3. Establish expected behavior from current intent and repository evidence.
4. Inspect the implementation and relevant call paths.
5. Check relevant:
   - normal behavior;
   - edge cases, invalid input, failure, and recovery;
   - state transitions and data integrity;
   - authorization, privacy, and security;
   - concurrency, idempotency, and ordering where applicable;
   - public contracts and compatibility;
   - external operations and data actually used, internal mappings, ignored
     provider data, unknown-field behavior, version assumptions, timeouts,
     retries, rate limits, and failure translation;
   - architecture boundaries;
   - verification quality and regression risk.
6. Run proportionate permitted checks where useful. After two failed attempts
   with the same verification path or tool, follow the selected work mode
   before investing more effort.
7. Separate confirmed defects, likely risks, and unknowns.
8. Repair small in-scope defects when the active request authorizes edits.
   Follow the selected work mode before a high-impact choice or material scope
   expansion.
9. Re-run affected checks after repairs.

## Output

Report the selected mode and boundary, inventory coverage, findings by impact
with file evidence, consequence, correction or disposition, verification
result, unverified areas, and residual risk. Whole-repository mode must not
claim exhaustive correctness when evidence or coverage is incomplete.

When automated evidence is insufficient, suggest manual scenarios
conversationally when they provide useful evidence.

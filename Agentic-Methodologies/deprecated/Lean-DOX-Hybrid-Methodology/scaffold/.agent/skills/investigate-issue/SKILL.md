---
name: investigate-issue
description: Diagnose a specific bug, regression, or unexpected behavior before committing to a fix. Use when reproduction, expected behavior, cause, affected surface, or regression evidence is uncertain.
---

# Skill: Investigate Issue

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may maintain `.agent-state/task-handoff.md` as temporary
runtime state outside `.agent/`, as defined in root `AGENTS.md`.

The default output is a diagnosis and recommended correction. Continue into
implementation only when the active request and selected work mode authorize
it.

## Required Context

Read:

- root `AGENTS.md`;
- relevant current specs and technical docs;
- affected code, logs, contracts, permitted tests, and configuration;
- normative technical docs when relevant;
- `../../../docs/planning.md` for known related concerns.

## Procedure

1. State the observed behavior, expected behavior, scope, and known evidence.
2. Reproduce or establish the failure as directly as practical.
3. Trace the narrowest credible path through inputs, state, code, dependencies,
   and outputs.
4. Test competing explanations instead of settling on the first plausible
   cause. After two failed attempts with the same diagnostic or verification
   path, stop and ask how to proceed before investing more effort.
5. Identify:
   - root cause or strongest current hypothesis;
   - affected and unaffected paths;
   - regression risk;
   - smallest credible correction;
   - useful permitted verification.
6. Ask for developer input when expected behavior is not established or the fix
   requires a high-impact decision.
7. If implementation is requested and the direction is clear, continue through
   `../work-on-app/SKILL.md`.

## Output

Separate confirmed facts, hypotheses, unknowns, recommended fix, verification
plan, and residual uncertainty.

Do not create task or incident artifacts unless the project independently
requires them.

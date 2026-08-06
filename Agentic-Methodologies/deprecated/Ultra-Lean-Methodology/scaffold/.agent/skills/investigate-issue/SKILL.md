---
name: investigate-issue
description: Diagnose a specific bug, regression, or unexpected behavior before committing to a fix. Use when reproduction, expected behavior, cause, affected surface, or regression evidence is uncertain.
---

# Skill: Investigate Issue

## Scope

The default output is a diagnosis and recommended correction. Continue into
implementation only when the active request authorizes it.

## Procedure

1. State the observed behavior, expected behavior, scope, and known evidence.
2. Reproduce or establish the failure as directly as practical.
3. Trace the narrowest credible path through inputs, state, code, dependencies,
   and outputs.
4. Test competing explanations instead of settling on the first plausible
   cause. After two failed attempts with the same diagnostic or verification
   path, ask before investing more effort.
5. Identify:
   - root cause or strongest current hypothesis;
   - affected and unaffected paths;
   - regression risk;
   - smallest credible correction;
   - useful permitted verification.
6. Ask for developer input when expected behavior is not established or the fix
   requires a high-impact decision.
7. If implementation is requested and the direction is clear, continue into
   the fix directly, keeping to the smallest credible correction and focused
   verification.

## Output

Separate confirmed facts, hypotheses, unknowns, recommended fix, verification
plan, and residual uncertainty.

Do not create task or incident artifacts unless the project independently
requires them.

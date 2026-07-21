---
name: docs-refinement
description: Improve the clarity, organization, navigation, and consistency of implemented-system documentation without changing runtime behavior. Use when application docs are confusing, duplicated, stale, poorly routed, or need focused editorial refinement grounded in code and tests.
---

# Skill: Documentation Refinement

## Work-State Check

A **task** is a repository-tracked feature, issue-fix, or refactoring work
item, not merely an agent prompt. Read `../../tasks/CURRENT.md`. This skill may
run while a task is active only when the refinement is in service of that task.
Otherwise, wait until no task is active.

## Engineer Handoffs

Whenever waiting for engineer confirmation, a decision, approval, or review,
end the response with the explicit question the engineer must answer. Put it in
a separate final paragraph and place no text after it.

## Inputs

- target docs or documentation area;
- desired outcome;
- relevant implementation evidence.

## Procedure

1. Apply the work-state check above.
2. Read `../../../docs/CONTEXT.md` and the selected docs.
3. Inspect code, tests, contracts, or decisions needed to validate behavior
   claims.
4. Identify:
   - ambiguous or outdated wording;
   - duplicated facts with conflicting canonical homes;
   - missing navigation;
   - proposed behavior presented as current;
   - implementation details that obscure useful behavior.
5. Propose a focused edit set.
6. After approval, edit docs only and verify links and claims.
7. Report changed files and any unresolved behavior uncertainty.

## Guardrails

- Do not invent behavior.
- Do not change specs through this skill.
- Do not change runtime behavior.
- Convert discovered behavior defects into formal issue-task proposals through
  `../create-task/SKILL.md`.

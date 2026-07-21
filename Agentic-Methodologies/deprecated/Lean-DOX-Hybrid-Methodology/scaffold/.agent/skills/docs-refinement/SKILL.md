---
name: docs-refinement
description: Improve the clarity, organization, navigation, and consistency of bounded technical project documentation without changing runtime behavior or creating public-facing docs.
---

# Skill: Documentation Refinement

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may maintain `.agent-state/task-handoff.md` as temporary
runtime state outside `.agent/`, as defined in root `AGENTS.md`.

This is editorial work grounded in implementation evidence. It is not a broad
drift audit unless the developer explicitly requests that scope.

## Inputs

- target docs or documentation area;
- desired outcome;
- relevant implementation evidence.

## Procedure

1. State the bounded documentation scope.
2. Read `.agent/docs/CONTEXT.md` and selected docs.
3. Inspect code, permitted tests, executable contracts, schemas, configuration,
   decisions, or authoritative external references needed to validate technical
   claims.
4. Identify:
   - ambiguous or outdated wording;
   - duplicated facts with conflicting canonical homes;
   - missing navigation;
   - planned technical direction presented as accepted or implemented;
   - detail that obscures useful architecture or integration constraints.
5. Edit the focused doc set when requested.
6. If a template-backed file has structural drift, compare it with the
   corresponding read-only template and repair only the live project file.
7. Verify links and claims.
8. Follow the selected work mode before expanding into a broad documentation
   area or recording a high-impact decision.
9. Report changed files and unresolved technical uncertainty.

## Guardrails

- Do not invent technical behavior or external contracts.
- Do not create end-user behavior narratives or public integration
  instructions.
- Do not edit root `AGENTS.md`, root `CONTEXT.md`, or anything under `.agent/`.
- Do not edit nested `AGENTS.md` files unless the requested refinement
  explicitly includes local agent guides.
- Do not change product intent; route that through `../update-specs/SKILL.md`.
- Do not change runtime behavior.
- If a runtime defect is discovered, report it and use
  `../investigate-issue/SKILL.md` or `../work-on-app/SKILL.md` as appropriate.
- Follow the selected work mode before expanding into a broad documentation
  area.

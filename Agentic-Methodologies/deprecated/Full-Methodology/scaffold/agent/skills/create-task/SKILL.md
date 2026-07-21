---
name: create-task
description: Create a repository-tracked feature, issue-fix, or refactoring task with the correct templates, scope, requirements, acceptance criteria, traceability, manual-testing guidance, planning state, and activity entry. Use when the engineer asks to formalize planned development work as a task.
---

# Skill: Create Task

## Methodology Context

A **task** is a repository-tracked development work item with durable scope,
artifacts, progress, evidence, and a lifecycle. A prompt or conversation is
**work**, not automatically a task.

`../../tasks/CURRENT.md` is the active-task lock. Do not create an unrelated task
while it names an active task. Task creation is planning work and does not occupy
the lock unless task execution begins.

This skill creates task artifacts only. It does not start the six-step execution
workflow or change application code.

## Engineer Handoffs

Whenever waiting for engineer confirmation, a decision, approval, or review,
end the response with the explicit question the engineer must answer. Put it in
a separate final paragraph and place no text after it.

## Select The Task Type

| Type | Use when |
|---|---|
| Feature | implementation should move toward intended product behavior authorized by current specs |
| Issue fix | existing behavior is incorrect and should be corrected |
| Refactoring | internal structure should change without an unintended functional behavior change |

If expected product behavior is not established by current specs, stop task
creation and use `../update-specs/SKILL.md`. Resume task creation only after the
required spec change has been accepted.

## Required Context

Always read:

- `../../tasks/CURRENT.md`;
- `../../tasks/CONTEXT.md`;
- `../../../AGENTS.md`, including its frontend automated-test policy;
- the selected type's `CONTEXT.md`, `_template/`, and `ACTIVITY.md`;
- `../../../docs/architecture/boundaries.md`;
- relevant current specs, code, tests, and application docs needed to define
  credible scope and evidence.

The selected type is under one of:

- `../../tasks/features/`;
- `../../tasks/issues/`;
- `../../tasks/refactoring/`.

If a required methodology artifact is absent, report the missing dependency and
ask for direction rather than inventing a replacement.

## Procedure

1. Confirm that `CURRENT.md` permits the requested planning work.
2. Select the task type and explain any non-obvious classification.
3. Inspect enough repository evidence to define the task accurately. Follow the
   selected type's creation rules and planning questions. If the work comes from
   a broad plan, revalidate its technical direction and assumptions against the
   current repository and engineer decisions; do not copy stale or provisional
   choices as settled facts.
4. Determine the next identifier within that task type by inspecting both open
   and `done/` task directories. Use `NNN-short-description`, zero-padded to at
   least three digits, without reusing an identifier. Start with `001` when the
   type has no existing tasks.
5. Copy the selected type's `_template/` into the new task directory.
6. Complete `BRIEF.md` with source references, task-local `REQ-NNN`
   requirements, observable `AC-NNN` acceptance criteria, non-goals,
   constraints, expected verification, relevant areas, risks, and open
   questions.
7. Draft `PLAN.md` only to the degree supported by current evidence. Keep its
   status `missing` or `draft` unless the engineer has explicitly approved it;
   never manufacture approval.
8. Initialize `PROGRESS.md` as planned and not started. Populate the requirement
   and acceptance-criteria columns of traceability; leave later execution
   evidence pending.
9. Initialize `MANUAL-TESTING.md`. When frontend automated tests are excluded
   and the task affects frontend behavior, map affected acceptance criteria to
   concise engineer-run scenarios. Otherwise record the expected manual scope or
   `N/A` with a reason.
10. Add a concise, useful entry to the type's free-form `ACTIVITY.md`. Preserve
   its existing organization and do not edit engineer-maintained content without
   permission. If the task comes from a broad plan in feature `ACTIVITY.md`,
   reference that plan's heading and update the candidate slice to link the
   resulting formal task.
11. Report the task path, classification, scope, unresolved decisions, planning
    status, and whether it is ready for execution step 1.

## Type-Specific Requirements

- For a feature, link the current spec files and headings that authorize the
  behavior and identify behavior intentionally left for later tasks.
- For an issue fix, record observed behavior, expected behavior, reproduction or
  evidence, and credible regression verification consistent with the frontend
  automated-test policy.
- For a refactoring, state the current structural problem, intended before/after
  boundaries, behavior-preservation evidence, and observable structural
  acceptance criteria.

## Guardrails

- Keep one coherent, reviewable change in each task.
- Do not mix feature behavior into an issue fix or refactoring task silently.
- Do not alter current specs from inside this skill; route spec changes through
  `update-specs`.
- Do not set `CURRENT.md`, mark the task `in_progress`, or begin implementation.
- Do not replace unresolved scope or design decisions with guesses.
- Do not inherit a broad plan's provisional technical assumption without
  revalidation and any required engineer decision.

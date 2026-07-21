---
name: planning-audit
description: Audit relationships among current specs, planned tasks, implementation evidence, and the active-task lock. Use to find deprecated tasks, check whether a specific spec is implemented, identify unimplemented specs with no planned task, or detect conflicting concurrent task state.
---

# Skill: Planning Audit

Use for one of these modes:

- `deprecated-tasks`;
- `specific-spec-implementation`;
- `missed-specs`;
- `multitasking`.

Diagnosis is the default. Do not edit specs, tasks, or code until the engineer
approves a repair.

## Methodology Context

A **task** is a repository-tracked feature, issue-fix, or refactoring work
item, not merely a prompt sent to the agent.

`../../tasks/CURRENT.md` is the active-task lock:

- `Current task: none` means no task is being executed;
- a task path means exactly that task owns the current repository workstream.

Open-task briefs and activity files describe planned work. Completed task
directories under `done/` are historical evidence, not open plans.

Candidate slices recorded by `plan-feature-work` in feature `ACTIVITY.md` are
broad planning guidance, not open tasks. In `missed-specs` mode, label matching
slices as broad-plan coverage only; do not count them as formal task coverage.

If `CURRENT.md` names a task, run this audit only in service of that task or
when the engineer explicitly requests diagnosis of conflicting task state.
Otherwise, wait until no task is active.

## Engineer Handoffs

Whenever waiting for engineer confirmation, a decision, approval, or review,
end the response with the explicit question the engineer must answer. Put it in
a separate final paragraph and place no text after it.

## Inputs

- audit mode;
- target spec area, task type, or module;
- optional exclusions.

## Required Context

- `../../../specs/CONTEXT.md`;
- relevant current specs;
- `../../tasks/CURRENT.md`;
- relevant open-task briefs and activity files;
- code, tests, and docs only when the selected mode requires them.

## Procedure

1. Apply the active-task rule above.
2. State the audit scope and exclusions.
3. Build a small evidence map from specs to open tasks and, when needed,
   implementation.
4. Run only the selected mode:
   - deprecated tasks: find open tasks invalidated or materially changed by
     current specs;
   - specific spec implementation: assess whether selected intent is
     implemented and evidenced;
   - missed specs: find selected unimplemented intent with no suitable open
     task, distinguishing broad-plan coverage from formal task coverage;
   - multitasking: find multiple active markers, lock/progress conflicts, or
     more than one in-progress task.
5. Separate confirmed findings, likely findings, and unknowns.
6. Ask the engineer how to resolve conflicts.

## Output

For each finding:

- severity or planning impact;
- spec evidence;
- task or implementation evidence;
- confidence;
- recommended minimal action;
- decision required.

Unimplemented specs are acceptable unless the selected mode is checking
implementation or whether an appropriate open task exists.

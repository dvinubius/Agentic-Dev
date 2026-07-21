# Developer Guide

This file explains how the engineer uses the repository methodology.

## Core Usage

1. Keep product intent current under `specs/` through the `update-specs` skill.
2. Use `plan-feature-work` when broad intended behavior needs an ordered,
   multi-task implementation plan.
3. Create feature, issue, or refactoring tasks through the `create-task` skill.
4. Allow only one task to occupy `agent/tasks/CURRENT.md`.
5. Execute the task through the six checkpoints in
   `agent/tasks/CONTEXT.md`.
6. Review the actual diff and verification evidence.
7. Approve commit handling only after the task record is complete.

Planning can be ahead of implementation. It should not occur concurrently with
an active repository workstream.

Use `.devnotes/` for private development-related notes that agents should
ignore. Do not place project rules, task state, or other required context there.

Use the `update-readme` skill to create or refresh the concise root project
README when project identity, development commands, or top-level docs and specs
navigation changes.

## Useful Requests

```text
Update the specs so that <intended behavior>. Do not implement it.
```

```text
Use the plan-feature-work skill to map <spec area> into ordered candidate
task slices. Do not create the tasks.
```

```text
Create a feature task for <goal>. Do not execute it.
```

```text
Assess and begin execution of <task path>. Stop after step 1 for review.
```

```text
Resume the task in agent/tasks/CURRENT.md from its recorded next action.
```

```text
Run the planning-audit skill in missed-specs mode for <spec area>.
Diagnosis only.
```

```text
Run a targeted drift audit for <module>. Do not edit files.
```

```text
Use the update-readme skill to create or refresh the root README.
```

## Plan Review

Approve a plan only when:

- scope is tight;
- proposed files and boundaries are credible;
- material stack choices and capabilities are established, approved, or clearly
  labeled as assumptions or unresolved decisions;
- the plan accounts for supporting work required by capabilities the intended
  stack does not provide;
- permitted automated tests, manual scenarios, or other checks can verify the
  acceptance criteria;
- no unnecessary architecture or dependency is introduced;
- non-goals remain protected;
- risks and assumptions are explicit.

Mark a plan `Execute with caution` when it is usable but requires extra
attention during implementation.

## Diff Review

Review the actual diff, not just the summary.

- Scope: only the requested problem was addressed.
- Correctness: behavior matches acceptance criteria, including edge cases.
- Architecture: boundaries were preserved; no important layer was bypassed.
- Verification: evidence follows the frontend automated-test policy, and manual
  scenarios cover affected acceptance criteria when frontend tests are excluded.
- Maintainability: names and abstractions are proportionate to the problem.
- Risk: migrations, dependencies, security, and compatibility are understood.
- Omni-Sync: docs, tests/contracts, and code describe the same built behavior.

## Lessons

`LESSONS.md` is optional and primarily engineer-maintained. Use it to capture:

- what worked;
- what the agent misunderstood;
- prompt corrections;
- project guidance to update;
- a skill to add or change;
- a new convention.

Promote only recurring lessons. Leave one-off details in the completed task.

## ChatGPT And Codex

Planning and execution are decoupled, so different tools may be used without
changing the repository process.

Use a reasoning-oriented conversation for:

- architecture options;
- turning rough intent into tasks;
- reviewing plans;
- research and tradeoff analysis;
- methodology improvements.

Use a repo-grounded coding agent for:

- codebase investigation;
- implementation and tests;
- mechanical refactoring;
- verification;
- documentation tied to actual code;
- producing reviewable diffs.

Repository task artifacts, not the choice of interface, preserve continuity.

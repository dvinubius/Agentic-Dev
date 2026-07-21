---
name: code-review
description: Review a task diff against its brief, approved plan, verification evidence, and project rules. Use during verification when required by task risk, when the engineer requests a review, or when diff complexity, uncertainty, or weak verification warrants a structured second pass.
---

# Skill: Code Review

## Methodology Context

A **task** is a repository-tracked development work item. Its standard package
contains:

- `BRIEF.md`: scope, requirements, and acceptance criteria;
- `PLAN.md`: approved implementation approach;
- `PROGRESS.md`: current workflow state and execution evidence;
- `MANUAL-TESTING.md`: engineer-run scenarios and reported results.

Task-execution Step 4 is verification: required checks have run and the current
diff is ready for a structured review.

For this review, **Omni-Sync** means that tests and contracts, code, and
application documentation agree about behavior already implemented. Specs may
be ahead of implementation and are not required to be fully implemented.

Read `../../tasks/CURRENT.md`. If it names an active task, review only that
task. If it says `none`, review another task only when the engineer explicitly
requests it and supplies or identifies the required task artifacts and diff.

## Invocation During Verification

During task-execution Step 4, this skill is:

- required if the task affects security or authorization, persistent data,
  public contracts, migrations, concurrency, or multiple architectural
  boundaries, or if implementation materially deviates from the approved
  plan;
- used if the engineer requests it;
- proposed by the agent if no required condition applies and the current diff's
  size or complexity, implementation uncertainty, or weak verification makes a
  second review pass valuable.

Review is diagnosis-only unless fixes are explicitly approved.

This is a structured second pass by the same agent, not an independent review,
and it does not replace the engineer's diff review.

## Engineer Handoffs

Whenever waiting for engineer confirmation, a decision, approval, or review,
end the response with the explicit question the engineer must answer. Put it in
a separate final paragraph and place no text after it.

## Required Context

- task `BRIEF.md`;
- task `PLAN.md`;
- task `PROGRESS.md`;
- task `MANUAL-TESTING.md`;
- actual diff;
- `../../../AGENTS.md`, including its frontend automated-test policy;
- `../../../docs/architecture/boundaries.md` when code changed;
- relevant specs, code, tests, docs, and architecture decisions.

## Procedure

1. Confirm the reviewed scope and baseline.
2. Inspect the actual diff, not only summaries.
3. Check:
   - correctness and acceptance-criteria coverage;
   - scope creep and unrelated changes;
   - missed edge cases and failure modes;
   - security, privacy, and data-integrity concerns;
   - architecture boundary violations;
   - API, migration, and compatibility risks;
   - meaningful verification gaps under the project test policy, including
     missing or weak manual scenarios where frontend automated tests are
     excluded;
   - maintainability problems with practical impact;
   - Omni-Sync gaps.
4. Exclude style-only comments unless they materially affect understanding,
   correctness, or maintenance.
5. Order findings by severity and cite exact files and lines.
6. State remaining verification gaps or residual risk when no defect is found.
7. Record that the skill ran, why it ran, its findings, and each finding's
   disposition in the task's `PROGRESS.md`.

## Finding Format

- severity;
- concise title;
- file and line;
- why it is a problem;
- triggering scenario or consequence;
- smallest credible correction.

If findings require edits during an active task, return the workflow to the
appropriate earlier step and update `PROGRESS.md`.

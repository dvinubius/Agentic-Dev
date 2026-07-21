# Task Management And Execution

Use this area to govern, plan, execute, resume, and complete formal tasks.
Create new task artifacts through `../skills/create-task/SKILL.md`.

Here, a **task** is a repository-tracked development work item with durable
scope, artifacts, progress, evidence, and a lifecycle. Agent activity requested
through prompts is **work**, not automatically a task.

## Preconditions

Read `CURRENT.md` before any repository-changing work.

- If it names a task, only that task may be advanced.
- If it says `none`, planning, complementary work, or one task execution may
  begin.
- Do not clear the lock merely because a conversation ended.

## Task Type Routing

| Work | Go to |
|---|---|
| Plan broad feature work without creating tasks | `../skills/plan-feature-work/SKILL.md` |
| Create a formal task | `../skills/create-task/SKILL.md` |
| Feature task | `features/CONTEXT.md` |
| Issue-fix task | `issues/CONTEXT.md` |
| Refactoring task | `refactoring/CONTEXT.md` |
| Reusable audit or review | `../skills/CONTEXT.md` |

## Standard Task Package

```text
NNN-short-description/
|-- BRIEF.md
|-- PLAN.md
|-- PROGRESS.md
|-- MANUAL-TESTING.md
`-- LESSONS.md        # optional
```

- Copy the relevant `_template/` files when creating a task.
- Keep intent in `BRIEF.md`, implementation design in `PLAN.md`, and execution
  evidence in `PROGRESS.md`.
- Keep concise engineer-run scenarios and their reported results in
  `MANUAL-TESTING.md`. When root `AGENTS.md` excludes frontend automated tests,
  this file is the required verification plan for affected frontend acceptance
  criteria.
- Move completed tasks to the task type's `done/` directory.
- Update the task type's `ACTIVITY.md` on creation, start, material re-scope,
  completion, or removal.

## Task Creation Governance

Use `../skills/create-task/SKILL.md` for the repeatable creation procedure.
The selected type's `CONTEXT.md` owns its classification, creation rules,
planning questions, and completion requirements. Its `_template/` owns the task
artifact shape.

Every new task must have the standard package, task-local requirements,
observable acceptance criteria, initial traceability, initialized manual-testing
guidance, an honest planning state, and a useful `ACTIVITY.md` entry. Task
creation does not occupy `CURRENT.md` unless execution begins.

## Execution Entry

1. Confirm `CURRENT.md` is `none`.
2. Set it to the selected task path.
3. Set the task status to `in_progress`.
4. Set `PROGRESS.md` current step to step 1.
5. Follow the steps below in order.

## Task Progress Tracking (TPT)

TPT is the durable execution record in the active task's `PROGRESS.md`. It
states the current workflow step and records the evidence, decisions, reviews,
verification, and next action needed to resume or complete the task.

## Six-Step Workflow

| Step | Required work | TPT evidence | Default gate |
|---|---|---|---|
| 1. Plan assessment | Reconcile specs, brief, plan, and current repo | findings, plan edits, approval state | engineer approval |
| 2. Verification preparation | Add/update permitted tests and checks; prepare manual scenarios where needed | evidence paths/checks linked to ACs, manual checklist, lint result | engineer review |
| 3. Implementation | Make the approved scoped changes | changed files, deviations, lint result | engineer review |
| 4. Verification | Run checks and repair task-related failures | commands, results, fixes, risks | review after pass |
| 5. Docs | Update docs and review architecture-boundary impact | doc paths, boundary disposition, lint result, traceability | engineer review |
| 6. Conclusion | Finalize evidence and request commit approval | final report and commit disposition | commit approval |

Update `PROGRESS.md` before every gate.

## Engineer Handoffs

At every review, approval, confirmation, or decision gate, summarize the
relevant status and evidence, then end the response with the explicit question
the engineer must answer. Put the question in a separate final paragraph and
place no text after it.

## Pre-Review Linting

Before requesting engineer review of changes made in step 2, 3, or 5:

- run the applicable lint or non-mutating format-check commands for the files or
  areas changed in that step;
- prefer a focused command when the project supports one;
- repair task-related failures before the handoff;
- if the applicable check is unusually extensive, obtain approval as required
  by `AGENTS.md` before running it;
- record the commands and results in the current step's `PROGRESS.md` notes.

If no applicable lint or format check exists, record that instead. Do not
present the step as ready for review with required lint failures unresolved
unless the engineer explicitly waives the requirement. Step 4 still performs
the broader verification appropriate to the task.

### Step 1: Plan Assessment

- Investigate only; do not edit application code.
- Inspect only context relevant to the task, broadening when coupling requires
  it.
- Reconcile `MANUAL-TESTING.md` with the acceptance criteria and root frontend
  automated-test policy. If the task predates this artifact, create it from the
  selected task type's template.
- When frontend automated tests are excluded, ensure each affected acceptance
  criterion is observable through a credible manual scenario or another
  permitted check.
- Read `../../docs/architecture/boundaries.md` as the current architecture
  baseline. Determine whether the proposed implementation preserves or changes
  those boundaries. If it changes them, describe the intended boundary changes
  explicitly in `PLAN.md` before requesting engineer approval.
- Identify partial implementation, stale assumptions, incompatible plans,
  missing prerequisites, and acceptance criteria that cannot prove the goal.
- Edit `BRIEF.md` and `PLAN.md` where necessary.
- Do not proceed without approved plan status.

### Step 2: Verification Preparation

- Read the frontend automated-test policy in root `AGENTS.md`.
- Prefer permitted automated tests before implementation where feasible.
- Test behavior, not incidental implementation.
- Link every automated test, manual scenario, or other check to acceptance
  criteria.
- If frontend automated tests are `excluded`, do not create or update them.
  Instead, complete `MANUAL-TESTING.md` with lean engineer-run scenarios for the
  affected acceptance criteria.
- If frontend automated tests are `enabled`, use `MANUAL-TESTING.md` only for
  useful manual coverage not credibly provided by automated checks; otherwise
  mark it `N/A` with a reason.
- For structural refactors, use characterization tests, static checks, graph or
  search evidence, build/typecheck, and focused review as appropriate.
- Record why no new test is useful rather than creating a meaningless one.

### Step 3: Implementation

- Follow the approved plan and existing conventions.
- Preserve the current rules in `../../docs/architecture/boundaries.md` except
  where the approved plan explicitly changes them.
- Keep the diff scoped and avoid unrelated cleanup.
- Return to step 1 for material scope or design changes.
- Record changed files and plan deviations.

### Step 4: Verification

- Run narrow checks first, then broaden based on risk.
- Respect the frontend automated-test policy in root `AGENTS.md`. When frontend
  automated tests are `excluded`, do not run them or any combined command that
  includes them.
- Run the project's applicable lint and non-mutating format-check commands
  against the final integrated change. Prefer the standard full-project commands
  when proportionate; otherwise run the broadest credible scope and record what
  was excluded. Obtain engineer approval before unusually extensive checks as
  required by `AGENTS.md`.
- Repair task-related code or permitted automated-test failures until required
  checks pass.
- Ask the engineer to execute applicable `MANUAL-TESTING.md` scenarios and
  record the results they report. A failed or unrun required scenario needs an
  explicit disposition and residual-risk record before conclusion.
- Record unrelated failures with evidence; do not hide or mislabel them.
- After required checks pass, read and run `../skills/code-review/SKILL.md`
  if the task affects security or authorization, persistent data, public
  contracts, migrations, concurrency, or multiple architectural boundaries, or
  if implementation materially deviates from the approved plan.
- Run the skill if the engineer requests it.
- If none of those required conditions applies, propose running the skill if
  the current diff's size or complexity, implementation uncertainty, or weak
  verification makes a second review pass valuable. Explain the reason and wait
  for approval.
- Record whether the skill ran, why it did or did not run, its findings, and
  each finding's disposition in `PROGRESS.md`.
- If review findings require edits, return to the relevant earlier step.

### Step 5: Documentation

- Update `docs/` for behavior actually implemented.
- Review `../../docs/architecture/boundaries.md`. Update it to reflect any
  boundary changes implemented by the current task; otherwise record that it
  was reviewed and no update was needed.
- Update decisions, contracts, or conventions only when changed.
- Do not turn task planning notes into application documentation.
- Complete documentation and traceability evidence.

### Step 6: Conclusion And Commit

- Give every acceptance criterion a final disposition.
- Finalize traceability, change summary, verification, and residual risk.
- Update `ACTIVITY.md`.
- Mark the task `ready_for_commit` and request commit approval.
- Prefer separate commits for task planning and Task Progress Tracking (TPT),
  verification artifacts, implementation, and docs when the task is
  substantial. A small task may use one clearly described commit.
- After approval, move the task under `done/`, set `CURRENT.md` to `none`, and
  include those closure changes in the approved commit set.
- Mark the task completed and record the commit disposition before committing.
- Report resulting commit references after the commit operation.
- If intentionally left uncommitted, record that decision before moving the
  task or releasing the lock.

## Review Overrides

The engineer may explicitly waive a review gate. Record the waiver and its
scope in `PROGRESS.md`.

## Resume Procedure

Read:

1. root `AGENTS.md`;
2. root `CONTEXT.md`;
3. `CURRENT.md`;
4. active `BRIEF.md`;
5. active `PLAN.md`;
6. active `PROGRESS.md`;
7. active `MANUAL-TESTING.md`;
8. only the routed project context needed for the next action.

Continue from `Next action`; do not infer progress from chat alone.

---
name: work-on-task
description: Align with the engineer, create a short-lived PRD, choose direct or issue-based execution, then coordinate review, approval, commit, and final task gates.
---

# Skill: Work On Task

## Current-Task State

Use this workflow for a coherent feature, fix, refactoring, or other
application task. The main agent may create, update, and delete short-lived
runtime artifacts under `.agent-state/current-task/`, including:

- `PRD.md`;
- issue files under `issues/` when issue-based execution is selected;
- concise implementation, issue, test, or review reports when useful.

These files are not repo state, a progress journal, or a substitute for
accepted technical decisions. They must not be committed.

Before continuing direct work, before a later issue, after context compaction,
or whenever context feels stale, reconstruct from:

1. current repository state and relevant source;
2. `git status` and the current diff;
3. `.agent-state/current-task/PRD.md`;
4. `.agent-state/current-task/issues/` when issue-based execution is active;
5. latest concise implementation, issue, test, or review reports.

Do not create permanent task directories, IDs, progress journals, acceptance
tables, manual-testing files, or issue-tracker records unless the engineer
explicitly asks for a separate external workflow.

## Conditional Skill Routing

Use `.agent/skills/CONTEXT.md` for optional skill routing. Do not read optional
skills by default; read one only when its trigger is present and the extra
procedure will reduce guessing or risk.

## Workflow

### 1. Align

Understand the engineer's request through conversation and targeted evidence.
Establish:

- requested outcome and observable behavior;
- scope boundaries and explicit non-goals;
- affected workflows, constraints, and terminology;
- accepted decisions and decisions still requiring approval;
- useful verification evidence.

The engineer's clarifying conversation is the primary source of task intent.

### 2. Draft The PRD

Use `../to-prd/SKILL.md` to create `.agent-state/current-task/PRD.md`.

The PRD summarizes the aligned task intent. It is not a durable product spec,
task tracker, or implementation diary.

Present the PRD to the engineer and ask for approval before choosing direct or
issue-based execution.
If approval changes the technical direction, update the PRD before continuing.

### 3. Choose Execution Mode

After PRD approval, choose direct PRD-backed execution or issue-based
execution. Do not read `../prd-to-issues/SKILL.md` merely to make this
decision.

Use direct execution when the approved PRD describes one coherent change that
the main agent can realistically implement, verify, review, and report in the
current session with less overhead than issue creation and subagent
delegation. This fits work that is small enough for one coherent review unit,
has an understood blast radius, does not need independent issue-worker
context, and would cost more to package for delegation than to execute.

Use issue-based execution when the approved PRD naturally breaks into multiple
reviewable slices, the implementation is risky or noisy enough to benefit from
isolated worker context or a separate review pass, context compaction is a
credible concern, or the engineer explicitly wants delegated execution.

Present the recommended execution mode and practical consequence to the
engineer. If direct execution is approved, skip issue creation and proceed to
direct implementation. If issue-based execution is approved, read
`../prd-to-issues/SKILL.md` and create ordered issue files under
`.agent-state/current-task/issues/`.

Issues must be small enough, and detailed enough, that a write-capable issue
subagent can execute them without the main agent's rich conversation context.
Each issue should include the relevant PRD intent, accepted decisions, scope,
non-goals, stop conditions, and verification expectations.

For issue-based execution, present the proposed issue breakdown to the
engineer. Ask whether granularity, dependencies, and technical direction are
right. Iterate until approved.

### 4. Record Accepted Technical Direction

After PRD and execution-mode approval, create or update accepted decision
records under `docs/normative/decisions/` when the approved task includes
durable technical choices whose rationale or consequences will matter later.

Do this before implementation and commit these ADR changes separately after
engineer approval. Keep current architecture and integration documents accurate
to the current implementation; do not rewrite them to describe future behavior
before the corresponding issue changes the code.

If no durable technical decision needs an ADR, say so and continue.

### 5. Execute Directly Or Execute Issues

For direct PRD-backed execution, the main agent implements the approved PRD,
updates affected normative and non-normative docs as required, runs focused
checks, inspects the actual diff for scope, quality, secrets, and accidental
churn, and asks the engineer for review or approval unless that gate was
explicitly waived or batched. Use a read-only review subagent only when the
final diff is large, risky, or noisy enough to justify the extra overhead. Do
not create local issues merely to obtain review. When the direct implementation
is approved, the main agent creates one coherent task commit unless the
engineer requested a different commit shape.

For issue-based execution, execute exactly one issue at a time. The main agent
orchestrates; it does not perform non-trivial implementation work directly
inside delegated issue scope.

For each issue:

1. Delegate the approved issue to one write-capable issue subagent.
2. Instruct the issue subagent to read the PRD, its issue file, relevant ADRs
   or normative docs, and the routed code/docs it needs.
3. Instruct the issue subagent to implement only that issue, update affected
   normative and non-normative docs as required by its changes, run focused
   checks, and finish with `../finish-issue/SKILL.md`.
4. After the issue subagent reports, the main agent performs a lightweight
   issue acceptance check: issue report completeness, acceptance criteria
   disposition, focused verification status, issue scope and non-goals, and
   obvious unrelated churn.
5. The main agent does not perform a full code review of each delegated issue
   by default. It checks intent-sensitive points itself and asks the engineer
   for review or approval unless the engineer explicitly waived or batched that
   gate.
6. For non-trivial cleanup or repair, send the work back to the issue worker
   with a narrow instruction. The main agent may handle only trivial formatting
   or documentation cleanup directly.
7. When the issue is approved, the main agent creates one commit for that
   issue. Do not commit without required approval.

If evidence invalidates the PRD, issue breakdown, or an accepted decision,
return to alignment with the engineer. Update the PRD, issues, and ADRs as
needed before resuming execution.

### 6. Finish The Task

After direct implementation is approved and committed, or after all approved
issues are accepted, approved, and committed, read and follow
`../finish-task/SKILL.md`.

Final task alignment is owned by the main agent because it retains the richest
context about the PRD and engineer intent. For issue-based execution, delegate
the substantive final review of the integrated task diff to a fresh read-only
review subagent. For direct execution, use a read-only review subagent when the
final diff is large, risky, noisy, or engineer-requested. Do not delegate the
PRD-intent judgment.

Delete `.agent-state/current-task/` only after the final report is
reconstructed and the task is complete, or immediately when the task is
abandoned. Remove `.agent-state/` when empty.

### 7. Report

Before reporting, inspect current repository state and the final diff, then
read the PRD, issue files, issue reports when present, and final verification
summary.

Report:

- PRD outcome and scope completed;
- direct execution outcome or issues completed and their commits;
- important files changed;
- tests created or changed and what they verify;
- verification commands and results;
- checks not run and why;
- manual scenarios worth exercising when automated evidence is insufficient;
- intentional omissions;
- residual risk and unresolved decisions.

## Guardrails

- Do not leave `.agent-state/current-task/` or an empty `.agent-state/`
  directory after completion or abandonment.
- Do not allow more than one write-capable issue subagent to work at a time.
- Do not allow review subagents to edit files.
- Do not allow issue subagents to self-review.
- Do not silently mix unrelated cleanup or features.
- Do not document unimplemented behavior as current behavior.
- Do not conceal failing or unrun checks.

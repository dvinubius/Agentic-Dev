# Developer Guide

This repository uses Ultra Lean agentic development: a developer-steered
workflow built around one task, one short-lived PRD, optional local issues,
and usually one PR.

The installed methodology consists of root `AGENTS.md` and `.agent/`.
`CONTEXT.md` is an optional project-owned glossary.

Temporary task artifacts live under `.agent-state/current-task/` while a task
is active. They are not repo state, are not committed, and are deleted when
the task completes or is abandoned.

## Core Usage

1. Keep repository paths, commands, normative technical docs, and conventions
   current under `docs/`; keep project-specific terminology in `CONTEXT.md`.
2. Start non-trivial work by aligning on the idea. Use the global
   `grill-with-docs` skill when terms, scope, or design choices are unclear.
3. Ask the agent to use `to-prd` to create or update the current-task PRD.
4. Review the PRD yourself. Correct product intent, technical direction,
   scope, non-goals, and verification expectations before implementation.
5. Once the PRD is ready, decide whether direct execution or issue-based
   execution is best. Skip issues for a small coherent PRD. Use
   `prd-to-issues` when the task benefits from reviewable slices.
6. For issue-based work, run one issue at a time with `implement-issue`.
7. For AFK implementation of an approved PRD, explicitly ask for
   `execute-prd-afk` and state which review points are waived.
8. Review each issue result lightly before accepting it.
9. Use `finish-task` only when you want help creating the PR or checking that
   PR changes satisfy the PRD.

Code is the primary authority for what the system currently does. Permitted
tests and executable contracts provide supporting evidence. The repository map
guides navigation; `docs/normative/` and `docs/adr/` record accepted technical
intent.

## Task Artifacts

For non-trivial application work, the agent may create short-lived files under
`.agent-state/current-task/`:

- `PRD.md`: summarizes the aligned task intent, user stories, implementation
  decisions, testing decisions, out-of-scope work, and notes.
- `issues/`: optional ordered issue files detailed enough for issue-sized
  implementation.

These artifacts are temporary planning and execution aids. They are not a
progress journal, task tracker, or durable history.

## Engineering Workflow

1. Idea: align on the outcome and constraints. This is where most cognitive
   effort belongs.
2. PRD: capture the task in `.agent-state/current-task/PRD.md`.
3. Execution mode: after the PRD is ready, choose direct execution for one
   coherent reviewable change or issue-based execution for work that benefits
   from vertical slices.
4. ADRs: record durable accepted technical decisions before they steer
   implementation.
5. Implementation: implement directly or run issues in order, each with
   developer review.
6. AFK implementation: when review points are waived, use
   `execute-prd-afk` to let the agent choose direct or issue-based execution,
   create a feature branch, use subagents efficiently, check final PRD
   alignment, and create the PR.
7. Finish: optionally create a PR and check PRD conformity.

## Issue Review

After an issue agent reports, perform a lightweight acceptance check:

- issue report completeness;
- acceptance criteria disposition;
- focused verification status;
- issue scope and non-goals;
- obvious unrelated churn.

This is not a full code review by default. It is the quick human check that
the issue result is complete enough, bounded enough, and verified enough to
accept, repair, or redirect.

Useful outcomes:

- accept the issue;
- ask for a narrow repair;
- broaden or correct the PRD;
- split follow-up work into another issue;
- stop because the current direction is wrong.

## Normative Docs

Accepted durable technical decisions should be recorded as ADRs when their
rationale or consequences will matter later.

Current architecture and integration docs should stay accurate to the code as
it currently exists. Do not update them to describe planned future behavior
before the corresponding implementation exists.

As implementation changes code, the implementing agent updates affected
normative docs for the behavior that now exists. Directly affected
non-normative docs, such as repository maps, development commands,
conventions, contributor guidance, and README navigation, should also stay
current.

## Confirmation

By default, expect the agent to ask before destructive operations,
deployments, production actions, unusually broad verification, expensive tool
calls, commits, pushes, PR creation when credentials or remote state are
involved, or edits to content marked developer-maintained.

For a specific task, you may explicitly waive review points. That
does not override external tool approvals, sandbox rules, repository policies,
credentials, legal/security constraints, or explicit prompt instructions.

## Explicit Steering

Ultra Lean stays small by relying on you to steer choices that matter for the
current task.

Useful things to state explicitly:

- whether to create issues or implement the PRD directly;
- whether to use `execute-prd-afk` after PRD approval and which review points
  are waived;
- whether to create or run frontend tests, browser checks, or only suggest
  manual UI scenarios;
- whether a simple UI change should be verified by you visually instead of
  spending agent tokens on automated frontend coverage;
- whether to prioritize minimum token use, maximum confidence, or a balanced
  pass;
- whether to use a named skill for deeper review, broader impact analysis, or
  documentation review;
- whether to use `finish-task` or handle the PR manually.

Examples:

```text
Create a PRD for this change. Do not split it into issues yet.
```

```text
Use prd-to-issues. Keep the issues small enough that each one is reviewable in
one commit.
```

```text
Implement issue 002. Do not touch the generated API client; stop and ask if it
needs regeneration.
```

```text
Check whether the PR changes satisfy the PRD, but do not create the PR.
```

```text
The PRD is approved. Use execute-prd-afk, choose direct or issue-based
execution yourself, and pause only for tool approvals or failed verification.
```

## Diff Review

Review the actual diff, not only the summary:

- Does it solve the selected PRD outcome without unrelated work?
- Are issue boundaries respected when issues were used?
- Are important edge cases and failure cases handled?
- Were architecture, validation, authorization, and data boundaries preserved?
- Is verification credible for the risk of the change?
- Which tests were created or changed, did they run, and what were the
  results?
- Are intentional omissions explicit?
- Do architecture and integration docs match the technical implementation?

## Planning Notes

`.devnotes/` is a git-tracked area for developer-only notes. Agents ignore it
during normal work and must not use it as context for execution.

`.devnotes/planning.md` is optional and free-form. Use it to help decide what
work to give the agent next, not as a normative source for the agent. It is
not template-backed, not required for execution, and not automatically
maintained by agent workflows.

When you explicitly ask an agent to create or update a file under
`.devnotes/`, the agent should first confirm that it is allowed to make that
specific exception to the normal `.devnotes/` ignore rule.

## Methodology Upgrades

Upgrade the methodology by replacing:

- root `AGENTS.md`;
- the `.agent/` directory.

Do not replace project-owned `CONTEXT.md`, `docs/`, or `.devnotes/`. If a
methodology upgrade adds or changes a template, reconcile the corresponding
live project file deliberately while preserving project content.

## Conversation Continuity

During an active task, a compacted or resumed conversation reconstructs from
current repository state, `git status`, the current diff,
`.agent-state/current-task/PRD.md`, current issue files when present, relevant
source, and concise reports in the thread. Outside an active task,
reconstruction uses current code, tests, docs, and Git history when needed.

## Skills

Skills are focused procedures under `.agent/skills/`. The agent should read a
skill only when the workflow phase requires it, the developer explicitly
requests it, or the current conditions match that skill's trigger.

### 1. Core phase workflow

- `to-prd`: turn aligned task context into `.agent-state/current-task/PRD.md`.
- `prd-to-issues`: break an approved PRD into optional ordered local issue
  files.
- `execute-prd-afk`: execute an approved PRD with waived review
  points by creating a feature branch, choosing direct or issue-based
  execution, using subagents efficiently, accepting issues lightly, checking
  final PRD alignment, and creating a PR after committed work.
- `implement-issue`: implement one current-task issue from start to finish.
- `finish-task`: optionally create a PR and check whether PR changes satisfy
  the PRD.

### 2. Investigation and impact

- `investigate-issue`: diagnose a specific bug, regression, or unexpected
  behavior before committing to a fix.
- `assess-change-impact`: assess blast radius before a consequential change
  that may affect callers, data, contracts, architecture, security, privacy,
  operations, cost, or external systems.

Global skills:

- `grill-with-docs`: clarify or stress-test plans, designs, and shared
  language while maintaining `CONTEXT.md` and `docs/adr/`.
- [`no-mistakes`](https://github.com/kunchenguid/no-mistakes): review and gate
  completed work before push.

### 3. Documentation

- Project documentation work is routed by `.agent/docs/CONTEXT.md`.

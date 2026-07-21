# Developer Guide

This repository uses a lean agentic development methodology based on
conversation alignment, a short-lived PRD, direct execution for suitably small
tasks, and ordered local issues with sequential subagent execution when
delegation adds value.

The installed methodology consists of root `AGENTS.md`, root `CONTEXT.md`, and
the installed `.agent/` directory. These paths are read-only during normal
project work and can be upgraded together without replacing project-specific
state in `docs/`.

Temporary current-task artifacts live under `.agent-state/current-task/` while
a task is active. They are not repo state, are not committed, and are deleted
when the task completes or is abandoned.

## Core Usage

1. Keep repository paths, commands, canonical terminology, normative technical
   docs, and conventions current under `docs/`.
2. Ask the agent to work on non-trivial features, fixes, or refactoring through
   `work-on-task`.
3. Expect the main agent to align with you, draft a PRD, recommend direct or
   issue-based execution, record accepted ADRs when needed, and either execute
   the PRD directly or orchestrate one write-capable issue subagent at a time.
4. Expect review and approval gates for the PRD, execution mode, issue
   breakdown when used, accepted technical decisions, non-trivial
   implementation results, commits, and final task completion unless you
   explicitly waive or batch those gates.
5. Expect meaningful progress updates, explicit test reporting, and a final
   diff summary.
6. Use the agent to change `docs/normative/`; avoid editing normative technical
   docs manually because agents treat them as accepted technical intent.

Code is the primary authority for what the system currently does. Permitted
tests/contracts provide supporting evidence. The repository map guides
navigation; `docs/normative/` defines accepted technical intent.

## Task Artifacts

For non-trivial application work, the main agent creates short-lived files
under `.agent-state/current-task/`:

- `PRD.md`: summarizes the aligned task intent, user stories, implementation
  decisions, testing decisions, out-of-scope work, and notes.
- `issues/`, when issue-based execution is selected: contains ordered issue
  files detailed enough for subagent execution without the full planning
  conversation.
- optional concise implementation, issue, or review reports when they help the
  main agent preserve context.

These artifacts are temporary planning and delegation aids. They are not a
progress journal, task tracker, or durable history.

Because there is no task handoff file anymore, the developer and agent should
be mindful of context and token quotas. Keep tasks sized so the PRD, selected
execution path, review, and final task check can realistically finish in one
session when possible.

## Normative Docs

Accepted durable technical decisions should be recorded as ADRs before
implementation begins when those decisions are needed to align execution.

Current architecture and integration docs should stay accurate to the code as
it currently exists. Do not update them to describe planned future behavior
before the corresponding issue changes the implementation.

As direct implementation or each issue changes code, the implementer updates
affected normative docs for the behavior that now exists. Near completion, the
main agent separately reviews affected non-normative project docs, such as
repository maps, development commands, conventions, contributor guidance, and
README navigation.

## Confirmation And Delegation

By default, expect the agent to keep you in the loop for consequential product,
scope, architecture, dependency, public contract, migration, security, privacy,
operational, destructive, expensive, or commit-related choices.

The agent should ask:

- before approving a PRD as execution basis;
- before approving direct or issue-based execution;
- before approving the issue breakdown when issue-based execution is selected;
- before recording accepted durable ADRs;
- after non-trivial direct implementation or each non-trivial issue is
  implemented and reviewed;
- before creating commits;
- again when a repair changes application code after the last approved review;
- after two failed attempts with the same verification path, before investing
  more effort.

For a specific task, you may explicitly choose direct execution, delegate
independent issue execution, or batch review gates. This can support unattended
execution, but it does not override
external tool approvals, sandbox rules, repository policies, credentials,
legal/security constraints, or explicit instructions in your prompt.

## Subagents

The main agent owns task intent, PRD alignment, execution-mode selection,
direct execution when selected, issue sequencing when used, review gate
coordination, commits, and final reporting.

Issue workers are write-capable subagents used only for issue-based execution.
Only one issue worker should edit tracked files at a time. An issue worker
implements one approved issue, runs focused checks, updates affected docs, and
finishes with `finish-issue`.

Issue workers do not self-review. For non-trivial issues, the main agent sends
the result to a fresh read-only review subagent or performs the review itself.
Review subagents receive only the PRD excerpt, issue file, relevant ADRs or
normative docs, actual diff, and focused verification results. Their reports
should be concise and findings-first.

For non-trivial cleanup or repair, the main agent sends a narrow instruction
back to an issue worker during issue-based execution. During direct execution,
the main agent may repair within the approved direct scope when the work
remains small and coherent; otherwise it returns to execution-mode alignment.

## Context Hygiene

Current-task artifacts preserve planning decisions, selected execution mode,
and issue delegation context when used, not every attempt. Keep them short and
current.

Subagent reports should normally stay under roughly 100-150 lines unless more
detail is explicitly requested. The main agent should keep only decisions,
findings, verification results, and next actions in the main thread.

## Explicit Steering

Lean stays small by leaving some work-style choices out of the auto-loaded
methodology. When one of those choices matters for the current task, steer it
explicitly in the prompt.

Useful things to state explicitly:

- whether to create or run frontend tests, browser checks, or only suggest
  manual UI scenarios;
- whether a simple UI change should be verified by you visually instead of
  spending agent tokens on automated frontend coverage;
- whether to prioritize minimum token use, maximum confidence, or a balanced
  pass;
- whether to waive or batch review gates for a delegated task;
- whether to prefer direct execution for a small PRD-backed task;
- whether to use a named skill for deeper review, broader impact analysis, or
  documentation review.

Examples:

```text
Make this small UI adjustment. Do not create or run frontend tests; I will
verify it visually.
```

```text
This touches a risky checkout flow. Use browser-driven frontend verification
and report exactly what ran.
```

## Diff Review

Review the actual diff, not only the summary:

- Does it solve the selected PRD outcome without unrelated work?
- Is the selected execution mode still appropriate?
- Are issue boundaries respected when issues were used?
- Are important edge cases and failure cases handled?
- Were architecture, validation, authorization, and data boundaries preserved?
- Is verification credible for the risk of the change?
- Which tests were created or changed, did they run, and what were the results?
- Are intentional omissions explicit?
- Do architecture and integration docs match the technical implementation?

## Planning Notes

`.devnotes/` is a git-tracked area for developer-only notes. Agents ignore it
during normal work and must not use it as context for execution.

`.devnotes/planning.md` is optional and free-form. Use it to help decide what
work to give the agent next, not as a normative source for the agent. It is not
template-backed, not required for execution, and not automatically maintained
by agent workflows.

When you explicitly ask an agent to create or update a file under
`.devnotes/`, the agent should first confirm that it is allowed to make that
specific exception to the normal `.devnotes/` ignore rule.

## Methodology Upgrades

Upgrade the methodology by replacing:

- root `AGENTS.md`;
- root `CONTEXT.md`;
- the `.agent/` directory.

Do not replace project-owned `docs/` or `.devnotes/`. If a
methodology upgrade adds or changes a template, reconcile the corresponding
live project file deliberately while preserving project content.

## Conversation Continuity

During an active task, a compacted conversation reconstructs from current
repository state, `git status`, the current diff,
`.agent-state/current-task/PRD.md`, current issue files when present, relevant
source, and concise implementation, issue, or verification reports. Outside an
active task,
reconstruction uses current code, tests, docs, and Git history when needed.

## Skills

Skills are focused procedures under `.agent/skills/`. The agent should read a
skill only when the workflow requires it, the developer explicitly requests it,
or the current conditions match that skill's trigger. Optional skills are not
loaded eagerly.

### 1. Core task workflow

- `work-on-task`: align with the engineer, create a PRD, choose direct or
  issue-based execution, coordinate review, commit the implementation, and
  finish the task.
- `to-prd`: turn aligned task context into `.agent-state/current-task/PRD.md`.
- `prd-to-issues`: after issue-based execution is selected, break an approved
  PRD into ordered local issue files.
- `finish-issue`: used by an issue worker before returning to the main agent.
- `finish-task`: used by the main agent before declaring a task complete.

### 2. Product intent and terminology

- `clarify-with-shared-language`: resolve ambiguous terminology, overloaded
  concepts, contradictory intent, or material design branches through focused
  questions.

### 3. Investigation, impact, architecture, and review

- `investigate-issue`: diagnose a specific bug, regression, or unexpected
  behavior before committing to a fix.
- `assess-change-impact`: assess blast radius before a consequential change
  that may affect callers, data, contracts, architecture, security, privacy,
  operations, cost, or external systems.
- `deepen-modules`: identify bounded module-deepening
  opportunities before accepted refactoring.
- `neatify-code`: refactor or review bounded code for maintainability while
  preserving behavior, using broad static evidence for routing and codegraph or
  repository-native follow-up for structural understanding where viable.
- `code-review`: review an actual diff or changed-file set for substantive
  defects, risks, and verification gaps.

### 4. Documentation

- Project documentation work is routed by `.agent/docs/CONTEXT.md`.

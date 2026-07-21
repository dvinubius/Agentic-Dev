---
name: prd-to-issues
description: When issue-based execution is selected, break an approved PRD into ordered local issue files that are detailed enough for sequential write-capable issue subagents.
---

# Skill: PRD To Issues

## Current-Task State

The main agent may create or update local issue files under
`.agent-state/current-task/issues/` as short-lived runtime state. These files
are not repo state and must not be committed.

## Purpose

Turn an approved PRD into one or more independently reviewable work chunks
after the main agent has selected issue-based execution. Issues are local
delegation artifacts, not external tracker records.

Do not use this skill merely to decide whether issues are needed. That
execution-mode decision belongs in `work-on-task` after PRD approval.

Each issue must be small enough and detailed enough that a write-capable issue
subagent can execute it without the main agent's rich conversation context.

## Required Context

Read:

- `.agent-state/current-task/PRD.md`;
- relevant code and tests needed to size the work;
- relevant normative docs and accepted decisions.

## Process

1. Gather the already aligned PRD context. Do not restart discovery unless the
   issue breakdown cannot be made safely.
2. Prefer vertical slices: each issue should deliver a narrow complete path
   through the affected behavior and be independently verifiable when possible.
3. Put enabling prefactors first when they make later issues smaller or safer.
4. Draft an ordered issue list with title, blockers, and covered user stories.
5. Ask the engineer whether granularity, dependencies, and technical direction
   are right. Iterate until approved.
6. Write approved issues in dependency order under
   `.agent-state/current-task/issues/`, using names such as
   `001-<short-title>.md`.

## Issue Template

```markdown
# Issue <number>: <title>

## PRD Reference

- PRD: `.agent-state/current-task/PRD.md`
- User stories covered: <numbers or names>

## What To Build

<Concise description of the vertical slice or enabling change. Describe the
end-to-end behavior and the relevant technical direction.>

## Scope

- <Included work.>

## Non-Goals

- <Explicitly excluded work.>

## Implementation Direction

- <Accepted decision, architecture constraint, interface/API/schema direction,
  expected module boundary, or relevant ADR/normative-doc reference.>

## Acceptance Criteria

- [ ] <Observable criterion.>
- [ ] <Observable criterion.>

## Verification

- <Expected tests, commands, manual checks, or evidence.>

## Blocked By

- <Issue number or "None - can start immediately".>

## Stop And Ask If

- <Decision branch, risk, unexpected coupling, failed assumption, or scope
  expansion that must return to the main agent and engineer.>
```

## Guardrails

- Do not create horizontal layer-only issues unless they are necessary enabling
  prefactors.
- Do not leave critical technical decisions implicit when the issue worker
  needs them.
- Do not over-specify implementation details that the issue worker should
  discover locally.
- Do not publish to or modify an issue tracker unless explicitly requested.

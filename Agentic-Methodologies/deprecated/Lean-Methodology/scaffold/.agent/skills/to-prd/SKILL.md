---
name: to-prd
description: Turn the aligned task conversation and targeted repository evidence into a short-lived PRD under .agent-state/current-task/PRD.md.
---

# Skill: To PRD

## Current-Task State

The main agent may create or update `.agent-state/current-task/PRD.md` as
short-lived runtime state. This file is not repo state and must not be
committed.

## Purpose

Create a concise PRD that captures the engineer-aligned task intent before
issue execution. The PRD combines user-facing intent with implementation and
testing decisions for the current task.

Do not publish the PRD to an issue tracker unless the engineer explicitly asks
for that separate workflow.

## Required Context

Use:

- the current conversation with the engineer;
- `docs/domain-language.md`;
- relevant code, tests, contracts, and technical docs already explored;
- relevant normative docs and accepted decisions.

Do not interview the engineer merely to fill every heading. Ask only when a
missing answer would make the PRD misleading or unsafe to execute.

## Process

1. Synthesize the current request and repository evidence.
2. Use canonical project terminology.
3. Prefer existing test seams. When new seams are needed, propose the highest
   useful seam that verifies behavior without excessive implementation detail.
4. Capture accepted implementation decisions. Do not present tentative
   alternatives as decided.
5. Write or update `.agent-state/current-task/PRD.md`.
6. Present the PRD summary and ask the engineer to approve or correct it before
   issue creation.

## PRD Template

```markdown
# PRD: <task title>

## Problem Statement

<The problem or opportunity from the user's or operator's perspective.>

## Solution

<The intended solution from the user's or operator's perspective.>

## User Stories

1. As a <role>, I want <capability>, so that <benefit>.

## Implementation Decisions

- <Accepted technical decision, affected module/interface/contract/schema/API
  shape, or architectural clarification.>

## Testing Decisions

- <Behavior to verify, useful test seam, prior art, and any manual check that
  is intentionally enough for low-risk UI or operational behavior.>

## Out of Scope

- <Explicit non-goal or deferred behavior.>

## Further Notes

- <Constraints, assumptions, references, or unresolved questions.>
```

## Guardrails

- Keep the PRD focused on the current task, not the whole product unless the
  engineer explicitly requested full-app planning.
- Include implementation decisions that are necessary for aligned execution,
  but avoid stale implementation trivia.
- Avoid specific file paths unless they materially help local issue delegation.
- Do not claim an implementation decision is accepted without engineer
  approval or strong conversation evidence.

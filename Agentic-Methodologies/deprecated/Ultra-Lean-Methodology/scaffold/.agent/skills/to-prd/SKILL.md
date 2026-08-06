---
name: to-prd
description: Turn aligned task intent and targeted repository evidence into a short-lived PRD under .agent-state/current-task/PRD.md.
---

# Skill: To PRD

## Current-Task State

The agent may create or update `.agent-state/current-task/PRD.md` as
short-lived runtime state. This file is not repo state and must not be
committed.

## Purpose

Create a concise PRD that captures the developer-aligned task intent before
direct implementation or optional issue creation. The PRD combines
user-facing intent with implementation and testing decisions for the current
task.

Do not publish the PRD to an issue tracker unless the developer explicitly
asks for that separate workflow.

Do not interview the developer merely to fill every heading. Ask only when a
missing answer would make the PRD misleading or unsafe to execute.

## Process

1. Synthesize the current request and repository evidence.
2. Use canonical project terminology.
3. Prefer existing test seams. When new seams are needed, propose the highest
   useful seam that verifies behavior without excessive implementation detail.
4. Capture accepted implementation decisions. Do not present tentative
   alternatives as decided.
5. Write or update `.agent-state/current-task/PRD.md`.
6. Present the PRD summary and ask the developer to approve or correct it
   before implementation or issue creation.

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
  developer explicitly requested full-app planning.
- Include implementation decisions that are necessary for aligned execution,
  but avoid stale implementation trivia.
- Avoid specific file paths unless they materially help local issue
  implementation.
- Do not claim an implementation decision is accepted without developer
  approval or strong conversation evidence.

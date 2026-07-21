# Project Context Router

This repository uses one agent, one active task, routed context, task-local
progress tracking, and Omni-Sync.

## Terminology

- **Task**: a repository-tracked development work item with durable scope,
  artifacts, progress, evidence, and a lifecycle.
- **Work**: activity requested from or performed by the agent, whether prompted
  once or across a conversation.

Do not use "task" merely to mean a prompt or agent assignment.

Omni-Sync means tests/contracts that exist, code, and implementation docs agree
for behavior already built. It does not require automated coverage of every
behavior. Specs may intentionally be ahead of implementation.

## First Check

For any work that may alter code, tests, specs, docs, task artifacts, or
methodology files:

1. read `agent/tasks/CURRENT.md`;
2. if a task is active, work only on that task unless the engineer explicitly
   resolves the conflict;
3. follow the route below.

## Task Routing

| Task | Where to go |
|---|---|
| Plan a broad feature area as ordered future work | `agent/skills/plan-feature-work/SKILL.md` |
| Clarify or stress-test a plan and its terminology | `agent/skills/clarify-with-shared-language/SKILL.md` |
| Create a formal task | `agent/skills/create-task/SKILL.md` |
| Plan, inspect, execute, resume, or complete an existing task | `agent/tasks/CONTEXT.md` |
| See whether a task is active | `agent/tasks/CURRENT.md` |
| Read or navigate product/business specs | `specs/CONTEXT.md` |
| Change product/business specs | `agent/skills/update-specs/SKILL.md` |
| Work on application or implemented-system docs | `docs/CONTEXT.md` |
| Create or update the root project README | `agent/skills/update-readme/SKILL.md` |
| Read current architecture boundaries | `docs/architecture/boundaries.md` |
| Find a reusable agent procedure | `agent/skills/CONTEXT.md` |
| Learn how the engineer should use this system | `agent/how-to.md` |

## Work Categories

| Category | Meaning |
|---|---|
| Planning | specs, broad feature planning, task creation, technical planning, specs/tasks audits |
| Task execution | one formal task through the six-step workflow |
| Complementary | targeted audits, reviews, docs refinement, module deepening |
| Informal | explicitly approved exception for work outside the formal routes |

## Context Rules

- Load only the files and sections needed for the current work.
- Prefer routing tables over prose.
- Read nested `CONTEXT.md` files only when entering their area.
- Read broader specs when excluding them could hide a relevant coupling.
- Store durable state in repository files, not only in chat.

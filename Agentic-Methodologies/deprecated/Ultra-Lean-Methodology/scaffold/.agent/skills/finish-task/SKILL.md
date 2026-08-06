---
name: finish-task
description: Create or update the branch PR and check whether the PR changes satisfy the current-task PRD.
---

# Skill: Finish Task

## Scope

Use this skill when the developer asks for help finishing the task through a
PR. The developer may skip this skill and create the PR or check PRD
conformity manually.

This skill creates a PR from the current branch unless one already exists. If
a PR already exists for the branch, work on that PR.

This skill does not replace issue acceptance, general code review, release
readiness, or broad repository audit. Judge the work from the changes present
in the PR against the PRD.

## Procedure

1. Identify the current branch and whether a PR already exists for it.
2. If no PR exists, create one from the current branch using a title and body
   derived from the PRD, PR changes, and verification evidence.
3. If a PR already exists, use that PR as the work surface.
4. Identify the exact PR change set.
5. Compare the PR change set against the PRD's problem, solution, user
   stories, implementation decisions, testing decisions, and out-of-scope
   items.
6. Report whether the PR appears to satisfy the PRD. List gaps, partial
   delivery, scope drift, or unresolved verification clearly.
7. If PR creation or update is blocked by missing commits, unpushed branch
   state, credentials, remotes, or tooling, report the blocker and the prepared
   PR content.

## PRD Conformity Output

Report:

- PRD satisfaction: `satisfied`, `partially satisfied`, or `not satisfied`;
- important PR changes;
- PRD goals covered;
- PRD goals not covered or explicitly deferred;
- scope drift, if any;
- verification evidence relevant to the PRD;
- checks not run and why;
- PR URL, or why PR creation or update was blocked.

Do not claim the PR satisfies the PRD while an essential PRD goal lacks an
explicit disposition.

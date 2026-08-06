---
name: implement-issue
description: Implement one approved current-task issue from start to finish, including focused checks, documentation updates, diff inspection, and acceptance reporting.
---

# Skill: Implement Issue

## Current-Task State

This skill uses `.agent-state/current-task/PRD.md` and one issue file under
`.agent-state/current-task/issues/` as short-lived runtime state. These files
are not repo state and must not be committed.

## Scope

Implement exactly one approved issue. Do not pull later issues, unrelated
cleanup, opportunistic refactors, or speculative product changes into the
diff.

This is the single issue-tackling skill: it covers issue orientation,
implementation, focused verification, self-check, and final report.

## Stop And Ask

Stop and ask the developer before:

- making a durable technical decision that needs an ADR but is not already
  accepted.

## Procedure

1. Reconstruct the issue intent from the PRD, issue file, accepted decisions,
   and current repository state.
2. Identify the narrow implementation surface and relevant verification path.
3. Implement only this issue.
4. Update ADRs when an accepted durable decision changes. Update normative
   docs when this issue changes accepted architecture or integration contracts.
   Normative docs must describe the code as it now works, not future planned
   behavior.
5. Update directly affected non-normative docs when the issue changes
   commands, repository navigation, conventions, or other project facts.
6. Run focused verification appropriate to the issue.
7. Inspect the actual diff for issue scope, acceptance criteria disposition,
   unrelated changes, accidental churn, secrets, and obvious quality problems.
8. Report the result for developer acceptance.

## Output

Report:

- issue file and title;
- scope completed and any intentional omissions;
- files changed;
- docs updated or why none were needed;
- tests created or changed and what they verify;
- commands or checks run, with pass, fail, or not-run result;
- acceptance criteria status;
- risks, blockers, or questions for review.

Do not declare the issue complete while an acceptance criterion lacks an
explicit disposition.

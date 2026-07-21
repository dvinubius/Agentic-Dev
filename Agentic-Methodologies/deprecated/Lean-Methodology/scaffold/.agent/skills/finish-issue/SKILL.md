---
name: finish-issue
description: Finish one delegated issue by checking scope, docs, focused verification, and reporting concise results for main-agent acceptance.
---

# Skill: Finish Issue

## Scope

Finish only the delegated issue. Do not pull later issues or unrelated cleanup
into the diff.

This skill is used by the issue worker before returning control to the main
agent. It is not a substitute for the main agent's lightweight acceptance
check or the final integrated task review.

## Required Context

Read:

- the delegated issue file under `.agent-state/current-task/issues/`;
- `.agent-state/current-task/PRD.md`;
- relevant ADRs or normative docs named by the issue;
- the actual current diff or changed-file set;
- relevant code, tests, contracts, and docs touched by the issue.

## Procedure

1. Check that the diff stays inside the delegated issue's scope and non-goals.
2. Check that implemented behavior satisfies the issue's acceptance criteria or
   clearly report any partial result.
3. Update normative docs when this issue changed accepted architecture,
   decisions, or integration contracts. Normative docs must describe the code
   as it now works, not future planned behavior.
4. Update directly affected non-normative docs when the issue changed commands,
   repository navigation, conventions, or other project facts.
5. Run focused verification appropriate to the issue. After two failed attempts
   with the same verification path or tool, stop and report rather than
   spending more effort.
6. Inspect the issue diff for unrelated changes, accidental churn, secrets, and
   obvious quality problems.
7. Return a concise report to the main agent.

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

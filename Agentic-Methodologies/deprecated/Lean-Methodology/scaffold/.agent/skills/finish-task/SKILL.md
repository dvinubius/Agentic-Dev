---
name: finish-task
description: Finish a PRD-backed task by checking direct implementation or completed issue commits against the approved PRD, final diff, verification evidence, and remaining documentation needs.
---

# Skill: Finish Task

## Current-Task State

The main agent may update and delete `.agent-state/current-task/` as
short-lived runtime state.

This is the lightweight completion workflow for the overall task. It does not
create a durable task archive.

## Scope

The default scope is the approved PRD, the selected execution mode, the direct
task commit or approved issue set and their commits, and directly affected
behavior, contracts, modules, and docs.

Do not turn completion into a subsystem-wide or repository-wide audit. If
evidence suggests a broad pass is needed, explain the evidence, proposed scope,
cost, and expected value, then ask before proceeding.

## Required Context

Read:

- root `AGENTS.md`;
- `.agent-state/current-task/PRD.md`;
- `.agent-state/current-task/issues/` when issue-based execution was selected;
- the actual current diff and direct task commit or completed issue commits;
- concise implementation, issue-worker, and review reports when present;
- relevant code, permitted tests, contracts, and docs;
- `docs/normative/README.md` and relevant normative docs when code changed.

## Entry Condition

For direct execution, the approved PRD should already be implemented,
reviewed when required, approved according to the selected gates, and
committed. For issue-based execution, all approved issues should already be
executed, accepted by the main agent, approved according to the selected gates,
and committed. If direct scope or an issue is intentionally deferred or
partial, the PRD and final report must say so explicitly.

Completion of a direct diff or all approved issues is not by itself completion
of the task. The main agent must still decide whether the implementation
satisfies the approved PRD.

## Procedure

1. Confirm the approved PRD outcome, selected execution mode, direct or issue
   scope, non-goals, and any explicitly partial delivery from current
   repository state and current-task artifacts.
2. Check that the direct task commit or completed issue commits, taken
   together, satisfy the PRD's stated goals and preserve its non-goals. The
   main agent owns this intent alignment check.
3. If a direct task is still incomplete, repair the gap directly when it still
   fits the approved direct execution mode. If the remaining work no longer
   fits direct execution, return to execution-mode alignment, create approved
   issues, and continue through the issue workflow. If an issue-based task is
   still incomplete even though the delegated issues were completed correctly,
   create a new issue for the remaining PRD gap under
   `.agent-state/current-task/issues/`. Return to the normal sequential issue
   workflow: obtain required engineer approval for the new issue, delegate it
   to a write-capable issue subagent, perform the lightweight issue acceptance
   check, obtain required implementation approval, commit it, and then run
   `finish-task` again. Do not classify this as failed subagent work when the
   earlier issues were correct.
4. Verify that relevant normative docs match the implemented technical
   behavior. Current architecture and integration docs must describe what now
   exists, not future planned behavior.
5. For issue-based execution, delegate the substantive final code review of the
   integrated task diff to a fresh read-only review subagent using
   `../code-review/SKILL.md`. For direct execution, do this when the final diff
   is large, risky, noisy, or engineer-requested. Keep reports concise and
   findings-first. Do not delegate final PRD alignment.
6. Repair only trivial formatting or documentation cleanup directly during
   issue-based finishing. For non-trivial issue-based cleanup or code repair,
   reopen the relevant issue path by sending a narrow instruction to an issue
   worker, then repeat lightweight issue acceptance, approval, and final review
   as needed. During direct finishing, repair within the approved direct scope
   when the work remains small and coherent; otherwise return to execution-mode
   alignment.
7. Run proportionate permitted verification, narrowest useful checks first.
   After two failed attempts with the same verification path or tool, ask
   before investing more effort.
8. Build an explicit test account:
   - test files created or changed;
   - behavior each test verifies;
   - test commands attempted;
   - whether each command passed, failed, or was not run;
   - relevant result or reason;
   - explicit `none` when no tests were created or changed.
9. Review all non-normative project docs affected by the final implementation,
   including repository maps, development commands, conventions, contributor
   guidance, and README navigation. Update them from final repository evidence.
   Do not edit `docs/normative/` in this final documentation step.
10. Inspect the actual final diff for unrelated changes, accidental churn,
   secrets, generated-file edits, and remaining substantive risk.
11. When manual verification would provide useful evidence, suggest a short
    set of scenarios in conversation. Do not create a repository worksheet.
12. Reconstruct the final report from the repository, final diff, PRD, issues,
    commit list, and concise verification or review reports. Then delete
    `.agent-state/current-task/` and remove `.agent-state/` when empty before
    declaring completion.

## Output

Report:

- PRD outcome and scope completed;
- direct execution outcome or issues completed, including commit identifiers
  when available;
- findings and repairs;
- tests created or changed, their purpose, whether they ran, and their
  results;
- commands or checks run and their results;
- checks not run and why;
- suggested manual verification scenarios when applicable;
- intentional omissions and deferred concerns;
- residual risk.

Do not say the task is complete while a required check is failing or an
essential PRD goal lacks an explicit disposition.
Do not treat a completed direct diff or complete issue set as sufficient when
final PRD alignment shows remaining required work.
Do not leave `.agent-state/current-task/` or an empty `.agent-state/`
directory after completion or abandonment.

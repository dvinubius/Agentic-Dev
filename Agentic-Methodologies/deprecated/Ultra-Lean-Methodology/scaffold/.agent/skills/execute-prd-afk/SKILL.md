---
name: execute-prd-afk
description: Execute an approved current-task PRD end to end with minimal developer involvement. Use only when the developer has approved the PRD and explicitly asked for AFK execution or waived the normal review points.
---

# Skill: Execute PRD AFK

## Scope

Use this skill only after the developer has approved
`.agent-state/current-task/PRD.md` and explicitly asked for AFK execution or
waived the normal review points.

This skill is for executing the approved PRD efficiently. It does not override
tool approvals, sandbox rules, repository policies, credential limits,
security constraints, or explicit developer instructions.

## Procedure

1. Confirm the current branch. If it is not already an appropriate feature
   branch for this PRD, create one before editing, using the repository's
   branch naming convention or a concise task-derived name. Do not create
   task commits on the default branch.
2. Read the completed execution plan implied by current-task state. If issue
   files exist, planning has already chosen issue-based execution. If no issue
   files exist, planning has already chosen direct PRD execution. Do not use
   this skill to revisit whether the PRD should have been split.
3. Follow the planned execution shape by default, but treat issue files as
   execution guidance rather than a binding implementation order. When the PRD
   is one cohesive product flow, shared UI surface, or tightly coupled
   integration path — when end-to-end coherence is the main risk — the main
   agent may bypass issue boundaries, combine issues, or work horizontally.
   If deviating from the planned issue structure, state the concrete reason
   before continuing, keep the PRD as the authority, and use the issue files
   as tracer bullets for final PRD alignment.
4. Use subagents by default for multi-issue AFK execution so the main agent
   keeps its context focused on orchestration, issue acceptance, commits,
   final integration, and PRD alignment. Prefer subagents for independent
   reading, investigation, review, and implementation slices with clear
   boundaries. Do not split write work across subagents when coherence is the
   main risk. If subagents are skipped for multi-issue execution, state the
   concrete reason before continuing. Do not run more than one write-capable
   issue subagent against tracked files at the same time.
5. After each issue result, perform a lightweight issue acceptance check:
   acceptance criteria disposition, focused verification status, scope and
   non-goals, obvious unrelated churn, and unresolved risks.
6. Choose a coherent commit shape for the completed work. One commit per
   accepted issue is allowed when it improves reviewability, but it is not
   required. A single task commit is allowed when the work is tightly coupled
   or reads better as one complete PRD implementation. In all cases, commits
   must be reviewable and traceable back to the PRD and any existing issue
   tracer bullets.
7. After direct execution or all issues are complete, perform a lightweight
   PRD-level conformity pass, not a second issue review. Map the PRD's goals,
   user stories, implementation decisions, testing decisions, and out-of-scope
   items to the completed issue reports, commits, final diff, and verification
   evidence. Check only for PRD coverage gaps, cross-issue integration gaps,
   scope drift, and partial or deferred scope that needs explicit disposition.
   A required PRD test may not be silently deferred; failing or unrun required
   tests block final alignment unless they are explicitly dispositioned.
8. After all issue work or direct work is committed and final PRD alignment is
   complete, use `finish-task` to create or update the PR and report PRD
   conformity against the PR change set.

## Output

Report:

- selected execution mode and why;
- whether the planned issue structure was followed or intentionally changed;
- feature branch used;
- direct result, issues completed, or intentional work reorganization,
  including commit identifiers when available;
- final PRD alignment status;
- verification performed and checks not run;
- `finish-task` PRD conformity status;
- PR URL, or why `finish-task` was blocked;
- scope deferred, risks, or follow-up needed.

Do not claim the PRD is complete while an essential PRD goal lacks an explicit
disposition.

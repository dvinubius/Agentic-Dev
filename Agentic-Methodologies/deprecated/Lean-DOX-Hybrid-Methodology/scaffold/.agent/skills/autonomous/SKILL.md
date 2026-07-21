---
name: autonomous
description: Apply AUTONOMOUS work mode, where the agent makes methodology-level decisions without interim developer review and preserves context hygiene for multi-step work.
---

# Skill: Autonomous Mode

## Mode Contract

Use this skill when the developer explicitly requests `AUTONOMOUS` mode.

In AUTONOMOUS mode, the agent may make methodology-level decisions that would
normally require interim developer review in `SUPERVISED` mode. It should not
stop for plan approval, phase confirmation, post-implementation review, or
high-impact methodology decision gates. Instead, make the best decision from
repository evidence, continue the work, and report important decisions,
tradeoffs, verification, and residual risk at the end.

AUTONOMOUS mode does not override external tool approvals, sandbox rules,
repository policies, credentials, legal/security constraints, or explicit
developer instructions.

Nested `AGENTS.md` files remain mutable project-owned local guides in this
methodology. AUTONOMOUS mode may decide whether to create, refresh, or skip
guide updates when the active skill authorizes local-guide maintenance, but it
does not allow editing root `AGENTS.md`, root `CONTEXT.md`, or installed
methodology under `.agent/` during normal project work.

## Context Hygiene

The main agent is the decision thread and single writer. It owns task intent,
developer communication, final decisions, source, test, configuration,
project-doc edits, authorized nested-guide edits, the canonical handoff, and
the final report. Do not run multiple main agents or concurrent writers
against the same repository.

Use disposable subagents, when available, to quarantine noisy work such as test
runs, log analysis, broad code search, external-documentation lookup, failure
analysis, and large-diff review. Multiple read-only subagents may run
concurrently when their work supports the same coherent outcome. This does not
violate the one-coherent-line-of-work rule.

Give each subagent a narrow question, explicit scope, and requested output
shape. Subagents:

- do not make product, scope, architecture, local-guide, or final
  implementation decisions;
- do not intentionally edit tracked repository files or
  `.agent-state/task-handoff.md`;
- keep raw logs and bulk findings out of the main conversation;
- return conclusions, evidence, commands and results, files inspected, and
  unresolved questions;
- keep reports under roughly 100-150 lines unless explicitly asked for more.

Use a bounded report with: purpose and scope; result (`Pass`, `Fail`,
`Partial`, or `Blocked`); commands and outcomes; key findings; relevant files
inspected; any incidental files generated or changed; and the recommended next
action.

If subagents are unavailable, keep noisy output out of durable context by
retaining only concise findings and verification summaries. Do not use
self-compaction or remembered transcript detail as the primary phase-handoff
mechanism.

## Working Rules

- Keep the work on one coherent line of intent.
- Read applicable nested `AGENTS.md` chains before editing project files.
- Use `.agent-state/task-handoff.md` for non-trivial multi-phase work when
  durable phase state becomes useful.
- Make and record decisions at phase boundaries instead of asking for interim
  confirmation.
- Prefer reversible, scoped implementation choices when evidence is incomplete.
- Stop only when continuing would violate external constraints, explicit
  developer instructions, or a required tool approval that cannot be obtained
  autonomously.

## Final Report

Report the completed outcome, important decisions made without interim review,
files changed, verification performed, local-guide updates or no-change
dispositions when relevant, checks not run, documentation updates, residual
risks, and any follow-up that still needs a developer decision.

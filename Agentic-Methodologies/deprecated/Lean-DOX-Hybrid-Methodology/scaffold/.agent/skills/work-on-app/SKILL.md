---
name: work-on-app
description: Investigate, plan, implement, verify, and document a coherent feature, bug fix, or refactoring in one conversational workflow under the selected AUTONOMOUS or SUPERVISED mode.
---

# Skill: Work On App

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may create, update, and delete
`.agent-state/task-handoff.md` as temporary runtime state outside `.agent/`.

Use one adaptive workflow for a feature, fix, or refactoring. Apply it under
the selected work mode:

- `AUTONOMOUS`: read `../autonomous/SKILL.md` and make methodology-level
  decisions without interim review gates.
- `SUPERVISED`: read `../supervised/SKILL.md` and stop at the review and
  approval gates defined there.

Do not create task directories, IDs, progress journals, acceptance tables, or
manual-testing files.

## Required Context

Read:

- root `AGENTS.md` and `CONTEXT.md`;
- the selected mode skill, either `../autonomous/SKILL.md` or
  `../supervised/SKILL.md`;
- `.agent/local-guides/CONTEXT.md` and every applicable nested `AGENTS.md` on
  the path to the likely edit area;
- `.agent/docs/CONTEXT.md` and `.agent/specs/CONTEXT.md` as relevant;
- `docs/planning.md`;
- relevant current specs and `specs/domain-language.md`;
- relevant code, permitted tests, contracts, and technical docs;
- `docs/normative/README.md` and relevant normative documents when technical
  design may be affected;
- relevant decision records and conventions.

Load only what is needed, broadening when a real coupling requires it.

For non-trivial multi-phase work, read an existing
`.agent-state/task-handoff.md` and verify it against current repository state
and the current diff. If none exists, create it when the first meaningful phase
boundary is reached.

## Workflow

### 1. Orient

Inspect repository evidence before committing to an approach. Establish:

- requested outcome and observable behavior;
- current behavior and likely cause or implementation point;
- scope boundaries and explicit non-goals;
- relevant architecture, contracts, and constraints;
- useful verification evidence;
- assumptions and decisions.

Use the selected mode's context-hygiene and developer-involvement rules while
gathering evidence.

### 2. Frame The Work

Tell the developer concisely:

- your understanding of the outcome;
- the intended approach;
- likely files or boundaries affected;
- verification strategy;
- decisions or risks that require attention.

Classify the plan:

- **Small and straightforward**: local, low risk, easily reversible, and no new
  or changed architecture boundary. The agent may continue after presenting the
  approach.
- **Significant**: materially changes application code, crosses multiple areas,
  has meaningful behavioral or compatibility risk, or would be expensive to
  unwind.
- **Architectural**: defines or changes responsibilities, ownership, dependency
  directions, shared interfaces, or cross-cutting boundaries.

In `SUPERVISED` mode, present significant or architectural plans for approval
before editing application code. In `AUTONOMOUS` mode, record the decision and
continue.

If the plan is large, decide whether to split it into ordered,
independently reviewable items according to the selected mode. If split
execution is chosen:

1. define the outcome, constraints, ordered items, and verification focus;
2. write the accepted or autonomously selected plan to `docs/planning.md`;
3. identify one current item;
4. begin only that item.

The active plan exists to support reliable straightforward execution,
including with reduced reasoning effort. It is temporary coordination, not a
formal backlog.

Once the technical design is accepted under the selected mode, update affected
normative architecture, decision records, and integration contracts before
application-code implementation. Record the accepted semantics and constraints
that can responsibly be settled at this point; implementation-specific paths,
fixtures, and verification references may be filled in as the implementation
establishes them. Keep tentative alternatives in `docs/planning.md`; do not
present them as accepted technical intent. A small change with no durable
technical-design impact needs no normative-doc edit.

Before implementation begins, update `.agent-state/task-handoff.md` with the
goal, scope, decisions, constraints, intended change, and verification focus.

### 3. Implement

- Keep the change coherent and scoped.
- Follow existing conventions and normative technical docs.
- Add or update proportionate automated verification where allowed.
- Make local reversible decisions consistent with the communicated approach.
- Report meaningful discoveries or deviations while working.

If evidence invalidates the approach materially, return to framing the work.
Settle the revised design under the selected mode and update affected normative
docs before resuming implementation. Local factual refinements that do not
change accepted intent may be recorded as implementation establishes them.

For a split plan, implement only the current item. Keep `docs/planning.md`
current and do not silently pull later items into the diff.

At the end of a meaningful implementation slice, update the handoff with the
current diff summary, observable outcome, changed files, and unresolved issues.

### 4. Review The Implementation

After changing application code as planned:

1. run only inexpensive focused checks needed to avoid presenting an obviously
   broken diff;
2. summarize changed behavior, files, deviations, tests created or changed, and
   preliminary check results;
3. in `SUPERVISED` mode, ask the developer to review and approve the
   implemented code; in `AUTONOMOUS` mode, continue to final verification and
   report the review-relevant summary at the end.

In `SUPERVISED` mode, do not proceed to final verification, non-normative
documentation, or conclusion until the developer approves, unless the
developer explicitly waives this gate or approves batching several small items
under one review.

Before final verification, reconstruct the phase from current repository state,
the actual diff, the handoff, and concise preliminary-check reports. Do not rely
on remembered exploration transcript.

### 5. Finish

For non-trivial changes, read and follow `../finish-change/SKILL.md`.

Delegate test execution, failure analysis, and large-diff review to bounded
read-only subagents when useful. Keep only commands, outcomes, relevant
findings, and next actions in the main context and handoff.

Check applicable nested `AGENTS.md` files through `ensure-docs-matched`.
Update them only when the change altered local scope, entry points,
constraints, protected paths, verification, or child-guide routing.

Suggest concise manual verification scenarios conversationally when useful. Do
not write a manual-testing worksheet.

Whether performed through `finish-change` or directly for a trivial change,
the final documentation step reviews all non-normative project docs affected
by the completed implementation, including but not limited to the repository
map, development commands, and applicable local agent guides. Update them from
final repository evidence. Do not edit `docs/normative/` in this step.

Update `docs/planning.md` only for information useful beyond the conversation:
open decisions, important deferred concerns, likely next increments, or intent
known to remain ahead. Remove stale notes rather than recording history.

For a split plan, mark the current item complete, select the next item only
after the current one is concluded, and follow the selected mode before
proceeding. In `SUPERVISED` mode, each item's post-implementation review still
applies unless the developer approved batching.

### 6. Report

Before reporting, inspect current repository state and the final diff, then
read the handoff and latest concise verification summary. Delete
`.agent-state/task-handoff.md` only after the task is complete and the final
report has been reconstructed. Also delete it when the task is explicitly
abandoned. On abandonment, also remove normative changes introduced solely for
the abandoned design while preserving independently accepted technical intent.
Remove `.agent-state/` when empty.

Report:

- behavior and important files changed;
- every test file created or changed and what it verifies;
- whether each relevant test or test command ran, with pass, fail, or not-run
  status and the actual result;
- when no tests were created or changed, state that explicitly;
- verification commands and results;
- manual scenarios worth exercising when automated evidence is insufficient;
- intentional omissions;
- residual risk and unresolved decisions;
- planning notes added, changed, or removed;
- local agent guides updated, or why no guide update was required when relevant.

## Guardrails

- Do not edit root `AGENTS.md`, root `CONTEXT.md`, or anything under `.agent/`.
- Only the main agent may maintain `.agent-state/task-handoff.md`.
- Do not allow subagents to intentionally edit tracked repository files or the
  handoff.
- Do not leave `.agent-state/task-handoff.md` or an empty `.agent-state/`
  directory after completion or abandonment.
- Do not silently mix unrelated cleanup or features.
- Do not treat `docs/planning.md` as a task record.
- Do not document unimplemented intent as current behavior.
- Do not claim completeness beyond the selected scope.
- Do not conceal failing or unrun checks.
- After two failed attempts with the same verification path or tool, follow the
  selected work mode before spending more effort.

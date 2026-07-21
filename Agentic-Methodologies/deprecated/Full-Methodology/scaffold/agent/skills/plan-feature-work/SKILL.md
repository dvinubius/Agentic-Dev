---
name: plan-feature-work
description: Map a broad area of current product specifications into an ordered implementation plan made of coherent candidate task slices, accounting for material current or intended stack capabilities without creating formal tasks. Use when the engineer explicitly asks to plan a substantial feature area, subsystem, API, or other multi-task body of intended behavior.
---

# Skill: Plan Feature Work

## Methodology Context

A **task** is a repository-tracked development work item with its own directory,
brief, plan, progress, evidence, and lifecycle.

This skill produces **candidate slices**: provisional chunks of future feature
work. A candidate slice is not a task and has no task ID, task directory,
task-local requirements, acceptance criteria, approval state, or execution
state. Later, `../create-task/SKILL.md` may convert one candidate slice into a
formal task after revalidating its scope against the current repository.
Any likely task type recorded in the broad plan is advisory until that
formalization.

The broad plan is planning work. Store it as a named free-form section in
`../../tasks/features/ACTIVITY.md`; do not create a separate plan file.

Broad planning may include intended implementation stack and other technical
direction when they materially affect feasibility, candidate-slice boundaries,
dependencies, ordering, risk, or verification. Such details are inputs to the
plan, not automatically permanent architecture decisions.

This skill is primarily engineer-requested. The agent may propose it when a
requested feature area clearly spans several coherent tasks, but must wait for
approval before running it.

## Preconditions

Read `../../tasks/CURRENT.md`. Run this skill only when it says
`Current task: none`, unless the engineer explicitly resolves the conflict with
an active task.

If a required methodology artifact is absent, report the missing dependency and
ask for direction rather than inventing a substitute.

## Engineer Handoffs

Whenever waiting for engineer confirmation, a decision, approval, acceptance,
or review, end the response with the explicit question the engineer must
answer. Put it in a separate final paragraph and place no text after it.

## Required Context

Read:

- `../../../AGENTS.md` for the established project stack and commands;
- `../../../docs/architecture/boundaries.md` for normative current
  architecture boundaries;
- `../../../specs/CONTEXT.md`, `../../../specs/README.md`, and
  `../../../specs/domain-language.md`;
- all current specs in the requested planning scope and any materially coupled
  specs;
- `../../tasks/features/CONTEXT.md`;
- `../../tasks/features/ACTIVITY.md`;
- relevant open and completed feature tasks to avoid duplicate planning;
- enough code, tests, contracts, and application docs to distinguish already
  implemented behavior from remaining work;
- relevant manifests, lockfiles, framework configuration, infrastructure
  configuration, and architecture decision records needed to establish current
  or intended technical capabilities;
- relevant issue or refactoring tasks when they constrain sequencing.

Specs define intended behavior, but may be ahead of implementation. Existing
implementation evidence establishes the planning baseline; it does not override
accepted specs.

## Planning Heuristics

- Prefer coherent, reviewable slices that deliver or enable observable behavior.
- Split by capability, domain boundary, dependency, or independently verifiable
  outcome rather than by arbitrary file count or endpoint count.
- Account for stack capabilities that materially change the work. A capability
  provided by the intended stack may collapse or remove a supporting slice; a
  missing capability required to meet the specs may create one.
- Label each material technical detail as established, engineer-approved for the
  plan, provisional assumption, or unresolved decision. Never present an
  unapproved preference as settled.
- Prefer feature slices. If repository evidence shows that an enabling
  refactoring or issue fix is genuinely required, identify it as a separately
  typed supporting candidate instead of hiding it inside feature scope.
- Keep hard prerequisites explicit. Do not invent foundation work without
  repository evidence that later slices require it.
- Order slices by dependencies, risk reduction, and useful incremental progress.
- Separate cross-cutting concerns from slice-specific work and show where each
  concern first becomes necessary.
- Cover the selected spec scope without silently omitting requirements or
  assigning the same behavior to several slices.
- Include implementation detail only to the level needed to justify feasibility,
  boundaries, dependencies, order, risk, or verification. Formal task planning
  will reassess the current codebase and assumptions later.

## Procedure

1. Confirm the planning scope, desired outcome, exclusions, and useful planning
   horizon with the engineer.
2. Apply the active-task precondition.
3. Build a compact baseline:
   - relevant intended behavior;
   - behavior already implemented and evidenced;
   - existing open or completed tasks;
   - established stack and available technical capabilities;
   - the frontend automated-test policy and its verification consequences;
   - approved choices, provisional assumptions, and unresolved stack decisions
     that could alter the plan;
   - known architecture, data, security, compatibility, and operational
     constraints.
4. Identify remaining spec coverage, materially coupled work, and technical
   capabilities required to meet the intended outcomes. Distinguish capabilities
   supplied by the intended stack from capabilities that require explicit work.
5. Divide the remaining work into candidate slices using the planning
   heuristics. Merge slices that are too dependent to review independently, and
   split slices that combine unrelated outcomes or excessive risk.
6. Order the slices and state hard dependencies, optional sequencing choices,
   and work that can be deferred.
7. Check the plan for spec coverage, duplication, missing prerequisites,
   oversized slices, hidden stack dependencies, and contradictions with existing
   tasks.
8. Present unresolved product or architectural decisions to the engineer. Route
   changes to accepted intent through `../update-specs/SKILL.md`; do not resolve
   them by rewriting specs inside this skill. Ask for an engineer decision when
   competing stack choices would materially change the plan.
9. After the engineer accepts the broad plan, add or update its named section in
   `../../tasks/features/ACTIVITY.md`.
10. Report the activity heading, accepted scope, candidate-slice count, first
    likely task candidate, unresolved decisions, and deferred work.

## Activity Output

Use the existing free-form organization of `ACTIVITY.md`. A broad plan should
contain the useful parts of this shape:

```markdown
## Broad Plan: <name>

### Outcome And Scope

### Current Baseline

### Technical Direction And Assumptions

| Area | Technology or capability | Status | Planning consequence |
|---|---|---|---|

### Spec Coverage

| Spec area | Current state | Candidate slice | Notes |
|---|---|---|---|

### Ordered Candidate Slices

| Order | Candidate slice | Likely task type | Outcome | Spec sources | Depends on | Verification focus |
|---|---|---|---|---|---|---|

### Cross-Cutting Concerns

### Decisions, Risks, And Deferred Work

### Task Creation Guidance
```

Adapt or omit headings when the existing activity structure communicates the
same information more clearly. Preserve engineer-maintained content.

## Guardrails

- Do not create task directories, allocate task IDs, or populate task templates.
- Do not mark candidate slices planned, active, blocked, completed, or approved
  as if they were formal tasks.
- Do not modify specs, application code, tests, contracts, or docs.
- Do not choose or add a dependency, framework, service, or infrastructure
  component without engineer approval.
- Do not use low-level implementation detail that does not affect the broad
  plan.
- Do not treat `ACTIVITY.md` as the sole canonical record for an adopted durable
  architecture decision; identify any follow-up documentation needed.
- Do not treat broad-plan order as permanent. Reassess each slice when it becomes
  a formal task.
- Do not create duplicate candidate slices for work already covered by a
  suitable open task; reference that task in the broad plan instead.

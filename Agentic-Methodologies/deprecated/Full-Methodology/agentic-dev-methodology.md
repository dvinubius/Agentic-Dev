# Agentic Development Methodology

## 1. Purpose

This methodology is for software projects in which:

- product and business requirements live in the repository;
- one engineer remains the strategist and final decision maker;
- one coding agent works on one line of work at a time;
- planning may be ahead of implementation;
- everything already implemented must remain internally consistent.

The repository is both the software workspace and the durable coordination
surface. Chat history is useful working context, but it is not the source of
truth for task scope, progress, verification, or project rules.

The reusable files for this methodology are under `Methodology/scaffold/`.

## 2. Vocabulary

Throughout this methodology:

- **task** means a repository-tracked development work item;
- **work** means activity requested from or performed by the agent, whether
  initiated by one prompt or several.

Do not use "task" merely to mean a prompt, conversation, or agent assignment.

### Task

A task describes a planned repository change and has durable scope, artifacts,
progress, evidence, and a lifecycle. There are three task types:

- feature;
- issue fix;
- refactoring.

### Work

Work is any activity the engineer asks the agent to do. Work may be:

- planning;
- task execution;
- complementary work;
- an explicitly approved informal change.

### Task Progress Tracking (TPT)

TPT is the durable execution record in a task's `PROGRESS.md`. It states the
current workflow step and records evidence produced at each step.

### Omni-Sync

Omni-Sync means that the parts of the repository describing and proving the
system already built agree with each other:

```text
tests and contracts <-> code <-> implementation documentation
```

Specs describe intended behavior and may be ahead of implementation. Therefore,
unimplemented specifications are not automatically Omni-Sync defects.
Omni-Sync requires consistency among tests and contracts that exist, code, and
implementation docs; it does not require automated test coverage of every
behavior. Verification completeness is governed separately by project policy,
task acceptance criteria, and recorded evidence.

## 3. Core Rules

### 3.1 Single Thread

Use one task at a time and one agent at a time.

`agent/tasks/CURRENT.md` is the task lock:

- `Current task: none` means task execution or complementary work may begin;
- a task path means that task owns the repository workstream;
- do not start unrelated planning, execution, complementary, or informal work
  while the lock is occupied;
- a paused conversation does not release the lock.

Planning may drift ahead of execution because the backlog can contain many
planned tasks. It does not imply simultaneous work.

### 3.2 The Engineer Is In Control

The agent investigates, proposes, edits, verifies, and reports. The engineer:

- chooses product direction;
- approves scope and important tradeoffs;
- reviews each execution checkpoint unless review is explicitly waived;
- decides how to resolve spec/task conflicts;
- reviews the actual diff;
- approves commits.

The agent should challenge contradictions or unsafe plans directly, but it
should not silently replace the engineer's strategy with its own.

### 3.3 Repository Artifacts Over Chat Memory

Durable information belongs in the repository:

- project rules in `AGENTS.md`;
- routing in `CONTEXT.md` files;
- intended product behavior in `specs/`;
- actual implementation behavior and decisions in `docs/`;
- task intent in `BRIEF.md`;
- technical design in `PLAN.md`;
- execution state and evidence in `PROGRESS.md`;
- reusable procedures in `agent/skills/`.

### 3.4 Context Is Routed, Not Bulk-Loaded

Use `CONTEXT.md` files as directory maps and routing layers.

- Start with root `AGENTS.md`, then root `CONTEXT.md`.
- Follow only the route relevant to the requested work.
- Load only the files and sections needed.
- Prefer routing tables over long prose.
- Read a nested `CONTEXT.md` only after entering its area.
- It is acceptable to read broader specs when excluding them would risk
  missing an important coupling.

There should normally be one root `AGENTS.md`. Nested behavior is expressed
through `CONTEXT.md` files and skills rather than additional `AGENTS.md` files.

`CONTEXT.md` and skills have different responsibilities:

- `CONTEXT.md` owns durable routing, area boundaries, invariants, canonical
  paths, and governing rules that apply whenever the area is entered;
- a skill owns a bounded, repeatable procedure that benefits from explicit
  triggers, ordered steps, guardrails, and a defined output;
- a `CONTEXT.md` may route to or require a skill, and the skill must explicitly
  load the governing context and templates it depends on;
- templates define artifact shape, while task and project files hold durable
  state.

Do not move a large governing lifecycle into a skill merely because parts of it
repeat. Package procedures such as spec changes or task creation as skills when
their scope and completion condition are clear, while keeping the full
task-execution lifecycle in its governing `CONTEXT.md`.

### 3.5 Planning Before Known Intent Is Implemented

Do not implement known business intent unless it is already represented in:

1. the relevant specs; and
2. an explicit task.

The exception is a trivial change or an informal change explicitly approved by
the engineer after the agent points out that it bypasses the preferred process.
Even then, Omni-Sync remains mandatory.

### 3.6 Explicit Engineer Handoffs

Whenever the agent stops because it needs engineer confirmation, a decision,
approval, or review:

1. summarize the relevant status and evidence first;
2. end the response with the explicit question the engineer must answer;
3. put that question in a separate final paragraph;
4. place no text after the question.

Do not leave the required action implicit or end only with a passive status
statement such as "This revision awaits acceptance." Ask directly, for example:

```text
Do you accept the revised spec set so I can create snapshot v0002?
```

## 4. Work Categories

### 4.1 Planning

Planning includes:

- creating or changing specs;
- mapping a broad spec area into ordered candidate task slices;
- creating feature, issue, or refactoring tasks;
- preparing or refining technical plans;
- auditing specs and tasks.

Planning is deliberately more flexible than execution. It does not require the
six execution checkpoints, but it must preserve consistency and ask for
decisions where intent is ambiguous.

### 4.2 Task Execution

Task execution implements one task through the ordered workflow in section 9.
It produces code, permitted verification artifacts, documentation, and
task-local evidence.

### 4.3 Complementary Work

Complementary work improves or checks the repository without executing a
feature, issue, or refactoring task. The initial scaffold includes:

- planning audit;
- drift audit;
- documentation refinement;
- clarify with shared language;
- improve codebase architecture;
- code review.

Complementary work may be diagnosis-only or may produce changes. It must not
run while a task is active, except when a skill is explicitly invoked as a
sub-check of that active task, such as code review during verification.

### 4.4 Informal Work

For a non-trivial change outside a task and outside an applicable agent skill,
the agent must:

1. state that a formal task is the preferred route;
2. ask the engineer to confirm proceeding informally;
3. if confirmed, use task-like rigor proportionate to risk;
4. keep existing tests, code, contracts, and implementation docs synchronized;
5. report verification and residual risk.

Trivial edits may proceed directly, but must not create known drift.

## 5. Repository Structure

```text
repo/
|-- README.md
|-- AGENTS.md
|-- CONTEXT.md
|-- specs/
|   |-- CONTEXT.md
|   |-- README.md
|   |-- domain-language.md
|   |-- <domain-oriented spec files>
|   `-- spec-history/
|       `-- README.md
|-- agent/
|   |-- how-to.md
|   |-- tasks/
|   |   |-- CONTEXT.md
|   |   |-- CURRENT.md
|   |   |-- features/
|   |   |-- issues/
|   |   `-- refactoring/
|   `-- skills/
|       |-- CONTEXT.md
|       `-- <skill>/SKILL.md
|-- docs/
|   |-- CONTEXT.md
|   |-- app-behavior/
|   |-- architecture/
|   |   `-- boundaries.md
|   |-- decisions/
|   `-- conventions.md
|-- src/
`-- tests/
```

The exact application directories are project-specific. The methodology
directories and their responsibilities should remain recognizable.

## 6. Root Control Files

### 6.1 `AGENTS.md`

Keep `AGENTS.md` short, stable, and project-specific. It should contain:

- project summary and stack;
- a compact map of stable, high-value repository paths;
- development and verification commands;
- coding and documentation standards;
- a pointer to the normative architecture boundaries in
  `docs/architecture/boundaries.md`;
- behavioral rules for the agent;
- actions that require approval and actions that are never allowed;
- the informal-work confirmation rule;
- a required pointer to root `CONTEXT.md`.

Do not put the full methodology in `AGENTS.md`.

Its verification guidance should require checks proportionate to the change:
straightforward local checks run implicitly, while unusually extensive checks
require a justification and engineer approval. Its safety rules should protect
pre-existing work and sensitive values, distinguish approval-required actions
from absolute prohibitions, and require credible alternate evidence when no
useful automated test is feasible.

Development commands should identify the command working directory, declared
toolchain and package manager, required local services, focused and full test
commands, relevant static checks, build command, and a canonical combined
verification command when the project has one. Remove entries that do not
apply.

`AGENTS.md` must declare the repository's frontend automated-test policy as
`enabled` or `excluded`. Frontend automated tests include browser, unit, and
integration tests whose primary subject is frontend behavior.

- When `enabled`, the normal task workflow creates and runs proportionate
  frontend tests.
- When `excluded`, the agent does not create, update, or run frontend automated
  tests and must not run a combined command that includes them. Tasks use
  `MANUAL-TESTING.md` for acceptance-criteria-linked engineer scenarios and
  reported results instead.

This policy does not waive backend tests, contracts, static analysis,
typechecking, linting, builds, or other non-frontend verification.
It is repository-wide and must not be silently overridden by an individual
task.
When an existing repository changes to `excluded`, the engineer must explicitly
decide what happens to existing frontend tests and commands. The flag does not
silently authorize deletion, and dormant tests must not be represented as
maintained verification.

The coding and documentation standards should require Tailwind CSS for styling
and prohibit introducing CSS Modules or CSS-in-JS.

The approval rules should require the agent to present a migration plan and
obtain approval before changing the database schema or creating or applying
migrations.

The agent must update the repository map when current work changes a stable,
high-value path or its responsibility, without adding transient or
task-specific paths. It must update the development-command section when
current work changes the supported toolchain, command names, working directory,
required services, or verification workflow. It must also use the
`update-readme` skill to keep the root README's duplicated development commands
synchronized.

### 6.2 Root `CONTEXT.md`

Root `CONTEXT.md` explains the operating model briefly and routes:

- root README creation and maintenance to the `update-readme` skill;
- spec navigation to `specs/CONTEXT.md` and spec changes to the `update-specs`
  skill;
- broad feature planning to the `plan-feature-work` skill;
- task creation to the `create-task` skill and existing-task planning or
  execution to `agent/tasks/CONTEXT.md`;
- application documentation work to `docs/CONTEXT.md`;
- current architecture boundaries to `docs/architecture/boundaries.md`;
- reusable agent procedures to `agent/skills/CONTEXT.md`.

For any request that may alter code, tests, specs, or docs, it first routes the
agent through `agent/tasks/CURRENT.md`.

### 6.3 Root `README.md`

Root `README.md` is the concise human-facing entry point to the repository. It
should:

- describe the project and architecture in no more than a few sentences;
- state that the repository uses the agentic development methodology and
  follows its repository-layout conventions;
- link to `specs/README.md`, selected relevant application documentation,
  `docs/architecture/boundaries.md`, and `agent/how-to.md`;
- include current development commands mirrored from `AGENTS.md`.

The README links to canonical sources rather than repeating specs, architecture
rules, decisions, or application documentation. `AGENTS.md` remains
authoritative for development commands, so command changes require README
synchronization through the `update-readme` skill.

## 7. Specifications

### 7.1 Role Of Specs

`specs/` is the canonical description of intended product and business
behavior. Specs are not required to describe how every requirement is
implemented.

Use natural-language headings. Do not force a global requirement-ID scheme.
Keep canonical project-specific terminology in `specs/domain-language.md`.

### 7.2 Spec Organization

Organize specs hierarchically by product area or independently understandable
domain. Prefer focused files, with roughly 300 lines as a useful signal rather
than a hard limit.

Do not split a spec when doing so would hide important coupling. `specs/README.md`
acts as the map and should identify cross-cutting relationships.

### 7.3 Spec Change Rules

Use the `update-specs` skill for the repeatable change procedure. The governing
rules remain:

Every accepted spec change must:

1. keep the current spec set internally consistent;
2. update the spec map where needed;
3. create a complete accepted snapshot in `specs/spec-history/`;
4. scan open tasks for requirements that were removed or changed;
5. present conflicts to the engineer rather than silently rewriting or deleting
   affected tasks.

A full snapshot may be a versioned directory that mirrors the current spec set.
The history format must preserve enough information to reconstruct the accepted
version.

Normally, the live spec set is the latest accepted version, so the agent should
not read the latest snapshot merely to duplicate the same context. During a
spec update, the live files may temporarily contain a proposed revision that
has not yet been accepted. Read the latest relevant accepted snapshot only when
needed to:

- distinguish the last accepted baseline from pending or uncertain live edits;
- recover an interrupted spec update;
- understand intent that was removed or materially changed;
- inspect historical rationale relevant to the requested change.

Snapshot creation remains mandatory after acceptance even when no historical
snapshot was read during the update.

### 7.4 Planning Audits

The `planning-audit` skill supports four targeted checks:

- deprecated tasks: open tasks invalidated by current specs;
- specific spec implementation: whether a selected requirement is implemented;
- missed specs: unimplemented requirements with no planned task;
- multitasking: more than one active task or inconsistent active-task markers.

An unimplemented requirement is not itself a defect. It becomes a planning
finding when it lacks an appropriate task or conflicts with task state.
Candidate slices in a broad feature plan do not count as open tasks. A planning
audit may report them as broad-plan coverage, but the requirement remains
without formal task coverage until `create-task` creates the task artifacts.

## 8. Task Model

### 8.1 Task Types

#### Feature Task

Moves the implementation toward intended product behavior. It must point to the
relevant spec files and headings.

#### Issue Task

Fixes incorrect existing behavior. It describes reproduction or observed
evidence and links relevant specs where applicable.

#### Refactoring Task

Changes internal structure because technical requirements or architectural
pressure justify it. It must state the architectural problem and intended
structural outcome. Functional behavior should remain unchanged unless
explicitly included in scope.

### 8.2 Task Directory

Each task is a directory:

```text
agent/tasks/features/NNN-short-description/
agent/tasks/issues/NNN-short-description/
agent/tasks/refactoring/NNN-short-description/
```

Each task directory contains:

```text
|-- BRIEF.md
|-- PLAN.md
|-- PROGRESS.md
|-- MANUAL-TESTING.md
`-- LESSONS.md        # optional, primarily maintained by the engineer
```

This split keeps stable intent, editable technical planning, and execution
evidence separate:

- `BRIEF.md`: what and why;
- `PLAN.md`: how;
- `PROGRESS.md`: where execution is and what evidence exists;
- `MANUAL-TESTING.md`: lean engineer-run verification scenarios and reported
  results;
- `LESSONS.md`: durable observations to consider after the task.

Completed task directories move under the type's `done/` directory. Do not move
a task until completion evidence is recorded and commit handling is resolved.

### 8.3 Task Brief

`BRIEF.md` includes:

- task metadata and status;
- goal and background;
- source spec references or issue/refactor motivation;
- task-local requirements, named `REQ-001`, `REQ-002`, and so on;
- non-goals and constraints;
- acceptance criteria, named `AC-001`, `AC-002`, and so on;
- expected verification;
- relevant files or directories;
- risk areas;
- open questions.

Task-local requirement IDs restate only the relevant spec meaning. They do not
replace headings in the canonical specs.

### 8.4 Technical Plan

`PLAN.md` includes:

- plan status: missing, draft, approved, or needs reassessment;
- codebase findings;
- proposed implementation;
- files and boundaries likely to change;
- verification strategy;
- the applicable frontend automated-test policy and manual-verification impact;
- documentation impact;
- ordered implementation steps;
- architecture considerations;
- risks, assumptions, and unresolved decisions;
- engineer approval record.

A planning task may be handed to execution with a missing or imperfect plan. A
plan may be marked `Execute with caution`. Execution cannot pass step 1 until
the agent has reconciled and the engineer has approved a viable plan.

### 8.5 Task Progress Tracking

`PROGRESS.md` is the resumable state. It includes:

- task status;
- current workflow step;
- last completed checkpoint;
- next expected action;
- a six-step status table;
- step notes and review decisions;
- traceability;
- changed-file summaries;
- pre-review lint results;
- verification results;
- engineer-reported manual-testing results and their dispositions;
- documentation changes;
- completion report and residual risk.

Update it before every review handoff and before ending a conversation that has
made progress.

### 8.6 Activity Files

Each task type has an `ACTIVITY.md` for the engineer's broader view:

- task order and grouping;
- short task descriptions;
- current progress and perspective;
- broader implementation intent and plans;
- links to related planning artifacts where useful.

Update it when tasks are created, started, completed, removed, or materially
re-scoped.

Activity files are free-form. They may use prose, lists, links, tables, or
headings as useful, but the methodology does not prescribe fixed lifecycle
sections. Content marked as engineer-maintained must not be silently changed.
If it appears stale, ask before editing it.

For broad implementation plans, feature `ACTIVITY.md` may include intended
implementation stack, platform capabilities, libraries, infrastructure, and
other technical direction when they materially affect:

- feasibility of meeting the specs;
- candidate-slice boundaries or the need for supporting work;
- dependencies and ordering;
- risk or verification strategy.

Label each material technical detail as established in the project,
engineer-approved for the plan, a provisional planning assumption, or an
unresolved decision. State its planning consequence. Do not present an agent
preference as an accepted choice.

`ACTIVITY.md` is allowed to hold this planning context, but it does not replace
canonical project configuration, the stack summary in `AGENTS.md`, the
normative boundaries in `docs/architecture/boundaries.md`, or an appropriate
decision record for a durable adopted architecture choice.

### 8.7 Broad Feature Planning

Use the `plan-feature-work` skill when a substantial area of accepted specs
needs an implementation plan spanning several future feature tasks. The skill
records the plan directly in `agent/tasks/features/ACTIVITY.md`.

The plan maps specs and current implementation to ordered **candidate slices**.
A candidate slice is planning guidance, not a formal task: it has no task ID,
task directory, task-local requirements, acceptance criteria, approval state,
or execution state. The broad plan should show:

- selected scope and current implementation baseline;
- established and intended technical capabilities, with decision status and
  planning consequences;
- coverage of the relevant specs;
- coherent candidate slices, likely task types, and intended outcomes;
- ordering, hard dependencies, and optional sequencing;
- cross-cutting concerns, risks, decisions, and deferred work;
- guidance for which candidate should become a task next.

The skill must not create task artifacts or modify accepted specs. Later,
`create-task` revalidates one candidate slice against the then-current
repository, stack, and planning assumptions, then turns it into a formal task.
Broad-plan order is useful guidance, not a permanent execution commitment.

### 8.8 Task Creation

Use the `create-task` skill to create a feature, issue-fix, or refactoring task.
The skill selects and loads the task type's governing `CONTEXT.md`, copies its
template, creates task-local requirements and acceptance criteria, initializes
traceability, planning state, and `MANUAL-TESTING.md`, and updates the free-form
activity file.

Task creation is planning work. It does not occupy `CURRENT.md`, start the
six-step execution workflow, or authorize implementation. If the intended
behavior is not established by current specs, stop task creation, update and
accept the required spec change, and only then resume task creation.

## 9. Execution Workflow

Execution always follows these steps unless the engineer explicitly approves a
different path for the task.

Before requesting engineer review of changes made during steps 2, 3, or 5, run
the applicable lint or non-mutating format-check commands for the files or
areas changed in that step. Prefer focused commands when available, repair
task-related failures, and record commands and results in `PROGRESS.md`. If no
applicable check exists, record that instead. Unusually extensive checks require
the approval described in `AGENTS.md`. Do not present the step as ready for
review with required lint failures unresolved unless the engineer explicitly
waives the requirement. Step 4 still performs broader task verification.

Every review, approval, confirmation, or decision handoff follows the explicit
engineer-handoff rule in section 3.6. The response must end with the question
the engineer needs to answer, as a separate final paragraph with no text after
it.

### Entry Preconditions

Before step 1:

1. read `agent/tasks/CURRENT.md`;
2. confirm no other task is active;
3. validate that the selected task directory exists;
4. set `CURRENT.md` to the task path;
5. set `PROGRESS.md` status to `in_progress` and current step to step 1.

### Step 1: Assess And Approve The Implementation Plan

Investigate without changing application code.

Reconcile:

- relevant specs;
- the task brief;
- the existing technical plan;
- `MANUAL-TESTING.md` and the root frontend automated-test policy;
- current code, tests, docs, and architecture;
- `docs/architecture/boundaries.md` as the current architecture baseline.

If a task predates `MANUAL-TESTING.md`, create it from the selected task type's
template during this step.

When frontend automated tests are excluded, ensure each affected acceptance
criterion is observable through a credible manual scenario or another
permitted check.

Determine whether the proposed implementation preserves or changes the current
boundaries. If it changes them, describe the intended boundary changes
explicitly in `PLAN.md` before requesting engineer approval. The current
boundaries remain normative outside that approved change.

Look only for discrepancies relevant to the task's scope. Examples:

- behavior is already partly implemented;
- the reported issue no longer reproduces;
- a planned data field does not exist;
- the proposed plan violates an existing boundary;
- acceptance criteria cannot prove the stated goal.

Update `BRIEF.md` or `PLAN.md` where needed, record the assessment in
`PROGRESS.md`, then ask the engineer to review and approve the plan.

Do not proceed to step 2 without approval.

### Step 2: Prepare Verification

Read the frontend automated-test policy in root `AGENTS.md`. Prepare the
permitted evidence that will verify the approved acceptance criteria.

- Prefer permitted automated tests before implementation when feasible.
- Link every automated test, manual scenario, contract, static check, or other
  verification artifact to acceptance criteria in traceability.
- Keep automated tests focused on behavior rather than incidental
  implementation.
- When frontend automated tests are `excluded`, do not create or update them.
  Complete `MANUAL-TESTING.md` with lean engineer-run scenarios for affected
  frontend acceptance criteria.
- When frontend automated tests are `enabled`, use `MANUAL-TESTING.md` only for
  useful manual coverage not credibly provided by automated checks; otherwise
  mark it `N/A` with a reason.
- For a refactor with no useful new automated test, record the existing tests,
  static checks, structural checks, or manual evidence that will prove behavior
  preservation and structural completion.
- Do not invent low-value tests merely to satisfy the step mechanically.

Update `PROGRESS.md`, then ask for review.

### Step 3: Implement

Implement the approved plan.

- Keep changes scoped.
- Follow project conventions and preserve the current rules in
  `docs/architecture/boundaries.md` except where the approved plan explicitly
  changes them.
- Do not add dependencies, migrations, services, or public API changes without
  approval.
- Stop and return to step 1 if implementation requires a material scope or
  design change.
- Record changed files and meaningful deviations from the plan.

Update `PROGRESS.md`, then ask for review.

### Step 4: Verify And Repair

Run the narrowest relevant checks first, then broaden according to risk.

Respect the frontend automated-test policy in root `AGENTS.md`. When frontend
automated tests are `excluded`, do not run them or any combined command that
includes them. Use narrower commands for the remaining applicable checks.

Run the project's applicable lint and non-mutating format-check commands
against the final integrated change. Prefer the standard full-project commands
when proportionate; otherwise run the broadest credible scope and record what
was excluded. Obtain engineer approval before unusually extensive checks as
required by `AGENTS.md`.

Loop on code and permitted automated tests until required checks pass. When a
failure is unrelated to the task:

- provide evidence;
- record it separately;
- do not claim a clean pass;
- ask for a decision if it blocks credible verification.

Ask the engineer to execute the applicable scenarios in `MANUAL-TESTING.md` and
record the results they report. A failed or unrun required scenario must have an
explicit disposition and residual-risk record before task conclusion. The
engineer may accept a known limitation or unverified scenario when temporary
risk is tolerable, but the task record must not present it as passed.

Report:

- commands or checks run;
- result of each;
- fixes made during verification and why;
- unrun checks and reasons;
- residual risk.

After required checks pass, run the `code-review` skill:

- if the task affects security or authorization, persistent data, public
  contracts, migrations, concurrency, or multiple architectural boundaries;
- if implementation materially deviates from the approved plan.

Also run it if the engineer requests it. If none of those required conditions
applies, the agent should propose it if the current diff's size or complexity,
implementation uncertainty, or weak verification makes a structured second
pass valuable, explain why, and wait for approval.

Using the skill means reading and following its `SKILL.md`, not merely
performing an informal review from general model behavior. Record whether it
ran, why it did or did not run, its findings, and each finding's disposition in
`PROGRESS.md`.

This same-agent review is a structured second pass, not an independent review,
and does not replace the engineer's diff review. Findings that require changes
return the task to the appropriate earlier step. Ask for review only after the
required verification state is reached.

### Step 5: Update Documentation

Update implementation documentation to describe actual behavior:

- user-visible or operator-visible behavior;
- APIs, data contracts, or configuration;
- architecture boundaries and decisions;
- conventions that genuinely changed.

Review `docs/architecture/boundaries.md`. Update it to reflect any boundary
changes implemented by the current task; otherwise record in `PROGRESS.md` that
it was reviewed and no update was needed.

Do not copy task planning prose into app docs. Update traceability and list
changed docs in `PROGRESS.md`, then ask for review.

### Step 6: Conclude And Commit

Before requesting commit approval:

1. confirm all acceptance criteria have dispositions;
2. finalize traceability;
3. summarize changed behavior and files;
4. record verification results and residual risks;
5. update the relevant `ACTIVITY.md`;
6. mark the task `ready_for_commit` in `PROGRESS.md`;
7. request commit approval.

After approval:

- move the task directory to `done/`;
- update links affected by the move;
- set `agent/tasks/CURRENT.md` to `Current task: none`;
- mark the task completed and record the commit disposition;
- include the task move and lock release in the approved commit set;
- report resulting commit references after the commit operation.

If the task is completed but intentionally not committed, record that decision
before moving it or releasing the lock.

### Review Policy

| Step | Default review gate |
|---|---|
| 1. Plan assessment | review and explicit approval required |
| 2. Verification preparation | review required |
| 3. Implementation | review required |
| 4. Verification | review after required checks pass |
| 5. Docs | review required |
| 6. Conclusion | no separate content review; commit approval required |

The engineer may waive a gate explicitly for a task. Record the waiver in
`PROGRESS.md`.

## 10. Traceability And Omni-Sync

### 10.1 Governing Model

```text
Specs describe intended behavior.
Permitted automated tests, contracts, manual scenarios, and other checks provide
verification evidence.
Code implements behavior.
Implementation docs describe actual behavior.
Task traceability maps the evidence.
```

Where frontend automated tests are excluded, engineer-run scenarios and other
permitted checks provide task-local verification evidence. They do not create
ongoing automated regression coverage.

Planning completeness and implementation completeness are different:

- specs may be ahead;
- completed implementation must not contradict its tests, contracts, or docs;
- task execution must not claim a requirement is implemented without evidence.

### 10.2 Task Traceability

Every task maintains a table in `PROGRESS.md`:

| Requirement | Acceptance Criteria | Verification Evidence | Implementation | Docs | Status |
|---|---|---|---|---|---|
| `REQ-001` | `AC-001` | path or check | path | path or N/A | planned / proven / gap |

At task creation, the first two columns are populated. During execution, the
remaining columns become evidence.

`N/A` must include a reason. A blank cell is unresolved, not implicitly
unnecessary.

### 10.3 Refactoring Evidence

Refactoring traceability may use:

- existing behavior tests;
- added characterization tests;
- public API snapshots or contract checks;
- typecheck, lint, and build results;
- dependency or import graph checks;
- searches proving obsolete names or paths are gone;
- benchmark comparisons where performance is in scope;
- focused manual review of architectural boundaries.

Structural acceptance criteria should be observable. "Improve architecture" is
not sufficient; "domain module no longer imports the UI layer" is.

### 10.4 Drift Audit

Use the `drift-audit` skill sparingly and target a module or bounded area.
Diagnosis comes first. It reports:

- implemented requirements without evidence required by project policy;
- tests with unclear requirement or behavior purpose;
- missing or stale required manual-testing scenarios;
- docs contradicting code;
- implemented behavior missing from docs;
- stale contracts or examples.

Ignore requirements that are intentionally planned but not implemented unless
the audit mode also asks for planning coverage.

The absence of a frontend automated test is not a finding when root `AGENTS.md`
excludes such tests. Existing tests and contracts must still agree with the
implementation.

Repairs should be approved before editing and should not change runtime behavior
unless converted into an explicit task.

## 11. Agent Skills

Agent skills are reusable procedures that may support planning work, task
execution, or complementary work. When a task is active, a skill may be used
only in service of that task; it must not open an unrelated workstream.

Each skill's `SKILL.md` starts with YAML frontmatter containing:

- `name`: the lowercase hyphenated skill name;
- `description`: what the skill does and the conditions that should trigger it.

This follows the Codex skill format. Trigger conditions belong in
`description`, while the body contains the operating procedure. In this
scaffold, `agent/skills/` is the repo-owned canonical source and skills are
discoverable through routing. If native Codex implicit discovery is desired,
install or link the skill directories into a supported `.agents/skills/`
location without creating a second independently maintained source.

### 11.1 Skill Self-Containment

A skill must be operationally self-contained. It may be explicitly invoked,
implicitly selected from its frontmatter description, reached through a nested
router, or reused without the agent first reading the root methodology.

When creating or updating a skill:

- define every nonstandard methodology concept required to follow its
  procedure;
- state work-state preconditions and relevant artifact paths;
- include exclusions that materially affect correct results;
- link required references and state when they must be read;
- if the skill can pause for engineer input, include the explicit handoff rule:
  end with the required question as a separate final paragraph and place no
  text after it;
- do not assume another skill or root `CONTEXT.md` has already been loaded.
- if a required methodology artifact is absent, identify the missing dependency
  and ask for direction rather than inventing a substitute.

The complete methodology remains canonical in its normal files. Repeating a
short operational definition inside a skill is intentional when it prevents
guessing or incorrect execution.

### 11.2 Skill Invocation

Skills have three invocation modes:

- **workflow-required**: a governing workflow defines objective triggers; when
  they apply, the agent reads and follows the skill;
- **engineer-requested**: the engineer explicitly asks for the skill;
- **agent-proposed**: the agent identifies a benefit, explains it, and asks
  before running the skill.

Skill discovery does not imply invocation. A workflow or skill should define
selection conditions and required evidence whenever consistent use matters.
When a skill is used, the agent reads its `SKILL.md`, follows its procedure and
guardrails, and records the prescribed output.

### 11.3 Update Specs

Changes canonical product or business intent, keeps the live spec set
consistent, checks open-task conflicts, obtains acceptance, and records a
complete versioned snapshot. It does not implement the changed behavior.

### 11.4 Plan Feature Work

Maps a substantial area of current specs and implementation evidence into an
ordered plan of coherent candidate task slices. It writes the accepted broad
plan to feature `ACTIVITY.md` without creating formal tasks or changing
implementation.

### 11.5 Create Task

Creates a repository-tracked feature, issue-fix, or refactoring task from the
correct type context and template. It defines scope, requirements, acceptance
criteria, traceability, planning state, manual-testing guidance, and activity
context without starting execution.

### 11.6 Planning Audit

Checks relationships among specs, open tasks, done tasks, and the current-task
lock. It is diagnosis-only by default.

### 11.7 Drift Audit

Diagnoses inconsistencies among implemented behavior, tests and contracts,
code, and application documentation in a bounded area. It is diagnosis-only by
default, ignores intentionally unimplemented specs unless planning coverage is
requested, and requires approval before repairs.

### 11.8 Documentation Refinement

Improves clarity, structure, navigation, and duplication in application docs.
It must validate behavior claims against code or tests and must not invent
behavior.

### 11.9 Clarify With Shared Language

Clarifies and stress-tests a plan through a one-question-at-a-time conversation
grounded in specs, shared domain language, decision records, code, and tests. It
sharpens terms, resolves design dependencies, checks claims against the
repository, and records confirmed planning decisions without starting
implementation.

### 11.10 Improve Codebase Architecture

Finds clusters of tightly coupled shallow modules that could become fewer deep
modules with smaller interfaces, greater leverage, stronger locality, and
better interface-level test surfaces. It produces architecture candidates and,
after discussion, refactoring task plans rather than silently changing runtime
code.

### 11.11 Code Review

Reviews the actual diff against the task brief and plan. Findings are ordered by
severity and focus on correctness, scope creep, security, architecture,
meaningful verification gaps under the project test policy, and maintainability.
Style-only comments are excluded unless they affect those concerns.

### 11.12 Update README

Creates or refreshes the concise root project README. It states that the
repository uses the agentic development methodology, links canonical specs,
application docs, architecture boundaries, and `agent/how-to.md`, and mirrors
the current development commands from `AGENTS.md` without duplicating detailed
project documentation.

Skills should grow only from recurring needs. The core methodology remains in
`AGENTS.md`, `CONTEXT.md`, and task artifacts rather than being hidden in a
skill.

## 12. Documentation Boundaries

`docs/` is for the application and the implemented system:

- actual application behavior;
- current architecture boundaries and important decisions;
- public or internal contracts;
- durable code and documentation conventions.

Do not put methodology instructions or repository-agent usage guides in
`docs/`. Those belong under `agent/`.

`docs/architecture/boundaries.md` is the normative source for current
architectural responsibilities, dependency directions, ownership, and
cross-cutting boundaries. It is the baseline for planning and implementation,
but an approved task plan may intentionally change it. Task execution must
review it during documentation and update it whenever the current task
implements a boundary change.

Decision records preserve the rationale and consequences of durable adopted
choices. They complement the boundaries file rather than replacing or
duplicating it.

## 13. Commit Hygiene

Commits are made in the final execution step, after review and verification.

For substantial tasks, prefer separate commits for:

1. task plan and TPT changes;
2. verification artifacts;
3. implementation;
4. documentation.

For small tasks, one commit is acceptable when its message or body clearly
separates these concerns.

Never:

- commit without approval;
- hide failing checks;
- mix unrelated cleanup into the task;
- rewrite engineer-owned history without explicit instruction.

## 14. Conversation Continuity And Compaction

Automatic context compaction is not a source of truth. Before a long
conversation ends, before a review gate, and whenever context loss is likely:

- update `PROGRESS.md`;
- record the current step and next action;
- record unresolved questions and decisions;
- ensure `CURRENT.md` points to the task.

A new conversation resumes by reading:

1. `AGENTS.md`;
2. root `CONTEXT.md`;
3. `agent/tasks/CURRENT.md`;
4. the active task's `BRIEF.md`, `PLAN.md`, `PROGRESS.md`, and
   `MANUAL-TESTING.md`;
5. only the relevant routed project files.

## 15. Engineer Operating Guide

### Before Approving A Plan

Check:

- scope is narrow enough;
- files and boundaries make sense;
- permitted automated tests, manual scenarios, or other checks can verify the
  acceptance criteria;
- no unnecessary architecture was invented;
- dependencies and migrations are justified;
- non-goals are preserved;
- expected diff size and risk are credible.

### During Human Diff Review

Review the actual diff, not only the agent summary:

- Did it solve only the requested problem?
- Does behavior match every acceptance criterion?
- Are edge cases and failure modes handled?
- Were architecture boundaries preserved?
- Did the change bypass validation, auth, or data-access layers?
- Does verification follow the frontend automated-test policy?
- Are permitted automated tests meaningful and behavior-focused?
- Where frontend tests are excluded, do manual scenarios cover the affected
  acceptance criteria and have honest reported results?
- Is there duplication or unnecessary abstraction?
- Are API, migration, security, or compatibility risks understood?
- Do docs describe the behavior now implemented?

### Capturing Lessons

After a task, the engineer may create or edit `LESSONS.md`:

- what worked;
- what the agent misunderstood;
- prompt corrections;
- project guidance to update;
- a skill to add or revise;
- a convention discovered.

Promote only durable, recurring lessons:

- project rule -> `AGENTS.md`;
- routing or task procedure -> `CONTEXT.md`;
- application fact -> `docs/`;
- reusable procedure -> `agent/skills/`;
- one-off detail -> leave it in the task.

## 16. Adopting The Scaffold

When copying `Methodology/scaffold/` into a project:

1. fill in the project summary, repository map, commands, standards, and
   architecture pointer in `AGENTS.md`, including an explicit frontend
   automated-test policy;
2. use the `update-readme` skill to create the concise root README;
3. update root and nested routing tables for the real repository;
4. replace placeholder specs and docs with project content, including current
   boundaries in `docs/architecture/boundaries.md`;
5. preserve the task package and execution workflow unless consciously
   tailoring it;
6. remove irrelevant optional skills rather than leaving misleading guidance;
7. keep `CURRENT.md` at `none` until execution begins;
8. make the first planned task a small real task and calibrate the process from
   evidence.

The methodology should evolve slowly. Change it when repeated experience shows
that a rule, artifact, or checkpoint adds or removes real value.

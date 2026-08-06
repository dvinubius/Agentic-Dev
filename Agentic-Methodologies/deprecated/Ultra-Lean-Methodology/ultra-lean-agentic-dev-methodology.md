# Ultra Lean Agentic Development Methodology

## 1. Purpose

Ultra Lean is for software projects where a developer stays actively in the
loop and steers agentic work through a small number of explicit phases:

1. Idea and alignment.
2. Short-lived PRD.
3. Optional local issues.
4. ADRs for durable technical decisions.
5. Issue or direct implementation with developer review.
6. PR creation and PRD conformity check when requested or AFK-executed.

It doesn't aim for "say the task once and have the agent autonomously do
everything." The developer watches the important moments, catches obvious
wrong turns, and decides how much process a task needs. That lets the
methodology remove many defensive instructions and rely more on the agent's
local judgment.

The reusable files are under `Ultra-Lean-Methodology/scaffold/`.

## 2. Governing Model

The repository separates reusable methodology, temporary task state, mutable
project documentation, and code:

```text
reusable methodology:
  AGENTS.md
  .agent/

optional project glossary:
  CONTEXT.md

temporary current-task artifacts:
  .agent-state/current-task/
    PRD.md
    optional issues/

mutable project state:
  docs/
  code and tests
  project configuration

developer-only notes:
  .devnotes/
```

`AGENTS.md` and `.agent/` are the replaceable methodology package. Root
`CONTEXT.md`, `docs/`, source, tests, project configuration, and `.devnotes/`
are project-owned.

`.agent-state/current-task/` is temporary runtime state. It may contain a PRD
and optional local issue files while a task is active. It is not a durable task
archive, progress journal, or issue tracker, and it must not be committed.

Code is the primary authority for current behavior. Tests and executable
contracts provide supporting evidence. Documentation accelerates orientation
but does not replace reading the implementation.

`docs/normative/` records current architecture and contracts with external
systems. `docs/adr/` records durable decisions. When implementation changes
accepted technical behavior, relevant docs should change with it.

`.devnotes/` is developer-owned planning space. Agents ignore it unless the
developer explicitly asks them to read or edit a named file there.

## 3. Core Principles

### 3.1 Developer-Steered Workflow

The developer is the strategist and final decision maker. The methodology
provides phase skills, not a single autonomous task runner.

The developer decides when to:

- clarify the idea;
- create or update a PRD;
- split the PRD into issues;
- record ADRs;
- implement directly or issue by issue;
- review an issue result;
- create the PR and check PRD conformity, or delegate that finish step through
  AFK execution.

Agents still challenge contradictions, weak assumptions, unsafe plans, missing
context, and scope expansion. Ultra Lean removes redundant process, not
engineering judgment.

### 3.2 One Task, One PRD, Optional Issues, One PR

The default work unit is:

```text
1 task -> 1 PRD -> optional issues -> 1 PR
```

Issues are optional. A small PRD can be implemented directly in the same
conversation. Larger or riskier PRDs can be split into ordered local issues
under `.agent-state/current-task/issues/`.

### 3.3 Short-Lived Planning Artifacts

The PRD and optional issue files preserve just enough shared intent to make
implementation reviewable and resumable. They are not permanent product
documents, acceptance ledgers, or diaries.

Before continuing after context compaction or in a later conversation, rebuild
context from current repository state, `git status`, the current diff, the
PRD, optional issue files, relevant source, and concise reports in the thread.

Delete `.agent-state/current-task/` when the task is complete or abandoned.
Remove `.agent-state/` when empty.

### 3.4 Context Is Loaded On Demand

Start with root `AGENTS.md`, which owns routing. Read root `CONTEXT.md` only
when its project glossary is relevant or a term is unclear. Load detailed
skills, documentation methodology, code, and docs only as needed.

Read broader code or documentation when excluding it could hide a material
dependency. Do not bulk-load the repository just because a route exists.

### 3.5 Confirmation Is Proportionate

Agents can run straightforward local checks without asking. They should stop
and ask before destructive operations, deployments, production actions,
unusually broad verification, expensive tool calls, or commits.

The developer is expected to review important outputs. That review replaces
many methodology-level prohibitions, but agents must still avoid silently
broadening scope, concealing failed checks, or changing developer-maintained
content.

## 4. Repository Structure

```text
repo/
|-- README.md
|-- AGENTS.md
|-- CONTEXT.md  # optional project glossary
|-- .agent/
|   |-- docs/
|   |   |-- CONTEXT.md
|   |   `-- templates/
|   |-- how-to.md
|   `-- skills/
|       |-- to-prd/
|       |-- prd-to-issues/
|       |-- implement-issue/
|       |-- finish-task/
|       `-- <focused skills>
|-- .agent-state/  # temporary; absent when no task is active
|   `-- current-task/
|       |-- PRD.md
|       `-- issues/
|-- .devnotes/  # developer-only notes; ignored by agents
|-- docs/
|   |-- adr/  # optional; created when a decision merits an ADR
|   |-- repository-map.md
|   |-- development-commands.md
|   |-- conventions.md
|   `-- normative/
|       |-- README.md
|       |-- architecture.md
|       `-- integrations/
|-- src/
`-- tests/
```

Application directories are project-specific. The important boundary is that
`AGENTS.md` and `.agent/` are replaceable methodology, while `CONTEXT.md`,
`docs/`, `.devnotes/`, source, tests, and project configuration are
project-owned.

## 5. Methodology Files

### 5.1 `AGENTS.md`

`AGENTS.md` gives compact global operating rules, owns workflow and skill
routing, and points to project references. It treats root `CONTEXT.md` as an
optional glossary and reads it only when terminology matters.

It should stay small. It is a routing and safety file, not a task workflow.

### 5.2 Root `CONTEXT.md`

Root `CONTEXT.md` is an optional project-owned glossary. It contains only
project-specific language, not routing, implementation details, or decisions.
The global `grill-with-docs` skill creates or updates it when shared language
needs active clarification.

### 5.3 `.agent/`

`.agent/` contains reusable methodology:

- `.agent/skills/` for phase and focused skills;
- `.agent/docs/` for documentation routing and templates;
- `.agent/how-to.md` for developer usage.

### 5.4 `.agent-state/`

`.agent-state/` is temporary runtime state outside the installed methodology.
During an active task it may contain:

- `.agent-state/current-task/PRD.md`;
- optional issue files under `.agent-state/current-task/issues/`.

Never commit `.agent-state/`. Delete it when the task is complete or
abandoned.

## 6. Ultra Lean Workflow

### 6.1 Idea

The developer and agent align on the outcome, constraints, scope, likely
technical surface, and open questions. Use the global `grill-with-docs` skill
when the plan, design, or shared language needs focused clarification.

This phase has the most cognitive effort. Good steering here prevents process
later.

### 6.2 PRD

Use `to-prd` to create `.agent-state/current-task/PRD.md`.

The PRD captures the current task's problem, solution, user stories,
implementation decisions, testing decisions, out-of-scope work, and notes. It
is the shared basis for implementation, not a durable product spec.

The developer reviews and corrects the PRD before implementation or issue
creation.

Once the PRD is ready, unless the developer intends to have the agent perform
an AFK prd implementation, the developer should consider whether direct execution
or issue-based execution best fits the task. Direct execution fits one
coherent reviewable change. Issue-based execution fits work that benefits
from vertical slices, focused review, or efficient subagent use.

### 6.3 Issues

Skip issues when the PRD is simple enough to implement and review directly.

Use `prd-to-issues` when the PRD naturally decomposes into reviewable slices,
the work is risky or noisy, context limits are likely, or the developer wants
issue-sized execution. Iterate until the issue set is small enough to become
tracer bullets: each issue should have clear scope, non-goals, acceptance
criteria, verification expectations, and stop conditions.

Issues are local files, not external tracker records unless the developer
explicitly asks for that separate workflow.

### 6.4 ADRs

Record ADRs for durable technical decisions whose rationale and consequences
will matter later. Do this when decisions are accepted, not for every passing
implementation thought.

Keep current architecture and integration docs accurate to implemented
behavior. Do not rewrite them to describe future planned behavior before code
changes make it true.

### 6.5 Implementation

For direct implementation, the developer may ask an agent to implement the PRD
directly in the active conversation. The agent reads the PRD and relevant
project context, changes only the approved scope, runs focused checks, and
reports the diff and verification.

For issue implementation, use `implement-issue` on exactly one issue at a
time. The issue agent reads the PRD, its issue file, relevant ADRs or
normative docs, and routed code/docs; implements only that issue; runs focused
checks; and reports acceptance criteria disposition, verification, and risks.

For AFK implementation of an approved PRD, use `execute-prd-afk` when the
developer has explicitly waived normal review points. The agent
creates a feature branch and reads the completed execution plan from the
current-task state: existing issue files mean planning chose issue-based
execution; no issue files means planning chose direct PRD execution. AFK
execution does not reopen whether the PRD should have been split, but it may
deviate from existing issue boundaries when following them would reduce the
chance of satisfying the PRD. For cohesive product flows, shared UI surfaces,
or tightly coupled integration paths, the agent may combine issues or work
horizontally if that better preserves end-to-end coherence. Such deviation
must be stated with a concrete reason, while the PRD remains the authority and
issue files remain tracer bullets for final alignment. The agent uses
subagents by default for multi-issue execution unless there is a concrete
reason not to, performs lightweight issue acceptance when issue results are
used, creates suitable commits, checks final PRD alignment as an
implementation-completion gate, then uses `finish-task` to create or update
the PR and report PRD conformity against the PR change set.

After an issue report, the developer performs a lightweight issue acceptance
check:

- report completeness;
- acceptance criteria disposition;
- focused verification status;
- issue scope and non-goals;
- obvious unrelated churn.

The developer decides whether to accept, request repair, broaden the PRD,
split a follow-up issue, or stop.

### 6.6 Finish Task

`finish-task` is optional outside AFK execution. Use it when the developer
wants agent help creating the PR or checking whether PR changes satisfy the
PRD. `execute-prd-afk` uses `finish-task` after committed implementation work
passes its lightweight PRD-level completion gate.

The developer may skip `finish-task` and create the PR or perform the PRD
conformity check manually.

## 7. Phase Skills

Core phase skills:

- `to-prd`: create or update `.agent-state/current-task/PRD.md`.
- `prd-to-issues`: create ordered local issues from an approved PRD.
- `execute-prd-afk`: execute an approved PRD with waived review
  points.
- `implement-issue`: tackle one issue from start to finish.
- `finish-task`: create or update a PR and check PRD conformity; optional
  outside AFK execution.

Focused local skills:

- `investigate-issue`: diagnose a bug or regression before fixing.
- `assess-change-impact`: assess blast radius before consequential changes.

Global skills:

- `grill-with-docs`: clarify or stress-test plans, designs, and shared
  language; maintain `CONTEXT.md` and `docs/adr/`.
- [`no-mistakes`](https://github.com/kunchenguid/no-mistakes): review and gate
  completed work before push.

Optional skills are not read eagerly. Use them when the developer asks or when
the current phase clearly benefits from the procedure.

## 8. Documentation Boundaries

Project documentation work follows `.agent/docs/CONTEXT.md`.

`docs/` contains mutable project state:

- repository map and development commands;
- conventions;
- ADRs under `docs/adr/` when needed;
- normative technical documentation.

Methodology instructions belong in `AGENTS.md` and `.agent/`, not in project
`CONTEXT.md` or `docs/`.

Template-backed files should preserve their template-defined structure while
retaining valid project-specific content.

Integration contracts describe this code's dependency on external systems.
They are not public instructions for external consumers unless the project
explicitly adopts that documentation purpose elsewhere.

## 9. Commit And PR Hygiene

Keep commits coherent and reviewable. Never:

- commit without required approval;
- conceal failing or unrun checks;
- mix unrelated cleanup into the change;
- rewrite developer-owned history without explicit instruction;
- discard unrelated pre-existing work.

For issue-based work, one commit per accepted issue is a useful default when
it improves reviewability. For direct PRD-backed work, or issue-planned work
that is implemented as one tightly coupled change, one coherent task commit is
also valid. The developer can choose a different commit shape.

One task should normally become one PR. If the PRD changes enough that this is
no longer true, return to alignment instead of silently widening the PR.

## 10. Adopting The Scaffold

When copying `Ultra-Lean-Methodology/scaffold/` into a project:

1. install `AGENTS.md` and `.agent/` as the reusable methodology; keep the
   scaffold `CONTEXT.md` only when a project glossary is useful;
2. fill `docs/repository-map.md` and `docs/development-commands.md` with
   current project information;
3. fill template-backed live files under `docs/` while preserving their
   structure;
4. fill `docs/normative/architecture.md` with current system context,
   dynamics, and accepted boundaries;
5. populate `docs/normative/integrations/` for accepted external
   interactions, or leave its index explicitly empty;
6. keep `.devnotes/planning.md` only as optional developer-owned orientation;
7. create or refresh root `README.md` from
   `.agent/docs/templates/root-readme.md`.

Upgrade an installed project by replacing only:

- `AGENTS.md`;
- `.agent/`.

Do not replace project-owned `CONTEXT.md`, `docs/`, or `.devnotes/` as part of
a methodology upgrade. `.agent-state/` is outside the replacement set.

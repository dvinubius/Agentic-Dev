# Lean Agentic Development Methodology

## 1. Purpose

This methodology is for software projects in which:

- one developer remains the strategist and final decision maker;
- one main coding agent owns task intent, planning, direct execution for
  suitably small tasks, orchestration, review coordination, commits, and final
  reporting;
- implementation work is either performed directly by the main agent for a
  small PRD-backed task or delegated sequentially to write-capable issue
  subagents when issue-based execution adds value;
- read-only review subagents may review integrated final diffs or noisy
  evidence;
- task planning is based on alignment with the developer, a short-lived PRD,
  and short-lived local issues only when decomposition or delegation is useful;
- implemented technical behavior remains consistent across code, tests,
  executable contracts, architecture documentation, and external dependency
  contracts.

The methodology deliberately trusts the agent's discernment, repository
awareness, and attention to detail. It uses a small number of durable sources,
short-lived task artifacts, and focused skills instead of permanent task
management. It keeps explicit developer review points where early feedback
prevents wrong direction, helps lower-effort reasoning produce reliable
results, or avoids wasteful verification and token usage.

The reusable files are under `Lean-Methodology/scaffold/`.

## 2. Governing Model

The repository separates reusable methodology, temporary current-task
artifacts, and mutable project state:

```text
reusable methodology:
  AGENTS.md
  CONTEXT.md
  .agent/

temporary current-task artifacts:
  .agent-state/current-task/
    PRD.md
    optional issues/
    optional concise implementation, issue, or review reports

mutable project state:
  docs/
  .devnotes/
  code and tests
```

The methodology is upgradable by replacing `AGENTS.md`, `CONTEXT.md`, and
`.agent/` together. Project-specific information belongs in mutable project
paths. Temporary task artifacts live separately under `.agent-state/`.

`docs/` contains repository orientation, commands, canonical terminology,
conventions, and normative technical documentation. `.devnotes/` may contain
git-tracked developer notes that agents ignore during normal work.

Code is the primary authority for current system behavior because it determines
what actually runs. Permitted tests and executable contracts provide supporting
evidence. The repository map accelerates targeted exploration.

`docs/normative/` is authoritative for accepted technical intent. Active
changes keep code and normative technical docs matched as implementation and
technical design evolve together.

Lean does not maintain end-user behavior documentation or prose instructions
for external consumers integrating with this system. Generate those on demand
or through a complementary methodology.

### Methodology Package

Root `AGENTS.md`, root `CONTEXT.md`, and installed files under `.agent/`
carry the reusable methodology. The main agent may create, update, and delete
`.agent-state/current-task/` while a non-trivial task is active.

Methodology templates live under `.agent/docs/templates/`. Mutable project
files begin with the same blank structure as their templates. Agents update
live project files and use templates only to preserve or restore structure.

### Technical State

Code and tests must match `docs/normative/`. Normative architecture records
accepted current structure and internal dynamics. Normative decisions explain
consequential accepted choices and their rationale. Normative integration
contracts record external systems, authoritative references, and the exact
contract surface used.

### No Formal Task Management

There is no permanent task directory, task identifier, progress journal,
acceptance table, or done-task archive.

Planning and execution form one conversational workflow. For an active
non-trivial task, `.agent-state/current-task/` may contain only the PRD,
approved issue files when issue-based execution is selected, and concise
reports useful for reconstruction. These files are short-lived execution
artifacts, not a task record or history. They are deleted when work is
completed or abandoned. The `.agent-state/` directory is removed when empty and
is never committed.

## 3. Core Rules

### 3.1 Confirmation And Review

The agent avoids expensive or risky work without confirmation. Before asking,
it summarizes the evidence, options, recommendation, and practical
consequence, then asks one concrete question.

The agent stops and asks before:

- running destructive operations, deployments, production actions, unusually
  broad verification, or expensive tool calls;
- creating commits.

For non-trivial application work, `.agent/skills/work-on-task/SKILL.md`
provides PRD, execution-mode, implementation-review, commit, and finishing
gates. Issue gates apply only when issue-based execution is selected.

### 3.2 The Developer Is The Strategist

The developer chooses product direction and decides how much review involvement
the agent should receive. Case-specific delegation for independent execution
must be explicit.

The agent should still challenge contradictions, weak assumptions, or unsafe
plans directly. It should not silently replace explicit developer strategy
with its own.

### 3.3 Workflow Gates Live In Skills

The `work-on-task` and related focused skills define the workflow-specific
approval and review points for:

- PRD approval;
- execution-mode approval;
- issue breakdown approval when issue-based execution is selected;
- accepted durable technical decisions;
- significant implementation plans in direct work or inside issues;
- architecture-boundary changes;
- high-impact product, security, privacy, migration, dependency, cost, or
  operational choices;
- non-trivial implementation diffs;
- final PRD alignment.

### 3.4 Context Is Routed

Use `CONTEXT.md` files as maps, not encyclopedias.

- Start with root `AGENTS.md` and root `CONTEXT.md`.
- Follow only routes relevant to the current work.
- Read broader code when excluding it could hide an important dependency.
- Keep methodology instructions generic and stable.
- Put repeatable procedures in skills and durable system facts in docs,
  code, tests, or accepted decisions.

### 3.5 Current-Task Artifacts Replace Transcript Dependence

The PRD and optional issues under `.agent-state/current-task/` preserve the
approved task basis:

- `PRD.md`: problem, solution, user stories, implementation decisions, testing
  decisions, out-of-scope work, and notes;
- `issues/`, when present: ordered issue files with scope, non-goals,
  implementation direction, acceptance criteria, verification expectations,
  blockers, and stop conditions;
- optional concise implementation, issue-worker, review, or verification
  reports.

These artifacts are not a diary. Obsolete plans, failed attempts, raw logs,
stack traces, and superseded hypotheses are not accumulated.

Before continuing after context compaction, before starting a later issue, or
when context feels stale, the main agent reconstructs from current repository
state, relevant source, `git status`, the current diff, current-task artifacts,
and concise verification or subagent reports. Mental compaction and remembered
transcript are not the recovery substrate.

Delete `.agent-state/current-task/` after the final report is reconstructed and
the task is complete, or immediately when the task is abandoned. Remove
`.agent-state/` when empty so no residual runtime state remains between tasks.

Because Lean no longer uses a handoff file, tasks should be sized and managed
so the main session can realistically carry planning, execution, verification,
and final review without running out of useful context.

### 3.6 Changes Stay Coherent

The agent should work on one coherent task at a time. It may address a small
directly related defect discovered during implementation when doing so is
clearly necessary and low risk. It must not silently combine unrelated cleanup,
features, or refactoring.

Issue subagents do not violate this rule when each delegated issue belongs to
the approved PRD and issue set.

If newly discovered work cannot be addressed without broadening scope, bring
the essential concern to the developer's attention.

### 3.7 Verification Is Proportionate

Run the narrowest useful checks first and broaden according to risk.

- Run straightforward local checks without asking.
- For checks that are unusually broad, costly, slow, or environmentally
  consequential, ask first.
- Never claim a check passed unless it ran successfully.
- Report relevant checks not run and why.
- Do not invent low-value tests merely to satisfy a process.
- Do not create a `MANUAL-TESTING.md` file or another persistent manual-test
  worksheet unless the developer explicitly requests one.

### 3.8 Dependency Installation Is Conservative

Before installing any package, verify that the package version is at least two
weeks old. If it is newer, do not install it and report the reason.

## 4. Repository Structure

```text
repo/
|-- README.md
|-- AGENTS.md
|-- CONTEXT.md
|-- .agent/
|   |-- docs/
|   |   |-- CONTEXT.md
|   |   `-- templates/
|   |       |-- domain-language.md
|   |       `-- <documentation templates>
|   |-- how-to.md
|   `-- skills/
|       |-- CONTEXT.md
|       `-- <skill>/SKILL.md
|-- .agent-state/  # temporary; absent when no task is active
|   `-- current-task/
|       |-- PRD.md
|       `-- issues/  # present only for issue-based execution
|-- .devnotes/  # git-tracked developer notes; ignored by agents
|   `-- planning.md
|-- docs/
|   |-- domain-language.md
|   |-- repository-map.md
|   |-- development-commands.md
|   |-- normative/
|   |   |-- README.md
|   |   |-- architecture.md
|   |   |-- decisions/
|   |   `-- integrations/
|   `-- conventions.md
|-- src/
`-- tests/
```

Application directories are project-specific. The important boundary is that
`AGENTS.md`, `CONTEXT.md`, and `.agent/` are replaceable methodology, while
`docs/`, `.devnotes/`, source, tests, and project configuration are
project-owned. `.agent-state/` is not part of the methodology upgrade package
and must not persist after its active task ends.

## 5. Methodology Files

### 5.1 `AGENTS.md`

`AGENTS.md` is generic methodology. It points to project-specific:

- `docs/repository-map.md`;
- `docs/development-commands.md`;
- `docs/normative/README.md`;
- `docs/conventions.md`;
- `docs/domain-language.md`.

These references are routing entry points. The agent loads the relevant
project files for the current work rather than treating the list as a required
recursive read.

### 5.2 Root `CONTEXT.md`

Root `CONTEXT.md` routes work to:

- `.agent/skills/work-on-task/SKILL.md` for non-trivial task work;
- `.agent/docs/CONTEXT.md`;
- `.agent/skills/CONTEXT.md`;
- the relevant workflow or focused skill.

It is generic methodology and contains no project-specific state.

### 5.3 `.agent/`

Installed files in `.agent/` contain reusable methodology:

- `.agent/skills/` contains reusable workflows;
- `.agent/docs/` routes documentation work and owns documentation templates;
- `.agent/how-to.md` explains developer usage.

### 5.4 `.agent-state/`

`.agent-state/` is temporary agent runtime state outside the installed
methodology. During active non-trivial task work it may contain only
`.agent-state/current-task/` artifacts created by the main agent:

- `PRD.md`;
- issue files under `issues/` when issue-based execution is selected;
- concise issue, review, or verification reports when useful.

Never commit it. Remove `.agent-state/current-task/` at task completion or
abandonment, and remove `.agent-state/` when empty. Durable implemented facts
and accepted decisions remain in their canonical project paths.

### 5.5 Root `README.md`

The root README is a concise human-facing entry point. It provides project
identity and links to canonical repository orientation, normative technical
docs, and `.agent/how-to.md` instead of duplicating them.
It is template-backed by `.agent/docs/templates/root-readme.md`.

## 6. `.devnotes/planning.md`

`.devnotes/` is git-tracked developer space. Agents ignore it during normal
work: they do not read, search, modify, or treat it as context.

`.devnotes/planning.md`, when present, is a free-form developer aid for
deciding what work to give the agent next. It is not template-backed, not a
canonical product or technical source, not a workflow input, and not maintained
by agent execution or finishing passes.

The developer may explicitly ask an agent to create or update a named file
under `.devnotes/`.

## 7. Work On Task Workflow

Use the `work-on-task` skill for non-trivial features, fixes, and refactoring.
The workflow is intentionally adaptive. Task execution is always based on an
approved PRD. After PRD approval, the main agent chooses either direct
PRD-backed execution or issue-based execution.

### 7.1 Align

Inspect enough implementation, tests, contracts, docs, and architecture
boundaries to understand the request and likely impact without bulk-loading
the repository.

When broad search, test reproduction, logs, external documentation, or similar
evidence gathering would be noisy, delegate bounded read-only questions to
subagents. Several read-only subagents may run concurrently when they support
the same outcome. The main agent keeps only their concise reports and validates
material conclusions against current repository evidence.

Optional skills are conditional, not eagerly loaded. During `work-on-task`,
use `.agent/skills/CONTEXT.md` to select an optional skill only when its
trigger is present and the extra procedure will reduce guessing or risk.

### 7.2 Create The PRD

Use `to-prd` to create `.agent-state/current-task/PRD.md`. The PRD captures:

- problem statement;
- solution;
- user stories;
- implementation decisions;
- testing decisions;
- out-of-scope work;
- further notes.

The PRD is the concise summary of what needs to be done for the current task.
It is not a durable product document or task tracker.

Present the PRD to the developer and obtain approval before choosing direct or
issue-based execution.

### 7.3 Choose Execution Mode

After PRD approval, decide whether the task should be executed directly by the
main agent or broken into local issues for subagent delegation. Do not load
`prd-to-issues` merely to make this decision.

Use direct PRD-backed execution when the approved PRD describes one coherent
change that the main agent can realistically implement, verify, review, and
report in the current session with less overhead than issue creation and
subagent delegation. This is appropriate when the change is small enough for a
single coherent review unit, the blast radius is understood, no independent
issue-worker context is needed, and the cost of issue/subagent setup would
exceed its value.

Use issue-based execution when the approved PRD is naturally decomposed into
multiple reviewable slices, the implementation is risky or noisy enough to
benefit from an isolated worker or review pass, context compaction is a
credible concern, or the developer explicitly wants delegated execution.

Present the recommended execution mode and practical consequence to the
developer. If direct execution is selected, proceed to implementation without
creating `.agent-state/current-task/issues/`. If issue-based execution is
selected, load `prd-to-issues` and create issues.

### 7.4 Create Issues When Needed

For issue-based execution, use `prd-to-issues` to break the approved PRD into
ordered local issue files under `.agent-state/current-task/issues/`.

Prefer vertical slices that are independently verifiable. Use enabling
prefactors first only when they make later issue execution simpler or safer.

Each issue must include enough context for a subagent to execute correctly
without the main agent's rich planning conversation:

- PRD reference and covered user stories;
- what to build;
- scope and non-goals;
- implementation direction and relevant accepted decisions;
- acceptance criteria;
- verification expectations;
- blockers;
- stop-and-ask conditions.

Present the issue breakdown to the developer. Ask whether granularity,
dependency relationships, and technical direction are right. Iterate until the
developer approves.

### 7.5 Record Accepted Technical Direction

Once the PRD and execution mode are approved, create or update ADRs under
`docs/normative/decisions/` for accepted durable technical choices whose
rationale or consequences will matter later. Commit these ADR changes
separately after required approval and before implementation begins.

Keep current architecture and integration docs accurate to the current
implementation. Do not update them to describe future planned behavior before
the corresponding issue changes code.

### 7.6 Execute Directly Or Execute Issues

For direct PRD-backed execution, the main agent performs the implementation,
updates affected docs, runs focused verification, inspects the actual diff for
scope, quality, secrets, and accidental churn, and asks for developer review or
approval unless that gate was explicitly waived or batched. The main agent may
use a read-only review subagent when the final diff is large, risky, or noisy,
but it does not create local issue files just to obtain review. After approval,
the main agent creates one coherent task commit unless the developer requested
a different commit shape.

For issue-based execution, the main agent orchestrates issue execution. It
does not perform non-trivial implementation, refactoring, or fixes directly
inside delegated issue scope.

For each issue:

1. Delegate exactly one approved issue to one write-capable issue subagent.
2. Instruct the issue worker to read the PRD, its issue file, relevant ADRs or
   normative docs, and the code/docs it needs.
3. The issue worker implements only that issue, updates affected docs, runs
   focused verification, and finishes with `finish-issue`.
4. The main agent performs a lightweight issue acceptance check: issue report
   completeness, acceptance criteria disposition, focused verification status,
   issue scope and non-goals, and obvious unrelated churn.
5. The main agent does not perform a full code review of each delegated issue
   by default. It checks intent-sensitive points itself, handles the engineer
   review/approval gate, and decides whether repair is needed.
6. For non-trivial cleanup or repair, the main agent sends a narrow instruction
   back to an issue worker. The main agent may perform only trivial formatting
   or documentation cleanup directly.
7. After approval, the main agent creates one commit for that issue.

Do not run more than one write-capable issue subagent at a time. Do not commit
without required approval. Do not silently pull later issues into the current
issue.

If evidence invalidates the PRD, issue breakdown, or an accepted decision,
return to alignment with the developer. Update the PRD, issues when present,
and ADRs as needed before resuming execution.

### 7.7 Finish The Task

Use the `finish-task` skill after direct implementation or all approved issues
have been completed, accepted, approved, and committed, or explicitly marked
partial/deferred.

The main agent owns final PRD alignment because it retains the richest context
about the engineer's intent. For issue-based execution, a fresh read-only
review subagent performs the substantive final review of the integrated task
diff. For direct execution, use a read-only review subagent when the final diff
is large, risky, noisy, or developer-requested. Review subagents report
findings and evidence; they do not decide whether the task intent was
satisfied.

If final PRD alignment shows that a direct task is still incomplete, the main
agent repairs the gap directly when it still fits the approved direct execution
mode. If the remaining work no longer fits direct execution, return to
execution-mode alignment, create approved issues, and continue through the
issue workflow. If final PRD alignment shows that an issue-based task is still
incomplete even though all delegated issues were completed correctly, the main
agent creates a new issue for the remaining PRD gap and runs it through the
same issue approval, delegation, acceptance, approval, and commit workflow.
This is not treated as failed subagent work when the prior issues were
correct. Repeat until the PRD is actually satisfied, or until the engineer
explicitly marks remaining scope partial or deferred.

The final task pass checks:

- direct task commit or completed issue commits against the PRD;
- relevant normative docs against implemented technical behavior;
- proportionate verification evidence;
- affected non-normative project docs;
- unrelated changes, accidental churn, secrets, generated-file edits, and
  remaining substantive risk.

Then inspect the actual diff and report:

- PRD outcome and scope completed;
- direct execution outcome or issues completed and their commits;
- important files changed;
- tests created or changed, including their paths and purpose;
- whether each relevant test or test command ran, and its result;
- an explicit statement when no tests were created or changed;
- verification and results;
- manual scenarios worth exercising when automated evidence is insufficient;
- known omissions and why they are intentional;
- residual risk and unresolved decisions.

Delete `.agent-state/current-task/` after the final report is reconstructed
and the task is complete, then remove `.agent-state/` when empty. If work is
abandoned, delete current-task artifacts and remove task-specific normative
changes introduced solely for the abandoned design while preserving
independently accepted technical intent.

## 8. Optional Skills

The scaffold includes these optional reusable procedures:

- `investigate-issue`: diagnosis-first bug investigation;
- `assess-change-impact`: focused analysis of dependencies, contracts, data,
  architecture, security, and operations before a consequential change;
- `code-review`: substantive review of an actual diff against the request,
  PRD, optional issues, communicated approach, and repository rules;
- `clarify-with-shared-language`: one-question-at-a-time clarification of
  terminology and design choices;
- `deepen-modules`: focused identification of deeper-module
  opportunities.
- `neatify-code`: behavior-preserving maintainability refactoring or review of
  bounded changed code using broad static evidence for routing and codegraph or
  repository-native follow-up for structural understanding where viable.

Methodology authors should add skills only when a procedure has recurring
value. Avoid skills that merely rename ordinary attentiveness or recreate
permanent task management.

## 9. Skill Design

Each `SKILL.md` uses Codex-compatible frontmatter:

- `name`: lowercase and hyphenated;
- `description`: what the skill does and when it should trigger.

Skills must be operationally self-contained:

- state required context and scope limits;
- define any nonstandard methodology concepts they use;
- identify high-impact confirmation triggers;
- explain whether they diagnose, edit, or both;
- avoid assuming another skill has already been read;
- report missing methodology dependencies instead of inventing replacements.

Invocation types are:

- **workflow-required**: the methodology names an objective trigger;
- **developer-requested**: the developer asks for the skill;
- **agent-selected**: the agent uses it because the current bounded work
  clearly benefits.

## 10. Documentation Boundaries

Follow routing and template rules in `.agent/docs/CONTEXT.md`.

`docs/` contains mutable project state:

- repository map and development commands;
- canonical project terminology in `docs/domain-language.md`;
- normative technical documentation under `docs/normative/`;
- configuration and technical failure behavior;
- stable conventions.

Do not store methodology instructions in `docs/`. Template-backed live files
must preserve the structure defined under `.agent/docs/templates/`. The root
`README.md` is also template-backed by
`.agent/docs/templates/root-readme.md`.

Use `docs/normative/README.md` as the map for accepted technical intent. It
routes architecture, accepted decisions, and contracts with external systems.
Proposed technical direction remains conversational or in the current-task PRD
and optional issues unless accepted as durable technical intent. Accepted
durable technical direction belongs in `docs/normative/`.

Decision records have no mandatory body template. They should make status,
scope, context, the decision, relevant alternatives, and consequences clear as
appropriate. Only accepted or superseded decisions belong in
`docs/normative/`. Do not create a decision record for every implementation
thought.

When an external interaction is accepted or materially changed, update its
normative contract as the implementation changes. Record authoritative
references, the exact surface used, internal mapping, ignored provider data,
unknown-field behavior, compatibility, operational behavior, and verification
evidence.

Integration contracts describe this code's dependency on external systems.
They must not become instructions for external consumers integrating with this
system. Public user, operator, API-reference, and integration documentation is
outside Lean and should be generated separately.

## 11. Conversation Continuity

Chat history is useful working context, but it is not guaranteed durable state.
During active non-trivial work, `.agent-state/current-task/` is the
phase-recovery substrate. It preserves the approved PRD, optional issue set,
and concise implementation, issue, or review reports, while durable
information belongs in:

- implemented facts in code and tests;
- accepted technical intent in `docs/normative/`;
- project-specific conventions in `docs/conventions.md`.

Before continuing direct work, before a later issue, after automatic
compaction, or in a new conversation continuing active work, reconstruct from:

1. current repository state and relevant source;
2. `git status` and the current diff;
3. `.agent-state/current-task/PRD.md`;
4. `.agent-state/current-task/issues/` when issue-based execution is active;
5. latest concise implementation, issue, verification, or review reports.

Do not use current-task artifacts as a durable fact store, progress journal, or
substitute for accepted decisions, code, tests, or docs. Delete them when the
task is completed or abandoned, and remove `.agent-state/` when empty. Outside
active work, new conversations reconstruct from the repository without a task
artifact.

## 12. Commit Hygiene

Keep commits coherent and reviewable. Never:

- commit without required approval;
- conceal failing or unrun checks;
- mix unrelated cleanup into the change;
- rewrite developer-owned history without explicit instruction;
- discard unrelated pre-existing work.

For the task workflow:

- commit accepted ADR-only technical direction before implementation when
  such ADRs are needed;
- create one coherent task commit for direct execution, or one commit per
  approved issue for issue-based execution;
- let the main agent create commits after review and approval;
- keep final task cleanup either trivial and clearly reported, or route it back
  through the selected execution path when non-trivial.

The final report before commit or PR work should make the actual diff and
verification state easy for the developer to review.

## 13. Adopting The Scaffold

When copying `Lean-Methodology/scaffold/` into a project:

1. install `AGENTS.md`, `CONTEXT.md`, and `.agent/` unchanged as reusable
   methodology; no `.agent-state/` directory is installed;
2. fill `docs/repository-map.md` and `docs/development-commands.md` with
   current project information;
3. fill template-backed live files under `docs/` while preserving their
   initial structure;
4. fill `docs/normative/architecture.md` with current system context, internal
   dynamics, and accepted boundaries;
5. populate `docs/normative/integrations/` for accepted external interactions,
   or leave its index explicitly empty;
6. keep `.devnotes/planning.md` only as optional developer-owned orientation;
   it is not agent context or a required setup artifact;
7. create or refresh root `README.md` from
   `.agent/docs/templates/root-readme.md`, using current project evidence and
   commands from `docs/development-commands.md`.

Upgrade an installed project by replacing only:

- `AGENTS.md`;
- `CONTEXT.md`;
- `.agent/`.

Then reconcile any changed templates with live project files deliberately.
Never overwrite `docs/` or `.devnotes/` as part of a methodology upgrade.
`.agent-state/` is outside the replacement set. Leave active current-task
artifacts untouched only when work is genuinely in progress; otherwise ensure
the directory does not exist.

Simplification is a governing constraint. Add durable artifacts or process
only when repeated evidence shows that agent attention, conversation, Git
history, short-lived current-task artifacts, and focused skills are
insufficient.

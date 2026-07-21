# Lean-DOX Hybrid Agentic Development Methodology

## 1. Purpose

This methodology is for software projects in which:

- product and business requirements live in the repository;
- one developer remains the strategist and final decision maker;
- one main coding agent owns the current line of work with substantial
  autonomy, using bounded disposable subagents for noisy supporting work;
- specifications may be ahead of implementation;
- the developer chooses either `AUTONOMOUS` or `SUPERVISED` mode for each
  substantive task;
- implemented technical behavior remains consistent across code, tests,
  executable contracts, architecture documentation, and external dependency
  contracts;
- sparse path-local agent guides reduce repeated discovery inside durable
  repository boundaries without replacing canonical project documentation.

The methodology deliberately trusts the agent's discernment, repository
awareness, and attention to detail. It uses a small number of durable sources
and focused skills instead of task directories, lifecycle records, or
historical spec snapshots. `SUPERVISED` mode keeps explicit developer review
points where early feedback prevents wrong direction, helps lower-effort
reasoning produce reliable results, or avoids wasteful verification and token
usage. `AUTONOMOUS` mode lets the agent make those methodology-level decisions
without interim review and report them at the end.

It preserves the Lean methodology's canonical documentation and workflow model
while adapting DOX's nested `AGENTS.md` hierarchy as a constrained, sparse
path-local routing layer. It does not adopt DOX's mutable root index or treat
the guide chain as a replacement for canonical repository documentation.

The reusable files are under `Lean-DOX-Hybrid-Methodology/scaffold/`.

## 2. Governing Model

The repository separates read-only methodology, temporary agent runtime state,
and mutable project state:

```text
read-only methodology:
  root AGENTS.md
  root CONTEXT.md
  .agent/

temporary agent runtime state:
  .agent-state/task-handoff.md

mutable project state:
  docs/
  specs/
  nested AGENTS.md local guides
  code and tests
```

The methodology is upgradable by replacing root `AGENTS.md`, root `CONTEXT.md`,
and `.agent/` together. Project-specific information must not be stored in
those methodology paths. Nested `AGENTS.md` files are mutable project-owned
local guides and are preserved during methodology upgrades. Temporary
active-task state lives separately under `.agent-state/`.

`docs/` contains repository orientation, commands, planning, conventions, and
normative technical documentation. `specs/` contains current product and
business intent. Selected
nested `AGENTS.md` files contain only path-local operational routing,
constraints, verification, and direct child-guide indexes.

Code is the primary authority for current system behavior because it determines
what actually runs. Permitted tests and executable contracts provide supporting
evidence. The repository map accelerates targeted exploration.
`docs/normative/` defines accepted technical intent.

Code is authoritative for what currently runs. `docs/normative/` is
authoritative for accepted technical intent. Active changes keep the two
matched as implementation and technical design evolve together.

Lean-DOX does not maintain end-user behavior documentation or prose
instructions for external consumers integrating with this system. Generate
those on demand or through a complementary methodology.

`docs/planning.md` is not canonical product truth and is not a task tracker.

### Read-Only Methodology

During normal project work, the agent may read but must not edit:

- root `AGENTS.md`;
- root `CONTEXT.md`;
- installed methodology under `.agent/`.

The main agent may create, update, and delete
`.agent-state/task-handoff.md` while a non-trivial task is active. This runtime
state is outside the methodology tree; `.agent/` remains fully read-only.

Methodology templates live under `.agent/docs/templates/` and
`.agent/specs/templates/`. The local-guide structural template and procedure
live under `.agent/local-guides/`. Mutable project files begin with or follow
their relevant blank structure. Agents update live project files and use
methodology templates only to preserve or restore structure.

Only an explicit methodology-upgrade request authorizes methodology edits.

### Product Intent And Technical State

Specifications may intentionally lead implementation. Therefore:

- a statement belongs in specs only when a product owner would assert it
  without choosing how the product is built and replacing the implementation
  would not make it false;
- product-level constraints may narrow implementation while still belonging in
  specs when they pass both tests;
- architecture candidates, technologies, internal models, algorithms,
  migrations, rollout mechanics, engineering sequencing, and test strategy are
  implementation reasoning, not product requirements;
- an unimplemented specification is not automatically a defect;
- implemented behavior must not contradict current specifications unless the
  discrepancy is explicitly known and awaiting a developer decision;
- code and tests must match `docs/normative/`;
- normative architecture records accepted structure and internal dynamics;
- normative decisions explain consequential choices and their rationale;
- normative integration contracts record external systems, authoritative
  references, and the exact contract surface used;
- completeness is judged against the scope the developer actually chose, not
  against every unimplemented specification.

### No Formal Task Management

There is no `.agent-state/tasks/` directory, active-task lock, task identifier,
template package, progress journal, acceptance table, or done-task archive.

Planning and execution form one conversational workflow. For an active
non-trivial multi-phase task, `.agent-state/task-handoff.md` preserves only
enough current state to cross phase boundaries or recover after compaction or
interruption. It is a single canonical overwrite-in-place handoff, not a task
record or history. It has no ID, owner field, lifecycle archive, acceptance
table, or completed-task retention, and it is deleted when work is completed
or abandoned. The `.agent-state/` directory is removed when empty and is never
committed.

### Current Specs Only

`specs/` contains only the current form of intended behavior. The methodology
does not create accepted-version snapshots or a `spec-history/` directory.
Git provides file history when prior wording or rationale must be inspected.

## 3. Core Rules

### 3.1 Work Mode Is Explicit

Each substantive task uses exactly one explicit work mode:

- `AUTONOMOUS`: the agent reads `.agent/skills/autonomous/SKILL.md`, makes
  methodology-level decisions without interim review gates, and reports
  important decisions, tradeoffs, verification, and residual risk at the end;
- `SUPERVISED`: the agent reads `.agent/skills/supervised/SKILL.md` and keeps
  the developer involved for significant plans, high-impact decisions, phase
  confirmations, and implementation review.

The developer must specify one mode in the prompt. If the prompt omits it, the
agent asks which mode to use before starting substantive work.

Mode controls methodology-level approval, review, confirmation, and phase
handoff behavior. It does not override external tool approvals, sandbox rules,
repository policies, credentials, legal/security constraints, local-guide
rules, or explicit developer instructions.

### 3.2 The Developer Is In Control

The agent investigates, plans, implements, verifies, documents, and reports.
The developer remains the strategist and final decision maker, but the selected
mode determines when the agent must stop for interim review.

The agent should challenge contradictions, weak assumptions, or unsafe plans
directly. In `AUTONOMOUS` mode it may choose among methodology-level options
itself; in `SUPERVISED` mode it should not silently replace the developer's
strategy with its own.

### 3.3 SUPERVISED Mode Keeps The Developer In The Loop

In `SUPERVISED` mode, the agent communicates at meaningful review points:

- after initial investigation, with its understanding and intended approach;
- after preparing a significant implementation plan, to obtain approval before
  editing application code;
- whenever a plan defines or changes architecture boundaries, even if the
  expected implementation diff is small;
- when a large plan may benefit from being split into ordered increments;
- when evidence invalidates an assumption or materially changes the approach;
- before any high-impact decision;
- before creating, reorganizing, or removing a broad local-agent-guide tree;
- after changing application code as approved, to obtain developer review
  before final verification, non-normative documentation, and conclusion;
- again whenever a finishing repair changes application code after the last
  approved review, unless the review is explicitly waived or batched;
- during long-running work, with concise progress updates;
- after verification, with evidence, omissions, and residual risk.

Small, straightforward, low-risk changes do not need a separate plan-approval
gate unless they define or change architecture boundaries. The post-code review
gate applies whenever application code was changed, unless the developer
explicitly waives or batches it.

These handoffs prevent wrong direction, support reliable lower-effort
execution, and avoid excessive tool, browser, and language-model usage when
the developer can review or verify the result more directly.

Whenever developer input is required, the agent first summarizes the relevant
evidence and then asks the concrete question that must be answered.

### 3.4 AUTONOMOUS Mode Continues Without Interim Review

In `AUTONOMOUS` mode, the agent should not stop for plan approval, phase
confirmation, post-implementation review, or high-impact methodology decision
gates. It makes the best decision from repository evidence, records important
decisions at phase boundaries, and reports decisions, tradeoffs, verification,
local-guide changes when relevant, and residual risk at the end.

The agent may still stop when continuing would violate external constraints,
explicit developer instructions, or a required tool approval that cannot be
obtained autonomously.

### 3.5 High-Impact Decisions Follow The Selected Mode

The agent must follow the selected work mode before:

- changing product intent or resolving ambiguous requirements;
- implementing a significant plan;
- materially broadening or changing the requested scope;
- defining or changing normative architecture boundaries or ownership;
- creating, reorganizing, or removing a broad local-agent-guide tree;
- adding or replacing dependencies, frameworks, external services, or
  infrastructure;
- changing public APIs or externally consumed contracts;
- changing the database schema or creating or applying migrations;
- making consequential security, privacy, authorization, or data-lifecycle
  choices;
- choosing among alternatives with materially different cost, lock-in,
  compatibility, or operational consequences;
- performing destructive operations, deployments, production actions, unusually
  expensive tool calls, or commits;
- initiating an unusually broad audit or verification pass.

The agent may make reversible, local implementation decisions when they follow
current specs, architecture, conventions, and the communicated approach.

### 3.6 Context Is Routed

Use `CONTEXT.md` files as maps, not encyclopedias.

- Start with root `AGENTS.md`, its required one-level project references, and
  root `CONTEXT.md`.
- Use the request, repository map, focused search, or available code
  intelligence to identify a likely target area.
- Before editing that area, read every nested `AGENTS.md` on the path from the
  repository root to the target. If the edit scope expands, read the newly
  applicable chain before editing it.
- Follow only routes relevant to the current work. Do not recursively load
  every local guide.
- Read broader specs or code when excluding them could hide an important
  dependency.
- Keep read-only methodology generic and stable.
- Put repeatable procedures in skills and durable system facts in specs or
  docs.

### 3.7 GitHub And Dev-Ops Tools

For GitHub operations, the installed scaffold briefly instructs agents to
prefer the GitHub CLI (`gh`) over GitHub MCP.

For deployment, release, infrastructure, environment, CI/CD, hosting, GitHub,
and other operational work, the methodology routes to
`.agent/skills/dev-ops/SKILL.md`. That skill carries the general preference for
available CLIs over MCP calls, local-guide context, and the operational
selected-mode approval or autonomous-decision reminders. The preference does
not apply to code exploration tools such as Codegraph and does not change
external approval requirements for deployments or production actions.

### 3.8 Path-Local Agent Guides

Nested `AGENTS.md` files are mutable project-owned local guides for selected
durable subtrees. They are a last-mile path router after the agent has used the
required first read and focused discovery to identify a likely work area.

A local guide may contain:

- precise covered and excluded paths;
- supported modification entry points;
- local constraints that change how an agent should work;
- protected, generated, vendored, migration, infrastructure, or
  security-sensitive paths;
- existing focused verification commands, working directories, and
  prerequisites;
- links to relevant canonical specs and docs;
- an index of direct child guides.

A guide must not become another home for product requirements, implemented
behavior, architecture rationale, accepted decisions, global conventions,
development commands, temporary planning, or task history. It may link to
those canonical sources and summarize only enough to route the agent.

Create a guide only when its directory is a durable boundary and at least one
meaningful signal exists:

- distinct ownership, dependency, permission, or side-effect rules;
- a distinct supported verification workflow or working directory;
- protected or generated content;
- several stable entry points agents repeatedly need to locate;
- child boundaries that need routing;
- repeated evidence of over-exploration or wrong-surface edits.

Do not create guides for every directory, obvious file listings, temporary
structure, or content already routed adequately by `docs/repository-map.md`.
Prefer roughly 1-2 KiB per guide and omit empty sections.

`docs/repository-map.md` indexes top-level local guides. Each nested guide
indexes only direct child guides. Root `AGENTS.md` remains generic and does not
contain mutable project indexes.

Use `maintain-local-agent-guides` for an explicit repository-wide
initialization or refresh. Agent-selected use remains focused on the current
change or a tightly bounded area. Broad creation or reorganization follows the
selected work mode before writes.

### 3.9 Main Agent And Disposable Subagents

The main agent is the decision thread and single writer. It owns:

- task intent and developer communication;
- product, scope, architecture, and implementation decisions;
- source, test, configuration, and project-documentation edits;
- `.agent-state/task-handoff.md`;
- the final report.

There must not be multiple main agents or concurrent writers working in the
same repository. Subagents are disposable workers for noisy bounded phases:
test execution, log and failure analysis, broad code search, external
documentation lookup, large-diff review, and similar evidence gathering.

Several read-only subagents may run concurrently when they all support the same
coherent line of work. Concurrency is an execution detail, not multiple lines
of ownership. Each subagent receives a narrow purpose, explicit scope, and
requested report shape. It must keep raw logs and bulk output in its own
context and return only decisions-relevant findings, evidence, commands and
results, files inspected, and unresolved questions.

Subagent reports should remain under roughly 100-150 lines unless the main
agent explicitly asks for more. They report purpose and scope, result, commands
and outcomes, key findings, relevant files inspected, incidental generated or
changed files, and the recommended next action. Subagents do not make final
decisions and do not intentionally edit tracked repository files or the
canonical handoff. If subagents are unavailable, the main agent follows the
same output discipline and retains only concise findings.

### 3.10 Phase Handoffs Replace Transcript Dependence

At meaningful boundaries in non-trivial multi-phase work, the main agent
updates `.agent-state/task-handoff.md`. The handoff contains only current:

- goal, phase, scope, and non-goals;
- decisions and constraints;
- implementation and observable-outcome summary;
- files changed;
- concise test and verification status;
- documentation status;
- unresolved risks or next action.

It is not a diary. Obsolete plans, failed attempts, raw logs, stack traces, and
superseded hypotheses are removed rather than accumulated.

Before starting a later phase, after context compaction, or when context feels
stale, the main agent reconstructs from current repository state and relevant
source, `git status`, the current diff, `.agent-state/task-handoff.md`, and the
latest concise verification or subagent report. Mental compaction and
remembered transcript are not the recovery substrate.

The handoff is updated before distinct transitions from investigation or
planning to implementation, implementation to verification, and verification
to documentation or final review. It is deleted after the final report is
reconstructed and the task is complete, or immediately when the task is
abandoned. Remove `.agent-state/` when empty so no residual runtime state
remains between tasks.

### 3.11 Changes Stay Coherent

The agent should work on one coherent line of work at a time. It may address a
small directly related defect discovered during implementation when doing so is
clearly necessary and low risk. It must not silently combine unrelated cleanup,
features, or refactoring.

Concurrent subagents do not violate this rule when every delegated question
supports the same main-agent-owned outcome.

If newly discovered work cannot be addressed without broadening scope, record
the essential concern in `docs/planning.md` and bring it to the developer's
attention through the selected work mode.

### 3.12 Verification Is Proportionate

Run the narrowest useful checks first and broaden according to risk.

- Run straightforward local checks without asking.
- Follow the selected work mode before checks that are unusually broad, costly,
  slow, or environmentally consequential.
- After two failed attempts to use the same verification path or tool, follow
  the selected work mode before investing more effort.
- Never claim a check passed unless it ran successfully.
- Report relevant checks not run and why.
- Do not invent low-value tests merely to satisfy a process.
- Do not create a `MANUAL-TESTING.md` file or another persistent manual-test
  worksheet unless the developer explicitly requests one.

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
|   |-- specs/
|   |   |-- CONTEXT.md
|   |   `-- templates/
|   |-- local-guides/
|   |   |-- CONTEXT.md
|   |   `-- template.md
|   |-- how-to.md
|   `-- skills/
|       |-- CONTEXT.md
|       `-- <skill>/SKILL.md
|-- .agent-state/  # temporary; absent when no task is active
|   `-- task-handoff.md
|-- docs/
|   |-- repository-map.md
|   |-- development-commands.md
|   |-- planning.md
|   |-- normative/
|   |   |-- README.md
|   |   |-- architecture.md
|   |   |-- decisions/
|   |   `-- integrations/
|   `-- conventions.md
|-- specs/
|   |-- README.md
|   |-- domain-language.md
|   `-- <domain-oriented spec files>
|-- src/
|   `-- AGENTS.md  # optional mutable local guide when justified
`-- tests/
```

Application directories are project-specific. The important boundary is that
root `AGENTS.md`, root `CONTEXT.md`, and `.agent/` are replaceable methodology,
while nested `AGENTS.md` files, `docs/`, `specs/`, source, tests, and project
configuration are project-owned. `.agent-state/` is not part of the
methodology upgrade package and must not persist after its active task ends.

## 5. Methodology And Agent Guidance Files

### 5.1 Root `AGENTS.md`

Root `AGENTS.md` is generic, read-only methodology. It points to
project-specific:

- `docs/repository-map.md`;
- `docs/development-commands.md`;
- `docs/normative/README.md`;
- `docs/conventions.md`;
- `docs/planning.md`;
- `specs/README.md`.

Whenever the agent reads root `AGENTS.md`, it must also read the required
direct project references and root `CONTEXT.md`. This is a required one-level
read, not recursive traversal. Further context, including applicable nested
guide chains, is loaded only when routed by the work.

### 5.2 Root `CONTEXT.md`

Root `CONTEXT.md` briefly explains the operating model and routes work to:

- `.agent/skills/dev-ops/SKILL.md` for deployment, release, infrastructure,
  environment, CI/CD, hosting, GitHub, or other operational work;
- `.agent/local-guides/CONTEXT.md` for nested guide loading and maintenance;
- `.agent/specs/CONTEXT.md`;
- `.agent/docs/CONTEXT.md`;
- `docs/planning.md`;
- `.agent/skills/CONTEXT.md`;
- the relevant workflow or focused skill.

It is generic read-only methodology and contains no project-specific state.

### 5.3 `.agent/`

Installed files in `.agent/` are read-only methodology:

- `.agent/skills/` contains reusable workflows;
- `.agent/docs/` routes documentation work and owns documentation templates;
- `.agent/specs/` routes specification work and owns specification templates;
- `.agent/local-guides/` defines nested guide scope, loading, content, and
  structural guidance;
- `.agent/how-to.md` explains developer usage.

There are no runtime-state exceptions inside `.agent/`.

### 5.4 Nested `AGENTS.md` Files

Nested `AGENTS.md` files outside the repository root are mutable project-owned
local guides. They:

- govern only their declared subtree;
- specialize but do not weaken root methodology or parent guidance;
- contain concise operational routing rather than substantive canonical
  project documentation;
- are loaded only when their path is relevant to likely edits;
- are preserved during methodology upgrades.

Their read-only procedure and structural template live under
`.agent/local-guides/`. The top-level index lives in
`docs/repository-map.md`; each guide indexes only direct child guides.

### 5.5 `.agent-state/`

`.agent-state/` is temporary agent runtime state outside the installed
methodology. During active non-trivial multi-phase work it may contain only:

- `.agent-state/task-handoff.md`.

The main agent owns this file. It is overwritten in place at phase boundaries,
never retained as history, and deleted when the task is completed or abandoned.
Never commit it. Remove `.agent-state/` when empty. Durable planning, product
intent, implemented facts, and decisions remain in their canonical project
paths.

### 5.6 Root `README.md`

The root README is a concise human-facing entry point. It provides project
identity and links to canonical specs, repository orientation, normative
technical docs, and `.agent/how-to.md` instead of duplicating them.

## 6. Specifications

`specs/` is the canonical current description of intended product and business
behavior.

- Follow read-only routing and rules in `.agent/specs/CONTEXT.md`.
- Apply both product-intent tests to requirements, examples, glossary terms,
  open questions, and explanatory prose.
- Organize specs by product area or understandable domain.
- Prefer natural-language headings over a global requirement-ID scheme.
- Keep canonical project terminology in `specs/domain-language.md`.
- Use `specs/README.md` as a map and identify important cross-cutting
  relationships.
- Keep coupled requirements together or make their relationship explicit.
- Preserve the template-defined structure of `specs/README.md` and
  `specs/domain-language.md`.

Use the `update-specs` skill for changes. It:

- edits the current spec set only;
- checks affected and coupled specs;
- separates implementation-independent product intent from technical design;
- updates the spec map and domain language when needed;
- routes accepted durable technical choices to `docs/normative/decisions/`;
- routes tentative alternatives and near-term technical reasoning to
  `docs/planning.md` while they remain useful;
- inspects relevant implementation consequences;
- follows the selected work mode when intent is ambiguous or high impact;
- does not create historical snapshots.

Git history may be inspected when prior wording matters, but historical states
are not maintained as methodology artifacts.

## 7. `docs/planning.md`

`docs/planning.md` is a short-lived orientation note for development. It may
contain:

- current development direction;
- likely next increments;
- an active ordered multi-item implementation plan when split execution is
  chosen under the active work mode;
- open decisions;
- temporary technical design impulses, alternatives, tradeoffs, and unknowns;
- important deferred concerns discovered during work;
- notes about where specs intentionally lead code or docs.

It must not become:

- a formal backlog;
- a task list with identifiers, owners, statuses, or lifecycle history;
- a progress journal;
- a duplicate of specs, architecture docs, issues, or Git history;
- a prerequisite for every change.

Update it only when a note is likely to matter beyond the current conversation.
Use short bullets. Remove stale, completed, superseded, or no-longer-useful
notes instead of archiving them.

`Technical Design Impulses` is a temporary, non-normative home for
implementation reasoning discovered during spec work or other planning. Detail
may be substantial when it preserves useful analysis, but entries are not
requirements, accepted architecture, or committed work. Once a consequential
technical choice is accepted and its rationale or consequences will matter
later, record it in `docs/normative/decisions/` and prune redundant planning
detail.

Decision records have no mandatory body template. They should make status,
scope, context, the decision, relevant alternatives, and consequences clear as
appropriate. Only accepted or superseded decisions belong in
`docs/normative/`; proposals remain in planning. Do not create a decision
record for every implementation thought.

An active multi-item plan is a permitted temporary exception to the usual
brevity. Record the outcome, constraints, ordered independently reviewable
items, current item, and verification focus. Temporary checkboxes may show which
item is current or complete while the plan is active. It exists so an agent can
execute straightforward increments reliably without repeatedly reconstructing
the whole plan. Remove it when the work is complete or abandoned; do not
preserve it as history.

Developer-maintained content must not be silently rewritten. If ownership is
unclear, propose the edit.

## 8. Unified Work Workflow

Use the `work-on-app` skill for non-trivial features, fixes, and refactoring.
The workflow is intentionally adaptive.

### 8.1 Orient

Read the relevant instructions, current specs, planning notes, implementation,
tests, contracts, docs, and architecture boundaries. Inspect enough evidence to
understand the request and likely impact without bulk-loading the repository.
After focused discovery identifies a likely edit area, read every nested
`AGENTS.md` on the path to it before editing. Load another guide chain only if
the likely edit scope expands.

When broad search, test reproduction, logs, external documentation, or similar
evidence gathering would be noisy, delegate bounded read-only questions to
subagents. Several may run concurrently when they support the same outcome.
The main agent keeps only their concise reports and validates material
conclusions against current repository evidence.

### 8.2 Frame The Work

Tell the developer:

- what the agent believes the requested outcome is;
- the intended implementation approach;
- important scope boundaries and non-goals;
- the likely verification approach;
- assumptions or high-impact decisions and how the selected work mode handles
  them.

Assess the plan before implementation:

- For a small, straightforward, low-risk change, the update may be sufficient
  and implementation may continue.
- For a significant application-code change or architectural change, follow
  the selected work mode before editing application code.
- If the plan is large, decide whether to split it into ordered,
  independently reviewable items according to the selected work mode.
- If incremental execution is chosen, write the accepted or autonomously
  selected plan to `docs/planning.md` before starting the first item.

Once a technical design is accepted under the selected work mode, update the
affected normative architecture, decision records, and integration contracts
before application-code implementation. Record the accepted semantics and
constraints that can responsibly be settled at this point;
implementation-specific paths, fixtures, and verification references may be
filled in as implementation establishes them. Tentative alternatives remain in
`docs/planning.md`. Straightforward changes that do not alter durable technical
intent need no normative-doc update.

For non-trivial multi-phase work, create or update
`.agent-state/task-handoff.md` before implementation with the goal, current
phase, scope, non-goals, decisions, constraints, intended change, and
verification focus.

### 8.3 Implement Attentively

Keep the change coherent and follow current architecture and conventions.
Maintain proportionate permitted automated-test coverage.

When evidence requires a material change in scope, design, dependency,
contract, migration, security behavior, or architecture, return to framing the
work. Settle the revised design under the selected mode and update affected
normative docs before resuming implementation. Local factual refinements that
do not change accepted intent may be recorded as implementation establishes
them.

For a split plan, implement one current item at a time. Keep the active plan
current and do not silently pull later items into the current change.

At meaningful implementation boundaries, replace stale handoff content with a
short current summary of observable outcomes, changed files, verification status,
and unresolved issues.

After changing application code as planned:

1. run only the inexpensive focused checks needed to avoid presenting an
   obviously broken diff;
2. summarize the implementation, deviations, changed files, and preliminary
   evidence;
3. in `SUPERVISED` mode, ask the developer to review and approve the
   implemented code before final verification, non-normative documentation,
   and conclusion;
   in `AUTONOMOUS` mode, continue and include that review-relevant summary in
   the final report.

In `SUPERVISED` mode, the developer may explicitly waive this review or
approve batching several small items under one review.

For split work, conclude and update the current item before selecting the next.
Follow the selected work mode before moving to the next item. In `SUPERVISED`
mode, the overall plan approval may cover later items, but each item's
post-code review still applies unless the developer approved batching.

Before final verification, reconstruct the phase from current repository
state, the actual diff, `.agent-state/task-handoff.md`, and concise
preliminary-check reports rather than relying on investigation or
implementation transcript.

### 8.4 Finish The Change

Use the `finish-change` skill for non-trivial changes. It coordinates focused
checks for:

1. correctness;
2. completeness relative to the chosen scope;
3. agreement between accepted technical intent, implementation, and project
   documentation.

If a repair during finishing changes application code after the last approved
review in `SUPERVISED` mode, summarize the repaired diff and obtain another
developer review before continuing. Repeat the gate whenever later work changes
the approved application code again, unless the developer explicitly waives or
batches that review.

Check applicable nested `AGENTS.md` files. Update the closest owning guide only
when the change altered local scope, supported entry points, constraints,
protected paths, focused verification, or direct child-guide routing. Ordinary
behavior changes do not require guide churn.

Then run proportionate verification. After it completes, perform a final
documentation pass over all non-normative project docs affected by the
completed implementation, including applicable local agent guides, not only
the repository map and development commands. Update them from final repository
evidence. Do not edit `docs/normative/` in this final step.

Then inspect the actual diff, update or prune `docs/planning.md`, and report:

- behavior changed;
- important files changed;
- tests created or changed, including their paths and purpose;
- whether each relevant test or test command ran, and its result;
- an explicit statement when no tests were created or changed;
- verification and results;
- manual scenarios worth exercising when automated evidence is insufficient;
- known omissions and why they are intentional;
- residual risk and unresolved decisions;
- applicable local guides changed, or why no update was required when relevant.

Use bounded read-only subagents for noisy test runs, failure analysis, or
large-diff review when useful. Their reports remain under roughly 100-150 lines
unless explicitly expanded. Before documentation or final reporting,
reconstruct from the current repository, final diff, handoff, and concise test
summary. Delete `.agent-state/task-handoff.md` after the final report is
reconstructed and the task is complete, then remove `.agent-state/` when
empty. If work is abandoned, remove normative changes introduced solely for
the abandoned design while preserving independently accepted technical intent.

## 9. Scope-Selected Assurance Skills

The three `ensure-*` skills preserve the full methodology's consistency goals
without imposing a formal task lifecycle.

### 9.1 Select Scope Before Inspection

Every `ensure-*` invocation uses exactly one mode:

- **current change**: the current diff or completed implementation increment
  and its directly affected surface;
- **selected area**: a named feature, subsystem, module, contract, path, spec
  section, documentation set, or outcome;
- **whole repository**: a systematic repository-wide audit.

If a standalone developer request does not make the mode and boundary clear,
the agent asks which mode to use before inspecting. It must not assume
current-change mode merely because recent work exists. A workflow such as
`finish-change` may explicitly supply current-change mode; no redundant
question is required.

Agent-selected use remains limited to current-change mode or one tightly
bounded directly affected area. Whole-repository mode requires an explicit
developer request in `SUPERVISED` mode or a recorded autonomous decision in
`AUTONOMOUS` mode. The agent must never silently expand from one mode to
another.

Selected-area and whole-repository checks begin with an inventory appropriate
to the skill, divide broad work into reviewable bounded passes, and report
coverage, exclusions, and unverifiable areas. A broad sample must not be
reported as a whole-repository audit.

### 9.2 Ensure Correctness

Checks that behavior is right for the selected scope:

- current specs and stated intent;
- edge cases and failure modes;
- security, authorization, privacy, and data integrity;
- architecture and contract adherence;
- external operations and data actually used, internal mappings, ignored
  provider data, unknown-field behavior, compatibility assumptions, and
  failure semantics;
- meaningful regression evidence;
- actual verification results.

It may repair small in-scope defects directly. Repairs that materially broaden
scope or require a high-impact decision follow the selected work mode.

Whole-repository mode inventories top-level subsystems, executable entry
points, public contracts, data stores and migrations, integrations, security
boundaries, and verification suites. It reports unverified areas and does not
claim exhaustive correctness when evidence is incomplete.

### 9.3 Ensure Completeness

Checks that the chosen increment is fully handled:

- all explicitly selected behavior and affected paths are addressed;
- necessary callers, states, errors, configuration, and cleanup are covered;
- tests or other evidence cover the intended outcome where allowed;
- partial delivery and exclusions are explicit and coherent;
- deferred essentials appear in `docs/planning.md` when they matter beyond the
  conversation.

It does not require implementing all current specs. A deliberately partial
increment may be complete for its agreed scope.

Whole-repository mode requires an explicit completion baseline. It inventories
product areas, entry points, specs, contracts, migrations, configuration,
tests, docs, and active planning claims, then reports coverage against that
baseline. It must not silently redefine completeness as "implement every
spec."

### 9.4 Ensure Docs Matched

Checks that accepted technical intent, implementation, and non-normative
project docs agree within the selected mode:

- active plans, delivery status, and technical design impulses in
  `docs/planning.md`;
- system context, internal dynamics, architecture boundaries, and durable
  decisions;
- external dependencies, authoritative references, exact used contract
  surfaces, data projections and mappings, compatibility assumptions,
  operational behavior, and verification;
- executable schemas and source contracts for externally consumed interfaces,
  configuration, and technical failure behavior;
- conventions and contributor guidance;
- root README navigation and development commands when affected;
- applicable nested local-guide routing and work constraints when affected.

Normative architecture, decisions, and integration contracts are accepted
technical intent. When implementation, tests, schemas, or executable contracts
disagree with them, the skill repairs the implementation side within its
authorized scope; it does not rewrite normative docs to legitimize existing
code. Non-normative repository maps, commands, planning notes, contributor
guidance, local agent guides, and README navigation are updated from their
canonical repository evidence.

The skill does not document unimplemented specs as current technical state and
does not create end-user behavior or public integration documentation.

The skill always reviews the whole of `docs/planning.md`, even in
current-change or selected-area mode, because stale planning state can
misdirect later work. Whole-repository mode inventories the repository's
documentation roots and indexes, tracks every discovered document as reviewed,
changed, excluded, generated, or unverifiable, and does not limit findings to
recent changes.

## 10. Planning Skills

### 10.1 Plan Feature Work

For a broad area, map current specs and implementation into a simple,
developer-readable direction:

- desired outcome and boundaries;
- current implementation baseline;
- coherent likely increments;
- dependencies and sequencing;
- assumptions, open decisions, risks, and intentionally deferred work.

Store only the useful durable remainder in `docs/planning.md`. When split
multi-item execution is accepted or autonomously selected, store that active
plan there before the first item begins. Do not create task identifiers,
owners, or historical lifecycle records.

Treat technical design impulses as candidates, not requirements. Validate them
against the current implementation and constraints. Promote accepted durable
choices to `docs/normative/decisions/`.

### 10.2 Planning Audit

Use a focused planning audit to check one selected area for:

- intended behavior that appears forgotten;
- `docs/planning.md` notes that are stale or contradicted;
- specs that conflict internally or with an accepted direction;
- implementation details presented as product requirements;
- accepted technical decisions stranded as temporary planning impulses;
- implementation that has caught up with or diverged from planning notes;
- missing developer decisions that materially block a credible next step.

An agent-initiated audit must remain narrowly scoped. A broad audit follows
the selected work mode.

## 11. Optional Skills

The scaffold includes these optional reusable procedures:

- `investigate-issue`: diagnosis-first bug investigation;
- `assess-change-impact`: focused analysis of dependencies, contracts, data,
  architecture, security, and operations before a consequential change;
- `code-review`: substantive review of the actual diff against the request,
  specs, communicated approach, and repository rules;
- `docs-refinement`: editorial improvement grounded in implementation evidence;
- `clarify-with-shared-language`: one-question-at-a-time clarification of
  terminology and design choices;
- `improve-codebase-architecture`: focused identification of deeper-module
  opportunities;
- `update-readme`: concise root README maintenance;
- `maintain-local-agent-guides`: initialize or refresh a sparse hierarchy of
  nested local guides from evidence-backed durable repository boundaries.

Methodology authors should add skills only when a procedure has recurring
value. Installed project agents must not add or modify skills during normal
project work. Avoid skills that merely rename ordinary attentiveness or
recreate task management.

### 11.1 Maintain Local Agent Guides

The skill has two modes:

- **initialization** surveys an explicitly selected repository or broad area,
  proposes the smallest useful initial guide tree, and follows the selected
  work mode before broad creation;
- **refresh** checks existing guides in the current change, a selected area, or
  an explicitly requested repository-wide scope, then updates stale content,
  proposes missing guides, and consolidates or removes guides that no longer
  justify their attention cost.

Both modes begin with structure, manifests, repository maps, architecture, and
verification roots, then inspect only enough representative code and docs to
confirm candidates. They do not recursively ingest all source by default.

The skill changes nested `AGENTS.md` files, their direct parent indexes, and
the top-level guide index in `docs/repository-map.md`. It does not edit
application code or distort canonical docs to make a guide proposal true.

## 12. Skill Design

Each `SKILL.md` uses Codex-compatible frontmatter:

- `name`: lowercase and hyphenated;
- `description`: what the skill does and when it should trigger.

Skills must be operationally self-contained:

- repeat the read-only methodology boundary;
- state required context and scope limits;
- define any nonstandard methodology concepts they use;
- identify selected-mode approval or autonomous-decision triggers;
- explain whether they diagnose, edit, or both;
- avoid assuming another skill has already been read;
- report missing methodology dependencies instead of inventing replacements.

Skills that edit project files must preserve the distinction between read-only
root methodology and mutable nested `AGENTS.md` files. They read applicable
guide chains before editing and change guides only when the skill's scope
authorizes local-guide maintenance.

Invocation modes are:

- **workflow-required**: the methodology names an objective trigger;
- **developer-requested**: the developer asks for the skill;
- **agent-selected**: the agent uses it because the current bounded work
  clearly benefits.

Assurance skills do not require separate permission when a workflow explicitly
applies them to the current change. Standalone ambiguous requests require scope
selection before inspection. Whole-repository agent-selected use follows the
selected work mode.

## 13. Documentation Boundaries

Follow read-only routing and template rules in `.agent/docs/CONTEXT.md`.

`docs/` contains mutable project state:

- repository map and development commands;
- current development planning;
- normative technical documentation under `docs/normative/`;
- configuration and technical failure behavior;
- stable conventions.

Nested `AGENTS.md` files are also mutable project state, but their canonical
scope is limited to path-local operational routing. They link to `docs/` and
`specs/` rather than duplicating substantive facts from them.

Do not store methodology instructions in `docs/`. Template-backed live files
must preserve the structure defined under `.agent/docs/templates/`.
`docs/planning.md` may contain temporary planning state, but speculative
planning must not be represented as accepted technical state elsewhere in
`docs/`.

Use `docs/normative/README.md` as the map for accepted technical intent. It
routes architecture, accepted decisions, and contracts with external systems.
Proposed technical direction remains in `docs/planning.md` until accepted.

When an external interaction is accepted or materially changed, update its
normative contract. Record authoritative references, the exact surface used,
internal mapping, ignored provider data, unknown-field behavior, compatibility,
operational behavior, and verification evidence.

Integration contracts describe this code's dependency on external systems.
They must not become instructions for external consumers integrating with this
system. Public user, operator, API-reference, and integration documentation is
outside Lean-DOX and should be generated separately.

Use `docs/repository-map.md` as the top-level local-guide index. Maintain local
guides through `.agent/local-guides/CONTEXT.md` and
`maintain-local-agent-guides`, not by placing project-specific content in root
`AGENTS.md`.

## 14. Conversation Continuity

Chat history is useful working context, but it is not guaranteed durable state.
During active non-trivial work, `.agent-state/task-handoff.md` is the canonical
phase-recovery substrate. It preserves current state only, while durable
information belongs in:

- product intent in `specs/`;
- implemented facts in code and tests;
- accepted technical intent in `docs/normative/`;
- a few still-relevant development notes in `docs/planning.md`;
- project-specific conventions in `docs/conventions.md`;
- path-local operational guidance in applicable nested `AGENTS.md` files.

Before a later phase, after automatic compaction, or in a new conversation
continuing active work, reconstruct from:

1. current repository state and relevant source;
2. `git status` and the current diff;
3. `.agent-state/task-handoff.md`;
4. the latest concise verification or subagent report.

Do not use the handoff as a durable fact store, progress journal, or substitute
for canonical specs, decisions, planning, code, tests, or docs. Delete it when
the task is completed or abandoned, and remove `.agent-state/` when empty.
Outside active work, new conversations reconstruct from the repository without
a task artifact.

## 15. Commit Hygiene

Keep commits coherent and reviewable. Never:

- commit without required approval or an explicit autonomous-mode instruction
  that authorizes commit work;
- conceal failing or unrun checks;
- mix unrelated cleanup into the change;
- rewrite developer-owned history without explicit instruction;
- discard unrelated pre-existing work.

The final report before commit should make the actual diff and verification
state easy for the developer to review.

## 16. Adopting The Scaffold

When copying `Lean-DOX-Hybrid-Methodology/scaffold/` into a project:

1. install root `AGENTS.md`, root `CONTEXT.md`, and `.agent/` unchanged as
   read-only methodology; no `.agent-state/` directory or handoff is
   installed;
2. fill `docs/repository-map.md` and `docs/development-commands.md` with current
   project information;
3. fill template-backed live files under `docs/` and `specs/` while preserving
   their initial structure;
4. fill `docs/normative/architecture.md` with system context, internal
   dynamics, and accepted boundaries;
5. populate `docs/normative/integrations/` for accepted external interactions,
   or leave its index explicitly empty;
6. keep `docs/planning.md` blank or brief until useful current notes emerge;
7. use `maintain-local-agent-guides` in initialization mode when the repository
   is large or modular enough to benefit, propose or autonomously record the
   sparse guide tree according to the selected mode, and create only
   evidence-backed guides;
8. use `update-readme` to create or refresh the root README.

Upgrade an installed project by replacing only:

- `AGENTS.md`;
- `CONTEXT.md`;
- `.agent/`.

Then reconcile any changed templates with live project files deliberately.
Never overwrite `docs/` or `specs/` as part of a methodology upgrade.
`.agent-state/` is outside the replacement set. Leave an active handoff
untouched only when work is genuinely in progress; otherwise ensure the file
and empty directory do not exist.

Nested `AGENTS.md` files are outside the replacement set. Preserve them and
reconcile changed local-guide methodology deliberately. Refresh their indexes
or content only when current repository evidence requires it.

Simplification is a governing constraint. Add durable artifacts or process
only when repeated evidence shows that agent attention, conversation, Git
history, and focused skills are insufficient.

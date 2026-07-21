# Developer Guide

This repository uses a Lean-DOX hybrid agentic development methodology with no
formal task system and no spec snapshots. It uses one temporary task handoff
only while multi-phase work is active and sparse nested `AGENTS.md` files for
path-local routing where durable repository boundaries justify them.

The installed methodology consists of root `AGENTS.md`, root `CONTEXT.md`, and
the installed `.agent/` directory. These paths are read-only during normal
project work and can be upgraded together without replacing project-specific
state in `docs/` or `specs/`. Temporary runtime state is kept separately at
`.agent-state/task-handoff.md`.

Nested `AGENTS.md` files are mutable project-owned local guides. They are not
replaced during methodology upgrades. `docs/repository-map.md` indexes
top-level guides, and each guide may index direct child guides.

## Core Usage

1. Keep repository paths, commands, normative technical docs, conventions, and
   planning current under `docs/`.
2. Keep intended product behavior current under `specs/`.
3. Specify exactly one work mode in the prompt: `AUTONOMOUS` or `SUPERVISED`.
   If you omit it, the agent asks before substantive work.
4. Ask the agent to investigate and implement features, fixes, or refactoring
   through one conversational workflow.
5. In `SUPERVISED` mode, expect review and approval gates for significant
   plans, high-impact decisions, split work, implemented app-code changes, and
   broad local-guide-tree changes.
6. In `AUTONOMOUS` mode, expect the agent to make those methodology-level
   decisions itself and report the decisions at the end.
7. Expect meaningful progress updates, explicit test reporting, and a final
   diff summary.
8. Keep `docs/planning.md` limited to short-lived orientation and deferred
   concerns that matter beyond the current conversation.
9. Use the agent to change `docs/normative/`; avoid editing normative technical
   docs manually because agents treat them as accepted technical intent and may
   change code to match them.
10. Expect one main agent to own decisions and edits. Read-only subagents may
    run concurrently for noisy work supporting the same coherent outcome.
11. Keep local agent guides sparse. Use them for stable entry points, local
    constraints, protected paths, focused verification, and child routing,
    while keeping substantive product and system facts in their canonical
    `specs/` and `docs/` homes.

Specs may be ahead of implementation. Completeness is evaluated against the
chosen increment, while code, tests/contracts, architecture, and integration
contracts must agree about technical behavior already built.

Code is the primary authority for what the system currently does. Permitted
tests/contracts provide supporting evidence. The repository map guides
navigation; `docs/normative/` defines accepted technical intent.

Avoid making manual changes under `docs/normative/`. Ask the agent to make
technical-design changes so it can assess and update the affected code, tests,
schemas, and normative docs together. Once the technical design is accepted,
the agent establishes affected normative docs during planning, before changing
application code. In `AUTONOMOUS` mode, expect the agent to act on normative
docs as accepted intent.

Near completion, the agent separately reviews every non-normative project doc
affected by the final implementation, including applicable local agent guides.
This final documentation pass may update repository maps, development commands,
conventions, contributor guidance, planning, README navigation, or future
non-normative docs, but it does not revise `docs/normative/`.

Lean-DOX does not maintain end-user behavior documentation or instructions for
external consumers integrating with this system. Generate those on demand or
through a complementary methodology.

Specs contain only statements a product owner would assert independently of
implementation and that would remain true if the implementation were replaced.
During spec work, route accepted technical choices with durable rationale to
`docs/normative/decisions/`. Keep tentative alternatives and near-term technical
reasoning under `docs/planning.md` > `Technical Design Impulses` only while
they remain useful.

## Work Modes

Use `SUPERVISED` when you want to stay in the loop for consequential product,
scope, architecture, dependency, public contract, migration, security, privacy,
operational, destructive, expensive, or broad local-guide-tree choices.

In `SUPERVISED` mode, the agent should also ask:

- before implementing a significant application-code plan;
- before implementing any plan that defines or changes architecture boundaries;
- whether a large plan should be split into ordered items;
- after changing application code as planned;
- again when a finishing repair changes application code after the last
  approved review;
- after two failed attempts with the same verification path, before investing
  more effort.

These reviews prevent wrong direction, support reliable execution at lower
reasoning effort, and avoid excessive token or browser-tool usage when the
developer can verify more efficiently.

Use `AUTONOMOUS` when you want the agent to decide those methodology-level
questions itself and continue without interim review gates. It should still
report important decisions, tradeoffs, verification, local-guide changes when
relevant, and residual risk at the end.

Work mode does not override external tool approvals, sandbox rules, repository
policies, credentials, legal/security constraints, local-guide boundaries, or
explicit instructions in your prompt.

For truly autonomous execution, make sure the agent environment allows it.
Codex, Claude Code, Cursor, and similar tools may still require confirmation
for edits, shell commands, network access, browser use, deployments, or other
actions depending on their current settings.

## Context Hygiene

The main agent is the single writer for production code, project docs, and the
canonical task handoff. Subagents are disposable workers for broad search,
tests, logs, external docs, failure analysis, and review. They may run
concurrently when all work contributes to the same feature, fix, or refactoring
and must return bounded reports of roughly 100-150 lines or less unless more is
explicitly requested.

For non-trivial multi-phase work, `.agent-state/task-handoff.md` carries only
current goal, phase, scope, decisions, implementation and observable-outcome
summary, changed files, concise test status, docs status, and unresolved risks.
Later phases recover from that file plus current repository state, the diff,
and concise verification reports. The file is not a history or task tracker
and is deleted when the task is completed or abandoned. The `.agent-state/`
directory is also removed when empty and is never committed.

## Explicit Steering

Lean-DOX stays small by leaving some work-style choices out of the auto-loaded
methodology. When one of those choices matters for the current task, steer it
explicitly in the prompt instead of relying on a repository flag.

Useful things to state explicitly:

- whether to create or run frontend tests, browser checks, or only suggest
  manual UI scenarios;
- whether a simple UI change should be verified by the developer visually
  instead of spending agent tokens on automated frontend coverage;
- whether to prioritize minimum token use, maximum confidence, or a balanced
  pass;
- whether to use a named skill for deeper assurance, broader impact analysis,
  guide maintenance, or documentation review.

This is especially relevant for frontend work. The best default for many
agents is to test UI behavior automatically, but simple visual changes can
sometimes be eye-balled by the developer in five seconds at zero token cost.
When that tradeoff matters, say so directly:

```text
AUTONOMOUS. Make this small UI adjustment. Do not create or run frontend
tests; I will verify it visually.
```

```text
SUPERVISED. This touches a risky checkout flow. Use browser-driven frontend
verification and report exactly what ran.
```

## Diff Review

Review the actual diff, not only the summary:

- Does it solve the selected outcome without unrelated work?
- Are important edge cases and failure modes handled?
- Were architecture, validation, authorization, and data boundaries preserved?
- Is verification credible for the risk of the change?
- Which tests were created or changed, did they run, and what were the results?
- Are intentional omissions explicit?
- Do normative technical docs match the implementation?
- Are all affected non-normative docs current?
- Do applicable nested `AGENTS.md` files still route agents to the right local
  entry points, constraints, and verification without duplicating canonical
  docs?

## Planning Notes

`docs/planning.md` may hold current direction, likely next increments, an
active ordered multi-item plan, open decisions, temporary technical design
impulses, deferred concerns, and known intent ahead of implementation.

Use an active plan only when split execution has been chosen under the active
work mode. Record the outcome, constraints, ordered items, current item, and
verification focus before starting the first item. Prune it when complete. Do
not add IDs, owners, completed-work history, or an exhaustive backlog.

Technical design impulses are non-normative. They may retain substantial
reasoning while alternatives are still live, but they are not requirements,
accepted architecture, or committed work. Promote accepted durable choices to
`docs/normative/decisions/`, then remove redundant planning detail.

The blank structure of `docs/planning.md` is defined by
`.agent/docs/templates/planning.md`. The agent may update live planning content
but must not edit the template or remove template-defined sections.

## Methodology Upgrades

Upgrade the methodology by replacing:

- root `AGENTS.md`;
- root `CONTEXT.md`;
- the `.agent/` directory.

Do not replace project-owned `docs/` or `specs/`. If a methodology upgrade adds
or changes a template, reconcile the corresponding live project file
deliberately while preserving project content.

Do not replace project-owned nested `AGENTS.md` files. Reconcile any changed
local-guide rules or template deliberately, preserving verified project
content and updating `docs/repository-map.md` only when the guide tree changes.

Use `.devnotes/` for private notes that agents should ignore. Do not place
required project context there.

## Conversation Continuity

During an active multi-phase task, a new or compacted conversation reconstructs
from current repository state, `git status`, the current diff,
`.agent-state/task-handoff.md`, relevant source, and concise verification
summaries. Outside an active task, reconstruction uses current specs, code,
tests, docs, Git history when needed, and useful orientation in
`docs/planning.md`.

## Useful Requests

```text
AUTONOMOUS. Implement <outcome>. Make methodology-level decisions yourself and
report important decisions, verification, and residual risk at the end.
```

```text
SUPERVISED. Implement <outcome>. Show me the implementation plan for approval
before changing app code, then stop again after the code changes for review.
```

```text
SUPERVISED. Update the current specs so that <intended behavior>. Do not
implement it.
```

```text
AUTONOMOUS. Use plan-feature-work for <area> and keep only the useful
near-term result in docs/planning.md.
```

```text
AUTONOMOUS. Run ensure-correctness in current-change mode.
```

```text
SUPERVISED. Run ensure-correctness in selected-area mode for <module,
behavior, contract, or spec section>.
```

```text
AUTONOMOUS. Run ensure-correctness in whole-repository mode.
```

```text
AUTONOMOUS. Run ensure-completeness in current-change mode. Complete means
<explicit outcome and accepted exclusions>.
```

```text
SUPERVISED. Run ensure-completeness in selected-area mode for <selected
outcome>. Complete means <explicit baseline>. This is intentionally a partial
delivery of <larger outcome>.
```

```text
AUTONOMOUS. Run ensure-completeness in whole-repository mode. Complete means
<explicit repository-wide baseline>.
```

```text
AUTONOMOUS. Run ensure-docs-matched in current-change mode.
```

```text
SUPERVISED. Run ensure-docs-matched in selected-area mode for <feature,
subsystem, path, or documentation set>.
```

```text
AUTONOMOUS. Run ensure-docs-matched in whole-repository mode and reconcile
implementation and project docs with accepted technical intent.
```

```text
SUPERVISED. Use dev-ops for <deployment, GitHub, CI/CD, hosting,
infrastructure, or environment operation>.
```

```text
SUPERVISED. Use maintain-local-agent-guides to initialize a sparse local guide
tree for this repository. Propose the candidate tree before creating it.
```

```text
AUTONOMOUS. Use maintain-local-agent-guides to refresh the guides under
<area>.
```

Whole-repository wording explicitly authorizes repository-wide assurance scope.
If an assurance request omits the mode or leaves its boundary ambiguous, the
agent asks whether to use current-change, selected-area, or whole-repository
mode before inspecting. Repository-wide guide initialization remains governed
by the separate guide-maintenance request above.

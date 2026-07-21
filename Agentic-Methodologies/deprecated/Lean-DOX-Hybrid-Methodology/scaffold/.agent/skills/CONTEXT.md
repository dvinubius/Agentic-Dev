# Agent Skills

Skills are focused reusable procedures. Governing methodology rules and routing
remain in root `AGENTS.md`, root `CONTEXT.md`, `.agent/docs/CONTEXT.md`, and
`.agent/specs/CONTEXT.md`.

This directory is the repository-owned canonical source. Each `SKILL.md` uses
Codex-compatible `name` and `description` frontmatter. Native implicit
discovery may require installing or linking these directories into a supported
`.agents/skills/` location.

## Invocation

- **Workflow-required**: the methodology defines an objective trigger.
- **Developer-requested**: the developer explicitly asks for the skill.
- **Agent-selected**: the agent chooses a skill because the current bounded
  work clearly benefits.

Using a skill means reading and following its `SKILL.md`, including its scope
limits and selected-mode approval or autonomous-decision triggers.

## Work Mode

Skills inherit the work mode selected under root `AGENTS.md`:

- `AUTONOMOUS`: read `autonomous/SKILL.md`.
- `SUPERVISED`: read `supervised/SKILL.md`.

Mode controls methodology-level approval, review, confirmation, and phase
handoff behavior for all skills.

## Read-Only Methodology Boundary

During normal project work, skills may read but must not edit:

- root `AGENTS.md`;
- root `CONTEXT.md`;
- installed methodology under `.agent/`.

The main agent may create, update, and delete
`.agent-state/task-handoff.md` as temporary runtime state outside `.agent/`, as
described in root `AGENTS.md`.

Skills edit live project files under `docs/`, `specs/`, source, tests, or other
project-owned paths, including nested `AGENTS.md` files when a skill explicitly
maintains local guides. When a template-defined project file needs structural
repair, read the corresponding template and restore the live file without
modifying the template.

## Assurance Scope Rule

Every `ensure-*` invocation uses one explicit mode: current change, selected
area, or whole repository. If a standalone developer request does not state a
clear mode and boundary, ask before inspecting. Workflow-required invocations
may pass the mode explicitly and do not require a redundant question.

Agent-selected use is limited to the current change or a tightly bounded
directly affected area. Whole-repository use follows the selected work mode.
Selected-area and whole-repository checks begin with an appropriate inventory,
use bounded passes, and report coverage, exclusions, and unverifiable areas.

## Routing

| Need | Skill |
|---|---|
| Work autonomously without interim methodology review gates | `autonomous/SKILL.md` |
| Work with developer review and approval gates | `supervised/SKILL.md` |
| Plan and execute a feature, fix, or refactoring | `work-on-app/SKILL.md` |
| Finish a non-trivial change coherently | `finish-change/SKILL.md` |
| Check correctness for a change, selected area, or the repository | `ensure-correctness/SKILL.md` |
| Check completeness against a declared scoped baseline | `ensure-completeness/SKILL.md` |
| Check technical docs and implementation for agreement | `ensure-docs-matched/SKILL.md` |
| Initialize or refresh nested local agent guides | `maintain-local-agent-guides/SKILL.md` |
| Change current product or business specs | `update-specs/SKILL.md` |
| Plan broad feature work without creating tasks | `plan-feature-work/SKILL.md` |
| Audit one planning area | `planning-audit/SKILL.md` |
| Diagnose a bug before changing behavior | `investigate-issue/SKILL.md` |
| Assess impact before a consequential change | `assess-change-impact/SKILL.md` |
| Review an actual diff for substantive problems | `code-review/SKILL.md` |
| Handle deployment, release, infrastructure, environment, CI/CD, hosting, GitHub, or operations | `dev-ops/SKILL.md` |
| Improve current documentation without runtime changes | `docs-refinement/SKILL.md` |
| Clarify a plan and shared terminology | `clarify-with-shared-language/SKILL.md` |
| Find focused architecture-deepening opportunities | `improve-codebase-architecture/SKILL.md` |
| Create or refresh the concise root README | `update-readme/SKILL.md` |

## Skill Design

Every skill must:

- state required context and scope limits;
- identify high-impact selected-mode approval or autonomous-decision triggers;
- explain whether it diagnoses, edits, or both;
- be usable without assuming another skill was already read;
- report missing methodology dependencies instead of inventing replacements.

Methodology authors add skills only after a procedure proves reusable.
Installed project agents do not add or modify skills during normal project
work. Do not recreate formal task management through skill outputs.

See `THIRD_PARTY_NOTICES.md` for adapted sources and licenses.

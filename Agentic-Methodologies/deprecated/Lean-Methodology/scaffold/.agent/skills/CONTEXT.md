# Agent Skills

Skills are focused reusable procedures. Governing methodology rules and routing
remain in root `AGENTS.md`, root `CONTEXT.md`, `.agent/docs/CONTEXT.md`, and
the selected skill.

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
limits and confirmation triggers.

## Project Files And Templates

When authorized by their scope, skills edit live project files under `docs/`,
source, tests, or other project-owned paths. When a template-defined project
file needs structural repair, read the corresponding template and restore the
live file's structure while retaining valid project-specific content.

## Routing

| Need | Skill |
|---|---|
| Plan and orchestrate a feature, fix, or refactoring | `work-on-task/SKILL.md` |
| Create a current-task PRD | `to-prd/SKILL.md` |
| Create current-task issues | `prd-to-issues/SKILL.md` |
| Finish one delegated issue | `finish-issue/SKILL.md` |
| Finish a non-trivial task coherently | `finish-task/SKILL.md` |
| Diagnose a bug before changing behavior | `investigate-issue/SKILL.md` |
| Assess impact before a consequential change | `assess-change-impact/SKILL.md` |
| Review an actual diff for substantive problems | `code-review/SKILL.md` |
| Clarify a plan and shared terminology | `clarify-with-shared-language/SKILL.md` |
| Find focused module-deepening opportunities | `deepen-modules/SKILL.md` |
| Refactor or review bounded code for maintainability while preserving behavior | `neatify-code/SKILL.md` |

## Conditional Application-Work Routing

During `work-on-task`, optional skills are not read by default. Read one only
when its trigger is present:

| Condition | Skill |
|---|---|
| Reproduction, expected behavior, root cause, affected surface, or regression evidence is uncertain enough that implementation would be speculative | `investigate-issue/SKILL.md` |
| A consequential proposed change may affect callers, persistent data, contracts, architecture boundaries, security, privacy, authorization, compatibility, operations, cost, or external systems, and the credible blast radius is unclear | `assess-change-impact/SKILL.md` |
| Ambiguous terminology, overloaded concepts, contradictory intent, or a material design branch blocks a precise plan | `clarify-with-shared-language/SKILL.md` |
| The work is explicitly architecture diagnosis, or evidence suggests a bounded deep-module refactoring candidate that needs design before code changes | `deepen-modules/SKILL.md` |
| The developer asks to neatify, simplify, clean up, refactor for maintainability, run a maintainability pass on changed code, or include maintainability-oriented evidence in review | `neatify-code/SKILL.md` |
| Finishing issue-based execution, the developer requests review, or the actual diff is large, risky, or cross-cutting enough to benefit from a dedicated review pass beyond normal finishing inspection | `code-review/SKILL.md` |

## Skill Design

Every skill must:

- state required context and scope limits;
- identify high-impact confirmation triggers;
- explain whether it diagnoses, edits, or both;
- be usable without assuming another skill was already read;
- report missing methodology dependencies instead of inventing replacements.

Methodology authors add skills only after a procedure proves reusable. Do not
recreate formal task management through skill outputs.

See `THIRD_PARTY_NOTICES.md` for adapted sources and licenses.

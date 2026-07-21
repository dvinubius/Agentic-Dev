# Project Context Router

This file and everything under `.agent/` are read-only methodology.
Temporary active-task state lives separately under `.agent-state/`.

## Operating Model

- `specs/` contains current product and business intent.
- `docs/` contains current project facts, development state, and implemented
  technical documentation.
- Code is the primary authority for current system behavior. Permitted
  tests/contracts provide supporting behavioral evidence. Documentation
  accelerates orientation but does not replace reading the implementation.
- Implementation-independent product assertions belong in specs. Accepted
  technical intent belongs in `docs/normative/`; proposed technical direction
  belongs in `docs/planning.md`.
- `.agent/` contains only read-only methodology routers, templates, skills, and
  references.
- Nested `AGENTS.md` files are mutable local project guides for selected
  durable subtrees.
- `.agent-state/task-handoff.md` is temporary state while a non-trivial task is
  active.
- Work mode is selected under root `AGENTS.md`; this router points to the
  corresponding mode skill.

## Routing

| Need | Methodology route | Project files |
|---|---|---|
| Work autonomously without interim methodology review gates | `.agent/skills/autonomous/SKILL.md` | current repository state and relevant task context |
| Work with developer review and approval gates | `.agent/skills/supervised/SKILL.md` | current repository state and relevant task context |
| Work on a feature, fix, or refactoring | `.agent/skills/work-on-app/SKILL.md` | relevant code, tests, specs, and docs |
| Finish a non-trivial change | `.agent/skills/finish-change/SKILL.md` | current diff and affected project files |
| Plan broad feature work | `.agent/skills/plan-feature-work/SKILL.md` | `docs/planning.md`, relevant specs and code |
| Read current development direction | `.agent/docs/CONTEXT.md` | `docs/planning.md` |
| Read or change product intent | `.agent/specs/CONTEXT.md` | `specs/README.md`, `specs/domain-language.md`, relevant specs |
| Work on technical project docs | `.agent/docs/CONTEXT.md` | relevant files under `docs/` |
| Read accepted technical intent | `.agent/docs/CONTEXT.md` | `docs/normative/README.md`, relevant normative docs, code, schemas, tests, and authoritative external references |
| Read current project conventions | `.agent/docs/CONTEXT.md` | `docs/conventions.md` |
| Read or maintain local agent guides | `.agent/local-guides/CONTEXT.md` | `docs/repository-map.md`, applicable nested `AGENTS.md` files |
| Initialize or refresh the local-guide tree | `.agent/skills/maintain-local-agent-guides/SKILL.md` | repository structure, existing guides, and guide indexes |
| Work on deployment, release, infrastructure, environment, CI/CD, hosting, GitHub, or operations | `.agent/skills/dev-ops/SKILL.md` | relevant configuration, scripts, workflows, operational docs, commands, and applicable local guides |
| Create or update the root README | `.agent/skills/update-readme/SKILL.md` | root `README.md` and linked project docs |
| Find a reusable procedure | `.agent/skills/CONTEXT.md` | as routed by the selected skill |
| Learn how the developer uses the methodology | `.agent/how-to.md` | none |

## Context Rules

- `AGENTS.md` requires one direct level of project references to be read.
- After that required read, load only context relevant to the current work.
- Before editing a likely target area, read every nested `AGENTS.md` on the
  path from the repository root to that target. Load another chain only if the
  edit scope expands.
- Do not recursively traverse linked files merely because links exist.
- Read broader specs or code when excluding them could hide a material
  dependency.
- Use `docs/repository-map.md` to locate implementation and
  `docs/normative/README.md` to route accepted technical intent. Neither
  substitutes for reading relevant code.
- Do not edit methodology paths during project work.
- Root `AGENTS.md` is methodology; nested `AGENTS.md` files are mutable project
  guides governed by `.agent/local-guides/CONTEXT.md`.
- The main agent may create, update, and delete
  `.agent-state/task-handoff.md`; it must not edit `.agent/`.
- Do not create task records, progress journals, or spec-history snapshots.

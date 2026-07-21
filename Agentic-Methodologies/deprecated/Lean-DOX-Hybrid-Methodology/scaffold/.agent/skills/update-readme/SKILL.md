---
name: update-readme
description: Create or update the repository root README.md as a concise onboarding page grounded in current specs, repository structure, normative technical docs, and development commands.
---

# Skill: Update README

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may maintain `.agent-state/task-handoff.md` as temporary
runtime state outside `.agent/`, as defined in root `AGENTS.md`.

The root `README.md` is a concise human-facing entry point. It is not the
canonical home for product requirements, architecture details, application
documentation, agent rules, or development planning.

## Required Context

Read:

- `../../../AGENTS.md`;
- `../../../CONTEXT.md`;
- existing `../../../README.md`, if present;
- `.agent/specs/CONTEXT.md`;
- `.agent/docs/CONTEXT.md`;
- `../../../docs/repository-map.md`;
- `../../../docs/normative/README.md`;
- `../../../docs/development-commands.md`;
- `../../../specs/README.md`;
- `../../how-to.md`;
- enough repository structure to validate links and identify the primary entry
  point.

## Procedure

1. Establish project name and a one- or two-sentence description from the
   existing README, current specs, repository structure, and implemented entry
   points.
2. Create or update the README with concise project, architecture,
   documentation, and development sections.
3. Copy usable development commands from `docs/development-commands.md`; it is
   authoritative for project commands.
4. Link instead of duplicating:
   - `specs/README.md`;
   - `docs/normative/README.md`;
   - `.agent/how-to.md`.
5. State briefly that the repository uses the Lean-DOX hybrid agentic
   development methodology.
6. Remove stale links, duplicated detail, transient planning, and obsolete
   commands.
7. Verify relative links and command consistency with
   `docs/development-commands.md`.

## Suggested Shape

````markdown
# <Project Name>

<One or two sentences describing the project.>

## Architecture

<Short summary and link to accepted technical documentation.>

## Documentation

- [Product specifications](specs/README.md)
- [Normative technical documentation](docs/normative/README.md)
- [Lean-DOX hybrid development guide](.agent/how-to.md)

## Development

```text
<current commands copied from docs/development-commands.md>
```
````

## Guardrails

- Keep the README brief and useful.
- Do not invent commands, behavior, or architecture.
- Do not copy specs, decision rationale, planning notes, or detailed docs.
- Do not expose secrets or private environment values.
- Do not read or reference `.devnotes/`.

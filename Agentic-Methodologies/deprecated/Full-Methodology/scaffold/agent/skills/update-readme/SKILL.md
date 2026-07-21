---
name: update-readme
description: Create or update the repository root README.md as a concise onboarding page that identifies the project, states that the agentic development methodology is used, links the methodology guide and relevant specs and docs, and mirrors current development commands from AGENTS.md. Use when the root README is missing, stale, or affected by changes to project identity, commands, architecture navigation, specs, or documentation entry points.
---

# Skill: Update README

## Methodology Context

The root `README.md` is a concise human-facing entry point. It is not the
canonical home for product requirements, architecture details, application
documentation, methodology procedures, or agent rules.

This repository uses the agentic development methodology represented by root
`AGENTS.md`, root `CONTEXT.md`, `specs/`, `agent/`, and `docs/`. The README must
state that the methodology is used because those paths and responsibilities are
part of the expected repository layout.

`../../tasks/CURRENT.md` is the active-task lock. If it names a task, use this
skill only when the README update serves that task.

## Engineer Handoffs

Whenever waiting for engineer confirmation, a decision, approval, or review,
end the response with the explicit question the engineer must answer. Put it in
a separate final paragraph and place no text after it.

## Required Context

Before editing:

- read `../../tasks/CURRENT.md`;
- read `../../../AGENTS.md`;
- read `../../../CONTEXT.md`;
- read the existing `../../../README.md`, if present;
- read `../../../specs/README.md` and `../../../specs/CONTEXT.md`;
- read `../../../docs/CONTEXT.md`;
- confirm that `../../how-to.md` exists;
- inspect only enough repository structure and linked files to validate the
  README links and identify the primary application entry point.

Read `../../../docs/architecture/boundaries.md` only when the architecture
summary in `AGENTS.md` is absent or insufficient for a one- or two-sentence
overview. Do not load all specs or docs merely to summarize them.

If a required methodology artifact is absent, report the missing dependency and
ask for direction rather than inventing a replacement.

## Procedure

1. Confirm that `CURRENT.md` permits the work.
2. Establish the project name and a one- or two-sentence project description
   from `AGENTS.md` and current repository evidence.
3. Create or update root `README.md` using the concise structure below.
4. Copy the usable development commands from `AGENTS.md`. Preserve command
   meaning and working-directory requirements. `AGENTS.md` remains authoritative
   when the two files disagree.
5. Link to relevant canonical entry points instead of repeating their contents:
   - `specs/README.md` for intended product behavior;
   - selected high-value docs identified through `docs/CONTEXT.md` for
     implemented-system documentation;
   - `docs/architecture/boundaries.md` for current architecture boundaries;
   - `agent/how-to.md` for using the agentic development methodology.
6. State briefly that the repository uses the agentic development methodology
   and that its layout follows the methodology's conventions.
7. Remove stale links, duplicated detail, transient status, task-specific
   information, and commands that no longer apply.
8. Verify every relative link and compare the development commands with
   `AGENTS.md`.
9. Report whether the README was created or updated, the links included, and any
   unresolved source inconsistency.

## README Shape

Use only sections that add current onboarding value:

````markdown
# <Project Name>

<One or two sentences describing the project.>

## Architecture

<One or two sentences at most, followed by a link to the canonical architecture
documentation.>

## Documentation

- [Product specifications](specs/README.md)
- [Implemented application behavior](docs/app-behavior/README.md)
- [Architecture boundaries](docs/architecture/boundaries.md)
- [Agentic development guide](agent/how-to.md)

This repository uses the agentic development methodology and follows its
repository-layout conventions.

## Development

<Working-directory or prerequisite note only when needed.>

```text
<current commands copied from AGENTS.md>
```
````

Adapt headings and link labels to the project, but preserve the same concise
responsibilities.

## Guardrails

- Keep the README brief and useful to a new contributor.
- Do not copy spec requirements, architecture rules, decision rationale, or
  application documentation into the README.
- Do not add badges, screenshots, contribution policy, license text, deployment
  instructions, or lengthy setup guidance unless the engineer requests them or
  the repository already treats them as essential onboarding.
- Do not expose secrets or private environment values.
- Do not invent commands, supported environments, behavior, or architecture.
- Do not treat the README as an agent router or replace `AGENTS.md`,
  `CONTEXT.md`, or `agent/how-to.md`.
- Do not read or reference `.devnotes/`.

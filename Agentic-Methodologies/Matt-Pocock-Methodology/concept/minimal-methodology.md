# Minimal Methodology

Earlier notes on Matt Pocock's workflow for a strategic developer. Skill names
and setup steps below may have changed; use Matt's maintained skills for the
current workflow. See the [workflow notes](matt-pocock-workflow.md) for my
reasoning about specs, docs, and TDD.

Within 1 session, issues are created. Potentially GH integrated.

In separate subsequent sessions, issues are tackled & PRs result from there.

## Components

- AGENTS.md
- CONTEXT.md
- skills
  - grill-with-docs
  - to-prd
  - to-issues
  - triage
  - implement
  - improve-codebase-architecture

## Getting started

Quick start guide from skills repo. Install skills in project then run setup skill. Configures:
- issue tracker
- ticket labels
- where to save docs

## Key Elements

- Planning is the heavy lifting and requires HITL, Execution can be AFK
- Good Planning requires
  - solid alignment btw. agent & dev, to clarify intent
  - tracer bullet issues
  - dev keeps the code in mind at all times, even during prd creation
- Good software architecture means token efficient work
- Prefers TDD for better feedback loops
- `docs/` are minimal
- `README.md` is minimal
- domain language glossary is part of `CONTEXT.md`

## Steps

1. Idea 
2. (optional) Research
3. (optional) Prototype
4. PRD
5. Kanban
6. Execution
7. QA / Review

## Additional elements

- Fallow for JS/TS projects

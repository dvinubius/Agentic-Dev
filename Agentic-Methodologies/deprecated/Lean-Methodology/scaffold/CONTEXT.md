# Project Context Router

## Routing

| Need | Methodology route | Project files |
|---|---|---|
| Work on a feature, fix, or refactoring | `.agent/skills/work-on-task/SKILL.md` | PRD, optional issues, relevant code, tests, and docs |
| Create a current-task PRD | `.agent/skills/to-prd/SKILL.md` | `.agent-state/current-task/PRD.md` |
| Create current-task issues after issue-based execution is selected | `.agent/skills/prd-to-issues/SKILL.md` | `.agent-state/current-task/issues/` |
| Finish one delegated issue | `.agent/skills/finish-issue/SKILL.md` | delegated issue, current diff, affected project files |
| Finish a non-trivial task | `.agent/skills/finish-task/SKILL.md` | PRD, optional issues, commits, current diff, affected project files |
| Work on technical project docs | `.agent/docs/CONTEXT.md` | relevant files under `docs/` |
| Read accepted technical intent | `.agent/docs/CONTEXT.md` | `docs/normative/README.md`, relevant normative docs, code, schemas, tests, and authoritative external references |
| Read current project conventions | `.agent/docs/CONTEXT.md` | `docs/conventions.md` |
| Create or update the root README | `.agent/docs/CONTEXT.md` and `.agent/docs/templates/root-readme.md` | root `README.md`, `docs/development-commands.md`, `docs/normative/README.md`, `.agent/how-to.md`, and linked project docs |
| Find a reusable procedure | `.agent/skills/CONTEXT.md` | as routed by the selected skill |
| Learn how the developer uses the methodology | `.agent/how-to.md` | none |

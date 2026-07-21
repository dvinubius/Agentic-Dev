# Agent Instructions

## Routing

Load only the route and project context needed for the work.

| Need | Route |
|---|---|
| Create or update the current-task PRD | `.agent/skills/to-prd/SKILL.md` |
| Create optional issues from an approved PRD | `.agent/skills/prd-to-issues/SKILL.md` |
| Execute an approved PRD with waived review points | `.agent/skills/execute-prd-afk/SKILL.md` |
| Implement one current-task issue | `.agent/skills/implement-issue/SKILL.md` |
| Create or update the PR and check PRD conformity | `.agent/skills/finish-task/SKILL.md` |
| Diagnose uncertain behavior before planning a fix | `.agent/skills/investigate-issue/SKILL.md` |
| Assess an unclear consequential blast radius | `.agent/skills/assess-change-impact/SKILL.md` |
| Clarify or stress-test a plan, design, or shared language | global `grill-with-docs` skill |
| Review and gate completed work before push | global [`no-mistakes`](https://github.com/kunchenguid/no-mistakes) skill |
| Work on project documentation | `.agent/docs/CONTEXT.md` |

Project references, read only when relevant:

- `CONTEXT.md`: optional project glossary; read only when project-specific
  language matters or a term is unclear.
- `docs/repository-map.md`: stable paths and responsibilities.
- `docs/development-commands.md`: development and verification commands.
- `docs/adr/`: accepted decisions, when present.
- `docs/normative/README.md`: accepted architecture and integration intent.
- `docs/conventions.md`: current conventions.

If a routed global skill is unavailable, report that instead of recreating it.

## Operating Model: Code vs. Docs

- Code is the primary authority for current system behavior. Tests/contracts
  provide supporting behavioral evidence. Documentation accelerates orientation
  but does not replace reading the implementation.
- `docs/` contains current project facts, development state, implemented
  technical documentation, accepted technical intent.
- Ignore `specs/` unless instructed otherwise.
- Ignore `.devnotes/`unless instructed otherwise.

## Agent Workflow

- Don’t assume. Don’t hide confusion. Surface tradeoffs.
- Minimum code that solves the problem. Nothing speculative.
- Touch only what you must. Clean up only your own mess.
- Define success criteria. Loop until verified.
- Avoid expensive or risky work without confirmation.
- Stop and ask before running destructive operations, deployments,
  production actions, unusually broad verification, expensive tool calls, or
  creating commits.

Never claim a command passed unless it ran successfully.

## Never

- Do not broaden scope silently.
- Do not bypass architecture, validation, authorization, or data-access layers.
- Do not skip or conceal failing checks.
- Do not revert, overwrite, or discard unrelated pre-existing work.
- Do not hand-edit generated or vendored files unless explicitly maintained.
- Do not expose credentials, tokens, secrets, or private environment values.

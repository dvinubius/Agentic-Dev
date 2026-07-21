# Agent Instructions

## Project References

Use these as routing entry points, then load only the context relevant to the
current work.

- Top-level routing: `CONTEXT.md`
- Repository map: `docs/repository-map.md`
- Development and verification commands: `docs/development-commands.md`
- Accepted technical intent: `docs/normative/README.md`
- Current conventions: `docs/conventions.md`
- Canonical domain language: `docs/domain-language.md`
- Project documentation methodology: `.agent/docs/CONTEXT.md`
- Skill routing: `.agent/skills/CONTEXT.md`

## Operating Model: Code vs. Docs vs. Methodology

- Code is the primary authority for current system behavior. Permitted
  tests/contracts provide supporting behavioral evidence. Documentation
  accelerates orientation but does not replace reading the implementation.
- `docs/` contains current project facts, development state, implemented
  technical documentation, accepted technical intent, and conventions.
- Accepted technical intent belongs in `docs/normative/`.
- `.agent/` contains methodology routers, templates, skills, and references.
- `.agent-state/current-task/` holds short-lived PRD, optional issue, and
  concise report artifacts while a non-trivial task is active.
- Ignore `specs/` if it is present.
- Ignore `.devnotes/`: do not read, search, modify, or treat it as context
  unless explicitly instructed by the developer.

## Agent Workflow

- Use `.agent/skills/work-on-task/SKILL.md` for non-trivial application work.
  If `.agent-state/current-task/` exists, treat it as active non-trivial task
  state and follow that skill before resuming.
- Only load routed context needed for the work.
- Don’t assume. Don’t hide confusion. Surface tradeoffs.
- Minimum code that solves the problem. Nothing speculative.
- Touch only what you must. Clean up only your own mess.
- Define success criteria. Loop until verified.
- Stop and ask before running destructive operations, deployments, production
  actions, unusually broad verification, expensive tool calls, or creating
  commits. When asking, first summarize the evidence, options, recommendation, 
  and practical consequence.

## Dependency Policy

- Before installing any package, verify that the package version is at least
  two weeks old. If it is newer, do not install it and report the reason.

## Never

- Do not claim a command passed unless it ran successfully.
- Do not bypass architecture, validation, authorization, or data-access layers.
- Do not skip or conceal failing checks.
- Do not hand-edit generated or vendored files unless explicitly maintained.
- Do not expose credentials, tokens, secrets, or private environment values.
- Do not silently edit content marked as developer-maintained.
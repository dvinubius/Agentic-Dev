# Application Documentation

`docs/` describes the application and implemented system. It is not the home of
the agentic methodology or repository-usage instructions.

## Routing

| Need | Location |
|---|---|
| User-, operator-, or system-visible implemented behavior | `app-behavior/` |
| Current normative architecture boundaries | `architecture/boundaries.md` |
| Important accepted architecture or implementation decisions | `decisions/` |
| Durable code and documentation conventions | `conventions.md` |
| Refine documentation without changing behavior | `../agent/skills/docs-refinement/SKILL.md` |
| Audit docs against code and tests | `../agent/skills/drift-audit/SKILL.md` |
| Find opportunities to consolidate shallow modules | `../agent/skills/improve-codebase-architecture/SKILL.md` |

Add project-specific rows as documentation grows.

## Documentation Rules

- Describe actual implemented behavior, not merely planned behavior.
- Validate behavior claims against code, tests, contracts, or runtime evidence.
- Update docs during task execution when behavior, contracts, architecture, or
  conventions change.
- Treat `architecture/boundaries.md` as normative and keep it synchronized with
  code changes that alter documented architectural boundaries.
- Keep one canonical home for each durable fact.
- Prefer links over duplicated explanations.
- Mark historical or proposed content clearly so it cannot be mistaken for
  current behavior.
- Use canonical project-specific terminology from
  `../specs/domain-language.md`; do not turn routing `CONTEXT.md` files into
  glossaries.

## Architecture

`architecture/boundaries.md` records the current architecture baseline. An
approved task may intentionally change it, and task execution must update the
file when that change is implemented. Decision records explain durable adopted
choices and their rationale. Other architecture documentation may be added when
useful, but it must not duplicate or contradict the current boundaries file.

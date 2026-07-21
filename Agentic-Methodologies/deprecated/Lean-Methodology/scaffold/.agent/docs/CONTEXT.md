# Project Documentation Methodology

This file routes documentation work. Mutable project documentation and
canonical terminology primarily live under root `docs/`; the concise root
`README.md` is also routed here because it is template-backed documentation.

## Routing

| Need | Live project file or area | Template |
|---|---|---|
| Concise project entry point | `README.md` | `templates/root-readme.md` |
| Stable repository paths and responsibilities | `docs/repository-map.md` | `templates/repository-map.md` |
| Development and verification commands | `docs/development-commands.md` | `templates/development-commands.md` |
| Canonical project terminology | `docs/domain-language.md` | `templates/domain-language.md` |
| Normative technical index | `docs/normative/README.md` | `templates/normative-readme.md` |
| Accepted architecture | `docs/normative/architecture.md` | `templates/architecture.md` |
| External integration index | `docs/normative/integrations/README.md` | `templates/integrations-readme.md` |
| Contract with one external system | `docs/normative/integrations/<system>.md` | `templates/integration-contract.md` |
| Durable project conventions | `docs/conventions.md` | `templates/conventions.md` |
| Accepted decision index | `docs/normative/decisions/README.md` | `templates/decisions-readme.md` |

## Rules

- Edit live project files during normal project work and use templates as
  structural references.
  - `.agent/docs/templates/` contains canonical templates for project docs.
  - When a template-backed project documentation file drifts structurally,
    restore its intended shape from the corresponding template without
    replacing valid project-specific content.
- Preserve the live file's template-defined headings and structural shape.
- Replace placeholders with project content; do not delete empty structural
  sections merely because they have no current entries.
- Keep root `README.md` concise and link-oriented. Use it for project identity,
  a short architecture pointer, documentation links, and current development
  commands copied from `docs/development-commands.md`.
- Keep `docs/repository-map.md` limited to stable, high-value paths rather than
  temporary work files or exhaustive listings.
- Keep `docs/development-commands.md` synchronized with the supported toolchain,
  working directories, required services, and actual commands. Remove command
  rows that do not apply.
- When structure drifts, compare with the template and restore the shape while
  retaining valid project-specific content.
- Keep documentation focused on codebase orientation, accepted technical
  structure, internal dynamics, and contracts with external dependencies.
- Do not maintain end-user behavior narratives or instructions for external
  consumers integrating with this system. Generate those separately when
  needed.
- Use code as the primary authority for implemented details and permitted
  tests/contracts as supporting evidence. Documentation should make the
  implementation faster to locate, assess, and verify, not replace reading it.
- Treat `docs/normative/` as accepted technical intent and keep relevant code,
  tests, schemas, and configuration matched with it.
- Record accepted durable technical decisions as ADRs before issue subagents
  execute when those decisions are needed for task alignment. Keep architecture
  and integration docs accurate to the implementation that currently exists;
  update them as issues change code rather than describing future planned
  behavior.
- Use `docs/normative/integrations/README.md` as the map for systems this code
  explicitly interacts with. Create or update an integration contract when an
  accepted change adopts or materially changes such an interaction.
- Integration contracts must identify authoritative external references and
  the exact surface this code uses, including consumed and produced data,
  internal mappings, ignored provider data, unknown-field behavior,
  compatibility assumptions, failure handling, and verification evidence.
- Do not use integration contracts as public instructions for consuming this
  system. Externally consumed interfaces should have executable schemas or
  source contracts near the implementation; link to them from architecture or
  repository documentation when useful.
- Use the repository map to find relevant code and the normative index to find
  accepted technical intent. Neither substitutes for reading implementation.
- Use `docs/normative/decisions/README.md` as the index for accepted decisions
  whose rationale and consequences will matter later.
- Keep one canonical home for each durable fact and prefer links over
  duplication.
- Use canonical terminology from `docs/domain-language.md`.
- Record accepted technical choices in `docs/normative/decisions/` when their
  rationale and consequences will matter later. No fixed ADR body template is required;
  make context, decision, alternatives when useful, consequences, status, and
  scope clear.

## Skills

- Module deepening:
  `../skills/deepen-modules/SKILL.md`

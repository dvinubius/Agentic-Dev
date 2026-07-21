# Project Documentation Methodology

This file and `templates/` are read-only methodology. Mutable project
documentation lives under root `docs/`.

## Routing

| Need | Live project file or area | Read-only template |
|---|---|---|
| Stable repository paths, responsibilities, and top-level local-guide index | `docs/repository-map.md` | `templates/repository-map.md` |
| Development and verification commands | `docs/development-commands.md` | `templates/development-commands.md` |
| Current development direction and active split plan | `docs/planning.md` | `templates/planning.md` |
| Normative technical index | `docs/normative/README.md` | `templates/normative-readme.md` |
| Accepted architecture | `docs/normative/architecture.md` | `templates/architecture.md` |
| External integration index | `docs/normative/integrations/README.md` | `templates/integrations-readme.md` |
| Contract with one external system | `docs/normative/integrations/<system>.md` | `templates/integration-contract.md` |
| Durable project conventions | `docs/conventions.md` | `templates/conventions.md` |
| Accepted decision index | `docs/normative/decisions/README.md` | `templates/decisions-readme.md` |

## Rules

- Edit live project files, never their templates, during normal project work.
- Preserve the live file's template-defined headings and structural shape.
- Replace placeholders with project content; do not delete empty structural
  sections merely because they have no current entries.
- Keep `docs/repository-map.md` limited to stable, high-value paths rather than
  temporary work files or exhaustive listings.
- Keep its `## Local Agent Guides` table limited to top-level nested
  `AGENTS.md` files. Deeper guides are indexed by their direct parent guide.
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
  whose rationale and consequences will matter later. Proposed decisions stay
  in `docs/planning.md`.
- Keep one canonical home for each durable fact and prefer links over
  duplication.
- Use canonical terminology from `specs/domain-language.md`.
- Keep `docs/planning.md` current and temporary; do not preserve completed plan
  history.
- Use `## Technical Design Impulses` for useful non-normative implementation
  reasoning discovered before or during spec work. Detail is allowed, but
  distinguish assumptions, alternatives, tradeoffs, and unknowns. Do not treat
  entries as requirements, accepted architecture, or committed work.
- Record accepted technical choices in `docs/normative/decisions/` when their
  rationale and consequences will matter later. No fixed ADR body template is
  required; make context, decision, alternatives when useful, consequences,
  status, and scope clear.
- Promote settled durable impulses to decision records and prune duplicated,
  stale, implemented, abandoned, or superseded planning detail.
- When no multi-item plan is active, reset the placeholders under
  `## Active Multi-Item Plan`; do not remove the template-defined section.

## Skills

- Technical documentation and implementation matching:
  `../skills/ensure-docs-matched/SKILL.md`
- Editorial refinement:
  `../skills/docs-refinement/SKILL.md`
- Architecture improvement:
  `../skills/improve-codebase-architecture/SKILL.md`
- Root README maintenance:
  `../skills/update-readme/SKILL.md`
- Local agent-guide initialization and refresh:
  `../skills/maintain-local-agent-guides/SKILL.md`

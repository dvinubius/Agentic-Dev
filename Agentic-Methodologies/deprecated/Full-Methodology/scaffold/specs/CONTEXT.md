# Specifications

`specs/` is the canonical home of intended product and business behavior.

## Routing

| Need | Read or update |
|---|---|
| Understand the spec set | `README.md` |
| Use or refine canonical project terminology | `domain-language.md` |
| Work on one product area | the mapped domain file(s) in `README.md` |
| Inspect accepted history when prior accepted intent or rationale is relevant | `spec-history/README.md` and the relevant snapshot |
| Change current product or business intent | `../agent/skills/update-specs/SKILL.md` |
| Audit specs against tasks or implementation | `../agent/skills/planning-audit/SKILL.md` |

## Organization

- Use natural-language headings rather than global requirement IDs.
- Use canonical project-specific terms from `domain-language.md`.
- Split by independently understandable product area or domain.
- Treat roughly 300 lines as a signal to consider splitting, not a limit.
- Keep coupled requirements together or make their relationship explicit in
  `README.md`.
- Read broader specs when excluding them could hide a relevant dependency.

## Change Governance

Use `../agent/skills/update-specs/SKILL.md` for the repeatable spec-change
procedure.

Every accepted change must keep the live spec set and its map consistent,
preserve canonical terminology, surface conflicts with open tasks, and create a
complete accepted snapshot under `spec-history/`. Do not silently rewrite or
delete affected tasks.

Normally, live specs represent the latest accepted version. Do not read the
latest snapshot merely to duplicate them. Read historical content only when
accepted intent must be distinguished from pending edits, an interrupted update
must be recovered, removed or materially changed intent must be understood, or
relevant historical rationale is needed.

Spec work is flexible and does not use task-execution gates, but unresolved
intent and conflicts still require engineer decisions.

## Relationship To Tasks

Feature tasks link relevant spec files and headings, then restate only their
task-local requirements as `REQ-NNN` entries for traceability.

Specs may be ahead of implementation. An unimplemented spec is not an Omni-Sync
failure by itself.

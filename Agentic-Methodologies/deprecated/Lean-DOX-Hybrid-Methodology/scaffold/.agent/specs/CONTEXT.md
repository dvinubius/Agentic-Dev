# Specification Methodology

This file and `templates/` are read-only methodology. Mutable current
specifications live under root `specs/`.

## Routing

| Need | Live project file or area | Read-only template |
|---|---|---|
| Understand and map the current spec set | `specs/README.md` | `templates/README.md` |
| Use or refine canonical terminology | `specs/domain-language.md` | `templates/domain-language.md` |
| Work on one product area | mapped file under `specs/` | create a focused domain file using current spec conventions |
| Change product intent | relevant files under `specs/` | follow `../skills/update-specs/SKILL.md` |

## Rules

- Edit live specs, never templates, during normal project work.
- Preserve template-defined headings in `specs/README.md` and
  `specs/domain-language.md`.
- Keep only current intent; do not create methodology-managed snapshots.
- Put a statement in specs only when both are true:
  - a product owner would assert it without choosing how the product is built;
  - replacing the implementation would not make the statement false.
- Product-level constraints remain valid spec content when they pass those
  tests, even if they constrain implementation.
- Do not put implementation plans, architecture candidates, technologies,
  internal data models, module boundaries, algorithms, migrations, rollout
  mechanics, or engineering sequencing in specs merely because they arose
  while reasoning about product intent.
- Route useful technical reasoning from spec work by maturity:
  - record an accepted technical decision in `docs/normative/decisions/` when its
    rationale and consequences will matter later;
  - keep tentative alternatives, unresolved design questions, and near-term
    implementation impulses under
    `docs/planning.md` > `Technical Design Impulses`.
- Planning impulses are non-normative implementation input, not requirements,
  accepted architecture, or committed work. Promote a settled durable choice
  to a decision record and remove duplicated planning detail.
- Use natural-language headings rather than global requirement IDs.
- Keep coupled requirements together or make relationships explicit.
- Read broader specs only when excluding them could hide a material dependency.
- An unimplemented spec is not itself an implementation defect.

## Skills

- Spec changes: `../skills/update-specs/SKILL.md`
- Planning audit: `../skills/planning-audit/SKILL.md`
- Shared-language clarification:
  `../skills/clarify-with-shared-language/SKILL.md`

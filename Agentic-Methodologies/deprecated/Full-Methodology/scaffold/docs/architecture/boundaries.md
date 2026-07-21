# Architecture Boundaries

This file is the normative source for the implemented system's current
architectural boundaries. Keep it synchronized with code changes that alter
responsibilities, dependency directions, ownership, or cross-cutting behavior.
An approved task plan may intentionally change these boundaries; until that
change is implemented and documented, this file remains the current baseline.

Document current architecture here. Record planned architecture in task plans,
and use decision records under `docs/decisions/` when the rationale and
tradeoffs of an adopted choice need to remain durable.

## System Shape

| Component or area | Responsibility | Owns | Must not own |
|---|---|---|---|
| `<name or path>` | `<primary responsibility>` | `<data, behavior, or decisions>` | `<responsibility kept elsewhere>` |

## Dependency Rules

- `<source area>` may depend on `<target area>` for `<purpose>`.
- `<source area>` must not depend on `<prohibited area>`.
- Shared interfaces belong in `<path or package>`.

## Placement And Ownership

| Concern | Canonical location | Boundary rule |
|---|---|---|
| `<concern>` | `<path>` | `<where related behavior must enter or remain>` |

## Cross-Cutting Boundaries

- Validation: `<where input is validated and where trusted data begins>`.
- Authorization: `<where access decisions are made and enforced>`.
- Data access: `<which layer owns persistence and transaction boundaries>`.
- Side effects: `<where network, filesystem, messaging, or external calls occur>`.
- Error handling: `<where errors are translated, logged, or exposed>`.

Remove concerns that do not apply and add project-specific boundaries only when
they are durable and architecturally meaningful.

## Public And Internal Interfaces

- Public or externally consumed interfaces: `<paths, packages, APIs, or none>`.
- Internal interfaces that callers should use: `<paths or packages>`.
- Implementation details callers must not depend on: `<paths or modules>`.

## Exceptions And Transitional States

Record approved exceptions with their reason, owning task or decision, and
removal condition. Remove the entry when the exception no longer exists.

- None.

## Update Triggers

Review and update this file when code changes:

- add, remove, split, merge, or relocate a responsibility;
- change an allowed dependency direction;
- move validation, authorization, data access, or side-effect ownership;
- introduce or remove a public or shared interface;
- create or retire an architectural exception.

Do not update it for internal implementation details that leave the documented
boundaries unchanged.

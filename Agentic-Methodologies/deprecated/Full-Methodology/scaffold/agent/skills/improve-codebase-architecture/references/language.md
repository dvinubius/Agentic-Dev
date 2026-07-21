# Architecture Language

Use these terms consistently when applying the
`improve-codebase-architecture` skill.

## Terms

**Module**: Anything with an interface and an implementation, including a
function, class, package, or vertical slice.

**Interface**: Everything callers must understand to use a module correctly,
including operations, types, invariants, ordering, errors, configuration, and
relevant performance characteristics.

**Implementation**: Code hidden behind the interface.

**Depth**: Leverage delivered through an interface. A deep module provides
substantial behavior behind a small interface. A shallow module exposes nearly
as much complexity as it hides.

**Seam**: A place where behavior can vary without editing the caller.

**Adapter**: A concrete implementation that satisfies an interface at a seam.

**Leverage**: Capability callers gain for the interface complexity they must
learn.

**Locality**: Concentration of related change, bugs, knowledge, and
verification in one place.

## Principles

- Depth is a property of the interface, not a reward for more implementation.
- A deep module may contain internal modules and seams that callers never see.
- Where automated tests are permitted by root `AGENTS.md`, the interface is the
  primary test surface. Otherwise it remains the primary behavior-verification
  surface for manual scenarios and other checks.
- Two real adapters justify a seam more strongly than one hypothetical adapter.
- Domain language should name modules and seams.

## Deletion Test

Imagine deleting a suspected shallow module:

- If complexity disappears, the module may have been unnecessary.
- If the complexity spreads into several callers, the module was hiding useful
  complexity and earning its place.

Use the test as evidence, not as an automatic deletion rule.

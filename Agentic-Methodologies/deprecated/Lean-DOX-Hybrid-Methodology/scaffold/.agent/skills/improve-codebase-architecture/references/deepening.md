# Deepening By Dependency Type

Classify dependencies before proposing how shallow modules should be
consolidated.

## In-Process

Pure computation or in-memory state. Consolidate and test directly through the
new interface. No adapter is normally required.

## Local-Substitutable

Infrastructure with a realistic local test substitute, such as a test database
or in-memory filesystem. Keep the seam internal and test the deepened module
with the substitute.

## Remote But Owned

Another service controlled by the same organization. Define a port at the
network seam. Use a production transport adapter and an in-memory or local test
adapter.

## External

A third-party service outside project control. Inject a narrow port and use a
test adapter that represents the external contract.

## Seam Discipline

- Do not expose internal seams in the external interface.
- Do not add a port for a dependency that cannot or will not vary.
- Prefer one strong interface-level test surface over layers of shallow-module
  tests.
- When interface-level tests replace implementation-coupled tests, remove
  obsolete tests rather than maintaining both indefinitely.

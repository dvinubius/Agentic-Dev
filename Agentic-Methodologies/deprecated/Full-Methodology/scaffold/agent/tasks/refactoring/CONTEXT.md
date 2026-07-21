# Refactoring Tasks

Use refactoring tasks for justified internal structural change.

## Creation Rules

- Describe the current architectural or maintainability problem in detail.
- State the technical requirement or pressure motivating the change.
- Define the intended before/after structure and dependency direction.
- Separate behavior preservation from structural acceptance criteria.
- Do not mix feature work into a refactor silently.
- Copy `_template/` to `NNN-short-description/`.
- Add the task to `ACTIVITY.md`.

## Observable Refactoring Evidence

Use the evidence appropriate to the task:

- existing behavior or characterization tests;
- engineer-run scenarios in `MANUAL-TESTING.md` when frontend automated tests
  are excluded or manual behavior-preservation evidence is otherwise useful;
- public API or contract snapshots;
- typecheck, lint, test, and build results;
- dependency/import graph checks;
- searches proving obsolete names, paths, or imports are gone;
- benchmark comparisons when performance is in scope;
- focused review of stated architecture boundaries.

Avoid vague criteria such as "improve modularity." Prefer observable criteria
such as "the domain package has no imports from the UI package."

## Completion

- Record the final architecture and any decision document changes.
- Show behavior-preservation evidence.
- Show structural acceptance evidence.
- Update `ACTIVITY.md`, then move the task under `done/` after approved commit
  handling.

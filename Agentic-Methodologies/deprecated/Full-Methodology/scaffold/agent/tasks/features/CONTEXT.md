# Feature Tasks

Use feature tasks to implement intended product behavior.

## Broad Planning

Use `../../skills/plan-feature-work/SKILL.md` when the engineer wants to map a
large spec area into ordered candidate slices before creating formal tasks. Its
plan belongs in `ACTIVITY.md`. Candidate slices are planning guidance, not task
records.

The broad plan may include intended stack and technical capabilities when they
materially affect feasibility, slice boundaries, dependencies, sequencing,
risk, or verification. Label established choices, approved choices,
provisional assumptions, and unresolved decisions distinctly.

## Creation Rules

- Link the relevant files and headings under `specs/`.
- Restate only the task-relevant meaning as local `REQ-NNN` entries.
- Define user- or system-observable `AC-NNN` acceptance criteria.
- Keep the task to one coherent, reviewable feature slice.
- Identify behavior intentionally left for later tasks.
- Copy `_template/` to `NNN-short-description/`.
- Add the task to `ACTIVITY.md`.

## Planning Questions

- What user or system outcome changes?
- Which current specs authorize the change?
- What data, API, UI, security, and operational boundaries are affected?
- Can each acceptance criterion be verified by a permitted automated test,
  manual scenario, or explicit check?
- Does this task require a spec change before execution?

If current specs do not authorize the intended behavior, stop task creation and
use `../../skills/update-specs/SKILL.md`. Resume task creation only after the
required spec change has been accepted.

## Completion

- The implementation must match the linked current specs.
- Traceability must connect local requirements to acceptance criteria,
  verification evidence, implementation files, and docs.
- Update `ACTIVITY.md`, then move the task under `done/` after approved commit
  handling.

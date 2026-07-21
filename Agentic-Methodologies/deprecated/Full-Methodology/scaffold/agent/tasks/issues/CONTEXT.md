# Issue-Fix Tasks

Use issue tasks to correct behavior that is currently wrong.

## Creation Rules

- Describe observed behavior, expected behavior, and evidence.
- Include reproduction steps when possible.
- Link relevant specs and implemented-behavior docs.
- Define acceptance criteria that prove the issue is fixed and important
  behavior is preserved.
- Copy `_template/` to `NNN-short-description/`.
- Add the task to `ACTIVITY.md`.

## Planning Questions

- Can the failure be reproduced or otherwise evidenced?
- What is the narrowest credible cause?
- Is the expected behavior already authorized by current specs?
- What permitted automated or manual regression evidence is credible under the
  frontend automated-test policy?
- Could the fix affect compatibility, data, security, or adjacent behavior?

If expected behavior is not established by current specs, stop task creation and
use `../../skills/update-specs/SKILL.md`. Resume task creation only after the
required spec change has been accepted.

## Completion

- Traceability must include regression evidence consistent with the frontend
  automated-test policy, or a reason no stronger evidence is useful.
- Record the root cause, fix, verification, and residual risk.
- Update `ACTIVITY.md`, then move the task under `done/` after approved commit
  handling.

---
name: update-specs
description: Change the repository's canonical product or business specifications while preserving consistency, checking affected open tasks, and recording an accepted versioned snapshot. Use when the engineer asks to add, revise, remove, or reorganize intended behavior under specs/.
---

# Skill: Update Specs

## Methodology Context

`specs/` is the canonical home of intended product and business behavior.
Specs may describe behavior that has not been implemented yet.

A **task** is a repository-tracked feature, issue-fix, or refactoring work item,
not merely a prompt sent to the agent. `../../tasks/CURRENT.md` is the
active-task lock. Do not begin unrelated spec work while it names an active
task.

Spec changes are planning work. They do not use the six task-execution gates,
but unresolved intent, conflicts, and acceptance still require engineer
decisions.

An engineer's instruction to make a spec change authorizes drafting the live
spec edits. It does not by itself constitute acceptance of the resulting spec
set, even when the requested intent appears fully decided. Treat the edited
live specs as proposed until the engineer explicitly accepts the resulting
wording or explicitly waives the spec-review gate.

## Engineer Handoffs

Whenever waiting for engineer confirmation, a decision, approval, acceptance,
or review, end the response with the explicit question the engineer must
answer. Put it in a separate final paragraph and place no text after it.

## Required Context

Before editing:

- read `../../../specs/CONTEXT.md`;
- read `../../../specs/README.md`;
- read `../../../specs/domain-language.md`;
- read `../../../specs/spec-history/README.md`;
- read `../../tasks/CURRENT.md`;
- read the affected specs and any coupled specs identified by the spec map;
- inspect relevant open-task briefs and activity files when requirements may
  change.

Do not read a historical snapshot by default. Normally, the live specs are the
latest accepted version. During an update, they may temporarily contain a
proposed revision that has not yet been accepted.

If a required methodology artifact is absent, report the missing dependency and
ask for direction rather than inventing a replacement.

## Procedure

1. Confirm that `CURRENT.md` permits the work.
2. State the intended spec change, affected product area, and known exclusions.
3. Inspect the current affected specs, canonical terminology, and materially
   coupled requirements. Read the latest relevant accepted snapshot only when
   needed to distinguish accepted intent from pending or uncertain live edits,
   recover an interrupted update, understand removed or materially changed
   intent, or inspect relevant historical rationale.
4. Identify ambiguities, contradictions, and decisions required from the
   engineer before treating the change as accepted.
5. Update the live spec files, spec map, and domain language consistently.
6. Review open tasks for requirements that were removed, changed, or newly
   contradicted.
7. Present spec/task conflicts to the engineer. Do not silently delete, rewrite,
   or re-scope affected tasks.
8. Present the completed live-spec changes and obtain explicit engineer
   acceptance of the resulting current spec set. Approval of the requested
   intent before editing is not acceptance of the resulting wording. Record the
   engineer's decisions or explicitly unresolved dispositions for affected
   tasks.
9. After acceptance, create the next complete versioned snapshot under
   `../../../specs/spec-history/` using that directory's documented format.
   Copy all live spec files needed to reconstruct the accepted version, excluding
   `spec-history/` itself.
10. Report changed spec files, terminology or map changes, task conflicts,
    acceptance status, and the snapshot path.

## Guardrails

- Do not implement the changed behavior as part of this skill.
- Do not treat an unimplemented accepted spec as an implementation defect.
- Do not read historical snapshots merely to duplicate the live spec context.
- Do not create the accepted snapshot before the engineer accepts the change.
- Do not continue into subsequent planning or implementation work until the
  engineer answers the spec-acceptance handoff, unless the engineer explicitly
  waives that handoff.
- Do not leave the live spec set internally inconsistent in order to defer a
  known decision.
- Do not edit engineer-maintained activity content without permission.

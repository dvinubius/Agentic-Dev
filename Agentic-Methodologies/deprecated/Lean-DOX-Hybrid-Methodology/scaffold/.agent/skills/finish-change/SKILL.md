---
name: finish-change
description: Finish a non-trivial implementation change by running focused correctness, completeness, and technical-alignment checks, proportionate verification, diff review, planning-note cleanup, and a concise final report. Use before declaring feature, fix, or refactoring work complete.
---

# Skill: Finish Change

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may update and delete `.agent-state/task-handoff.md` as
temporary runtime state outside `.agent/`.

This is the lightweight completion workflow. It coordinates focused assurance
without creating a formal task lifecycle or retained task artifacts.

## Scope

The default scope is the current change and its directly affected behavior,
contracts, modules, and docs.

Do not turn completion into a subsystem-wide or repository-wide audit. If
evidence suggests a broad pass is needed, explain the evidence, proposed scope,
cost, and expected value, then follow the selected work mode.

## Required Context

Read:

- root `AGENTS.md`;
- `.agent/local-guides/CONTEXT.md` and applicable nested `AGENTS.md` files;
- `.agent-state/task-handoff.md` when present;
- the actual current diff or changed-file set;
- relevant specs, code, permitted tests, contracts, and docs;
- `docs/normative/README.md` and relevant normative docs when code changed;
- `docs/planning.md`.

## Entry Condition

If application code changed in `SUPERVISED` mode, the developer must already
have reviewed and approved the implemented code, unless that review was
explicitly waived or batched. This skill does not replace the supervised
post-implementation review gate.

## Procedure

1. Confirm the intended outcome, current scope, and any explicitly partial
   delivery from current repository state, the actual diff, and the handoff
   rather than relying on earlier transcript.
2. Run `../ensure-correctness/SKILL.md` in current-change mode.
3. Run `../ensure-completeness/SKILL.md` in current-change mode, using the
   intended outcome and accepted exclusions as its completion baseline.
4. Run `../ensure-docs-matched/SKILL.md` in current-change mode. Review the
   whole of `docs/planning.md` as required by that skill, even when stale notes
   predate the current change. When external-system interaction changed, verify
   that its previously accepted integration contract and index row match the
   implementation. Check applicable local guides and update them only when
   their routing or work contract changed.
5. Repair small in-scope gaps and repeat the relevant focused check.
6. In `SUPERVISED` mode, if any repair changes application code after the last
   approved review, summarize the repaired diff and request another developer
   review before continuing. Repeat this gate whenever later work changes the
   approved application code again, unless the developer explicitly waives or
   batches the review.
7. Follow the selected work mode if a repair would materially broaden scope or
   require a high-impact decision.
8. Run proportionate permitted verification, narrowest useful checks first.
   After two failed attempts with the same verification path or tool, follow
   the selected work mode before investing more effort.
   Use bounded read-only subagents for noisy test runs, failure analysis, or
   large-diff review when available. Reports must stay under roughly 100-150
   lines unless explicitly expanded, and raw logs remain outside the main
   context.
9. Build an explicit test account:
   - test files created or changed;
   - the behavior each test verifies;
   - test commands attempted;
   - whether each command passed, failed, or was not run;
   - the relevant result or reason;
   - an explicit `none` when no tests were created or changed.
10. Review all non-normative project docs affected by the final implementation,
    including but not limited to repository maps, development commands,
    conventions, planning, contributor guidance, README navigation, and local
    agent guides. Update them from final repository evidence. Do not edit
    `docs/normative/` in this step.
11. Inspect the actual diff for unrelated changes, accidental churn, secrets,
    generated-file edits, and remaining substantive risk.
12. When manual verification would provide useful evidence, suggest a short
    set of scenarios in conversation. Do not create a repository worksheet.
13. Update `.agent-state/task-handoff.md` with final verification and
    documentation status, reconstruct the final report from the repository,
    diff, handoff, and concise reports, then delete the handoff and remove
    `.agent-state/` when empty before declaring completion.

## Output

Report:

- outcome and scope completed;
- focused assurance findings and repairs;
- tests created or changed, their purpose, whether they ran, and their results;
- commands or checks run and their results;
- checks not run and why;
- suggested manual verification scenarios when applicable;
- intentional omissions and deferred concerns;
- local agent-guide changes or a concise no-change disposition when relevant;
- residual risk.

Do not say the work is complete while a required check is failing or an
essential scope item lacks an explicit disposition.
Do not leave `.agent-state/task-handoff.md` or an empty `.agent-state/`
directory after completion or abandonment.

---
name: drift-audit
description: Diagnose drift among implemented behavior, tests and contracts, code, and application documentation in a bounded area. Use for targeted consistency audits, suspected stale docs or contracts, missing behavioral proof, or implemented behavior that may be undocumented.
---

# Skill: Drift Audit

Diagnosis is the default. Do not edit files during the first pass.
Avoid whole-repository audits unless the engineer explicitly requests one.

## Omni-Sync Scope

In this methodology, **Omni-Sync** means consistency among artifacts that
describe and prove behavior already implemented:

- required verification evidence supports the behavior;
- tests and contracts that exist agree with the behavior;
- code implements the behavior;
- application documentation describes the behavior.

Specs describe intended behavior and may intentionally be ahead of
implementation. An unimplemented spec is not an Omni-Sync defect unless
planning coverage is also part of the requested audit. **Planning coverage**
asks whether unimplemented intended behavior is represented by an appropriate
open task.

## Work-State Check

A **task** is a repository-tracked feature, issue-fix, or refactoring work
item, not merely an agent prompt. Read `../../tasks/CURRENT.md`. If it names an
active task, run this skill only in service of that task. Otherwise, do not
start the audit until the engineer resolves the conflict.

## Engineer Handoffs

Whenever waiting for engineer confirmation, a decision, approval, or review,
end the response with the explicit question the engineer must answer. Put it in
a separate final paragraph and place no text after it.

## Inputs

- target module or area;
- relevant specs, docs, code, existing tests, contracts, and manual-testing
  evidence;
- optional exclusions.

## Procedure

1. Apply the work-state check above.
2. State scope and evidence sources.
3. Read root `AGENTS.md` for the frontend automated-test policy, then read only
   relevant specs, docs, implementation, existing tests, contracts, and task
   manual-testing evidence. Do not run excluded frontend tests.
4. Report:
   - implemented requirements without evidence required by the project policy;
   - tests with unclear requirement or behavior purpose;
   - missing, stale, or insufficient manual scenarios where frontend automated
     tests are excluded;
   - docs that contradict code or contracts;
   - implemented behavior missing from docs;
   - stale examples, contracts, or configuration guidance.
5. Ignore intentionally unimplemented specs unless planning coverage is also in
   scope.
6. Propose minimal repairs grouped by artifact type.
7. Wait for approval before editing.

## Repair Rules

- Preserve runtime behavior.
- If a repair requires runtime behavior change, use
  `../create-task/SKILL.md` to create an issue or feature task instead.
- Re-run the targeted audit after approved repairs.

## Output

Order findings by impact. Include file evidence, the contradiction or gap,
confidence, and the smallest credible repair.

---
name: code-review
description: Review an actual diff or bounded changed-file set against the developer request, PRD or issue context when present, communicated approach, project rules, verification evidence, and technical docs. Focus on substantive defects and risks.
---

# Skill: Code Review

## Scope

Review the actual diff. The default scope is the current change. A broad
historical or subsystem review requires confirmation.

## Required Context

- developer request and communicated implementation approach;
- PRD and issue context when the review is part of active task work;
- actual diff and relevant surrounding code;
- normative technical docs, conventions, and applicable authoritative external
  references;
- permitted tests, contracts, verification results, and affected docs;
- explicit exclusions and accepted limitations.

## Procedure

1. Confirm the reviewed scope and baseline.
2. Inspect the actual diff and enough surrounding code to evaluate it.
3. Check:
   - correctness and selected-scope completeness;
   - edge cases and failure modes;
   - scope creep and unrelated churn;
   - security, privacy, authorization, and data integrity;
   - architecture boundary violations;
   - API, migration, compatibility, concurrency, and operational risks;
   - meaningful verification gaps;
   - whether tests created or changed are identified, whether they ran, and
     whether their reported results are accurate;
   - stale or missing architecture or integration docs;
   - maintainability problems with practical impact.
4. Exclude style-only comments unless they materially affect correctness,
   clarity, or maintenance.
5. Order findings by severity and cite exact files and lines.
6. State residual risk and unrun checks even when no defect is found.

## Finding Format

- severity;
- concise title;
- file and line;
- triggering scenario or consequence;
- smallest credible correction.

Review is diagnosis-only unless the developer requested fixes or the review is
part of active implementation. High-impact corrections require confirmation.

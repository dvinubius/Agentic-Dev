---
name: neatify-code
description: Refactor or review bounded code for clarity, maintainability, locality, duplication, complexity, dead code, and project-standard fit while preserving behavior. Use when the developer asks to neatify, simplify, clean up, refactor for maintainability, run a maintainability pass on changed code, or include maintainability-oriented refactoring evidence in code review.
---

# Skill: Neatify Code

## Scope

Improve or assess a bounded area of code while preserving current behavior.
Default to the changed code or the developer-selected area. A repository-wide
cleanup requires confirmation.

Use this skill as:

- an editing procedure when the developer requested cleanup or refactoring;
- a diagnostic procedure when invoked from review context or when edit
  authority is unclear.

Do not change public APIs, persistent data shape, authorization behavior,
external contracts, generated files, or architecture boundaries without
explicit approval.

## Required Context

Read:

- root `AGENTS.md`;
- `../../../docs/conventions.md`;
- `../../../docs/domain-language.md`;
- relevant `../../../docs/normative/` files;
- relevant source, tests, and contracts;
- [references/simplifier.md](references/simplifier.md).

For JavaScript or TypeScript projects where Fallow is available or approved,
also read [references/fallow.md](references/fallow.md).

Use Fallow and codegraph for different jobs:

- Fallow: broad static routing for JavaScript/TypeScript maintainability,
  hotspots, duplication, dead code, and cleanup targets.
- codegraph: narrow structural follow-up for the selected targets, especially
  callers, callees, impact, ownership, and dependency relationships.

Do not use codegraph as a substitute for broad maintainability triage when
Fallow is available. Do not use Fallow as a substitute for understanding the
behavior and accepted design intent of the files being changed. When codegraph
is unavailable, use repository-native search, language tooling, dependency
graphs, tests, and direct source reading to inspect the same relationships.

## Procedure

### 1. Establish Scope And Authority

Identify:

- reviewed or edited baseline;
- files, symbols, or feature slice in scope;
- whether edits are allowed or findings should be reported first;
- behavior and interfaces that must remain unchanged;
- project verification commands that are proportionate.

If the scope is broad or findings are likely to exceed one coherent change,
triage first and ask the developer to select the slice to handle now.

### 2. Collect Static Evidence First

Use cheap deterministic evidence before deep manual refactoring or broad source
reading:

- project typecheck, lint, formatter check, test discovery, dead-code,
  dependency, or complexity tools when configured and cheap;
- Fallow for JavaScript or TypeScript when already available, or when the
  developer approves adding it under the repository package-installation
  policy; use [references/fallow.md](references/fallow.md) for authoritative
  source and command selection.

For JavaScript or TypeScript audits, use Fallow early when it is already
available or the developer has approved installing a policy-compliant version:

- run a broad routing pass such as `fallow health --score --hotspots --targets`;
- run cleanup-specific passes such as `fallow dead-code --format json` and
  `fallow dupes --format json` when useful;
- run changeset audit only when the task is actually about changed files or a
  pull request; if `fallow audit` fails because base-snapshot attribution cannot
  create a temporary worktree, report that and use the broader health/dead-code/
  duplication outputs instead of forcing the audit path.

Prefer machine-readable tool output when available. Treat static findings as
evidence, not commands.

Do not install packages or run `npx` commands that may fetch packages until the
developer approves the dependency addition and the package and version satisfy
the repository package-installation policy, if one exists.

### 3. Route From Broad Evidence To Narrow Context

Use Fallow's output as a routing map, not a complete answer.

For each top target or suspected cleanup slice:

- use codegraph when available to inspect the relevant symbols, callers,
  callees, impact, and nearby structure; otherwise use repository-native search,
  language tooling, dependency graphs, tests, and direct source reading for the
  same follow-up;
- read only the routed source, relevant tests/contracts, and relevant accepted
  design docs needed to judge behavior preservation;
- avoid a full manual sweep after static routing unless the task explicitly
  requires repository-wide coverage or the evidence suggests a cross-cutting
  concern.

Examples:

- If Fallow flags a renderer function, inspect callers/state dependencies with
  codegraph or the fallback tools, then read that frontend file, its DOM
  anchors, and API shape contracts.
- If Fallow flags parser duplication, inspect parser callers/exports with
  codegraph or the fallback tools, then read both parsers, parser tests, and
  normative parser decisions.
- If Fallow flags an unused file or export, verify whether it is a static entry,
  generated/test artifact, external API, or runtime-loaded path before reporting
  it as real dead code.

### 4. Triage Findings

Classify issues as:

- fix now: changed-code maintainability risk, unsafe duplication, dead code,
  excessive complexity, or project-standard mismatch in scope;
- candidate: useful refactor with clear behavior-preservation evidence;
- defer: broad historical cleanup, noisy generated/config/test duplication, or
  work outside the selected slice;
- needs decision: accepted duplication, intentional complexity, API migration,
  architecture boundary change, or unclear behavior.

Document accepted exceptions at the right durability:

- local report for one-off or task-local decisions;
- `docs/conventions.md` for recurring project conventions;
- ADR under `docs/normative/decisions/` only for durable architectural
  exceptions or choices whose rationale will matter later.

### 5. Refactor Or Report

When edits are allowed, make the smallest coherent behavior-preserving
improvement. Prefer:

- clearer names and domain language;
- reduced nesting and branch complexity;
- explicit data flow over hidden global state;
- removal of obsolete abstractions, dead code, and redundant comments;
- consolidation of duplicated real behavior into a clearer capability;
- smaller functions when that improves readability without cluttering context
  passing;
- tests at useful behavior or interface boundaries instead of brittle internal
  details.

When in review context, report maintainability findings before editing unless
the developer explicitly requested fixes.

### 6. Route Work That Is No Longer Cleanup

Stop and route or ask when evidence shows the work is not straightforward
behavior-preserving refactoring:

- uncertain expected behavior, regression, or root cause:
  `../investigate-issue/SKILL.md`;
- consequential blast radius across callers, data, contracts, security,
  privacy, authorization, operations, cost, or external systems:
  `../assess-change-impact/SKILL.md`;
- architecture diagnosis or a bounded deep-module candidate that needs design
  before code changes: `../deepen-modules/SKILL.md`;
- substantive actual-diff review beyond maintainability:
  `../code-review/SKILL.md`.

### 7. Verify And Report

Run the narrowest useful checks first. Never claim behavior preservation unless
verification actually ran or the remaining evidence gap is explicit.

Report:

- scope handled;
- static tools used, including Fallow/codegraph commands when applicable, and
  important findings handled, deferred, rejected as false positives, or
  accepted;
- files changed or findings reported;
- verification commands and results;
- remaining risks, deferred cleanup, and any documentation or ADR follow-up.

## Guardrails

- Do not optimize for fewer lines at the expense of clarity.
- Do not extract abstractions for hypothetical reuse.
- Do not merge frontend components merely to create a larger test target.
- Do not hide domain policy inside generic services.
- Do not silently broaden cleanup beyond the selected task or changed code.
- Do not treat Fallow, linters, or codegraph output as a substitute for
  understanding project behavior.

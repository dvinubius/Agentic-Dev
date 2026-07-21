---
name: assess-change-impact
description: Assess the bounded impact of a proposed consequential change across callers, data, contracts, architecture, security, operations, verification, and docs before implementation. Use when scope or blast radius is uncertain.
---

# Skill: Assess Change Impact

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may maintain `.agent-state/task-handoff.md` as temporary
runtime state outside `.agent/`, as defined in root `AGENTS.md`.

Assess only the proposed change and credible dependency surface. This skill
does not authorize implementation.

## Scope

State the exact proposed change and stop expanding when additional areas no
longer have a credible dependency path.

If the assessment itself would become unusually broad, explain the reason,
scope, cost, and value and follow the selected work mode.

## Required Context

- current specs and stated intent;
- relevant code, callers, contracts, permitted tests, and configuration;
- `docs/normative/README.md` and relevant normative docs;
- applicable decisions, operational docs, and `docs/planning.md`.

## Procedure

1. Define the proposed change and alternatives under consideration.
2. Trace direct and important indirect effects on:
   - callers and entry points;
   - public and internal contracts;
   - persistent data and migrations;
   - architecture ownership and dependencies;
   - validation, authorization, privacy, and security;
   - compatibility and rollout;
   - external contract surface, data projection, mapping, and provider-version
     assumptions;
   - operations, cost, and failure recovery;
   - verification and technical docs.
3. Separate required consequences from speculative possibilities.
4. Identify high-impact decisions and handle them through the selected work
   mode.
5. Recommend a smallest coherent scope and proportionate verification
   strategy.

## Output

Report affected areas, evidence, risk level, required decisions, recommended
scope, likely verification, and areas deliberately excluded from the analysis.

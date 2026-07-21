---
name: assess-change-impact
description: Assess the bounded impact of a proposed consequential change across callers, data, contracts, architecture, security, operations, verification, and docs before implementation. Use when scope or blast radius is uncertain.
---

# Skill: Assess Change Impact

## Scope

Assess only the proposed change and credible dependency surface. This skill
does not authorize implementation.

State the exact proposed change and stop expanding when additional areas no
longer have a credible dependency path.

If the assessment itself would become unusually broad, explain the reason,
scope, cost, and value and ask before proceeding.

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
4. Identify high-impact decisions and ask before proceeding with them.
5. Recommend a smallest coherent scope and proportionate verification
   strategy.

## Output

Report affected areas, evidence, risk level, required decisions, recommended
scope, likely verification, and areas deliberately excluded from the analysis.

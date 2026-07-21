---
name: supervised
description: Apply SUPERVISED work mode, where the agent keeps the developer involved for significant plans, high-impact decisions, phase confirmations, and implementation review.
---

# Skill: Supervised Mode

## Mode Contract

Use this skill when the developer explicitly requests `SUPERVISED` mode.

In SUPERVISED mode, keep the developer involved at review points that prevent
wrong direction, avoid expensive or risky work without confirmation, and make
complex multi-phase work reviewable.

Before asking, summarize the evidence, options, recommendation, and practical
consequence. Ask one concrete question.

## Approval And Review Gates

Stop and ask before:

- changing or resolving ambiguous product intent;
- implementing a significant application-code plan that has not been approved;
- materially broadening scope;
- defining or changing normative architecture boundaries;
- creating, reorganizing, or removing a broad local-agent-guide tree;
- adding dependencies, frameworks, services, infrastructure, or migrations;
- changing public APIs or externally consumed contracts;
- changing database schema or creating or applying migrations;
- making consequential security, privacy, authorization, data-lifecycle,
  compatibility, cost, or operational choices;
- running destructive operations, deployments, production actions, unusually
  broad verification, or expensive tool calls;
- creating commits.

For complex, multi-phase work:

- present significant implementation plans before editing application code;
- ask whether a large plan should be split into ordered, independently
  reviewable items;
- if split execution is accepted, write the active plan to `docs/planning.md`
  before its first item;
- after planned application-code changes, ask the developer to review and
  approve the implementation before final verification, non-normative
  documentation, and conclusion, unless the developer explicitly waives or
  batches that review;
- if a finishing repair later changes application code, ask the developer to
  review the repaired diff before continuing; repeat whenever subsequent work
  changes the approved application code again unless that review is explicitly
  waived or batched;
- after two failed attempts with the same verification path, summarize the
  failures and ask how to proceed before investing more effort.

## Architecture, Specs, And Guides

New or changed architecture boundaries require developer approval before
implementation. Product intent changes and unresolved high-impact product
decisions require developer input before dependent implementation proceeds.

Nested `AGENTS.md` files may be maintained only under the local-guide rules.
Broad guide initialization, broad refresh, structural reorganization, or guide
removal requires developer approval before writes.

## Output

Report approvals requested, decisions received, any waived or batched review
gates, verification performed, local-guide changes when relevant, and remaining
decisions or risks.

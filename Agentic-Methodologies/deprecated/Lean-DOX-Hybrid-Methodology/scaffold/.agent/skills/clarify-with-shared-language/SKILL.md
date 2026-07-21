---
name: clarify-with-shared-language
description: Clarify and stress-test a plan through a one-question-at-a-time conversation grounded in current specs, domain language, decisions, code, and permitted tests. Use to resolve design branches, sharpen terminology, or expose hidden assumptions.
---

# Skill: Clarify With Shared Language

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may maintain `.agent-state/task-handoff.md` as temporary
runtime state outside `.agent/`, as defined in root `AGENTS.md`.

Interview the developer until the selected plan and terminology are clear
enough to act on. Resolve prerequisite decisions before dependent ones and ask
one question per turn.

For every question:

- give a recommended answer and reasoning;
- inspect the repository instead of asking for discoverable facts;
- distinguish facts, assumptions, decisions, and open questions;
- wait for the developer's response before continuing.

This skill does not implement runtime changes.

## Required Context

Read:

- relevant specs and `../../../specs/domain-language.md`;
- relevant normative architecture and decisions;
- `../../../docs/planning.md`;
- only the code, permitted tests, contracts, and docs needed to verify claims.

Read [references/domain-language-format.md](references/domain-language-format.md)
before updating the glossary. Read
[references/decision-record-format.md](references/decision-record-format.md)
before proposing a decision record.

## Clarification Discipline

- Challenge terminology that conflicts with the domain glossary.
- Propose one precise canonical term when wording is vague or overloaded.
- Use concrete scenarios to expose edge cases and unclear boundaries.
- Cross-check claims about current behavior against implementation evidence.
- Surface contradictions directly and ask which source should change.
- Explore roles, permissions, lifecycle, failure, recovery, data ownership,
  compatibility, and operations when relevant.
- During spec clarification, separate product-owner assertions from technical
  design. A spec statement must remain true if the implementation is replaced.
- Challenge outcomes that cannot be credibly verified.
- Prioritize consequential questions over exhaustive questioning.

## Durable Updates

As decisions crystallize:

- route product-intent changes through `../update-specs/SKILL.md`;
- update `../../../specs/domain-language.md` after terminology is confirmed;
- record accepted technical choices in `../../../docs/normative/decisions/`
  when their rationale and consequences will matter later;
- put tentative architecture candidates, technologies, internal models,
  algorithms, migrations, rollout ideas, sequencing, and other implementation
  impulses in `../../../docs/planning.md` under
  `## Technical Design Impulses`;
- use decision records only for durable, costly, surprising, or otherwise
  consequential choices, not every implementation thought;
- promote settled planning impulses to decision records and remove duplicated
  temporary detail;
- keep only short still-useful direction or open decisions in
  `../../../docs/planning.md`;
- do not begin implementation unless separately requested.

## Completion

Summarize decisions, terminology changes, unresolved questions,
contradictions, artifacts updated, and the recommended next action.

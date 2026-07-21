---
name: clarify-with-shared-language
description: Clarify and stress-test a plan through a one-question-at-a-time conversation grounded in domain language, decisions, code, and permitted tests. Use to resolve design branches, sharpen terminology, or expose hidden assumptions.
---

# Skill: Clarify With Shared Language

## Scope

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

- `../../../docs/domain-language.md`;
- relevant normative architecture and decisions;
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
- Challenge outcomes that cannot be credibly verified.
- Prioritize consequential questions over exhaustive questioning.

## Durable Updates

As decisions crystallize:

- update `../../../docs/domain-language.md` after terminology is confirmed;
- record accepted technical choices in `../../../docs/normative/decisions/`
  when their rationale and consequences will matter later;
- use decision records only for durable, costly, surprising, or otherwise
  consequential choices, not every implementation thought;
- do not begin implementation unless separately requested.

## Completion

Summarize decisions, terminology changes, unresolved questions,
contradictions, artifacts updated, and the recommended next action.

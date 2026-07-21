---
name: clarify-with-shared-language
description: Clarify and stress-test a plan through a one-question-at-a-time conversation grounded in current specs, shared domain language, decisions, code, and tests. Use when the engineer wants to resolve design branches, sharpen terminology, expose hidden assumptions, or reconcile a plan with documented and implemented behavior.
---

# Skill: Clarify With Shared Language

Interview the engineer rigorously until the plan and its terminology are
understood well enough to act on. Walk one branch of the design tree at a time,
resolve prerequisite decisions before dependent ones, and ask one question per
turn.

For every question:

- give a recommended answer and the reasoning behind it;
- wait for the engineer's response before continuing;
- inspect the repository instead of asking if code, tests, specs, or docs can
  answer the question;
- distinguish confirmed facts, assumptions, decisions, and open questions.

This skill sharpens planning. It does not implement runtime changes.

## Engineer Handoffs

Whenever waiting for engineer confirmation, a decision, approval, review, or an
answer to the next clarification question, end the response with the explicit
question the engineer must answer. Put it in a separate final paragraph and
place no text after it.

## Methodology Context

A **task** is a repository-tracked feature, issue-fix, or refactoring work
item. Its planning artifacts are `BRIEF.md` and `PLAN.md`; execution state is
recorded in `PROGRESS.md`.

Work contexts mean:

- **planning work**: refining specs, creating tasks, or improving a task plan;
- **task execution**: advancing the one task named in
  `../../tasks/CURRENT.md`;
- **complementary work**: an approved audit or refinement outside task
  execution.

If `CURRENT.md` names a task, use this skill only in service of that task.

## Domain Awareness

Before clarifying:

1. Apply the active-task rule above.
2. Identify the governing work context: planning, active task execution, or
   complementary work.
3. Read the relevant specs, task artifacts, `specs/domain-language.md`,
   decision records under `docs/decisions/`, and only the code/tests needed to
   verify claims.
4. If `specs/domain-language.md` does not exist, create it only after the first
   project-specific term is confirmed and only under the Durable Updates rules
   below.

Read [references/domain-language-format.md](references/domain-language-format.md)
before creating or updating the glossary. Read
[references/decision-record-format.md](references/decision-record-format.md)
before proposing a decision record.

## Clarification Discipline

- Challenge terminology that conflicts with the domain glossary.
- When a term is vague or overloaded, propose one precise canonical term.
- Use concrete scenarios to expose edge cases and unclear concept boundaries.
- Cross-check statements about current behavior against code and tests.
- Surface contradictions directly and ask which source should change.
- Explore roles, permissions, lifecycle, failure, recovery, data ownership,
  compatibility, and operational constraints when relevant.
- Challenge acceptance criteria that cannot prove the intended outcome.

## Durable Updates

Capture confirmed decisions as they crystallize, subject to the governing
workflow:

- planning work: route spec changes through `../update-specs/SKILL.md`, route new
  tasks through `../create-task/SKILL.md`, and update an existing task brief or
  plan under its governing task context;
- task execution: update task artifacts immediately, but defer application-doc
  edits to the documentation step unless the engineer approves otherwise;
- complementary work: route domain-language changes through
  `../update-specs/SKILL.md`, and update decision records after the engineer
  confirms the content.

Offer a decision record only when all are true:

1. the decision is costly to reverse;
2. a future reader would find it surprising without context;
3. it resolves a genuine tradeoff among credible alternatives.

## Completion

End with:

- decisions made;
- terminology added or changed;
- unresolved questions;
- contradictions requiring follow-up;
- artifacts updated;
- proposed next planning action.

## Guardrails

- Do not manufacture uncertainty where the documents are clear.
- Prioritize consequential questions over exhaustive questioning.
- Do not start implementation.
- Do not turn routing `CONTEXT.md` files into domain glossaries.
- Do not create a decision record for reversible, obvious, or non-decisions.

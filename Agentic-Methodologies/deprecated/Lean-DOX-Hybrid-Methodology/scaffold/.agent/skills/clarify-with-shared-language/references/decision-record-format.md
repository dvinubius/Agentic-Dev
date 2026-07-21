# Decision Record Format

Decision records live under `docs/normative/decisions/` and use the project's
numbering convention, normally `NNNN-short-title.md`.

There is no mandatory body template. Choose a shape that makes the record easy
to understand later. Make the following clear as applicable:

- status and date;
- scope and related specs or planning;
- context that made a decision necessary;
- the accepted decision;
- meaningful alternatives and why they were not selected;
- consequences, constraints, risks, and follow-up implications.

The record must distinguish accepted direction from proposals or unresolved
questions. Keep temporary exploration in `docs/planning.md` rather than
disguising it as a decision.

Only accepted or superseded decisions belong in `docs/normative/`. Proposed
decisions remain in planning until the developer accepts them.

## When A Record Is Justified

A record is useful when the choice is accepted and one or more are true:

- changing it later would be costly;
- the result is surprising without its context;
- credible alternatives existed and a real tradeoff was resolved;
- it defines architecture, ownership, dependencies, or a durable technical
  constraint;
- its rationale or consequences are likely to matter in future work.

Typical examples include:

- architecture shape;
- communication patterns between major areas;
- high-lock-in technology choices;
- ownership and dependency rules;
- deliberate deviations from the obvious design;
- constraints not visible in code;
- non-obvious rejected alternatives.

Do not create records merely to preserve every technical thought. Obvious
choices, reversible details, temporary priorities, and unsettled alternatives
normally belong in code, conversation, or `docs/planning.md`.

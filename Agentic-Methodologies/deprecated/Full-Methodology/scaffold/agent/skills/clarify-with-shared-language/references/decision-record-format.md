# Decision Record Format

Decision records live under `docs/decisions/` and use the project's numbering
convention, normally `NNNN-short-title.md`.

Start concise:

```markdown
# <Decision Title>

Status: accepted
Date: YYYY-MM-DD

<State the context, decision, and reason in one to three short paragraphs.>
```

Add alternatives or consequences only when they will help a future reader.

## When A Record Is Justified

All three conditions should hold:

1. changing the decision later would be costly;
2. the chosen result is surprising without its context;
3. credible alternatives existed and a real tradeoff was resolved.

Typical examples include:

- architecture shape;
- communication patterns between major areas;
- high-lock-in technology choices;
- ownership and dependency rules;
- deliberate deviations from the obvious design;
- constraints not visible in code;
- non-obvious rejected alternatives.

Do not create records for obvious choices, reversible details, or temporary
priorities.

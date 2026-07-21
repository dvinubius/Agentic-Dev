# Architecture Review Report

Prefer a self-contained HTML report in the OS temp directory when rendering is
available. Otherwise produce an equivalent Markdown report.

Do not save generated reports in the repository unless the developer requests
it.

## Candidate Format

For every deepening candidate show:

- title;
- recommendation strength;
- files and modules;
- dependency category;
- one-sentence problem;
- one-sentence proposed consolidation;
- concise leverage, locality, and verification gains;
- before and after diagram;
- accepted-decision conflict, if any.

Use diagrams to show the architectural point. Useful patterns include:

- call or dependency graph;
- several shallow modules collapsing into one deep module;
- interface-size versus implementation-depth comparison;
- cross-section through pass-through modules;
- before/after sequence.

## Recommendation Strength

- **Strong**: clear friction and credible consolidation with manageable risk.
- **Worth exploring**: promising but important design questions remain.
- **Speculative**: weak evidence or high uncertainty.

End with one top recommendation and the reason it should be explored first.
Do not bury the developer in every theoretical refactor.

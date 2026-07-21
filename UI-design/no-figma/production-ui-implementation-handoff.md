# Production UI Implementation Handoff

This file defines the boundary between design-stage mockups and production application UI code.

## Definition

**Production UI implementation** means generating or changing real application UI code.

This includes:

- framework components
- routes and pages
- production styles and design-system primitives
- state wiring for UI behavior
- accessibility behavior
- tests
- browser verification
- integration with the existing repo structure

This does **not** include:

- design package generation
- design package self-review
- fresh-context design review
- SVG quick-look generation
- static HTML/CSS mockup generation
- prototype-only JavaScript
- browser mockup review
- mockup consistency checking

Those are design workflow activities.

## Source-of-truth order

Use this order unless the project states otherwise:

1. Functional specs or PRD for product behavior.
2. `/design/tokens.json` for color, spacing, sizing, radius, typography, shadows/elevation, breakpoints, and semantic visual decisions.
3. `/design/*` Markdown artifacts for screens, flows, states, components, visual direction, accessibility requirements, and interaction intent.
4. `/design/design-package-self-review.md` for same-agent consistency findings and resolved issues.
5. `/design/design-package-fresh-context-review.md`, if present, for independent review findings.
6. `/design/mockups/*` as visual and interaction references.
7. `/design/mockups/consistency-check.md` for known token and artifact traceability issues.
8. `/design/svg/*` as optional first-look layout references only.

Mockups are not product behavior authority. If mockups conflict with specs, follow the specs and update the design package or mockups.

## Token enforcement at production handoff

Before production UI implementation starts, verify that `tokens.json` is stable enough to seed or update the production design system.

Requirements:

- `tokens.json` must be the single source of truth for color, spacing, sizing, radius, typography, shadows/elevation, and breakpoints.
- Every sizing/layout token must state behavior: `fixed`, `min`, `max`, `grow`, `fluid`, or `clamp`.
- Mockups must consume tokens through CSS variables.
- Any layout-affecting literal in mockup code must be documented as an intentional exception.
- Production UI code should preserve token intent rather than copying arbitrary values from mockup CSS.

## Before production UI implementation starts

Verify that:

- [ ] the design package exists
- [ ] `tokens.json` includes behavior metadata for sizing and layout tokens
- [ ] the design package has passed mandatory same-agent self-review
- [ ] critical self-review findings have been resolved or explicitly deferred
- [ ] the developer was asked whether to run fresh-context review
- [ ] fresh-context review was either completed or explicitly skipped
- [ ] critical fresh-context findings, if any, have been resolved or deferred
- [ ] `mockups/index.html` previews the primary flow or screen set
- [ ] `mockups/states.html` covers representative states
- [ ] `mockups/consistency-check.md` exists and does not contain unresolved critical token contradictions
- [ ] known mockup limitations are documented in `mockups/README.md`
- [ ] token exceptions are documented in `mockups/README.md`
- [ ] open questions are either resolved or documented as implementation blockers/non-blockers

## When mockups are sufficient for production UI handoff

Mockups are sufficient when:

- screen hierarchy is clear
- primary actions are clear
- reusable components are identifiable
- important states are represented in `states.html`
- responsive behavior is described or visible
- layout widths and sizing behavior are token-traceable
- accessibility requirements are documented
- remaining ambiguity is documented
- visual fidelity is good enough for the intended production UI pass

## When to delay production UI implementation

Delay production UI implementation when:

- core screens are missing
- main user flows are unclear
- state coverage is weak
- visual hierarchy is visibly inconsistent
- components are named inconsistently across screens
- tokens are incomplete or contradictory
- sizing/layout token behavior is missing
- mockup values contradict `tokens.json`
- accessibility requirements are absent
- open questions affect product behavior or critical UI states

## Prompt: production UI readiness review

Run this before generating production application UI code if the design package or mockups feel incomplete.

```txt
Review this design package and browser mockup set for production UI implementation readiness.

Inputs:
- functional specs or PRD
- /design/*
- /design/tokens.json
- /design/design-package-self-review.md
- /design/design-package-fresh-context-review.md, if present
- /design/mockups/*
- /design/mockups/consistency-check.md
- /design/svg/*, if present

Do not implement production code.

Assess:
- product behavior consistency
- screen and flow completeness
- state coverage
- component readiness
- design token readiness
- sizing/layout token behavior: fixed / min / max / grow / fluid / clamp
- traceability of mockup colors, spacing, sizing, type, radius, shadows, and breakpoints to tokens.json
- visual hierarchy
- responsive behavior
- accessibility requirements
- mismatch between design artifacts and mockups
- unresolved open questions
- production UI risks

Return:
1. Ready / not ready verdict
2. Critical blockers
3. Important non-blocking issues
4. Missing states or screens
5. Component and token gaps
6. Token traceability and sizing-behavior issues
7. Accessibility and responsive risks
8. Concrete revisions needed before production UI implementation
9. Suggested production UI build order if ready
```

## Prompt: production UI implementation from `/design` and browser mockups

```txt
Implement the MVP production UI from the repo design package and browser mockups.

Terminology:
- Production UI implementation means modifying the actual application UI codebase.
- /design/mockups contains design-stage HTML/CSS/JS references only.
- Do not copy prototype-only JavaScript into production application logic.

Source of truth:
- /specs/**/*.md for product behavior
- /design/tokens.json for visual primitives and semantic visual decisions
- /design/product-brief.md for product context
- /design/user-flows.md for core flows
- /design/screen-inventory.md for screens and states
- /design/ui-spec.md for layout, copy, component states, and interactions
- /design/component-inventory.md for reusable UI structure
- /design/states-and-edge-cases.md for state coverage
- /design/accessibility-notes.md for accessibility requirements
- /design/design-package-self-review.md for self-review findings
- /design/design-package-fresh-context-review.md for independent review findings, if present
- /design/production-ui-handoff-notes.md for implementation sequencing and risks
- /design/mockups/* as visual and interaction references only
- /design/mockups/consistency-check.md for known token and artifact traceability issues
- /design/svg/* as optional rough layout references only

Requirements:
- Use existing repo conventions and framework patterns.
- Create or update reusable components before pages.
- Create a minimal production design system from /design/tokens.json if none exists.
- Preserve token intent, including fixed/min/max/grow/fluid/clamp sizing behavior.
- Do not copy arbitrary mockup literals into production code when a token exists.
- Implement the primary MVP flow end-to-end.
- Include empty, loading, error, success, validation, permission, and destructive-confirmation states where specified.
- Implement responsive behavior from the reviewed design package, not from accidental mockup CSS drift.
- Ensure keyboard and screen-reader accessibility.
- Do not invent product behavior that is not in /specs or /design.
- Add or update tests where appropriate.
- Run lint, typecheck, and tests.
- Use browser verification for the completed flow.
- Summarize changed files, implemented screens, verified states, token mappings, and remaining design gaps.
```

## Production UI verification checklist

Before considering production UI implementation complete:

- [ ] Primary flow works end-to-end.
- [ ] Reusable components are implemented before duplicative screens.
- [ ] Production styles are driven by the project design system or tokens derived from `/design/tokens.json`.
- [ ] Sizing/layout behavior matches token intent.
- [ ] Empty, loading, error, success, validation, permission, and destructive-confirmation states are covered where specified.
- [ ] Responsive behavior is verified.
- [ ] Keyboard navigation is verified.
- [ ] Screen reader labels are present for icon-only controls.
- [ ] Form errors are announced or exposed accessibly.
- [ ] Contrast and visible focus are acceptable.
- [ ] Reduced-motion expectations are respected where relevant.
- [ ] Lint passes.
- [ ] Typecheck passes.
- [ ] Tests pass or missing tests are explicitly documented.
- [ ] Browser verification was performed.
- [ ] Remaining design gaps are summarized.

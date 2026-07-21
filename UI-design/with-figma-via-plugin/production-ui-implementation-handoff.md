# Production UI Implementation Handoff

This file defines implementation terminology and provides prompts for the moment when design work turns into production application UI code.

## Definition

**Implementation** means generating or changing production application UI code.

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

- design artifact generation
- SVG mockup generation
- static HTML/CSS prototype generation
- Claude Design canvas exploration
- html.to.design import
- rough Figma layer cleanup

Those are design workflow activities.

## Source-of-truth order

Use this order unless the project states otherwise:

1. `/specs/**/*.md` or PRD/functional specs for product behavior.
2. `/design/*` for product structure, screens, states, components, tokens, and visual system.
3. Refined Figma node links only after screens are manually cleaned up and approved.
4. SVG and static HTML/CSS mockups as visual references only.

## When `/design/*` is the implementation source

Use `/design/*` when:

- Figma does not exist
- Figma import has not been manually refined
- imported layers are rough
- visual fidelity is less important than product correctness
- production UI should create the real component system
- generated mockups are only visual references

## When exact Figma node links are the implementation source

Use exact Figma node links when:

- screens were manually cleaned up
- components and variants were organized in Figma
- stakeholders approved the screens
- layout fidelity is important
- the Figma file is more authoritative than generated mockups

Even then, keep specs and `/design/*` as the behavioral and structural source of truth.

## Prompt: production UI implementation from `/design/*`

```txt
Implement the MVP UI from the repo design package.

Source of truth:
- /specs/**/*.md for behavior
- /design/product-brief.md for product context
- /design/user-flows.md for core flows
- /design/screen-inventory.md for screens and states
- /design/ui-spec.md for layout, copy, component states, and interactions
- /design/component-inventory.md for reusable UI structure
- /design/tokens.json for the visual system
- /design/accessibility-notes.md for accessibility requirements
- /design/mockups/*.svg and /design/html-to-figma/* as visual references only

Requirements:
- Create a minimal design system from /design/tokens.json if none exists.
- Implement reusable components first.
- Implement the primary MVP flow end-to-end.
- Use existing repo conventions and framework patterns.
- Include empty, loading, error, and success states.
- Implement responsive behavior.
- Ensure keyboard and screen-reader accessibility.
- Add or update tests where appropriate.
- Run lint, typecheck, and tests.
- Use browser verification for the completed flow.
- Summarize changed files, implemented screens, and remaining design gaps.
```

## Prompt: production UI implementation from a refined Figma node

```txt
Implement this refined Figma design in the repo.

Figma source:
[paste exact Figma frame/node link]

Use the Figma frame as the visual source of truth.
Use /specs/**/*.md and /design/* as the behavioral and structural source of truth.

Requirements:
- Reuse existing repo structure and framework conventions.
- If the repo has no design system, create one from /design/tokens.json.
- Match layout, spacing, typography, color, radius, and states from the Figma node.
- Implement responsive behavior from /design/screen-inventory.md.
- Implement empty, loading, error, and success states.
- Ensure keyboard and screen-reader accessibility.
- Add or update tests where appropriate.
- Run lint, typecheck, and tests.
- Use browser verification to compare the implementation against the Figma reference.
- Summarize changed files and any visual differences.
```

## Prompt: production UI implementation from Claude Design handoff bundle

```txt
Implement the production UI from the Claude Design handoff bundle.

Use:
- the handoff bundle for visual structure, design tokens, layout hierarchy, and referenced assets
- /specs/**/*.md for behavior
- /design/* for screen/state/component structure if present
- existing repo conventions and framework patterns

Requirements:
- Do not treat the handoff bundle as product behavior authority if it conflicts with /specs.
- Create or update reusable components before pages.
- Preserve the intended visual system from the bundle and /design/tokens.json.
- Include empty, loading, error, and success states.
- Implement responsive behavior.
- Ensure keyboard and screen-reader accessibility.
- Add or update tests where appropriate.
- Run lint, typecheck, and tests.
- Use browser verification for the completed flow.
- Summarize changed files, implemented screens, and remaining design gaps.
```

## Verification checklist

Before considering production UI implementation complete:

- [ ] Primary flow works end-to-end.
- [ ] Reusable components are implemented before duplicative screens.
- [ ] Empty, loading, error, and success states are covered.
- [ ] Responsive behavior is verified.
- [ ] Keyboard navigation is verified.
- [ ] Screen reader labels are present for icon-only controls.
- [ ] Contrast and visible focus are acceptable.
- [ ] Lint passes.
- [ ] Typecheck passes.
- [ ] Tests pass or missing tests are explicitly documented.
- [ ] Browser verification was performed.
- [ ] Remaining design gaps are summarized.

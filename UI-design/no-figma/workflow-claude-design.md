# Workflow: Claude Design to HTML-CSS-JS Mockups

Use this workflow when you want canvas-based visual exploration first, but the final package target is browser-previewable HTML/CSS/JS mockups.

The target is not production application code. The target is a design-stage mockup package that can be reviewed in a browser and used as a reference for later production UI implementation.

## Best for

- visual exploration before browser mockups
- quickly testing layout direction, density, and UI personality
- using a canvas to iterate on screens before codifying the result
- producing browser mockups after the design direction stabilizes

## Not best for

- skipping textual design artifacts entirely
- production UI implementation
- treating a visual canvas as the only source of truth
- large systems without a reviewed design package

## Output

```txt
/design
  product-brief.md
  ux-principles.md
  visual-direction.md
  information-architecture.md
  user-flows.md
  screen-inventory.md
  ui-spec.md
  component-inventory.md
  states-and-edge-cases.md
  accessibility-notes.md
  tokens.json
  design-package-self-review.md
  design-package-fresh-context-review.md   # optional
  open-questions.md

  /mockups
    README.md
    index.html
    styles.css
    app.js                              # optional; prototype-only
    states.html
    consistency-check.md
    /screens                            # optional for larger flows
```

Optional quick-look output:

```txt
/design/svg
  index.html
  *.svg
  svg-generation-notes.md
  svg-consistency-check.md
```

## Model allocation

Use the cheaper model for:

- extracting or preparing textual design artifacts
- creating routine mockup files
- applying specific revision instructions
- same-agent self-consistency checks

Use a stronger or higher-effort model for:

- fresh-context design-package review
- critique of Claude Design output against the reviewed design package
- critique of product hierarchy and UX risks
- final readiness review before production UI implementation

## Workflow sequence

```txt
1. Main agent gathers PRD, functional specs, constraints, and any existing visual direction.
2. Main agent delegates design package creation to a subagent when the task is non-trivial.
3. Subagent creates /design/*.
4. Generating agent runs mandatory design-package self-review.
5. Generating agent revises /design/*.
6. Agent asks developer whether to run fresh-context consistency review.
7. If approved, separate reviewer agent reviews /design/*.
8. Generating agent revises /design/* again.
9. Use the reviewed package to guide Claude Design exploration.
10. Translate the stabilized visual direction into browser-previewable HTML/CSS/JS mockups.
11. Generate states.html as a consolidated state gallery.
12. Run mandatory mockup consistency check against tokens.json and /design/*.
13. Revise mockups and update /design/* where needed.
14. Stop, or run production UI implementation handoff if real app UI code is next.
```

## Step 1 — Create the design package using a subagent

Do not start with canvas exploration alone for non-trivial products. First create a compact, reviewable design package.

Prompt:

```txt
You are the design-package generation subagent.

Read the PRD, functional specs, and any existing visual or brand constraints provided by the main agent.

Create a design package under /design that can guide both visual exploration and browser mockup generation.

Produce:
- /design/product-brief.md
- /design/ux-principles.md
- /design/visual-direction.md
- /design/information-architecture.md
- /design/user-flows.md
- /design/screen-inventory.md
- /design/ui-spec.md
- /design/component-inventory.md
- /design/states-and-edge-cases.md
- /design/accessibility-notes.md
- /design/tokens.json
- /design/open-questions.md

Token requirements:
- tokens.json is the single source of truth for color, spacing, sizing, radius, typography, shadows/elevation, and breakpoints.
- Every sizing/layout token must state behavior: fixed, min, max, grow, fluid, or clamp.
- The package must define layout-sensitive requirements explicitly: page max width, major container behavior, grids, cards, sidebars, modals, breakpoints, and responsive stacking behavior.
- Visual direction and screen specs must not contradict token intent.

Do not generate browser mockups yet.
Do not generate production application code.
Return only a concise summary, file list, assumptions, open questions, and risks to the main agent.
```

## Step 2 — Mandatory same-agent design-package self-review

Run this before using the design package to guide Claude Design or browser mockups.

Prompt:

```txt
Review the design package you just generated for consistency, coverage, clarity, and token traceability.

Inputs:
- PRD / functional specs
- /design/product-brief.md
- /design/ux-principles.md
- /design/visual-direction.md
- /design/information-architecture.md
- /design/user-flows.md
- /design/screen-inventory.md
- /design/ui-spec.md
- /design/component-inventory.md
- /design/states-and-edge-cases.md
- /design/accessibility-notes.md
- /design/tokens.json
- /design/open-questions.md

Check:
- product hierarchy is clear enough for visual exploration
- screens match user flows
- user flows match functional specs
- ui-spec covers every priority screen
- states are complete and not contradictory
- components are named consistently
- visual direction can be expressed through tokens.json
- every sizing/layout token has behavior: fixed, min, max, grow, fluid, or clamp
- layout constraints such as widths, max-widths, minimum card sizes, sidebars, and breakpoints are explicit
- accessibility notes cover keyboard, focus, semantics, labels, and error states
- open questions contain real ambiguities only

Save the review as /design/design-package-self-review.md.
Then revise the design package to resolve all critical and important issues before proceeding.
```

## Step 3 — Ask about fresh-context review

After self-review and revisions, ask the developer:

```txt
Would you like a fresh-context consistency review before visual exploration and mockup generation?
Recommended for multi-screen or non-trivial packages. This uses another agent, ideally with a stronger model, to review /design/* without authoring-memory bias.
```

Fresh-context review prompt:

```txt
You are a fresh-context design package reviewer. You did not author this package.

Review /design/* in read-only mode.

Assess:
- consistency with the functional specs
- coverage of screens, flows, states, and edge cases
- clarity of product hierarchy
- whether the package is specific enough to guide canvas-based exploration
- component naming and reuse
- visual direction consistency
- tokens.json completeness
- sizing/layout token behavior: fixed, min, max, grow, fluid, clamp
- contradictions between visual-direction.md, ui-spec.md, screen-inventory.md, component-inventory.md, states-and-edge-cases.md, and tokens.json
- accessibility and responsive risks
- anything likely to cause browser mockups to drift from the design package

Return:
1. Critical issues
2. Important issues
3. Nice-to-have improvements
4. Token and sizing behavior issues
5. Missing screens, states, or components
6. Specific revision instructions

Save as /design/design-package-fresh-context-review.md.
Do not generate mockups.
Do not rewrite the package directly unless asked.
```

If skipped, record that it was skipped in `/design/mockups/README.md` later.

## Step 4 — Use Claude Design for exploration

Use the reviewed design package as the briefing material.

Prompt for Claude Design:

```txt
Use the reviewed design package below to explore the visual direction for the priority screens.

Design from:
- product brief
- UX principles
- visual direction
- information architecture
- user flows
- screen inventory
- UI spec
- component inventory
- states and edge cases
- accessibility notes
- tokens.json

Important constraints:
- tokens.json is the single source of truth for color, spacing, sizing, radius, typography, shadows/elevation, and breakpoints.
- Respect sizing/layout token behavior: fixed, min, max, grow, fluid, or clamp.
- Do not reinterpret fixed width as flexible growth or max width as fixed width.
- Do not invent product behavior outside the specs.
- Include visual treatment for empty, loading, error, success, validation, permission, disabled, and destructive-confirmation states where relevant.

Return a visual direction that can be translated into browser-previewable HTML/CSS/JS mockups.
```

## Step 5 — Critique the visual exploration

Use a stronger model if the output will guide a full mockup package.

Prompt:

```txt
Critique the current visual exploration against the reviewed design package.

Assess:
- product hierarchy
- information hierarchy
- screen-to-screen consistency
- component consistency
- state coverage
- layout density
- responsive risks
- accessibility risks
- token consistency
- whether widths and layout behavior match tokens.json
- any drift from the functional specs or /design/*

Return prioritized revision instructions.
Do not regenerate the design from scratch.
```

Apply the revision instructions before producing browser mockups.

## Step 6 — Generate HTML/CSS/JS mockups

Prompt:

```txt
Translate the stabilized visual direction and reviewed /design package into browser-previewable design-stage mockups.

Create:
- /design/mockups/README.md
- /design/mockups/index.html
- /design/mockups/styles.css
- /design/mockups/app.js, only if prototype-only interactions improve review
- /design/mockups/states.html
- optional /design/mockups/screens/*.html for larger flows

Requirements:
- Use semantic HTML.
- Use CSS variables generated from /design/tokens.json.
- tokens.json is the single source of truth for color, spacing, sizing, radius, typography, shadows/elevation, and breakpoints.
- Do not restate a token's value as a disconnected CSS literal.
- Do not override a token's intent.
- Widths, min-widths, max-widths, heights, spacing, radius, type sizes, line heights, shadows, and breakpoints must trace to tokens.
- Respect sizing/layout token behavior: fixed, min, max, grow, fluid, or clamp.
- Use readable class names that map to component-inventory.md.
- Include realistic placeholder data.
- Include responsive behavior for priority viewports.
- Use prototype-only JavaScript only for reviewable interactions such as tabs, menus, modals, state toggles, and simple validation demos.
- Include inline annotations for assumptions and unresolved questions.
- Include states.html as a consolidated state gallery.
- Do not generate production application code.
```

## Step 7 — Mandatory mockup consistency check

Run this before calling the workflow complete.

Prompt:

```txt
Run a mockup self-consistency check.

Inputs:
- /design/tokens.json
- /design/visual-direction.md
- /design/screen-inventory.md
- /design/ui-spec.md
- /design/component-inventory.md
- /design/states-and-edge-cases.md
- /design/accessibility-notes.md
- /design/mockups/*

Check every layout-affecting value in the mockups:
- colors
- spacing
- widths
- min-widths
- max-widths
- heights
- radii
- shadows
- typography sizes
- line heights
- breakpoints

For each value, verify that it traces to tokens.json or is documented as an intentional exception.

Also check:
- every mockup screen matches screen-inventory.md and ui-spec.md
- every reusable visual pattern maps to component-inventory.md
- every required state is represented in states.html or explicitly deferred
- responsive behavior follows the design package
- prototype-only JS does not invent product behavior
- no artifact contradicts tokens.json

Resolve conflicts in favor of tokens.json and the reviewed design package.
Save the report as /design/mockups/consistency-check.md.
Revise mockups after the report.
```

## Optional SVG quick-look

SVG quick-look is optional in this workflow. Use it only when the team wants a fast static first look before or instead of full browser mockups.

If generated, SVGs must follow `tokens.json`, document exceptions, and include `/design/svg/svg-consistency-check.md`.

## Done criteria

The workflow is complete only when:

- `/design/*` exists
- `/design/design-package-self-review.md` exists
- the developer was asked about fresh-context review
- fresh-context review was completed or explicitly skipped
- the stabilized visual direction has been translated into browser mockups
- `/design/mockups/index.html` exists
- `/design/mockups/states.html` exists
- `/design/mockups/consistency-check.md` exists
- `styles.css` consumes `tokens.json` through CSS variables
- sizing/layout behavior follows token intent
- known token exceptions are documented
- no production application UI code was generated unless the task explicitly moved to production UI implementation

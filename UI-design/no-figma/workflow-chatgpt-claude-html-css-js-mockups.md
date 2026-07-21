# Workflow: ChatGPT / Claude Chat HTML-CSS-JS Mockups

Use this workflow when you want a chat-based agent to turn specs and design artifacts into browser-previewable HTML/CSS/JS mockups.

The target is not production application code. The target is a design-stage mockup package that can be reviewed in a browser.

## Best for

- quick design exploration from text
- one screen or a small multi-screen flow
- low-cost browser mockups
- evaluating hierarchy, copy, layout, states, and basic interactions
- producing a concrete reference before production UI implementation

## Not best for

- production UI code
- full app implementation
- complex repo-aware generation
- very large products without a repo agent

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

- first-pass design package generation
- first-pass HTML/CSS/JS mockup generation
- routine revisions
- same-agent self-consistency checks

Use a stronger or higher-effort model for:

- fresh-context design-package review
- critique of visual hierarchy and UX risks
- final readiness review before production UI implementation

## Workflow sequence

```txt
1. Main agent gathers specs and constraints.
2. Main agent delegates design package creation to a subagent when the task is non-trivial.
3. Subagent creates /design/*.
4. Generating agent runs mandatory design-package self-review.
5. Generating agent revises /design/*.
6. Agent asks developer whether to run fresh-context consistency review.
7. If approved, separate reviewer agent reviews /design/*.
8. Generating agent revises /design/* again.
9. Optional: generate SVG quick-look files.
10. Generate browser-previewable HTML/CSS/JS mockups.
11. Generate states.html as a consolidated state gallery.
12. Run mandatory mockup consistency check against tokens.json and /design/*.
13. Revise mockups and update /design/* where needed.
14. Stop, or run production UI implementation handoff if real app UI code is next.
```

## Step 1 — Create the design package using a subagent

For non-trivial packages, use a subagent so the main conversation does not become overloaded with design-generation detail.

Prompt:

```txt
You are the design-package generation subagent.

Read the PRD, functional specs, and any existing product notes provided by the main agent.

Create a browser-mockup-oriented design package under /design.

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
- Visual and layout decisions in the Markdown artifacts must reference token intent where relevant.
- Do not leave width, max-width, min-width, height, spacing, radius, type, shadow, or breakpoint decisions implicit if they affect the mockups.

Do not create browser mockups yet.
Do not generate production application code.
Return only a concise summary, file list, assumptions, open questions, and risks to the main agent.
```

## Step 2 — Mandatory same-agent design-package self-review

Run this every time before mockup generation.

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
- screens match user flows
- user flows match functional specs
- ui-spec covers every priority screen
- states are complete and not contradictory
- components are named consistently
- visual direction is reflected in tokens.json
- every sizing/layout token has behavior: fixed, min, max, grow, fluid, or clamp
- every layout-sensitive rule has an obvious token or a documented reason to become a token
- accessibility notes cover keyboard, focus, semantics, labels, and error states
- open questions contain real ambiguities only

Save the review as /design/design-package-self-review.md.
Then revise the design package to resolve all critical and important issues before proceeding.
```

## Step 3 — Ask about fresh-context review

After self-review and revisions, ask the developer:

```txt
Would you like a fresh-context consistency review before mockup generation?
Recommended for multi-screen or non-trivial packages. This uses another agent, ideally with a stronger model, to review /design/* without authoring-memory bias.
```

If the developer says yes, run the review before mockup generation.

Fresh-context review prompt:

```txt
You are a fresh-context design package reviewer. You did not author this package.

Review /design/* in read-only mode.

Assess:
- consistency with the functional specs
- coverage of screens, flows, states, and edge cases
- clarity of product hierarchy
- clarity of primary and secondary actions
- component naming and reuse
- visual direction consistency
- tokens.json completeness
- sizing/layout token behavior: fixed, min, max, grow, fluid, clamp
- contradictions between visual-direction.md, ui-spec.md, screen-inventory.md, component-inventory.md, states-and-edge-cases.md, and tokens.json
- accessibility and responsive risks
- anything likely to cause mockups to drift from the design package

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

## Step 4 — Optional SVG quick-look

Use SVG only when a quick first-look is useful before spending time on browser mockups.

Prompt:

```txt
Generate optional SVG quick-look files from the reviewed design package.

Create:
- /design/svg/index.html
- one SVG per priority screen or layout variant
- /design/svg/svg-generation-notes.md
- /design/svg/svg-consistency-check.md

Requirements:
- Use tokens.json as the source for colors, spacing, sizing, radius, typography, shadows, and breakpoints.
- Do not restate token-equivalent values as arbitrary literals.
- If an SVG value cannot reasonably be tokenized, document it as an intentional exception.
- Treat SVGs as rough first-look artifacts only.
- Do not create production UI code.
```

## Step 5 — Generate HTML/CSS/JS mockups

Prompt:

```txt
Generate browser-previewable design-stage mockups from the reviewed /design package.

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

## Step 6 — Mandatory mockup consistency check

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
- /design/svg/* if present

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
If SVG files exist, save SVG-specific findings as /design/svg/svg-consistency-check.md.
Revise mockups after the report.
```

## Done criteria

The workflow is complete only when:

- `/design/*` exists
- `/design/design-package-self-review.md` exists
- the developer was asked about fresh-context review
- fresh-context review was completed or explicitly skipped
- `/design/mockups/index.html` exists
- `/design/mockups/states.html` exists
- `/design/mockups/consistency-check.md` exists
- `styles.css` consumes `tokens.json` through CSS variables
- sizing/layout behavior follows token intent
- known token exceptions are documented
- no production application UI code was generated unless the task explicitly moved to production UI implementation

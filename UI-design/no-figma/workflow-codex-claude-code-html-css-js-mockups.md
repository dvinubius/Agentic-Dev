# Workflow: Codex / Claude Code HTML-CSS-JS Mockups

Use this workflow when a repo-aware agent can read specs from the codebase and generate a repo-owned design package plus browser-previewable mockups.

The target is not production application code. The target is `/design/*` plus `/design/mockups/*` that can guide review and later production UI implementation.

## Best for

- projects with specs already in the repo
- multi-screen design packages
- keeping design artifacts versioned with the codebase
- generating browser mockups from repo-owned artifacts
- using subagents to avoid context bloat in the main thread

## Not best for

- one-off tiny mockups where a chat workflow is enough
- production UI implementation without a reviewed design package
- skipping consistency checks

## Expected input

```txt
/specs/**/*.md
AGENTS.md, if present
existing product notes, if present
existing design tokens or styles, if present
```

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
  production-ui-handoff-notes.md
  open-questions.md

  /mockups
    README.md
    index.html
    styles.css
    app.js                              # optional; prototype-only
    states.html
    consistency-check.md
    /screens                            # optional for larger flows
      dashboard.html
      settings.html
      project-detail.html
    /assets                             # optional placeholder assets only
```

Optional quick-look output:

```txt
/design/svg
  index.html
  *.svg
  svg-generation-notes.md
  svg-consistency-check.md
```

## Model and agent allocation

Use the cheaper repo agent or subagent for:

- reading specs
- generating the first-pass design package
- generating HTML/CSS/JS mockups
- applying concrete revision instructions
- mandatory same-agent self-consistency checks

Use a stronger or higher-effort model for:

- fresh-context design-package review
- critique of multi-screen UX hierarchy
- token and cross-file consistency review
- final production UI readiness review

## Workflow sequence

```txt
1. Main agent reads repo instructions and identifies relevant specs.
2. Main agent delegates design package creation to a subagent.
3. Design-package subagent creates /design/*.
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

## Step 1 — Add or update repo instructions

Add this to the repo-level `AGENTS.md` or equivalent instruction file.

```md
## Product and design source of truth

- Functional specs live in /specs/**/*.md or the project-specific specs directory.
- Generated design artifacts live in /design.
- Browser mockups live in /design/mockups.
- Optional SVG quick-look files live in /design/svg.
- Treat specs as canonical for product behavior.
- Treat /design/tokens.json as canonical for color, spacing, sizing, radius, typography, shadows/elevation, and breakpoints.
- Treat the rest of /design/* as canonical for screens, flows, states, components, visual direction, accessibility requirements, and interaction intent.
- Do not invent product behavior that is not in specs.
- Do not invent visual rules after /design/tokens.json exists; update tokens.json instead.
- Mockups must consume tokens through CSS variables.
- Do not restate a token value as an unrelated literal in mockup CSS, HTML inline styles, JS style mutations, or SVG attributes.
- Every sizing/layout token must state behavior: fixed, min, max, grow, fluid, or clamp.
- Run a mandatory design-package self-review before mockup generation.
- Ask the developer whether to run a fresh-context consistency review before mockup generation.
- Run a mandatory mockup consistency check before considering the workflow complete.

## Terminology

- Design workflow means generating /design artifacts and browser-reviewable mockups.
- Mockup generation means creating HTML, CSS, optional prototype-only JavaScript, and optional SVG files for review.
- Production UI implementation means modifying the actual application UI codebase.
- Do not call mockup generation implementation.
```

## Step 2 — Generate the design package using a subagent

Use a subagent for design-package generation to avoid context bloat in the main thread.

Prompt:

```txt
You are the design-package generation subagent.

Read:
- AGENTS.md
- all relevant specs under /specs/**/*.md
- any existing design, style, or token files in the repo

Create a browser-mockup-oriented design package in /design.

Produce:
1. /design/product-brief.md
   - product summary
   - core user roles
   - primary jobs-to-be-done
   - key workflows
   - constraints and assumptions

2. /design/ux-principles.md
   - UX principles inferred from the product domain
   - interaction principles
   - accessibility principles
   - what the UX should avoid

3. /design/visual-direction.md
   - visual personality
   - layout density
   - typography direction
   - color direction
   - motion and interaction direction for prototype-only interactions
   - what the UI should avoid visually

4. /design/information-architecture.md
   - primary navigation
   - secondary navigation
   - major content areas
   - route/screen hierarchy if applicable

5. /design/user-flows.md
   - core user journeys
   - alternate paths
   - edge cases
   - permissions/auth states

6. /design/screen-inventory.md
   For every screen:
   - screen name
   - purpose
   - entry points
   - data shown
   - user actions
   - validation rules
   - empty/loading/error/success states
   - permission states
   - responsive behavior
   - accessibility notes
   - token-relevant layout requirements

7. /design/ui-spec.md
   For priority screens:
   - layout sections
   - visual hierarchy
   - components
   - copy and placeholder content
   - component states
   - validation rules
   - responsive behavior notes
   - prototype-only interaction rules
   - explicit references to relevant layout/sizing tokens

8. /design/component-inventory.md
   - required UI components
   - reusable patterns
   - variants and states
   - token dependencies
   - missing components

9. /design/states-and-edge-cases.md
   - global app states
   - per-screen states
   - validation failures
   - network failures
   - permission failures
   - destructive-action confirmations
   - success flows
   - optimistic update failures where relevant
   - which representative states should appear in /design/mockups/states.html

10. /design/accessibility-notes.md
    - semantic HTML requirements
    - keyboard navigation
    - focus order
    - visible focus
    - screen reader labels
    - error announcement behavior
    - reduced-motion expectations

11. /design/tokens.json
    Include:
    - color tokens
    - typography tokens
    - spacing scale
    - sizing and layout tokens
    - radius scale
    - shadow/elevation scale
    - breakpoint tokens
    - semantic tokens

    Requirements:
    - tokens.json is the single source of truth for color, spacing, sizing, radius, typography, shadows/elevation, and breakpoints.
    - Every sizing/layout token must state behavior: fixed, min, max, grow, fluid, or clamp.
    - Every token should include value and intent/description.
    - Width, max-width, min-width, height, spacing, radius, type, shadow, and breakpoint decisions must be tokenized or explicitly marked as open questions.

12. /design/production-ui-handoff-notes.md
    - recommended production UI build order, if later needed
    - reusable components to build first
    - routing implications
    - state/data dependencies
    - accessibility requirements
    - testing recommendations
    - known risks

13. /design/open-questions.md
    - list only genuine ambiguities
    - mark each as blocking or non-blocking

Do not generate browser mockups yet.
Do not generate production application code.
Return only a concise summary, file list, assumptions, open questions, and risks to the main agent.
```

## Step 3 — Mandatory same-agent design-package self-review

Run this every time before visual mockup generation.

Prompt:

```txt
Review the design package you just generated for consistency, coverage, clarity, and token traceability.

Inputs:
- AGENTS.md
- /specs/**/*.md
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
- /design/production-ui-handoff-notes.md
- /design/open-questions.md

Check:
- every functional spec requirement is represented or explicitly deferred
- screens match user flows
- user flows match functional specs
- screen-inventory and ui-spec agree
- states-and-edge-cases covers required screen states
- component-inventory covers repeated UI patterns
- component names are consistent across files
- visual-direction.md is compatible with tokens.json
- tokens.json contains all visual primitives needed by mockups
- every sizing/layout token has behavior: fixed, min, max, grow, fluid, or clamp
- layout requirements such as content width, sidebars, grids, cards, modals, and breakpoints are tokenized
- open questions contain real ambiguities only
- no artifact contradicts another artifact

Save the review as /design/design-package-self-review.md.
Then revise /design/* to resolve critical and important issues before proceeding.
```

## Step 4 — Ask about fresh-context review

After self-review and revisions, ask the developer:

```txt
Would you like a fresh-context consistency review before mockup generation?
Recommended for multi-screen or non-trivial packages. This uses another agent, ideally with a stronger model, to review /design/* without authoring-memory bias.
```

Fresh-context review prompt:

```txt
You are a fresh-context design package reviewer. You did not author this package.

Review /design/* in read-only mode.

Inputs:
- AGENTS.md
- /specs/**/*.md
- /design/*

Assess:
- consistency with functional specs
- coverage of screens, flows, states, and edge cases
- clarity of product hierarchy
- clarity of primary and secondary actions
- navigation and information architecture
- component reuse and naming consistency
- visual direction consistency
- tokens.json completeness
- token behavior consistency, especially fixed/min/max/grow/fluid/clamp layout rules
- contradictions between artifacts
- accessibility requirements
- responsive behavior requirements
- unresolved ambiguity and risk
- whether the package is ready for browser mockup generation

Return:
1. Ready / not ready verdict for mockup generation
2. Critical issues
3. Important issues
4. Nice-to-have improvements
5. Token and sizing behavior issues
6. Missing screens, states, or components
7. Specific revision instructions

Save as /design/design-package-fresh-context-review.md.
Do not generate mockups.
Do not rewrite the package directly unless asked.
```

If skipped, record that it was skipped in `/design/mockups/README.md` later.

## Step 5 — Optional SVG quick-look

SVG quick-look can be useful before producing full browser mockups, but it is optional.

Prompt:

```txt
Generate optional SVG quick-look files from the reviewed design package.

Create:
- /design/svg/index.html
- one SVG per priority screen or layout variant
- /design/svg/svg-generation-notes.md
- /design/svg/svg-consistency-check.md

Requirements:
- Use /design/tokens.json as the source for colors, spacing, sizing, radius, typography, shadows, and breakpoints.
- Do not restate token-equivalent values as arbitrary literals.
- Respect sizing/layout token behavior: fixed, min, max, grow, fluid, or clamp.
- If an SVG value cannot reasonably be tokenized, document it as an intentional exception.
- Treat SVGs as rough first-look artifacts only.
- Do not generate production UI code.
```

## Step 6 — Generate HTML/CSS/JS mockups

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
- optional /design/mockups/assets/* placeholder assets

Requirements:
- Use semantic HTML.
- Use CSS variables generated from /design/tokens.json.
- tokens.json is the single source of truth for color, spacing, sizing, radius, typography, shadows/elevation, and breakpoints.
- Do not restate a token's value as a disconnected CSS literal.
- Do not override a token's intent.
- Widths, min-widths, max-widths, heights, spacing, radius, type sizes, line heights, shadows, and breakpoints must trace to tokens.
- Respect sizing/layout token behavior: fixed, min, max, grow, fluid, or clamp.
- Use readable class names that map to /design/component-inventory.md.
- Include realistic placeholder data.
- Include responsive behavior for priority viewports.
- Use prototype-only JavaScript only for reviewable interactions such as tabs, menus, modals, state toggles, and simple validation demos.
- Include inline annotations for assumptions and unresolved questions.
- Include /design/mockups/states.html as a consolidated state gallery rather than creating a combinatorial explosion of state files.
- Do not generate production application code.
```

## Step 7 — Mandatory mockup consistency check

Run this before calling the workflow complete.

Prompt:

```txt
Run a mockup self-consistency check.

Inputs:
- AGENTS.md
- /specs/**/*.md
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
- no artifact contradicts another artifact without a documented resolution

Resolve conflicts in favor of tokens.json and the reviewed design package.
Save the report as /design/mockups/consistency-check.md.
If SVG files exist, save SVG-specific findings as /design/svg/svg-consistency-check.md.
Revise mockups after the report.
```

## Step 8 — Browser preview

Preview locally from `/design/mockups`.

Example:

```bash
cd design/mockups
python3 -m http.server 4173
```

Open:

```txt
http://localhost:4173/index.html
http://localhost:4173/states.html
```

Check:

- primary screens render
- navigation between mockup screens works if included
- prototype-only interactions work if included
- responsive behavior works at target widths
- states.html covers representative states
- visual values respect token intent

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
- browser preview was checked
- no production application UI code was generated unless the task explicitly moved to production UI implementation

# Agentic Design Workflows

Agentic design can be done in multiple ways using different tools. This package assumes the product already has a PRD, functional specifications, or equivalent behavior documentation.

The target is deliberately simple:

```txt
functional specs
→ design-package subagent creates /design/*
→ generating agent runs mandatory self-consistency review
→ optional fresh-context review by another agent / stronger model
→ revised design package
→ browser-previewable HTML/CSS/JS mockups
→ mandatory mockup consistency check against tokens.json and /design/*
→ production UI implementation handoff, if needed
```

HTML/CSS/JS mockups are the primary design-stage visual artifact. SVG generation remains available only as an optional quick first-look step.

## Terminology

**Design workflow** means turning product behavior into design artifacts and browser-reviewable mockups.

**Design package** means the Markdown and JSON artifacts under `/design` that define structure, hierarchy, states, components, accessibility requirements, visual direction, and tokens.

**Mockup generation** means creating HTML, CSS, optional prototype-only JavaScript, and optional SVG files for design review.

**Production UI implementation** means generating or modifying the actual application UI code. This includes framework components, routes, pages, production styles, accessibility behavior, tests, and browser verification.

Do not use the word implementation for mockup generation unless the task explicitly targets production application code.

## Choosing a workflow

Use the questions below to pick the right workflow:

- Do you want quick browser mockups from text? Use the ChatGPT / Claude Chat workflow.
- Do you want visual exploration and canvas-based iteration first? Use the Claude Design workflow.
- Do you want repo-owned design artifacts and mockups generated from specs in the codebase? Use the Codex / Claude Code workflow.
- Do you need only a first look at layout and density? Add the optional SVG quick-look step.
- Are mockups about to guide production application UI code? Run the production UI implementation handoff review.

## Package files

```txt
agentic-design-workflows.md
  Main routing guide.

design-artifact-definitions.md
  Definitions for the design package, token rules, review artifacts, mockup files, states gallery, and optional SVG quick-look files.

workflow-chatgpt-claude-html-css-js-mockups.md
  Chat-based workflow for generating browser mockups.

workflow-claude-design.md
  Claude Design workflow that ends in browser-previewable HTML/CSS/JS mockups.

workflow-codex-claude-code-html-css-js-mockups.md
  Repo-aware workflow for generating /design and /design/mockups.

production-ui-implementation-handoff.md
  Boundary and prompts for turning approved design artifacts and mockups into production app UI code.
```

## Shared source-of-truth model

The design package is the source of truth for design structure. Browser mockups visualize and test that package.

Recommended authority order:

1. Functional specs are canonical for product behavior.
2. `tokens.json` is canonical for color, spacing, sizing, radius, typography, shadow/elevation, and breakpoint decisions.
3. The rest of `/design/*` is canonical for screens, states, components, visual direction, accessibility requirements, and interaction intent.
4. Browser mockups are review artifacts, not product behavior authority.
5. Optional SVGs are rough first-look artifacts only.

If artifacts conflict, resolve in favor of the higher-authority source and update the lower-authority artifact.

## Token enforcement rules

These rules apply to every workflow.

`tokens.json` is the single source of truth for:

- color
- spacing
- sizing
- radius
- typography
- shadow / elevation
- breakpoints
- semantic visual decisions

Rules:

- Mockups must consume `tokens.json` through CSS variables.
- Do not restate a token value as an unrelated literal in CSS, HTML inline styles, JS style mutations, or SVG attributes.
- Do not override a token's intent with local CSS that contradicts the token name or documented behavior.
- Every sizing or layout token must state behavior, not only value.
- Behavior must be explicit: `fixed`, `min`, `max`, `grow`, `fluid`, or `clamp`.
- Width, max-width, min-width, height, spacing, radius, type size, line height, shadows, and breakpoints must be traceable to tokens or documented as intentional exceptions.
- Intentional exceptions must be listed in the relevant consistency report and in `mockups/README.md`.

Example token shape:

```json
{
  "size": {
    "contentMaxWidth": {
      "value": "1120px",
      "behavior": "max",
      "description": "Maximum width for primary page content containers."
    },
    "sidebarWidth": {
      "value": "280px",
      "behavior": "fixed",
      "description": "Desktop navigation sidebar width."
    },
    "cardMinWidth": {
      "value": "280px",
      "behavior": "min",
      "description": "Minimum width before cards wrap or stack."
    }
  }
}
```

## Default design package structure

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
    app.js                              # optional; prototype-only interactions
    states.html                         # consolidated state gallery
    consistency-check.md                # mandatory after mockup generation
    /screens                            # optional for larger flows
      dashboard.html
      settings.html
      project-detail.html
    /assets                             # optional placeholder assets only

  /svg                                  # optional quick first-look only
    index.html
    *.svg
    svg-generation-notes.md
    svg-consistency-check.md            # mandatory if SVGs are generated
```

For small work, the package can be lighter. For repo-centered work, keep this structure so design artifacts and mockups remain synchronized.

## Subagent-first design package generation

For non-trivial work, the main conversation should not carry the full design-generation burden.

Recommended pattern:

```txt
main agent / orchestrator
→ delegates design package creation to a subagent
→ receives concise subagent summary and file list
→ runs or delegates review
→ delegates mockup generation using the reviewed /design package
```

Benefits:

- avoids context bloat in the main thread
- keeps design package generation focused
- leaves the main thread available for decisions, review, and handoff
- makes fresh-context review easier and more meaningful

The subagent should write files, not long prose back into the main conversation. The main agent should ask for only:

- created files
- assumptions
- open questions
- known risks
- next recommended step

## Mandatory design-package self-review

Every workflow must include a same-agent self-review after the design package is generated and before browser mockups are produced.

The generating agent must cross-check:

- every design artifact against functional specs
- every screen in `screen-inventory.md` against `user-flows.md`
- every component in `ui-spec.md` against `component-inventory.md`
- every state in `screen-inventory.md` against `states-and-edge-cases.md`
- every visual rule in `visual-direction.md` against `tokens.json`
- every sizing/layout decision against token behavior
- every unresolved ambiguity against `open-questions.md`

The output must be saved as:

```txt
/design/design-package-self-review.md
```

The agent must revise the design package after this self-review before moving forward.

## Optional fresh-context design-package review

After the mandatory self-review and revisions, the agent should pause and ask the developer:

```txt
Would you like a fresh-context consistency review before mockup generation?
Recommended for multi-screen or non-trivial packages. This uses another agent, ideally with a stronger model, to review /design/* without authoring-memory bias.
```

If the developer says yes, use a separate agent or stronger model in read-only review mode.

The fresh-context reviewer should check:

- consistency with functional specs
- coverage of screens, flows, states, and edge cases
- clarity of product hierarchy
- clarity of primary and secondary actions
- navigation and information architecture
- component reuse and naming consistency
- visual direction and token completeness
- token behavior consistency, especially fixed/min/max/grow layout rules
- accessibility requirements
- responsive behavior requirements
- contradictions between artifacts
- unresolved ambiguity and risk

The output should be saved as:

```txt
/design/design-package-fresh-context-review.md
```

The generating agent should then revise the design package before producing HTML/CSS/JS mockups.

For a single-screen mockup, the developer may skip this step. For a full package or a multi-screen flow, it is strongly recommended.

## Mandatory mockup consistency check

Before any workflow is considered complete, the generating agent must run a consistency pass over the mockups.

The agent must cross-check:

- every color against `tokens.json`
- every spacing value against `tokens.json`
- every width, max-width, min-width, height, and breakpoint against `tokens.json`
- every radius, type size, line height, and shadow against `tokens.json`
- every screen against `screen-inventory.md`
- every component against `component-inventory.md`
- every state represented in `states.html` against `states-and-edge-cases.md`
- every layout rule against the token behavior field: fixed / min / max / grow / fluid / clamp
- every intentional literal or exception

The result must be saved as:

```txt
/design/mockups/consistency-check.md
```

If SVG quick-look files are generated, the result must also be saved as:

```txt
/design/svg/svg-consistency-check.md
```

The check should resolve conflicts in favor of `tokens.json` and the reviewed design package.

## Standard workflow sequence

```txt
1. Main agent delegates design package generation to a subagent when work is non-trivial.
2. Subagent generates /design/* from specs.
3. Generating agent runs mandatory design-package self-review.
4. Generating agent revises /design/*.
5. Agent asks developer whether to run optional fresh-context review.
6. If approved, separate reviewer agent reviews /design/*.
7. Generating agent revises /design/* again.
8. Optionally generate SVG quick-look files.
9. Generate browser-previewable HTML/CSS/JS mockups.
10. Include a consolidated states.html page.
11. Run mandatory mockup consistency check against tokens.json and /design/*.
12. Preview in a browser.
13. Revise mockups and update design package where needed.
14. Run production UI implementation handoff only when real app code will be generated.
```

## Optional SVG quick-look

SVG generation is optional. It is useful when you want a very fast first look at layout, density, and rough hierarchy before producing browser mockups.

Use SVG for:

- early layout comparison
- quick stakeholder review
- density checks
- presentation-only first look

Skip SVG when:

- HTML/CSS mockups can be generated directly
- interaction review matters
- state toggles matter
- the workflow needs to stay short

SVG files are never production UI assets. If generated, SVG files must still pass token and artifact consistency checks.

## HTML/CSS/JS mockup requirements

The primary visual output is a browser-readable mockup package.

Requirements:

- Use semantic HTML.
- Use CSS variables generated from `tokens.json`.
- Do not hardcode token-equivalent values as arbitrary literals.
- Use readable class names that map to components.
- Use prototype-only JavaScript only when it improves review of interactions.
- Include responsive behavior for the priority viewports.
- Include realistic placeholder data.
- Include inline annotations for assumptions and unresolved questions.
- Include `states.html` for consolidated state coverage.
- Include `README.md` with preview instructions, known gaps, token exceptions, and skipped review steps.

## State coverage strategy

States are easy to under-deliver. Do not rely on each screen file to accidentally cover them.

Default strategy:

```txt
/design/mockups/states.html
```

Use `states.html` as a consolidated state gallery that shows representative components and screens in:

- empty state
- loading state
- error state
- success state
- validation error state
- permission denied state
- disabled state
- destructive confirmation state
- optimistic update failure state, when relevant

For very large products, split state galleries by area, but keep an index page that links all state coverage.

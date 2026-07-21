# Design Artifact Definitions

This reference defines the design artifacts used across the agentic design workflows.

The target is a clear design package plus browser-previewable HTML/CSS/JS mockups. Optional SVG files may be used for quick first-look layout review.

## Default `/design` structure

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
    consistency-check.md                # mandatory
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

## Source-of-truth order

Use this order unless a project states otherwise:

1. Functional specs / PRD for product behavior.
2. `tokens.json` for visual primitives and semantic visual decisions.
3. Markdown artifacts in `/design/*` for structure, hierarchy, components, states, accessibility, and interaction intent.
4. Browser mockups in `/design/mockups/*` as visual and interaction review artifacts.
5. Optional SVGs in `/design/svg/*` as first-look layout artifacts only.

If artifacts contradict each other, resolve in favor of the higher-authority source and update the lower-authority artifact.

## Artifact definitions

### `product-brief.md`

Defines:

- product summary
- core user roles
- primary jobs-to-be-done
- key workflows
- constraints and assumptions
- what the design must optimize for

### `ux-principles.md`

Defines:

- UX principles inferred from the product domain
- interaction principles
- accessibility principles
- decision-making principles for tradeoffs
- what the UX should avoid

### `visual-direction.md`

Defines:

- visual personality
- layout density
- typography direction
- color direction
- motion and interaction direction for prototype-only interactions
- what the UI should avoid visually

Every visual rule here must be compatible with `tokens.json`. If a visual rule implies a token that does not exist, add or revise the token.

### `information-architecture.md`

Defines all screens, pages, routes, navigation groups, and content relationships.

Example format:

```txt
- Dashboard
  - Overview
  - Analytics
- Projects
  - Project List
  - Project Detail
    - Settings
    - Members
- Account
  - Profile
  - Billing
```

### `user-flows.md`

Defines step-by-step task completion paths, including branches, alternate paths, edge cases, and authentication or permission states.

Example format:

```txt
Flow: Create a new project
1. User clicks "New Project" on the Dashboard.
2. A modal appears with a Name field and a Template picker.
3a. If template selected → pre-fills settings.
3b. If "Blank" selected → all fields empty.
4. User fills in name and clicks "Create".
5. Redirected to the new Project Detail screen.
```

### `screen-inventory.md`

For every screen, include:

- screen name
- purpose
- entry points
- data shown
- primary user actions
- secondary user actions
- validation rules
- empty, loading, error, and success states
- permission states
- responsive behavior
- accessibility notes
- token-relevant layout requirements, such as content max width, sidebar width, grid behavior, and breakpoint behavior

### `ui-spec.md`

A layout-oriented screen description used to generate browser mockups.

For each priority screen, include:

- screen name and entry point
- layout sections
- visual hierarchy
- components
- copy and placeholder content
- component states: default, hover, active, disabled, error, loading, empty
- validation rules
- responsive behavior notes
- prototype-only interaction rules
- annotations needed in mockups
- explicit references to relevant layout/sizing tokens

### `component-inventory.md`

Lists reusable UI components, variants, states, reusable patterns, proposed component APIs where useful, and missing components.

Example format:

| Component | Variants | States |
|---|---|---|
| Button | Primary, Secondary, Ghost | Default, Hover, Disabled, Loading |
| Input | Text, Select, Textarea | Default, Focus, Error, Disabled |
| Card | Default, Highlighted | Default, Selected |
| Badge | Status, Count | Success, Warning, Error, Info |

Each reusable component should identify the tokens it depends on for color, spacing, type, radius, and size.

### `states-and-edge-cases.md`

Defines:

- global app states
- per-screen states
- validation failures
- network failures
- permission failures
- destructive-action confirmations
- success flows
- optimistic update failures
- offline or degraded-mode behavior, when relevant
- which representative states should appear in `mockups/states.html`

### `accessibility-notes.md`

Defines requirements for:

- contrast targets
- semantic HTML
- ARIA needs for prototype-only interactions
- keyboard navigation
- focus order
- visible focus indicators
- screen reader labels for icon-only buttons
- error announcement behavior
- reduced-motion expectations

### `tokens.json`

`tokens.json` is the single source of truth for visual primitives and semantic visual decisions.

It must define, at minimum:

- color tokens
- typography tokens
- spacing scale
- sizing and layout tokens
- radius scale
- shadow or elevation scale
- breakpoint tokens
- semantic tokens

#### Normative token rules

- Mockups must consume tokens through CSS variables.
- Do not restate a token value as an unrelated literal in CSS, HTML inline styles, JS style mutations, or SVG attributes.
- Do not override a token's intent with local CSS that contradicts the token name or documented behavior.
- Every sizing or layout token must state behavior, not only value.
- Behavior must be explicit: `fixed`, `min`, `max`, `grow`, `fluid`, or `clamp`.
- Width, max-width, min-width, height, spacing, radius, type size, line height, shadows, and breakpoints must be traceable to tokens or documented as intentional exceptions.
- Intentional exceptions must be listed in `mockups/consistency-check.md` and `mockups/README.md`.

#### Recommended token shape

```json
{
  "color": {
    "primary": {
      "value": "#2563EB",
      "role": "brand action color"
    },
    "surface": {
      "value": "#F8FAFC",
      "role": "page background"
    },
    "textPrimary": {
      "value": "#0F172A",
      "role": "primary readable text"
    }
  },
  "spacing": {
    "sm": {
      "value": "8px",
      "behavior": "fixed",
      "description": "Small fixed spacing unit."
    },
    "md": {
      "value": "16px",
      "behavior": "fixed",
      "description": "Default fixed spacing unit."
    }
  },
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
    },
    "mainContent": {
      "value": "1fr",
      "behavior": "grow",
      "description": "Main content expands after fixed sidebar is allocated."
    }
  },
  "radius": {
    "button": {
      "value": "6px",
      "behavior": "fixed"
    },
    "card": {
      "value": "12px",
      "behavior": "fixed"
    }
  },
  "breakpoint": {
    "md": {
      "value": "768px",
      "behavior": "min",
      "description": "Tablet and larger layouts."
    },
    "lg": {
      "value": "1024px",
      "behavior": "min",
      "description": "Desktop layout threshold."
    }
  }
}
```

### `design-package-self-review.md`

Mandatory review produced by the generating agent after creating the design package and before mockup generation.

It should include:

- reviewed files
- consistency issues found
- missing screens, flows, states, components, or tokens
- contradictory requirements
- token traceability issues
- sizing/layout behavior issues
- accessibility gaps
- responsive behavior gaps
- revisions applied
- remaining risks

This file should not be a vague approval note. It should be a literal cross-file consistency report.

### `design-package-fresh-context-review.md`

Optional but strongly recommended for multi-screen or non-trivial packages.

This review should be performed by another agent or a stronger model that did not generate the original package. It should be read-only until its findings are returned.

It should include:

- consistency findings
- coverage findings
- clarity findings
- token and sizing behavior findings
- contradictions between artifacts
- UX risks
- accessibility risks
- required revisions before mockup generation

If this step is skipped, record the skip in `mockups/README.md` or the workflow summary.

### `production-ui-handoff-notes.md`

Defines what production UI implementation should know after design mockups stabilize:

- recommended production UI build order
- reusable components to build first
- routing implications
- state/data dependencies
- accessibility requirements
- testing recommendations
- known risks
- intentionally deferred items

This file is not a production implementation plan until the project explicitly moves to production UI code generation.

### `open-questions.md`

Lists only genuine ambiguities.

Rules:

- Do not invent product behavior to avoid asking a question.
- Mark each question as blocking or non-blocking.
- Mark whether the question affects design package generation, mockup generation, or production UI implementation.

## Browser mockup artifacts

### `/design/mockups/index.html`

Primary browser entry point. It should link to all priority screens and to `states.html`.

### `/design/mockups/styles.css`

Primary mockup stylesheet.

Requirements:

- define CSS variables from `tokens.json`
- consume those variables throughout mockup CSS
- avoid arbitrary token-equivalent literals
- document unavoidable exceptions in `consistency-check.md`
- keep class names mapped to components and screen sections

### `/design/mockups/app.js`

Optional prototype-only JavaScript.

Use it only for:

- tab switching
- modal open/close
- menu toggles
- state toggles
- simple validation demonstrations
- interaction review

Do not treat it as production application logic.

### `/design/mockups/states.html`

Mandatory consolidated state gallery for non-trivial mockups.

It should show representative screens and components in:

- empty state
- loading state
- error state
- success state
- validation error state
- permission denied state
- disabled state
- destructive confirmation state
- optimistic update failure state, when relevant

### `/design/mockups/consistency-check.md`

Mandatory after mockup generation.

It should cross-check:

- CSS variables against `tokens.json`
- literal colors, spacing, widths, heights, radii, shadows, type sizes, line heights, and breakpoints
- layout behavior against token behavior: fixed / min / max / grow / fluid / clamp
- screen coverage against `screen-inventory.md`
- state coverage against `states-and-edge-cases.md`
- component coverage against `component-inventory.md`
- contradictions between mockups and design artifacts
- intentional exceptions
- revisions applied

### `/design/mockups/README.md`

Should include:

- how to preview the mockups locally
- file map
- supported interactions
- known limitations
- token exceptions
- state coverage summary
- whether fresh-context review was run or skipped

## Optional SVG artifacts

SVG files are optional quick first-look artifacts. They are not production assets.

If generated, include:

- `/design/svg/index.html`
- one SVG file per screen or priority view
- `/design/svg/svg-generation-notes.md`
- `/design/svg/svg-consistency-check.md`

SVGs must still trace layout-affecting values to `tokens.json` or document exceptions.

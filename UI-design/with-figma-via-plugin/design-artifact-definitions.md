# Design Artifact Definitions

This reference defines the design artifacts used across the agentic design workflows. These artifacts sit between product/functional specifications and production UI implementation.

## Recommended `/design` structure

Core artifacts:

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
  implementation-brief.md
  open-questions.md
```

Design-stage visual artifacts:

```txt
/design
  svg-model.json
  svg-generation-notes.md

/design/mockups
  index.html
  *.svg

/design/html-to-figma
  index.html
  styles.css
  README.md
  /screens
    *.html
```

Optional advanced Figma generation artifacts:

```txt
/design
  figma-model.json
  figma-generation-notes.md

/tools/figma-generator
  manifest.json
  code.ts
  package.json
  tsconfig.json
  README.md
```

Claude Design and downstream handoff artifacts:

```txt
Claude Design session/canvas
Claude Design handoff bundle
Standalone HTML export
ZIP export
PDF export
PPTX export
Canva export
Internal share URL
Figma frames captured through html.to.design
Cleaned Figma components, variables, annotations, and developer notes
```

## Artifact definitions

### Product brief

Describes:

- product summary
- core user roles
- primary jobs-to-be-done
- key workflows
- constraints and assumptions

### UX principles

Defines:

- UX principles inferred from the product domain
- interaction principles
- accessibility principles
- what the interface should optimize for
- behaviors the UI should avoid

### Visual direction

Defines:

- proposed visual personality
- layout density
- typography direction
- color direction
- motion and interaction direction
- what the UI should avoid visually

### Information architecture / sitemap

Defines all screens, pages, routes, navigation groups, and relationships.

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

### User flows / task flows

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

### Screen inventory

For every screen, include:

- screen name
- purpose
- entry points
- data shown
- user actions
- validation rules
- empty, loading, error, and success states
- responsive behavior
- accessibility notes

### UI spec / screen spec

A layout-oriented screen description. This is the closest text-based equivalent of a Figma annotation layer.

For each screen, include:

- screen name and entry point
- sections and their components
- copy and placeholder text
- component states: default, hover, active, disabled, error, loading, empty
- validation rules
- responsive behavior notes
- interaction rules

### Component inventory

Lists reusable UI components, variants, states, reusable patterns, proposed component APIs where useful, and missing components.

Example format:

| Component | Variants | States |
|---|---|---|
| Button | Primary, Secondary, Ghost | Default, Hover, Disabled, Loading |
| Input | Text, Select, Textarea | Default, Focus, Error, Disabled |
| Card | Default, Highlighted | Default, Selected |
| Badge | Status, Count | Success, Warning, Error, Info |

### States and edge cases

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

### Accessibility notes

Define requirements for:

- WCAG AA or AAA contrast targets
- semantic HTML requirements
- ARIA roles for non-semantic elements
- keyboard navigation
- focus order
- visible focus indicators
- screen reader labels for icon-only buttons
- error announcement behavior
- reduced-motion expectations

### Design tokens

Machine-readable visual primitives and semantic tokens. Include at minimum:

- color tokens
- typography tokens
- spacing scale
- radius scale
- shadow/elevation scale
- breakpoint tokens
- semantic tokens

Example shape:

```json
{
  "color": {
    "primary": { "value": "#2563EB" },
    "surface": { "value": "#F8FAFC" },
    "text-primary": { "value": "#0F172A" }
  },
  "spacing": {
    "sm": { "value": "8px" },
    "md": { "value": "16px" },
    "lg": { "value": "24px" }
  },
  "radius": {
    "card": { "value": "12px" },
    "button": { "value": "6px" }
  }
}
```

If tokens already live in the codebase, such as Tailwind config, CSS variables, or an existing `tokens.json`, point the design tool to the existing source rather than inventing a second system.

### Implementation brief

A planning artifact for **production UI implementation**. It should not describe mockup generation as implementation.

Include:

- recommended production UI build order
- reusable components to build first
- routing implications
- state and data dependencies
- accessibility requirements
- testing recommendations
- browser verification requirements
- known design gaps that may block production UI work

### Open questions

List only genuine ambiguities. Do not invent product behavior.

Good open questions:

- A user role appears in one spec but not in another.
- A destructive action is specified without confirmation behavior.
- A screen requires data but no empty state is specified.
- A visual token cannot be inferred from existing brand or product material.

Poor open questions:

- Questions that can be answered directly from the specs.
- New product ideas not implied by the specs.
- Preferences that do not block design or production UI implementation.

## Visual and Figma handoff artifacts

### SVG model

A structured JSON model used to generate deterministic presentation-only SVG mockups.

Include:

- screens
- viewport sizes
- layout regions
- components
- placeholder data
- states
- spacing
- typography
- color tokens
- annotations
- responsive variants

### SVG mockups

Presentation-only visual references. Useful for fast review, PR discussion, and comparing screens side by side.

SVG mockups are not production UI assets and should not be treated as exact implementation material.

### Static HTML/CSS mockups

Browser-viewable design-stage prototypes. Useful for:

- visual review
- responsive checks
- html.to.design import
- stakeholder walkthroughs

These files are not production app code unless deliberately rewritten or integrated according to the application's framework conventions.

### Figma model

A deterministic JSON model used by an optional local Figma plugin to create native Figma frames.

Include:

- pages
- frames
- auto-layout settings
- text styles
- color styles
- components and component instances
- form controls
- lists, tables, cards
- state frames
- responsive variants
- layer names
- implementation annotations

### Figma generation notes

Explain:

- intended Figma page structure
- known limitations
- manual cleanup expected after plugin generation
- where token mapping may need manual correction

### Claude Design handoff bundle

A Claude Design export intended for Claude Code. It may include component structure, design tokens used on the canvas, layout hierarchy, and referenced assets.

This is a production UI implementation handoff artifact, not a Figma artifact.

### Standalone HTML export

A self-contained HTML export from Claude Design or a chat-generated prototype. It can be opened in a browser and captured into Figma with `html.to.design`.

### Cleaned Figma frames

Figma frames that have been manually reviewed and corrected after import or generation.

A Figma frame should only become the visual source of truth for production UI implementation after:

- layer structure is understandable
- repeated UI is promoted into components where useful
- typography, spacing, color, and radius are cleaned up
- variables or token bindings are applied where practical
- stakeholders approve the relevant screen or flow

## Prompt: generate the design package

Use this with a repo agent such as Codex or Claude Code before mockup generation.

```txt
Read AGENTS.md and all markdown files under /specs.

Create a design package in /design.

The app has complete functional specs but no visual specs and no design system.

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

3. /design/visual-direction.md
   - proposed visual personality
   - layout density
   - typography direction
   - color direction
   - motion/interaction direction
   - what the UI should avoid

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
   - responsive behavior
   - accessibility notes

7. /design/ui-spec.md
   For every important screen or flow:
   - layout sections
   - components
   - copy and placeholder text
   - component states
   - interaction rules
   - responsive behavior notes

8. /design/component-inventory.md
   - required UI components
   - reusable patterns
   - proposed component API where useful
   - missing components

9. /design/states-and-edge-cases.md
   - global app states
   - per-screen states
   - validation failures
   - network failures
   - permission failures
   - destructive-action confirmations

10. /design/accessibility-notes.md
    - contrast requirements
    - keyboard navigation
    - focus behavior
    - semantic HTML expectations
    - ARIA and screen reader labels

11. /design/tokens.json
    Include:
    - color tokens
    - typography tokens
    - spacing scale
    - radius scale
    - shadow/elevation scale
    - breakpoint tokens
    - semantic tokens

12. /design/implementation-brief.md
    This is for production UI implementation planning only. Include:
    - recommended production UI build order
    - reusable components to build first
    - routing implications
    - state/data dependencies
    - accessibility requirements
    - testing recommendations

13. /design/open-questions.md
    List only genuine ambiguities. Do not invent product behavior.

Do not create Figma files.
Do not use Figma MCP.
Do not generate production app UI code yet.
```

Expected result:

```txt
/design/product-brief.md
/design/ux-principles.md
/design/visual-direction.md
/design/information-architecture.md
/design/user-flows.md
/design/screen-inventory.md
/design/ui-spec.md
/design/component-inventory.md
/design/states-and-edge-cases.md
/design/accessibility-notes.md
/design/tokens.json
/design/implementation-brief.md
/design/open-questions.md
```

## Recommended artifact preparation checklist

Before starting a new design workflow, verify you have:

- [ ] PRD or product summary
- [ ] Functional spec
- [ ] Information architecture / sitemap
- [ ] User flow for the target task
- [ ] UI spec for the target screen or flow
- [ ] Component inventory
- [ ] Design tokens or existing visual system references
- [ ] Accessibility notes
- [ ] Open questions list

You do not need all of these for every session. A UI spec plus design tokens is often enough for a single-screen mockup. The fuller the set, the less post-generation cleanup is needed.

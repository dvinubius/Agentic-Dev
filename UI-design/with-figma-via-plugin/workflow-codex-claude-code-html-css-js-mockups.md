# Workflow: Codex / Claude Code Based HTML/CSS/JS Mockup Generation

This workflow uses a repo-aware coding agent, such as Codex or Claude Code, to generate design artifacts and design-stage visual mockups from functional specs. The agent may write HTML/CSS/JS files, but those files are mockups unless explicitly converted into production application UI code later.

## When to use this workflow

Use this path when:

- complete functional specs already exist in the repo
- there are no visual specs yet
- there is no design system yet, or the design system needs to be inferred
- the repo should remain the source of truth
- you want deterministic design artifacts in `/design`
- you want SVG or static HTML/CSS mockups for review
- you may later import static HTML/CSS into Figma with `html.to.design`
- you want to avoid or conserve Figma MCP calls

## Workflow overview

```txt
/specs/**/*.md
→ /design/* design package
→ design-stage visual outputs:
   A. SVG mockups for presentation-only review
   B. static HTML/CSS mockups for browser review and html.to.design import
   C. optional local Figma plugin model for deterministic native Figma generation
→ production UI implementation handoff
```

## Core principle

Because the app has no visual specification or design system, do not start by generating Figma screens directly.

Start by creating a design package in the repo. This package becomes the shared source of truth for:

- product structure
- user flows
- screen inventory
- UI states
- component inventory
- initial visual direction
- design tokens
- production UI implementation guidance

Figma, SVGs, HTML prototypes, and production UI should all derive from this package.

## Step 1: Generate the design package

Use the full prompt in [`design-artifact-definitions.md`](design-artifact-definitions.md).

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

## Path A: SVG presentation-only mockups

Use this when you want fast, low-cost visual review artifacts.

SVG mockups are useful for:

- reviewing layout direction
- sharing visual concepts in a PR
- comparing screens side by side
- giving production UI implementation a visual reference

SVG mockups are not useful for:

- interaction design
- editable design systems
- component variants in Figma
- production UI assets

Workflow:

```txt
/design/*
→ /design/svg-model.json
→ /design/mockups/*.svg
→ /design/mockups/index.html
→ production UI implementation handoff
```

Expected artifacts:

```txt
/design
  svg-model.json
  svg-generation-notes.md

/design/mockups
  index.html
  login.desktop.svg
  login.mobile.svg
  dashboard.desktop.svg
  dashboard.mobile.svg
  settings.desktop.svg
  settings.mobile.svg
```

Prompt: generate SVG model

```txt
Using /design/screen-inventory.md, /design/ui-spec.md, /design/component-inventory.md, and /design/tokens.json, create /design/svg-model.json.

The model should be suitable for deterministic SVG generation.

Include:
- screens
- viewport sizes
- layout regions
- components
- text content
- placeholder data
- states
- spacing
- typography
- color tokens
- annotations
- responsive variants

This is presentation-only.
Do not include interaction logic.
Do not generate production app UI code.
```

Prompt: generate SVG mockups

```txt
Generate presentation-only SVG mockups from /design/svg-model.json.

Create:
- /design/mockups/index.html
- one SVG file per screen and viewport variant
- /design/svg-generation-notes.md

Requirements:
- Use only SVG, HTML, and CSS.
- No JavaScript interactions.
- No production app UI code.
- Use /design/tokens.json for visual consistency.
- Include desktop and mobile variants where specified.
- Include key empty/loading/error/success states.
- Add screen names and variant labels.
- Make the SVGs suitable for design review and production UI implementation reference.
```

## Path B: Static HTML/CSS to Figma with html.to.design

This is the recommended Figma path when Figma MCP calls are limited.

Instead of creating a custom Figma plugin, ask the repo agent to create static HTML/CSS mockups, then import those into Figma with the existing `html.to.design` plugin.

Use this path when you want:

- editable Figma layers without using Figma MCP
- a fast path from generated visuals to Figma
- less custom tooling to maintain
- mockups that can also be opened directly in a browser

Workflow:

```txt
/design/*
→ /design/html-to-figma/*.html
→ browser preview
→ import with html.to.design
→ editable Figma frames
→ manual cleanup/refinement
→ production UI implementation handoff
```

Expected artifacts:

```txt
/design/html-to-figma
  index.html
  styles.css
  README.md
  /screens
    login.html
    dashboard.html
    settings.html
    empty-state.html
    error-state.html
```

Prompt: generate static HTML/CSS for Figma import

```txt
Read AGENTS.md and all markdown specs under /specs.

Generate a Figma-importable static HTML/CSS design prototype in /design/html-to-figma.

Use:
- /design/screen-inventory.md
- /design/ui-spec.md
- /design/component-inventory.md
- /design/tokens.json
- /design/accessibility-notes.md

Requirements:
- Create static HTML/CSS only.
- No app logic.
- No framework-specific production app code.
- No JavaScript interactions unless needed only for static navigation between pages.
- One HTML file per screen.
- Include desktop and mobile responsive layouts.
- Include representative empty, loading, error, and success states.
- Use semantic class names that map to components.
- Use CSS variables generated from /design/tokens.json.
- Make each screen suitable for import into Figma via html.to.design.
- Include /design/html-to-figma/README.md with exact import instructions.

Do not use Figma MCP.
Do not create a custom Figma plugin.
Do not generate production app UI code yet.
```

Manual Figma import steps:

```txt
1. Open Figma.
2. Install or open the html.to.design plugin.
3. Import from either:
   - pasted HTML/CSS, or
   - a locally served URL from /design/html-to-figma.
4. Import desktop and mobile variants separately if needed.
5. Review the imported layers.
6. Clean up typography, spacing, grouping, components, and naming.
7. Promote repeated UI patterns into Figma components if needed.
8. Bind tokens with Tokens Studio or Figma variables where useful.
9. Add annotations and developer notes.
```

Suggested local preview command:

```bash
cd design/html-to-figma
python3 -m http.server 4173
```

Then import screens from:

```txt
http://localhost:4173/index.html
```

or individual screen files:

```txt
http://localhost:4173/screens/dashboard.html
```

## Path C: Custom local Figma plugin, advanced option

A custom Figma plugin is not the default recommendation. Use it only when deterministic native Figma generation from a repo-owned model is required.

Use a custom plugin when you need:

- repeatable regeneration from `/design/figma-model.json`
- predictable Figma pages, frames, layer names, and annotations
- direct mapping from spec IDs to Figma layers
- custom Figma metadata
- native Figma frame/component generation without relying on HTML conversion
- full control over how design tokens map to Figma layers

Avoid a custom plugin when:

- `html.to.design` is sufficient
- you only need one round of editable mockups
- deterministic regeneration is not required
- you want to minimize maintenance
- you are still exploring visual direction

Workflow:

```txt
/design/*
→ /design/figma-model.json
→ /tools/figma-generator
→ run local plugin in Figma
→ native editable Figma frames
→ optional manual cleanup
→ production UI implementation handoff
```

Expected artifacts:

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

Prompt: generate Figma model

```txt
Using /design/screen-inventory.md, /design/ui-spec.md, /design/component-inventory.md, and /design/tokens.json, create /design/figma-model.json.

The model should be deterministic and suitable for a Figma plugin to consume.

Include:
- pages
- frames
- frame sizes
- layout direction
- auto-layout settings
- spacing
- padding
- text styles
- color styles
- semantic tokens
- components
- component instances
- text layers
- form controls
- tables/lists/cards
- empty/loading/error/success states
- responsive variants
- layer names
- annotations for production UI implementation

Also create /design/figma-generation-notes.md explaining:
- intended Figma page structure
- known limitations
- manual cleanup expected after plugin generation
```

Prompt: generate custom local Figma plugin

```txt
Create a local Figma plugin in /tools/figma-generator that reads /design/figma-model.json and creates editable Figma frames.

Generate:
- manifest.json
- code.ts
- package.json
- tsconfig.json
- README.md

Requirements:
- Create a Figma page for the generated app design.
- Create frames for each screen.
- Use auto layout where appropriate.
- Create reusable components where practical.
- Use clean, predictable layer names.
- Apply colors, typography, spacing, radius, and shadows from /design/tokens.json.
- Create desktop and mobile variants where specified.
- Create empty/loading/error/success state frames.
- Do not use raster images unless unavoidable.
- Do not use Figma MCP.
```

Manual plugin run steps:

```txt
1. Open Figma.
2. Go to Plugins → Development.
3. Choose Import plugin from manifest.
4. Select /tools/figma-generator/manifest.json.
5. Run the plugin in a blank Figma file.
6. Review and clean up generated frames.
```

## Handoff to production UI implementation

Use [`production-ui-implementation-handoff.md`](production-ui-implementation-handoff.md) once the design package and any visual references are ready.

Default source:

```txt
/design/*
```

Use exact Figma node links only after the Figma file has become more authoritative than the generated design package.

## Anti-patterns

Avoid:

- starting with Figma generation before creating `/design/*`
- calling static HTML/CSS mockups production implementation
- copying static mockup HTML directly into the app without adapting it to repo conventions
- treating SVGs as exact production assets
- using a custom Figma plugin when `html.to.design` is sufficient
- letting Figma cleanup diverge from `/design/tokens.json` without updating tokens

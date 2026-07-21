# Workflow: Claude Design

This workflow uses Claude Design for visual exploration, click-and-prompt refinement, and polished design outputs. It can feed production UI implementation later, but the design session itself is not production UI implementation.

## When to use this workflow

Use Claude Design when:

- you want interactive exploration and visual iteration
- you want click-and-prompt refinement
- manual design refinement matters
- stakeholders need polished prototypes, slides, one-pagers, or interactive experiences
- you want a handoff bundle for Claude Code
- you want editable Figma frames without Figma MCP usage

## Inputs

What you usually already have:

- PRD — describes what the product does, for whom, and why
- Functional Spec — specific behaviors, edge cases, error states, and user flows

What to feed into Claude Design:

- information architecture / sitemap
- user flows / task flows
- UI spec / screen spec
- design tokens
- component inventory
- accessibility notes
- product brief and visual direction, if available

See [`design-artifact-definitions.md`](design-artifact-definitions.md) for definitions.

## Workflow overview

```txt
PRD / functional specs
→ design artifacts
→ Claude Design generation and refinement
→ one of:
   A. handoff bundle for production UI implementation in Claude Code
   B. standalone HTML export → html.to.design → Figma cleanup
   C. Canva / PDF / PPTX / internal share URL for review
```

## Step 1: Generate and refine in Claude Design

Open Claude Design and provide the relevant design artifacts.

Refine through:

- chat instructions
- inline comments on elements
- direct text edits on the canvas
- generated adjustment controls for variables like spacing, radius, or density

Keep core decisions synchronized back into the design artifacts, especially:

- `ui-spec.md`
- `component-inventory.md`
- `tokens.json`
- `states-and-edge-cases.md`
- `accessibility-notes.md`

## Path A: Claude Design → Claude Code handoff bundle

Use this when production UI code is the next goal and Figma is not required.

```txt
Claude Design canvas
→ handoff bundle
→ Claude Code production UI implementation
→ browser validation
```

When satisfied, export the handoff bundle. The bundle may include:

- component structure as a machine-readable spec
- design tokens used on the canvas
- layout hierarchy
- referenced assets

Pass the bundle to Claude Code and generate production UI code according to the application framework and repo conventions.

Use [`production-ui-implementation-handoff.md`](production-ui-implementation-handoff.md) for the production UI implementation prompt.

## Path B: Claude Design → Figma via HTML export and html.to.design

Use this when the team needs editable, annotatable Figma files without Figma MCP calls.

```txt
Claude Design canvas
→ standalone HTML export
→ browser verification
→ html.to.design capture
→ Figma cleanup
→ optional production UI implementation from refined Figma node links
```

Steps:

1. Export standalone HTML or ZIP from Claude Design.
2. Open the exported HTML in Chrome.
3. Verify the design renders correctly.
4. Capture the page into Figma with `html.to.design`.
5. Clean up the imported frames.

After import:

- Apply design system components where the plugin created raw shapes.
- Bind token variables to color and spacing fills.
- Set up auto-layout on frames that need responsive behavior.
- Add annotations and developer notes.

Helpful Figma cleanup tools:

| Tool | Purpose |
|---|---|
| html.to.design | Convert HTML pages or live URLs into editable Figma layers |
| Tokens Studio | Import/export design tokens JSON; sync with codebase |
| Figma Variables | Bind colors and spacing to library variables |
| Batch Styler | Bulk-apply text and color styles after import |
| Anima | HTML/code to Figma; may help with alternative import workflows |

## Path C: Claude Design → Canva / PDF / PPTX / share URL

Use this for non-production design review, marketing assets, one-pagers, decks, and stakeholder communication.

```txt
Claude Design canvas
→ Canva / PDF / PPTX / internal share URL
→ stakeholder review
```

Use Canva when:

- the team uses Canva for marketing or presentation work
- the output is not a functional application UI
- Figma component-linking is not required

## Export options reference

| Export format | Best for |
|---|---|
| Handoff bundle | Production UI implementation in Claude Code |
| Standalone HTML | Figma import via html.to.design |
| ZIP folder | Archiving or custom processing |
| PDF | Stakeholder review or static sign-off |
| PPTX | Presenting designs in slide form |
| Canva | Marketing assets and non-engineering stakeholders |
| Internal share URL | View/comment/edit sharing within an organization |

## Decision guide

```txt
Start: Design is ready in Claude Design
         │
         ├─► Do you need production UI code directly?
         │         YES → handoff bundle → Claude Code
         │
         ├─► Do you need editable Figma frames?
         │         YES → HTML export → html.to.design → Figma cleanup
         │
         └─► Is the output a non-UI deliverable?
                   YES → Canva / PDF / PPTX / share URL
```

## Anti-patterns

Avoid:

- treating a Claude Design visual exploration as production UI implementation
- skipping textual artifacts and relying only on a canvas
- treating raw HTML export as production app code
- treating imported Figma layers as final before manual cleanup
- letting visual exploration invent behavior that contradicts functional specs

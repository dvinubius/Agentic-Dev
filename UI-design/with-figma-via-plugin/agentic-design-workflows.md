# Agentic Design Workflows

Agentic design can be done in multiple ways using different tools. This guide is the short routing document. Detailed artifact definitions and workflow instructions live in separate files so the structure is readable.

## Terminology

In this guide, **implementation** means generating or changing production application UI code: framework components, routes, pages, styles, tests, accessibility behavior, and browser-verified user flows.

Do **not** use implementation to describe design-stage prototype or mockup creation. During the design stage, use these terms instead:

- **design artifact generation** — creating product/design documents such as screen inventories, UI specs, design tokens, and component inventories
- **mockup generation** — creating SVG, static HTML/CSS, or visual prototypes for design review
- **prototype generation** — creating non-production HTML/CSS/JS for review, iteration, or Figma import
- **Figma import/refinement** — converting mockups into editable Figma layers and manually cleaning them up
- **production UI implementation** — generating the real application UI code after design artifacts or approved Figma frames are ready

This distinction matters: HTML/CSS/JS mockups can look like code, but in these workflows they are design deliverables unless they are explicitly integrated into the application codebase as production UI.

## Decision questions

Use these questions to pick a workflow:

- Are editable Figma deliverables required and expected to be improved manually?
- Should the design be interactive, presentation-only, or a static visual reference?
- Do we want to iterate in a focused click-and-prompt canvas with an agent?
- Do we have complete functional specifications for the app?
- Is the best source of truth the repo, Claude Design, manually refined Figma screens, or a combination?
- Is the next step design exploration, mockup generation, Figma refinement, or production UI implementation?

## Complete functional specs available

When complete specs exist, the safest workflow is to create text-based design artifacts before generating visuals or production UI code.

Recommended sequence:

```txt
Functional specs / PRD
→ design artifacts
→ mockups or Claude Design exploration
→ optional Figma import and manual refinement
→ production UI implementation from design artifacts first
→ exact Figma node links only after Figma is refined and approved
```

## Shared source-of-truth model

For repo-centered projects, keep design artifacts in `/design`. Treat functional specs as canonical for behavior and `/design` as canonical for design structure, states, and visual system decisions.

Rules:

- Functional specs live in `/specs/**/*.md` or equivalent PRD/spec locations.
- Generated design artifacts live in `/design`.
- Treat `/specs` as canonical for product behavior.
- Treat `/design/tokens.json` as canonical for visual system decisions once generated.
- Do not invent product behavior that is not in the specs.
- Do not invent visual rules after `/design/tokens.json` exists; update the token file instead.
- Figma, SVGs, HTML mockups, and production UI should derive from the design package.

## Reference files

Read these files in order:

1. [`design-artifact-definitions.md`](design-artifact-definitions.md) — artifact definitions, recommended `/design` structure, design package prompt, and checklist.
2. [`workflow-chatgpt-claude-html-css-js-mockups.md`](workflow-chatgpt-claude-html-css-js-mockups.md) — direct chat-based static prototype/mockup generation and Figma import.
3. [`workflow-claude-design.md`](workflow-claude-design.md) — Claude Design exploration, handoff bundle, Figma export, Canva/PDF/PPTX exports.
4. [`workflow-codex-claude-code-html-css-js-mockups.md`](workflow-codex-claude-code-html-css-js-mockups.md) — repo-centered Codex/Claude Code generation of `/design`, SVG mockups, static HTML/CSS mockups, and optional Figma plugin model.
5. [`production-ui-implementation-handoff.md`](production-ui-implementation-handoff.md) — production UI implementation definition, source-of-truth rules, and handoff prompts.

## Workflow overview

### ChatGPT / Claude Chat based HTML/CSS/JS mockup generation

Use when specs are detailed enough and you want fast, low-cost prototype generation without opening Claude Design.

```txt
PRD / functional specs
→ design artifacts
→ static HTML/CSS/JS prototype for review
→ browser preview
→ optional html.to.design import
→ optional manual Figma cleanup
→ production UI implementation handoff
```

Detailed guide: [`workflow-chatgpt-claude-html-css-js-mockups.md`](workflow-chatgpt-claude-html-css-js-mockups.md)

### Claude Design

Use when visual exploration, click-and-prompt iteration, stakeholder-facing prototypes, or polished design outputs are important.

```txt
PRD / functional specs
→ design artifacts
→ Claude Design generation and refinement
→ one of:
   A. handoff bundle for production UI implementation in Claude Code
   B. standalone HTML export → html.to.design → Figma cleanup
   C. Canva / PDF / PPTX / internal share URL for review
```

Detailed guide: [`workflow-claude-design.md`](workflow-claude-design.md)

### Codex / Claude Code based HTML/CSS/JS mockup generation

Use when the repo is the center of gravity and the agent should generate a structured `/design` package before creating visual mockups.

```txt
/specs/**/*.md
→ /design/* design package
→ one or more design-stage outputs:
   A. SVG mockups for presentation-only review
   B. static HTML/CSS mockups for browser review and html.to.design import
   C. optional deterministic Figma model/plugin artifacts
→ production UI implementation handoff
```

Detailed guide: [`workflow-codex-claude-code-html-css-js-mockups.md`](workflow-codex-claude-code-html-css-js-mockups.md)

## Choosing the right path

| Situation | Recommended workflow | Design-stage output | Production UI implementation source |
|---|---|---|---|
| Fast visual review | Codex / Claude Code mockup generation | SVG or static HTML/CSS mockups | `/design/*` |
| Editable Figma without MCP | ChatGPT/Claude Chat or Codex static HTML/CSS | HTML imported through `html.to.design` | `/design/*` until Figma is refined |
| Visual exploration | Claude Design | interactive Claude Design canvas | handoff bundle, `/design/*`, or refined Figma node links |
| Stakeholder-reviewed Figma screens | Claude Design or HTML/CSS → Figma | cleaned Figma frames | exact Figma node links plus `/design/*` |
| Repeatable native Figma generation | Codex / Claude Code advanced path | `figma-model.json` + local plugin | refined Figma node links or `/design/*` |
| No Figma needed | ChatGPT/Claude Chat or Codex | browser-viewable static mockups | `/design/*` |

## Recommended default for this project shape

Given complete functional specs, no visual specs, no design system, limited Figma MCP calls, and access to `html.to.design`, use this sequence:

```txt
1. Generate /design/* from /specs/**/*.md.
2. Generate fast visual review mockups: SVG and/or static HTML/CSS.
3. Import static HTML/CSS into Figma only if editable Figma is useful.
4. Manually clean up high-value Figma screens.
5. Start production UI implementation from /design/*.
6. Use exact Figma node links later only for refined and approved screens.
```

Default production UI implementation source:

```txt
/design/*
```

Use exact Figma node links only after the Figma file has become more authoritative than the generated design package.

## Suggested repo-level `AGENTS.md` addition

```md
## Product and design source of truth

- Functional specs live in /specs/**/*.md.
- Generated design artifacts live in /design.
- Treat /specs as canonical for behavior.
- Treat /design/tokens.json as canonical for visual system decisions once generated.
- Do not invent product behavior that is not in /specs.
- Do not invent visual rules after /design/tokens.json exists; update the token file instead.

## Design workflow

Before production UI implementation:
1. Generate or update /design/product-brief.md.
2. Generate or update /design/ux-principles.md.
3. Generate or update /design/visual-direction.md.
4. Generate or update /design/information-architecture.md.
5. Generate or update /design/user-flows.md.
6. Generate or update /design/screen-inventory.md.
7. Generate or update /design/ui-spec.md.
8. Generate or update /design/component-inventory.md.
9. Generate or update /design/states-and-edge-cases.md.
10. Generate or update /design/accessibility-notes.md.
11. Generate or update /design/tokens.json.
12. Generate one or more design-stage visual outputs:
    - /design/mockups/*.svg for presentation-only review, or
    - /design/html-to-figma/* for editable Figma import through html.to.design, or
    - /design/figma-model.json for advanced native Figma plugin generation, or
    - a Claude Design handoff/export if using Claude Design.

## Production UI implementation workflow

- Use /specs for behavior.
- Use /design for structure, states, and visual system.
- Use refined Figma node links only after Figma screens are reviewed and approved.
- Reuse existing repo conventions.
- Create a minimal design system only if none exists.
- Implement reusable components before screens.
- Verify responsive, empty, loading, error, and success states.
- Ensure keyboard and screen-reader accessibility.
```

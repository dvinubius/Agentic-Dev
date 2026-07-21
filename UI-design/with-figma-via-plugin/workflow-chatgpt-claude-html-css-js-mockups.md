# Workflow: ChatGPT / Claude Chat Based HTML/CSS/JS Mockup Generation

This workflow uses a chat assistant to generate static HTML/CSS/JS prototypes from written design artifacts. It is a design workflow, not a production UI implementation workflow.

## When to use this workflow

Use this path when:

- you want to skip Claude Design and generate directly from specs
- specs are detailed and structured enough for direct mockup generation
- you want quick iteration in a chat session
- you want zero Figma MCP calls
- you need multiple screens generated in parallel across separate chats
- you want more control over HTML output than a visual design agent provides

## Output

Primary output:

```txt
Static HTML/CSS/JS prototype for design review
```

Optional output:

```txt
Editable Figma frames imported through html.to.design
```

Not output:

```txt
Production application UI code
```

## Workflow

```txt
PRD / functional specs
→ design artifacts
→ static HTML/CSS/JS prototype
→ browser preview
→ optional html.to.design import
→ optional Figma cleanup
→ production UI implementation handoff
```

## Step 1: Prepare or reference the artifacts

Use the shared artifacts in [`design-artifact-definitions.md`](design-artifact-definitions.md).

For a single-screen generation, the minimum useful set is:

- UI spec for the target screen
- user flow for the task
- component inventory
- design tokens
- accessibility notes

The fuller the artifact set, the less cleanup the generated mockup will need.

## Step 2: Generate the static prototype

Prompt:

```txt
Using the UI spec, component inventory, user flow, design tokens, and accessibility notes below, generate a styled static HTML/CSS prototype for the target screen or flow.

Requirements:
- Use static HTML and CSS.
- Use JavaScript only for prototype-only navigation or state toggles.
- Do not generate production app UI code.
- Do not use framework-specific application code.
- Use semantic class names that map to components.
- Use CSS variables generated from the design tokens.
- Include representative default, hover, disabled, loading, empty, error, and success states.
- Include desktop and mobile responsive behavior.
- Make the HTML suitable for browser preview and Figma import through html.to.design.
```

## Step 3: Iterate in chat

Refine the prototype through follow-up messages.

Good iteration targets:

- layout hierarchy
- density
- copy
- component states
- responsive behavior
- contrast
- navigation between static screens
- empty, loading, error, and success states

Keep important changes flowing back into the textual artifacts. Do not let an untracked one-off HTML file become the only description of the design.

## Step 4: Preview in browser

Save the HTML locally and open it in Chrome or another target browser.

Verify:

- visual hierarchy
- responsive behavior
- text sizing
- state coverage
- keyboard focus visibility
- basic semantic structure
- obvious accessibility failures

## Step 5: Import into Figma with html.to.design

Use `html.to.design` to capture the local page or a locally served URL as editable Figma layers.

After import:

- Review grouping and layer names.
- Convert repeated raw shapes into Figma components where useful.
- Bind colors and spacing to tokens or Figma variables.
- Set up auto-layout for frames that need responsive behavior.
- Add annotations and developer notes.

## Suggested local preview command

If the prototype is split across multiple files:

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

## Handoff to production UI implementation

Before Figma is cleaned up, treat the generated static HTML/CSS/JS as a visual reference only. Use `/design/*` as the source of truth for production UI implementation.

After Figma screens are manually cleaned up and approved, exact Figma node links may become the visual source of truth.

Use the prompts in [`production-ui-implementation-handoff.md`](production-ui-implementation-handoff.md).

## Anti-patterns

Avoid:

- calling static prototype generation "implementation"
- copying generated prototype HTML directly into the app without adapting it to repo conventions
- treating rough html.to.design layers as final Figma design system components
- letting chat-generated mockup details override specs or design tokens silently
- skipping empty, loading, error, success, and responsive states

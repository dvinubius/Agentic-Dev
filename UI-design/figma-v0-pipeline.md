# Figma-v0 pipeline

Figma Make (Claude-based) generates interactive React components.

Vercel’s v0 takes those components and refines them.

## Workflow

A designer opens Figma Make. They describe a component in natural language, or they select existing design elements and ask the tool to generate code from them. The tool reads the design tokens, the spacing, the typography, the color system, and produces React components that reflect the design system correctly. Not approximately. Correctly.

The output goes into v0 for refinement. The engineer can now add interactivity, wire up state, connect to an API. Or the designer can. The tools have made the purely technical parts of frontend work accessible to anyone who understands what they want the component to do.

What is left for the frontend engineer in this loop is narrower than it used to be. The judgment calls that require understanding how a component will behave at scale, what accessibility requirements the AI consistently gets wrong, how the state management will interact with the rest of the application. Genuine expertise still matters. It matters in a smaller portion of the work than it did eighteen months ago.


## Shortfalls

The pipline
- cannot make architectural decisions about how a component will scale when ten thousand users are using it simultaneously. 
- cannot identify the accessibility failures that 95.9% of AI-generated UIs contain, according to WebAIM’s 2026 analysis.
- cannot understand the history of a codebase well enough to know why a particular design pattern was chosen two years ago and what breaks if you change it.
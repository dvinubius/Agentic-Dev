# Concept - Work in Progress

This is not part of the methodology, but a dump of ideas to be incorporated.


## Basic Assumptions

Shimeles works based on a staging -> feature branch -> PR into staging workflow.

Staging PR into main is a separate workflow.

Use frontier models, accept high token usage.

Work in small increments. Use planning before starting a task and / or within a task. Around a task: task sequence planning; inside a task: technical planning.

Each task (feature / refactor / fix) creates a PR.

PRs are the reviewable end result (not the diffs pre-commit).

Rely on the agent to do everything, including the review.

Code beats docs: for dependencies rely on source code not the docs. Assume agent is powerful & smart enough.

## Shimeles Elements

`AGENTS.md` describes the workflows.

Skills:
- `code-structure` for service layer
- greptile, greploop

Code beats docs:
- npx opnesrc - local source code for deps, so that agent looks at the actual code



## Lean Integration

### Clean Code

Use neat-code by default. Only add code-structure if it makes sense for the project.

- Explicit instruction: Search the existing code before creating new abstractions.
- Explicit test: run `neat-code` -> this must be scoped to the current diff
- greptile & greploop should also be leveraging Fallow


### Separation
The files that constitute the methodology (giving the agent instructions) should not be mixed up with project files. I need to be able to remove the entire methodology at any point and not have project code or docs or specs be affected in any way by that.

### Context Routing
I want to have it in a similar fashion here, as I have it in Lean-Methodology.

### The structure of the scaffold
What's inside the scaffold would typically be pasted into the root of a repo.

- AGENTS.md, CLAUDE.md and CONTEXT.md (if present) live at the root
- an `.agent/` directory holds the rest: instructions on docs, specs, skills and a how-to for the dev
- `.agent/skills` should include the skills from [skills](../../../Shimeles-Methodology/scaffold/skills/) , but not the workflow skill (see below)
- I want to have the `.agent/specs/` part pretty much as it is in Lean-Methodology (and associated skills should be included)


### Config
No need for `.agent/config.properties`

### Codegraph
No need to mention codegraph, like in Lean-Methodology. The agent should pick up on it on its own, or the dev will explicitly ask the agent to use codegraph

the instructions to the dev should be in `scaffold/agent`

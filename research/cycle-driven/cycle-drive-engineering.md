# Cycle Driven Engineering

**Types of Work**
- investigation
- planning
- execution

=> any non-trivial feature work requires at least 3 sessions

This distinction is important when it comes to assembling the context for any given task.


## Context Layer

```text
Knowledge -> Classification -> Discovery -> Selection -> Task context
```

### Docs

See as [**image**](repo-docs.png)

**STRUCTURE**
- **System Overview**
  - purpose, boundaries, major components, dependencies and technology stack
  - technical concepts
    - how CQRS is applied
    - how asynchronous processing works
    - how services communicate
- **Architecture**
  - how and why the system was built like this
  - overlap with system overview: 
    - overview provides the map
    - architecture explains the structures and decisions behind it
- **Features**
  - For each feature, document
    - how it is expected to work
    - relevant technical implementation
  - Covers business rules, important scenarios, state transitions, integrations, affected components and feature-specific constraints. 

Machine readable **Diagrams** (Mermaid) should exist at each level.

**Contrast to SDD**
An engineer or agent working on a feature should not need to reconstruct its intended behaviour from controllers, database tables, tests and old tickets.

```text
docs/
├── README.md                          # routing
│
├── systemOverview/
│   ├── README.md                      # routing
│   ├── purpose & boundaries
│   ├── major components
│   ├── dependencies
│   ├── technology stack
│   └── technical concepts
│
├── architecture/
│   ├── README.md                      # routing
│   ├── component interactions
│   ├── data flows
│   ├── deployment
│   ├── cross-cutting patterns
│   └── ADRs
│
└── features/
    ├── README.md                      # routing
    │
    ├── feature-a/
    │   ├── domain behaviour
    │   ├── technical implementation
    │   ├── integrations
    │   └── constraints
    │
    └── feature-b/
        ├── domain behaviour
        ├── technical implementation
        ├── integrations
        └── constraints
```


#### Gradual Adoption

For an existing project with little or poor documentation, the goal should not be to describe the entire system upfront. 
The starting point can be a high-level system map, the most important architectural patterns and the features currently being changed or repeatedly misunderstood. The knowledge base can then grow through normal engineering work, with each task filling a real context gap rather than producing documentation for its own sake.

#### Classification

The folder structure already provides a first level of classification:
- Knowledge under systemOverview is broad and descriptive.
- Documentation under architecture explains deeper technical structures and decisions.
- Material under features is scoped to a particular area of product behaviour and its implementation. 

As the hierarchy becomes more specific, so does the context it can provide.

Important documents should state their scope, purpose and status **explicitly**.

Use a small amount of consistent metadata or a standard introductory section per document:
- the system, component or feature it applies to;
- whether it is descriptive, normative or historical;
- whether it represents a mandatory rule, an accepted decision, a recommended pattern or an example;
- whether it is active, deprecated or superseded;
- who owns it and which document replaces it when applicable.

#### Discovery

A task involving a feature may begin in `features`, then lead towards the relevant domain description, technical implementation and architectural decisions (`architecture`). A task affecting a shared technical concern may instead move from the `system overview` into `architecture`: patterns or ADRs. **Cross-links** between related areas are important because project knowledge rarely fits perfectly inside a single branch of the structure.

Discovery identifies the sources that may be relevant. It does not yet decide which of them belong in the final working context. That is the responsibility of selection.

#### Selection

Repository and path-level rules provide the mandatory baseline, while **domain-specific sub-agents** and **granular skills** narrow the available knowledge according to the feature, component or technical concern involved.

The descriptions attached to sub-agents and skills are therefore part of the selection mechanism.

Selection should also account for the phase of work:
- investigation
- planning
- execution
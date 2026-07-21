# System Definition 

Especially when Doing agentic software engineering, it's good to have a clear system definition concept.

Ideally, separate the layers of
- **intent**
- **specification**
- **implementation**

and treat **verification** as a cross-layer concept. 

For each non-trivial task that goes into developing a software system in an agentic workflow, the planning should include
- a PRD
- potentially ADRs 

as a basis for the execution & verification. 

## Layers

**Intent** = desired outcome and outcome boundaries; what would make the outcome unacceptable

**Specification** = expected observable behavior

**Implementation** = how the system will be built to satisfy the intent and spec

**Verification** is attached to each layer, not floating separately.

## PRD

Covers Intent & Specification. It may mention implementation constraints.

Typically it contains:
```md
- problem / goal        - Intent
- target users          - Intent
- product requirements  - Specs
- user flows            - Specs
- acceptance criteria   - Intent
- constraints           - Intent, usually
- non-goals             - Intent
- success metrics       - Intent / Specs - related
- verification          - Intent / Specs - related
```

Implementation Verification is too technical to be included in a PRD, and heavily depends on the stack, workflow etc.

## ADRs

Detailed architecture.

Technical discussions to justify specific choices regarding the implementation of what the PRD describes.
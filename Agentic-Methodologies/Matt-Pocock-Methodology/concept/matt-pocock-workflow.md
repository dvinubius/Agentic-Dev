# Matt Pocock Workflow

A workflow for the strategic engineer, with HITL during planning and the option to have AFT execution of issues.

Work is organized in "tasks", which correspond to issues, all under one PRD.

Typically there is 1 session for the planning and the rest of the work is done flexibly in other sessions.

Human in the loop?
- specs (idea, opt. research, opt. prototype): HITL
- planning: HITL
- Implementation: AFK
- QA / Review: HITL

Implementation may occur in parallel. 

As a strategic dev, keep the code in mind at all times, even during prd creation.


## The main flow: idea → ship

The route most work travels. You have an idea and want it built.

1. **`/grill-with-docs`** — sharpen the idea by interview. Start here when you **have a codebase**: it's stateful, retaining what it learns in `CONTEXT.md` and ADRs. (No codebase? Use `/grill-me` — see Standalone.)
2. **Branch — can you settle every question in conversation?** If a question needs a runnable answer (state, business logic, a UI you have to see), detour through a prototype, bridged by **`/handoff`** in both directions (see Crossing sessions):
   - **`/handoff`** out, then open a fresh session against that file,
   - **`/prototype`** to answer the question with throwaway code,
   - **`/handoff`** back what you learned, and reference it from the original idea thread.
3. **Branch — is this a multi-session build?**
   - **Yes** → **`/to-prd`** (turn the thread into a PRD) → **`/to-issues`** (split the PRD into independently-grabbable issues). Because the issues are independent, **clear context between each one**: start a fresh session per issue and kick off **`/implement`** by passing it the PRD and the single issue to work on.
   - **No** → **`/to-prd`** (turn the thread into a PRD) → **`/implement`** right here, in the same context window.


## Specs: clarify what needs to be done

**Idea**

/grill-with-docs  to get alignment with the AI on what this work should achieve.

**Research**
Optional. If execution would involve difficult 'explore' phases, create a research.md asset to cache them.

**Prototype**
Optional. Hash out ideas in code to get early feedback. Provide assets that can later be used in implementation.


### On Grilling
- **Handoff** out & back in for reaearch & prototyping if necessary; one reason would be that the question is too high fidelity, and you couldn't answer without mock-ups.
- Scope grilling so that a single grilling session doesn't fill up context more than 120k
- Conflicting stances on the viability of a PRD as a handoff
  - A couple months ago, Matt presented the idea that PRD is merely a summary and the rich context is what gives an agent the alignment. So work should be resumed in the grilling session
  - In a more recent video, Matt says a PRD only necessary when a handoff needs to be done at the end of a grilling session in case of context being too loaded; so a PRD actually is viable as a handoff

## Plan work in phases

Work on a branch and open a PR already.

/write-a-prd => local md file in issues/  (Matt also uses it with GH issues)

During PRD creation, approve proposed implementation changes carefully. But don't put extreme effort into making the perfect PRD. The better place for heavy human work is in QA. That's where you have higher chances of finding the right answers to very detailed questions.

PRD template:
- problem statement
- solution
- user stories
- implementation decisions
- testing decisions
- out of scope

The PRD should be just a summary of everything discussed so far. No need to review.

Next, split the work: `/prd-to-issues`

Issue_n 
  - prd.md
  - plan.md

Make sure the AI does complete vertical slices. 
Issue may be saved locally or on GH.
Issues are organized in a DAG. 

What results is a **Kanban** with individual **tickets** with blocking relationships. (order constraints become clear)

## Execution

Implementation is TDD. Feedback loops are essential in agentic development. Aim for high quality feebdack loops.

AFK.

Issues can be implemented sequentially and even in parallel, when there are multiple issues at the same depth in the DAG.

Tests and Review done by agent as part of the implementation.  This is independent of the QA and Review done by the engineer.

Can use .ralph execution. bash scripts for once and loop.

Parallelization: Sandcastle (prefer to not use for now...)

All issue work commits the changes to the same branch. 

The subsequent QA / Review of the engineer evaluates the entire PR.

## QA / Review

Create more issues for the Kanban board.

## Applying it in practice (My Take)

Put specs and broad planning in agent-ignored `.devnotes/`.
Both are optional and dev-owned.


### New repo scenario

#### Preliminary Work

A minimal spec describing the app should be created from the start. Having this allows us to
- choose a tech stack
- define a basic architecture
- create a plan with milestones, to organize future work; non-normative, just for the engineer

#### Task Zero
This should be a task which has the goal of laying an app foundation, with functionality close to 0 but with the system parts created and interconnected.
- frontend
- backend
- DB
- ...

Every subsystem implementation could be a phase of Task Zero. Interconnecting them could be the last phase of Task Zero.

#### Subsequent Tasks

Regular workflow, building on top of foundation

The broad plan with milestones can be used to determine suitable "chunks" of functionality, then one chunk becomes the starting point for a new task.

Task work fleshes out specs and updates the plan with milestones.

At some point the plan with milestones may be completed and deleted. Then the app is further built in small increments (1 task each).



## Matt's Approach (Latest) vs. 3-Layer approach

Matt’s spec = 3-layer compact system definition artifact.

**Matt’s Spec**
A broad, implementation-ready artifact describing the thing to build. It may include product behavior, technical decisions, testing decisions, and scope boundaries. A PRD is narrower and more product-centered, so “PRD” was the wrong name for that artifact. Now he calls it "spec".

**Our 3-Layer system definition**
- Intent defines the desired outcome and boundaries.
- Product Spec defines observable behavior.
- Implementation defines how the system is built.
- A PRD usually covers Intent and Product Spec, maybe with some implementation constraints.
- A broader System Definition includes all three layers, with verification attached to each layer.

| Term              | Matt Pocock                                                                        | Our conversation                                                                                                            |
| ----------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| PRD               | Product-focused document; too narrow for the mixed artifact his skill was creating | Usually includes intent + product specification; may include some implementation constraints, but not full technical design |
| Spec              | Broad build artifact; can include product, technical, and testing decisions        | We used “Product Spec” more narrowly: observable behavior of the system                                                     |
| System Definition | Not Matt’s chosen term here                                                        | Our umbrella term for Intent + Product Spec + Implementation Brief + Verification                                           |
| Tickets           | Work breakdown underneath the spec                                                 | Same; implementation slices derived from the agreed system definition                                                       |
| Wayfinder         | Pre-spec map of unresolved decisions for large/foggy work                          | Pre-system-definition discovery and decision process                                                                        |

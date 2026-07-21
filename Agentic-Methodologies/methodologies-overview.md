# Alternative Methodologies

## My Own

### Spartan

Absolutely minimal. No formal workflow, no PRD. 

Just `AGENTS.md` w/ rules & minimal routing, and local `skills/`

Designed for
- fully autonomous execution with zero engineer involvement after the initial prompt
- HITL execution with minimal agentic scaffold & max. flexibility to add complementary skills / workflows
- quick prototypes, low-stakes experiments
- doing a lot in a short time
- One-shotting an entire app

The best to combine with [`openspec`](https://github.com/Fission-AI/openspec).

Packaged variant: [3-Layer-Spartan](3-Layer-Spartan/3-layer-spartan-methodology.md) — uses 3-layer planning specs (normative `specs/`) instead of `openspec`, plus `tdd`, `deepen-modules`, `neatify-code`.

### Ultra Lean

Works with a PRD and issues derived from it. 
The engineer is always involved in planning (intent clarification, alignment, research, PRD creation)
The engineer orchestrates agents manually — one issue per session. 
A capable agent with a PRD and issues will naturally handle orchestration (sub-tasks, reviews) without explicit instructions.
Optional AFK prd execution based on skill.

### Matt Pocock

Best for serious development on larger projects. 

The planning, qa and review is HITL. 

Implementation is TDD. 

Requires much discipline and good team work when used in a team.

Includes parallelizable AFK execution of implementations. (ralph loops)


### Engineer Involvement Scenarios

**Full AFK only makes sense for full app prototypes.** For any serious, long-running project, the engineer must be involved at least in planning. One-shotting a complex feature or fix without engineer-driven planning is not appropriate for production-quality work.
 
| Scenario | Description |
|---|---|
| **Fully AFK** | No involvement after the initial prompt. Suitable only for prototypes or entire app generation. |
| **Planning & Final Review** | Engineer collaborates on planning, reviews and approves a PRD, then steps away. AI executes autonomously against the approved plan. Engineer reviews PR at the end |
| **Fully HITL** | Engineer drives the workflow throughout — creates PRD, breaks it into issues, hands each issue to an agent in a separate session, reviews output, and moves to the next. |


### Methodology Compatibility Table
 
| Scenario | Spartan | Ultra Lean | Matt Pocock |
|---|---|---|---|
| **Fully AFK** | ✅ Best fit | ⚠️ Possible with engineer waiving all reviews, risky for large PRDs | ⚠️ HITL planning & final review required |
| **Planning & Final Review** (PRD approved, then AFK) | ✅ Ad-hoc PRD or `openspec` format | ✅ Good fit (single orchestrating agent + good prompt) | ⚠️ Risky for large PRDs |
| **Human in the loop throughout** | ✅ Ideal for experiments | ✅ Great fit (engineer orchestrates per-issue sessions) | ✅ Great fit |


## Other Methodologies - In Research


### OpenSpec

See `../research/planning-at-scale.md`.

### BMAD

See `../research/workflow-tools.md`

### QRSPI

"Crispy" - see `../Agentic-Methodologies/Crispy-Methodology/concept.md`


### HAK - Agentive Stack

Similar to Matt Pocock: DDD, vertical slicing, TDD implementation, Docs.

But more simple.

Some details on the docs are not clear - needs research

https://github.com/dvinubius/agentive-skills (fork)

https://agentivestack.ai/build


## Excluded

**Shimeles**

Staging branch based.

PR Review heavy. Lots of greploop, very little human review of the code => not as sophisticated engineering wise, probably not as solid long-term for ambitious projects with complex systems.

Opinionated on "service layer" - not as easily applicable to frontends.
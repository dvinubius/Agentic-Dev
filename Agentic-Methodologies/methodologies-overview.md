# Alternative Methodologies

## My Own

### Spartan

**Status: methodology draft; not ready for use.**

Absolutely minimal. No formal workflow, no PRD. 

Just `AGENTS.md` w/ rules & minimal routing, and local `skills/`

Designed for
- fully autonomous execution with zero engineer involvement after the initial prompt
- HITL execution with minimal agentic scaffold & max. flexibility to add complementary skills / workflows
- quick prototypes, low-stakes experiments
- doing a lot in a short time
- One-shotting an entire app

The best to combine with [`openspec`](https://github.com/Fission-AI/openspec).

See the [Spartan SDD concept](Spartan-SDD/concept.md).

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
 
| Scenario | Spartan | Matt Pocock |
|---|---|---|
| **Fully AFK** | ✅ Best fit | ⚠️ HITL planning & final review required |
| **Planning & Final Review** (PRD approved, then AFK) | ✅ Ad-hoc PRD or `openspec` format | ⚠️ Risky for large PRDs |
| **Human in the loop throughout** | ✅ Ideal for experiments | ✅ Great fit |


## Other Methodologies - In Research


### OpenSpec

See `../research/planning-at-scale.md`.

### BMAD

See `../research/workflow-tools.md`

### QRSPI

"Crispy" - see [the QRSPI research notes](../research/QRSPI-Methodology/concept.md).


### HAK - Agentive Stack

Similar to Matt Pocock: DDD, vertical slicing, TDD implementation, Docs.

But more simple.

Some details on the docs are not clear - needs research

https://github.com/dvinubius/agentive-skills (fork)

https://agentivestack.ai/build

### Hodik (Irreplaceable Engineer Lab)

Low overhead, high leverage, requires good engineering judgement and HITL.

See `research/hodik-irreplaceable`


## Deprecated

**Ultra Lean**

Deprecated because it overlaps too heavily with the highly effective Matt
Pocock workflow. The methodology is retained in
[`deprecated/Ultra-Lean-Methodology/`](deprecated/Ultra-Lean-Methodology/) for
historical comparison.

## Excluded

**Shimeles**

Staging branch based.

PR Review heavy. Lots of greploop, very little human review of the code => not as sophisticated engineering wise, probably not as solid long-term for ambitious projects with complex systems.

Opinionated on "service layer" - not as easily applicable to frontends.

# Agentic Development Research

An ongoing personal research project on how AI coding agents can contribute to
reliable software development—not merely by generating code, but by fitting
into a deliberate workflow across the software development life cycle (SDLC).

The aim is to develop, test, and document practical conclusions about agentic
software development: which tools and interaction patterns work, where human
judgment remains essential, and what lightweight methodology makes work more
repeatable without turning it into bureaucracy.

This is a working research repository. It records experiments, provisional
conclusions, alternative approaches, and some obsolete paths alongside the
current work. It is shared as a portfolio of real thinking and iteration, not
as a polished framework for others to adopt unchanged.

## Research focus

The work looks at agentic development end to end:

- **Planning and specification** — turning ambiguous intent into small,
  reviewable work with an appropriate level of precision.
- **Context and agent harnesses** — repository instructions, skills, task
  state, context management, and constraints that help agents act reliably.
- **Implementation and verification** — task decomposition, implementation
  loops, tests, review, and recovery when an agent takes a wrong turn.
- **Human–agent collaboration** — deciding where a developer should steer,
  review, approve, or deliberately step away.
- **Design workflows** — connecting product and UI-design artifacts to
  implementation, with and without Figma-based workflows.
- **Tools and models** — comparing practical strengths, limitations, and
  failure modes rather than treating any model or tool as universally best.

### **The Holy Grail**

A versatile approach that fits
- greenfield & brownfield projects
- simple and complex tasks: simple without friction, complex without quality loss.
- HITL and AFK one-shot execution of larger tasks

## Current working conclusions

These are hypotheses shaped by ongoing experiments, not universal rules:

1. Full autonomy is most credible for bounded prototypes and low-stakes work.
   For durable or complex software, human involvement in planning and review
   remains a core reliability mechanism.
2. The valuable unit of work is not an open-ended chat; it is a task with
   enough explicit intent, context, and verification to be inspected and
   resumed.
3. A methodology should be proportional to the risk and scope of the change.
   Small work benefits from a lean scaffold; larger work needs clearer
   specifications, decisions, and decomposition.
4. Agent capability and the surrounding harness are inseparable. Instructions,
   artifacts, available tools, and feedback loops strongly influence outcomes.
5. Long-running agent work needs deliberate context management. Recovering
   from a compacted or restarted session should rely on repository state and
   concise task artifacts, not conversational memory alone.

The evidence and counterexamples behind these points are kept in the research
notes rather than hidden behind a single definitive claim.

## Repository guide

| Area | What it contains |
| --- | --- |
| [`research/`](research/) | Notes, comparisons, experiments, terminology, workflow observations, and takeaways. Start with [models and harnesses](research/models-and-harnesses-takeaways.md), [workflow tools](research/workflow-tools.md), and [workflow takeaways](research/workflow-TAKEAWAYS.md). |
| [`Agentic-Methodologies/`](Agentic-Methodologies/) | Evolving methodology concepts and reusable scaffolds. See the [methodologies overview](Agentic-Methodologies/methodologies-overview.md). |
| [`Agentic-Methodologies/Spartan-SDD/`](Agentic-Methodologies/Spartan-SDD/) | A newly promoted methodology draft for minimal agent guidance and specification-driven development. It is still a work in progress and is not ready for use. |
| [`Universal-Benchmark/`](Universal-Benchmark/) | Work in progress on a universal benchmark for comparing coding models across project scenarios and execution styles. |
| [`research/QRSPI-Methodology/`](research/QRSPI-Methodology/) | Research notes on the QRSPI workflow for planning and delivering complex brownfield changes. |
| [`UI-design/`](UI-design/) | Research into agentic UI and design-to-implementation workflows, including paths with and without Figma. |
| [`Agentic-Methodologies/deprecated/`](Agentic-Methodologies/deprecated/) | Earlier approaches retained for comparison and historical context. They are not current recommendations. |

## Methodology direction

The methodology work explores several levels of structure rather than a single
prescriptive process. The current direction favors **developer-steered,
proportionate workflows**: make intent explicit, give agents bounded work and
useful context, retain human decisions at consequential points, and verify the
result against the intended behavior.

The [Spartan SDD methodology](Agentic-Methodologies/Spartan-SDD/concept.md) is
the newest draft in this direction, but it is not ready for use. Ultra Lean has
been deprecated because it overlaps too heavily with the highly effective
[Matt Pocock workflow](Agentic-Methodologies/Matt-Pocock-Methodology/concept),
and is retained under `Agentic-Methodologies/deprecated/` for historical
comparison.

## How to read this repository

Read the material as an evolving lab notebook:

- Notes may be incomplete, opinionated, or superseded by later findings.
- “Deprecated” material is intentionally preserved because failed or abandoned
  approaches are useful research evidence.
- The repository prioritizes traceable reasoning and practical artifacts over
  polished documentation.
- Conclusions should be tested against the reader’s own codebase, risk level,
  team practices, and tooling.

## Status

Work in progress. The scope, terminology, methodology variants, and conclusions
will continue to change as experiments produce stronger evidence.

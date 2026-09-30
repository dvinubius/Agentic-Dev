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
| [`Agentic-Methodologies/`](Agentic-Methodologies/) | Notes on Matt Pocock's actively maintained approach and historical alternatives. See the [methodologies overview](Agentic-Methodologies/methodologies-overview.md). |
| [`Agentic-Methodologies/Matt-Pocock-Methodology/`](Agentic-Methodologies/Matt-Pocock-Methodology/concept/) | Working notes on the reasons behind the approach's spec, documentation, and TDD choices. |
| [`Universal-Benchmark/`](Universal-Benchmark/) | Work in progress on a universal benchmark for comparing coding models across project scenarios and execution styles. |
| [`research/QRSPI-Methodology/`](research/QRSPI-Methodology/) | Research notes on the QRSPI workflow for planning and delivering complex brownfield changes. |
| [`UI-design/`](UI-design/) | Research into agentic UI and design-to-implementation workflows, including paths with and without Figma. |
| [`skills/`](skills/) | Reusable coding-agent skills, scripts, and reference material. See [Skills](#skills). |
| [`explainers/`](explainers/) | Visual explainers in HTML and PDF. See [Explainers](#explainers). |
| [`Agentic-Methodologies/deprecated/`](Agentic-Methodologies/deprecated/) | Earlier approaches retained for comparison and historical context. They are not current recommendations. |

## Skills

Each skill lives in `skills/<name>/SKILL.md`. An agent environment that supports
skills can load these files from this repository; the supporting scripts and
references remain beside their respective skills.

| Skill | Purpose |
| --- | --- |
| [`daedalus`](skills/daedalus/SKILL.md) | Turn finished coding work into a deliberate-practice challenge. |
| [`explain-diff`](skills/explain-diff/SKILL.md) | Create an interactive HTML explanation of a code change. |
| [`feynman`](skills/feynman/SKILL.md) | Teach a technical theme through its mechanism, examples, and an exercise. |
| [`neatify-code`](skills/neatify-code/SKILL.md) | Improve maintainability in a bounded code area while preserving behavior. |
| [`no-bs-opus`](skills/no-bs-opus/SKILL.md) | Apply a direct, concise communication style. |
| [`no-bs-opus-explicit`](skills/no-bs-opus-explicit/SKILL.md) | Apply the original, more explicit version of that style. |
| [`reflow-markdown`](skills/reflow-markdown/SKILL.md) | Rewrap Markdown prose without changing its words or structure. |
| [`socrates`](skills/socrates/SKILL.md) | Guide reasoning with targeted questions and graduated hints. |
| [`validate-markdown-repo`](skills/validate-markdown-repo/SKILL.md) | Check local Markdown links, skill frontmatter, and template pairs. |

Check this README, the attribution notice, and the skill documentation from
the repository root with
`python3 skills/validate-markdown-repo/scripts/validate_markdown_repo.py --root . --frontmatter-root skills --include README.md --include THIRD_PARTY_NOTICES.md --include 'skills/**/*.md'`.
The [Markdown reflower](skills/reflow-markdown/scripts/reflow_markdown.py) is
available for repositories with an established wrap width; this repository
does not enforce one. See [third-party notices](THIRD_PARTY_NOTICES.md) for
attribution of adapted skills.

## Explainers

The visual explainers are available as HTML and PDF:

| Topic | HTML | PDF |
| --- | --- | --- |
| Agent loop | [Read](explainers/agent-loop.html) | [Download](explainers/agent-loop.pdf) |
| Cognitive surrender | [Read](explainers/cognitive-surrender.html) | [Download](explainers/cognitive-surrender.pdf) |
| Context management | [Read](explainers/context-management-system.html) | [Download](explainers/context-management-system.pdf) |

## Methodology direction

Matt Pocock's approach is the only methodology here I currently find viable
for ongoing use. I use it mostly as Matt maintains it. The
[workflow notes](Agentic-Methodologies/Matt-Pocock-Methodology/concept/matt-pocock-workflow.md)
remain here to explain why some choices have proved useful in my work and to
make less obvious decisions about specs, documentation, and TDD explicit.
They are an interpretation and record of practical experience, not a local
replacement for Matt's maintained skills.

[Spartan SDD](Agentic-Methodologies/deprecated/Spartan-SDD/concept.md) is
deprecated because it is no longer worth maintaining. Ultra Lean and other
earlier approaches are also retained under
[`Agentic-Methodologies/deprecated/`](Agentic-Methodologies/deprecated/)
for historical context, not as current recommendations.

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

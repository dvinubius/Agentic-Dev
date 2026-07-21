# CRISPY (qrspi)

Workflow for a feature in a brownfield project.

https://github.com/matanshavit/qrspi

- QRDSP (pre execution)
  - Questions
  - Research
  - Design Discussion
  - Structure Outline
  - Plan
- Execution
  - Worktree
  - Implement
  - Review

Every step from QRDSP is in a **new context window**, with a new prompt.

## Applicability

For complex, multi-file changes in existing codebases — the kind where 
getting the design wrong is expensive. Not every task needs all 8 phases:

- Simple bug fix: Skip to /qrspi/7_implement with a hand-written plan
- Small feature: Start at /qrspi/3_design if you already know the codebase

If a task can be described in one sentence and 
touches fewer than 3 files, QRSPI is overkill.

## Pre-Execution Steps

### Questions

Generate questions regarding the task at hand.
Purpose: identify what the agent doesn’t know / can't figure out.
The engineer writes questions that force the model to touch all 
relevant parts of the codebase — moving from a vague ticket to
a concrete list of technical inquiries. 

As a result, the engineer finds out what the agents needs to be 
told since it can't figure it out on its own. 

### Research

Research for answers to the questions above. The agent gathers 
objective facts about the current codebase. 

Deterministically **hide the ticket/task** from the research context window.

The agent traces logic flows and identifies existing system parts without 
forming opinions on how to change them. It produces a technical map — 
not a plan, not a recommendation. A factual record of what the code does.

This step is not driven by the goal of doing the ticket / building the feature etc.
What results is not a persuasive discourse, but cold facts.

The human reviews the result before any implementation thinking begins.

### Design Discussion

Create a shared "design concept" between human and agent.

The highest-leverage stage. The agent “brain dumps” its understanding.

Purpose: catch bad assumptions or wrong patterns. If caught, redirect 
the agent toward correct architectural standards before any code is planned.

**Design Discussion doc (~200 lines)** captures
- current state
- desired end state
- patterns to follow
- resolved decisions
- open questions

"Do not outsource the thinking."

### Structure Outline

Design is “where we’re going,” Structure Outline is “how we get there.”

**Structure/Outline doc (~2 pages)** 
- a high-level breakdown of phases/order of implementation and testing checkpoints
- not full code details
- as opposed to 8-page plans
- enforce vertical slicing & checkpoints

### Plan

The tactical implementation document.

Agent creates it based on design discussion docs and Structure/Outline doc.
This ensures alignment

**Do not review the plan** in depth: this would below leverage -
it may be implemented differently after all, so code review is needed anyway.

The high leverage was in the design discussion.

---

## Execution Steps

### Work Tree

The agent organizes tasks into a manageable hierarchy based on
the vertical slices from the Structure Outline. 
Each branch maps to a testable unit of work.

Biggest issue: vertical slices are not easily to do in parallel. 
They typically build on each other, so sequence is needed.

### Implement

### Pull Request (PR)

Human review of the code. **Read and own the code**. No exceptions.
But because the team already aligned on Design and Structure documents,
reviews are faster and contain fewer surprises. 

The craft standard: no slop makes it into production.

---

## vs. M. Pocock 

Common ground
- seek shared "design concept" (alignment goal)
- prefer vertical slices
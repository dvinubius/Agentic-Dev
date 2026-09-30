# Methodologies Overview

## Current approach: Matt Pocock

Matt Pocock's approach is the only methodology in this repository that I
currently find viable for ongoing use. I use it mostly as Matt maintains it,
rather than maintaining a separate local workflow. The
[workflow notes](Matt-Pocock-Methodology/concept/matt-pocock-workflow.md) record
my practical insights and explain the reasoning behind choices that can be easy
to miss, especially the roles of specs, documentation, and TDD. They are not a
substitute for Matt's maintained skills.

For serious, long-running work, my experience favors developer involvement in
planning and final review. Implementation can be delegated after the work is
clear enough to execute and verify. Small vertical slices and fast feedback
help expose misunderstandings before they spread through the codebase.

| Choice | Why it matters in my practice |
| --- | --- |
| **Spec** | Captures the agreed work, including intent, observable behavior, scope, and relevant implementation and testing decisions. It is a useful handoff for a bounded task, not a demand for exhaustive upfront documentation. |
| **Docs** | Code shows current behavior; shared language and decision records preserve context that code alone does not explain. Keep these documents small and update them when understanding changes. |
| **TDD** | Provides a tight feedback loop and evidence that an implementation meets its requirements. The goal is useful verification, not tests written only to satisfy a ritual. |

## Other work in this repository

The [QRSPI research notes](../research/QRSPI-Methodology/concept.md) and
[workflow-tools research](../research/workflow-tools.md) explore other ideas and
tools. They are research material, not competing current recommendations.

## Deprecated approaches

- [Spartan SDD](deprecated/Spartan-SDD/concept.md) is no longer worth
  maintaining. Its minimal rules added little value as models and harnesses
  improved.
- [Ultra Lean](deprecated/Ultra-Lean-Methodology/) overlaps too heavily with
  Matt Pocock's approach.
- The other material under [`deprecated/`](deprecated/) remains for historical
  comparison and to show how the methodology thinking evolved.

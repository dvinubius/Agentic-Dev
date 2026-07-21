# Interface Design Alternatives

Use this process only after the engineer selects a deepening candidate.

## Frame The Problem

State:

- responsibilities the interface must expose;
- behavior and complexity it should hide;
- invariants, ordering, errors, and performance constraints;
- dependency categories and seam constraints;
- callers and permitted verification that will use it.

## Produce Alternatives

Design at least three meaningfully different interfaces sequentially:

1. minimum surface: one to three entry points with high leverage;
2. flexible surface: supports credible extension needs;
3. common-path surface: makes the dominant caller trivial.

Add a ports-and-adapters alternative when a remote or external dependency makes
it relevant.

For each alternative include:

- operations, types, and important non-type contract details;
- a caller example;
- complexity hidden behind the interface;
- dependency and adapter strategy;
- verification approach under the root frontend automated-test policy;
- tradeoffs in depth, locality, and flexibility.

## Compare

Compare alternatives by:

- interface size;
- leverage;
- locality;
- seam placement;
- verifiability;
- migration risk;
- compatibility with accepted decisions.

Recommend one design or a clearly described hybrid.

# Simplifier Reference

This reference adapts the general code-simplification guidance from
Anthropic's `code-simplifier` agent for Lean's `neatify-code` skill.

## Core Intent

Simplify and refine code for clarity, consistency, and maintainability while
preserving exact behavior. Focus on recently modified code unless the developer
selects a broader scope.

## Principles

- Preserve functionality, outputs, side effects, errors, and public contracts.
- Follow project standards from local instructions and `docs/conventions.md`.
- Prefer readable, explicit code over clever compression.
- Reduce unnecessary complexity, nesting, redundancy, and incidental
  abstraction.
- Improve names when they make control flow, data flow, or domain concepts
  clearer.
- Consolidate related logic when it improves locality and does not hide
  important policy.
- Remove comments that restate obvious code; keep comments that explain
  non-obvious intent, invariants, or constraints.
- Avoid nested ternaries and dense one-liners when a simple branch or helper is
  easier to read.
- Preserve helpful abstractions that clarify ownership, variation, or
  verification boundaries.
- Do not combine too many concerns into one function, component, service, or
  module.
- Do not prioritize fewer lines over debuggability or future change.

## Balance Checks

Before applying a simplification, ask:

- Is the resulting behavior demonstrably the same?
- Is the new version easier to understand for a maintainer who knows the
  project?
- Did this remove real complexity, or just move it elsewhere?
- Did this improve locality without creating a larger hidden dependency?
- Did this keep domain policy, validation, authorization, and persistence
  responsibilities in their accepted homes?

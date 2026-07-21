---
name: ensure-docs-matched
description: Check and reconcile technical documentation and implementation for the current change, a selected area, or an explicitly requested whole-repository audit so accepted technical intent, code, tests, contracts, planning, commands, guidance, and local agent guides agree.
---

# Skill: Ensure Docs Matched

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may maintain `.agent-state/task-handoff.md` as temporary
runtime state outside `.agent/`, as defined in root `AGENTS.md`.

Keep implementation matched with accepted technical intent and keep
non-normative project docs matched with current repository facts. Normative
docs are inputs to implementation, not generated descriptions of whatever the
code currently does. Do not create end-user behavior or public integration
documentation.

## Scope Selection

Use exactly one mode:

- **current change**: normative docs, implementation, and project docs affected
  by the current diff or completed implementation work;
- **selected area**: technical docs and implementation evidence for a named
  feature, subsystem, contract, path, spec section, or documentation set;
- **whole repository**: a systematic technical-alignment audit across the
  repository.

If a standalone developer request does not make the mode and boundary clear,
ask which mode to use before inspecting. Do not assume "current change" merely
because recent work exists. A workflow that invokes this skill may supply the
mode explicitly; do not ask again when it does.

Agent-selected use is limited to current-change mode or one tightly bounded
directly affected area. Whole-repository mode follows the selected work mode.
Never silently expand from one mode to another.

`../../../docs/planning.md` is a cross-cutting orientation file. Review the
entire file in every mode, not only notes introduced or affected by the current
change. Remove or update stale and contradicted state that repository evidence
can resolve safely; report uncertainty instead of preserving known drift.

## Required Context

Read:

- `.agent/docs/CONTEXT.md`;
- the current diff, selected implementation area, or repository inventory,
  according to the chosen mode;
- relevant current specs;
- affected code, permitted tests, contracts, and docs;
- `../../../docs/planning.md`;
- `../../../docs/normative/README.md` and relevant normative documents when
  code changed;
- `../../../docs/repository-map.md` and
  `../../../docs/development-commands.md` when paths, commands, or navigation
  may be affected;
- `.agent/local-guides/CONTEXT.md` and applicable nested `AGENTS.md` files when
  local scope, entry points, constraints, protected paths, verification, or
  child-guide routing may be affected;
- root `README.md`, if present, when navigation may be affected.

## Procedure

1. State the selected mode, boundary, exclusions, and evidence sources.
2. Build the review set:
   - in current-change mode, trace the accepted design, diff, and completed
     outcome across affected normative docs, implementation, and project docs;
   - in selected-area mode, inventory the area's docs and the code, specs,
     contracts, configuration, and navigation that can confirm or contradict
     them;
   - in whole-repository mode, inventory documentation roots and indexes,
     including root `README.md`, `../../../docs/`, relevant specs, and
     repository-owned local guides. Divide the audit into bounded passes and
     track every discovered document as reviewed, changed, intentionally
     excluded, generated, or unverifiable.
3. Check:
   - architecture responsibilities, system context, dependency directions, and
     important internal dynamics;
   - external systems used, authoritative references, used contract surfaces,
     data projections and mappings, ignored data, unknown-field behavior,
     compatibility assumptions, operational behavior, and verification;
   - executable schemas and source contracts for externally consumed
     interfaces when affected, without turning technical docs into public
     integration instructions;
   - configuration, permissions, and technical failure handling;
   - durable decisions and conventions;
   - active plans, delivery status, technical design impulses, and stale or
     contradicted notes across the whole of `../../../docs/planning.md`;
   - root README links and development commands when affected;
   - applicable local agent-guide scope, entry points, constraints, protected
     paths, verification, and direct child-guide indexes.
4. Reconcile each in-scope mismatch according to its canonical source:
   - when implementation, tests, schemas, or executable contracts disagree
     with `../../../docs/normative/`, repair them to match accepted technical
     intent;
   - when repository maps, commands, planning notes, contributor guidance,
     local agent guides, or root README navigation disagree with canonical
     repository evidence, update those non-normative docs;
   - do not rewrite normative docs merely to legitimize existing code.
5. Update the closest applicable nested `AGENTS.md` only when the change alters
   its local routing or work contract. Ordinary behavior changes do not belong
   in a local guide.
6. Repair small in-scope gaps when the active request authorizes edits. Follow
   the selected work mode when a repair materially broadens scope or requires
   a high-impact decision. In whole-repository mode, do not limit findings to
   recent changes or exclude a mismatch because of its age.
7. Compare template-backed files with their read-only templates when their
   structure appears damaged. Restore structure in the live file only.
8. Keep one canonical home for each fact and prefer links over duplication.
9. Verify implemented behavior against code and supporting executable evidence;
   verify technical direction against architecture, decisions, and integration
   contracts. Use schemas, configuration, and authoritative external references
   as supporting evidence.

## Guardrails

- Do not document unimplemented specs as current technical state.
- Do not create end-user behavior narratives or instructions for external
  consumers integrating with this system.
- Do not edit root `AGENTS.md`, root `CONTEXT.md`, or anything under `.agent/`.
- Do not use a nested `AGENTS.md` as another technical, architecture, decision,
  planning, command, or convention document.
- Do not copy temporary planning prose into `docs/`.
- Do not create a decision record for an obvious or easily reversible detail.
- Follow the selected work mode before documenting a high-impact decision that
  has not yet been accepted.
- Do not change normative technical intent as a cleanup response to code drift.

## Output

Report the selected mode and boundary, technical surfaces compared, mismatches
found, code or non-normative docs repaired, local-guide changes or no-change
disposition when relevant, exclusions, unverifiable claims, and unresolved
uncertainty. In whole-repository mode, include inventory coverage so "whole
repository" is not represented by a sample.

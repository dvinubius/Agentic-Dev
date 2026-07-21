---
name: maintain-local-agent-guides
description: Initialize or refresh a sparse hierarchy of mutable nested AGENTS.md files at durable repository boundaries so agents can load precise local routing, constraints, and verification without duplicating canonical project documentation.
---

# Skill: Maintain Local Agent Guides

## Methodology Boundary

Root `AGENTS.md`, root `CONTEXT.md`, and installed methodology under `.agent/`
are read-only during normal project work. This skill may create, update, move,
or remove nested `AGENTS.md` files as mutable project state. It may update
`docs/repository-map.md` and parent nested guides to keep indexes current.

Do not edit application code, tests, specs, behavior docs, architecture docs,
decisions, conventions, or planning merely to make a proposed guide true.
Report missing or contradictory canonical information instead.

## Modes

Use one of two modes:

- **Initialization:** identify the smallest useful initial guide hierarchy for
  a repository or explicitly selected broad area that has no adequate local
  guide structure.
- **Refresh:** assess existing guides in the current change, a selected area,
  or an explicitly requested repository-wide scope; update stale guides,
  identify missing useful guides, and remove or consolidate guides that no
  longer justify their cost.

A repository-wide initialization or refresh is a broad documentation pass. Run
it only when the developer explicitly requests that scope in `SUPERVISED` mode
or when the agent records an autonomous decision in `AUTONOMOUS` mode.
Agent-selected use must remain limited to the current change or one tightly
bounded affected area.

## Required Context

Read:

- root `AGENTS.md` and root `CONTEXT.md`;
- `.agent/local-guides/CONTEXT.md` and
  `.agent/local-guides/template.md`;
- `docs/repository-map.md`;
- `docs/normative/README.md` and relevant normative docs;
- `docs/development-commands.md`;
- `docs/conventions.md`;
- existing nested `AGENTS.md` files in scope;
- relevant package manifests, build configuration, source entry points, tests,
  generated-file notices, and canonical docs needed to evaluate candidate
  boundaries.

Begin with repository structure, manifests, and focused search. Do not read
every source file merely because the requested scope is broad.

## Candidate Standard

A candidate directory must be a durable subtree boundary and have evidence for
at least one meaningful signal:

- distinct ownership, dependency, permission, or side-effect rules;
- a distinct supported verification workflow or working directory;
- generated, vendored, migration, infrastructure, security-sensitive, or
  otherwise protected paths;
- several stable entry points agents repeatedly need to locate;
- direct child boundaries that need routing;
- repeated evidence that agents over-explore, choose the wrong entry point, or
  edit the wrong surface.

Reject a candidate when:

- a directory listing or `docs/repository-map.md` already provides enough
  guidance;
- the boundary is temporary, speculative, or likely to move;
- the proposed content would mostly duplicate specs, behavior docs,
  architecture docs, decisions, commands, conventions, or root methodology;
- the guide would contain only obvious statements;
- a parent guide can express the useful rule concisely without becoming broad
  or ambiguous.

Prefer one guide per major application, service, package family, or
infrastructure area. Add deeper guides only when evidence supports them.

## Procedure

### 1. Establish Scope And Mode

State:

- initialization or refresh;
- requested repository or area scope;
- whether the pass is explicit and broad or agent-selected and bounded;
- files that may be changed: nested `AGENTS.md` files,
  `docs/repository-map.md`, and affected parent guide indexes.

Do not mix application implementation work into this skill.

### 2. Build A Structural Map

Inspect structure before content:

- top-level applications, services, packages, infrastructure, migrations, and
  generated or vendored areas;
- package and workspace manifests;
- existing repository-map and architecture entries;
- existing nested guide paths and index relationships;
- distinct build and verification roots.

Then inspect only enough representative source, tests, configuration, and docs
to confirm or reject each candidate.

Use bounded read-only subagents for large independent areas when available.
Require concise reports containing candidate path, evidence, proposed scope,
useful local content, duplication risks, and recommendation.

### 3. Evaluate Existing Guides

For every existing guide in scope, check:

- declared scope matches its directory and current responsibility;
- local map points to supported, stable entry points;
- constraints are current and genuinely local;
- verification commands exist and include the correct working directory and
  prerequisites;
- canonical references resolve and avoid substantive duplication;
- direct child-guide index is complete;
- no child weakens root methodology or parent rules;
- no product intent, behavior narrative, decision rationale, temporary plan,
  or task history has leaked into the guide;
- the guide remains concise enough to improve attention.

Classify each as `keep`, `update`, `consolidate`, or `remove`.

### 4. Propose The Guide Tree

In `SUPERVISED` mode, before a broad initialization, broad refresh, or
structural reorganization, present a proposed tree with:

| Candidate path | Action | Evidence | Intended local value | Canonical sources linked |
|---|---|---|---|---|

Also list rejected candidates and the reason they do not justify a guide.

Obtain developer approval before creating or reorganizing a broad guide tree in
`SUPERVISED` mode. In `AUTONOMOUS` mode, record the evidence and decision
before writes. A focused refresh of already applicable guides after an accepted
application change may proceed without a separate approval when it does not
broaden scope or change architecture.

### 5. Create Or Refresh Guides

For accepted or autonomously selected candidates:

- use `.agent/local-guides/template.md` as the structural guide;
- replace placeholders with verified project facts;
- omit empty sections;
- declare precise covered and excluded paths;
- include only supported modification entry points and local constraints;
- include only verification that already exists;
- link to canonical docs rather than copying their content;
- index only direct child guides;
- target roughly 1-2 KiB unless additional content clearly earns its cost.

Do not create a root project index in root `AGENTS.md`.

For removals or consolidation:

- preserve still-useful unique guidance in the nearest appropriate parent or
  canonical source;
- update all affected indexes;
- do not delete a guide while its unique operational constraints would be
  lost.

### 6. Update Indexes

Update `docs/repository-map.md` under `## Local Agent Guides` with top-level
guide paths and concise scopes.

Update each affected parent guide's `## Child Guides` table with direct
children only. Remove stale rows immediately.

### 7. Validate

Check:

- every indexed guide exists;
- every guide is indexed by `docs/repository-map.md` or its direct parent;
- declared scopes match paths and do not overlap ambiguously;
- parent and child guidance does not conflict;
- root methodology remains unchanged;
- links and canonical references resolve;
- verification commands are present in the supported toolchain;
- no guide duplicates product requirements, implemented behavior,
  architecture rationale, decisions, planning, or global methodology;
- no guide contains placeholders, diary content, or stale warnings;
- the final tree is sparse and each guide has an evidence-backed purpose.

Run `git diff --check` and inspect the actual diff.

## Output

Report:

- mode and scope;
- guides created, updated, consolidated, removed, or left unchanged;
- evidence for each structural decision;
- candidates rejected and why;
- repository-map and parent-index changes;
- validation performed;
- canonical documentation gaps discovered but not changed;
- any residual uncertainty or area intentionally not scanned.

Do not claim initialization or refresh is complete when indexes are stale,
guide scope is ambiguous, or a guide's commands and references were not
verified.

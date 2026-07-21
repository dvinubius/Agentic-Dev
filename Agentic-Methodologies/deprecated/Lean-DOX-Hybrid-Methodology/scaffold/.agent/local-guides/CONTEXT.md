# Local Agent Guide Methodology

This file and `template.md` are read-only methodology. Mutable local agent
guides are nested `AGENTS.md` files outside the repository root.

## Purpose

Local agent guides provide path-specific operational context after the agent
has identified a likely work area. They reduce repeated discovery of stable
entry points, local constraints, protected or generated paths, focused
verification, and deeper guide boundaries.

They are a last-mile path router. They do not replace topic-oriented specs,
normative technical docs, conventions, planning, or source inspection.

## Authority And Ownership

- Root `AGENTS.md`, root `CONTEXT.md`, and `.agent/` are read-only methodology.
- Nested `AGENTS.md` files are mutable project-owned local guides.
- A nested guide governs only its declared subtree.
- A closer guide may specialize local work but must not weaken or contradict
  root methodology or a parent guide.
- Code remains the primary authority for current behavior.
- Use canonical project files for durable facts:
  - product intent: `specs/`;
  - accepted technical intent: `docs/normative/`;
  - commands: `docs/development-commands.md`;
  - conventions: `docs/conventions.md`;
  - temporary direction: `docs/planning.md`.

Local guides may link to or briefly route toward those sources. They must not
duplicate their substantive content.

## Loading Rules

1. Read root `AGENTS.md` and its required first-level project context.
2. Use the request, `docs/repository-map.md`, focused search, or available code
   intelligence to identify a likely target area.
3. Before the first edit in that area, read every nested `AGENTS.md` on the
   route from the repository root to the target.
4. Treat the nearest guide as the most specific local instruction while
   preserving every broader rule.
5. If investigation expands the edit scope, read the newly applicable guide
   chain before editing that area.

Do not recursively load every guide merely because it exists.

## Creation Criteria

Create a guide only for a durable subtree boundary when at least one of these
signals is meaningful:

- distinct ownership, dependency, permission, or side-effect rules;
- a distinct supported verification workflow or working directory;
- generated, vendored, migration, infrastructure, security-sensitive, or
  otherwise protected paths;
- several stable entry points agents repeatedly need to locate;
- direct child boundaries that need routing;
- repeated evidence that agents over-explore, choose the wrong entry point, or
  edit the wrong surface.

Do not create a guide:

- for every directory or merely because a folder exists;
- to restate names visible from a directory listing;
- for temporary branch or feature structure;
- when `docs/repository-map.md` already gives sufficient routing;
- before the boundary is stable enough to describe;
- when the content would primarily duplicate another canonical source.

Use `.agent/skills/maintain-local-agent-guides/SKILL.md` for initialization or
refresh. Broad guide creation, removal, or reorganization follows the selected
work mode.

## Content Rules

Use `template.md` as the structural guide. Omit empty sections in a created
guide.

A local guide may contain:

- precise covered and excluded paths;
- a compact map of supported modification entry points;
- local constraints that change how an agent should work;
- existing focused verification commands, working directories, and
  prerequisites;
- links to relevant canonical specs, docs, boundaries, and decisions;
- an index of direct child guides.

A local guide must not contain:

- product requirements or user-visible behavior narratives;
- architecture rationale or accepted decision history;
- temporary plans, task state, progress, or completed-work history;
- copied repository-wide methodology or conventions;
- speculative commands or checks that do not exist.

Prefer roughly 1-2 KiB per guide. A larger guide should justify why its content
does not belong in a canonical document or reusable skill.

## Indexing

- `docs/repository-map.md` contains the top-level local-guide index.
- Each nested guide indexes only its direct child guides.
- Do not put a mutable project index in root `AGENTS.md`.
- Update indexes when a guide is created, deleted, moved, or changes scope.

## Change Closeout

For an affected subtree, update the closest applicable guide when a change
alters:

- scope, ownership, or supported entry points;
- local constraints, protected paths, permissions, or side effects;
- focused verification commands or prerequisites;
- direct child-guide structure.

Ordinary behavior changes do not belong in local guides. Accepted architecture,
decisions, and external dependency contracts belong in `docs/normative/`.
Small code changes that do not alter local routing or work constraints do not
require guide churn.

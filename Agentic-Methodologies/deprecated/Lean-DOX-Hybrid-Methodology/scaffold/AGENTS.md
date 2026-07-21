# Agent Instructions

This file, root `CONTEXT.md`, and the installed files under `.agent/` are the
Lean-DOX hybrid methodology. They are read-only to the agent during normal
project work. Nested `AGENTS.md` files are mutable project-owned local guides,
not installed methodology. Temporary active-task state lives outside the
methodology tree at `.agent-state/task-handoff.md`.

## Required First Read

When reading this file, always read these direct references as one required
level of project context:

- `docs/repository-map.md`
- `docs/development-commands.md`
- `docs/normative/README.md`
- root `CONTEXT.md`

Do not recursively follow every link found in those files. After this required
one-level read, follow only the routes relevant to the current work.

## Project References

- Repository map: `docs/repository-map.md`
- Development and verification commands: `docs/development-commands.md`
- Accepted technical intent: `docs/normative/README.md`
- Current conventions: `docs/conventions.md`
- Current development planning: `docs/planning.md`
- Intended product behavior: `specs/README.md`

The project files above are mutable. Their canonical blank formats are
read-only templates under `.agent/docs/templates/` and
`.agent/specs/templates/`.

## Methodology Is Read-Only

During ordinary feature, fix, refactoring, documentation, specification, or
planning work:

- do not edit root `AGENTS.md`;
- do not edit root `CONTEXT.md`;
- do not edit, delete, move, rename, or generate files under `.agent/`;
- do not customize methodology files for the project;
- do not remove methodology headings, templates, routes, placeholders, or
  boilerplate because they appear unused.

Only an explicit request to upgrade or modify the methodology authorizes
changes to these paths. Nested `AGENTS.md` files may be maintained as local
project guides under the rules in `.agent/local-guides/CONTEXT.md`. Other
durable project-specific facts belong in `docs/`, `specs/`, source, tests,
configuration, or other project-owned files. `.agent-state/` contains only
temporary active-task state.

When a mutable project file drifts structurally, restore its intended shape
from the corresponding read-only template without replacing valid
project-specific content.

## GitHub Tools

For GitHub operations, prefer the GitHub CLI (`gh`) over GitHub MCP. Use
GitHub MCP only when `gh` is unavailable, insufficient for the specific
operation, or explicitly requested.

## Local Agent Guides

After the required first read, use the request, `docs/repository-map.md`, and
focused discovery to identify the likely work area. Before editing that area,
read every nested `AGENTS.md` on the path from the repository root to the
target. If the edit scope expands, read the newly applicable chain before
editing it. Do not recursively load every guide.

Nested guides may specialize local entry points, work constraints, protected
paths, verification, and child routing. They must not weaken this file or
duplicate canonical specs, technical documentation, architecture rationale,
decisions, conventions, commands, or planning. Follow
`.agent/local-guides/CONTEXT.md`.

## Work Mode

The developer must choose exactly one work mode in the prompt:

- `AUTONOMOUS`: read and follow `.agent/skills/autonomous/SKILL.md`.
- `SUPERVISED`: read and follow `.agent/skills/supervised/SKILL.md`.

If the prompt does not specify a mode, ask which mode to use before starting
substantive work.

Mode controls methodology-level approval, review, confirmation, and phase
handoff behavior. It does not override external tool approvals, sandbox rules,
repository policies, credentials, legal/security constraints, local-guide
rules, or explicit developer instructions.

## Task Handoff

For non-trivial multi-phase work, the main agent maintains the single canonical
`.agent-state/task-handoff.md`. Create the parent directory and file when
durable phase state becomes useful, update it at meaningful phase boundaries,
and keep it short and current. It is not a diary, plan archive, task tracker,
or substitute for specs, decisions, or `docs/planning.md`. Never commit
`.agent-state/`.

Include only:

- goal and current phase;
- scope and non-goals;
- decisions and constraints;
- current implementation and observable-outcome summary;
- files changed;
- concise test and verification status;
- documentation status;
- unresolved risks or next action.

Delete obsolete attempts instead of accumulating history. Before a later phase,
after context compaction, or whenever context feels stale, reconstruct from:

1. current repository state and relevant source;
2. `git status` and the current diff;
3. `.agent-state/task-handoff.md`;
4. the latest concise test or subagent report.

Update the handoff before switching from investigation or planning to
implementation, from implementation to verification, and from verification to
documentation or final review when those phases are distinct. Delete
`.agent-state/task-handoff.md` when the task is completed or abandoned. A
completed task must not leave a residual handoff file. Remove `.agent-state/`
too when it is empty.

## Development And Verification

Use the commands and environment rules in `docs/development-commands.md`.
Run straightforward local checks without asking. For unusually broad, costly,
slow, or environmentally consequential checks, follow the selected work mode.
After two failed attempts with the same verification path or tool, follow the
selected work mode before investing more effort.

Never claim a command passed unless it ran successfully.

## Coding And Documentation Standards

- Prefer small, coherent, reviewable changes.
- Follow current conventions in `docs/conventions.md`.
- Preserve public APIs unless the selected change requires otherwise.
- Add proportionate automated verification where allowed.
- Keep code and tests matched with `docs/normative/`.
- Do not reformat or clean up unrelated files.
- Ignore `.devnotes/`: do not read, search, modify, or treat it as context.
- Use `docs/` only for project orientation, accepted technical state, external
  dependency contracts, decisions, conventions, commands, and planning.
- Use `specs/` only for current product and business intent.
- Keep implementation details out of specs. A spec statement must be something
  a product owner would assert without choosing how the product is built and
  must remain true if the implementation is replaced.
- Route accepted durable technical decisions to
  `docs/normative/decisions/`; route tentative or near-term technical reasoning
  to `docs/planning.md` > `Technical Design Impulses`.
- Keep root `README.md` concise and link-oriented.
- Keep applicable nested `AGENTS.md` files current only when a change alters
  their local scope, entry points, constraints, verification, protected paths,
  or direct child-guide index.

Code is authoritative for what currently runs. `docs/normative/` is
authoritative for accepted technical intent. Use the repository map to locate
implementation and normative docs to assess whether it matches that intent.

Do not maintain end-user behavior documentation or instructions for external
consumers as part of this methodology. Generate such documentation separately
when needed.

## Normative Technical Documentation

`docs/normative/` contains accepted architecture, decisions, and external
integration contracts. Read its index and relevant documents before work that
could affect technical design. Proposed technical direction belongs in
`docs/planning.md` until accepted.

## Agent Workflow

- The developer is the strategist and final decision maker.
- Work on one coherent line of work at a time.
- Follow root `CONTEXT.md` and only load routed context needed for the work.
- Read and apply the selected work mode skill before substantive work.
- Read the applicable nested `AGENTS.md` chain before editing project files.
- Use `.agent/skills/work-on-app/SKILL.md` for non-trivial application work.
- Use `.agent/skills/finish-change/SKILL.md` before declaring non-trivial work
  complete.
- At completion, list tests created or changed, what they verify, whether they
  ran, and their pass, fail, or not-run results.

## Assurance Scope

The `ensure-*` skills support current-change, selected-area, and
whole-repository modes. For a standalone request whose mode or boundary is
ambiguous, ask the developer to choose before inspecting. A workflow may pass
an explicit mode without a redundant question.

Agent-initiated assurance remains limited to the current change or a tightly
bounded directly affected area. Whole-repository mode requires explicit
developer request in `SUPERVISED` mode or a recorded autonomous decision in
`AUTONOMOUS` mode, and must report inventory coverage, exclusions, and
unverifiable areas.

## Never

- Do not broaden scope silently.
- Do not bypass architecture, validation, authorization, or data-access layers.
- Do not skip or conceal failing checks.
- Do not revert, overwrite, or discard unrelated pre-existing work.
- Do not hand-edit generated or vendored files unless explicitly maintained.
- Do not expose credentials, tokens, secrets, or private environment values.
- Do not silently edit content marked as developer-maintained.

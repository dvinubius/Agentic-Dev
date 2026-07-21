# Agent Instructions

Read this file first, then read `CONTEXT.md` for methodology and routing.

## Project Overview

- Product: `<short description>`
- Stack: `<languages, frameworks, storage, hosting>`
- Architecture: `<one-paragraph summary or docs path>`

If the project identity or high-level architecture summary changes, use
`agent/skills/update-readme/SKILL.md` to keep the root README current.

## Repository Map

| Area | Path | Purpose |
|---|---|---|
| Application source | `<path>` | `<main implementation responsibility>` |
| Tests | `<path>` | `<test types and scope>` |
| Entry points | `<path>` | `<runtime, CLI, API, or UI entry points>` |
| Configuration | `<path>` | `<build, runtime, and environment configuration>` |
| Generated or vendored content | `<path or none>` | `<how it is produced and whether agents may edit it>` |
| Migrations or infrastructure | `<path or none>` | `<schema, deployment, or infrastructure responsibility>` |

Remove rows that do not apply and add only stable, high-value paths. Keep
detailed navigation in `CONTEXT.md` files.

If the current work changes a stable, high-value path or its responsibility,
update this table. Do not add transient or task-specific paths.
If the change affects top-level contributor navigation, also update the root
README through `agent/skills/update-readme/SKILL.md`.

## Development Commands

Run commands from `<repository root or specified directory>` unless noted.

- Toolchain versions: `<version files or setup source>`
- Package manager: `<name and lockfile>`
- Required local services: `<services, setup command, or none>`
- Frontend automated tests: `<enabled / excluded>`

```text
install:      <command>
dev:          <command>
test:focused: <command or usage pattern>
test:full:    <command>
lint:         <command>
format:check: <command>
typecheck:    <command>
build:        <command>
verify:       <canonical combined verification command, if available>
```

Remove entries that do not apply. Use the repository's declared toolchain and
package manager. Never claim a command passed unless it ran successfully.

The frontend automated-test policy applies to browser, unit, and integration
tests whose primary subject is frontend behavior:

- `enabled`: create and run proportionate frontend tests under the normal task
  workflow;
- `excluded`: do not create, update, or run frontend automated tests. Use the
  task's `MANUAL-TESTING.md` to map affected acceptance criteria to concise
  manual scenarios for the engineer.

When frontend automated tests are excluded, do not run a combined test or
verification command that includes them. Use a narrower command that preserves
the remaining applicable checks. The exclusion does not waive backend tests,
contract checks, static analysis, typechecking, linting, builds, or other
non-frontend verification.

Do not override this repository policy inside an individual task. A policy
change requires an explicit engineer decision and an update to this file.
When changing an existing repository to `excluded`, explicitly decide the
disposition of existing frontend tests and commands. Do not delete them merely
because the flag changed, and do not present them as maintained verification if
they are no longer run.

If the current work changes the supported toolchain, command names, working
directory, required services, or verification workflow, update this section.
Also use `agent/skills/update-readme/SKILL.md` to keep the root README's
development commands synchronized.

After changing code, tests, or docs, choose verification checks proportionate
to the change. Run straightforward, local checks without asking. Before running
checks that are unusually extensive in duration, cost, scope, or environment
impact, explain why they are warranted and obtain the engineer's approval.
Report any relevant checks not run and why.

## Coding And Documentation Standards

- Prefer small, composable, reviewable changes.
- Follow existing conventions before introducing new patterns.
- Preserve public APIs unless the approved task requires a change.
- Behavior changes and bug fixes require proportionate automated tests unless
  the frontend automated-test policy excludes them or no useful automated test
  is feasible. In either case, record the reason and use credible alternate
  verification.
- Keep code, tests, contracts, and implementation docs synchronized.
- Do not reformat or clean up unrelated files.
- Ignore `.devnotes/`: do not read, search, modify, or treat it as project
  context or a source of truth.
- Use `docs/` only for application and implemented-system documentation.
- Keep the root `README.md` concise and link-oriented. Create or update it
  through `agent/skills/update-readme/SKILL.md`.
- Use Tailwind CSS for styling; do not introduce CSS Modules or CSS-in-JS.

## Architecture Boundaries

`docs/architecture/boundaries.md` is the normative source for current
architectural responsibilities, dependency directions, ownership, and
cross-cutting boundaries.

- Read it before planning or making code changes that could affect architecture.
- Treat it as the current baseline. Depart from it only when an approved task
  plan explicitly changes the affected boundaries.
- Update it whenever code changes alter the documented architecture.

## Agent Workflow

- The engineer remains the strategist and final decision maker.
- Use one task at a time and one agent at a time.
- Before work that may alter repository artifacts, check
  `agent/tasks/CURRENT.md`.
- If `agent/tasks/CURRENT.md` names a task, do not start unrelated work.
- Follow root `CONTEXT.md` and only load routed context needed for the work.
- Use formal tasks for non-trivial feature, issue-fix, or refactoring work.
- During task execution, stop at the review gates in
  `agent/tasks/CONTEXT.md` unless the engineer explicitly waives one.
- Update task progress before every handoff and before ending an active work
  session.

## Engineer Handoffs

Whenever waiting for engineer confirmation, a decision, approval, or review:

1. summarize the relevant status and evidence first;
2. end the response with the explicit question the engineer must answer;
3. put that question in a separate final paragraph;
4. place no text after the question.

Do not merely state that work awaits acceptance, approval, confirmation, or
review. Ask for the required response directly.

## Informal Change Rule

If asked for a non-trivial code, test, or substantive application-doc change
outside a formal task and outside an applicable agent skill:

1. remind the engineer that a formal task is preferred;
2. ask for confirmation before proceeding informally;
3. if confirmed, apply task-like rigor proportionate to risk;
4. preserve Omni-Sync and report verification.

Trivial edits may proceed directly when they cannot create meaningful drift.

## Approval Required

- Add or replace dependencies or external services.
- Change the database schema or create or apply migrations; present the
  migration plan first.
- Change public APIs or externally consumed contracts.
- Run destructive operations, deployments, or actions against production
  systems.
- Create commits.

## Never

- Do not broaden scope silently.
- Do not bypass architecture, validation, authorization, or data-access layers.
- Do not silently skip or conceal failing checks.
- Do not revert, overwrite, or discard pre-existing work unrelated to the
  current request.
- Do not hand-edit generated or vendored files unless the repository explicitly
  designates them as maintained that way.
- Do not commit, print, or expose credentials, tokens, secrets, or private
  environment values.
- Do not silently edit sections marked as engineer-maintained.

---
name: dev-ops
description: Handle deployment, release, infrastructure, environment, CI/CD, hosting, GitHub operations, or other operational work while preferring available CLIs over MCP calls.
---

# Skill: Dev Ops

## Methodology Boundary

During normal project work, do not edit root `AGENTS.md`, root `CONTEXT.md`,
or installed methodology under `.agent/`. These are read-only methodology.
Nested `AGENTS.md` files are mutable project guides; read the applicable guide
chain before editing their subtree and update guides only according to
`.agent/local-guides/CONTEXT.md`.
The main agent may maintain `.agent-state/task-handoff.md` as temporary
runtime state outside `.agent/`, as defined in root `AGENTS.md`.

## Scope

Use this skill for deployment, release, hosting, infrastructure, environment,
CI/CD, GitHub, or other operational work.

This skill does not authorize destructive operations, production actions,
deployments, commits, pushes, or dependency installation without the approvals
or autonomous decisions required by the selected work mode, repository rules,
and the developer.

## Required Context

Read:

- root `AGENTS.md`;
- `.agent/local-guides/CONTEXT.md` and applicable nested `AGENTS.md` files for
  affected operational paths;
- `docs/development-commands.md`;
- relevant project configuration, scripts, workflows, deployment files, and
  operational docs;
- applicable specs, normative technical docs, and planning notes
  when the operational work could affect behavior, contracts, data, security,
  privacy, cost, or availability.

## Procedure

Prefer an available CLI over MCP calls when a CLI can perform the operation
reliably.

If the relevant CLI is unavailable, suggest installing or configuring it before
suggesting an MCP server installation or using an existing MCP integration.

Use an MCP tool only when:

- no suitable CLI is available;
- the MCP tool is known to be more reliable or complete for the specific
  operation;
- the developer explicitly requests that MCP tool.

Before any consequential operational action, state the target, command or tool,
environment, expected effect, rollback or recovery path when relevant, and
approval or autonomous decision needed.

## Output

Report the operational target, tool used, commands or MCP calls attempted,
results, approvals obtained, checks run, local guide changes or no-change
disposition when relevant, and any remaining risk or follow-up.

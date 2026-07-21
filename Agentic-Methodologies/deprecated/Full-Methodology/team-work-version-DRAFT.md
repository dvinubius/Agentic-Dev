# GitHub-Backed Team Work Version

## Status

This document is a conceptual team-work variant of the methodology. It is not
the canonical methodology and does not yet change the scaffold.

## 1. Purpose

This variant supports several engineers working in parallel without giving up:

- one active task per engineer workspace;
- repository-grounded agent execution;
- durable task evidence;
- explicit planning and review;
- efficient analysis of the shared backlog.

GitHub Issues becomes the shared task tracker. The repository keeps the active
task's execution package on its branch and preserves completed execution
records after the work is ready to merge.

## 2. Governing Model

The system has three task representations with different responsibilities:

| Representation | Responsibility | Git tracked |
|---|---|---|
| GitHub Issues | Shared backlog, task definition, assignment, status, priority, and dependencies | External |
| Local issue snapshot | Generated local view of open GitHub issues for efficient agent analysis | No |
| Repository task package | Active execution state and completed execution evidence | Yes |

These representations must not be treated as interchangeable copies.

### 2.1 GitHub Is Canonical For Planned Tasks

GitHub Issues is the canonical source for tasks that have not entered local
execution. An issue owns:

- issue identity and URL;
- task type;
- goal and background;
- source spec references;
- task-local requirements;
- acceptance criteria;
- non-goals and constraints;
- risk and verification expectations;
- dependencies and known overlap;
- assignment and shared workflow status.

Issue comments may contain discussion, but accepted scope and decisions must be
folded into the issue body or another canonical artifact. Required task meaning
must not exist only in comments.

### 2.2 The Repository Is Canonical For Execution

When an engineer begins a task, its current GitHub issue is materialized into
the standard repository task package:

```text
agent/tasks/<type>/<github-number>-short-description/
|-- BRIEF.md
|-- PLAN.md
|-- PROGRESS.md
`-- LESSONS.md        # optional
```

During execution:

- `BRIEF.md` is the accepted local execution scope;
- `PLAN.md` is the approved implementation design;
- `PROGRESS.md` is the resumable execution state and evidence;
- the task package records its GitHub issue number, URL, and materialization
  timestamp.

Later changes to the GitHub issue do not silently replace active task files.
Material changes must be reconciled explicitly through the task workflow.

### 2.3 Completed Evidence Remains In Git

After execution is complete and the branch is ready to merge, move the task
package under the appropriate `done/` directory.

The completed package preserves:

- approved scope and plan;
- acceptance-criteria traceability;
- verification evidence;
- meaningful review decisions;
- residual risk;
- branch commit and pull-request references available before merge.

GitHub remains canonical for final shared status. The issue should normally be
closed automatically when the implementing pull request merges.

## 3. Scope Of `CURRENT.md`

`agent/tasks/CURRENT.md` is a workspace and branch lock, not a team-wide lock.

It prevents one engineer from directing agents in the same working tree toward
unrelated concurrent work. Different engineers may execute different tasks in
parallel on separate branches and working trees.

The rule becomes:

> One active task per engineer workspace, with team-wide coordination handled
> through GitHub assignment and status.

The repository's default branch must always have:

```text
Current task: none
```

A task branch may contain an active task while work is in progress. A draft
pull request may therefore temporarily show a non-empty `CURRENT.md`, but the
pull request must not be mergeable in that state.

## 4. Team Coordination In GitHub

GitHub needs a small, explicit task-state convention. A minimal label set is:

```text
task:feature
task:issue
task:refactoring
status:planned
status:in-progress
status:blocked
status:ready-for-merge
```

Assignment identifies the responsible engineer. Labels communicate lifecycle
state to people and agents.

Starting execution requires:

1. refresh the local issue snapshot;
2. confirm the issue is open and not already claimed;
3. check for conflicting or overlapping active work;
4. assign the issue to the engineer;
5. change its status to `status:in-progress`;
6. fetch the issue again and confirm the intended assignment and status;
7. create or switch to a dedicated branch or worktree;
8. materialize the issue into the task package;
9. set that workspace's `CURRENT.md`.

Claiming the issue must happen before implementation. If claiming fails or the
issue was claimed concurrently, execution must not start until the conflict is
resolved. GitHub assignment is coordination state rather than an atomic
distributed lock, so the post-mutation verification is required.

GitHub assignment reduces accidental duplicate execution, but it does not
replace communication for work that touches shared boundaries or requires
coordinated sequencing.

## 5. Local Open-Issue Snapshot

Each developer keeps a generated local snapshot of the repository's currently
open GitHub issues. This restores a complete, low-latency local planning view
without making planned tasks part of Git history.

### 5.1 Snapshot Properties

The snapshot must be:

- excluded from Git;
- reproducible from GitHub;
- safe to delete and rebuild;
- scoped to one known GitHub repository;
- machine-readable;
- easy for an agent to search;
- stamped with the last successful synchronization time;
- explicit about partial or failed synchronization.

A suitable conceptual layout is:

```text
.agent-cache/
`-- github-issues/
    |-- manifest.json
    |-- issues.json
    `-- issues/
        `-- <number>.md
```

`issues.json` is the structured source for scripts and audits. Per-issue
Markdown is a generated agent-readable projection. The tracked synchronization
script, not the cache, defines the format.

### 5.2 Required Snapshot Data

For each open issue, capture at least:

- number, title, body, state, and URL;
- labels, assignees, and milestone;
- creation and update timestamps;
- task type and workflow status when represented by labels;
- explicit dependencies, overlap, or supersession links present in the body;
- pull-request links exposed by the synchronization source.

Comments need not be copied if the project enforces the rule that current task
scope and accepted decisions belong in the issue body. If comments can change
task meaning, the snapshot must include them or the process must normalize
their accepted conclusions into the body.

### 5.3 Synchronization Contract

A tracked script should refresh the snapshot through the GitHub API, connector,
or authenticated `gh` CLI. It should:

1. resolve and verify the expected `owner/repository`;
2. fetch all open issues with pagination;
3. exclude pull requests returned by issue-oriented APIs;
4. write to a temporary location;
5. validate completeness and the expected schema;
6. replace the previous snapshot atomically only after success;
7. record repository identity, synchronization time, item count, and tool
   version in the manifest;
8. preserve the last successful snapshot when refresh fails;
9. mark the snapshot unavailable for task-aware operations when refresh fails;
10. report failure clearly rather than making stale data look current.

The script should support both:

- a normal incremental or conditional refresh for routine use;
- a forced complete refresh for correctness-sensitive audits.

### 5.4 Freshness Rules

Any operation that depends on the current open-task set requires a successful
snapshot refresh immediately before the operation. If refresh fails, the
operation stops.

| Operation | Required backlog state |
|---|---|
| General orientation involving open tasks | Successful refresh |
| Creating a task | Successful refresh |
| Broad feature planning | Successful refresh |
| Spec change conflict review | Successful refresh |
| Deprecated-task or missed-spec audit | Successful forced complete refresh |
| Activating or claiming a task | Successful refresh, then live GitHub verification and mutation |
| Completing a task | Successful refresh, then live GitHub update |

The previous successful snapshot may be retained to aid diagnosis, but agents
must not use it to continue an operation after a failed refresh.

### 5.5 Limits Of The Open-Issue Snapshot

The snapshot does not replace:

- completed task records in Git;
- live verification before claiming or mutating an issue;
- GitHub history for cancelled, duplicate, or rejected issues;
- normal Git conflict detection and pull-request review.

Duplicate checks should search:

1. the refreshed open-issue snapshot;
2. completed task packages in the repository;
3. relevant broad plans and current implementation.

Search closed GitHub issues when those sources do not resolve a likely
historical duplicate, or when cancelled and rejected proposals materially
affect the decision.

## 6. Task Lifecycle

### 6.1 Create

The `create-task` skill creates a GitHub issue rather than a planned task
directory.

Before creation it must:

1. refresh the open-issue snapshot;
2. inspect relevant current specs, code, docs, broad plans, open issues, and
   completed task records;
3. search for duplicates, partial overlaps, contradictory scope, and existing
   dependencies;
4. present credible matches to the engineer;
5. create the issue only after unresolved conflicts are addressed;
6. refresh or update the snapshot after successful creation;
7. link the issue from any broad-plan candidate that produced it.

The issue number replaces locally allocated task identifiers.

Task creation does not create `BRIEF.md`, `PLAN.md`, or `PROGRESS.md` and does
not occupy `CURRENT.md`.

### 6.2 Plan And Audit

Planning and analysis skills use the refreshed local snapshot as their primary
open-task input.

This includes:

- broad feature planning;
- duplicate and overlap analysis;
- spec-change conflict review;
- deprecated-task audits;
- missed-spec audits;
- architecture-improvement planning;
- dependency and sequencing analysis.

Skills should invoke the tracked synchronization script rather than each
implementing unrelated GitHub query logic. The script provides one normalized
local contract for all skills.

### 6.3 Activate

Activation converts one GitHub issue into branch-local execution state.

The activation procedure must:

1. verify and claim the issue live in GitHub;
2. create the task branch or worktree;
3. materialize the latest accepted issue body into `BRIEF.md`;
4. initialize `PLAN.md` and `PROGRESS.md`;
5. record GitHub identity and source timestamps;
6. set the workspace's `CURRENT.md`;
7. begin execution at plan assessment.

Materialization is not blind copying. Step 1 of execution still reconciles the
issue, specs, repository state, architecture, and acceptance criteria before
the plan is approved.

### 6.4 Execute

The existing six-step execution workflow remains branch-local.

During execution:

- the issue tracks shared assignment and coarse status;
- the task package tracks detailed scope, plan, progress, and evidence;
- issue changes that affect scope require explicit reconciliation;
- relevant discovered dependencies or blockers are synchronized back to the
  issue;
- another task may proceed in a different workspace when its scope does not
  conflict.

### 6.5 Prepare For Merge

Before a pull request becomes mergeable:

1. required checks and reviews pass;
2. acceptance criteria have final dispositions;
3. task evidence is complete;
4. the task package moves to `done/`;
5. `CURRENT.md` returns to `none`;
6. the GitHub issue is updated to `status:ready-for-merge`;
7. the pull request links the issue and is configured to close it on merge.

At this point the local execution is complete, but the GitHub issue remains
open until the pull request merges.

### 6.6 Merge And Close

On merge:

- GitHub closes the issue through the pull-request closing reference;
- the merged repository contains the completed execution record;
- other developers receive that record through normal Git synchronization;
- local issue snapshots remove the issue on their next refresh.

If a pull request is abandoned after being marked ready:

- reopen the task's execution state on its branch if work will continue; or
- release the GitHub assignment and status deliberately;
- do not leave the issue looking completed when no merge occurred.

## 7. Pull-Request And Branch Rules

The repository should enforce these merge conditions:

- `agent/tasks/CURRENT.md` says `Current task: none`;
- no active task directory exists outside a task type's `done/` directory;
- a normal task pull request adds exactly one completed task record;
- every newly added completed task record identifies a GitHub issue;
- task evidence is complete enough for the methodology's conclusion step;
- the pull request references the implementing issue;
- required code, test, documentation, and review checks pass.

These conditions should be checked by a tracked validation script in CI, not
only by reviewer memory.

Draft pull requests may fail the task-state check while execution is active.
The check must pass before the pull request is marked ready or merged.

Direct changes to the protected default branch should be disallowed. Normal
Git merge conflicts, required reviews, and CI remain responsible for detecting
code and documentation conflicts between parallel tasks.

Before final approval, a task branch should be updated from the intended merge
base and rerun required verification. This catches interactions introduced by
parallel work after the task began.

## 8. Rebase-Based Branch Synchronization

Task branches should incorporate changes from the remote default branch through
rebase before final pull-request approval. A `rebase-task-branch` skill should
govern this procedure.

The skill must handle both textual merge conflicts and semantic conflicts. A
clean Git rebase does not prove that the task remains behaviorally,
architecturally, or logically compatible with recent changes on the default
branch.

### 8.1 Preconditions

Before analysis or rebase, the skill should:

1. confirm the current branch belongs to the active task;
2. require a clean worktree;
3. fetch the remote default branch;
4. identify the current task-branch head and the actual merge base with the
   fetched remote branch;
5. record the target upstream commit;
6. create a temporary recovery ref or branch before rewriting commits.

The skill must not rely on a remembered branch-point commit or stale local
remote-tracking state.

### 8.2 Change Analysis

The skill should compare:

- upstream changes from the merge base to the fetched remote default branch;
- task changes from the merge base to the current task-branch head.

It should inspect both commit history and aggregate diffs. Commit messages,
completed task records, specs, tests, implementation docs, and architecture
decisions may be needed to understand why recent upstream changes were made.

The analysis should classify:

- textual conflicts;
- overlapping edits without textual conflicts;
- behavioral or logical conflicts;
- architecture-boundary conflicts;
- API, contract, schema, or migration conflicts;
- test-assumption conflicts;
- task-artifact and documentation conflicts.

### 8.3 Engineer Confirmation

If upstream changes are clearly independent from the task, the agent may
summarize that conclusion and request approval to proceed with the rebase.

If there is material overlap, the agent must first present:

- its understanding of the upstream intent;
- the current task's intent;
- the affected behavior, boundaries, contracts, tests, and documentation;
- ambiguities or missing context.

The developer confirms or corrects that understanding before resolution is
designed.

### 8.4 Reconciliation Before Rebase

For each material conflict, the agent should propose a complete conceptual
resolution:

- what each line of work intends;
- why the intentions conflict;
- the combined behavior or architecture that should result;
- which implementation elements should survive, change, or be removed;
- required changes to task scope, plan, acceptance criteria, tests, docs, or
  architecture boundaries.

The rebase must wait until the developer approves the reconciliation.

If reconciliation materially changes task scope, acceptance criteria,
architecture, or implementation design, return the task to plan assessment and
record the new approval. Do not treat such a change as mechanical conflict
resolution.

### 8.5 Rebase Execution

Apply the task commits onto the fetched remote default branch, resolving each
conflict according to the approved reconciliation.

The skill must:

- preserve the intent of both upstream work and the active task where they are
  compatible;
- avoid indiscriminate use of `--ours`, `--theirs`, or automatic whole-file
  acceptance;
- inspect each rewritten commit and the resulting branch diff;
- stop and use `git rebase --abort` when a conflict cannot be resolved from the
  approved design;
- never guess merely to complete the rebase.

### 8.6 Verification

After a successful rebase, verify both bodies of intent:

- every active-task acceptance criterion;
- upstream behavior touched by overlapping changes;
- architecture boundaries;
- APIs, contracts, schemas, and migrations where relevant;
- tests and implementation documentation for Omni-Sync;
- the final commit range and diff for accidentally dropped task changes.

Run focused checks first, followed by the applicable lint, format check,
typecheck, tests, and build commands. Tests introduced or affected by upstream
changes should run when they cover the overlap.

Material reconciliation requires another structured code-review pass even if
one ran before the rebase. Record the upstream commit, analysis, decisions,
conflict resolutions, commands, results, and residual risk in `PROGRESS.md`.

### 8.7 Push And Pull-Request State

Rebase and remote branch update are separate actions.

If the branch was already pushed, updating it requires explicit developer
approval for:

```text
git push --force-with-lease
```

Plain `--force` is prohibited. The skill should report that rebasing may
invalidate pull-request approvals and will start a new CI run. The pull request
must not be treated as ready until required checks and reviews apply to the
rebased head.

## 9. Canonicality And Drift Rules

The hybrid model intentionally divides ownership:

| Information | Canonical home |
|---|---|
| Planned task and shared status | GitHub issue |
| Open-backlog analysis cache | Local generated snapshot |
| Active detailed execution state | Branch task package |
| Completed execution evidence | Repository `done/` task package |
| Final merged/closed state | GitHub issue and pull request |
| Intended product behavior | Repository specs |
| Implemented behavior | Code, tests/contracts, and implementation docs |

Synchronization rules follow from this ownership:

- never hand-edit the generated issue snapshot;
- never infer current shared assignment from a task package alone;
- never silently overwrite active task scope from GitHub;
- never treat the snapshot as more current than its manifest;
- update the GitHub issue when shared status, dependencies, or externally
  relevant task scope changes;
- preserve detailed execution evidence in Git rather than duplicating all of it
  into issue comments.

## 10. Required Skill And Router Changes

Adopting this model would eventually require coordinated changes to:

- root and task-area `CONTEXT.md` files;
- `create-task`;
- `plan-feature-work`;
- `update-specs`;
- `planning-audit`;
- task activation and execution guidance;
- task templates;
- task completion guidance;
- repository adoption instructions.

The following bounded procedures may justify new skills or tracked tools:

- synchronize the open-issue snapshot;
- activate and materialize a GitHub issue;
- rebase a task branch onto the current remote default branch;
- validate task state before merge.

The full execution lifecycle should remain in `agent/tasks/CONTEXT.md`; GitHub
integration does not justify moving it into one oversized skill.

## 11. Failure Handling

The methodology must define failure handling explicitly:

- **Snapshot refresh fails:** stop the task-aware operation. Retain the previous
  snapshot only for diagnosis and do not use it as current task state.
- **Issue creation succeeds but the post-creation refresh fails:** report the
  created issue and stop further task-management actions until refresh succeeds.
- **Issue claim succeeds but materialization fails:** release the claim or
  record the task as blocked before stopping.
- **Repository work completes but GitHub update fails:** keep the pull request
  non-mergeable and record the failed synchronization.
- **GitHub issue changes during execution:** compare update timestamps and
  reconcile material differences before the next approval gate.
- **Cache repository identity differs from the Git remote:** reject the cache
  and stop the task-aware operation.

No failure mode should permit task-aware work to continue from stale or partial
external state.

## 12. Expected Benefits

This model provides:

- a shared team backlog and familiar collaboration interface;
- parallel task execution across isolated branches and worktrees;
- efficient local analysis without repeated ad hoc GitHub searches;
- continued use of repository-grounded task progress and evidence;
- completed task history that travels with the code;
- clear division between shared coordination and detailed execution state;
- a mechanical rule preventing active task state from entering the default
  branch.

## 13. Accepted Tradeoffs

The team version introduces unavoidable costs:

- planning operations depend on GitHub availability for fresh shared state;
- synchronization scripts and cache validation become methodology
  infrastructure;
- the issue and active task package can drift and require reconciliation;
- task claiming is no longer enforced by `CURRENT.md`;
- closed but unimplemented proposals may require GitHub history lookup;
- cross-task conflicts still require engineering judgment and normal
  pull-request integration discipline.

The local snapshot reduces query cost and improves analysis, but it does not
remove the external-system dependency. GitHub remains the shared authority for
planned tasks and team coordination.

## 14. Decisions To Resolve Before Adoption

Before implementing this variant, decide:

- the exact GitHub label and assignment convention;
- the issue body schema and whether GitHub issue forms are used;
- the cache path and serialization format;
- the synchronization implementation and authentication mechanism;
- whether comments are synchronized or accepted decisions must always be
  normalized into the issue body;
- branch and worktree naming;
- merge strategy and required branch protection;
- how cancelled or rejected issues are considered during duplicate analysis;
- whether issue status updates are mandatory at every review gate or only at
  major lifecycle transitions.

These choices should be tested on a real multi-developer workflow before this
variant replaces the current single-workstream methodology.

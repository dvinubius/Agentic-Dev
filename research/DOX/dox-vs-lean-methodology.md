# DOX vs. the Lean Agentic Development Methodology

See https://github.com/agent0ai/dox/ for DOX.

This comparison refers to an older version of Lean - parts of it may no longer apply.

## Executive conclusion

Lean and DOX can be combined, but not by copying DOX's `AGENTS.md` into the
Lean scaffold unchanged.

Their goals are strongly compatible:

- route the agent to the smallest useful context;
- keep durable repository knowledge current;
- make local constraints explicit before edits;
- prefer concise operational documentation over narrative history;
- remove stale information instead of accumulating it.

Their storage and ownership models conflict:

- Lean treats root `AGENTS.md`, root `CONTEXT.md`, and `.agent/` as replaceable,
  read-only methodology.
- DOX treats root and nested `AGENTS.md` files as mutable project
  documentation that the agent updates after meaningful changes.
- Lean assigns product intent, implemented behavior, architecture, decisions,
  planning, commands, and conventions to distinct canonical files.
- DOX's default child shape invites some of those same facts into
  `AGENTS.md`, creating competing canonical homes unless its scope is narrowed.

The useful combination is therefore **Lean with scoped local agent guides**,
not Lean plus the full DOX contract.

Under that hybrid:

1. Root `AGENTS.md` remains generic, read-only Lean methodology.
2. Nested `AGENTS.md` files are mutable project-owned routing documents at
   selected durable code boundaries.
3. Nested files contain local operational guidance and links, not product
   requirements, behavior documentation, architectural rationale, or planning.
4. `docs/repository-map.md` indexes the local guides, because Lean's root
   `AGENTS.md` cannot contain a mutable project-specific DOX index.
5. The agent reads the applicable path chain before editing and when its target
   scope expands, rather than recursively loading the whole tree.
6. The documentation closeout checks affected local guides alongside the
   existing canonical Lean documentation.

This can improve repository exploration in medium or large modular
repositories. It is most valuable when a path corresponds to a real ownership
or verification boundary and its guide saves the agent from rediscovering
local entry points, constraints, generated files, or commands.

It will not reliably improve exploration if guides are generated everywhere,
repeat global rules, duplicate `docs/`, or force a recursive documentation
walk before the agent knows the task's likely area. That version increases
attention competition and maintenance cost.

My recommendation is to adopt the constrained hybrid experimentally, with a
small number of nested guides and explicit size and ownership rules. Do not
adopt DOX verbatim.

## Sources and maturity

This analysis uses:

- the local canonical Lean explanation,
  [`lean-agentic-dev-methodology.md`](../Agentic-Methodologies/Lean-Methodology/lean-agentic-dev-methodology.md);
- the local Lean
  [`scaffold/AGENTS.md`](../Agentic-Methodologies/Lean-Methodology/scaffold/AGENTS.md),
  routers, templates, and relevant workflow and documentation skills;
- the current
  [`agent0ai/dox` README](https://github.com/agent0ai/dox/blob/main/README.md)
  and
  [`AGENTS.md`](https://github.com/agent0ai/dox/blob/main/AGENTS.md);
- OpenAI's current
  [custom instructions with `AGENTS.md`](https://developers.openai.com/codex/guides/agents-md)
  documentation.

DOX is very new. Its public repository was introduced on June 1, 2026 and had
three commits as of June 12, 2026. It contains the instruction file, README,
license, and banner, but no reference implementation, evaluation, tests, or
published measurements. Its claim to be "highly performant" should therefore
be treated as a design hypothesis, not demonstrated evidence.

That does not make its idea unsound. It means the exploration benefit should
be tested in representative repositories rather than assumed from the README.

## What Lean already does

Lean is already a routed-context methodology. Its routing model has several
layers:

- Root `AGENTS.md` establishes global workflow, approval, documentation,
  verification, and ownership rules.
- A required first-read set gives the agent a small project baseline:
  `docs/overview.md`, `docs/repository-map.md`,
  `docs/development-commands.md`, `docs/app-behavior/README.md`, root
  `CONTEXT.md`, and `.agent/config.properties`.
- Root `CONTEXT.md` routes the task by kind to specs, docs, skills, planning,
  or optional code intelligence.
- `docs/repository-map.md` and `docs/architecture/boundaries.md` route from
  repository concepts to implementation.
- `docs/app-behavior/README.md` routes to human-readable implemented behavior.
- `specs/README.md` routes to intended product behavior.
- Skills load task-specific procedures only when relevant.
- Codegraph is preferred for broad code discovery when a healthy index is
  available, with immediate fallback otherwise.
- A temporary handoff preserves active phase state without turning repository
  documentation into a work journal.

Lean also has a deliberate canonical-source model:

| Information | Canonical home |
|---|---|
| Product and business intent | `specs/` |
| Implemented behavior for humans | `docs/app-behavior/` |
| Normative architecture boundaries | `docs/architecture/boundaries.md` |
| Durable technical decisions and rationale | `docs/decisions/` |
| Stable repository paths | `docs/repository-map.md` |
| Supported development commands | `docs/development-commands.md` |
| Conventions | `docs/conventions.md` |
| Temporary development direction | `docs/planning.md` |
| Actual current behavior | Code, supported by permitted tests/contracts |
| Reusable agent procedures | Read-only `.agent/skills/` |

This separation is a major strength. It prevents a single agent instruction
file from becoming a mixture of product truth, architecture, runbooks,
temporary plans, and prompting rules.

Lean's current weakness is that routing becomes less precise below the
repository-map level. Once the agent reaches a large source area, it normally
has to discover local entry points, generated-file rules, package-specific
commands, and ownership constraints from code, general docs, or search.

DOX is aimed directly at that gap.

## What DOX adds

DOX defines a hierarchy of root and child `AGENTS.md` files.

Its operational loop is:

1. Identify the paths likely to be edited.
2. Walk from repository root to each target.
3. Read every `AGENTS.md` along those routes.
4. Treat the nearest file as the local contract and parents as broader rules.
5. After meaningful edits, update the nearest owning guide and affected
   parent or child indexes.

Its child documents use this default shape:

- Purpose
- Ownership
- Local Contracts
- Work Guidance
- Verification
- Child DOX Index

The important contribution is not another documentation category. It is
**path-addressable local context**: an agent can learn what matters for a
subtree without first reconstructing it from many unrelated files.

This aligns with native Codex instruction precedence. Codex concatenates
instruction files from the project root down to the current working directory,
and closer files override earlier guidance. The default combined project
instruction limit is 32 KiB.

There is an important qualification: Codex builds that automatic chain only
from the project root to the process's current working directory. If Codex is
started at the repository root, a nested `services/payments/AGENTS.md` is not
automatically loaded merely because the agent later edits a file there. DOX's
manual "walk to the target path" rule is therefore operationally significant,
not redundant.

## Compatibility

### Compatible principles

The two methods agree on the following:

- **Progressive disclosure:** load more specific context only when the task
  needs it.
- **Operational documentation:** tell the agent what is true and what to do,
  not how the repository reached its current state.
- **Locality:** place specific guidance near the area where it applies.
- **Current-state bias:** remove stale or contradictory text.
- **No diary:** neither method wants durable progress narration in repository
  guidance.
- **Documentation closeout:** implementation changes should trigger a focused
  check for affected documentation.
- **Hierarchy:** broad rules belong at a broad level; local details belong at a
  local level.
- **Verification awareness:** the agent should know the checks that actually
  exist for the area it changes.

These similarities are substantial enough that DOX's routing idea can fit
Lean without changing Lean's developer-control, task-handoff, verification,
specification, or decision-record models.

### Fundamental conflicts in a literal merge

#### 1. `AGENTS.md` mutability

Lean says root `AGENTS.md` is read-only methodology and only an explicit
methodology upgrade may change it. DOX says the root file holds project-wide
instructions, user preferences, and the top-level child index, and must be
updated as the project changes.

Both cannot be true of the same root file.

#### 2. Upgradeability

Lean upgrades replace root `AGENTS.md`, root `CONTEXT.md`, and `.agent/` while
preserving project state. A DOX root file containing a generated project index
and project facts would either be overwritten during upgrades or require
project-specific merge logic.

That would weaken one of Lean's clearest operational boundaries.

#### 3. Canonical information ownership

DOX asks child guides to describe purpose, ownership, contracts, work
guidance, and verification. Unqualified, those categories overlap with:

- `docs/repository-map.md`;
- `docs/architecture/boundaries.md`;
- `docs/development-commands.md`;
- `docs/conventions.md`;
- `docs/app-behavior/`;
- `specs/`;
- `docs/decisions/`.

The result could be two descriptions of the same boundary or behavior, both
claiming to be current. This is more dangerous than ordinary duplication
because `AGENTS.md` is instruction-bearing: stale duplication can change agent
behavior, not merely confuse a reader.

#### 4. Initialization scope

The uninitialized DOX file tells the agent to scan the project deeply and
recursively and create nested files where needed before continuing. Lean says
to avoid bulk-loading the repository, follow only relevant routes, keep broad
audits bounded, and prefer focused exploration.

A one-time explicit indexing task can be compatible with Lean. Making that
scan an automatic prerequisite for unrelated work is not.

#### 5. Update triggers

DOX requires a pass after every meaningful change and has broad update
categories. Lean updates documentation affected by the selected change and
keeps agent-initiated assurance focused.

The principles are compatible, but the trigger must be narrowed. Otherwise,
agents may churn multiple `AGENTS.md` files on ordinary behavior changes that
belong in `docs/app-behavior/`, specs, or decisions.

#### 6. Precedence and authority

DOX says closer files control local details, while children may not weaken
DOX. Lean has additional non-negotiable global rules around approvals,
single-writer ownership, methodology immutability, specification boundaries,
and verification.

The hybrid must explicitly state that nested guides can specialize local work
but cannot override root methodology or redefine canonical documentation
ownership.

## Effect on exploration

### Where local guides can improve exploration

A good nested guide can reduce exploration when it answers questions that are
otherwise expensive to rediscover:

- Which package or service owns this concern?
- What is the supported entry point?
- Which files are generated or vendored?
- Which internal interface must callers use?
- Which package-local command verifies a change?
- Which adjacent subtree is intentionally out of scope?
- Which canonical spec, behavior doc, boundary, or decision is relevant?
- Does this subtree contain another durable boundary with its own guide?

For a modular repository, that can reduce:

- broad `rg` or directory scans;
- reading unrelated package manifests and test configurations;
- accidental edits to generated files;
- use of the wrong verification command;
- changes through an internal implementation instead of a supported interface;
- repeated reconstruction of package boundaries in each conversation.

This is real value, especially when Codegraph is absent or when the missing
information is operational rather than symbol-graph information.

### Where DOX does not replace Lean routing

Path hierarchy and knowledge hierarchy are not the same.

A behavior may span UI, API, worker, persistence, configuration, and tests.
The relevant context cannot always be found by walking toward one target path.
Lean's topic-oriented maps remain necessary:

- specs describe intent across implementation paths;
- app-behavior docs describe end-to-end observable behavior;
- architecture boundaries describe dependency and ownership rules across
  directories;
- decisions explain why cross-cutting choices exist;
- planning captures unresolved or near-term direction.

DOX is best understood as a **last-mile path router**, not a replacement for
Lean's semantic documentation routes.

### Attention cost

The current Lean scaffold root `AGENTS.md` is about 11.8 KiB. Its required
first-read set totals about 17.5 KiB in the blank scaffold. The DOX
`AGENTS.md` is about 3.9 KiB. A literal concatenation would still fit below
Codex's default 32 KiB project-instruction limit, but the hard byte limit is
not the main concern.

The more important costs are:

- duplicated rules competing for attention;
- multiple closeout procedures expressed in different words;
- ambiguity about whether `AGENTS.md` or `docs/` owns a fact;
- an unconditional recursive indexing instruction;
- requiring the agent to predict every edited path before investigation;
- repeatedly loading parent and child text that restates global methodology.

Conversely, nested files need not enlarge the first prompt when Codex starts at
the repository root. They are loaded automatically only when the working
directory is under them, or manually when the root routing rule tells the
agent to read an applicable chain. This allows local context to be deferred.

The optimal design is therefore:

- a smaller root routing rule;
- sparse nested guides;
- no repeated global methodology in child files;
- one relevant chain at a time;
- strict size and content budgets.

### Expected net result

The likely effect by repository type is:

| Repository shape | Expected result |
|---|---|
| Small, shallow application | Little benefit; maintenance may exceed saved exploration |
| Medium modular application | Moderate benefit if guides follow real package boundaries |
| Large monorepo with distinct services/packages | High potential benefit |
| Cross-cutting task spanning many areas | Mixed; union of several guide chains can become costly |
| Rapidly changing or poorly bounded codebase | Low initial benefit; guides will drift unless boundaries stabilize |
| Repository with healthy Codegraph and strong existing maps | Incremental benefit, mainly for operational constraints and local verification |

The answer to "would it improve exploration?" is therefore conditional:

**Yes, a constrained path-local layer probably improves exploration in
repositories with durable subdomain boundaries. Literal DOX adoption probably
does not, because its duplicated authority and mandatory scanning add more
attention cost than necessary.**

## Recommended hybrid

### 1. Preserve the Lean root boundary

Keep root `AGENTS.md`, root `CONTEXT.md`, and `.agent/` read-only and
replaceable.

Add only a concise generic rule to root `AGENTS.md`, conceptually:

> Before editing project files, identify the current target area and read any
> nested `AGENTS.md` files on the route from the repository root to that area.
> Nested guides are mutable project routing documents. They may specialize
> local operational guidance but may not override this methodology or become
> canonical homes for specs, implemented behavior, architecture decisions, or
> planning. If the target expands, load the newly applicable chain before
> editing it.

The full procedure and child template should live under `.agent/`, not in the
root prompt.

### 2. Make nested guides project state

Change Lean's boundary from:

> all `AGENTS.md` files are read-only methodology

to:

> root `AGENTS.md` is read-only methodology; nested `AGENTS.md` files are
> mutable project-owned local guides.

This is the minimum conceptual change required.

The distinction must be repeated in relevant skills so agents do not either
edit the root or refuse to update an affected nested guide.

### 3. Put the index in `docs/repository-map.md`

Do not put a mutable "Child DOX Index" in root `AGENTS.md`.

Extend `docs/repository-map.md` with a compact table such as:

| Area | Local guide | Scope |
|---|---|---|
| Payments service | `services/payments/AGENTS.md` | Payments runtime, persistence, and tests |
| Web application | `apps/web/AGENTS.md` | Frontend source and browser-facing verification |

Each nested guide may index only its direct child guides.

This preserves Lean upgradeability and ensures the guide map is included in
the existing required first-read set.

### 4. Narrow the child guide's canonical role

A Lean-compatible child guide should be canonical only for:

- the subtree it covers;
- local agent work constraints;
- supported local entry points for modification;
- generated or protected paths;
- local verification commands or links to command definitions;
- direct child-guide routing;
- links to relevant canonical Lean docs.

It should not be canonical for:

- product requirements;
- user-visible behavior;
- architecture rationale;
- accepted decisions;
- temporary plans;
- task progress;
- repository-wide conventions;
- duplicated global workflow rules.

Suggested shape:

```markdown
# <Area> Agent Guide

## Scope

- Covers: `<paths and responsibility>`
- Excludes: `<adjacent ownership boundaries>`

## Local Map

| Concern | Path or entry point |
|---|---|
| `<concern>` | `<path>` |

## Work Constraints

- `<local rule that changes how an agent should work here>`

## Verification

- `<existing focused command, working directory, and prerequisite>`

## Canonical References

- Behavior: `<docs/app-behavior/... or none>`
- Architecture: `<docs/architecture/boundaries.md section>`
- Decisions: `<docs/decisions/... or none>`
- Specs: `<specs/... or none>`

## Child Guides

| Area | Guide | Scope |
|---|---|---|
| `<child>` | `<path>/AGENTS.md` | `<scope>` |
```

Empty sections should be omitted rather than retained as placeholders. The
goal is high signal, not uniform bulk.

### 5. Create guides sparsely

Create a nested guide only when the directory is a durable boundary and at
least one of these is true:

- it has distinct ownership or dependency rules;
- it has a distinct supported verification workflow;
- it contains generated, vendored, migration, infrastructure, or security
  constraints;
- it has several stable entry points that agents repeatedly need to locate;
- it contains child boundaries that need routing;
- repeated task evidence shows agents over-explore or edit the wrong surface.

Do not create a guide:

- for every directory;
- solely because a directory exists;
- to restate file names visible from a listing;
- for a temporary feature branch structure;
- when `docs/repository-map.md` already provides enough routing;
- before a boundary is stable enough to document.

A practical initial ceiling is one guide per major application, service,
package family, or infrastructure area, then add deeper guides only from
observed need.

### 6. Use two-stage discovery

DOX's instruction to identify every file expected to change before reading
local guidance is too strict. Agents often need limited exploration to know
the target.

Use:

1. Read Lean's required first-level project context.
2. Form a likely target area from the request, repository map, and focused
   search or Codegraph.
3. Read the applicable nested guide chain before the first edit.
4. If exploration expands the scope, read the additional chain before editing
   that area.

This preserves local safety without forcing a broad up-front scan.

### 7. Integrate closeout without duplicating it

Do not add a separate DOX closeout workflow beside `finish-change` and
`ensure-docs-current`.

Instead, extend `ensure-docs-current` to ask:

- Did the change alter the scope, entry points, local constraints,
  verification, protected paths, or child-guide index of an affected subtree?
- If yes, update the nearest applicable nested guide.
- If no, report that applicable local guides were checked and did not need an
  update only when that information is useful.

Behavior changes still update `docs/app-behavior/`, not a child guide.
Architecture changes still update `docs/architecture/boundaries.md` and
possibly decisions. Command changes still update
`docs/development-commands.md`; a child guide may link to or summarize the
area-specific invocation when it materially helps local work.

### 8. Add anti-drift validation

The methodology's validation should check:

- root `AGENTS.md` remains project-agnostic;
- every indexed nested guide exists;
- every nested guide's declared scope matches its path;
- parent child-guide indexes are current;
- nested guides do not contain product requirements, planning state, or
  implemented-behavior narratives;
- nested guides do not weaken root methodology;
- local verification commands exist in the supported toolchain;
- no guide repeats large global rule blocks;
- guides remain within an agreed size budget.

A soft budget of roughly 1-2 KiB per nested guide is a reasonable starting
point. A larger guide should justify why its content is not better owned by a
canonical document or skill.

## What not to adopt from DOX

Do not adopt these parts unchanged:

- replacing the Lean root `AGENTS.md`;
- storing the mutable project index in the root methodology file;
- recursively scanning the whole repository as a prerequisite for normal work;
- creating nested guides "deep" by default;
- treating all durable repository knowledge as understandable from the
  `AGENTS.md` chain alone;
- recording durable user behavior preferences in `AGENTS.md` when they are
  product intent, conventions, configuration, or methodology choices;
- updating `AGENTS.md` for every meaningful behavior change;
- allowing a closer guide to override global Lean governance;
- using the child guide as another architecture or app-behavior document.

These are the areas where literal adoption would make Lean less coherent.

## Evaluation plan

The exploration benefit should be measured with representative tasks before
making the hybrid a default scaffold feature.

### Trial setup

Choose one medium or large repository and add three to six guides at real
boundaries. Avoid changing application code during guide creation. Run matched
tasks with:

- baseline Lean routing;
- Lean plus the constrained local-guide layer.

Include:

- one narrow change within a single package;
- one bug whose cause is not at the initially reported symptom;
- one change involving generated or protected files;
- one task with package-specific verification;
- one cross-cutting change spanning two or more guide chains.

### Measures

Record:

- files read before the first credible implementation plan;
- tool calls used for discovery;
- approximate input/context volume;
- irrelevant files read;
- whether the correct entry point was found initially;
- whether generated or internal-only files were edited accidentally;
- whether the correct focused verification command was selected;
- corrections requested by the developer;
- documentation files changed;
- stale or duplicated claims introduced;
- completion quality and elapsed interaction turns.

### Success criteria

Keep the hybrid if it produces a material reduction in irrelevant exploration
or wrong-surface edits without increasing:

- first-turn instruction confusion;
- duplicated documentation;
- routine documentation churn;
- missed cross-cutting dependencies;
- total context on multi-area tasks.

The most meaningful signal is not whether agents report liking the guides. It
is whether they reach the correct implementation and verification surface with
less irrelevant reading and fewer corrections.

## Final answers

### Can Lean and DOX be combined?

Yes, at the level of path-local routing and scoped operational guidance.

No, not literally. Their root `AGENTS.md` ownership, mutability, upgrade, and
canonical-document models conflict. Combining them requires keeping Lean's
root methodology boundary and redefining nested `AGENTS.md` files as narrowly
scoped mutable project guides.

### Would the combination improve agent exploration?

Probably, for modular repositories, if the nested guides are sparse, concise,
target-loaded, and subordinate to Lean's canonical docs.

The benefit comes from reducing last-mile discovery inside a known area. It
does not come from adding the full DOX text to the initial prompt.

A literal combination would likely make exploration worse by increasing
instruction duplication, document-authority ambiguity, and mandatory scanning.
The constrained hybrid can improve exploration precisely because most of its
additional context remains out of the first prompt and is loaded only for the
subtree being changed.

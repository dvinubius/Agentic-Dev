# Agent Skills

Skills are targeted reusable procedures. Governing rules and routing remain in
root and area `CONTEXT.md` files.

Skills may be used when suitable during planning work, task execution, or
complementary work.

This directory is the repository-owned canonical source. Each `SKILL.md` uses
Codex-compatible `name` and `description` frontmatter. Routing through this
file makes the skills available to the methodology; native Codex implicit
discovery additionally requires installing or linking them into a supported
`.agents/skills/` location.

## Invocation Modes

An agent uses a skill in one of three ways:

- **Workflow-required**: a governing `CONTEXT.md` defines objective trigger
  conditions. When they apply, read and follow the named `SKILL.md`.
- **Engineer-requested**: the engineer explicitly asks for the skill. Read and
  follow it unless doing so conflicts with an active task or another governing
  rule.
- **Agent-proposed**: the agent identifies a likely benefit not covered by a
  required trigger. Explain the reason and ask before running the skill.

Merely knowing that a skill exists does not mean it should run. When a skill is
selected, "use the skill" means reading its `SKILL.md`, following its procedure
and guardrails, and recording the required output or evidence.

## Skill Self-Containment

A skill may be invoked directly, selected from its frontmatter description, or
reused without the agent first reading root methodology files. Therefore, every
skill must contain the minimum context required to execute it correctly.

When creating or updating a skill:

- define nonstandard methodology terms used by its procedure;
- state required work-state checks and relevant artifact paths;
- explain exclusions that materially change the result;
- link required references and say when to read them;
- if the skill can pause for engineer input, require the response to end with
  the explicit question as a separate final paragraph, with no text after it;
- do not assume root `CONTEXT.md` or another skill was read first.
- if a required methodology artifact is absent, report the missing dependency
  and ask for direction rather than guessing its replacement.

Brief duplication is preferable to forcing the agent to guess. Keep the full
methodology canonical in its normal files, but repeat the minimum operational
definition inside the skill.

## Preconditions

- Read `../tasks/CURRENT.md`.
- If a task is active, use a skill only in service of that task.
- Do not use a skill to start unrelated planning or complementary work while a
  task is active.
- Skills are diagnosis-only by default unless their procedure explicitly
  includes approved edits.

## Routing

| Need | Skill |
|---|---|
| Change current product or business specifications | `update-specs/SKILL.md` |
| Map broad specs and material stack capabilities into ordered candidate task slices | `plan-feature-work/SKILL.md` |
| Create a formal feature, issue-fix, or refactoring task | `create-task/SKILL.md` |
| Check deprecated tasks, missed specs, implementation of a spec, or multitasking | `planning-audit/SKILL.md` |
| Check consistency among implemented behavior, tests/contracts, code, and docs | `drift-audit/SKILL.md` |
| Improve clarity and structure of current application docs | `docs-refinement/SKILL.md` |
| Create or refresh the concise root project README | `update-readme/SKILL.md` |
| Clarify and stress-test a plan against shared domain language, decisions, docs, and code | `clarify-with-shared-language/SKILL.md` |
| Find opportunities to consolidate shallow modules into deeper modules | `improve-codebase-architecture/SKILL.md` |
| Review a task diff for substantive problems | `code-review/SKILL.md` |

Add skills only after a procedure proves reusable. Remove skills that no longer
produce useful, distinct behavior.

See `THIRD_PARTY_NOTICES.md` for adapted skill sources and licenses.

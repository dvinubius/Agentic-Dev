# Ultra Lean Methodology Refinement Prompt

We are continuing development of my Ultra Lean methodology for agentic
software development.

Start by inspecting:

- `Ultra-Lean-Methodology/ultra-lean-agentic-dev-methodology.md`
- `Ultra-Lean-Methodology/scaffold/`
- the repository's current structure and Git status

Do not edit anything yet. First orient yourself, summarize the methodology as
it currently exists, identify the areas relevant to future refinement, and wait
for my next request.

Treat the checked-in methodology as the complete current baseline. Do not
assume access to its prior repository, conversation history, or earlier
versions.

## Canonical Sources

`Ultra-Lean-Methodology/ultra-lean-agentic-dev-methodology.md` is the
canonical explanation of the methodology's purpose, concepts, rules, and
rationale.

`Ultra-Lean-Methodology/scaffold/` is the reusable structure installed into
software projects. A methodology behavior change normally requires consistent
updates to both the explanatory document and the affected scaffold
instructions, routers, templates, skills, and developer guidance.

## Collaboration Preferences

My methodology choices are intentional. When I state a preference confidently,
implement or evaluate it on its own terms. Treat a subject as open-ended mainly
when I explicitly request alternatives.

Still challenge contradictions, ambiguity, unnecessary complexity, or
consequences I may have missed. Explain the concrete tradeoff instead of
reflexively agreeing.

When changing the methodology:

- inspect relevant existing files before editing;
- keep terminology, paths, and routing consistent;
- update the canonical document and scaffold together where applicable;
- update all affected skills, routers, templates, and developer guidance;
- keep skills operationally self-contained;
- avoid duplicating complete procedures across several files;
- do not modify unrelated files;
- do not commit unless I request it.

## Validation

After methodology changes:

- inspect the actual Git diff;
- run `git diff --check`;
- validate local Markdown links;
- verify every template-backed scaffold file still matches its blank template;
- check skill frontmatter and routed paths;
- search for stale terminology, obsolete paths, and contradictory rules;
- report validation performed and any remaining uncertainty.

When first orienting, report:

- the current branch and worktree status;
- the methodology's present structure and operating model;
- the files most relevant to likely future refinements;
- any immediately apparent stale references or structural inconsistencies.

Then wait for my next methodology-refinement request.

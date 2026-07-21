# AGENTS.md

Instructions for AI coding agents working with this codebase.

## Branch and PR Workflow

Use `staging` as the integration branch for feature work.

- Create feature branches from the latest `staging`, preferably in isolated worktrees under `.worktrees/<branch-name>`.
- Open small, focused PRs from each feature branch into `staging`.
- Do not merge unrelated feature work into another feature branch unless the PR is intentionally stacked and the dependency is real.
- Keep PRs reviewable for code review agents: split by feature, ownership boundary, or behavioral surface rather than accumulating a large mixed diff.
- After a feature PR merges into `staging`, update any active feature branches from `staging` before continuing work.
- Promote `staging` to `main` only when the integrated set of changes is ready for release.

## Source Code Reference

Source code for dependencies is available in `opensrc/` for deeper understanding of implementation details.

See `opensrc/sources.json` for the list of available packages and their versions.

Use this source code when you need to understand how a package works.

## Fetching Additional Source Code

To fetch source code for a package or repository you need to run:

```sh
npx opensrc <package>           # npm package (e.g. react)
npx opensrc pypi:<package>      # Python package (e.g. requests)
npx opensrc crates:<package>    # Rust crate (e.g. serde)
npx opensrc <owner>/<repo>      # GitHub repo (e.g. facebook/react)
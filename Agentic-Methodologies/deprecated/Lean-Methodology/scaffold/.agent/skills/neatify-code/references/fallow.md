# Fallow Reference

Use this reference when `neatify-code` runs on a JavaScript or TypeScript
project and Fallow is already available or explicitly approved for use.

Authoritative source: https://github.com/fallow-rs/fallow

## What Fallow Provides

Fallow is codebase intelligence for JavaScript and TypeScript. Use it for
deterministic evidence about changed-code risk, hotspots, duplication,
complexity, architecture issues, dependency hygiene, and cleanup opportunities.

Treat findings as evidence for triage, not automatic edit instructions.

## Command Selection

Prefer the narrowest useful command:

- changed-code audit: `fallow audit --format json`
- quality scoring and refactor targets: `fallow health --score --hotspots --targets`
- cleanup-specific findings: `fallow dead-code --format json`
- duplication findings: `fallow dupes --format json`

`fallow dupes --format json` uses the Fallow CLI's `--format <FORMAT>` option
with `json`. In grouped JSON output, duplication findings are structured under
fields such as `grouped_by`, `groups`, `clone_groups`, and `clone_families`.

If only a package-manager wrapper is available, use the repository's package
manager command for the already-installed dependency, such as:

- `npm exec fallow -- audit --format json`
- `npm exec fallow -- dupes --format json`
- `pnpm exec fallow audit --format json`
- `pnpm exec fallow dupes --format json`
- `yarn fallow audit --format json`
- `yarn fallow dupes --format json`
- `bunx --bun fallow audit --format json`
- `bunx --bun fallow dupes --format json`

Do not use `npx fallow` or another command that may fetch packages unless the
developer approves the dependency addition and the selected package version
satisfies the repository package-installation policy.

## Interpreting Findings

Common legitimate exceptions include:

- duplicated fixture, test, or configuration setup;
- high-complexity code that is clearer as a single context-heavy flow;
- generated, vendored, framework-convention, or compatibility code;
- intentionally public exports used by external consumers outside static
  reachability.

Escalate accepted recurring exceptions to `docs/conventions.md`; use an ADR
only when the exception is a durable architectural choice whose rationale will
matter later.

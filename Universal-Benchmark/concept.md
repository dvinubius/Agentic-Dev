# Universal Benchmark

## Goal 

The goal is to have a setup for benchmarking models on realistic development tasks on full stack web apps.

The setup should be automated as much as possible, requiring the engineer only for parts that are typically best assessed by a human.

The setup should allow comparing model performance based on different scenarios and work styles (low/high spec, test-first/code-first).

The setup should automate the reporting as much as possible for swift publishing.

## Setup

2 competing models. Frontier & medium-high thinking.

Small scope, AFK execution

3 Setups:

- greenfield low-spec: brief & superficial specs (trust the model in the gaps)
- greenfield high-spec: Specs in a PRD, relatively detailed; include mockups
- brownfield high-spec: Specs in a PRD, relatively detailed; include mockups

Per setup:
2 execution styles for each setup: 
- test first (TDD)
- code first

Set up feedback on finished-hook: bash script performing
- formatting
- linting
- fallow
Script should output a prompt - continue to PR & watch the workflow
Github workflow on PR
- sonar

Levels of reporting
- LEVEL 0: per setup, code first / test first
- LEVEL 1: compare LEVEL 0 for harness A / B
- LEVEL 2: aggregate LEVEL 1 for setup X / Y / Z

### A single setup run (SSR)

Wrap the 2 execution styles as runs in a single agent task
1. to be executed using subagents
2. to be evaluated using the token-police parser
3. to leave locally served apps for me to try out and manually QA
4. to take my manual QA response and make it part of the report
5. create an `.md` report comparing TDD vs code-first  (LEVEL 0 reporting)

### Compose & Automate. Comparative SRR (CSSR)

For one specific setup.

Trigger in parallel for Codex & once for CC.
- trigger once with `claude --p`  and `codex exec`  with a prompt for the steps 1-3.
- I write my review in a dedicated file for each agent.
- trigger again with a prompt for steps 4. and 5. 
- Create an `.md` report comparing the 2 models (LEVEL 1 reporting)
- Explain visually & export as pdf

### Aggregate multiple setups. (AGG)

If multiple setups are defined, perform CSSR on multiple setups

- run CSSR for multiple setups (brownfield, greenfield low-spec, greenfield high-spec)
- combine 3 CSSR reports into a single master `.md` report (LEVEL 2 reporting)
  - executive summary, refer to LEVEL 1 reports (links to blog page and pdf hosted on my website)
  - host executive summary as dedicated blog page and downloadable pdf

If only a single setup is defined, we stay at LEVEL 1

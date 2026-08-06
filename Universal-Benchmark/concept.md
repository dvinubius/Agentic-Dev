# Universal Benchmark

## Goal 

The goal is to have a setup for benchmarking models on realistic development tasks on full stack web apps.

The setup should be automated as much as possible, requiring the engineer only for parts that are typically best assessed by a human.

The setup should allow comparing model performance based on different scenarios and work styles (low/high spec, test-first/code-first).

The setup should automate the reporting as much as possible for swift publishing.

## Setup

2 competing models, only worth doing for frontier models & medium-high effort.

Aim for Small scope, AFK execution

3 project scenarios (types of **tasks**):
- greenfield low-spec: brief & superficial specs (trust the model in the gaps)
- greenfield high-spec: Specs in a PRD, relatively detailed; include mockups
- brownfield high-spec: Specs in a PRD, relatively detailed; include mockups

The project tasks definition requires real work. Project must be adequate (full stack),
task scope must be adequate. This is probably something every developer should
define based on personal needs. Specs also have to be proper and the developer should
be familiar with them, so that he or she can assess the agent's work. Especially for
high-spec greenfield projects this can mean a lot of work.

Per Run:
2 execution styles for each task run:
- test first (TDD)
- code first

Set up feedback on finished hook: hard gate, deterministic. A bash script performs
- formatting
- linting
- fallow
and prompts the agent to fix unless output is free of errors.

By performing these runs, reports are generated at different levels.

Levels of reporting
- LEVEL 0: per setup, code first / test first
- LEVEL 1: compare LEVEL 0 for harness A / B
- LEVEL 2: aggregate LEVEL 1 for setup X / Y / Z

### A single task run (STR)

Wrap the 2 execution styles (TDD vs code-first) as runs in a single agent task
1. to be executed using subagents
2. to be evaluated using the token-police parser
3. to open locally served apps for me to try out and manually QA
4. to take my manual QA response and make it part of the report
5. create an `.md` report comparing execution styles (LEVEL 0 reporting)


### Compose & Automate. Comparative SRR (CSTR)

For one specific task.

Trigger an agent to run this in parallel for Codex & once for CC.
- trigger once with `claude --p`  and `codex exec`  with a prompt for the steps 1-3.
- I write my review in a dedicated file for each agent.
- trigger again with a prompt for steps 4. and 5. 
- Create an `.md` report comparing the 2 models (LEVEL 1 reporting)
- Explain visually & export as pdf

### Aggregate multiple runs. (AMR)

If multiple tasks are defined, perform CSTR on multiple tasks

- trigger CSTR for multiple tasks (brownfield, greenfield low-spec, greenfield high-spec)
- Aggregation agent prompt: combine 3 CSTR reports into a single master `.md` report (LEVEL 2 reporting)
  - executive summary, refer to LEVEL 1 reports (links to blog page and pdf hosted on my website)
  - host executive summary as dedicated blog page and downloadable pdf

If only a single setup is defined, we're done at LEVEL 1


### Further agentification
For the sake of clarity, in this bench draft this part is not packaged as an agent guided workflow. But it could be. The agent would ask which scenarios are relevant to the dev, and further execute LEVEL 1 triggers on its own, while asking the developer to intervene whenever a LEVEL 0 review is expected.

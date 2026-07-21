# Ralph Loop For Next

A method of executing multi step tasks with a ralph loop by
- having a plan for the entire task execution, broken up in subtasks
- making the prompt refer to a target that keeps changing, i.e. "the next subtask to take given the current state"
- persisting state which allows the agent in any interation to infer which is the next subtask to take

## Josh Morony approach to a complete workflow

Prep: instruct CC to research ralph loops and set up the generic mechanism (as a skill?). This one defines:
- nomenclature (task, subtasks)  - "tracks" & "phases"
- main agent role - the smart one; its purpose is to plan & design a track & phases, not handle implementations
- ralph agents role
- bash loop & prompt
- persistence across subtasks



1. Spec & Plan: start a main agent, show it previous PRs for best prep on what needs to be tackled next
2. Ralph Loop

The loop setup:
- Bash script based loop
- Persisted task progress
- First ralph opens pr, takes subtask 1
- Last ralph ensures quality gates pass (only this one?) - typescript compiles, tests pass, specific quality gates decided during planning
- Main agent is manually prompted to review at the end & fixes on its own
- Engineer reviews PR (comments), then invokes ralph-loop for PR handling:
  - if LGTM, it's good to merge
  - if not, ralph fixes what needs to be fixed

Morony works with worktrees (potentially parallelizing). First ralph creates a worktree too.
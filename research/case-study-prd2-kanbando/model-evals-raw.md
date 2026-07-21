## Task: PRD 2

This refers to `PRD-2.md` from kanbando, see that one for the full PRD.

Runs were performed in the interval **Jun 20 2026 - Jun 21 2026**.

### PRD Solution Section
Deliver the full lifecycle of a **personal todo** (a todo with no candidates,
visible only to its creator) on the three fixed lanes — **New**, **In
Progress**, **Done**. A user can create a todo, see it on the board, drag it
between lanes (lane = status) and reorder it within a lane, open its detail,
edit its brief (with the original preserved), and delete it. Collaboration,
deadlines, thumbnails, notes, outcome, archiving, and notifications are out of
scope this iteration and build on top of this slice later.


### Run 1 - CC Opus 4.8 High, AFK with 5 issues but no subagents

❗️ Model decided to execute directly on 5 issues. 
"I never spawned subagents during this task (the PRD allowed them, but the dependencies between slices made inline work cleaner)"

exhausted 90% of 5h quota, ~63M tokens, 280 LLM calls; context: ~360K

PRD mostly satisfied, 1 bug not caught by any review

Had a new agent review it with `code-review` and it caught the issue, but didn't see it as a true bug. It would have merged if left to decide on its own.

### Run 2 - Codex GPT 5.5 Medium, AFK with 5 issues but no subagents

❗️ Model decided to execute directly on 5 issues.

"the issues were tightly coupled across the same files: shared types, schema, service/routes, API client, board state, and UI. Running write-capable subagents serially would not have reduced latency meaningfully. I should have called that out explicitly since execute-prd-afk says to use subagents when they reduce risk or latency."

exhausted 40% of 5h quota; ~9M tokens, 104 LLM calls; context: ~140K

PRD statisfied, no bugs. **DnD visually underwhelming** but it works.


### Run 3 - CC Opus 4.8 High, AFK with 5 issues and subagents

explicit subagent instruction needed in prompt

exhausted 5h quota, 368 LLM calls; 38M tokens; context: ~85K

issue 5 almost complete (verification stage) - but board was not functional

continuing in new 5h window - took 10% more of the quota; 390 LLM calls, 40M tokens, context ~112K

❗️ Agent did not run test explicitly assigned to it the PRD ("create → New; drag…; reload to confirm persistence") claiming that it deffered it.

UI/UX is better than with codex medium


### Run 4 - CC Opus 4.8 Medium, AFK with 5 issues, direct execution

exhausted 88% of 5h quota, 273 LLM calls, 66M tokens; context ~370K

completed work, everything works, decent UI


### Run 5 - CC Opus 4.8 Medium, AFK with 5 issues and subagentss

exhausted 5h quota, ~40M tokens, 422 LLM calls; context: ~82K

progress: last issue completed by subagent

PRD satisfied, no bugs



### Run 6 - Codex GPT 5.5 Medium, AFK with 5 issues and subagents

explicit subagent instruction needed in prompt

used 42% of 5h quota, 86 LLM calls, 6.5M tokens, context ~145K

PRD satisfied. UI is underwhelming, amateurish. DnD still amateurish.


### Run 7 - CC Opus 4.8 Medium, AFK with no issues, direct execution

Custom prompt: execute directly, plan as you see fit. Issues removed, only PRD remains.

used 42% of 5h quota, 128 LLM calls, 20M tokens; 219K context

PRD satisfied. UI is nicer than on issue-based executed, but small improvements are necessary.

used 52% of 5h quota for completion w/ fix. 149 LLM calls, 25M tokens, 250K context

The LLM claims the cause of the UI slip is that it didn't stick to the suggested tracer bullets but implemented horizontally.

It only created 1 commit.

Made it much more efficient, but resulted in a small UI issue.

### Run 8 - Codex GPT 5.5 Medium, AFK with no issues, direct execution

Custom prompt: execute directly, plan as you see fit. Issues removed, only PRD remains.

used 40% of 5h quota, 90 LLM calls, 9M tokens, ~145K context

PRD satisfied, fully functional; UI underwhelming, amateurish.
But DnD looks better than codex medium issues based direct execution and codex medium issues based subagents execution.
Those both had a poor DnD implementation. Functional but poor.

It followed the tracer bullets conceptually, but not as separate issue-sized commits

### Run 9 - CC Opus 4.8 High, AFK with no issues & direct execution

Custom prompt: execute directly, plan as you see fit. Issues removed, only PRD remains.

used 53% of 5h quota, 225 LLM calls, 41M tokens, ~280K context


PRD satisfied, fully functional, great UI.
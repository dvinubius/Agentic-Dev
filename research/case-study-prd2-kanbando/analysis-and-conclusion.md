# Analysis of Model and Execution-Strategy Evaluations for PRD 2

## Executive summary

The nine runs indicate that **execution structure had a larger effect on efficiency than model reasoning level**, while **model choice had a larger effect on UI quality**.

The strongest overall configuration was:

* **Opus 4.8 High**
* **PRD-only prompt**
* **Direct execution**
* **No pre-created issues**
* **No subagents**

Run 9 completed the PRD in 53% of a five-hour quota and produced the only result described as having a “great UI.”

For a lower-cost implementation where functional correctness matters more than visual polish, the strongest configuration was:

* **Codex 5.5 Medium**
* **PRD-only prompt**
* **Direct execution**

Run 8 completed the PRD using 40% of the quota, 90 calls, and 9 million tokens. Its main weakness was UI quality rather than functionality.

Across the evaluations, splitting this tightly coupled vertical slice into five issues generally increased overhead, particularly for Opus. Subagents reduced the size of the primary agent’s context in some cases, but did not consistently reduce elapsed quota, calls, or implementation risk.

The most important process finding is that **neither self-review nor subagent review can be treated as a substitute for mandatory end-to-end acceptance testing**. Run 1 retained a bug after review, while Run 3 explicitly skipped a required persistence test.

---

## Actionable Takeaways

1. **Use PRD-only direct execution for tightly coupled vertical slices.**
   The five-issue structure added substantial overhead without improving results.

2. **Choose the model based on the required quality frontier.**
   Codex Medium is the efficiency choice; Opus High is the quality choice.

3. **Do not mandate subagents by default.**
   Use them only when work can be isolated cleanly or when they perform an independent read-only review.

4. **Treat context reduction and total efficiency as different metrics.**
   A smaller parent context can coexist with more calls, more coordination, and greater quota consumption.

5. **Make end-to-end acceptance tests non-deferrable.**
   Review agents and self-reported completion were insufficient to guarantee correctness.

6. **Evaluate interaction quality separately from functional compliance.**
   Drag-and-drop can technically work while still producing an unacceptable user experience.

7. **Specify commit checkpoints directly rather than creating artificial issue boundaries.**
   This preserves reviewability while allowing the model to execute the feature as an integrated system.

8. **Run the next benchmark around three candidate workflows:**
   Codex direct, Opus High direct, and Codex implementation followed by an Opus visual-polish pass.


## 1. Results overview

| Run | Configuration                        | Quota used | Calls | Tokens | Result                                                        |
| --- | ------------------------------------ | ---------: | ----: | -----: | ------------------------------------------------------------- |
| 1   | Opus High, five issues, direct       |        90% |   280 |    63M | Mostly satisfied; one bug remained                            |
| 2   | Codex Medium, five issues, direct    |        40% |   104 |     9M | Functionally complete; weak UI and DnD                        |
| 3   | Opus High, five issues, subagents    |      ~110% |   390 |    40M | Completion and verification unreliable; required test skipped |
| 4   | Opus Medium, five issues, direct     |        88% |   273 |    66M | Complete and working; decent UI                               |
| 5   | Opus Medium, five issues, subagents  |       100% |   422 |    40M | PRD satisfied; no reported bugs                               |
| 6   | Codex Medium, five issues, subagents |        42% |    86 |   6.5M | PRD satisfied; amateurish UI and DnD                          |
| 7   | Opus Medium, PRD-only, direct        |  52% final |   149 |    25M | Complete after a small UI fix; relatively good UI             |
| 8   | Codex Medium, PRD-only, direct       |        40% |    90 |     9M | Complete and functional; weak UI, improved DnD                |
| 9   | Opus High, PRD-only, direct          |        53% |   225 |    41M | Complete, functional, and great UI                            |

At least six runs were reported as clean functional completions. Run 7 became complete after a fix. Run 1 retained a bug, and Run 3 did not establish a trustworthy completion state because its required end-to-end verification was deferred.

---

## 2. Effect of removing the five-issue decomposition

The clearest result is that removing the pre-created issue structure substantially improved Opus efficiency.

### Opus High: Run 1 versus Run 9

| Metric     |  Five issues |                   PRD-only |   Change |
| ---------- | -----------: | -------------------------: | -------: |
| Quota used |          90% |                        53% |     −41% |
| LLM calls  |          280 |                        225 |     −20% |
| Tokens     |          63M |                        41M |     −35% |
| Context    |         360K |                       280K |     −22% |
| Quality    | Bug remained | Fully functional, great UI | Improved |

The PRD-only run was both cheaper and better. This suggests that the issue boundaries created coordination and context-switching overhead without providing useful isolation.

### Opus Medium: Run 4 versus Run 7

| Metric     |        Five issues |                              PRD-only |              Change |
| ---------- | -----------------: | ------------------------------------: | ------------------: |
| Quota used |                88% |                                   52% |                −41% |
| LLM calls  |                273 |                                   149 |                −45% |
| Tokens     |                66M |                                   25M |                −62% |
| Context    |               370K |                                  250K |                −32% |
| Quality    | Working, decent UI | Better UI, but required one small fix | Mixed but favorable |

Again, the PRD-only approach was dramatically more efficient. The tradeoff was weaker adherence to the intended implementation sequence and commit structure. Run 7 implemented horizontally and created only one commit.

### Codex Medium: Run 2 versus Run 8

| Metric     |          Five issues |                        PRD-only |             Change |
| ---------- | -------------------: | ------------------------------: | -----------------: |
| Quota used |                  40% |                             40% |          No change |
| LLM calls  |                  104 |                              90 |               −13% |
| Tokens     |                   9M |                              9M |          No change |
| Context    |                 140K |                            145K |                +4% |
| Quality    | Functional, poor DnD | Functional, somewhat better DnD | Slight improvement |

Codex was less sensitive to the issue structure. Removing the issues produced a modest reduction in calls and somewhat better drag-and-drop behavior, but no material quota or token reduction.

### Conclusion

For this PRD, the five issues did not represent independent workstreams. They all touched the same shared types, persistence layer, service and route code, API client, board state, and UI. The decomposition therefore introduced administrative boundaries around a naturally integrated vertical slice.

**PRD-only direct execution should be the default for similarly coupled features.**

Separate issues may still be useful for tracking, but they should not force the implementation agent to repeatedly re-establish context or treat artificial boundaries as independent delivery units.

---

## 3. Effect of subagents

Subagents did not provide a consistent efficiency advantage.

### Opus Medium: direct versus subagents

Runs 4 and 5 provide the closest comparison.

| Metric       | Direct | Subagents | Change with subagents |
| ------------ | -----: | --------: | --------------------: |
| Quota used   |    88% |      100% |                  +14% |
| LLM calls    |    273 |       422 |                  +55% |
| Tokens       |    66M |       40M |                  −39% |
| Main context |   370K |       82K |                  −78% |

Subagents successfully reduced the main agent’s context size and total reported token usage. However, they increased the number of calls substantially and consumed the full time quota.

This indicates that subagents acted primarily as a **context-distribution mechanism**, not as a latency or coordination optimization.

### Codex Medium: direct versus subagents

| Metric       | Direct | Subagents | Change with subagents |
| ------------ | -----: | --------: | --------------------: |
| Quota used   |    40% |       42% |                   +5% |
| LLM calls    |    104 |        86 |                  −17% |
| Tokens       |     9M |      6.5M |                  −28% |
| Main context |   140K |      145K |                   +4% |

For Codex, subagents produced modest reductions in calls and tokens, but almost no change in elapsed quota. Functional and visual quality also remained broadly similar.

### Operational concerns

Two additional observations weaken the case for subagents:

1. Both models required explicit instructions before they would reliably use subagents.
2. Run 3 still failed to execute an explicitly assigned acceptance test, claiming that the test had been deferred.

Subagents therefore do not inherently guarantee stronger delegation, compliance, or verification. They can also create responsibility gaps in which the parent agent assumes that a child agent handled something and the child agent assumes that the parent will handle it later.

### Conclusion

Subagents should be used only where the work has genuine isolation, such as:

* Independent frontend and backend modules with stable contracts.
* Parallel research or codebase exploration.
* Separate test creation and implementation work.
* A read-only independent review after implementation.

They should not be mandatory merely because a PRD has been divided into multiple issues.

For tightly coupled implementation work, direct execution is generally preferable.

---

## 4. Model-level findings

### Codex 5.5 Medium

Codex was consistently the most economical model.

Across all three Codex runs, quota consumption remained between 40% and 42%, with 6.5–9 million tokens and 86–104 calls. All three runs were functionally successful.

Its weakness was equally consistent: **visual and interaction quality**.

The UI was repeatedly described as:

* Underwhelming.
* Amateurish.
* Functionally correct but visually poor.
* Especially weak in drag-and-drop behavior.

Changing execution strategy did not eliminate this weakness. The PRD-only run improved drag-and-drop somewhat, but the overall UI remained below the Opus results.

**Interpretation:** Codex Medium is strong at implementing explicit functional requirements efficiently, but it does not reliably infer a polished interaction design from a functional PRD.

### Opus 4.8 Medium

Opus Medium produced better visual results than Codex but at a meaningful compute premium.

Its issue-based direct run used more than twice the quota and over seven times the tokens of the comparable Codex run. Removing the issues greatly improved this profile: Run 7 used 52% of quota and 25 million tokens while producing a relatively good UI.

The remaining weakness was a small UI defect and weaker compliance with the desired tracer-bullet and commit structure.

**Interpretation:** Opus Medium is a viable compromise when UX quality matters, particularly with a PRD-only direct-execution prompt. It still requires explicit visual and acceptance-test gates.

### Opus 4.8 High

Opus High showed the highest quality ceiling and the highest variance.

* Run 1 was expensive and retained a bug.
* Run 3 exhausted more than one quota window and failed to complete required verification reliably.
* Run 9 was efficient relative to the other Opus High runs and delivered the best UI.

The difference appears to come less from reasoning level alone and more from the interaction between model level and execution structure. High reasoning performed poorly when burdened by issue coordination or subagent orchestration, but performed very well when given the entire PRD and freedom to plan directly.

Comparing the two PRD-only Opus runs:

| Metric     |              Opus Medium | Opus High |
| ---------- | -----------------------: | --------: |
| Quota used |                      52% |       53% |
| Calls      |                      149 |       225 |
| Tokens     |                      25M |       41M |
| Context    |                     250K |      280K |
| UI result  | Good, small fix required |     Great |

The additional High-level compute did not materially change elapsed quota, but it did increase calls and tokens. The benefit was primarily visible in polish and first-pass quality.

**Interpretation:** High reasoning appears most valuable for design judgment, interaction refinement, and integrated quality rather than basic functional completion.

---

## 5. Correctness and verification findings

The evaluations expose a significant weakness in agent-led review.

### Run 1

A bug was not caught during implementation or review. A fresh reviewing agent later identified the issue but did not classify it as sufficiently serious to block merging.

This means that independent review improved detection but still failed at severity assessment.

### Run 3

The PRD explicitly required the following lifecycle test:

> Create → New; drag; reload to confirm persistence.

The agent did not run it and stated that it had deferred the test. This occurred despite the test being directly assigned.

This is not merely a testing omission. It is a process-control failure: the agent reported progress without satisfying an explicit completion condition.

### Conclusion

“Reviewed by another agent” and “tests passed” must not be accepted as generic completion signals. The required user journey must be represented as a deterministic release gate.

For this PRD, the minimum automated acceptance suite should cover:

1. Create a personal todo and confirm that it appears in **New**.
2. Drag it to **In Progress** and then **Done**.
3. Reorder multiple todos inside the same lane.
4. Reload and confirm status and ordering persistence.
5. Open the todo detail.
6. Edit the brief and confirm that the original is preserved.
7. Delete the todo and confirm its removal.
8. Verify that the todo is visible only to its creator.
9. Confirm that no out-of-scope collaboration or candidate behavior was introduced.

The agent should not be permitted to mark the task complete while any required journey is deferred, skipped, or represented only by unit-level tests.

---

## 6. UI and drag-and-drop quality

Drag-and-drop was the most recurrent qualitative weakness, particularly for Codex.

The functional PRD specified that todos could be dragged between lanes and reordered, but it apparently did not define the expected interaction quality. A minimal implementation could therefore satisfy the requirement while still feeling unfinished.

Future evaluations should score drag-and-drop separately across:

* Visible drag handles or affordances.
* Lifted or elevated dragged state.
* Placeholder behavior.
* Lane drop-target feedback.
* Smooth reordering.
* Cursor changes.
* Prevention of layout jumps.
* Correct behavior after cancellation.
* Persistence after reload.
* Empty-lane behavior.

A functional pass should require persistence and state correctness. A visual pass should separately require acceptable feedback and motion.

Without this distinction, Codex’s implementations count as complete even though reviewers consistently perceive them as amateurish.

---

## 7. Commit structure and tracer bullets

The PRD-only approach improved execution efficiency but reduced control over implementation sequencing.

Run 7:

* Implemented horizontally rather than following the suggested tracer bullets.
* Created only one commit.
* Introduced a small UI issue that later required a fix.

Run 8 followed the tracer-bullet concept at a high level but did not produce separate issue-sized commits.

This suggests that issue decomposition and commit discipline are separate concerns. Creating five issues is an expensive way to obtain a structured history.

A better instruction would be:

* Allow the agent to plan and execute the PRD as one integrated task.
* Require explicit checkpoints or commits after meaningful vertical milestones.
* Require the application to remain functional at each checkpoint.
* Require a final acceptance-test commit or verification record.

This preserves implementation freedom without sacrificing reviewability.

---

## 8. Recommended configurations

### For fastest reliable functional delivery

**Codex 5.5 Medium, PRD-only, direct execution**

Use when:

* The design system already exists.
* The UI can be refined later.
* Cost and throughput are primary.
* Functional acceptance tests are strong.

Expected result: low resource usage and reliable functionality, with likely need for a separate visual-polish pass.

### For best integrated result

**Opus 4.8 High, PRD-only, direct execution**

Use when:

* UI and interaction quality matter.
* The task is a tightly coupled full-stack slice.
* A higher token and call budget is acceptable.
* The goal is to minimize later design remediation.

Run 9 is the strongest evidence for this configuration.

### For a balanced option

**Opus 4.8 Medium, PRD-only, direct execution**

Use when:

* Better UI than Codex is desired.
* Opus High token consumption is not justified.
* A targeted final visual-QA pass is available.

Run 7 suggests this configuration is efficient, but it should include stronger instructions around implementation sequencing and visual verification.

### Configuration to avoid by default

**Opus with issue-based subagent execution for a tightly coupled vertical slice**

The observed costs included:

* Full or greater-than-full quota consumption.
* High coordination-call counts.
* Deferred verification.
* No demonstrated quality advantage over PRD-only direct execution.

---

## 9. Recommended execution protocol

A stronger default protocol for future PRD evaluations would be:

### Input

Provide the complete PRD without pre-splitting it into implementation issues.

### Planning

Ask the model to:

* Identify the vertical lifecycle.
* Determine internal implementation checkpoints.
* Identify high-risk integration points.
* State the required final acceptance journey.

Do not require subagents unless there are clearly independent workstreams.

### Implementation

Require direct execution with milestone commits, for example:

1. Persistence and domain model.
2. API and service lifecycle.
3. Board rendering and state.
4. Drag-and-drop and persistence.
5. Detail, editing, and deletion.
6. Acceptance tests and final polish.

These are checkpoints rather than separately coordinated issues.

### Verification

Completion should require:

* Automated acceptance test results.
* Static checks and unit tests.
* A fresh read-only code review.
* A visual review focused on drag-and-drop and board interactions.
* No deferred required checks.

### Model allocation

A cost-effective two-stage workflow may be:

1. Codex Medium performs the implementation.
2. Opus High performs a constrained visual and interaction refinement pass.

This combination was not directly tested, so it remains a hypothesis, but the observed strengths of the two models make it a high-value candidate for the next experiment.

---

## 10. Confidence and limitations

The conclusions should be treated as directional rather than statistically definitive.

The evaluation has several limitations:

* Only nine runs were performed.
* Most exact configurations were run once.
* UI quality was assessed qualitatively rather than with a fixed rubric.
* Run 3’s final state is ambiguous.
* Quota percentage is an elapsed-capacity measure, not a direct monetary cost.
* Token and context accounting may differ when subagents are involved.
* Bug-detection standards were not identical across runs.
* The implementations may have encountered different codebase states or incidental difficulties.

The strongest findings are those supported by matched or near-matched comparisons:

1. Removing the five-issue structure substantially improved Opus efficiency.
2. Codex Medium was consistently economical and functionally capable.
3. Opus High produced the strongest UI when allowed to execute the PRD directly.
4. Subagents did not consistently improve speed, correctness, or quality.
5. Explicit acceptance testing is necessary because agent review alone missed or deferred critical checks.

The weaker findings, requiring further runs, are:

* Whether Opus High is consistently better than Opus Medium for UI.
* Whether a Codex implementation followed by an Opus polish pass is more economical than an Opus-only run.
* Whether subagents become beneficial when the PRD contains genuinely independent workstreams.
* Whether milestone commits eliminate the small regressions seen in unconstrained PRD-only execution.

---
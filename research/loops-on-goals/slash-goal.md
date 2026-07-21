# The `/goal` command

In contrast to the common approach that attempts to achieve intelligent work by describing a high level goal… Use on well-defined tasks where not much human judgment is required, but human execution would be very tedious

## Examples
- Scan production logs for errors or anomalies every day. A scheduled job.
- Deploy to production, but not when stakes are very high and uptime is super critical.
- Daily triaging of tickets.

## General Applicability

| Category       | Job                      | Example                                  |
| -------------- | ------------------------ | ---------------------------------------- |
| Maintenance    | Improve codebase quality | docs drift, production bugs, flaky tests |
| Implementation | Complete longer tasks    | multi-ticket Passage goal                |
| Monitoring     | Watch changing state     | CI, PR comments, deploys                 |
| Triage         | Sort open work           | old GitHub issues, stale PRs, noisy logs |



## Costs?

If the looping is used for examples like these (semi-straightforward & tedious),
it may be worth the couple of extra tokens. Saves a lot of time & human attention.

Loops for solving sophisticated problems can be much more expensive.
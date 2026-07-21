# Planning at scale

For seriously documented projects, even smaller ones,
it may be too much work upfront to create an entire PRD.

Even with a clear vision.

There are 2 iterative approaches to solving this issue.

## 1. M. Pocock style - no specs, only per-feature-PRDs

There are no global "specs". There is no PRD representing
the entire product.

Each non-trivial feature is worked on via a PRD, which is
created ad-hoc in a grilling session.

**Initial planning (greenfield)**

- A rough roadmap of work packages, to be tackled as "features".
- An architecture discussion, to establish a direction to start
with.
- A work package for the initial stack & infrastructure setup (if applicable)
  - may include CI/CD

**Incremental building**

Each work package is worked on as a "feature".

## 2. Openspec style - per-task changes & global specs

Openspec has no opinions on planning in the broad sense.
I creates no PRDs as such and expects none to exist.

Openspec works based on changes (per work package) and specs.

BUT it comes close to a PRD with its **change package**:

```markdown
proposal.md       Product intent, rationale, scope, impact
specs/**/*.md     Normative behavior and acceptance scenarios; FRs and sometimes NFRs
design.md         Technical decisions, constraints, risks, non-goals
tasks.md          Implementation and test work
/opsx:verify      Verification against all of the above
```

NFRs also belong in specs when they constitute externally meaningful or verifiable system behavior.
The OpenSpec documentation explicitly identifies security, privacy, reliability, and compatibility constraints as good spec content.

**Initial planning (greenfield)**
  





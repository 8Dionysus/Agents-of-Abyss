# First Cycle

This is the first route through an AbyssOS organ.

It gives an agent enough grammar to begin safely. It is not a full lifecycle
engine, workflow runner, or replacement for local mechanics.

## Cycle

| Step | Question | Output |
|---|---|---|
| `intent` | What is being changed or inspected? | a narrow task statement |
| `route` | Which owner, surface state, and local `AGENTS.md` apply? | owner path and verification lane |
| `work` | What is the smallest useful mutation or review? | changed source, generated output, or audit finding |
| `proof` | Which local check makes the claim reviewable? | validator, test, audit note, or owner evidence |
| `record` | What should survive this cycle? | decision, quest, checkpoint, trace, landing log, changelog, or no-record note |
| `land` | Is the surface ready to merge, publish, or hand off? | landed change, owner request, rollback, or deferred route |
| `handoff` | Which owner carries the next truth? | target owner, remaining validation, and next route |

## Use

Use the first cycle when:

- entering a repository that has not yet localized the full AoA mechanics stack
- preparing a downstream owner handoff
- changing a repo-organ contract surface
- reviewing whether a public claim has enough owner evidence
- checking whether a generated or trace surface is being treated as source

## Record route

Record only what should survive the diff:

| Situation | Route |
|---|---|
| durable rationale | `docs/decisions/` |
| durable obligation | `QUESTBOOK.md` and `quests/` |
| intermediate state worth carrying | checkpoint route |
| evidence-led review | audit mechanic |
| raw-to-active extraction | distillation mechanic |
| release-visible change | `CHANGELOG.md` and release-support |
| movement evidence | `docs/traces/` or owner provenance |

If no durable record is needed, say so in closeout.

## Finish line

The first cycle is complete when the next agent can see:

- what changed
- why it belonged to that owner
- what proof ran
- what record was made or intentionally skipped
- where the next owner route begins

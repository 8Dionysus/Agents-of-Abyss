# Spark Lane

`Spark/` is the fast session lane for GPT-5.3-Codex-Spark style work in the
Agents-of-Abyss center.

Use it when the work can be done as one bounded scenario in one separate Spark
session. The session must finish the lane or leave a portable handoff for a
future session.

## Core Contract

| Rule | Meaning |
|---|---|
| one scenario | choose exactly one registered scenario from `Spark/registry.json` |
| one scope | keep the file family and validation path small |
| done-or-handoff | finish the lane or write a handoff; do not wait for an in-session model switch |
| owner respect | link to stronger owner surfaces instead of absorbing their authority |
| evidence | name files read, files changed, validation run, and remaining risk |

## Start Here

1. Read root `AGENTS.md`.
2. Read [`AGENTS.md`](AGENTS.md).
3. Choose a scenario from [`registry.json`](registry.json).
4. Read that scenario `README.md` and `PROMPT.md`.
5. Finish with a result or a handoff.

## Scenarios

| Scenario | Use |
|---|---|
| [`audit`](scenarios/audit/README.md) | fast drift, noise, duplicate, and path audit |
| [`test-factory`](scenarios/test-factory/README.md) | bounded test generation for an already clear contract |
| [`diff-review`](scenarios/diff-review/README.md) | review a concrete diff or PR for risks and missed checks |
| [`registry-sync`](scenarios/registry-sync/README.md) | align README, AGENTS, registry, validator, and release gate surfaces |
| [`distillation-scout`](scenarios/distillation-scout/README.md) | map legacy/raw material before deeper distillation |
| [`quest-triage`](scenarios/quest-triage/README.md) | turn durable tails into quest candidates without making a TODO pile |
| [`micro-patch`](scenarios/micro-patch/README.md) | make one small patch with local validation |
| [`release-prep`](scenarios/release-prep/README.md) | run a fast release readiness pass before support hardens |

## Output Homes

| Home | Role |
|---|---|
| [`handoffs/open/`](handoffs/open/) | portable packets for future non-Spark or later Spark sessions |
| [`handoffs/closed/`](handoffs/closed/) | closed handoff packets kept as traceable examples |
| [`results/`](results/) | reusable completed Spark results worth preserving beyond chat closeout |

## Validation

Use the validation lane in [`AGENTS.md`](AGENTS.md#validation).

# Decision Note: Decision Memory Uses AGENTS Before Hooks

Status: accepted
Date: 2026-04-29

## Context

`docs/decisions/` existed, but agents did not have a reliable closeout habit for
recording meaningful decisions. Significant architecture, topology, workflow,
and validator-authority changes could land without a durable explanation of why
the chosen path was better than the alternatives.

The workspace also has shared root AGENTS guidance mirrored through
`8Dionysus`. That guidance is read top-down regardless of the agent's eventual
working directory, so it is the right place for a short cross-repository
decision-memory reminder.

## Options considered

1. Rely on agent memory and occasional use of `docs/decisions/`.
2. Add a hook that reminds agents after large diffs.
3. Put a short decision-review rule in AGENTS law, then make AoA's
   `docs/decisions/` format and validator enforce the local practice.

## Decision

Use AGENTS as the primary decision-memory law.

The shared workspace root reminder tells agents to perform a decision review
after meaningful structural, ownership, workflow, route-law, validator-authority,
public-contract, or topology changes. AoA then owns the local decision-record
format, validator, and closeout rule under `docs/decisions/`.

Hooks may become a future reminder layer, but they are not the source of law for
this practice.

## Rationale

Decision records are semantic, not merely diff-size based. Hooks can notice
large or suspicious changes, but they cannot reliably judge whether future
agents need the rationale for a route choice.

AGENTS guidance is already the top-down law surface agents read before editing.
Keeping the top-level rule short avoids noise while ensuring the obligation is
visible in every deep path. The repo-local validator then makes the durable
surface reviewable.

## Consequences

- Future closeouts should state whether a decision record was created or why no
  record was needed.
- AoA release checks now validate decision-record shape and README indexing.
- `docs/decisions/` gains a template and stronger AGENTS law.
- Hooks remain available as a future safety net if repeated misses still occur.

## Source surfaces

- `/srv/AbyssOS/8Dionysus/AGENTS.md`
- `/srv/AGENTS.md`
- `AGENTS.md`
- `docs/AGENTS.md`
- `mechanics/AGENTS.md`
- `docs/decisions/AGENTS.md`
- `docs/decisions/TEMPLATE.md`
- `scripts/validate_decision_records.py`
- `scripts/release_check.py`

## Follow-up route

If future agents continue to miss decision reviews despite AGENTS law and
release validation, add a hook as a reminder layer while keeping
`docs/decisions/` as the source-owned record surface.

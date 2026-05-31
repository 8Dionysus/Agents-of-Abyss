# Spark Session Lane Contract

- Decision ID: AOA-CENTER-D-0024

## Status

Superseded.

## Index Metadata

- Original date: 2026-04-30
- Surface classes: agent lane, release workflow
- Center facets: spark lane, agent guidance
- Mechanic parents: cross-mechanic
- Guard families: AGENTS/mesh, release/tooling
- Posture: superseded placement rationale

## Context

At the time of this record, `Spark/` existed as a fast-lane surface for
GPT-5.3-Codex-Spark style work, but it only had local AGENTS guidance and a
swarm note. The lane did not yet define how a Spark-only session should end,
where unfinished work should go, or how future agents should validate scenario
shape.

Spark sessions are expected to run separately from slower model sessions. That
means unfinished work cannot rely on an in-session model switch.

## Options considered

1. Keep `Spark/` as a loose AGENTS note plus swarm recipe.
2. Convert Spark into a full mechanic package under `mechanics/`.
3. Keep Spark as an agent lane and add registry-backed session scenarios with a
   done-or-handoff exit contract.

## Decision

Spark remained a root agent lane at this point in the repository history. It
used `Spark/registry.json` to define session-contained scenarios, and each
scenario had to provide a launch prompt, result template, handoff template, and
example result. Work that Spark could not finish moved into
`Spark/handoffs/open/` as a portable packet. Reusable completed Spark results
could live in `Spark/results/`.

The placement part of this decision is superseded by
[`AOA-CENTER-D-0027-codex-spark-agent-lane-home`](AOA-CENTER-D-0027-codex-spark-agent-lane-home.md).
The done-or-handoff contract survives under `.agents/spark/`.

## Rationale

Spark is useful as a fast operator, scout, reviewer, and small patch executor,
but it should not become a new source of AoA doctrine. A scenario registry gives
future sessions a clean entry shape without promoting Spark to mechanic status.
The done-or-handoff contract keeps fast work honest when a task needs deeper
architecture or owner-local judgment.

## Consequences

- New Spark scenarios must be registered and validated.
- Spark sessions must finish the scenario or leave a handoff packet.
- `release_check.py` validates Spark lane shape.
- `Spark/scripts/` and `Spark/tests/` are recognized as agent-lane homes, not
  root script/test ownership.
- The root AGENTS mesh changes when Spark AGENTS guidance changes.

## Source surfaces

- `Spark/README.md`
- `Spark/AGENTS.md`
- `Spark/SWARM.md`
- `Spark/registry.json`
- `Spark/scenarios/`
- `Spark/scripts/validate_spark_lane.py`
- `Spark/tests/test_spark_lane.py`
- `scripts/release_check.py`

## Follow-up route

When a Spark scenario starts carrying durable process law beyond launch,
handoff, and validation shape, route that law to the owning mechanic or
repository. When a Spark handoff becomes active work, close or move the packet
after the owner session resolves it.

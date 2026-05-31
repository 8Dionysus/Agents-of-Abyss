# Codex Spark Agent Lane Home

- Decision ID: AOA-CENTER-D-0027

## Status

Accepted.

## Index Metadata

- Original date: 2026-05-13
- Surface classes: agent lane, root surface
- Center facets: spark lane, agent guidance
- Mechanic parents: cross-mechanic
- Guard families: AGENTS/mesh, center route law
- Posture: accepted rationale

## Context

The Spark lane is a Codex Spark-specific agent lane with a registry-backed
done-or-handoff contract. It was previously rooted at `Spark/`, which made it
look like a durable root district beside `scripts/`, `tests/`, `docs/`, and
other center surfaces.

The lane is not a mechanic package, a constitutional source, or a general root
district. It is agent-facing launch, result, and handoff material. The root
already has `.agents/` as the owner lane for local agent assets, prompts,
skills, and model-facing operation help.

## Options considered

1. Keep `Spark/` at root and document it as a special root agent lane.
2. Promote Spark into `mechanics/` as a center mechanic package.
3. Move Spark under `.agents/spark/`, update route contracts and validators,
   and keep the topology change trace in decision records.

## Decision

Move the Codex Spark lane from `Spark/` to `.agents/spark/`.

`.agents/spark/` owns the Spark `AGENTS.md`, scenario registry, launch prompts,
result and handoff templates, storage directories, validator, and tests. Root
surfaces should route to `.agents/` and `.agents/spark/` instead of treating
Spark as a root district.

The earlier done-or-handoff contract remains active. The placement decision in
`AOA-CENTER-D-0024-spark-session-lane-contract.md` is superseded only for its root
home.

## Rationale

`.agents/spark/` matches the real ownership: Spark is a Codex agent operating
lane, not an AoA center doctrine surface and not a reusable mechanic. Keeping it
under `.agents/` lets a future Codex Spark session start from the nearest
agent-lane card while keeping the repository root focused on civic, governance,
technical district, and mechanic entry surfaces.

This also makes the future route simpler. A session that needs Spark reads
`.agents/AGENTS.md`, then `.agents/spark/AGENTS.md`, then the Spark registry and
scenario prompt. Other agents can ignore the lane unless they are changing its
contracts or validation.

## Consequences

- `Spark/` is removed as a root directory.
- `.agents/spark/` becomes the current Spark source surface.
- `release_check.py`, pytest collection, script/test registries, and the AGENTS
  mesh route to `.agents/spark/`.
- Root README and root-surface law treat Spark as an `.agents` lane rather than
  a technical root district.
- Historical root placement remains visible only through decision records.

## Source surfaces

- `.agents/AGENTS.md`
- `.agents/spark/README.md`
- `.agents/spark/AGENTS.md`
- `.agents/spark/SWARM.md`
- `.agents/spark/registry.json`
- `.agents/spark/scenarios/`
- `.agents/spark/scripts/validate_spark_lane.py`
- `.agents/spark/tests/test_spark_lane.py`
- `README.md`
- `docs/ROOT_SURFACE_LAW.md`
- `config/agents_mesh.json`
- `scripts/release_check.py`
- `scripts/registry.json`
- `tests/registry.json`
- `pytest.ini`
- `docs/decisions/AOA-CENTER-D-0024-spark-session-lane-contract.md`

## Follow-up route

If Spark scenarios begin carrying durable process law beyond launch, result,
handoff, and validation shape, move that law to the owning mechanic or root
source surface. If the lane becomes model-agnostic rather than Codex Spark
specific, revisit the `.agents/spark/` name with another decision record before
renaming.

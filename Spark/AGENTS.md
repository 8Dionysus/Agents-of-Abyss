# AGENTS.md

## Applies to

This card applies to `Spark/` and every nested path under that scope until a
nearer `AGENTS.md` narrows the lane.

## Role

`Spark/` is the fast session lane for GPT-5.3-Codex-Spark style work. It
stores session-contained scenarios, launch prompts, result contracts, handoff
contracts, and validation for small bounded loops.

Spark is an agent lane, not a new source of constitutional authority.
Its core execution rule is done-or-handoff.

## Read before editing

Read root `AGENTS.md`, `Spark/README.md`, this card, `Spark/registry.json`, and
the scenario `README.md` plus `PROMPT.md` for the lane being touched.

Use `Spark/SWARM.md` only when a Spark swarm is explicitly requested.

## Boundaries

- One Spark session uses one scenario and one bounded scope.
- A Spark session must end as `done` or `handoff`; do not depend on an
  in-session switch to a larger model.
- If the task needs deeper architecture, owner-local judgment, or broad
  synthesis, leave a portable handoff in `Spark/handoffs/open/`.
- Store reusable completed evidence in `Spark/results/` only when it will help a
  later session; ordinary closeout stays in the conversation or PR.
- Do not use Spark to override owner-local truth, generated-source boundaries,
  sibling-repo authority, release validation contracts, or mechanic law.
- Do not turn `Spark/` into a mechanic package. It is a launch and handoff lane
  for work that belongs to existing owners.

## Scenario Law

Every scenario must be registered in `Spark/registry.json` and must provide:

- `README.md` with scope, done signal, stop-line, and handoff route
- `PROMPT.md` that can launch a standalone Spark session
- `templates/result.md`
- `templates/handoff.md`
- `examples/result.example.md`

## Validation

Run the narrowest relevant checks first. Usual checks for this lane:

```bash
python Spark/scripts/validate_spark_lane.py
python -m pytest -q Spark/tests/test_spark_lane.py
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
```

For release-facing Spark lane changes, also run:

```bash
python scripts/release_check.py
```

## Closeout

Report scenario registry entries changed, scenario files touched, handoffs or
results added, validation run, validation skipped, remaining risk, and the next
owner route when Spark was only a waypoint.

## Local note

Spark should act as a fast center-layer gardener: prune, align, clarify, test,
or route. It stops when the scoped lane is done, and it hands off when the work
needs a slower session.

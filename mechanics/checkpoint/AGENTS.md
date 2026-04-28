# AGENTS.md

## Applies to

This card applies to `mechanics/checkpoint/` and every nested path under that
scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, this card,
`mechanics/checkpoint/README.md`, `mechanics/checkpoint/DIRECTION.md`,
`mechanics/checkpoint/PARTS.md`, and the relevant active part before changing
this package.

For owner boundaries, start from `mechanics/checkpoint/OWNER_MAP.md`.
For evidence lineage, use `mechanics/checkpoint/PROVENANCE.md`; do not start
from runtime-local `.aoa/` logs or sibling raw histories.

## Boundaries

- Do not turn checkpoint into a hidden scheduler, autonomous self-repair loop,
  runtime worker, memory object family, proof authority, or stats source.
- Do not treat `aoa-sdk` checkpoint controls as the source of checkpoint law.
- Do not treat center checkpoint wording as owner acceptance.
- Do not promote raw checkpoint append history into center doctrine.
- If checkpoint work needs owner-local implementation, proof, memory, runtime,
  role, route, playbook, stats, or seed behavior, update the owner-request
  surfaces instead of claiming it in the center.

## Closeout

Closeout must name changed checkpoint surfaces, whether `PROVENANCE.md` was
consulted, owner requests affected, checks run, checks skipped, remaining risk,
and the next owner route if checkpoint was only a waypoint.

If `PROVENANCE.md` was consulted, name only the relevant source bridge or
receipt section. Do not enumerate runtime logs or sibling histories unless the
task specifically audited that evidence in depth.

## Role

Checkpoint owns AoA center law for bounded intermediate states: session carry,
review gates, return anchors, closeout bridges, runtime export boundaries, and
owner handoffs.

It does not own checkpoint implementation, memory canon, proof verdicts,
runtime activation, route dispatch, stats truth, or owner-local acceptance.

## Source Surfaces

- `README.md`: package entry and route.
- `DIRECTION.md`: current active mechanic direction.
- `PARTS.md`: active functioning-part map.
- `parts/`: concise active checkpoint contracts.
- `OWNER_MAP.md`: checkpoint owner boundary and stronger-owner split.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `ROADMAP.md`: current and next checkpoint contour.
- `LANDING_LOG.md`: checked checkpoint landing ledger.
- `PROVENANCE.md`: controlled bridge to source evidence.
- `docs/`: detailed doctrine and support notes.

## Post-change route review

After checkpoint changes, check whether the next agent can start from
`README.md`, `DIRECTION.md`, `PARTS.md`, and the relevant active part without
reading raw runtime or sibling history.

Check whether the move changed:

- `DIRECTION.md`: current checkpoint posture or return-anchor emphasis.
- `PARTS.md`: active part boundaries or functioning-part map.
- `OWNER_MAP.md`: owner boundary, stop-line, or handoff target.
- `OWNER_REQUESTS.md` and `mechanics/owner-request-queue.json`: runtime,
  memory, proof, route, role, playbook, stats, or SDK asks.
- `ROADMAP.md`: future route pressure or unresolved checkpoint contour.
- `LANDING_LOG.md`: a checked landing or planted contract.
- `PROVENANCE.md`: source bridge, receipt route, or archive map.
- `mechanics/registry.json` and generated indexes: card-facing route, owner
  boundary, validation refs, or public summaries.

Only update a surface when its meaning moved. Leave it untouched when the
change does not affect its job.

## Validation

Run the narrow checkpoint lane after package changes:

```bash
python scripts/validate_mechanics_topology.py --mechanic checkpoint
python scripts/validate_mechanic_readme_cards.py --mechanic checkpoint
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_mechanic_landing_logs.py --mechanic checkpoint
python scripts/validate_mechanic_artifact_topology.py --mechanic checkpoint
python mechanics/checkpoint/scripts/validate_checkpoint_mechanic.py
python -m pytest -q mechanics/checkpoint/tests
```

If owner requests changed, also run:

```bash
python scripts/validate_owner_request_queue.py --mechanic checkpoint
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic checkpoint
```

For release-readiness or cross-mechanic edits, finish with:

```bash
python scripts/release_check.py
```

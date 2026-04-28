# AGENTS.md

## Applies to

This card applies to `mechanics/distillation/` and every nested path until a
nearer `AGENTS.md` narrows the lane.

## Read before editing

Read the repository root `AGENTS.md`, `mechanics/AGENTS.md`, this card,
`README.md`, `DIRECTION.md`, `PARTS.md`, `OWNER_MAP.md`, and
`OWNER_REQUESTS.md` before changing files in this lane.

Use `PROVENANCE.md` only when source lineage matters. Do not start by opening
legacy material.

## Boundaries

- `mechanics/distillation/` owns center law, route grammar, active parts, and
  owner request packets for distillation.
- It does not own technique canon, executable skills, playbook scenarios,
  runtime behavior, memory canon, proof verdicts, seed staging, SDK helpers, or
  ToS-authored meaning.
- Legacy and raw material stay behind provenance routes; active parts stay
  light and source-linked.

## Editing posture

- Change the active part first when behavior changes.
- Keep raw inventories behind `PROVENANCE.md`, `legacy/INDEX.md`, and
  `legacy/DISTILLATION_LOG.md`.
- Keep active docs free of raw-source catalogs and long packet tails.
- Route technique, skill, playbook, runtime, memo, proof, seed, SDK, and ToS
  claims through `OWNER_REQUESTS.md`.
- Update `ROADMAP.md` when a future route or unresolved owner pressure changes.
- Update `LANDING_LOG.md` when a checked landing changes.

## Closeout

Closeout must name changed active parts, whether `PROVENANCE.md` was consulted,
owner requests affected, checks run, checks skipped, remaining risk, and the
next owner route if this lane was only a waypoint.

If `PROVENANCE.md` was consulted, name only the relevant source bridge,
archive map, or distillation log section. Do not enumerate raw files unless the
task specifically audited archive evidence in depth.

## Role

Distillation is the center law for turning raw, long, noisy, historical,
checkpoint, donor, runtime, or witness-facing material into active,
reviewable, owner-routable surfaces without severing provenance or inflating
authority.

It is not summarization, proof, memory canon, owner acceptance, ToS canon, or
runtime activation.

## Source Surfaces

- `README.md`: package entry and route.
- `DIRECTION.md`: current active mechanic direction.
- `PARTS.md`: active functioning-part map.
- `parts/`: concise active distillation contracts.
- `OWNER_MAP.md`: distillation owner boundary and stronger-owner split.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `ROADMAP.md`: current and next distillation contour.
- `LANDING_LOG.md`: checked distillation landing ledger.
- `PROVENANCE.md`: controlled bridge to legacy and source accounting.
- `legacy/INDEX.md`: archive map.
- `legacy/DISTILLATION_LOG.md`: archival distillation record.
- `docs/`: detailed doctrine and support notes.

## Post-change route review

After any distillation change, check whether the next agent can start from
`README.md`, `DIRECTION.md`, `PARTS.md`, and the relevant active part without
opening `legacy/raw/`.

Check whether the move changed:

- `DIRECTION.md`: current distillation posture or active operating route.
- `PARTS.md`: active part boundaries or functioning-part map.
- `OWNER_MAP.md`: owner boundary, stop-line, or handoff target.
- `OWNER_REQUESTS.md` and `mechanics/owner-request-queue.json`: technique,
  skill, playbook, runtime, memo, proof, seed, SDK, KAG, or ToS asks.
- `ROADMAP.md`: future route pressure or unresolved distillation contour.
- `LANDING_LOG.md`: a checked landing or planted contract.
- `PROVENANCE.md`: source bridge, receipt route, or archive map.
- `legacy/INDEX.md` and `legacy/DISTILLATION_LOG.md`: archival accounting,
  only when archive evidence moved.
- `mechanics/registry.json` and generated indexes: card-facing route, owner
  boundary, validation refs, or public summaries.

Only update a surface when its meaning moved. Leave it untouched when the
change does not affect its job.

## Validation

```bash
python mechanics/distillation/scripts/validate_distillation_mechanic.py
python scripts/validate_mechanics_topology.py --mechanic distillation
python scripts/validate_mechanic_readme_cards.py --mechanic distillation
python scripts/validate_owner_request_queue.py --mechanic distillation
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic distillation
python scripts/validate_mechanic_landing_logs.py --mechanic distillation
```

For release-bound changes, also run the central mechanics and release checks
from `mechanics/AGENTS.md`.

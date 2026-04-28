# AGENTS.md

## Applies to

This card applies to `mechanics/distillation/` and every nested path until a
nearer `AGENTS.md` narrows the lane.

## Read before editing

Read:

- `mechanics/AGENTS.md`
- `mechanics/distillation/README.md`
- `mechanics/distillation/DIRECTION.md`
- `mechanics/distillation/PARTS.md`
- `mechanics/distillation/OWNER_MAP.md`

Use `PROVENANCE.md` only when source lineage matters. Do not start by opening
legacy material.

## Role

Distillation is the center law for turning raw, long, noisy, historical,
checkpoint, donor, runtime, or witness-facing material into active,
reviewable, owner-routable surfaces without severing provenance or inflating
authority.

It is not summarization, proof, memory canon, owner acceptance, ToS canon, or
runtime activation.

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

## Closeout

Closeout must name changed active parts, whether `PROVENANCE.md` was consulted,
owner requests affected, checks run, checks skipped, remaining risk, and the
next owner route if this lane was only a waypoint.

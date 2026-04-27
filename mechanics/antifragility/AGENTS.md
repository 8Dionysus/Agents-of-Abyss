# AGENTS.md

## Applies to

This card applies to `mechanics/antifragility/` and every nested path under that
scope until a nearer `AGENTS.md` narrows the lane.

## Role

Antifragility owns center stress posture, via negativa, anti-authority rules,
sprawl control, fragile-pattern tracking, repair-proof routing, and owner-local
cleanup handoff discipline.

It does not own owner-local deletion, proof verdicts, memory truth, runtime
recovery, public health claims, or sibling-repo cleanup execution.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, this file, and
[`README.md`](README.md). For active work, prefer [`DIRECTION.md`](DIRECTION.md),
[`PARTS.md`](PARTS.md), [`OWNER_MAP.md`](OWNER_MAP.md), and
[`OWNER_REQUESTS.md`](OWNER_REQUESTS.md) before opening historical source
material.

Use [`PROVENANCE.md`](PROVENANCE.md) as the only default bridge into source
history.

## Boundaries

- Do not turn antifragility into one-score health.
- Do not turn deletion into performance theater.
- Do not claim owner-local cleanup authority from the center.
- Do not hide historical source material inside active parts.
- Do not publish repair success without proof or owner-local receipts.
- Do not add a new tracked surface without naming what becomes smaller,
  narrower, moved, merged, suppressed, quarantined, deprecated, or deleted.

## Validation

For package changes, run:

```bash
python mechanics/antifragility/scripts/validate_antifragility_distillation.py
python scripts/validate_mechanics_topology.py --mechanic antifragility
python scripts/validate_mechanic_readme_cards.py --mechanic antifragility
python scripts/validate_mechanic_landing_logs.py --mechanic antifragility
python scripts/validate_owner_request_queue.py --mechanic antifragility
python scripts/validate_owner_request_docs.py --mechanic antifragility
python scripts/build_mechanic_card_index.py --check
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python -m pytest -q mechanics/antifragility/tests
```

Run wider checks when registry, generated, root route, or release surfaces
change.

<!-- centralized-child-validation:start -->

### Centralized Child Validation

Executable validation commands from child docs live here. Child docs should
route to this section instead of carrying command blocks.

#### `mechanics/antifragility/README.md`

```bash
python mechanics/antifragility/scripts/validate_antifragility_distillation.py
python scripts/validate_mechanics_topology.py --mechanic antifragility
python scripts/validate_mechanic_readme_cards.py --mechanic antifragility
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic antifragility
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic antifragility
```

<!-- centralized-child-validation:end -->

## Closeout

Closeout must name changed active parts, whether `PROVENANCE.md` was consulted,
owner requests affected, checks run, checks skipped, remaining risk, and the
next owner route if this lane was only a waypoint.

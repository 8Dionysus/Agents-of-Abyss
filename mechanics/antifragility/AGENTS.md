# AGENTS.md

## Applies to

This card applies to `mechanics/antifragility/` and every nested path under that
scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read the repository root `AGENTS.md`, `mechanics/AGENTS.md`, this card,
`README.md`, `DIRECTION.md`, `PARTS.md`, `OWNER_MAP.md`, and
`OWNER_REQUESTS.md` before changing files in this lane.

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

## Closeout

Closeout must name changed active parts, whether `PROVENANCE.md` was consulted,
owner requests affected, checks run, checks skipped, remaining risk, and the
next owner route if this lane was only a waypoint.

If `PROVENANCE.md` was consulted, name only the relevant provenance bridge or
archive map/log section. Do not enumerate individual archived files unless the
task specifically audited archive evidence in depth.

## Role

Antifragility owns center stress posture, via negativa, anti-authority rules,
sprawl control, fragile-pattern tracking, repair-proof routing, and owner-local
cleanup handoff discipline.

It does not own owner-local deletion, proof verdicts, memory truth, runtime
recovery, public health claims, or sibling-repo cleanup execution.

## Source Surfaces

- `README.md`: package entry and route.
- `DIRECTION.md`: current active mechanic direction.
- `PARTS.md`: active functioning-part map.
- `parts/`: concise active part contracts.
- `OWNER_MAP.md`: owner boundary and stronger-owner split.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `ROADMAP.md`: current and next antifragility contour.
- `LANDING_LOG.md`: checked antifragility landing ledger.
- `FRAGILITY_BLACKLIST.md`: active fragile-pattern route surface.
- `PROVENANCE.md`: controlled bridge to legacy and source accounting.
- `legacy/`: archival source material, not active law.
- `docs/`: detailed doctrine and support notes.

## Post-change route review

After any antifragility change, check whether the move changed:

- `DIRECTION.md`: current stress, subtraction, or repair posture.
- `PARTS.md`: active part boundaries or the functioning-part map.
- `FRAGILITY_BLACKLIST.md`: active fragile-pattern route entries.
- `OWNER_MAP.md`: owner boundary, stop-line, or stronger-owner split.
- `OWNER_REQUESTS.md` and `mechanics/owner-request-queue.json`: cleanup,
  proof, runtime, memory, or owner-local asks.
- `ROADMAP.md`: future route pressure or unresolved repair contour.
- `LANDING_LOG.md`: a checked landing or superseded contract.
- `PROVENANCE.md`: source bridge, archive map, or receipt route.
- `mechanics/registry.json` and generated indexes: card-facing route, owner
  boundary, validation refs, or public summaries.

Only update a surface when its meaning moved. Leave it untouched when the
change does not affect its job.

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

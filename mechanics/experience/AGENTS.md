# AGENTS.md

## Applies to

This card applies to `mechanics/experience/` and every nested path under that scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read the repository root `AGENTS.md`, `mechanics/AGENTS.md`, this card, `README.md`, `DIRECTION.md`, and `PARTS.md` before changing files in this lane.

## Boundaries

Do not use this lane to override owner-local truth, generated-source boundaries, sibling-repo authority, release validation contracts, live runtime, hidden memory sovereignty, or ToS-authored meaning.


## Closeout

Closeout must name changed active parts, whether `PROVENANCE.md` was consulted, owner requests affected, checks run, checks skipped, remaining risk, and the next owner route if this lane was only a waypoint.

If `PROVENANCE.md` was not consulted, say so explicitly. If it was consulted,
name only the relevant provenance bridge or archive map/log section. Do not
enumerate individual archived files unless the task specifically audited archive
evidence in depth.

## Role

Experience owns center-level experience capture, certification, deployment, federation harvest, adoption, governance, office posture, service mesh, continuity loom, and living-workspace boundary doctrine.

It does not activate live workspace runtime, owner-local offices, hidden memory sovereignty, direct KAG promotion, direct ToS writes, or assistant operational authority.

## Source Surfaces

- `README.md`: package entry and route.
- `DIRECTION.md`: current active mechanic direction.
- `PARTS.md`: active functioning-part map.
- `parts/`: concise active part contracts.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `ROADMAP.md`: current and next Experience contour.
- `LANDING_LOG.md`: canonical Experience landing ledger.
- `artifact-map.json`: machine-readable receipt from old flat artifact paths to
  active part-local homes.
- `provenance-receipts.json`: machine-readable receipt IDs for old packets,
  sibling surfaces, and staged seed inputs referenced by active artifacts.
- `PROVENANCE.md`: controlled bridge to archival accounting.
- `docs/`: compatibility route only.

## Post-change route review

After any Experience change, check whether the move changed:

- `DIRECTION.md`: the mechanic's current operating direction.
- `PARTS.md`: the active part map or part boundaries.
- `ROADMAP.md`: future work, route shape, unresolved owner pressure, or current contour.
- `LANDING_LOG.md`: a checked landing, supersession, or planted contract.
- `OWNER_REQUESTS.md` and `mechanics/owner-request-queue.json`: stronger-owner asks or stop-lines.
- `artifact-map.json`: old flat artifact paths, active part homes, or artifact
  placement receipts.
- `provenance-receipts.json`: receipt IDs, source refs, or active artifact
  provenance indirection.
- `mechanics/registry.json` and generated indexes: card-facing route, owner boundary, validation refs, or public summaries.

Only update a surface when its meaning moved. Leave it untouched when the change
does not affect its job.

If a change reveals work that should happen later but is not ready now, record
it in `ROADMAP.md` only when the trigger is concrete. Use a short "time has
come when" note: condition, future move, and guardrail. Do not put speculative
plans into active part contracts, `LANDING_LOG.md`, or `PROVENANCE.md`.

## Validation

Use `python mechanics/experience/scripts/validate_experience_distillation.py` after active-part or provenance-route changes.
Use `python scripts/validate_mechanic_artifact_topology.py --mechanic experience` after schema, example, script, or test placement changes.
Use `python scripts/validate_mechanic_landing_logs.py --mechanic experience` after landing-log or surface-chain changes.
Use the nearest `parts/<part>/scripts/*.py` and `parts/<part>/tests/test_*.py`
for part-specific artifact surfaces.

<!-- centralized-child-validation:start -->

### Centralized Child Validation

Executable validation commands from child docs live here. Child docs should
route to this section instead of carrying command blocks.

#### `mechanics/experience/DIRECTION.md`

```bash
python mechanics/experience/scripts/validate_experience_distillation.py
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
```

#### `mechanics/experience/OWNER_REQUESTS.md`

```bash
python scripts/validate_owner_request_queue.py --mechanic experience
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
```

#### `mechanics/experience/PARTS.md`

```bash
python mechanics/experience/scripts/validate_experience_distillation.py
python scripts/validate_mechanic_artifact_topology.py --mechanic experience
```

#### `mechanics/experience/README.md`

```bash
python mechanics/experience/scripts/validate_experience_distillation.py
python scripts/validate_mechanic_artifact_topology.py --mechanic experience
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic experience
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic experience
```

<!-- centralized-child-validation:end -->

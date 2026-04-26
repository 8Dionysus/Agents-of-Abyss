# AGENTS.md

## Applies to

This card applies to `mechanics/agon/` and every nested path under that scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read the repository root `AGENTS.md`, `mechanics/AGENTS.md`, this card,
`README.md`, `DIRECTION.md`, and `PARTS.md` before changing files in this lane.

## Boundaries

Do not use this lane to override owner-local truth, generated-source
boundaries, sibling-repo authority, release validation contracts, live arena
execution, assistant contestant authority, live rank mutation, KAG canon, or ToS
canon writes.

## Closeout

Closeout must name changed active parts, whether `PROVENANCE.md` was consulted,
owner requests affected, checks run, checks skipped, remaining risk, and the
next owner route if this lane was only a waypoint.

If `PROVENANCE.md` was not consulted, say so explicitly. If it was consulted,
name only the relevant source-doc family or map section. Do not enumerate
detailed source files unless the task specifically audited source-doc evidence
in depth.

## Role

Agon owns center-level pressure, contest, lawful move language, arena grammar,
state packets, verdict contours, retention, rank, school, KAG pressure,
canon-restraint, and threshold doctrine.

It does not activate live arena execution, assistant contestant authority,
runtime mutation, proof sovereignty, rank mutation, KAG canon, or ToS canon
writes.

## Source Surfaces

- `README.md`: package entry and route.
- `DIRECTION.md`: current active mechanic direction.
- `PARTS.md`: active functioning-part map.
- `parts/`: concise active part contracts.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `ROADMAP.md`: current and next Agon contour.
- `LANDING_LOG.md`: canonical Agon landing ledger.
- `PROVENANCE.md`: controlled bridge to detailed source-doc accounting.
- `artifact-map.json`: old flat artifact path to active part-home receipts.
- `legacy/`: provenance and artifact receipts; enter through `PROVENANCE.md`.
- `docs/`: compatibility route only.

## Post-change route review

After any Agon change, check whether the move changed:

- `DIRECTION.md`: the mechanic's current operating direction.
- `PARTS.md`: the active part map or part boundaries.
- `ROADMAP.md`: future work, route shape, unresolved owner pressure, or current contour.
- `LANDING_LOG.md`: a checked landing, supersession, or planted contract.
- `OWNER_REQUESTS.md` and `mechanics/owner-request-queue.json`: stronger-owner asks or stop-lines.
- `PROVENANCE.md`: source-doc family routes or detailed accounting bridge.
- `mechanics/registry.json` and generated indexes: card-facing route, owner boundary, validation refs, or public summaries.

Only update a surface when its meaning moved. Leave it untouched when the change
does not affect its job.

If a change reveals work that should happen later but is not ready now, record
it in `ROADMAP.md` only when the trigger is concrete. Use a short "time has
come when" note: condition, future move, and guardrail. Do not put speculative
plans into active part contracts, `LANDING_LOG.md`, or `PROVENANCE.md`.

## Validation

Use `python mechanics/agon/scripts/validate_agon_distillation.py` after
active-part or provenance-route changes.
Use `python scripts/validate_mechanic_artifact_topology.py --mechanic agon`
after schema, example, config, generated artifact, script, or test placement
changes.
Use `python scripts/validate_mechanic_landing_logs.py --mechanic agon` after
landing-log or surface-chain changes.
Use the nearest part-local `scripts/*agon*.py` and `tests/test_agon_*.py` for
generated or model-specific changes.

# AGENTS.md

## Applies to

This card applies to `mechanics/audit/` and every nested path under that scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read `DIRECTION.md`, `PARTS.md`, and the relevant owner route only when Audit meaning changes.
## Boundaries

Do not use this lane to create proof verdicts, owner-local remediation authority, runtime authority, memory truth, release authority, generated authority, or archival authority.

## Closeout


If `PROVENANCE.md` was not consulted, say so explicitly. If it was consulted,
name only the relevant provenance bridge or legacy map section. Do not enumerate
individual archived files unless the task specifically audited archive evidence
in depth.

## Role

Audit owns center-level seeing: source maps, evidence ledgers, risk signals, finding lifecycle, owner routing, validation gates, campaign routes, and event bridges.

It turns unclear surfaces into reviewable next moves. It does not repair the owner surface by itself, certify proof strength by itself, or turn raw evidence into law.

## Source Surfaces

- `README.md`: package entry and mechanic card.
- `DIRECTION.md`: current active audit direction.
- `PARTS.md`: active functioning-part map.
- `OWNER_MAP.md`: stronger-owner routing map.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `ROADMAP.md`: current and future audit contour.
- `LANDING_LOG.md`: canonical audit landing ledger.
- `PROVENANCE.md`: controlled bridge to legacy audit accounting.
- `docs/AUDIT_LAW.md`: center audit law.
- `docs/AUDIT_OWNER_REPO_REQUESTS.md`: compatibility route to owner requests.
- `parts/`: concise active part contracts.
- `legacy/`: archived route receipts and raw source preservation.

## Post-change route review

After any Audit change, check whether the move changed:

- `DIRECTION.md`: the mechanic's current operating direction.
- `PARTS.md`: the active part map or part boundaries.
- `ROADMAP.md`: future work, route shape, unresolved owner pressure, or current contour.
- `LANDING_LOG.md`: a checked landing, supersession, or planted contract.
- `OWNER_REQUESTS.md` and `mechanics/owner-request-queue.json`: stronger-owner asks or stop-lines.
- `PROVENANCE.md`: archive bridge, source migration map, or legacy accounting.
- `mechanics/registry.json` and generated indexes: card-facing route, owner boundary, validation refs, or public summaries.

Only update a surface when its meaning moved. Leave it untouched when the change does not affect its job.

If a change reveals work that should happen later but is not ready now, record
it in `ROADMAP.md` only when the trigger is concrete. Use a short "time has
come when" note: condition, future move, and guardrail. Do not put speculative
plans into active part contracts, `LANDING_LOG.md`, or `PROVENANCE.md`.

## Validation

Child routes remain keyed by `mechanics/validation-routes.json`.

The Audit mechanic route is defined in the repository [`VALIDATION.md`](../../VALIDATION.md) for Audit mechanic changes.

The applicable route for route, generated, or root docs reference changes is defined in the repository [`VALIDATION.md`](../../VALIDATION.md).

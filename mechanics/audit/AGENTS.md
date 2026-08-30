# AGENTS.md

## Applies to

This card applies to `mechanics/audit/` and every nested path under that scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read the repository root `AGENTS.md`, `mechanics/AGENTS.md`, this card, `README.md`, `DIRECTION.md`, and `PARTS.md` before changing files in this lane.

## Boundaries

Do not use this lane to create proof verdicts, owner-local remediation authority, runtime authority, memory truth, release authority, generated authority, or archival authority.

## Closeout

Closeout must name changed active parts, whether `PROVENANCE.md` was consulted, owner requests affected, checks run, checks skipped, remaining risk, and the next owner route if this lane was only a waypoint.

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

Use these commands after Audit mechanic changes:

```bash
python mechanics/audit/scripts/validate_audit_distillation.py
python scripts/mechanics_topology/validate_mechanics_topology.py --mechanic audit
python scripts/mechanics_topology/validate_mechanic_readme_cards.py --mechanic audit
python scripts/mechanics_topology/validate_mechanic_landing_logs.py --mechanic audit
python scripts/owner_requests/validate_owner_request_queue.py --mechanic audit
python scripts/owner_requests/validate_owner_request_docs.py --mechanic audit
```

Use these commands after route, generated, or root docs references change:

```bash
python scripts/mechanics_topology/build_mechanic_card_index.py --check
python scripts/owner_requests/build_owner_request_queue.py --check
python scripts/center_entry/build_center_entry_map.py --check
python scripts/center_entry/validate_center_entry_map.py
python scripts/hygiene/validate_markdown_shape.py
python scripts/hygiene/validate_links.py
```

### Routed child validation

Child-specific commands are source-owned by `mechanics/validation-routes.json`.
Run `python scripts/mechanics_topology/run_validation_route.py --surface <repo-relative-path>`;
add `--show` to inspect the route without executing it.

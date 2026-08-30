# AGENTS.md

## Applies to

This card applies to `mechanics/release-support/` and every nested path under
that scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read the repository root `AGENTS.md`, `mechanics/AGENTS.md`, this card,
`README.md`, `DIRECTION.md`, `PARTS.md`, `OWNER_MAP.md`, and
`OWNER_REQUESTS.md` before changing files in this lane.

Use `PROVENANCE.md` only when source lineage, release history, or transition
evidence matters. Do not start from legacy material.

## Boundaries

- Do not use this lane to override owner-local truth, generated-source
  boundaries, sibling-repo authority, or release validation contracts.
- Do not turn release support into public promise authority, owner acceptance,
  proof verdict, runtime truth, or rollback execution.
- Do not put mechanic landing history, roadmap detail, or owner-local release
  truth into root release surfaces.

## Closeout

Closeout must name changed active parts, whether `PROVENANCE.md` was consulted,
owner requests affected, release-facing surfaces affected, checks run, checks
skipped, remaining risk, and the next owner route if this lane was only a
waypoint.

If `PROVENANCE.md` was consulted, name only the relevant protocol, archive map,
or receipt section. Do not enumerate legacy sources unless the task
specifically audited archive evidence in depth.

## Role

Release-support owns center state-transition gates, public support posture,
federation release protocol, center release procedure, direction-surface
routing, changelog/roadmap/landing-log separation, owner handoff stop-lines,
and rollback/return posture.

It does not turn unverified future work into public claims, owner acceptance,
proof verdicts, runtime truth, or public projection authority.

## Source Surfaces

- `README.md`: package entry and route.
- `DIRECTION.md`: current active mechanic direction.
- `PARTS.md`: active functioning-part map.
- `parts/`: concise active release-support contracts.
- `OWNER_MAP.md`: release-support owner boundary and stronger-owner split.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `ROADMAP.md`: current and next release-support contour.
- `LANDING_LOG.md`: checked release-support landing ledger.
- `PROVENANCE.md`: controlled bridge to legacy and source accounting.
- `legacy/`: archival source material, not active law.
- `docs/`: detailed doctrine and support notes.

## Post-change route review

After any release-support change, check whether the move changed:

- `DIRECTION.md`: current transition, release, or public-support posture.
- `PARTS.md`: active part boundaries or state-transition route.
- `OWNER_MAP.md`: owner boundary, stop-line, or handoff target.
- `OWNER_REQUESTS.md` and `mechanics/owner-request-queue.json`: release,
  proof, runtime, public projection, SDK, or owner-local asks.
- `ROADMAP.md`: future route pressure or unresolved release contour.
- `LANDING_LOG.md`: a checked landing or planted contract.
- `PROVENANCE.md`: source bridge, receipt route, or archive map.
- `CHANGELOG.md`, root `ROADMAP.md`, or release protocol surfaces: only when
  repo-level release semantics actually changed.
- `mechanics/registry.json` and generated indexes: card-facing route, owner
  boundary, validation refs, or public summaries.

Only update a surface when its meaning moved. Leave it untouched when the
change does not affect its job.

## Validation

Run `python scripts/mechanics_topology/validate_mechanics_topology.py --mechanic release-support`
after package changes.

For active-part or transition-law changes, run:

```bash
python mechanics/release-support/scripts/validate_release_support_distillation.py
```

### Routed child validation

Child-specific commands are source-owned by `mechanics/validation-routes.json`.
Run `python scripts/mechanics_topology/run_validation_route.py --surface <repo-relative-path>`;
add `--show` to inspect the route without executing it.

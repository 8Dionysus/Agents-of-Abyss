# Release Preflight Route Surface

Status: accepted
Date: 2026-04-30

## Context

The active center release runbook lives in
`mechanics/release-support/docs/RELEASING.md`, but the federation release
preflight checks for a repo-level `docs/RELEASING.md` entry. Without that
surface, the center can pass local release validation while failing the
federation publish gate.

## Options considered

1. Change the release helper to accept only the mechanic runbook path.
2. Add a concise repo-level release route that points to the release-support
   mechanic and stays current in the docs-root surface index.

## Decision

Keep `mechanics/release-support/docs/RELEASING.md` as the active release-support
runbook, and add `docs/RELEASING.md` as the repo-level GitHub release route
required by release preflight.

## Rationale

The repo-level route gives release tooling and future agents a stable,
auditable entry without moving release-support doctrine out of its mechanic
home. It also keeps the `docs/` root honest: current release routing is visible
there, while detailed transition law remains in the owning package.

## Consequences

- Release preflight can verify that this repository exposes a release route.
- Future release work has a short docs entry and a deeper mechanic runbook.
- The docs-root allowlist must include `RELEASING.md` so cleanup guardrails do
  not treat the release entry as stray material.

## Source surfaces

- `docs/RELEASING.md`
- `docs/guardrails/CURRENT_SURFACE_INDEX.md`
- `docs/guardrails/thematic_districts.json`
- `mechanics/release-support/docs/RELEASING.md`
- `scripts/validate_mechanics_topology.py`

## Follow-up route

If the federation release helper changes its required release-doc path, update
`docs/RELEASING.md`, the docs-root surface index, and the release-support
runbook together.

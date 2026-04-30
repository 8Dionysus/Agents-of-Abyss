# Root Scripts District Contract

Status: accepted
Date: 2026-04-30

## Context

The root `scripts/` district had become the release-facing execution seam for
center validators, builders, hygiene checks, mechanics topology checks, and
generated-surface freshness checks. After mechanic-owned scripts moved into
`mechanics/<slug>/.../scripts/`, the root script guidance still carried
historical wave-specific names and did not have a machine-readable map that
kept new root scripts from appearing unowned.

## Options considered

1. Keep `scripts/README.md` and `scripts/AGENTS.md` as long hand-maintained
   lists.
2. Move all scripts into mechanic or district folders.
3. Keep root scripts for root-owned center tooling and add a registry-backed
   district contract.

## Decision

Root `scripts/` keeps root-owned center tooling and is governed by
`scripts/registry.json`. Mechanic-owned scripts stay in their owning mechanic
or part. The scripts district validator checks that every root Python script is
registered in exactly one family and that mechanic script-home routes stay
visible.

## Rationale

The center still needs a small root execution seam for release checks, root
registries, docs districts, hygiene, AGENTS mesh, mechanics topology, and owner
request queues. Moving those scripts away from root would make the release
gate harder to read. Keeping only prose lists would let stale wave-era names
drift back into the active route.

A registry-backed district gives agents a compact map without turning the
folder into a semantic source of truth. It also matches the repo pattern now
used by config, schema, generated, and manifest districts.

## Consequences

- New root scripts must be registered before they are relied on.
- `release_check.py` now runs the scripts district validator.
- `scripts/README.md` and `scripts/AGENTS.md` can stay compact and family-led.
- The registry names script families, not detailed behavioral authority.
- Mechanic-local validation remains in `mechanics/<slug>/.../scripts/`.

## Source surfaces

- `scripts/README.md`
- `scripts/AGENTS.md`
- `scripts/registry.json`
- `scripts/validate_scripts_district.py`
- `tests/test_scripts_district.py`
- `scripts/release_check.py`

## Follow-up route

When a root script becomes mechanic-specific, move it to the owning mechanic or
part and update `scripts/registry.json`. When a new root release-facing script
appears, add it to one family or create a new family before wiring it into
`release_check.py`.

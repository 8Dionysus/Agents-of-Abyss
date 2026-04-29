# Traces District

This district holds repo-level movement receipts: move manifests, link-repair
traces, conflict receipts, and generic apply-script output.

Traces explain movement. They do not define meaning.

## District law

Keep this district small, reviewable, and labeled. A reader or agent should know
which source action produced a trace and which current surface owns the meaning
before citing it.

## Current surfaces

Add surfaces here only when they match the classifier in
[`../guardrails/thematic_districts.json`](../guardrails/thematic_districts.json)
and no more specific owner home exists. Keep this README as the local gate.

| Surface | Role |
|---|---|
| [`LINK_SHAPE_HYGIENE_APPLY_MANIFEST_2026_04_25.json`](LINK_SHAPE_HYGIENE_APPLY_MANIFEST_2026_04_25.json) | historical apply manifest for the link/shape hygiene package |
| [`HYGIENE_REPAIR_MANIFEST.json`](HYGIENE_REPAIR_MANIFEST.json) | link-repair trace written by the repair helper |

`DOCS_THEMATIC_MOVE_MANIFEST.json` may appear here only as output from
`scripts/plan_docs_thematic_cleanup.py --apply`.

`conflicts/` may appear only when thematic migration preserves a conflicting
source as a movement receipt.

## Belongs here

- generic docs movement manifests
- generic link-repair traces
- generic package apply manifests
- conflict receipts produced by migration tooling

## Routes away

| Material | Route |
|---|---|
| mechanic-specific source trace | `mechanics/<slug>/legacy/raw/` plus that mechanic `PROVENANCE.md` or `LANDING_LOG.md` |
| audit evidence, drift review, deletion candidates, or cleanup findings | `mechanics/audit/` or `mechanics/audit/legacy/raw/` |
| decision rationale | `docs/decisions/` |
| generated read model | `generated/` |
| owner-local truth | the owning repository |

## Mechanic connection

Mechanics may cite a trace as evidence, but the owning mechanic or owner
repository decides meaning. Generic repo movement stays here. Mechanic-owned
history stays with the mechanic.

Other repositories should create a trace district only after they have real
movement receipts to preserve. Do not add empty trace doors.

## Must not claim

Traces explain movement, not meaning.

Do not use this district to absorb owner-local truth from sibling repositories.

Do not put mechanic-specific receipts here when a mechanic package can own
`legacy/raw/` and `PROVENANCE.md`.

## Promotion path

A document in this district may influence current law only when a change names
the surviving canonical surface, updates links, rebuilds generated indexes, and
runs the docs thematic cleanup validators.

## Validation

Use the nearest `AGENTS.md` for the current command lane.

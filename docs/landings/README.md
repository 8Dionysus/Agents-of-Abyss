# Landing Receipts

This directory holds historical seed manifests and wave receipts that should remain reviewable but should not stand in repository root as civic law.

A landing receipt may explain what a wave planted, why it belonged in the center, and how it was validated. It should not become the canonical doctrine for the mechanic after the deeper surfaces have landed.

Canonical mechanic landing ledgers now live one level up:

- [`AGON_LANDING_LOG`](../../mechanics/agon/LANDING_LOG.md)
- [`EXPERIENCE_LANDING_LOG`](../../mechanics/experience/LANDING_LOG.md)

Use this directory for archived receipts and seed manifests. Use the
LANDING_LOG surfaces for active mechanic landing history, required validators,
owner boundaries, and stop-lines.

## District law

Landing receipts preserve provenance. They may explain what a wave planted, but
they must route current mechanic doctrine to the owning mechanic package.

## Current surfaces

| Surface | Role |
|---|---|
| [`AGON_WAVE3_SEED_MANIFEST`](AGON_WAVE3_SEED_MANIFEST.md) | moved root seed manifest for Agon Wave III lawful move language |

## Must not claim

Receipts do not prove owner-local implementation.

Do not use this district to absorb owner-local truth from sibling repositories.

## Promotion path

A later docs-architecture pass may decide whether more historical receipt files
should move here. That migration should update links, LANDING_LOG entries,
validators, generated capsules, and tests together.

## Validation

```bash
python scripts/plan_docs_thematic_cleanup.py --check
python scripts/validate_docs_thematic_districts.py
python scripts/build_docs_thematic_index.py --check
python scripts/validate_docs_thematic_index.py
```

# Schema District

This directory holds machine-readable shape contracts for center-planted surfaces.

A schema checks shape. It does not prove truth, grant authority, or replace the source document that gives meaning to the object.

## Main families

| Family | Examples | Meaning |
|---|---|---|
| Center and federation | `center-entry-map.schema.json`, `ecosystem-registry.schema.json` | compact center and registry contracts |
| Agon | `agon-*.schema.json`, `agon-*.json` | pre-protocol and candidate grammar shapes |
| Experience | `experience-v*.schema.json` | staged Experience contract shapes |
| Runtime-boundary doctrine | `constitution_runtime_*.json` | center-side boundary contracts, not runtime implementation |
| Audit and pruning | `deletion_candidate_list_v1.json` | audit artifact shape, not deletion command |
| Office and authority surfaces | `assistant_office_*.json`, `authority_resolution_v1.json` | center contract shapes for office/authority posture |

## Rules

- A schema must have a source document, builder, validator, or generated surface that explains why the shape exists.
- A schema must not become the source of meaning by itself.
- If a schema changes, update the nearest builder, validator, generated artifact, and test.
- Do not widen a schema to make weak data pass.
- Do not add runtime authority through a schema name or field.

## Before editing

1. Identify the source document that owns the semantics.
2. Identify the generated artifact or validator that consumes the schema.
3. Check [`docs/MECHANICS.md`](../docs/MECHANICS.md) if the schema belongs to Agon, Experience, recurrence, quest/RPG, or another mechanic.
4. Run the nearest validator and `python -m pytest -q tests`.

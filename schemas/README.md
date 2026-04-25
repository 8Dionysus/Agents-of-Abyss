# Schema District

This directory holds machine-readable shape contracts for center-planted surfaces.

A schema checks shape. It does not prove truth, grant authority, or replace the source document that gives meaning to the object.

Mechanic-owned schemas live in `mechanics/<slug>/schemas/`. Root paths such as
`schemas/agon-*` may exist as compatibility aliases only.

## Main families

| Family | Examples | Meaning |
|---|---|---|
| Center and federation | `center-entry-map.schema.json`, `ecosystem-registry.schema.json` | compact center and registry contracts |
| Mechanic aliases | `agon-*`, `experience-*`, `dual_vocabulary_overlay.schema.json`, `deletion_candidate_list_v1.json` | stable root routes to mechanic-owned schemas |

## Rules

- A schema must have a source document, builder, validator, or generated surface that explains why the shape exists.
- A schema must not become the source of meaning by itself.
- If a schema changes, update the nearest builder, validator, generated artifact, and test.
- Do not widen a schema to make weak data pass.
- Do not add runtime authority through a schema name or field.

## Before editing

1. Identify the source document that owns the semantics.
2. Identify the generated artifact or validator that consumes the schema.
3. Check [`mechanics/README.md`](../mechanics/README.md) if the schema belongs to Agon, Experience, RPG, antifragility, questbook, or another mechanic.
4. Run the nearest validator and `python -m pytest -q tests`.

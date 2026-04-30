# Schema District

`schemas/` owns root-level machine-readable shape contracts for center
publication surfaces. Mechanic-owned schemas live with their owning mechanic or
part.

A schema constrains shape. Source docs, builders, validators, and owner
surfaces still own meaning.

## Current Surface

| Surface | Role |
|---|---|
| [`registry.json`](registry.json) | canonical registry of root schemas and schema-home routes |

## Root Contracts

| Schema | Consumer |
|---|---|
| [`center-entry-map.schema.json`](center-entry-map.schema.json) | `generated/center_entry_map.min.json` |
| [`ecosystem-registry.schema.json`](ecosystem-registry.schema.json) | `generated/ecosystem_registry.min.json` |
| [`federation-supporting-inventory.schema.json`](federation-supporting-inventory.schema.json) | `generated/federation_supporting_inventory.min.json` |

## Schema Homes

| Home | Role |
|---|---|
| `mechanics/<slug>/schemas/` | mechanic-level schema contracts |
| `mechanics/<slug>/parts/<part>/schemas/` | part-local mechanic schema contracts |

## Source Order

When a schema and another surface disagree, read authority in this order:

1. owner source document or mechanic package
2. builder, validator, or seed config that produces the object
3. schema contract
4. generated or derived consumer surface

## Editing Route

- Add root schemas here only for root-owned center contracts.
- Add mechanic schemas under the owning mechanic or part.
- Update `registry.json` when a root schema or schema home route changes.
- Keep generated surfaces, validators, and tests aligned with schema changes.

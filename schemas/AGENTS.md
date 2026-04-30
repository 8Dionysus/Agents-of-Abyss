# AGENTS.md

## Applies to

This card applies to `schemas/` and every nested path under that scope until a
nearer `AGENTS.md` narrows the lane.

## Role

`schemas/` owns root-level JSON schema contracts and the registry that routes
agents to schema homes. It keeps root shape contracts visible without absorbing
mechanic-owned schemas.

## Read before editing

Read root `AGENTS.md`, local `README.md`, `schemas/registry.json`, and the
source surface named by the schema registry entry.

Use mechanic package guidance for schemas under `mechanics/<slug>/`.

## Boundaries

- Root `schemas/` owns root center contracts.
- Mechanic schemas belong with the owning mechanic or part.
- `ecosystem-registry.schema.json` is a public center registry contract; any
  contract change to `$id`, visibility, maturity, relation, kind, or required
  fields must stay aligned with `validate_ecosystem.py`.
- Do not widen a schema just to make weak or inconsistent data pass.
- Do not use schema names or fields to create runtime authority, owner
  acceptance, or source meaning.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

```bash
python scripts/validate_schema_registry.py
python -m pytest -q tests/test_schema_district.py
python scripts/validate_ecosystem.py
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_generated_freshness.py
```

For release-facing schema changes, also run:

```bash
python scripts/release_check.py
```

## Closeout

Report schema registry entries changed, root schemas touched, source surfaces
consulted, generated files rebuilt or intentionally left untouched, checks run,
checks skipped, and the owner route when a schema belongs outside root.

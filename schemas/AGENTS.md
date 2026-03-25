# AGENTS.md

This file applies to JSON schema contracts under `schemas/`.

## Role of this directory

`ecosystem-registry.schema.json` defines the contract for `generated/ecosystem_registry.min.json`.
It is the boundary surface for the shape of the AoA center's machine-readable registry.

## Editing posture

Treat any schema change here as a contract change.

When editing the schema:

- keep `$schema`, `$id`, required keys, and enums explicit
- preserve alignment with `generated/ecosystem_registry.min.json`
- update `scripts/validate_ecosystem.py` when the allowed shape or allowed values change
- prefer additive clarity over casual churn
- make shared-maturity and status changes intentionally, because they change public interpretation

Do not widen the schema casually just to make inconsistent data pass.
If the schema changes, the docs and registry should explain why.

## Validation

After changing `ecosystem-registry.schema.json`, run:

```bash
python scripts/validate_ecosystem.py
```

If the schema change is intentional, mention the contract shift clearly in the review notes or changelog entry.

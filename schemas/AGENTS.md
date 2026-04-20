# AGENTS.md

This file applies to JSON schema contracts under `schemas/`.

## Role of this directory

`ecosystem-registry.schema.json` defines the contract for
`generated/ecosystem_registry.min.json`.
`agon-imposition-readiness.schema.json` defines the contract for
`generated/agon_imposition_readiness.min.json`.
`agon-lawful-move.schema.json` and `agon-lawful-move-registry.schema.json`
define the contracts for the Wave III lawful move vocabulary and registry.
`agon-move-owner-binding.schema.json` and
`agon-move-owner-binding-registry.schema.json` define the contracts for the
Wave IV owner-binding seed and registry.
These files are the boundary surfaces for tracked machine-readable center
publication, Wave 0 Agon readiness, Wave III lawful move language, and Wave IV
owner binding law.

## Editing posture

Treat any schema change here as a contract change.

When editing the schema:

- keep `$schema`, `$id`, required keys, and enums explicit
- preserve alignment with the corresponding generated surface
- update the matching validator or builder when the allowed shape or allowed
  values change
- prefer additive clarity over casual churn
- make shared-maturity and status changes intentionally, because they change public interpretation

Do not widen the schema casually just to make inconsistent data pass.
If the schema changes, the docs and registry should explain why.

## Validation

After changing `ecosystem-registry.schema.json`, run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_ecosystem.py
```

After changing `agon-imposition-readiness.schema.json`, also run:

```bash
python scripts/build_agon_imposition_readiness.py --check
python scripts/validate_agon_imposition_readiness.py
python -m pytest -q tests/test_agon_imposition_readiness.py
```

After changing the Wave III lawful move schemas, also run:

```bash
python scripts/build_agon_lawful_move_registry.py --check
python scripts/validate_agon_lawful_moves.py
python -m pytest -q tests/test_agon_lawful_moves.py
```

After changing the Wave IV owner-binding schemas, also run:

```bash
python scripts/build_agon_move_owner_binding_registry.py --check
python scripts/validate_agon_move_owner_bindings.py
python -m pytest -q tests/test_agon_move_owner_bindings.py
```

If a schema change is intentional, mention the contract shift clearly in the
review notes or changelog entry.

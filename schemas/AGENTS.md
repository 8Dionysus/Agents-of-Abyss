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
`agon-gate-routing-handoff-request.schema.json` defines the contract for the
Wave V center handoff request.
`experience-wave1-flow.schema.json` defines the contract for the first
experience-capture kernel example.
`experience-wave2-certification-watchtower.schema.json` defines the contract
for the second experience wave's certification and contract-only watchtower
example.
`experience-wave3-federation-adoption.schema.json` defines the contract for the
third experience wave's federation harvest and owner-local adoption example.
`experience-wave4-polis-constitution.schema.json` defines the contract for the
fourth experience wave's polis governance and constitution runtime example.
These files are the boundary surfaces for tracked machine-readable center
publication, Wave 0 Agon readiness, Wave III lawful move language, Wave IV
owner binding law, the Wave V gate-routing handoff, and the Experience Wave 1
center kernel plus the Experience Wave 2 certification/watchtower center and
Experience Wave 3 federation/adoption center plus the Experience Wave 4
polis/constitution center.

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

After changing the Wave V gate-routing handoff schema, also run:

```bash
python scripts/build_agon_gate_routing_handoff_request.py --check
python scripts/validate_agon_gate_routing_handoff_request.py
python -m pytest -q tests/test_agon_gate_routing_handoff_request.py
```

After changing the Experience Wave 1 schema, also run:

```bash
python scripts/validate_experience_wave1.py
python -m pytest -q tests/test_experience_wave1.py
```

After changing the Experience Wave 2 schema, also run:

```bash
python scripts/validate_experience_wave2.py
python -m pytest -q tests/test_experience_wave2.py
```

After changing the Experience Wave 3 schema, also run:

```bash
python scripts/validate_experience_wave3.py
python -m pytest -q tests/test_experience_wave3.py
```

After changing the Experience Wave 4 schema, also run:

```bash
python scripts/validate_experience_wave4.py
python -m pytest -q tests/test_experience_wave4.py tests/test_experience_wave4_seed_contracts.py
```

If a schema change is intentional, mention the contract shift clearly in the
review notes or changelog entry.

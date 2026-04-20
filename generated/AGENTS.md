# AGENTS.md

This file applies to compact machine-readable publication surfaces under `generated/`.

## Role of this directory

`generated/ecosystem_registry.min.json` is the current compact machine-readable registry for AoA center-layer routing.
It summarizes repository names, roles, statuses, shared maturity, and kind for the public ecosystem map.
`generated/federation_supporting_inventory.min.json` is the companion machine-readable inventory for supporting consumer/control-plane surfaces that stay outside compact registry v1.
`generated/agon_imposition_readiness.min.json` is the tracked Wave 0 readiness capsule for the center-owned Agon imposition gate.
`generated/agon_lawful_move_registry.min.json` is the tracked Wave III lawful
move registry for the center-owned pre-protocol legal vocabulary.

This directory is derived in purpose, but the registry is currently maintained as a tracked JSON artifact inside this repository.
Treat it as a published summary surface, not a hidden second charter.

## Editing posture

When editing `ecosystem_registry.min.json` or `federation_supporting_inventory.min.json`:

- keep it aligned with `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/LAYERS.md`, and `docs/FEDERATION_RULES.md`
- preserve the current field contract around `name`, `role`, `status`, `shared_maturity`, and `kind`
- keep entries compact, explicit, and reviewable
- do not smuggle layer-owned implementation detail, speculative repos, or private assumptions into the registry
- keep compact registry v1 and supporting inventory boundaries explicit instead of blurring them together
- prefer the smallest coherent change that keeps the center more legible

When editing `agon_imposition_readiness.min.json`:

- keep it aligned with `docs/AGON_IMPOSITION_POSTURE.md`,
  `docs/AGON_SURVIVAL_CRITERIA.md`, `docs/AGON_DOUBT_AUDIT.md`,
  `docs/PRE_AGON_BASELINE.md`, and
  `schemas/agon-imposition-readiness.schema.json`
- treat `scripts/build_agon_imposition_readiness.py` as the canonical builder
  and `scripts/validate_agon_imposition_readiness.py` as the explicit Wave 0
  validator
- keep the capsule additive and witness-shaped; it must not become a shadow
  arena protocol or readiness government

When editing `agon_lawful_move_registry.min.json`:

- keep it aligned with `docs/AGON_LAWFUL_MOVE_LANGUAGE.md`,
  `docs/AGON_MOVE_REGISTRY_MODEL.md`,
  `docs/AGON_MOVE_OWNER_HANDOFFS.md`, and
  `config/agon_lawful_moves.seed.json`
- treat `scripts/build_agon_lawful_move_registry.py` as the canonical builder
  and `scripts/validate_agon_lawful_moves.py` as the explicit Wave III
  validator
- keep every move explicitly pre-protocol; the registry must not become a
  shadow arena runtime, verdict government, scar ledger, or retention engine

There is no builder script for the compact registry or supporting inventory
surfaces today. If that changes later, update this guide and
`scripts/validate_ecosystem.py` together.

## Validation

After changing a generated center inventory surface, run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_ecosystem.py
python -m pytest -q tests
```

After changing the Agon readiness capsule, also run:

```bash
python scripts/build_agon_imposition_readiness.py --check
python scripts/validate_agon_imposition_readiness.py
python -m pytest -q tests/test_agon_imposition_readiness.py
```

After changing the Agon lawful move registry, also run:

```bash
python scripts/build_agon_lawful_move_registry.py --check
python scripts/validate_agon_lawful_moves.py
python -m pytest -q tests/test_agon_lawful_moves.py
```

A registry edit is only done when the JSON, the schema, and the center-layer prose still agree.

# AGENTS.md

This file applies to compact machine-readable publication surfaces under `generated/`.

## Role of this directory

`generated/ecosystem_registry.min.json` is the current compact machine-readable registry for AoA center-layer routing.
It summarizes repository names, roles, statuses, shared maturity, and kind for the public ecosystem map.

This directory is derived in purpose, but the registry is currently maintained as a tracked JSON artifact inside this repository.
Treat it as a published summary surface, not a hidden second charter.

## Editing posture

When editing `ecosystem_registry.min.json`:

- keep it aligned with `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/LAYERS.md`, and `docs/FEDERATION_RULES.md`
- preserve the current field contract around `name`, `role`, `status`, `shared_maturity`, and `kind`
- keep entries compact, explicit, and reviewable
- do not smuggle layer-owned implementation detail, speculative repos, or private assumptions into the registry
- prefer the smallest coherent change that keeps the center more legible

There is no builder script for this file today.
If that changes later, update this guide and `scripts/validate_ecosystem.py` together.

## Validation

After changing the registry, run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_ecosystem.py
```

A registry edit is only done when the JSON, the schema, and the center-layer prose still agree.

# AGENTS.md

This file applies to compact machine-readable publication surfaces under `generated/`.

## Role of this directory

`generated/ecosystem_registry.min.json` is the current compact machine-readable registry for AoA center-layer routing.
It summarizes repository names, roles, statuses, shared maturity, and kind for the public ecosystem map.
`generated/federation_supporting_inventory.min.json` is the companion machine-readable inventory for supporting consumer/control-plane surfaces that stay outside compact registry v1.
`generated/center_entry_map.min.json` is the compact machine-facing route
capsule for the shared `Start here` contract.
`generated/agon_imposition_readiness.min.json` is the tracked Wave 0 readiness capsule for the center-owned Agon imposition gate.
`generated/agon_lawful_move_registry.min.json` is the tracked Wave III lawful
move registry for the center-owned pre-protocol legal vocabulary.
`generated/agon_move_owner_binding_registry.min.json` is the tracked Wave IV
owner-binding registry for the center-owned pre-protocol owner-binding law.
`generated/agon_gate_routing_handoff_request.min.json` is the tracked Wave V
center handoff request for thin pre-protocol Agon gate routing.

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

When editing `center_entry_map.min.json`:

- rebuild it with `scripts/build_center_entry_map.py`
- keep it aligned with `docs/START_HERE_ROUTE_CONTRACT.md`, `README.md`,
  `AGENTS.md`, `docs/README.md`, `CONTRIBUTING.md`, `mechanics/README.md`, and
  `mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md`
- run `scripts/validate_entry_surface_sync.py` so route modes remain visible
  across human and generated entry surfaces
- do not let the compact route capsule replace authored human docs

When editing `agon_imposition_readiness.min.json`:

- keep it aligned with `mechanics/agon/docs/AGON_IMPOSITION_POSTURE.md`,
  `mechanics/agon/docs/AGON_SURVIVAL_CRITERIA.md`, `mechanics/agon/docs/AGON_DOUBT_AUDIT.md`,
  `mechanics/agon/docs/PRE_AGON_BASELINE.md`, and
  `schemas/agon-imposition-readiness.schema.json`
- treat `scripts/build_agon_imposition_readiness.py` as the canonical builder
  and `scripts/validate_agon_imposition_readiness.py` as the explicit Wave 0
  validator
- keep the capsule additive and witness-shaped; it must not become a shadow
  arena protocol or readiness government

When editing `agon_lawful_move_registry.min.json`:

- keep it aligned with `mechanics/agon/docs/AGON_LAWFUL_MOVE_LANGUAGE.md`,
  `mechanics/agon/docs/AGON_MOVE_REGISTRY_MODEL.md`,
  `mechanics/agon/docs/AGON_MOVE_OWNER_HANDOFFS.md`, and
  `config/agon_lawful_moves.seed.json`
- treat `scripts/build_agon_lawful_move_registry.py` as the canonical builder
  and `scripts/validate_agon_lawful_moves.py` as the explicit Wave III
  validator
- keep every move explicitly pre-protocol; the registry must not become a
  shadow arena runtime, verdict government, scar ledger, or retention engine

When editing `agon_move_owner_binding_registry.min.json`:

- keep it aligned with `mechanics/agon/docs/AGON_MOVE_OWNER_BINDING.md`,
  `mechanics/agon/docs/AGON_MOVE_BINDING_MATRIX_MODEL.md`,
  `mechanics/agon/docs/AGON_OWNER_REPO_REQUESTS.md`,
  `mechanics/agon/docs/AGON_PRE_PROTOCOL_STOP_LINES.md`, and
  `config/agon_move_owner_bindings.seed.json`
- treat `scripts/build_agon_move_owner_binding_registry.py` as the canonical
  builder and `scripts/validate_agon_move_owner_bindings.py` as the explicit
  Wave IV validator
- keep `Agents-of-Abyss` as the legal owner on every binding while all
  non-center owner references stay `requested_not_landed`
- keep every binding explicitly pre-protocol; the registry must not become a
  shadow owner-landing ledger, live arena runtime, verdict government, scar
  ledger, retention engine, or ToS promotion path

When editing `agon_gate_routing_handoff_request.min.json`:

- keep it aligned with `mechanics/agon/docs/AGON_GATE_ROUTING_HANDOFF.md`,
  `mechanics/agon/docs/AGON_GATE_ROUTING_OWNER_REQUEST.md`,
  `mechanics/agon/docs/AGON_GATE_ROUTING_STOP_LINES.md`,
  `mechanics/agon/docs/AGON_WAVE5_CENTER_HANDOFF.md`, and
  `config/agon_gate_routing_handoff_request.seed.json`
- treat `scripts/build_agon_gate_routing_handoff_request.py` as the canonical
  builder and `scripts/validate_agon_gate_routing_handoff_request.py` as the
  explicit Wave V validator
- keep the handoff explicitly pre-protocol; it must not become a shadow arena
  activation record, routing-owned Agon law, verdict government, scar ledger,
  retention engine, runtime dispatch authority, or ToS promotion path

There is no builder script for the compact registry or supporting inventory
surfaces today. If that changes later, update this guide and
`scripts/validate_ecosystem.py` together.

## Validation

After changing a generated center inventory surface, run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_entry_surface_sync.py
python scripts/validate_ecosystem.py
python -m pytest -q tests
```

After changing the center entry map, also run:

```bash
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
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

After changing the Agon move owner binding registry, also run:

```bash
python scripts/build_agon_move_owner_binding_registry.py --check
python scripts/validate_agon_move_owner_bindings.py
python -m pytest -q tests/test_agon_move_owner_bindings.py
```

After changing the Agon gate routing handoff request, also run:

```bash
python scripts/build_agon_gate_routing_handoff_request.py --check
python scripts/validate_agon_gate_routing_handoff_request.py
python -m pytest -q tests/test_agon_gate_routing_handoff_request.py
```

A registry edit is only done when the JSON, the schema, and the center-layer prose still agree.

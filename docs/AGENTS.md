# AGENTS.md

This file applies to center-layer doctrine under `docs/`.

## Role of this directory

`docs/` is the doctrine-and-map surface for the AoA center.
It explains how the federation is shaped and how it should grow without collapsing source-of-truth boundaries.

Important documents here include:

- `README.md` as the human-first map of the docs surface.
- `LAYERS.md` for the conceptual layer model.
- `REPO_ROLES.md` for compact ownership routing.
- `FEDERATION_RULES.md` for source-of-truth boundaries.
- `ROOT_SURFACE_LAW.md` for root placement and cleanup law.
- `START_HERE_ROUTE_CONTRACT.md` for public entry route modes.
- `MECHANICS.md` as a compatibility route to `../mechanics/README.md`.
- `THEMATIC_DISTRICT_PROTOCOL.md`, `CURRENT_SURFACE_INDEX.md`, and
  `thematic_districts.json` for old-to-current docs cleanup.

Mechanic-owned doctrine now lives under `../mechanics/`.
Use `../mechanics/AGENTS.md` and the nearest `../mechanics/<slug>/AGENTS.md`
before editing Agon, Experience, recurrence, method-growth, antifragility,
questbook, RPG, ToS-bridge, or release-support surfaces.
The former docs-root mechanic anchors now route through packages, including
`ROOTLINE.md`, `METHOD_SPINE.md`, `COUNTERPART_BRIDGE.md`, and
`WITNESS_COMPOST.md`.

## Editing posture

Keep docs compact, declarative, and routing-aware.

When editing:

- prefer boundaries, roles, and relationships over implementation detail
- route readers to neighboring AoA repositories instead of restating their internals
- keep AoA versus `Tree-of-Sophia` ownership boundaries explicit
- update related center-layer documents coherently when terminology or wave doctrine changes
- preserve chronological naming and sequence across rootline and later-wave support docs

Do not let this directory become a shadow corpus for techniques, skills, evals, memory objects, runtime configs, or ToS-authored meaning.

Historical, evidential, and support material should live in the nearest
thematic district such as `agent-lane/`, `audits/`, `landings/`, `registry/`,
`decisions/`, `postmortems/`, `traces/`, `agon/`, `experience/`, or `legacy/`.

## Validation

After changing docs here, review the connected center-layer surfaces:

- `README.md`
- `CHARTER.md`
- `ECOSYSTEM_MAP.md`
- `ROADMAP.md`
- `generated/ecosystem_registry.min.json`

Then run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/plan_docs_thematic_cleanup.py --check
python scripts/validate_docs_thematic_districts.py
python scripts/validate_docs_migration_map.py
python scripts/build_docs_thematic_index.py --check
python scripts/validate_docs_thematic_index.py
python scripts/validate_ecosystem.py
python -m pytest -q tests
```

If you changed the Agon imposition surfaces, also run:

```bash
python scripts/build_agon_imposition_readiness.py --check
python scripts/validate_agon_imposition_readiness.py
python -m pytest -q tests/test_agon_imposition_readiness.py
```

If you changed the Agon lawful move language surfaces, also run:

```bash
python scripts/build_agon_lawful_move_registry.py --check
python scripts/validate_agon_lawful_moves.py
python -m pytest -q tests/test_agon_lawful_moves.py
```

If you changed the Agon move owner binding surfaces, also run:

```bash
python scripts/build_agon_move_owner_binding_registry.py --check
python scripts/validate_agon_move_owner_bindings.py
python -m pytest -q tests/test_agon_move_owner_bindings.py
```

If you changed the Agon gate routing handoff surfaces, also run:

```bash
python scripts/build_agon_gate_routing_handoff_request.py --check
python scripts/validate_agon_gate_routing_handoff_request.py
python -m pytest -q tests/test_agon_gate_routing_handoff_request.py
```

If you changed the Experience Wave 1 surfaces, also run:

```bash
python scripts/validate_experience_wave1.py
python -m pytest -q tests/test_experience_wave1.py
```

If you changed the Experience Wave 2 surfaces, also run:

```bash
python scripts/validate_experience_wave2.py
python -m pytest -q tests/test_experience_wave2.py
```

If you changed the Experience Wave 3 surfaces, also run:

```bash
python scripts/validate_experience_wave3.py
python -m pytest -q tests/test_experience_wave3.py
```

If you changed the Experience Wave 4 surfaces, also run:

```bash
python scripts/validate_experience_wave4.py
python -m pytest -q tests/test_experience_wave4.py tests/test_experience_wave4_seed_contracts.py
```

If you changed the Experience Wave 5 surfaces, also run:

```bash
python scripts/validate_experience_wave5.py
python -m pytest -q tests/test_experience_wave5.py
```

If you changed the Experience v1.2-v2.0 bridge surfaces, also run:

```bash
python scripts/validate_experience_v1_2_to_v2_0_bridge.py
python -m pytest -q tests/test_experience_v1_2_to_v2_0_bridge.py
```

If you changed the Experience v1.2 service mesh operations surfaces, also run:

```bash
python scripts/validate_experience_v1_2_service_mesh_operations.py
python -m pytest -q tests/test_experience_v1_2_service_mesh_operations.py
```

If you changed the Experience v1.3 office foundry role-pair surfaces, also run:

```bash
python scripts/validate_experience_v1_3_office_foundry_role_pairs.py
python -m pytest -q tests/test_experience_v1_3_office_foundry_role_pairs.py
```

If you changed the Experience v1.4 mechanical arena kernel surfaces, also run:

```bash
python scripts/validate_experience_v1_4_agonic_pair_trials_mechanical_arena_kernel.py
python -m pytest -q tests/test_experience_v1_4_agonic_pair_trials_mechanical_arena_kernel.py
```

If you changed the Experience v1.5 epistemic duel model-of-other forge surfaces, also run:

```bash
python scripts/validate_experience_v1_5_epistemic_duel_model_of_other_forge.py
python -m pytest -q tests/test_experience_v1_5_epistemic_duel_model_of_other_forge.py
```

If you changed ownership, routing, or maturity language, confirm the machine-readable registry still matches the prose.

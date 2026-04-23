# AGENTS.md

This file applies to center-layer doctrine under `docs/`.

## Role of this directory

`docs/` is the doctrine-and-map surface for the AoA center.
It explains how the federation is shaped and how it should grow without collapsing source-of-truth boundaries.

Important documents here include:

- `README.md` as the human-first map of the docs surface
- `LAYERS.md` for the conceptual layer model
- `REPO_ROLES.md` for compact ownership routing
- `FEDERATION_RULES.md` for source-of-truth boundaries
- `ROOTLINE.md` for the trunk-first planting spine
- `RECURRENCE_PRINCIPLE.md` for the standing recovery law when a route loses axis and must regain a valid anchor
- `METHOD_SPINE.md` for the second-wave method doctrine
- `COUNTERPART_BRIDGE.md` for bounded counterpart and KAG restraint
- `WITNESS_COMPOST.md` for the witness and compost pilot
- `AGON_PREPARATION_POSTURE.md`, `AGON_IMPOSITION_POSTURE.md`,
  `AGON_SURVIVAL_CRITERIA.md`, `AGON_DOUBT_AUDIT.md`,
  `PRE_AGON_BASELINE.md`, and `AGON_WAVE0_LANDING.md` for the center-owned
  Agon holding boundary, first imposition turn, survival lens, audit frame,
  before-image, and landing order
- `AGON_LAWFUL_MOVE_LANGUAGE.md`, `AGON_MOVE_REGISTRY_MODEL.md`,
  `AGON_MOVE_OWNER_HANDOFFS.md`, and `AGON_WAVE3_LANDING.md` for the first
  pre-protocol lawful move vocabulary and its owner-handoff stop-lines
- `AGON_MOVE_OWNER_BINDING.md`, `AGON_MOVE_BINDING_MATRIX_MODEL.md`,
  `AGON_OWNER_REPO_REQUESTS.md`, `AGON_PRE_PROTOCOL_STOP_LINES.md`, and
  `AGON_WAVE4_LANDING.md` for the first owner-binding turn, its compact
  binding matrix, cross-repo request law, stop-lines, and landing order
- `AGON_GATE_ROUTING_HANDOFF.md`, `AGON_GATE_ROUTING_OWNER_REQUEST.md`,
  `AGON_GATE_ROUTING_STOP_LINES.md`, and `AGON_WAVE5_CENTER_HANDOFF.md` for
  the first center-owned gate-routing handoff, its owner request, stop-lines,
  and landing order
- `EXPERIENCE_WAVE1_KERNEL.md` for the first experience-capture kernel and
  its friction -> recurrence -> candidate -> verdict -> memory gate -> owner
  route -> inert projection order
- `EXPERIENCE_WAVE2_CERTIFICATION_WATCHTOWER.md` for the second experience
  wave, its v0.4 certification spine, v0.5 contract-only watchtower spine,
  and release/deployment authority stop-lines
- `EXPERIENCE_WAVE3_FEDERATION_ADOPTION.md` for the third experience wave,
  its v0.6 federation harvest spine, v0.7 owner-local adoption spine, and
  KAG/ToS/runtime/assistant stop-lines
- `EXPERIENCE_WAVE4_POLIS_CONSTITUTION.md` for the fourth experience wave,
  its v0.8 polis governance spine, v0.9 constitution runtime spine, and
  council/vote/stay/replay/precedent authority stop-lines
- `EXPERIENCE_WAVE5_SOVEREIGN_OFFICE.md` for the fifth experience wave, its
  v1.0 installation spine, v1.1 live-office spine, and release/office
  authority stop-lines
- `EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md` for the center bridge from the
  `Dionysus` v1.2-v2.0 intake line into future owner-local waves without
  treating archive transport as owner truth
- `EXPERIENCE_V1_2_SERVICE_MESH_OPERATIONS.md` for the v1.2 service mesh
  operations contract, office-failure rehearsal laws, owner routing, and
  no-runtime stop-lines
- `TOS_GROWTH_SUPPORT.md`, `TOS_TEMPLATE_SUPPORT.md`, `TOS_LINEAGE_PILOT_SUPPORT.md`, and `TOS_SOIL_PREP_SUPPORT.md` for current AoA support doctrine around `Tree-of-Sophia`

## Editing posture

Keep docs compact, declarative, and routing-aware.

When editing:

- prefer boundaries, roles, and relationships over implementation detail
- route readers to neighboring AoA repositories instead of restating their internals
- keep AoA versus `Tree-of-Sophia` ownership boundaries explicit
- update related center-layer documents coherently when terminology or wave doctrine changes
- preserve chronological naming and sequence across rootline and later-wave support docs

Do not let this directory become a shadow corpus for techniques, skills, evals, memory objects, runtime configs, or ToS-authored meaning.

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

If you changed ownership, routing, or maturity language, confirm the machine-readable registry still matches the prose.

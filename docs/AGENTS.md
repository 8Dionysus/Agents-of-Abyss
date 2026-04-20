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

If you changed ownership, routing, or maturity language, confirm the machine-readable registry still matches the prose.

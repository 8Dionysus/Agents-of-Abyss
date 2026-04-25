# AGENTS.md

## Applies to

This card applies to `docs/` and every nested path under that scope until a nearer `AGENTS.md` narrows the lane.

## Role

This AGENTS card keeps local work inside the Agents-of-Abyss center lane, names the nearest owner boundary, and routes wider claims back to the root card.

## Read before editing

Read the repository root `AGENTS.md`, this card, and the nearest `README.md` or protocol surface before changing files in this lane.

## Boundaries

Do not use this lane to override owner-local truth, generated-source boundaries, sibling-repo authority, or release validation contracts.

## Closeout

Closeout must name changed surfaces, checks run, checks skipped, remaining risk, and the next owner route if this lane was only a waypoint.

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
- `LINK_AND_SHAPE_HYGIENE_PROTOCOL.md`, `HYGIENE_GUARDRAIL_INDEX.md`, and
  `../config/link_shape_hygiene.json` for local link, Markdown shape, status
  vocabulary, and generated freshness guardrails.
- `AGENTS_MESH_PROTOCOL.md`, `AGENTS_MESH_INDEX.md`, and
  `../config/agents_mesh.json` for local AGENTS-card coverage, shape, and
  generated mesh guardrails.

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
python scripts/repair_known_link_drifts.py --check
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
python scripts/validate_status_vocabulary.py
python scripts/build_link_shape_hygiene_index.py --check
python scripts/validate_link_shape_hygiene_index.py
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
python scripts/validate_generated_freshness.py
python scripts/validate_hygiene_suite.py
python scripts/validate_ecosystem.py
python -m pytest -q
```

If you changed the Agon imposition surfaces, also run:

```bash
python mechanics/agon/scripts/build_agon_imposition_readiness.py --check
python mechanics/agon/scripts/validate_agon_imposition_readiness.py
python -m pytest -q mechanics/agon/tests/test_agon_imposition_readiness.py
```

If you changed the Agon lawful move language surfaces, also run:

```bash
python mechanics/agon/scripts/build_agon_lawful_move_registry.py --check
python mechanics/agon/scripts/validate_agon_lawful_moves.py
python -m pytest -q mechanics/agon/tests/test_agon_lawful_moves.py
```

If you changed the Agon move owner binding surfaces, also run:

```bash
python mechanics/agon/scripts/build_agon_move_owner_binding_registry.py --check
python mechanics/agon/scripts/validate_agon_move_owner_bindings.py
python -m pytest -q mechanics/agon/tests/test_agon_move_owner_bindings.py
```

If you changed the Agon gate routing handoff surfaces, also run:

```bash
python mechanics/agon/scripts/build_agon_gate_routing_handoff_request.py --check
python mechanics/agon/scripts/validate_agon_gate_routing_handoff_request.py
python -m pytest -q mechanics/agon/tests/test_agon_gate_routing_handoff_request.py
```

If you changed the Experience Wave 1 surfaces, also run:

```bash
python mechanics/experience/parts/capture-kernel/scripts/validate_capture_kernel.py
python -m pytest -q mechanics/experience/parts/capture-kernel/tests/test_capture_kernel.py
```

If you changed the Experience Wave 2 surfaces, also run:

```bash
python mechanics/experience/parts/certification-proof/scripts/validate_certification_proof.py
python -m pytest -q mechanics/experience/parts/certification-proof/tests/test_certification_proof.py
```

If you changed the Experience Wave 3 surfaces, also run:

```bash
python mechanics/experience/parts/adoption-federation/scripts/validate_adoption_federation.py
python -m pytest -q mechanics/experience/parts/adoption-federation/tests/test_adoption_federation.py
```

If you changed the Experience Wave 4 surfaces, also run:

```bash
python mechanics/experience/parts/governance-polis/scripts/validate_governance_polis.py
python -m pytest -q mechanics/experience/parts/governance-polis/tests/test_governance_polis.py mechanics/experience/parts/governance-polis/tests/test_governance_polis_seed_contracts.py
```

If you changed the Experience Wave 5 surfaces, also run:

```bash
python mechanics/experience/parts/office-operations/scripts/validate_office_operations.py
python -m pytest -q mechanics/experience/parts/office-operations/tests/test_office_operations.py
```

If you changed the Experience v1.2-v2.0 bridge surfaces, also run:

```bash
python mechanics/experience/parts/runtime-boundary/scripts/validate_runtime_boundary_bridge.py
python -m pytest -q mechanics/experience/parts/runtime-boundary/tests/test_runtime_boundary_bridge.py
```

If you changed the Experience v1.2 service mesh operations surfaces, also run:

```bash
python mechanics/experience/parts/service-mesh/scripts/validate_service_mesh.py
python -m pytest -q mechanics/experience/parts/service-mesh/tests/test_service_mesh.py
```

If you changed the Experience v1.3 office foundry role-pair surfaces, also run:

```bash
python mechanics/experience/parts/office-operations/scripts/validate_office_role_pairs.py
python -m pytest -q mechanics/experience/parts/office-operations/tests/test_office_role_pairs.py
```

If you changed the Experience v1.4 mechanical arena kernel surfaces, also run:

```bash
python mechanics/experience/parts/compatibility-bridges/scripts/validate_agonic_pair_trials_bridge.py
python -m pytest -q mechanics/experience/parts/compatibility-bridges/tests/test_agonic_pair_trials_bridge.py
```

If you changed the Experience v1.5 epistemic duel model-of-other forge surfaces, also run:

```bash
python mechanics/experience/parts/compatibility-bridges/scripts/validate_epistemic_duel_bridge.py
python -m pytest -q mechanics/experience/parts/compatibility-bridges/tests/test_epistemic_duel_bridge.py
```

If you changed ownership, routing, or maturity language, confirm the machine-readable registry still matches the prose.

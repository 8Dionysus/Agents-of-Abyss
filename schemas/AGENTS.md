# AGENTS.md

## Applies to

This card applies to `schemas/` and every nested path under that scope until a nearer `AGENTS.md` narrows the lane.

## Role

This AGENTS card keeps local work inside the Agents-of-Abyss center lane, names the nearest owner boundary, and routes wider claims back to the root card.

## Read before editing

Read the repository root `AGENTS.md`, this card, and the nearest `README.md` or protocol surface before changing files in this lane.

## Boundaries

Do not use this lane to override owner-local truth, generated-source boundaries, sibling-repo authority, or release validation contracts.

## Closeout

Closeout must name changed surfaces, checks run, checks skipped, remaining risk, and the next owner route if this lane was only a waypoint.

This file applies to JSON schema contracts under `schemas/`.

## Role of this directory

Root `schemas/` owns repository-wide shape contracts. Mechanic-owned schema
sources live under `mechanics/<slug>/schemas/`.

`ecosystem-registry.schema.json` defines the contract for
`generated/ecosystem_registry.min.json`.
`agon-imposition-readiness.schema.json` defines the contract for
`mechanics/agon/parts/imposition-readiness/generated/agon_imposition_readiness.min.json`.
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
`experience-v1-2-service-mesh-operations.schema.json` defines the contract for
the v1.2 service mesh operations center example.
`experience-v1-3-office-foundry-role-pairs.schema.json` defines the contract
for the v1.3 office foundry role-pairs center example.
`experience-v1-4-agonic-pair-trials-mechanical-arena-kernel.schema.json`
defines the contract for the v1.4 agonic pair trial and mechanical arena
kernel center example.
`experience-v1-5-epistemic-duel-model-of-other-forge.schema.json` defines the
contract for the v1.5 epistemic duel and model-of-other forge center example.
These files are the boundary surfaces for tracked machine-readable center
publication, Wave 0 Agon readiness, Wave III lawful move language, Wave IV
owner binding law, the Wave V gate-routing handoff, and the Experience Wave 1
center kernel plus the Experience Wave 2 certification/watchtower center and
Experience Wave 3 federation/adoption center plus the Experience Wave 4
polis/constitution center plus the v1.2-v1.5 planting campaign contracts.

## Editing posture

Treat any schema change here as a contract change.

When editing the schema:

- edit mechanic-owned schemas directly under `mechanics/<slug>/schemas/`
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
python mechanics/agon/parts/imposition-readiness/scripts/build_agon_imposition_readiness.py --check
python mechanics/agon/parts/imposition-readiness/scripts/validate_agon_imposition_readiness.py
python -m pytest -q mechanics/agon/parts/imposition-readiness/tests/test_agon_imposition_readiness.py
```

After changing the Wave III lawful move schemas, also run:

```bash
python mechanics/agon/parts/lawful-move-grammar/scripts/build_agon_lawful_move_registry.py --check
python mechanics/agon/parts/lawful-move-grammar/scripts/validate_agon_lawful_moves.py
python -m pytest -q mechanics/agon/parts/lawful-move-grammar/tests/test_agon_lawful_moves.py
```

After changing the Wave IV owner-binding schemas, also run:

```bash
python mechanics/agon/parts/owner-binding/scripts/build_agon_move_owner_binding_registry.py --check
python mechanics/agon/parts/owner-binding/scripts/validate_agon_move_owner_bindings.py
python -m pytest -q mechanics/agon/parts/owner-binding/tests/test_agon_move_owner_bindings.py
```

After changing the Wave V gate-routing handoff schema, also run:

```bash
python mechanics/agon/parts/gate-routing/scripts/build_agon_gate_routing_handoff_request.py --check
python mechanics/agon/parts/gate-routing/scripts/validate_agon_gate_routing_handoff_request.py
python -m pytest -q mechanics/agon/parts/gate-routing/tests/test_agon_gate_routing_handoff_request.py
```

After changing the Experience Wave 1 schema, also run:

```bash
python mechanics/experience/parts/capture-kernel/scripts/validate_capture_kernel.py
python -m pytest -q mechanics/experience/parts/capture-kernel/tests/test_capture_kernel.py
```

After changing the Experience Wave 2 schema, also run:

```bash
python mechanics/experience/parts/certification-proof/scripts/validate_certification_proof.py
python -m pytest -q mechanics/experience/parts/certification-proof/tests/test_certification_proof.py
```

After changing the Experience Wave 3 schema, also run:

```bash
python mechanics/experience/parts/adoption-federation/scripts/validate_adoption_federation.py
python -m pytest -q mechanics/experience/parts/adoption-federation/tests/test_adoption_federation.py
```

After changing the Experience Wave 4 schema, also run:

```bash
python mechanics/experience/parts/governance-polis/scripts/validate_governance_polis.py
python -m pytest -q mechanics/experience/parts/governance-polis/tests/test_governance_polis.py mechanics/experience/parts/governance-polis/tests/test_governance_polis_seed_contracts.py
```

After changing the Experience v1.2 or v1.3 campaign schemas, also run the matching contract validator and tests:

```bash
python mechanics/experience/parts/service-mesh/scripts/validate_service_mesh.py
python -m pytest -q mechanics/experience/parts/service-mesh/tests/test_service_mesh.py
python mechanics/experience/parts/office-operations/scripts/validate_office_role_pairs.py
python -m pytest -q mechanics/experience/parts/office-operations/tests/test_office_role_pairs.py
```

After changing the Experience v1.4 campaign schema, also run:

```bash
python mechanics/experience/parts/compatibility-bridges/scripts/validate_agonic_pair_trials_bridge.py
python -m pytest -q mechanics/experience/parts/compatibility-bridges/tests/test_agonic_pair_trials_bridge.py
```

After changing the Experience v1.5 campaign schema, also run:

```bash
python mechanics/experience/parts/compatibility-bridges/scripts/validate_epistemic_duel_bridge.py
python -m pytest -q mechanics/experience/parts/compatibility-bridges/tests/test_epistemic_duel_bridge.py
```

If a schema change is intentional, mention the contract shift clearly in the
review notes or changelog entry.

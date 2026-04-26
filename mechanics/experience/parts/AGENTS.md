# AGENTS.md

## Applies to

This card applies to `mechanics/experience/parts/` and all active Experience part packages.

## Role

Experience parts hold functioning contracts. They distill source pressure into readable center-owned direction, owner boundaries, and validation routes.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/experience/AGENTS.md`, `mechanics/experience/DIRECTION.md`, `mechanics/experience/PARTS.md`, and the part file you are changing.

## Boundaries

Do not move archival inventories into active part docs wholesale. Do not claim runtime activation, hidden memory authority, owner acceptance, proof verdicts, or ToS-authored meaning from this lane.

## Part evolution

A part may grow, split, merge, shrink, or retire when that improves its function.
Make the route cleaner and more useful; do not optimize for size alone. When a
part boundary changes, review `PARTS.md`, the package `ROADMAP.md`, owner
requests, validators, and the landing log before closing.

## Validation

Run:

```bash
python mechanics/experience/scripts/validate_experience_distillation.py
python scripts/validate_mechanic_artifact_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
python scripts/validate_mechanic_landing_logs.py --mechanic experience
```

<!-- centralized-child-validation:start -->

### Centralized Child Validation

Executable validation commands from child docs live here. Child docs should
route to this section instead of carrying command blocks.

#### `mechanics/experience/parts/adoption-federation/VALIDATION.md`

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part adoption-federation
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
python mechanics/experience/parts/adoption-federation/scripts/validate_adoption_federation.py
python -m pytest -q mechanics/experience/parts/adoption-federation/tests/test_adoption_federation.py
python scripts/validate_owner_request_queue.py --mechanic experience
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic experience
```

#### `mechanics/experience/parts/capture-kernel/VALIDATION.md`

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part capture-kernel
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
python mechanics/experience/parts/capture-kernel/scripts/validate_capture_kernel.py
python -m pytest -q mechanics/experience/parts/capture-kernel/tests/test_capture_kernel.py
```

#### `mechanics/experience/parts/certification-proof/VALIDATION.md`

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part certification-proof
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
python mechanics/experience/parts/certification-proof/scripts/validate_certification_proof.py
python -m pytest -q mechanics/experience/parts/certification-proof/tests/test_certification_proof.py
```

#### `mechanics/experience/parts/compatibility-bridges/VALIDATION.md`

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part compatibility-bridges
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
python mechanics/experience/parts/runtime-boundary/scripts/validate_runtime_boundary_bridge.py
python mechanics/experience/parts/compatibility-bridges/scripts/validate_agonic_pair_trials_bridge.py
python mechanics/experience/parts/compatibility-bridges/scripts/validate_epistemic_duel_bridge.py
python -m pytest -q mechanics/experience/parts/runtime-boundary/tests/test_runtime_boundary_bridge.py
python -m pytest -q mechanics/experience/parts/compatibility-bridges/tests/test_agonic_pair_trials_bridge.py
python -m pytest -q mechanics/experience/parts/compatibility-bridges/tests/test_epistemic_duel_bridge.py
```

#### `mechanics/experience/parts/continuity-context/VALIDATION.md`

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part continuity-context
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
python mechanics/experience/parts/continuity-context/scripts/validate_memory_rank_reputation.py
python mechanics/experience/parts/continuity-context/scripts/validate_affective_economy.py
python mechanics/experience/parts/continuity-context/scripts/validate_context_routing.py
python mechanics/experience/parts/continuity-context/scripts/validate_context_memory_weaving.py
python -m pytest -q mechanics/experience/parts/continuity-context/tests/test_memory_rank_reputation.py
python -m pytest -q mechanics/experience/parts/continuity-context/tests/test_affective_economy.py
python -m pytest -q mechanics/experience/parts/continuity-context/tests/test_context_routing.py
python -m pytest -q mechanics/experience/parts/continuity-context/tests/test_context_memory_weaving.py
```

#### `mechanics/experience/parts/governance-polis/VALIDATION.md`

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part governance-polis
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
python mechanics/experience/parts/governance-polis/scripts/validate_governance_polis.py
python -m pytest -q mechanics/experience/parts/governance-polis/tests/test_governance_polis.py mechanics/experience/parts/governance-polis/tests/test_governance_polis_seed_contracts.py
```

#### `mechanics/experience/parts/office-operations/VALIDATION.md`

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part office-operations
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
python mechanics/experience/parts/office-operations/scripts/validate_office_operations.py
python mechanics/experience/parts/office-operations/scripts/validate_office_role_pairs.py
python -m pytest -q mechanics/experience/parts/office-operations/tests/test_office_operations.py
python -m pytest -q mechanics/experience/parts/office-operations/tests/test_office_operations_seed_contracts.py
python -m pytest -q mechanics/experience/parts/office-operations/tests/test_office_role_pairs.py
```

#### `mechanics/experience/parts/release-deployment/VALIDATION.md`

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part release-deployment
python mechanics/experience/parts/release-deployment/scripts/validate_release_deployment.py
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
python mechanics/experience/parts/office-operations/scripts/validate_office_operations.py
python mechanics/experience/parts/runtime-boundary/scripts/validate_runtime_boundary_bridge.py
python -m pytest -q mechanics/experience/parts/release-deployment/tests/test_release_deployment.py
python -m pytest -q mechanics/experience/parts/office-operations/tests/test_office_operations.py
python -m pytest -q mechanics/experience/parts/office-operations/tests/test_office_operations_seed_contracts.py
python -m pytest -q mechanics/experience/parts/runtime-boundary/tests/test_runtime_boundary_bridge.py
```

#### `mechanics/experience/parts/runtime-boundary/VALIDATION.md`

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part runtime-boundary
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
python mechanics/experience/parts/runtime-boundary/scripts/validate_runtime_boundary_bridge.py
python mechanics/experience/parts/continuity-context/scripts/validate_living_workspace_continuity.py
python -m pytest -q mechanics/experience/parts/runtime-boundary/tests/test_runtime_boundary_bridge.py
python -m pytest -q mechanics/experience/parts/continuity-context/tests/test_living_workspace_continuity.py
```

#### `mechanics/experience/parts/service-mesh/VALIDATION.md`

```bash
python mechanics/experience/scripts/validate_experience_distillation.py --part service-mesh
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
python mechanics/experience/parts/service-mesh/scripts/validate_service_mesh.py
python -m pytest -q mechanics/experience/parts/service-mesh/tests/test_service_mesh.py
```

<!-- centralized-child-validation:end -->

## Closeout

Report the active part changed, whether `PROVENANCE.md` was consulted, owner requests affected, checks run, and any unresolved distillation risk.

If `PROVENANCE.md` was not consulted, say so explicitly. If it was consulted,
name only the relevant provenance bridge or archive map/log section. Do not
enumerate individual archived files unless the task specifically audited archive
evidence in depth.

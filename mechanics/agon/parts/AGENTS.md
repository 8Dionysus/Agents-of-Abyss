# AGENTS.md

## Applies to

This card applies to `mechanics/agon/parts/` and every descendant active part.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/agon/AGENTS.md`,
`mechanics/agon/DIRECTION.md`, and `mechanics/agon/PARTS.md` before changing an
active part.

## Boundaries

Active parts are concise working contracts. Do not turn them into source-doc
inventories, landing ledgers, proof verdicts, memory objects, runtime
activation, or ToS canon.

If a task needs detailed source accounting, route through
`mechanics/agon/PROVENANCE.md`.

## Validation

```bash
python mechanics/agon/scripts/validate_agon_distillation.py
python scripts/validate_mechanic_artifact_topology.py --mechanic agon
```

Run the nearest Agon builder, validator, and test when a part-specific model
artifact changes.

<!-- centralized-child-validation:start -->

### Centralized Child Validation

Executable validation commands from child docs live here. Child docs should
route to this section instead of carrying command blocks.

#### `mechanics/agon/parts/README.md`

```bash
python mechanics/agon/scripts/validate_agon_distillation.py
```

#### `mechanics/agon/parts/compatibility-bridges/VALIDATION.md`

```bash
python mechanics/agon/parts/compatibility-bridges/scripts/build_agon_ccs_law_registry.py --check
python mechanics/agon/parts/compatibility-bridges/scripts/validate_agon_ccs_laws.py
python mechanics/agon/parts/compatibility-bridges/scripts/build_agon_slc_registry.py --check
python mechanics/agon/parts/compatibility-bridges/scripts/validate_agon_slc_registry.py
python -m pytest -q mechanics/agon/parts/compatibility-bridges/tests/test_agon_ccs_laws.py mechanics/agon/parts/compatibility-bridges/tests/test_agon_slc_registry.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

#### `mechanics/agon/parts/duel-kernel/VALIDATION.md`

```bash
python mechanics/agon/parts/duel-kernel/scripts/build_agon_duel_kernel_model_registry.py --check
python mechanics/agon/parts/duel-kernel/scripts/validate_agon_duel_kernel_models.py
python mechanics/agon/parts/duel-kernel/scripts/build_agon_mechanical_trial_suite_registry.py --check
python mechanics/agon/parts/duel-kernel/scripts/validate_agon_mechanical_trial_suites.py
python -m pytest -q mechanics/agon/parts/duel-kernel/tests/test_agon_duel_kernel_models.py mechanics/agon/parts/duel-kernel/tests/test_agon_mechanical_trial_suites.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

#### `mechanics/agon/parts/epistemic-kag/VALIDATION.md`

```bash
python mechanics/agon/parts/epistemic-kag/scripts/build_agon_epistemic_agon_registry.py --check
python mechanics/agon/parts/epistemic-kag/scripts/validate_agon_epistemic_agon.py
python mechanics/agon/parts/epistemic-kag/scripts/build_agon_kag_promotion_path_registry.py --check
python mechanics/agon/parts/epistemic-kag/scripts/validate_agon_kag_promotion_path_registry.py
python -m pytest -q mechanics/agon/parts/epistemic-kag/tests/test_agon_epistemic_agon.py mechanics/agon/parts/epistemic-kag/tests/test_agon_kag_promotion_path_registry.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

#### `mechanics/agon/parts/gate-routing/VALIDATION.md`

```bash
python mechanics/agon/parts/gate-routing/scripts/build_agon_gate_routing_handoff_request.py --check
python mechanics/agon/parts/gate-routing/scripts/validate_agon_gate_routing_handoff_request.py
python -m pytest -q mechanics/agon/parts/gate-routing/tests/test_agon_gate_routing_handoff_request.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

#### `mechanics/agon/parts/imposition-readiness/VALIDATION.md`

```bash
python mechanics/agon/parts/imposition-readiness/scripts/build_agon_imposition_readiness.py --check
python mechanics/agon/parts/imposition-readiness/scripts/validate_agon_imposition_readiness.py
python -m pytest -q mechanics/agon/parts/imposition-readiness/tests/test_agon_imposition_readiness.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

#### `mechanics/agon/parts/lawful-move-grammar/VALIDATION.md`

```bash
python mechanics/agon/parts/lawful-move-grammar/scripts/build_agon_lawful_move_registry.py --check
python mechanics/agon/parts/lawful-move-grammar/scripts/validate_agon_lawful_moves.py
python -m pytest -q mechanics/agon/parts/lawful-move-grammar/tests/test_agon_lawful_moves.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

#### `mechanics/agon/parts/owner-binding/VALIDATION.md`

```bash
python mechanics/agon/parts/owner-binding/scripts/build_agon_move_owner_binding_registry.py --check --strict-lawful_move-check
python mechanics/agon/parts/owner-binding/scripts/validate_agon_move_owner_bindings.py
python -m pytest -q mechanics/agon/parts/owner-binding/tests/test_agon_move_owner_bindings.py
python scripts/validate_owner_request_docs.py --mechanic agon
python scripts/validate_owner_request_queue.py --mechanic agon
python mechanics/agon/scripts/validate_agon_distillation.py
```

#### `mechanics/agon/parts/packet-arena/VALIDATION.md`

```bash
python mechanics/agon/parts/packet-arena/scripts/build_agon_state_packet_registry.py --check
python mechanics/agon/parts/packet-arena/scripts/validate_agon_state_packets.py
python mechanics/agon/parts/packet-arena/scripts/build_agon_arena_session_model_registry.py --check
python mechanics/agon/parts/packet-arena/scripts/validate_agon_arena_session_models.py
python -m pytest -q mechanics/agon/parts/packet-arena/tests/test_agon_state_packets.py mechanics/agon/parts/packet-arena/tests/test_agon_arena_session_models.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

#### `mechanics/agon/parts/recurrence-adapter/VALIDATION.md`

```bash
python mechanics/agon/parts/recurrence-adapter/scripts/build_agon_recurrence_adapter_request.py --check
python mechanics/agon/parts/recurrence-adapter/scripts/validate_agon_recurrence_adapter_request.py
python -m pytest -q mechanics/agon/parts/recurrence-adapter/tests/test_agon_recurrence_adapter_request.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

#### `mechanics/agon/parts/sophian-threshold/VALIDATION.md`

```bash
python mechanics/agon/parts/sophian-threshold/scripts/build_agon_sophian_threshold_registry.py --check
python mechanics/agon/parts/sophian-threshold/scripts/validate_agon_sophian_threshold_registry.py
python -m pytest -q mechanics/agon/parts/sophian-threshold/tests/test_agon_sophian_threshold_registry.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

#### `mechanics/agon/parts/trial-handoff/VALIDATION.md`

```bash
python mechanics/agon/parts/trial-handoff/scripts/build_agon_trial_playbook_request.py --check
python mechanics/agon/parts/trial-handoff/scripts/validate_agon_trial_playbook_request.py
python -m pytest -q mechanics/agon/parts/trial-handoff/tests/test_agon_trial_playbook_request.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

#### `mechanics/agon/parts/verdict-retention-rank/VALIDATION.md`

```bash
python mechanics/agon/parts/verdict-retention-rank/scripts/build_agon_retention_rank_economy_registry.py --check
python mechanics/agon/parts/verdict-retention-rank/scripts/validate_agon_retention_rank_economy.py
python mechanics/agon/parts/verdict-retention-rank/scripts/build_agon_court_memo_stats_prebinding_request.py --check
python mechanics/agon/parts/verdict-retention-rank/scripts/validate_agon_court_memo_stats_prebinding_request.py
python mechanics/agon/parts/verdict-retention-rank/scripts/build_agon_vds_bridge_registry.py --check
python mechanics/agon/parts/verdict-retention-rank/scripts/validate_agon_vds_bridges.py
python -m pytest -q mechanics/agon/parts/verdict-retention-rank/tests/test_agon_retention_rank_economy.py
python -m pytest -q mechanics/agon/parts/verdict-retention-rank/tests/test_agon_court_memo_stats_prebinding_request.py
python -m pytest -q mechanics/agon/parts/verdict-retention-rank/tests/test_agon_vds_bridges.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

<!-- centralized-child-validation:end -->

## Closeout

Report active parts changed, whether `PROVENANCE.md` was consulted, owner
requests affected, checks run, checks skipped, remaining risk, and the next
owner route if this lane was only a waypoint.

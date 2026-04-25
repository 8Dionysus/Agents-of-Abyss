# AGENTS.md

This file applies to validation and builder tooling under `scripts/`.

## Role of this directory

`scripts/` is the lightweight validation seam for the AoA center.

Current scripts include:

- `validate_ecosystem.py` for schema, registry, and center-level `QUESTBOOK` surface checks
- `validate_nested_agents.py` for required local directory guidance under `docs/`, `generated/`, `schemas/`, and `scripts/`
- `validate_entry_surface_sync.py` for route-mode parity across public entry surfaces
- `release_check.py` for the release-gate bundle that runs docs thematic, link
  and shape hygiene, entry sync, center-entry, mechanics, generated freshness,
  ecosystem, and tests
- `plan_docs_thematic_cleanup.py`, `build_docs_thematic_index.py`, and
  `validate_docs_thematic_*.py` for Wave D docs district cleanup checks
- `hygiene_common.py`, `repair_known_link_drifts.py`, `validate_links.py`,
  `validate_status_vocabulary.py`, `build_link_shape_hygiene_index.py`,
  `validate_link_shape_hygiene_index.py`, `validate_generated_freshness.py`,
  and `validate_hygiene_suite.py` for Wave E link, Markdown shape, status
  vocabulary, generated freshness, and known-repair guardrails
- `build_mechanic_card_index.py`, `validate_mechanic_card_index.py`, and
  `validate_mechanic_readme_cards.py` for the mechanic card contract
- `build_owner_request_queue.py`, `validate_owner_request_queue.py`,
  `validate_generated_owner_request_queue.py`, and
  `validate_owner_request_docs.py` for center-side owner request packets
- `validate_candidate_lineage_contract.py` for the narrow cross-repo Growth Refinery example-chain witness
- `validate_wave4_kernel_automation.py` for the reviewed wave 4 next-kernel and automation follow-through seam across sibling repos
- `agon_imposition_common.py` for the canonical Agon Wave 0 capsule payload,
  local-reference checks, and shared build/validate entrypoints
- `build_agon_imposition_readiness.py` for deterministic rebuild or stale-check
  of `generated/agon_imposition_readiness.min.json`
- `validate_agon_imposition_readiness.py` for the explicit Wave 0 readiness
  contract check
- `build_agon_lawful_move_registry.py` for deterministic rebuild or stale-check
  of `generated/agon_lawful_move_registry.min.json`
- `validate_agon_lawful_moves.py` for the explicit Wave III lawful move
  vocabulary contract check
- `build_agon_move_owner_binding_registry.py` for deterministic rebuild or
  stale-check of `generated/agon_move_owner_binding_registry.min.json`
- `validate_agon_move_owner_bindings.py` for the explicit Wave IV move owner
  binding contract check
- `build_agon_gate_routing_handoff_request.py` for deterministic rebuild or
  stale-check of `generated/agon_gate_routing_handoff_request.min.json`
- `validate_agon_gate_routing_handoff_request.py` for the explicit Wave V
  gate-routing handoff contract check
- `validate_experience_wave1.py` for the first center-owned experience-capture
  kernel contract check
- `validate_experience_wave2.py` for the second center-owned experience
  certification/watchtower contract check
- `validate_experience_wave3.py` for the third center-owned experience
  federation/adoption contract check
- `validate_experience_wave4.py` for the fourth center-owned experience
  polis governance and constitution runtime contract check
- `validate_experience_v1_2_service_mesh_operations.py` for the v1.2 service
  mesh operations center contract check
- `validate_experience_v1_3_office_foundry_role_pairs.py` for the v1.3 office
  foundry role-pairs center contract check
- `validate_experience_v1_4_agonic_pair_trials_mechanical_arena_kernel.py` for
  the v1.4 agonic pair trial and mechanical arena kernel center contract check
- `validate_experience_v1_5_epistemic_duel_model_of_other_forge.py` for the
  v1.5 epistemic duel and model-of-other forge center contract check

## Editing posture

Keep this script surface small, repo-relative, deterministic, and limited to the documented dependencies in `requirements-dev.txt`.

When changing script logic:

- prefer crisp failure messages over hidden magic
- keep checks anchored to public repository surfaces
- avoid network access, speculative repo discovery, or layer-owned validation that belongs elsewhere
- keep cross-repo checks witness-shaped: they may validate that owner examples line up, but they must not turn this center repo into a candidate ledger
- update the local `AGENTS.md` guidance when validator expectations change
- preserve Python 3.12 compatibility for the GitHub Actions path

If a validation rule becomes complicated enough to need a broader contract, encode that contract in docs or schema first.

## Validation

After changing validator logic, run:

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
python scripts/validate_generated_freshness.py
python scripts/validate_hygiene_suite.py
python scripts/validate_entry_surface_sync.py
python scripts/validate_ecosystem.py
python scripts/release_check.py
```

After changing the Agon Wave 0 builder or validator, also run:

```bash
python scripts/build_agon_imposition_readiness.py --check
python scripts/validate_agon_imposition_readiness.py
python -m pytest -q tests/test_agon_imposition_readiness.py
```

After changing the Agon Wave III builder or validator, also run:

```bash
python scripts/build_agon_lawful_move_registry.py --check
python scripts/validate_agon_lawful_moves.py
python -m pytest -q tests/test_agon_lawful_moves.py
```

After changing the Agon Wave IV builder or validator, also run:

```bash
python scripts/build_agon_move_owner_binding_registry.py --check
python scripts/validate_agon_move_owner_bindings.py
python -m pytest -q tests/test_agon_move_owner_bindings.py
```

After changing the Agon Wave V builder or validator, also run:

```bash
python scripts/build_agon_gate_routing_handoff_request.py --check
python scripts/validate_agon_gate_routing_handoff_request.py
python -m pytest -q tests/test_agon_gate_routing_handoff_request.py
```

After changing the Experience Wave 1 validator, also run:

```bash
python scripts/validate_experience_wave1.py
python -m pytest -q tests/test_experience_wave1.py
```

After changing the Experience Wave 2 validator, also run:

```bash
python scripts/validate_experience_wave2.py
python -m pytest -q tests/test_experience_wave2.py
```

After changing the Experience Wave 3 validator, also run:

```bash
python scripts/validate_experience_wave3.py
python -m pytest -q tests/test_experience_wave3.py
```

After changing the Experience Wave 4 validator, also run:

```bash
python scripts/validate_experience_wave4.py
python -m pytest -q tests/test_experience_wave4.py tests/test_experience_wave4_seed_contracts.py
```

After changing the Experience v1.2 or v1.3 campaign validators, also run:

```bash
python scripts/validate_experience_v1_2_service_mesh_operations.py
python -m pytest -q tests/test_experience_v1_2_service_mesh_operations.py
python scripts/validate_experience_v1_3_office_foundry_role_pairs.py
python -m pytest -q tests/test_experience_v1_3_office_foundry_role_pairs.py
```

After changing the Experience v1.4 campaign validator, also run:

```bash
python scripts/validate_experience_v1_4_agonic_pair_trials_mechanical_arena_kernel.py
python -m pytest -q tests/test_experience_v1_4_agonic_pair_trials_mechanical_arena_kernel.py
```

After changing the Experience v1.5 campaign validator, also run:

```bash
python scripts/validate_experience_v1_5_epistemic_duel_model_of_other_forge.py
python -m pytest -q tests/test_experience_v1_5_epistemic_duel_model_of_other_forge.py
```

A script change is done when the failure mode is clearer, not more mysterious.

# Scripts District

This directory holds builders, validators, release checks, and local guardrails for the AoA center.

Scripts may build or validate compact surfaces. They do not create constitutional authority by themselves.

Mechanic-owned builders, validators, and helper modules live in
`mechanics/<slug>/scripts/`. Root `scripts/` contains root-owned release,
topology, hygiene, and shared validators.

## Main families

| Family | Examples | Role |
|---|---|---|
| Center builders | `build_center_entry_map.py` | build compact center-entry surfaces |
| Center validators | `validate_center_entry_map.py`, `validate_ecosystem.py` | check center and registry contracts |
| Mechanic scripts | `mechanics/<slug>/scripts/*.py` | mechanic-owned validators and builders called directly |
| Mechanics validators | `build_mechanic_card_index.py`, `validate_mechanic_card_index.py`, `validate_mechanic_readme_cards.py`, `validate_mechanic_artifact_topology.py`, `validate_questbook_lifecycle.py`, `build_questbook_index.py`, `validate_questbook_index.py` | check mechanic cards, artifact homes, quest lifecycle board, Questbook generated views, and generated card index |
| Owner-request validators | `build_owner_request_queue.py`, `validate_owner_request_queue.py`, `validate_generated_owner_request_queue.py`, `validate_owner_request_docs.py` | check center-side owner request packets |
| Docs thematic validators | `plan_docs_thematic_cleanup.py`, `build_docs_thematic_index.py`, `validate_docs_thematic_*.py` | check docs district cleanup grammar |
| Link and shape hygiene | `repair_known_link_drifts.py`, `validate_links.py`, `validate_status_vocabulary.py`, `build_link_shape_hygiene_index.py`, `validate_generated_freshness.py`, `validate_hygiene_suite.py` | check local links, status words, generated freshness, and Wave E hygiene mirrors |
| AGENTS mesh | `validate_agents_md_shape.py`, `validate_agents_mesh.py`, `build_agents_mesh_index.py`, `validate_agents_mesh_index.py` | check local AGENTS-card shape, coverage, and generated Wave F mesh |
| Release checks | `release_check.py` | guard public release posture |
| Documentation guardrails | `validate_markdown_shape.py` | protect human and agent readability of civic docs |

## Rules

- Prefer dry-run, check-only, or explicit output paths when possible.
- A builder should have a corresponding source document, schema, generated surface, validator, or test.
- A validator should state what it checks and what it does not check.
- Do not hide mutation behind a convenience script.
- Do not make a script the only place where a constitutional boundary is explained.

## Baseline checks

```bash
python scripts/plan_docs_thematic_cleanup.py --check
python scripts/validate_docs_thematic_districts.py
python scripts/validate_docs_migration_map.py
python scripts/build_docs_thematic_index.py --check
python scripts/validate_docs_thematic_index.py
python scripts/repair_known_link_drifts.py --check
python scripts/validate_links.py
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python mechanics/experience/scripts/validate_experience_distillation.py
python scripts/validate_mechanic_artifact_topology.py
python mechanics/questbook/scripts/validate_questbook_lifecycle.py
python mechanics/questbook/scripts/build_questbook_index.py --check
python mechanics/questbook/scripts/validate_questbook_index.py
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_ecosystem.py
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
python -m pytest -q
```

Run narrower or wider checks based on the touched surfaces.

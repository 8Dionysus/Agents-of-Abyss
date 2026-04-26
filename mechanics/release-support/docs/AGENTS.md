# AGENTS.md

## Applies to

This card applies to `mechanics/release-support/docs/` and all descendant source documents.

## Role

`mechanics/release-support/docs/` holds detailed center-source doctrine, models, waves, stop-lines,
handoffs, packets, or support notes for the `Release support` mechanic. The package `README.md`
remains the entry card; this docs directory holds the deeper material.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/release-support/AGENTS.md`,
`mechanics/release-support/README.md`, and the specific source document you are changing. If a
generated surface mirrors this document, read the builder and validator before editing.

## Boundaries

- Keep detailed doctrine package-local and linked from the package README when it becomes an entry path.
- Do not create owner-local activation claims, runtime claims, proof verdicts, memory objects, role contracts, playbook choreography, KAG canon, or ToS-authored meaning here.
- If this document becomes historical, route it through landing, trace, or legacy posture instead of deleting provenance.
- If this document creates a request to a stronger owner, update the owner-request queue rather than pretending the owner accepted it.

## Validation

Run package and link checks:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/validate_links.py
python scripts/validate_mechanic_readme_cards.py
python scripts/validate_mechanics_topology.py
python scripts/validate_mechanic_landing_logs.py --mechanic release-support
python -m pytest -q
```

Run any targeted builder, validator, and test named by the generated or version-specific surface you touched.

<!-- centralized-child-validation:start -->

### Centralized Child Validation

Executable validation commands from child docs live here. Child docs should
route to this section instead of carrying command blocks.

#### `mechanics/release-support/docs/RELEASE_SUPPORT_OWNER_REPO_REQUESTS.md`

```bash
python scripts/validate_owner_request_queue.py --mechanic release-support
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic release-support
python scripts/validate_mechanics_topology.py --mechanic release-support
```

#### `mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md`

```bash
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
python scripts/validate_entry_surface_sync.py
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_mechanics_topology.py
python scripts/validate_mechanic_landing_logs.py
python scripts/validate_generated_freshness.py
python scripts/validate_hygiene_suite.py
python scripts/validate_ecosystem.py
python -m pytest -q
```

#### `mechanics/release-support/docs/RELEASING.md`

```bash
python scripts/release_check.py
```

<!-- centralized-child-validation:end -->

## Closeout

Report source docs changed, package README or registry updates needed, generated mirrors rebuilt or not rebuilt, owner-request status affected, and checks run or skipped.

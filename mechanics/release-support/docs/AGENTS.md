# AGENTS.md

## Applies to

This card applies to `mechanics/release-support/docs/` and all descendant source documents.

## Role

`mechanics/release-support/docs/` holds detailed center-source doctrine,
models, stop-lines, handoffs, packets, or support notes for the `Release
support` mechanic. The package `README.md` remains the entry card; `DIRECTION.md`
and active `parts/` hold the default operating route.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/release-support/AGENTS.md`,
`mechanics/release-support/README.md`, and the specific source document you are changing. If a
generated surface mirrors this document, read the builder and validator before editing.

## Boundaries

- Keep detailed doctrine package-local and linked from the package README when it becomes an entry path.
- Do not create owner-local activation claims, runtime claims, proof verdicts, memory objects, role contracts, playbook choreography, KAG canon, or ToS-authored meaning here.
- If this document becomes historical, route it through landing, trace, or legacy posture instead of deleting provenance.
- If this document creates a request to a stronger owner, update the owner-request queue rather than pretending the owner accepted it.
- Do not make docs the default operating surface when a concise active part can carry the route.

## Validation

Run package and link checks:

```bash
python scripts/agents_mesh/validate_agents_md_shape.py
python scripts/agents_mesh/validate_agents_mesh.py
python scripts/hygiene/validate_links.py
python mechanics/release-support/scripts/validate_release_support_distillation.py
python scripts/mechanics_topology/validate_mechanic_readme_cards.py
python scripts/mechanics_topology/validate_mechanics_topology.py
python scripts/mechanics_topology/validate_mechanic_landing_logs.py --mechanic release-support
python -m pytest -q
```

Run any targeted builder, validator, and test named by the generated or version-specific surface you touched.

### Routed child validation

Child-specific commands are source-owned by `mechanics/validation-routes.json`.
Run `python scripts/mechanics_topology/run_validation_route.py --surface <repo-relative-path>`;
add `--show` to inspect the route without executing it.


## Closeout

Report source docs changed, package README or registry updates needed, generated mirrors rebuilt or not rebuilt, owner-request status affected, and checks run or skipped.

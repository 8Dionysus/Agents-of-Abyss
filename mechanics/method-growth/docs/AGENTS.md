# AGENTS.md

## Applies to

This card applies to `mechanics/method-growth/docs/` and all descendant source
documents.

## Role

`mechanics/method-growth/docs/` holds detailed center-source doctrine, models,
stop-lines, handoffs, packets, and support notes for the `Method-growth`
mechanic. The package root owns active route surfaces; this docs directory
holds the deeper material.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`,
`mechanics/method-growth/AGENTS.md`, `mechanics/method-growth/README.md`, and
the specific source document you are changing. If a generated surface mirrors
this document, read the builder and validator before editing.

## Boundaries

- Keep detailed doctrine package-local and linked from the package README when
  it becomes an entry path.
- Do not create owner-local activation claims, runtime claims, proof verdicts,
  memory objects, role contracts, playbook choreography, KAG canon, or
  ToS-authored meaning here.
- If this document becomes historical, route it through landing, trace, or
  provenance posture instead of deleting its audit trail.
- If this document creates a request to a stronger owner, update
  `mechanics/method-growth/OWNER_REQUESTS.md` and the owner-request queue
  rather than pretending the owner accepted it.

## Validation

Run package and link checks:

```bash
python mechanics/method-growth/scripts/validate_method_growth_mechanic.py
python scripts/agents_mesh/validate_agents_md_shape.py
python scripts/agents_mesh/validate_agents_mesh.py
python scripts/hygiene/validate_links.py
python scripts/mechanics_topology/validate_mechanic_readme_cards.py --mechanic method-growth
python scripts/mechanics_topology/validate_mechanics_topology.py --mechanic method-growth
python scripts/mechanics_topology/validate_mechanic_landing_logs.py --mechanic method-growth
python -m pytest -q mechanics/method-growth/tests
```

Run any targeted builder, validator, and test named by the generated or
version-specific surface you touched.

### Routed child validation

Child-specific commands are source-owned by `mechanics/validation-routes.json`.
Run `python scripts/mechanics_topology/run_validation_route.py --surface <repo-relative-path>`;
add `--show` to inspect the route without executing it.


## Closeout

Report source docs changed, package README or registry updates needed,
generated mirrors rebuilt or not rebuilt, owner-request status affected, and
checks run or skipped.

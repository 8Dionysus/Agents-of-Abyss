# AGENTS.md

## Applies to

This card applies to `mechanics/agon/docs/` and all descendant source documents.

## Role

`mechanics/agon/docs/` holds detailed center-source doctrine, models, waves, stop-lines, handoffs,
packets, or support notes for the `Agon` mechanic. The package `README.md` remains the entry card;
this docs directory holds the deeper material.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/agon/AGENTS.md`,
`mechanics/agon/README.md`, and the specific source document you are changing. If a generated
surface mirrors this document, read the builder and validator before editing.

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
python scripts/validate_mechanic_landing_logs.py --mechanic agon
python -m pytest -q tests
```

Run any targeted builder, validator, and test named by the generated or version-specific surface you touched.

## Closeout

Report source docs changed, package README or registry updates needed, generated mirrors rebuilt or not rebuilt, owner-request status affected, and checks run or skipped.

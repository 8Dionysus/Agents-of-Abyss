# AGENTS.md

## Applies to

This card applies to `manifests/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`manifests/` holds the repo-level registry for machine-readable manifest homes.
It routes agents to canonical manifest records without storing mechanic-owned
records in the root district.

## Read before editing

Read root `AGENTS.md`, local `README.md`, `manifests/registry.json`, and the
owning manifest home named by the registry.

Use owner docs, mechanic packages, schemas, builders, validators, and owner
repositories as stronger authority than a manifest receipt.

## Boundaries

- Root `manifests/` owns registry and route shape.
- Manifest homes own their local records and local validation.
- Mechanic-owned component or hook records belong in the owning manifest home.
- Do not place mechanic component or hook records in root `manifests/`.
- Manifest registry entries are route metadata, not hidden state, runtime
  authority, or owner acceptance.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

```bash
python scripts/validate_manifests_registry.py
python -m pytest -q tests/test_manifests_district.py
python scripts/validate_links.py
python scripts/validate_generated_freshness.py
python -m pytest -q
```

If a listed validator is missing, report it and run the closest available
guardrail.

## Closeout

Report registry entries changed, manifest homes touched, source surfaces
consulted, generated files rebuilt or intentionally left untouched, checks run,
checks skipped, and the next owner route when the manifest is only a waypoint.

# AGENTS.md

## Applies to

This card applies to `manifests/` and all descendants unless a nearer
`AGENTS.md` narrows the path.

## Role

`manifests/` holds the repo-level registry for machine-readable manifest homes.
It routes agents to canonical manifest records without storing mechanic-owned
records in the root district.

The authoritative registry is `manifests/registry.json`.

## Read before editing

Read the manifest registry and owner route only when placement or validation mapping changes.
## Boundaries

- Root `manifests/` owns registry and route shape.
- Manifest homes own their local records and local validation.
- Mechanic-owned component or hook records belong in the owning manifest home.
- Do not place mechanic component or hook records in root `manifests/`.
- Manifest registry entries are route metadata, not hidden state, runtime
  authority, or owner acceptance.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

If a listed validator is missing, report it and run the closest available
guardrail.

## Closeout

Report registry entries changed, manifest homes touched, source surfaces
consulted, generated files rebuilt or intentionally left untouched, checks run,
checks skipped, and the next owner route when the manifest is only a waypoint.

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

Select only the source, contract, or owner route that can change the interpretation of the named task.
A nearby human README is on-demand: use it when its explanation, package map, provenance, compatibility, or usage contract is material to the task.
Exact executable checks belong to the applicable `VALIDATION.md`, validated manifest, runner, or stronger owner procedure surface.
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

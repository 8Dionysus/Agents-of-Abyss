# AGENTS.md

## Applies to

This card applies to `scripts/` and every nested path under that scope until a
nearer `AGENTS.md` narrows the lane.

## Role

`scripts/` is the root validation and build seam for the AoA center. It keeps
root-owned validators, builders, release checks, and shared helper modules
visible as family-scoped directories without absorbing mechanic-owned tooling.
The authoritative family map is `scripts/registry.json`.

## Read before editing

Select only the source, contract, or owner route that can change the interpretation of the named task.
A nearby human README is on-demand: use it when its explanation, package map, provenance, compatibility, or usage contract is material to the task.
Exact executable checks belong to the applicable `VALIDATION.md`, validated manifest, runner, or stronger owner procedure surface.
## Boundaries

- Root `scripts/` owns repo-relative center tooling through registered family
  directories.
- Root-level `scripts/*.py` files are not command homes; use
  `scripts/<family>/*.py` for root-owned Python tooling.
- Mechanic-owned scripts belong with the owning mechanic or part.
- Keep scripts deterministic and limited to dependencies in
  `requirements-dev.txt`.
- Preserve Python 3.12 compatibility for the GitHub Actions path.
- Use `validate_nested_agents.py` and `validate_ecosystem.py` as root
  guardrails for local AGENTS coverage and ecosystem registry shape.
- Keep cross-repo checks witness-shaped; do not turn this center repo into an
  owner-local ledger for sibling repos.
- Do not widen a validator just to make weak or inconsistent data pass.
- Do not make a script the only place where a constitutional boundary is
  explained.

## Validation

Run the narrowest relevant checks first. Usual checks for this district:

For release-facing script changes, also run:

## Closeout

Report script registry entries changed, root scripts touched, source surfaces
consulted, generated files rebuilt or intentionally left untouched, checks run,
checks skipped, and the owner route when a script belongs outside root.

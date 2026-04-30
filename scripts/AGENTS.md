# AGENTS.md

## Applies to

This card applies to `scripts/` and every nested path under that scope until a
nearer `AGENTS.md` narrows the lane.

## Role

`scripts/` is the root validation and build seam for the AoA center. It keeps
root-owned validators, builders, release checks, and shared helper modules
visible without absorbing mechanic-owned tooling.

## Read before editing

Read root `AGENTS.md`, local `README.md`, `scripts/registry.json`, and the
source surface named by the relevant registry family.

Use mechanic package guidance for scripts under `mechanics/<slug>/scripts/` or
`mechanics/<slug>/parts/<part>/scripts/`.

## Boundaries

- Root `scripts/` owns repo-relative center tooling.
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

```bash
python scripts/validate_scripts_district.py
python -m pytest -q tests/test_scripts_district.py
python scripts/validate_nested_agents.py
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
python scripts/validate_generated_freshness.py
python scripts/validate_ecosystem.py
```

For release-facing script changes, also run:

```bash
python scripts/release_check.py
```

## Closeout

Report script registry entries changed, root scripts touched, source surfaces
consulted, generated files rebuilt or intentionally left untouched, checks run,
checks skipped, and the owner route when a script belongs outside root.

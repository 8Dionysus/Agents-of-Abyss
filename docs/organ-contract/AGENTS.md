# AGENTS.md

## Applies to

This card applies to `docs/organ-contract/` and every descendant.

## Role

`docs/organ-contract/` owns the AoA center's AbyssOS organ contract. It names
how a repository presents itself as a reviewable organ without turning AoA into
the SDK, router, runtime, role layer, proof layer, or owner-local executor.

## Read before editing

Read root `AGENTS.md`, `docs/AGENTS.md`, this card, and then:

1. `README.md`
2. `ORGAN_CONTRACT.md`
3. `SURFACE_STATES.md`
4. `FIRST_CYCLE.md`
5. `EVENTS.md`
6. `CHARTER.md`
7. `ECOSYSTEM_MAP.md`
8. `docs/START_HERE_ROUTE_CONTRACT.md`
9. `docs/REPO_ROLES.md`

## Boundaries

- This district owns organ alignment law for the center.
- `aoa-sdk` owns typed helpers, compatibility, activation, and control-plane
  implementation.
- `aoa-routing` owns operational dispatch and navigation surfaces.
- `aoa-agents`, `aoa-playbooks`, `aoa-evals`, `aoa-memo`, `aoa-kag`, and
  `aoa-stats` own their layer-local object classes.
- `abyss-stack` owns runtime body, services, storage, workers, and deployed
  state.
- `Tree-of-Sophia` owns ToS-authored meaning.

## Editing posture

Keep this district compact and constitutional. Prefer reusable route grammar,
surface-state vocabulary, and owner-boundary checks over repository-specific
implementation detail.

When a change would require executable discovery, activation, typed adapters,
or dashboards, leave an owner route for `aoa-sdk` instead of growing this
district.

## Validation

Run:

```bash
python scripts/validate_organ_contract.py
python scripts/validate_entry_surface_sync.py
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_docs_thematic_districts.py
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
python -m pytest -q tests/test_organ_contract.py tests/test_center_entry_map.py tests/test_entry_surface_sync.py
```

For release-facing changes, also run:

```bash
python scripts/release_check.py
```

## Closeout

Report changed organ-contract surfaces, route modes affected, owner routes
preserved, generated surfaces rebuilt or intentionally left untouched, checks
run, checks skipped, remaining risk, and whether a decision record was needed.

# Entry Validation Baseline Surface

Status: accepted

Date: 2026-04-30

## Context

Center entry surfaces must stay synchronized on route modes and validation
expectations. Previously `validate_entry_surface_sync.py` required every human
entry surface, or its local validation authority, to contain every baseline
validation command literally.

That kept the machine contract strict, but it forced root `AGENTS.md` and other
entry surfaces to carry long command blocks even when the better human route was
to name the broad gate and point to a canonical validation surface.

## Options considered

- Keep literal command-list repetition in every entry surface.
- Let `scripts/release_check.py` be the only visible validation route.
- Add a dedicated entry validation baseline surface and let entry surfaces point
  to it.

## Decision

Add `docs/guardrails/ENTRY_SURFACE_VALIDATION_BASELINE.md` as the human-readable
baseline command surface for entry synchronization.

Keep `scripts/center_entry_map_common.py` as the machine source for the command
tuple. `scripts/validate_entry_surface_sync.py` now verifies that the baseline
surface contains the full command set and that entry surfaces either contain the
commands directly or point to the baseline surface.

## Rationale

This keeps the machine contract strict while allowing root entry documents to
stay readable. It also gives future route-law changes a named surface to update
instead of forcing command-list repetition across multiple docs.

## Consequences

- Root `AGENTS.md` can point to the baseline instead of repeating the full list.
- The baseline remains checked by tests and `validate_entry_surface_sync.py`.
- Changes to baseline validation now need source, docs, validator, generated
  capsule, and tests to move together.

## Source surfaces

- `docs/guardrails/ENTRY_SURFACE_VALIDATION_BASELINE.md`
- `scripts/center_entry_map_common.py`
- `scripts/validate_entry_surface_sync.py`
- `docs/START_HERE_ROUTE_CONTRACT.md`
- `AGENTS.md`
- `generated/center_entry_map.min.json`

## Follow-up route

If the baseline grows into a richer machine contract, promote it through the
guardrails district with schema or config support rather than reintroducing
command-list duplication into entry surfaces.

# Entry Surface Validation Baseline

This guardrail surface names the canonical validation route that center entry
surfaces may reference instead of repeating commands inline.

## Role

The machine source for the baseline is
`scripts/center_entry/center_entry_map_common.py`.
`scripts/center_entry/validate_entry_surface_sync.py` verifies that entry
surfaces point here or to their local validation authority.

`scripts/release_gate/release_check.py` owns broad executable orchestration for
release-facing or repo-wide changes. The root and nearest local `AGENTS.md`
cards own human command entrypoints.

## Baseline route

Use root `AGENTS.md#verify` for the broad human entrypoint. Use the nearest
local `AGENTS.md#validation` for a narrower district or mechanic lane. The
release gate remains the single executable orchestration source for the broad
battery; individual builders and validators remain the executable owners of
their own behavior.

## Boundary

This baseline does not replace local validators. It gives entry surfaces a
compact route to executable owners while local `AGENTS.md` cards continue to
own lane-specific commands.

# Ecosystem Registry v2 Landing

Status: accepted
Date: 2026-04-29

## Context

`docs/registry/REGISTRY_V2_NOTES.md` described a future split of the compact
ecosystem registry into clearer axes, but keeping it as a standing design note
left a route tail after the needed migration became actionable.

The center needed the registry contract itself to carry the clearer shape
instead of preserving a separate docs district for unexecuted registry plans.

## Options considered

1. Keep `docs/registry/` as a registry-evolution district and leave v2 as a
   planned migration.
2. Land registry v2 now by updating the schema, generated registry, validator,
   tests, and public contour docs, then remove the temporary registry-note
   district.

## Decision

Land ecosystem registry v2 as the current machine contract and remove
`docs/registry/` as an active docs district.

Registry evolution now moves through the aligned schema, generated capsule,
validator, source docs, and decision-record route when the change affects public
interpretation.

## Rationale

The v2 axes are concrete enough to validate now. Keeping the old design-note
district would preserve a stale planning surface that agents could mistake for
current law or revive as a holding area for future tails.

Moving the contract into `schemas/ecosystem-registry.schema.json`,
`generated/ecosystem_registry.min.json`, and `scripts/validate_ecosystem.py`
keeps the source-of-truth path executable and reviewable.

## Consequences

- Registry entries now expose `visibility`, `maturity`, `relation`, and `kind`
  separately.
- `aoa-sdk` remains in the supporting inventory rather than entering the
  ecosystem registry.
- Future registry changes need contract updates, not a parked registry-note
  folder.
- The remaining risk is that historical references in raw audit receipts still
  mention the former note route; those stay historical and must not be read as
  current law.

## Source surfaces

- `schemas/ecosystem-registry.schema.json`
- `generated/ecosystem_registry.min.json`
- `scripts/validate_ecosystem.py`
- `ECOSYSTEM_MAP.md`
- `docs/REPO_ROLES.md`
- `docs/ROOT_SURFACE_LAW.md`
- `docs/guardrails/thematic_districts.json`

## Follow-up route

Use `scripts/validate_ecosystem.py` for registry contract checks. If a future
registry change alters public interpretation, add or amend a decision record
under `docs/decisions/` while updating schema, generated capsule, validator,
and source docs in the same landing.

# Manifests District

`manifests/` is the repo-level control surface for machine-readable manifest
homes. It tells agents where manifest records live, who owns them, and which
validator protects each home.

Manifest records themselves live with their owning mechanic or root district.
The root district keeps the registry and the routing contract.

## Current Surface

| Surface | Role |
|---|---|
| [`registry.json`](registry.json) | canonical registry of manifest homes, owners, classes, globs, and validators |

## Source Order

When a manifest and another surface disagree, read authority in this order:

1. owner repository or source mechanic package
2. schema, validator, builder, or source config that produced the record
3. manifest receipt
4. generated or derived consumer surface

## Registered Homes

| Home | Owner | Validator |
|---|---|---|
| [`mechanics/agon/parts/recurrence-adapter/manifests/`](../mechanics/agon/parts/recurrence-adapter/manifests/) | Agon recurrence adapter | `mechanics/agon/parts/recurrence-adapter/scripts/validate_agon_recurrence_manifests.py` |

## Editing Route

- Add manifest records to the owning mechanic, part, or root district.
- Add or update `registry.json` when a new manifest home becomes canonical.
- Keep runtime effect, owner boundary, source refs, and validator refs explicit.
- Keep generated mirrors in `generated/` with a builder and validator route.

## Before Editing

1. Read the owning manifest home README and AGENTS card.
2. Read [`docs/ROOT_SURFACE_LAW.md`](../docs/ROOT_SURFACE_LAW.md) before adding
   a new root-published manifest class.
3. Update `registry.json` and run the registry validator.

## Validation

```bash
python scripts/validate_manifests_registry.py
python -m pytest -q tests/test_manifests_district.py
python scripts/validate_links.py
```

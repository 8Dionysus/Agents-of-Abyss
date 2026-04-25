# Experience Distillation Log

This log records decisions that move Experience from long raw packets into light active parts.

## 2026-04-25 - Active docs provenance-load cleanup

Status: landed.

Owner boundary: `Agents-of-Abyss` keeps active Experience parts concise while
legacy preserves the detailed source inventory, raw packet map, and distillation
accounting.

Moved or clarified:

- Active part `README.md` files no longer carry per-source legacy lists.
- Active part `VALIDATION.md` files no longer carry archive accounting sections.
- `mechanics/experience/PROVENANCE.md` is the single active bridge back to this
  legacy district.
- `mechanics/experience/legacy/INDEX.md` remains the detailed map from every
  preserved raw source to the active part that absorbed it.

Validation:

- `python mechanics/experience/scripts/validate_experience_distillation.py`
- `python scripts/validate_mechanic_landing_logs.py --mechanic experience`

Stop-lines: do not delete raw provenance, do not duplicate archive inventories
inside active part docs, and do not let legacy become the normal first route for
routine mechanic edits.

Next route: future packet landings update the active part and this legacy map;
active parts stay short.

## 2026-04-25 - Part-local artifact homes

Status: landed.

Owner boundary: `Agents-of-Abyss` keeps Experience schemas, examples,
validators, and tests close to their functioning parts while preserving old flat
paths as receipts.

Moved or clarified:

- Flat `mechanics/experience/schemas/` files moved into
  `mechanics/experience/parts/<part>/schemas/`.
- Flat `mechanics/experience/examples/` files moved into
  `mechanics/experience/parts/<part>/examples/`.
- Part-specific validators moved into
  `mechanics/experience/parts/<part>/scripts/` with clearer names.
- Part-specific tests moved into `mechanics/experience/parts/<part>/tests/`.
- `mechanics/experience/artifact-map.json` records every old path and active
  destination.
- `mechanics/experience/legacy/artifacts/README.md` explains the receipt route.

Validation:

- `python mechanics/experience/scripts/validate_experience_distillation.py`
- `python scripts/validate_mechanic_artifact_topology.py --mechanic experience`
- `python -m pytest -q mechanics/experience/tests mechanics/experience/parts`

Stop-lines: do not recreate flat aliases, do not let old wave names dictate
active part names, and do not treat examples or generated receipts as owner
truth.

Next route: future Experience artifacts land directly in the active part that
uses them, then update the artifact map and landing ledger.

## 2026-04-25 - Active parts plus legacy raw provenance

Status: landed.

Owner boundary: `Agents-of-Abyss` keeps center Experience direction, part contracts, landing ledger, and owner requests. Raw wave and version provenance remains preserved in `legacy/raw/`; operational runtime, memory, proof, routing, KAG, ToS meaning, and live offices remain with stronger owners.

Surfaces:

- `mechanics/experience/DIRECTION.md`
- `mechanics/experience/PARTS.md`
- `mechanics/experience/parts/README.md`
- `mechanics/experience/legacy/README.md`
- `mechanics/experience/legacy/INDEX.md`
- `mechanics/experience/legacy/raw/`
- `mechanics/experience/scripts/validate_experience_distillation.py`

Validation:

- `python mechanics/experience/scripts/validate_experience_distillation.py`
- `python scripts/validate_mechanic_landing_logs.py --mechanic experience`

Stop-lines: do not turn `legacy/raw/` into the active route, do not delete provenance, and do not claim owner-local activation from center distillation.

Next route: future Experience packets land through raw provenance plus active part updates, then owner requests when a stronger owner must accept or prove a slice.

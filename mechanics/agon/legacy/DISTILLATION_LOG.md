# Agon Distillation Log

This log records decisions that move Agon from long raw packets into light
active parts.

## 2026-04-26 - Active parts plus legacy raw provenance

Status: landed.

Owner boundary: `Agents-of-Abyss` keeps center Agon direction, part contracts,
landing ledger, owner requests, and provenance bridge. Raw wave and model
provenance remains preserved in `legacy/raw/`; live arena execution, actor
authority, runtime behavior, proof verdicts, memory objects, KAG source truth,
and ToS canon remain with stronger owners.

Moved or clarified:

- Raw `AGON_*` and `PRE_AGON_BASELINE` documents moved from `docs/` into
  `legacy/raw/`.
- `docs/` is now only a compatibility route to active Agon surfaces.
- `legacy/INDEX.md` maps every preserved raw source to the active part that
  absorbed or is pressured by it.
- `mechanics/agon/PROVENANCE.md` is the single active bridge back to this
  legacy district.

Validation:

- `python mechanics/agon/scripts/validate_agon_distillation.py`
- `python scripts/validate_mechanic_landing_logs.py --mechanic agon`

Stop-lines: do not turn `legacy/raw/` into the active route, do not delete
provenance, and do not claim owner-local activation from center distillation.

Next route: future Agon packets land through raw provenance plus active part
updates, then owner requests when a stronger owner must accept or prove a slice.

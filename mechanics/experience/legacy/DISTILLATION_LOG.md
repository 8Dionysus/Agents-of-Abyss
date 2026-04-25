# Experience Distillation Log

This log records decisions that move Experience from long raw packets into light active parts.

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
- `scripts/validate_experience_distillation.py`

Validation:

- `python scripts/validate_experience_distillation.py`
- `python scripts/validate_mechanic_landing_logs.py --mechanic experience`

Stop-lines: do not turn `legacy/raw/` into the active route, do not delete provenance, and do not claim owner-local activation from center distillation.

Next route: future Experience packets land through raw provenance plus active part updates, then owner requests when a stronger owner must accept or prove a slice.

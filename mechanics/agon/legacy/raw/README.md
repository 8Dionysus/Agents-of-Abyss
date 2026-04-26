# Agon Raw Legacy

This directory preserves raw `AGON_*` and `PRE_AGON_BASELINE` source files after
active direction moved to `mechanics/agon/parts/`.

## Rules

- Keep raw filenames stable unless a validator or landing log intentionally
  changes with the move.
- Index every raw file in `../INDEX.md`.
- If a raw file changes active guidance, update the relevant part contract and
  `../DISTILLATION_LOG.md`.
- Do not claim raw provenance is current active direction by itself.

## Validation

```bash
python mechanics/agon/scripts/validate_agon_distillation.py
python scripts/validate_links.py
```

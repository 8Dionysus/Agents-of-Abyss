# Experience Raw Legacy

This directory preserves raw `EXPERIENCE_*` source files after active direction moved to `mechanics/experience/parts/`.

## Rules

- Keep raw filenames stable unless a validator or landing log intentionally changes with the move.
- Index every raw file in `../INDEX.md`.
- If a raw file changes active guidance, update the relevant part contract and `../DISTILLATION_LOG.md`.
- Do not claim raw provenance is current active direction by itself.

## Validation

```bash
python mechanics/experience/scripts/validate_experience_distillation.py
python scripts/validate_links.py
```

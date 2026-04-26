# Questbook Legacy

Legacy is not a trash archive. It is the provenance district for Questbook
source contours that are too heavy for the active route.

## Layout

- `raw/`: preserved historical source documents.
- `INDEX.md`: every raw source mapped to an active Questbook part route.
- `DISTILLATION_LOG.md`: dated accounting for raw-to-active distillation.

The active package reaches this district only through
[`../PROVENANCE.md`](../PROVENANCE.md). Do not duplicate this archive inventory
inside active part docs.

## Use this when

- you need the exact historic surface behind an active part
- you are checking whether old source pressure was fully distilled
- you are auditing stop-lines, owner boundaries, or first-contour provenance

## Stop-lines

- Do not use raw files as the normal first route for routine edits.
- Do not delete raw provenance after distillation.
- Do not make `legacy/raw` the only place a current active rule lives.

## Validation

```bash
python mechanics/questbook/scripts/validate_questbook_distillation.py
python scripts/validate_mechanic_landing_logs.py --mechanic questbook
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
```

# Experience Legacy

Legacy is not a trash archive. It is the provenance district for Experience waves, bridges, laws, tables, compatibility records, and version packets that are too heavy for the active route.

## Layout

- `raw/`: preserved `EXPERIENCE_*` source files.
- `artifacts/`: receipt notes for old flat schemas, examples, validators, and
  tests that now live under active part homes.
- `INDEX.md`: every raw source mapped to an active part route.
- `DISTILLATION_LOG.md`: dated accounting for raw-to-active distillation decisions.

The active package reaches this district only through
[`../PROVENANCE.md`](../PROVENANCE.md). Do not duplicate this archive inventory
inside active part docs.

## Use this when

- you need the exact historic surface behind an active part
- you are checking whether a new wave should become active direction
- you are auditing stop-lines, owner boundaries, or version provenance

## Stop-lines

- Do not use raw files as the normal first route for routine edits.
- Do not delete raw provenance after distillation.
- Do not make legacy/raw the only place a current active rule lives.

## Validation

```bash
python mechanics/experience/scripts/validate_experience_distillation.py
python scripts/validate_mechanic_artifact_topology.py --mechanic experience
python scripts/validate_mechanic_landing_logs.py --mechanic experience
```

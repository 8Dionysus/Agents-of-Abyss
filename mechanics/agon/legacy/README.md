# Agon Legacy

Legacy is not a trash archive. It is the provenance district for Agon waves,
models, stop-lines, handoffs, and source packets that are too heavy for the
active route.

## Layout

- `raw/`: preserved `AGON_*` and `PRE_AGON_BASELINE` source files.
- `artifacts/`: receipt route for the flat-to-part technical artifact move.
- `INDEX.md`: every raw source mapped to an active part route.
- `DISTILLATION_LOG.md`: dated accounting for raw-to-active distillation
  decisions.

The active package reaches this district only through
[`../PROVENANCE.md`](../PROVENANCE.md). Do not duplicate this archive inventory
inside active part docs.

## Use this when

- you need the exact historic surface behind an active part
- you are checking whether a new wave should become active direction
- you are auditing stop-lines, owner boundaries, or source provenance

## Stop-lines

- Do not use raw files as the normal first route for routine edits.
- Do not delete raw provenance after distillation.
- Do not make `legacy/raw/` the only place a current active rule lives.

## Validation

Use the validation lane in [mechanics/agon/legacy/AGENTS.md](AGENTS.md#validation) for executable commands.

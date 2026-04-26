# Experience Provenance Bridge

This is the only active Experience surface that routes back to archival
provenance. Use it when you are auditing how an old source packet was distilled,
not when you need the current operating contract.

## Current route first

Start with the active surfaces:

- [README](README.md)
- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [parts/](parts/)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)

If those surfaces answer the task, stop there. Do not pull archival detail into
the active route.

## Receipt and archive map

The receipt layer and detailed archive account live here:

- [provenance receipts](provenance-receipts.json): receipt IDs used by active
  schemas, examples, validators, and tests when they must cite older packets,
  staged seed inputs, or sibling-owner surfaces without pulling those names into
  the active route. This is an active receipt registry, not an active contract.
- [legacy index](legacy/INDEX.md): preserved source packets mapped to active
  Experience parts.
- [distillation log](legacy/DISTILLATION_LOG.md): what was distilled, where it
  landed, and which boundaries survived.
- [artifact receipt](legacy/artifacts/README.md): how old flat schemas,
  examples, validators, and tests were moved into active part homes.
- [legacy overview](legacy/README.md): archive role, stop-lines, and validation.
- [raw packet district](legacy/raw/README.md): preserved source packet storage.

## Distillation rule

When an archival source changes current behavior, update the relevant active
part first, then update the archive map and distillation log. Active part docs
must not grow per-source lists or archival inventories.

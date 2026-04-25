# Mechanics Route

This file is a compatibility route for older links.

The canonical mechanics atlas now lives at [mechanics/README.md](../mechanics/README.md).
Use that file for the full mechanics compass, package boundaries, stop-lines,
landing logs, and validation paths.

## Current Role

`docs/MECHANICS.md` no longer owns mechanic doctrine.
It exists so readers and older automation that still route through `docs/` can
arrive at the new first-class `mechanics/` tree without treating this file as a
second atlas.

## Canonical Surfaces

- [mechanics/README.md](../mechanics/README.md): mechanics atlas and compass.
- [mechanics/AGENTS.md](../mechanics/AGENTS.md): shared mechanics editing law.
- [mechanics/registry.json](../mechanics/registry.json): machine-readable package registry.
- [mechanics/agon/LANDING_LOG.md](../mechanics/agon/LANDING_LOG.md): Agon landing ledger.
- [mechanics/experience/LANDING_LOG.md](../mechanics/experience/LANDING_LOG.md): Experience landing ledger.

## Compatibility Rule

Do not add new mechanic doctrine here.
Add or update the owning `mechanics/<slug>/` package, then update this route only
if the compatibility story changes.

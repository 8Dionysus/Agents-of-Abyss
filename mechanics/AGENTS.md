# AGENTS.md

This file applies to the root `mechanics/` tree.

## Role

`mechanics/` is the canonical home for center-level AoA mechanics that cross
layers, repos, or future implementation surfaces.
It is not the home for constitutional law, repository ownership law, generated
truth, or owner-local implementation.

Mechanics packages explain how a kind of move grows, repeats, returns, gets
tested, becomes visible, or stays bounded.
They must keep the owning repository boundary explicit.

## Package Law

Every `mechanics/<slug>/` package must contain:

- `AGENTS.md`
- `README.md`
- `ROADMAP.md`
- `LANDING_LOG.md`
- `docs/`

The package `README.md` is the mechanic entry.
The package `ROADMAP.md` is the forward contour.
The package `LANDING_LOG.md` is the checked landing ledger.
The package `docs/` directory holds detailed mechanic-owned doctrine, models,
waves, handoffs, or support notes.

## Boundaries

- `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/FEDERATION_RULES.md`, `docs/LAYERS.md`,
  and `docs/REPO_ROLES.md` remain governance surfaces.
- `QUESTBOOK.md` remains a root public obligation index; `mechanics/questbook/`
  owns questbook mechanics.
- `quests/` remains the quest item store.
- `docs/landings/` remains an archive and receipt district, not a canonical
  mechanic log.
- Generated, schema, config, example, script, and test artifacts may still live
  in root technical districts until a later artifact migration lands.

## Editing Posture

When editing a mechanic:

1. Read this file, then the nearest `mechanics/<slug>/AGENTS.md`.
2. Keep package-local truth in the package.
3. Keep owner-local implementation claims out of center mechanics.
4. Update the mechanic `LANDING_LOG.md` when a checked landing changes.
5. Update `mechanics/registry.json` when a package, owner boundary, required
   surface, or validation route changes.

## Validation

Run the narrow mechanic validator for package topology:

```bash
python scripts/validate_mechanics_topology.py
```

For release-bound mechanics changes, also run:

```bash
python scripts/validate_markdown_shape.py
python scripts/validate_mechanic_landing_logs.py
python scripts/validate_ecosystem.py
python -m pytest -q tests
```

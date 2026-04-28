# Mechanic Artifact Topology

## Purpose

Mechanic packages are not document archives only. A mechanic may own the
schemas, examples, seed config, generated companions, validators, tests, and
quest rules that make its contracts usable.

This topology keeps root technical districts as repository-wide lanes while
moving mechanic-owned substance into mechanic homes.

This file owns placement law only. It does not list every moved file, preserve
old aliases, or replace mechanic-local `artifact-map.json` receipts.

## Root lane

Root technical districts own repository-wide contracts:

- `schemas/`: center, ecosystem, federation, and root-public shape contracts.
- `examples/`: center examples that are not owned by a specific mechanic.
- `config/`: repo-wide validator and hygiene configuration.
- `generated/`: repo-wide compact mirrors and root indexes.
- `scripts/`: release gate, topology, hygiene, and shared root validators.
- `tests/`: root contract tests for root-owned surfaces.
- `quests/`: public quest item store, organized by Questbook lifecycle state.

Root technical districts must not keep mechanic-owned aliases. Established
commands, tests, and public links should be routed to the mechanic-owned path
instead of preserving duplicate root entries.

## Mechanic lane

Mechanic-owned artifacts live under their package. For large mechanics with
functioning parts, prefer the nearest owning part:

```text
mechanics/<slug>/
  parts/<part>/
    schemas/
    examples/
    config/
    generated/
    scripts/
    tests/
```

Use these homes when an artifact only makes sense inside the mechanic's owner
boundary. Examples:

- Agon lawful moves, arena/session packets, duel kernels, retention/rank
  economy, KAG promotion paths, and gate-routing requests belong under
  `mechanics/agon/parts/<part>/`.
- Experience wave, office, service, governance, continuity, deployment, and
  runtime-boundary contracts belong under `mechanics/experience/parts/<part>/`.
- RPG vocabulary overlays and adjunct projection contracts belong under
  `mechanics/rpg/`.
- Antifragility pruning and via-negativa contract checks belong under
  `mechanics/antifragility/`.
- Method-growth lineage witnesses and reviewed-growth seam checks belong under
  `mechanics/method-growth/`.
- Quest lifecycle schemas, quest projections, quest validators, and quest
  closure checks belong under `mechanics/questbook/`.

When a mechanic-owned artifact moves, update callers, validators, generated
indexes, and docs to use the owning path directly; do not add root or flat
package aliases as convenience copies.

Package-local `legacy/raw`, seed, and landing receipt districts are allowed
when they preserve source lineage without becoming alternate active routes.

## Questbook

Questbook is the one intentional root-store exception: `mechanics/questbook/`
owns quest lifecycle, placement, closure, harvest, generated read models, and
owner-routing rules, while root `QUESTBOOK.md` stays a compact frontier index
and `quests/` stays the public item store.

Use `quests/` only for public, reviewable obligations that should survive the
current diff. Do not use it for private scratch work, temporary plans, or
roadmap duplication.

## Validation

Use the validation lane in [mechanics/AGENTS.md](AGENTS.md#validation) for executable commands.

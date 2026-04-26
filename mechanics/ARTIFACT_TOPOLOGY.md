# Mechanic Artifact Topology

## Purpose

Mechanic packages are not document archives only. A mechanic may own the
schemas, examples, seed config, generated companions, validators, tests, and
quest rules that make its contracts usable.

This topology keeps root technical districts as repository-wide lanes while
moving mechanic-owned substance into mechanic homes.

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

## No Root Aliases

Do not add new root-authored mechanic artifacts. Add them to the owning
mechanic package and update callers, validators, generated indexes, and docs to
use that path directly.

For part-based mechanics, do not recreate flat package aliases either. Use
`mechanics/<slug>/artifact-map.json` as the receipt when old flat paths have
been moved into part-local homes.

## Questbook

Questbook is a mechanic, not a TODO pile. The root `QUESTBOOK.md` stays a compact
frontier index, and `quests/` stays the public item store. Quest source objects
live in lane-first lifecycle directories such as `quests/center/triaged/`,
`quests/agon/triaged/`, and `quests/experience/triaged/`; top-level
`quests/AOA-Q-*` aliases are intentionally absent. The questbook package owns
lifecycle, placement, closure, harvest, generated read models, and
owner-routing rules.

Use quests when an obligation should survive the current diff as a public,
reviewable game-object for agents. Do not use quests for private scratch work,
temporary plans, or roadmap duplication.

## Validation

Run:

```bash
python scripts/validate_mechanic_artifact_topology.py
python mechanics/questbook/scripts/validate_questbook_lifecycle.py
python mechanics/questbook/scripts/build_questbook_index.py --check
python mechanics/questbook/scripts/validate_questbook_index.py
```

For release-bound work, also run:

```bash
python scripts/release_check.py
```

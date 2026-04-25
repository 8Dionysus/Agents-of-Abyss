# Mechanic Artifact Topology

## Purpose

Mechanic packages are not document archives only. A mechanic may own the
schemas, examples, seed config, generated companions, validators, tests, and
quest rules that make its contracts usable.

This topology keeps root technical districts as stable entry lanes while moving
mechanic-owned substance into mechanic homes.

## Root lane

Root technical districts own repository-wide contracts:

- `schemas/`: center, ecosystem, federation, and root-public shape contracts.
- `examples/`: center examples that are not owned by a specific mechanic.
- `config/`: repo-wide validator and hygiene configuration.
- `generated/`: repo-wide compact mirrors and root indexes.
- `scripts/`: release gate, topology, hygiene, root wrappers, and shared
  validators.
- `tests/`: root contract tests and compatibility checks.
- `quests/`: public quest item store, organized by Questbook lifecycle state.

Root may keep compatibility aliases for mechanic-owned artifacts when older
commands, tests, or public links still rely on the path. The alias is not the
source of meaning.

## Mechanic lane

Mechanic-owned artifacts live under their package:

```text
mechanics/<slug>/
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
  `mechanics/agon/`.
- Experience wave, office, service, governance, continuity, deployment, and
  runtime-boundary contracts belong under `mechanics/experience/`.
- RPG vocabulary overlays and adjunct projection contracts belong under
  `mechanics/rpg/`.
- Antifragility pruning and via-negativa contract checks belong under
  `mechanics/antifragility/`.
- Method-growth lineage witnesses and reviewed-growth seam checks belong under
  `mechanics/method-growth/`.
- Quest lifecycle schemas, quest projections, quest validators, and quest
  closure checks belong under `mechanics/questbook/`.

## Compatibility aliases

A compatibility alias may remain in a root district only when:

- the target is inside the owning mechanic package;
- the owning mechanic package is the stronger source path;
- the alias exists to keep an established command or public route working;
- validators can distinguish the alias from a root-authored artifact.

Do not add new root-authored mechanic artifacts. Add them to the owning
mechanic package and expose a root alias only when a compatibility surface needs
it.

## Questbook

Questbook is a mechanic, not a TODO pile. The root `QUESTBOOK.md` stays a compact
frontier index, and `quests/` stays the public item store. Quest source objects
live in lifecycle directories such as `quests/triaged/` and `quests/done/`;
top-level `quests/AOA-Q-*` paths are compatibility aliases. The questbook
package owns lifecycle, placement, closure, harvest, and owner-routing rules.

Use quests when an obligation should survive the current diff as a public,
reviewable game-object for agents. Do not use quests for private scratch work,
temporary plans, or roadmap duplication.

## Validation

Run:

```bash
python scripts/validate_mechanic_artifact_topology.py
python scripts/validate_questbook_lifecycle.py
```

For release-bound work, also run:

```bash
python scripts/release_check.py
```

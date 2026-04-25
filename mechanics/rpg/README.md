# RPG Mechanic

RPG is an adjunct reflection layer.
It helps humans read progression, quests, roles, skills, feats, and campaigns
without rewriting ownership or creating a hidden runtime ledger.

## Start Here

- [RPG layer model](docs/RPG_LAYER_MODEL.md)
- [RPG architecture RFC](docs/RPG_ARCHITECTURE_RFC.md)
- [RPG boundary map](docs/RPG_BOUNDARY_MAP.md)
- [RPG first wave](docs/RPG_FIRST_WAVE.md)
- [RPG second wave](docs/RPG_SECOND_WAVE.md)
- [LANDING_LOG](LANDING_LOG.md)

## Owner Boundary

`Agents-of-Abyss` owns center RPG reflection posture.
Role contracts, skills, techniques, playbooks, runtime state, and quest items
remain owner-local or district-owned.

## Validation

```bash
python scripts/validate_mechanics_topology.py --mechanic rpg
```

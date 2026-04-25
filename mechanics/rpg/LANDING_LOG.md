# RPG Landing Log

Canonical landing ledger for the RPG mechanic.

## Entries

### Root mechanics topology migration

Status: landed

Owner boundary: `Agents-of-Abyss` owns adjunct RPG reflection; role, skill,
technique, playbook, quest item, and runtime truth remain owner-local.

Surfaces:

- `mechanics/rpg/README.md`
- `mechanics/rpg/ROADMAP.md`
- `mechanics/rpg/docs/RPG_LAYER_MODEL.md`
- `mechanics/rpg/docs/RPG_ARCHITECTURE_RFC.md`
- `mechanics/rpg/docs/RPG_BOUNDARY_MAP.md`
- `mechanics/rpg/docs/RPG_FIRST_WAVE.md`
- `mechanics/rpg/docs/RPG_SECOND_WAVE.md`

Validation: `python scripts/validate_mechanics_topology.py --mechanic rpg`

Stop-lines: no hidden ontology, runtime ledger, or role-canon mutation.

Next route: keep future RPG projection behind explicit owner gates.

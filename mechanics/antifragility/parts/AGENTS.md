# AGENTS.md

## Applies to

This card applies to `mechanics/antifragility/parts/`.

## Role

Parts are the active operating surface for antifragility. They should be short,
route-shaped, and free of raw wave history.

## Boundaries

- Do not include historical source inventories in part READMEs.
- Do not duplicate validation command blocks in child files.
- Do not claim owner-local deletion, proof, memory, stats, playbook, skill,
  technique, or runtime authority.
- If a part needs historical source material, route to
  `mechanics/antifragility/PROVENANCE.md`.

## Validation

Run:

```bash
python mechanics/antifragility/scripts/validate_antifragility_distillation.py
python scripts/validate_mechanics_topology.py --mechanic antifragility
python -m pytest -q mechanics/antifragility/tests
```

## Closeout

Name the active part changed, the owner route affected, whether `PROVENANCE.md`
was consulted, and which checks were run.

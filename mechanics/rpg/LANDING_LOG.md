# RPG Landing Log

Canonical landing ledger for the RPG mechanic.

## Current Index

- Root mechanics topology migration landed the package and first source docs.
- RPG vocabulary overlay and route polish made the dual-vocabulary contract machine-checkable and linked the remaining active RPG docs into registry, release, and landing validation.
- RPG world-grammar direction defined when game language strengthens agent work and when it must stay silent.

## Entries

### Root mechanics topology migration

Status: landed

Owner boundary: `Agents-of-Abyss` owns adjunct RPG reflection; role, skill, technique, playbook, quest item, and runtime truth remain owner-local.

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

### RPG vocabulary overlay and route polish

Status: landed

Owner boundary: `Agents-of-Abyss` owns RPG presentation vocabulary and center route law; `aoa-agents`, `aoa-skills`, `aoa-playbooks`, `aoa-evals`, `quests/`, and `abyss-stack` keep stronger owner truth.

Surfaces:

- `mechanics/rpg/AGENTS.md`
- `mechanics/rpg/README.md`
- `mechanics/rpg/ROADMAP.md`
- `mechanics/rpg/LANDING_LOG.md`
- `mechanics/rpg/docs/AGENTS.md`
- `mechanics/rpg/docs/RPG_CANONICAL_TERMINOLOGY.md`
- `mechanics/rpg/docs/RPG_SKILLS_AND_FEATS.md`
- `mechanics/rpg/docs/RPG_BRIDGE_WAVE.md`
- `mechanics/rpg/docs/RPG_RUNTIME_PROJECTION_WAVE.md`
- `mechanics/rpg/docs/RPG_OWNER_REPO_REQUESTS.md`
- `mechanics/rpg/schemas/dual_vocabulary_overlay.schema.json`
- `mechanics/rpg/examples/dual_vocabulary_overlay.example.json`
- `mechanics/rpg/generated/dual_vocabulary_overlay.json`
- `mechanics/rpg/scripts/validate_rpg_dual_vocabulary_overlay.py`
- `mechanics/rpg/tests/test_rpg_dual_vocabulary_overlay.py`
- `mechanics/registry.json`
- `scripts/validate_mechanic_landing_logs.py`
- `scripts/release_check.py`
- `tests/test_mechanic_landing_logs.py`
- `CHANGELOG.md`

Validation: `python mechanics/rpg/scripts/validate_rpg_dual_vocabulary_overlay.py`; `python -m pytest -q mechanics/rpg/tests`; `python scripts/validate_mechanic_landing_logs.py --mechanic rpg`; `python scripts/release_check.py`

Stop-lines: no hidden ontology, runtime ledger, role-canon mutation, owner-local activation, proof verdict, quest ownership transfer, or presentation-label overwrite of canonical keys.

Next route: if RPG grows beyond source-doc clarity, create active parts only after the repeated sub-mechanic needs are visible; if wave docs become receipts, move them through a deliberate legacy landing rather than leaving stale active contours.

### RPG world-grammar direction

Status: planted

Owner boundary: `Agents-of-Abyss` may define RPG as world grammar for route, role, quest, consequence, and progression language; owner repositories still own the underlying role, skill, playbook, proof, quest, runtime, memory, and source truth.

Surfaces:

- `mechanics/rpg/DIRECTION.md`
- `mechanics/rpg/AGENTS.md`
- `mechanics/rpg/README.md`
- `mechanics/rpg/ROADMAP.md`
- `mechanics/rpg/LANDING_LOG.md`
- `mechanics/registry.json`
- `generated/agents_mesh.min.json`
- `generated/mechanic_card_index.min.json`
- `scripts/validate_mechanic_landing_logs.py`
- `CHANGELOG.md`

Validation: `python scripts/validate_mechanic_landing_logs.py --mechanic rpg`; `python scripts/release_check.py`

Stop-lines: no toy layer, decorative game skin, universal power score, hidden ontology, runtime ledger, role canon, proof verdict, quest ownership transfer, or presentation-label overwrite of canonical keys.

Next route: deepen RPG only when a repeated world form improves routing, judgment, memory, proof, or consequence; otherwise keep the mechanic quiet and let the owning surface speak plainly.

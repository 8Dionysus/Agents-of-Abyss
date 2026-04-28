# RPG Landing Log

Canonical landing ledger for the RPG mechanic.

## Route index for agents

Read this index before scanning the full ledger. It names the current shape of
RPG without requiring every older landing entry to be re-read.

- Root mechanics topology migration landed the package and first RPG contour sources; those raw sources now live in `mechanics/rpg/legacy/raw/`.
- RPG vocabulary overlay and route polish made the dual-vocabulary contract machine-checkable; the active overlay now lives in `mechanics/rpg/parts/vocabulary-overlay/`.
- RPG world-grammar direction defined when game language strengthens agent work and when it must stay silent.
- RPG active parts and legacy provenance distillation moved working doctrine into `mechanics/rpg/parts/` and kept raw wave notes as receipts.
- RPG active-route polish made every part entry follow one concise route shape and made wave-era prose invalid in active RPG routes.
- RPG usage contract landed a decision table for when RPG language belongs in a task and when plain repository language should win.
- RPG and Questbook now share a playable obligation bridge for derived quest readings without moving quest ownership or lifecycle authority.
- RPG now has one worked playable-obligation route example that shows ordinary task to quest route to RPG reading to proof route to owner handoff without becoming a reusable quest template.
- RPG parts now use explicit route checks and output gates so every part can act as a small working organ without adding more long-form doctrine.
- RPG owner requests now carry ready-to-carry handoff packets so sibling owners can accept, reject, land, or prove slices without reading center requests as acceptance.

Current active route: `mechanics/rpg/README.md`,
`mechanics/rpg/DIRECTION.md`, `mechanics/rpg/USAGE.md`,
`mechanics/rpg/PARTS.md`, `mechanics/rpg/parts/README.md`, and the relevant
part README.

## How to update this log

Every landing entry uses the same shape:

- `Status:`
- `Owner boundary:`
- `Surfaces:`
- `Validation:`
- `Stop-lines:`
- `Next route:`

When a change touches RPG docs, parts, owner requests, source bridges,
validators, examples, or tests, update the relevant entry here or explain in
the PR why the change is not a landing change.

## Entries

### Root mechanics topology migration

Status: landed

Owner boundary: `Agents-of-Abyss` owns adjunct RPG reflection; role, skill, technique, playbook, quest item, and runtime truth remain owner-local.

Surfaces:

- `mechanics/rpg/README.md`
- `mechanics/rpg/ROADMAP.md`
- `mechanics/rpg/legacy/raw/RPG_LAYER_MODEL.md`
- `mechanics/rpg/legacy/raw/RPG_ARCHITECTURE_RFC.md`
- `mechanics/rpg/legacy/raw/RPG_BOUNDARY_MAP.md`
- `mechanics/rpg/legacy/raw/RPG_FIRST_WAVE.md`
- `mechanics/rpg/legacy/raw/RPG_SECOND_WAVE.md`

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
- `mechanics/rpg/parts/vocabulary-overlay/TERMINOLOGY.md`
- `mechanics/rpg/parts/progression-unlocks/README.md`
- `mechanics/rpg/parts/quest-campaign/README.md`
- `mechanics/rpg/parts/runtime-projection/README.md`
- `mechanics/rpg/OWNER_REQUESTS.md`
- `mechanics/rpg/parts/vocabulary-overlay/schemas/dual_vocabulary_overlay.schema.json`
- `mechanics/rpg/parts/vocabulary-overlay/examples/dual_vocabulary_overlay.example.json`
- `mechanics/rpg/parts/vocabulary-overlay/generated/dual_vocabulary_overlay.json`
- `mechanics/rpg/parts/vocabulary-overlay/scripts/validate_vocabulary_overlay.py`
- `mechanics/rpg/parts/vocabulary-overlay/tests/test_vocabulary_overlay.py`
- `mechanics/registry.json`
- `scripts/validate_mechanic_landing_logs.py`
- `scripts/release_check.py`
- `tests/test_mechanic_landing_logs.py`
- `CHANGELOG.md`

Validation: `python mechanics/rpg/parts/vocabulary-overlay/scripts/validate_vocabulary_overlay.py`; `python -m pytest -q mechanics/rpg/parts/vocabulary-overlay/tests`; `python scripts/validate_mechanic_landing_logs.py --mechanic rpg`; `python scripts/release_check.py`

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

### RPG active parts and legacy provenance distillation

Status: landed

Owner boundary: `Agents-of-Abyss` owns active RPG parts and package-level provenance; legacy raw sources remain receipts, not current law, and stronger owner repositories still own role, skill, proof, quest, runtime, playbook, memory, and derived summary truth.

Surfaces:

- `mechanics/rpg/PARTS.md`
- `mechanics/rpg/PROVENANCE.md`
- `mechanics/rpg/OWNER_REQUESTS.md`
- `mechanics/rpg/docs/README.md`
- `mechanics/rpg/parts/README.md`
- `mechanics/rpg/parts/AGENTS.md`
- `mechanics/rpg/parts/world-grammar/README.md`
- `mechanics/rpg/parts/world-grammar/CONTRACT.md`
- `mechanics/rpg/parts/world-grammar/VALIDATION.md`
- `mechanics/rpg/parts/source-boundary/README.md`
- `mechanics/rpg/parts/source-boundary/CONTRACT.md`
- `mechanics/rpg/parts/source-boundary/VALIDATION.md`
- `mechanics/rpg/parts/vocabulary-overlay/README.md`
- `mechanics/rpg/parts/vocabulary-overlay/CONTRACT.md`
- `mechanics/rpg/parts/vocabulary-overlay/VALIDATION.md`
- `mechanics/rpg/parts/vocabulary-overlay/TERMINOLOGY.md`
- `mechanics/rpg/parts/vocabulary-overlay/schemas/dual_vocabulary_overlay.schema.json`
- `mechanics/rpg/parts/vocabulary-overlay/examples/dual_vocabulary_overlay.example.json`
- `mechanics/rpg/parts/vocabulary-overlay/generated/dual_vocabulary_overlay.json`
- `mechanics/rpg/parts/vocabulary-overlay/scripts/validate_vocabulary_overlay.py`
- `mechanics/rpg/parts/vocabulary-overlay/tests/test_vocabulary_overlay.py`
- `mechanics/rpg/parts/quest-campaign/README.md`
- `mechanics/rpg/parts/quest-campaign/CONTRACT.md`
- `mechanics/rpg/parts/quest-campaign/VALIDATION.md`
- `mechanics/rpg/parts/progression-unlocks/README.md`
- `mechanics/rpg/parts/progression-unlocks/CONTRACT.md`
- `mechanics/rpg/parts/progression-unlocks/VALIDATION.md`
- `mechanics/rpg/parts/runtime-projection/README.md`
- `mechanics/rpg/parts/runtime-projection/CONTRACT.md`
- `mechanics/rpg/parts/runtime-projection/VALIDATION.md`
- `mechanics/rpg/parts/owner-handoffs/README.md`
- `mechanics/rpg/parts/owner-handoffs/CONTRACT.md`
- `mechanics/rpg/parts/owner-handoffs/VALIDATION.md`
- `mechanics/rpg/legacy/AGENTS.md`
- `mechanics/rpg/legacy/README.md`
- `mechanics/rpg/legacy/INDEX.md`
- `mechanics/rpg/legacy/DISTILLATION_LOG.md`
- `mechanics/rpg/legacy/raw/README.md`
- `mechanics/rpg/legacy/raw/RPG_LAYER_MODEL.md`
- `mechanics/rpg/legacy/raw/RPG_ARCHITECTURE_RFC.md`
- `mechanics/rpg/legacy/raw/RPG_BOUNDARY_MAP.md`
- `mechanics/rpg/legacy/raw/RPG_FIRST_WAVE.md`
- `mechanics/rpg/legacy/raw/RPG_SECOND_WAVE.md`
- `mechanics/rpg/legacy/raw/RPG_SKILLS_AND_FEATS.md`
- `mechanics/rpg/legacy/raw/RPG_BRIDGE_WAVE.md`
- `mechanics/rpg/legacy/raw/RPG_RUNTIME_PROJECTION_WAVE.md`
- `mechanics/rpg/legacy/artifacts/README.md`
- `mechanics/rpg/scripts/validate_rpg_distillation.py`
- `mechanics/rpg/tests/test_rpg_distillation.py`
- `mechanics/registry.json`
- `mechanics/owner-request-queue.json`
- `scripts/validate_mechanic_artifact_topology.py`
- `scripts/validate_mechanic_landing_logs.py`
- `scripts/release_check.py`
- `scripts/validate_ecosystem.py`
- `tests/test_validate_ecosystem.py`
- `generated/owner_request_queue.min.json`
- `generated/mechanic_card_index.min.json`
- `CHANGELOG.md`

Validation: `python mechanics/rpg/scripts/validate_rpg_distillation.py`; `python mechanics/rpg/parts/vocabulary-overlay/scripts/validate_vocabulary_overlay.py`; `python -m pytest -q mechanics/rpg/tests mechanics/rpg/parts/vocabulary-overlay/tests`; `python scripts/validate_mechanic_landing_logs.py --mechanic rpg`; `python scripts/release_check.py`

Stop-lines: no active route starts from raw legacy, no flat `docs/RPG_*.md` source docs, no flat RPG artifact alias directories, no owner acceptance claim, no runtime activation claim, no universal power score, no presentation-label overwrite of canonical keys.

Next route: route future RPG changes through the specific active part; consult `mechanics/rpg/PROVENANCE.md` only when a historical receipt is needed, then distill rather than dragging raw sources into working docs.

### RPG active-route polish and wave-noise guardrails

Status: landed

Owner boundary: `Agents-of-Abyss` owns concise RPG part routes and validator guardrails; legacy raw sources remain receipts, and stronger owner repositories still own role, skill, proof, quest, runtime, playbook, memory, and derived summary truth.

Surfaces:

- `mechanics/rpg/README.md`
- `mechanics/rpg/PARTS.md`
- `mechanics/rpg/parts/world-grammar/README.md`
- `mechanics/rpg/parts/source-boundary/README.md`
- `mechanics/rpg/parts/vocabulary-overlay/README.md`
- `mechanics/rpg/parts/vocabulary-overlay/TERMINOLOGY.md`
- `mechanics/rpg/parts/quest-campaign/README.md`
- `mechanics/rpg/parts/progression-unlocks/README.md`
- `mechanics/rpg/parts/runtime-projection/README.md`
- `mechanics/rpg/parts/owner-handoffs/README.md`
- `mechanics/rpg/scripts/validate_rpg_distillation.py`
- `mechanics/rpg/tests/test_rpg_distillation.py`
- `scripts/validate_ecosystem.py`
- `tests/test_validate_ecosystem.py`
- `CHANGELOG.md`

Validation: `python mechanics/rpg/scripts/validate_rpg_distillation.py`; `python scripts/validate_ecosystem.py`; `python -m pytest -q mechanics/rpg/tests tests/test_validate_ecosystem.py`

Stop-lines: no wave-era phrasing, raw-source filenames, direct legacy/raw routing, decorative slogans, owner acceptance claim, runtime activation claim, universal power score, or presentation-label overwrite of canonical keys in active RPG routes.

Next route: keep future RPG part changes in the concise active-route shape; if historical detail is needed, route through `mechanics/rpg/PROVENANCE.md` and update the relevant part only after distillation.

### RPG usage contract

Status: landed

Owner boundary: `Agents-of-Abyss` owns the decision table for applying RPG language; stronger owner repositories still own source truth, proof, quest objects, runtime state, memory objects, role canon, skill canon, playbook choreography, and derived stats.

Surfaces:

- `mechanics/rpg/USAGE.md`
- `mechanics/rpg/AGENTS.md`
- `mechanics/rpg/README.md`
- `mechanics/rpg/DIRECTION.md`
- `mechanics/rpg/PARTS.md`
- `mechanics/rpg/ROADMAP.md`
- `mechanics/rpg/scripts/validate_rpg_distillation.py`
- `mechanics/rpg/tests/test_rpg_distillation.py`
- `mechanics/registry.json`
- `CHANGELOG.md`

Validation: `python mechanics/rpg/scripts/validate_rpg_distillation.py`; `python -m pytest -q mechanics/rpg/tests`; `python scripts/validate_mechanics_topology.py --mechanic rpg`; `python scripts/validate_mechanic_readme_cards.py --mechanic rpg`; `python scripts/build_mechanic_card_index.py --check`; `python scripts/validate_mechanic_card_index.py`

Stop-lines: no decorative RPG layer, hidden owner transfer, runtime state claim, proof verdict, quest closure, universal power score, or presentation-label overwrite of canonical keys.

Next route: use `mechanics/rpg/USAGE.md` before selecting an RPG part; for quest-shaped obligations, route first through Questbook and then attach RPG reading only as derived context.

### RPG and Questbook playable obligation bridge

Status: landed

Owner boundary: `Agents-of-Abyss` owns the RPG reading shape for playable obligations; Questbook owns source quest objects, lifecycle, lane placement, public index posture, generated read models, and source contracts.

Surfaces:

- `mechanics/rpg/parts/quest-campaign/PLAYABLE_OBLIGATION.md`
- `mechanics/rpg/parts/quest-campaign/README.md`
- `mechanics/rpg/README.md`
- `mechanics/rpg/USAGE.md`
- `mechanics/rpg/scripts/validate_rpg_distillation.py`
- `mechanics/rpg/tests/test_rpg_distillation.py`
- `mechanics/questbook/parts/model-spine/RPG_PLAYABLE_READING.md`
- `mechanics/questbook/README.md`
- `mechanics/questbook/PARTS.md`
- `mechanics/questbook/parts/README.md`
- `mechanics/questbook/parts/model-spine/README.md`
- `mechanics/questbook/parts/registry.json`
- `mechanics/questbook/scripts/validate_questbook_distillation.py`
- `mechanics/questbook/tests/test_questbook_distillation.py`
- `mechanics/registry.json`
- `CHANGELOG.md`

Validation: `python mechanics/rpg/scripts/validate_rpg_distillation.py`; `python mechanics/questbook/scripts/validate_questbook_distillation.py`; `python -m pytest -q mechanics/rpg/tests mechanics/questbook/tests/test_questbook_distillation.py`; `python scripts/validate_mechanics_topology.py --mechanic questbook`; `python scripts/validate_mechanics_topology.py --mechanic rpg`; `python scripts/validate_mechanic_readme_cards.py --mechanic questbook`; `python scripts/validate_mechanic_readme_cards.py --mechanic rpg`

Stop-lines: no RPG quest lifecycle authority, quest closure, proof completion, owner acceptance, reward authority, universal score, runtime state, or boilerplate RPG fields across quest sources.

Next route: use the bridge when a quest needs campaign, party, stake, proof route, unlock question, or consequence reading; keep source quest movement in Questbook.

### RPG playable obligation worked route example

Status: landed

Owner boundary: `Agents-of-Abyss` owns one explanatory worked route for RPG reflection; Questbook still owns quest lifecycle and source quest truth, while owner repositories keep proof, runtime, memory, and acceptance authority.

Surfaces:

- `mechanics/rpg/parts/quest-campaign/examples/playable-obligation-route.md`
- `mechanics/rpg/README.md`
- `mechanics/rpg/DIRECTION.md`
- `mechanics/rpg/USAGE.md`
- `mechanics/rpg/scripts/validate_rpg_distillation.py`
- `mechanics/rpg/tests/test_rpg_distillation.py`
- `mechanics/registry.json`

Validation: `python mechanics/rpg/scripts/validate_rpg_distillation.py`; `python -m pytest -q mechanics/rpg/tests`

Stop-lines: no repeated example boilerplate across quest sources, no quest lifecycle claim, no proof verdict, no runtime activation, no owner acceptance, and no memory ownership claim from the example.

Next route: use the example only to understand the shape of a route; for live work, start from the source quest and the relevant owner surface.

### RPG part usability route checks

Status: landed

Owner boundary: `Agents-of-Abyss` owns the active RPG part route shape; stronger owner repositories still own role, skill, technique, proof, stats, quest, playbook, memo, runtime, and presentation authority.

Surfaces:

- `mechanics/rpg/PARTS.md`
- `mechanics/rpg/ROADMAP.md`
- `mechanics/rpg/parts/world-grammar/README.md`
- `mechanics/rpg/parts/world-grammar/CONTRACT.md`
- `mechanics/rpg/parts/source-boundary/README.md`
- `mechanics/rpg/parts/source-boundary/CONTRACT.md`
- `mechanics/rpg/parts/vocabulary-overlay/README.md`
- `mechanics/rpg/parts/vocabulary-overlay/CONTRACT.md`
- `mechanics/rpg/parts/quest-campaign/README.md`
- `mechanics/rpg/parts/quest-campaign/CONTRACT.md`
- `mechanics/rpg/parts/progression-unlocks/README.md`
- `mechanics/rpg/parts/progression-unlocks/CONTRACT.md`
- `mechanics/rpg/parts/runtime-projection/README.md`
- `mechanics/rpg/parts/runtime-projection/CONTRACT.md`
- `mechanics/rpg/parts/owner-handoffs/README.md`
- `mechanics/rpg/parts/owner-handoffs/CONTRACT.md`
- `mechanics/rpg/scripts/validate_rpg_distillation.py`
- `mechanics/rpg/tests/test_rpg_distillation.py`
- `CHANGELOG.md`

Validation: `python mechanics/rpg/scripts/validate_rpg_distillation.py`; `python -m pytest -q mechanics/rpg/tests`

Stop-lines: no new doctrine sprawl, no hidden owner transfer, no proof verdict, no runtime activation, no quest lifecycle claim, and no universal score.

Next route: grow individual parts only when their route check exposes a repeated form that needs a new checked surface.

### RPG ready-to-carry owner request packets

Status: landed

Owner boundary: `Agents-of-Abyss` owns center-side request packets and stop-lines; `aoa-agents`, `aoa-skills`, `aoa-playbooks`, `aoa-evals`, `abyss-stack`, and `aoa-stats` still accept, reject, land, prove, or defer their own slices.

Surfaces:

- `mechanics/rpg/OWNER_REQUESTS.md`
- `mechanics/rpg/scripts/validate_rpg_distillation.py`
- `mechanics/rpg/tests/test_rpg_distillation.py`
- `mechanics/rpg/LANDING_LOG.md`
- `CHANGELOG.md`

Validation: `python mechanics/rpg/scripts/validate_rpg_distillation.py`; `python -m pytest -q mechanics/rpg/tests`

Stop-lines: ready-to-carry packets are not owner acceptance, owner landing, proof verdict, runtime activation, stats authority, role canon, skill canon, playbook choreography, or quest closure.

Next route: carry the relevant `ORQ-RPG-*` card into the owner repository only when that owner is ready to accept or decline the slice, then return an owner-local receipt before updating queue refs.

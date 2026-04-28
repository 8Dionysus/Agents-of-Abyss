# AGENTS.md

## Applies to

This card applies to `mechanics/rpg/` and every nested path under that scope
until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, this card,
`mechanics/rpg/README.md`, `mechanics/rpg/DIRECTION.md`,
`mechanics/rpg/PARTS.md`, and `mechanics/rpg/USAGE.md` before changing this
package.
For active doctrine, start from `mechanics/rpg/PARTS.md` and the relevant part under `mechanics/rpg/parts/`.
For historical evidence, use `mechanics/rpg/PROVENANCE.md` first; consult `legacy/raw/` only through that route.
For vocabulary artifacts, read `mechanics/rpg/parts/vocabulary-overlay/TERMINOLOGY.md` before touching schema, example, generated overlay, or validator files.

## Boundaries

- Do not turn RPG terms into hidden ontology, runtime ledger authority, role canon, proof verdicts, or quest ownership.
- Do not let presentation labels replace canonical machine keys.
- Do not treat generated RPG artifacts as authored meaning; they must mirror the terminology and schema contract.
- Do not cite raw legacy sources as active law; distill needed material into a part and record provenance.
- If RPG creates a stronger-owner request, update `mechanics/rpg/OWNER_REQUESTS.md` and the owner-request queue surfaces instead of pretending the owner accepted it.

## Closeout

Closeout must name changed RPG active parts, whether `PROVENANCE.md` was
consulted, whether vocabulary or owner requests changed, checks run, checks
skipped, remaining risk, and the next owner route if RPG was only a reflection
waypoint.

If `PROVENANCE.md` was consulted, name only the relevant legacy map,
distillation log, or receipt section. Do not enumerate raw legacy sources
unless the task specifically audited archive evidence in depth.

## Role

RPG owns adjunct reflection for progression, questlines, campaigns, skills,
feats, unlock proof, and readable navigation.

It makes cross-owner work easier to see without changing the owner of roles,
skills, playbooks, proof, quests, runtime state, or source meaning.

## Source Surfaces

- `README.md`: package entry and route.
- `DIRECTION.md`: current active mechanic direction.
- `USAGE.md`: active usage posture.
- `PARTS.md`: active functioning-part map.
- `parts/`: concise active RPG contracts.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `ROADMAP.md`: current and next RPG contour.
- `LANDING_LOG.md`: checked RPG landing ledger.
- `PROVENANCE.md`: controlled bridge to legacy and source accounting.
- `legacy/`: archival source material, not active law.
- `docs/`: detailed doctrine and support notes.

## Post-change route review

After RPG changes, check whether the next agent can start from `README.md`, `DIRECTION.md`, `USAGE.md`, `PARTS.md`, and the relevant active part without reading raw legacy.
If an active part needs history, distill the rule into the part and route the evidence through `PROVENANCE.md`, `legacy/INDEX.md`, and `legacy/DISTILLATION_LOG.md`.

Check whether the move changed:

- `DIRECTION.md`: current RPG posture or language boundary.
- `USAGE.md`: usage route, task-reading route, or reflection posture.
- `PARTS.md`: active part boundaries or functioning-part map.
- `OWNER_REQUESTS.md` and `mechanics/owner-request-queue.json`: role, skill,
  playbook, proof, quest, runtime, or owner-local asks.
- `ROADMAP.md`: useful future route or unresolved RPG contour.
- `LANDING_LOG.md`: a reviewable landing or planted contract.
- `PROVENANCE.md`: legacy bridge, receipt route, or archive map.
- vocabulary artifacts: terminology, schema, example, generated overlay, or
  validator surfaces.
- `mechanics/registry.json` and generated indexes: card-facing route, owner
  boundary, validation refs, or public summaries.

Only update a surface when its meaning moved. Leave it untouched when the
change does not affect its job.

## Validation

Run the narrow RPG lane after package changes:

```bash
python scripts/validate_mechanics_topology.py --mechanic rpg
python scripts/validate_mechanic_readme_cards.py --mechanic rpg
python scripts/validate_mechanic_landing_logs.py --mechanic rpg
python scripts/validate_mechanic_artifact_topology.py --mechanic rpg
python mechanics/rpg/scripts/validate_rpg_distillation.py
python mechanics/rpg/parts/vocabulary-overlay/scripts/validate_vocabulary_overlay.py
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python -m pytest -q mechanics/rpg/tests mechanics/rpg/parts/vocabulary-overlay/tests
```

If owner requests changed, also run:

```bash
python scripts/validate_owner_request_queue.py --mechanic rpg
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic rpg
```

For release-readiness or cross-mechanic edits, finish with:

```bash
python scripts/release_check.py
```

<!-- centralized-child-validation:start -->

### Centralized Child Validation

Executable validation commands from child docs live here. Child docs should
route to this section instead of carrying command blocks.

#### `mechanics/rpg/README.md`

```bash
python scripts/validate_mechanics_topology.py --mechanic rpg
python scripts/validate_mechanic_readme_cards.py --mechanic rpg
python scripts/validate_mechanic_landing_logs.py --mechanic rpg
python scripts/validate_mechanic_artifact_topology.py --mechanic rpg
python mechanics/rpg/scripts/validate_rpg_distillation.py
python mechanics/rpg/parts/vocabulary-overlay/scripts/validate_vocabulary_overlay.py
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python -m pytest -q mechanics/rpg/tests mechanics/rpg/parts/vocabulary-overlay/tests
python scripts/validate_owner_request_queue.py --mechanic rpg
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic rpg
```

<!-- centralized-child-validation:end -->

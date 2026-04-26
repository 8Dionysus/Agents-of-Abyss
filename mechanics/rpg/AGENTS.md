# AGENTS.md

## Applies to

This card applies to `mechanics/rpg/` and every nested path under that scope until a nearer `AGENTS.md` narrows the lane.

## Role

RPG owns adjunct reflection for progression, questlines, campaigns, skills, feats, unlock proof, and readable navigation.
It makes cross-owner work easier to see without changing the owner of roles, skills, playbooks, proof, quests, runtime state, or source meaning.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, this card, `mechanics/rpg/README.md`, and `mechanics/rpg/DIRECTION.md` before changing this package.
For detailed doctrine, read the specific source document under `mechanics/rpg/docs/`.
For vocabulary artifacts, read `mechanics/rpg/docs/RPG_CANONICAL_TERMINOLOGY.md` before touching schema, example, or generated overlay files.

## Boundaries

- Do not turn RPG terms into hidden ontology, runtime ledger authority, role canon, proof verdicts, or quest ownership.
- Do not let presentation labels replace canonical machine keys.
- Do not treat generated RPG artifacts as authored meaning; they must mirror the terminology and schema contract.
- If RPG creates a stronger-owner request, update `mechanics/rpg/docs/RPG_OWNER_REPO_REQUESTS.md` and the owner-request queue surfaces instead of pretending the owner accepted it.

## Validation

Run the narrow RPG lane after package changes:

```bash
python scripts/validate_mechanics_topology.py --mechanic rpg
python scripts/validate_mechanic_readme_cards.py --mechanic rpg
python scripts/validate_mechanic_landing_logs.py --mechanic rpg
python mechanics/rpg/scripts/validate_rpg_dual_vocabulary_overlay.py
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python -m pytest -q mechanics/rpg/tests
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

Executable validation commands from child docs live here. Child docs should route to this section instead of carrying command blocks.

#### `mechanics/rpg/README.md`

```bash
python scripts/validate_mechanics_topology.py --mechanic rpg
python scripts/validate_mechanic_readme_cards.py --mechanic rpg
python scripts/validate_mechanic_landing_logs.py --mechanic rpg
python mechanics/rpg/scripts/validate_rpg_dual_vocabulary_overlay.py
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python -m pytest -q mechanics/rpg/tests
python scripts/validate_owner_request_queue.py --mechanic rpg
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic rpg
```

<!-- centralized-child-validation:end -->

## Closeout

Closeout must name changed RPG surfaces, whether vocabulary or owner requests changed, checks run, checks skipped, remaining risk, and the next owner route if RPG was only a reflection waypoint.

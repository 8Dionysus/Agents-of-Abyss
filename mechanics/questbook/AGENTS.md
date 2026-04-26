# AGENTS.md

## Applies to

This card applies to `mechanics/questbook/` and every nested path under that
scope until a nearer `AGENTS.md` narrows the lane.

## Role

Questbook owns the mechanics of public obligations, quest lifecycle, placement,
risk, difficulty, relations, and harvest rules.

Root `QUESTBOOK.md` remains the public index. `quests/` remains the quest item
store. Source quest objects live under lane-first lifecycle directories such as
`quests/center/triaged/`, `quests/agon/ready/`, and `quests/experience/done/`;
root-level `AOA-Q-*` aliases and root lifecycle directories are intentionally
absent.

## Read before editing

Read the repository root `AGENTS.md`, this card, and the nearest `README.md` or
protocol surface before changing files in this lane.

For source-law changes, read `parts/model-spine/README.md` first, then the
narrow part source it points to. For relation changes, also read
`parts/relation-shape/README.md`. For ready-owner route changes, read
`parts/lane-owner-routes/README.md`, edit the JSON registry, and rebuild the
Markdown projection instead of editing generated route rows by hand.
For source object shape changes, read `parts/source-contract/README.md` before
touching quest files.

## Boundaries

- Do not use this lane to override owner-local truth, generated-source
  boundaries, sibling-repo authority, or release validation contracts.
- Do not treat `sidequest` as owner transfer, dependency, acceptance, or closure
  proof.
- Do not turn Questbook into a second roadmap, private scratchpad, scheduler,
  proof ledger, runtime state, or hidden memory.
- Generated Questbook surfaces summarize source quest files; they do not author
  quest meaning.

## Editing route

- If the source quest files change, rebuild generated Questbook views.
- If relation shape changes, run relation validation.
- If an owner-request route changes, rebuild the ready-owner route projection,
  validate the owner-request queue, and validate owner-request docs.
- If package entry surfaces change, validate mechanic topology and README cards.
- Keep executable validation commands in this file. Other Questbook Markdown
  surfaces should route here instead of duplicating command blocks.

## Post-change Route Review

Before closeout, review the changed route rather than only the changed file:

- Source quest changed: confirm lane, lifecycle state, source contract,
  relation shape, generated Questbook views, and owner boundary.
- Part changed: confirm `parts/registry.json`, `PARTS.md`, `parts/README.md`,
  the part contract, validation route, landing log, and provenance route still
  agree.
- Owner-request route changed: confirm the request packet, queue, generated
  queue, ready-owner route table, and owner acceptance boundary.
- AGENTS, docs, or decision surface changed: rebuild the matching generated
  index and make sure the active route did not move into legacy/raw.
- Repeated defaults appear in quest sources: move the default to the lane
  README and keep only a short per-quest route to it.

## Validation

Run the narrow checks for the touched surface:

```bash
python scripts/validate_mechanics_topology.py --mechanic questbook
python scripts/validate_mechanic_readme_cards.py --mechanic questbook
python scripts/validate_mechanic_landing_logs.py --mechanic questbook
python mechanics/questbook/scripts/validate_questbook_source_contract.py
python mechanics/questbook/scripts/validate_questbook_lifecycle.py
python mechanics/questbook/scripts/build_questbook_index.py --check
python mechanics/questbook/scripts/validate_questbook_index.py
python mechanics/questbook/scripts/validate_quest_relations.py
python mechanics/questbook/scripts/build_ready_owner_routes.py --check
python mechanics/questbook/scripts/validate_ready_owner_routes.py
python mechanics/questbook/scripts/validate_questbook_distillation.py
python scripts/validate_owner_request_queue.py --mechanic questbook
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic questbook
python scripts/validate_owner_request_queue.py --mechanic experience
python scripts/validate_owner_request_docs.py --mechanic experience
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_ecosystem.py
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
python scripts/validate_generated_freshness.py
python -m pytest -q mechanics/questbook/tests
```

Use `python scripts/release_check.py` when route, generated, validation, or
release-facing surfaces change together.

## Closeout

Closeout must name changed surfaces, generated mirrors rebuilt or not rebuilt,
owner-request status affected, checks run, checks skipped, remaining risk, and
the next owner route if this lane was only a waypoint.

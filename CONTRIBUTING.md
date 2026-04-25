# Contributing to Agents of Abyss

Thank you for helping shape AoA.

`Agents-of-Abyss` is the constitutional polis of AoA. It names, maps, governs, audits, and routes the federation. It is not the default home for every technique, skill, proof, memory object, role, playbook, graph projection, runtime service, or ToS-authored meaning.

A good contribution here makes the federation more legible without making the center fatter.

## What belongs here

Good contributions for this repository include:

- improvements to the AoA charter
- clearer ecosystem maps
- better layer definitions and repository-role routing
- better federation rules and source-of-truth boundaries
- root surface governance and cleanup
- glossary improvements
- questbook entries that cross repository boundaries
- program-level roadmap updates
- compact machine-readable ecosystem registry improvements
- entrypoints for humans, low-context models, and coding agents
- validators and tests that protect center-level claims

## What usually does not belong here

Do not use this repository as the default home for:

- new technique bundles
- new skill bundles
- new eval bundles
- memory objects
- role/persona canon
- scenario playbook canon after the scenario becomes operational
- graph or retrieval projections as source canon
- runtime implementation details
- ToS-authored knowledge meaning
- large specialized corpora that already belong in a dedicated AoA repository

If a change mainly belongs to one specialized layer, prefer changing that layer's source repository first.

## Source-of-truth discipline

When contributing, preserve this rule:

- source repositories own meaning
- coordination repositories own maps
- derived repositories own downstream projections
- routing repositories route
- runtime repositories run the body
- support surfaces help without becoming authority

Examples:

- `aoa-techniques` owns technique truth
- `aoa-skills` owns skill truth
- `aoa-evals` owns eval truth
- `aoa-stats` owns derived observability, not authority
- `aoa-routing` owns navigation surfaces
- `aoa-memo` owns memory and recall posture
- `aoa-agents` owns role and persona truth
- `aoa-playbooks` owns recurring scenario choreography once operational
- `aoa-kag` owns derived knowledge substrate work
- `abyss-stack` owns runtime infrastructure
- `Tree-of-Sophia` owns ToS-authored knowledge meaning
- `Agents-of-Abyss` owns ecosystem-level truth, center mechanics, and root surface law

## Before you edit

Use the canonical route contract before you widen a center claim or move
material into this repository:
[`docs/START_HERE_ROUTE_CONTRACT.md`](docs/START_HERE_ROUTE_CONTRACT.md).

| Route mode | Contributor use |
|---|---|
| `first-reading` | understand the center before expanding a claim |
| `root-editing` | add, move, delete, rename, or rewrite root surfaces |
| `direction-change` | change roadmap, phase, maturity, release contour, or declared direction |
| `ownership-routing` | decide which repository owns a change |
| `mechanic-change` | edit center-level process, Agon, Experience, recurrence, quest/RPG, antifragility, or ToS support |
| `public-claim-validation` | check whether public language is honest and supportable |
| `low-context-agent` | use a compact machine route before full reading |
| `district-work` | follow local README gates inside technical districts |

Use this check path:

1. Read [CHARTER](CHARTER.md) for ownership boundaries.
2. Read [ECOSYSTEM_MAP](ECOSYSTEM_MAP.md) for the current documented public federation contour.
3. Read [docs/FEDERATION_RULES](docs/FEDERATION_RULES.md) for source-of-truth discipline.
4. Read [docs/ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md) before adding, moving, deleting, or renaming any root-level file.
5. Read [mechanics/README](mechanics/README.md) before editing center-level process, Agon, Experience, recurrence, quest/RPG, antifragility, or ToS-support surfaces.
6. Read the relevant LANDING_LOG before editing Agon or Experience landing surfaces: [Agon LANDING_LOG](mechanics/agon/LANDING_LOG.md) or [Experience LANDING_LOG](mechanics/experience/LANDING_LOG.md).
7. Read the local district README before changing `generated/`, `scripts/`, `schemas/`, `tests/`, `config/`, `examples/`, `manifests/`, or `quests/`.
   For mechanic-owned artifacts, follow the root alias into `mechanics/<slug>/`.
8. Read [ROADMAP](ROADMAP.md) for declared direction and current phase.
9. Check generated capsules before claiming the change is complete.

## How to decide where a change belongs

Ask these questions in order:

1. Does this change define or revise the meaning of a specialized object class?
   - If yes, it probably belongs in a specialized repository.
2. Does this change clarify how AoA layers relate to one another?
   - If yes, it may belong here.
3. Does this change add a new ecosystem-level rule, boundary, or roadmap statement?
   - If yes, it may belong here.
4. Does this change add, remove, rename, or move a root-level file?
   - If yes, state the root surface class from [docs/ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md).
5. Does this change duplicate material that already has a better source-of-truth home?
   - If yes, move or route to the better home instead.
6. Does this change make a center claim?
   - If yes, state what owner truth it deliberately does not absorb.

## Pull request shape

A strong pull request in this repository should explain:

- what ecosystem-level surface changed
- why the change belongs in `Agents-of-Abyss`
- which root surface class, mechanic branch, or technical district is involved
- what neighboring repositories are affected
- what is intentionally left to specialized repositories
- which generated surfaces, schemas, scripts, and tests were checked
- what future step remains open, if any

Prefer opening a clear next step over planting a placeholder.

## Validation

Use the smallest relevant validation set, then widen when generated surfaces or schemas are touched.

Baseline center checks:

```bash
python scripts/plan_docs_thematic_cleanup.py --check
python scripts/validate_docs_thematic_districts.py
python scripts/validate_docs_migration_map.py
python scripts/build_docs_thematic_index.py --check
python scripts/validate_docs_thematic_index.py
python scripts/repair_known_link_drifts.py --check
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
python scripts/validate_status_vocabulary.py
python scripts/build_link_shape_hygiene_index.py --check
python scripts/validate_link_shape_hygiene_index.py
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
python scripts/validate_entry_surface_sync.py
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_mechanics_topology.py
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_mechanic_landing_logs.py
python scripts/validate_generated_freshness.py
python scripts/validate_hygiene_suite.py
python scripts/validate_ecosystem.py
python -m pytest -q tests
```

If the change touches Agon, Experience, generated capsules, schemas, quests, or release posture, run the nearest matching validator and test named by the affected surface.

## Style guidance

Prefer:

- compactness over sprawl
- explicit boundaries over vague ambition
- readable maps over abstract grandiosity
- stable layer distinctions over convenience duplication
- one canonical surface over duplicate meaning
- reviewable receipts over hidden mutation
- future routes over inert stubs

Avoid:

- adding a root file because a thought feels important
- turning audit artifacts into constitutional law
- copying owner-local truth into center prose
- letting generated surfaces outrank sources
- making a route hint sound like authority
- using examples as proof
- using memory as verdict

## If you are unsure

When in doubt, choose the narrower change.

If the change feels like the beginning of a new layer, name that possibility explicitly and route it. Do not force it into the wrong repository just because the center is nearby.

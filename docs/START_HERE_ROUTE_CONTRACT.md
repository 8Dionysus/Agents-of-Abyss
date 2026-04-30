# Start Here Route Contract

This document is the canonical route contract for the `Start here` surface of `Agents-of-Abyss`.
The canonical file path is `docs/START_HERE_ROUTE_CONTRACT.md`.

It answers one question: when a human, agent, contributor, validator, or downstream owner enters the center, what path should they follow before changing or trusting anything?

The route contract exists because one flat reading list is no longer enough. The same entry sequence cannot serve first-time readers, root editors, mechanic authors, release auditors, low-context agents, and technical district workers equally well.

## Contract rule

Every public entry surface must agree on the same route modes.

The route modes are reflected in:

- `README.md`
- `docs/README.md`
- `mechanics/README.md`
- `mechanics/registry.json`
- `mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md`
- `CONTRIBUTING.md`
- `generated/center_entry_map.min.json`
- `schemas/center-entry-map.schema.json`
- `scripts/center_entry_map_common.py`
- `scripts/validate_center_entry_map.py`
- `tests/test_center_entry_map.py`

If one of those surfaces changes the route order or adds a new route mode, the others must be updated in the same change.

## Route modes

| Route mode | Audience | Job | Canonical path |
|---|---|---|---|
| `first-reading` | humans, new agents, outside readers | understand the center without entering every district | `README.md` -> `CHARTER.md` -> `ECOSYSTEM_MAP.md` -> `docs/FEDERATION_RULES.md` |
| `root-editing` | contributors, coding agents, maintainers | change root surfaces without making the root a warehouse | first reading -> `CONTRIBUTING.md` -> `docs/ROOT_SURFACE_LAW.md` |
| `direction-change` | maintainers, release agents | update roadmap, phase, maturity, transition, or release contour | first reading -> `ROADMAP.md` -> `mechanics/release-support/DIRECTION.md` -> `mechanics/release-support/docs/DIRECTION_SURFACES.md` -> `CHANGELOG.md` |
| `ownership-routing` | humans and agents deciding where work belongs | choose the owner repository for a change | first reading -> `docs/LAYERS.md` -> `docs/REPO_ROLES.md` |
| `mechanic-change` | authors of Agon, Experience, recurrence, growth, quest/RPG, release-support, or ToS support surfaces | edit a process without stealing owner truth | first reading -> `mechanics/README.md` -> `mechanics/<slug>/README.md` -> the relevant stop-line surface |
| `public-claim-validation` | release agents, public docs editors, reviewers | decide whether the center may honestly claim something | `mechanics/release-support/README.md` -> `mechanics/release-support/PARTS.md` -> `mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md` -> generated capsules -> validators |
| `low-context-agent` | small models, retrieval systems, capsule-first agents | get a compact route before reading full docs | `generated/center_entry_map.min.json` |
| `district-work` | contributors already inside a technical district | respect local file purpose and validation boundaries | root route -> local district `README.md` |

## First-reading route

The first-reading route is the shortest honest center overview.

Read:

1. `README.md`
2. `CHARTER.md`
3. `ECOSYSTEM_MAP.md`
4. `docs/FEDERATION_RULES.md`

This route answers:

- what the polis is
- what the federation is
- what the center owns
- what the center must not absorb
- what source-of-truth discipline protects

This route does not answer every mechanic, implementation, proof, memory, role, runtime, graph, or ToS question. It points to the owner surface that can answer those questions.

## Root-editing route

Use this route before changing anything visible at repository root.

Read:

1. first-reading route
2. `CONTRIBUTING.md`
3. `docs/ROOT_SURFACE_LAW.md`
4. local audit evidence when cleanup is involved

Root-editing changes must state the root surface class:

- civic law and public map
- public governance or legal surface
- thin civic index
- machine or developer district
- agent lane
- development requirement

Root-editing changes must not create root files merely because a package, note, audit, or future idea feels important. Mechanic receipts belong in the owning `mechanics/<slug>/legacy/raw/` route. Generic movement traces belong in `docs/traces/`. Audit artifacts belong in `mechanics/audit/` or `mechanics/audit/legacy/raw/`. Registry evolution belongs in the aligned schema, generated capsule, validator, source docs, and decision-record route when it changes public interpretation. Generated objects belong in `generated/`.

## Direction-change route

Use this route before changing the roadmap, current phase, maturity posture,
state-transition contour, or public release contour.

Read:

1. first-reading route
2. `ROADMAP.md`
3. `mechanics/release-support/DIRECTION.md`
4. `mechanics/release-support/docs/DIRECTION_SURFACES.md`
5. `CHANGELOG.md`
6. `mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md` when the change affects public claims

Direction changes must distinguish:

- current state
- next work
- long-horizon direction
- released history
- owner-local commitments

`ROADMAP.md` should not become the ledger of every package. Mechanic landing
history belongs in the relevant `LANDING_LOG`, repository release history
belongs in `CHANGELOG.md`, historical receipts belong in the owning mechanic legacy or `docs/traces/`, and
source detail remains in the relevant wave-specific docs.

## Ownership-routing route

Use this route when the question is where a change belongs.

Read:

1. first-reading route
2. `docs/LAYERS.md`
3. `docs/REPO_ROLES.md`
4. `mechanics/README.md` only if the change is also a process or mechanic

Ownership-routing changes must not move owner truth into the center because the center is nearby. The center may name and route. The owner repository owns the primary object.

## Mechanic-change route

Use this route when the change touches an engineering-philosophy mechanic.

Examples:

- Agon
- Experience
- recurrence, return, or continuity
- method and growth refinery
- antifragility or via negativa
- questbook or RPG reflection
- boundary bridge, ToS support, witness, or compost support
- release, audit, or public support posture

Read:

1. first-reading route
2. `mechanics/README.md`
3. `mechanics/<slug>/README.md`
4. `mechanics/<slug>/LANDING_LOG.md` when a landing changed
5. the stop-line surface for the specific branch
6. the builder, validator, and test named by the affected generated surface when one exists

Mechanic changes must name their owner split. A mechanic is healthy only when it makes ownership easier to inspect.

## Public-claim-validation route

Use this route when a sentence sounds like a public promise or an internal
transition is about to become public-facing.

Read:

1. `mechanics/release-support/README.md`
2. `mechanics/release-support/PARTS.md`
3. `mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md`
4. `CHARTER.md`
5. `ECOSYSTEM_MAP.md`
6. `docs/FEDERATION_RULES.md`
7. generated capsules
8. validators

A center claim is honest only when the human docs, generated capsules, validators, and release posture agree in the same landed state.

## Low-context-agent route

Use this route when a small model, retrieval system, or coding agent needs a compact entry surface.

Read:

1. `generated/center_entry_map.min.json`
2. the `surface_ref` for the selected route
3. the `human_path` for that route
4. the `verification_refs` before trusting the route

The generated route is a companion, not a replacement. It accelerates orientation. It does not author meaning.

## District-work route

Use this route when you are already inside a technical district.

Local gates include:

- `generated/README.md`
- `scripts/README.md`
- `schemas/README.md`
- `tests/README.md`
- `config/README.md`
- `examples/README.md`
- `manifests/README.md`
- `quests/README.md`

A district README explains local purpose, not constitutional authority. When local guidance conflicts with center law, return to the stronger center surface and re-enter through a smaller change.

## Machine contract

The machine-facing route contract is `generated/center_entry_map.min.json`.

It must publish:

- `schema_version`
- `route_contract_ref`
- `authority_ref`
- `public_root_ref`
- `registry_ref`
- `supporting_inventory_ref`
- `validation_refs`
- `routes`

Each route must publish:

- `route_id`
- `route_mode`
- `priority`
- `audience`
- `need`
- `surface_ref`
- `human_path`
- `machine_surface_refs`
- `verification_refs`
- `must_not_claim`

The compact route should be useful to an agent without encouraging it to skip human docs.

## Validation

Run:

```bash
python scripts/repair_known_link_drifts.py --check
python scripts/validate_traces_district.py
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
python scripts/validate_mechanic_landing_logs.py
python scripts/validate_generated_freshness.py
python scripts/validate_hygiene_suite.py
python scripts/validate_ecosystem.py
python -m pytest -q
```

If a route change touches Agon, Experience, quests, schemas, generated surfaces, or release posture, run the nearest specific validator and test as well.

## Anti-stub rule

Do not add empty route modes, future placeholders, or vague next-step labels.

A route must either:

- point to a current readable surface
- name a clear owner and stop-line
- or be deferred as a quest or roadmap item rather than pretending to exist

Opening a real next step is better than planting an inert stub.

## Final rule

The `Start here` surface is healthy when a reader can stop early without being deceived and go deeper without getting lost.

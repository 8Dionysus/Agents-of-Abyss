# Public Support Posture

This note records the public onboarding, support, release, and CI posture for the AoA center.
It is about what the center may honestly claim, not about taking ownership away from sibling repositories.

## Canonical route contract

Public support language follows
[`docs/START_HERE_ROUTE_CONTRACT.md`](../../../docs/START_HERE_ROUTE_CONTRACT.md).

This file is the first surface for the `public-claim-validation` route.

## Shortest onboarding path

For ecosystem understanding, read in this order:

1. `README.md`
2. `CHARTER.md`
3. `ECOSYSTEM_MAP.md`
4. `docs/FEDERATION_RULES.md`

Stop there for a first-pass center view.
Use `docs/LAYERS.md` and `ROADMAP.md` only when you need conceptual detail or declared direction after the overview.

For small-model and low-context entry, use `generated/center_entry_map.min.json` as the compact machine-facing companion to the same route. The route modes are governed by `docs/START_HERE_ROUTE_CONTRACT.md`.
`README.md` remains the public human root, and `CHARTER.md` remains the authority surface.

## Route modes in public posture

| Route mode | Public support use |
|---|---|
| `first-reading` | explains the center without claiming owner-local implementation |
| `root-editing` | protects public root surfaces from becoming a warehouse |
| `direction-change` | separates current direction from released history and future wishes |
| `ownership-routing` | points work to the right owner without transferring truth |
| `mechanic-change` | keeps Agon, Experience, recurrence, growth, quest/RPG, antifragility, and ToS support bounded |
| `public-claim-validation` | checks whether a sentence can be honestly stated by the center |
| `low-context-agent` | gives compact route help while preserving human source docs |
| `district-work` | keeps local technical gates local and subordinate to center law |

## Public support posture

The center may publicly support:

- ecosystem identity and naming
- the current public layer map
- federation rules and source-of-truth boundaries
- compact registry surfaces for the documented public contour
- reviewable routing toward layer-owned repositories

The center does not publicly support:

- layer-owned truth that belongs in `aoa-techniques`, `aoa-skills`, `aoa-evals`, `aoa-stats`, `aoa-memo`, `aoa-agents`, `aoa-playbooks`, or `aoa-kag`
- runtime guarantees that belong in `abyss-stack`
- ToS-authored meaning that belongs in `Tree-of-Sophia`
- typed consumer or control-plane guarantees that belong in `aoa-sdk`

## Release semantics

An `Agents-of-Abyss` public claim is only honest when these stay aligned in the same landed state:

- `CHARTER.md`
- `ECOSYSTEM_MAP.md`
- `docs/FEDERATION_RULES.md`
- `docs/START_HERE_ROUTE_CONTRACT.md`
- `mechanics/agon/LANDING_LOG.md`
- `mechanics/experience/LANDING_LOG.md`
- `generated/center_entry_map.min.json`
- `generated/ecosystem_registry.min.json`
- `generated/federation_supporting_inventory.min.json`

This repository names the federation contour.
It does not version or release the primary meaning of sibling repositories.

## CI tier map

Use the tiers below when you need to verify center claims:

| tier | purpose | surface |
|---|---|---|
| Tier 1 | compact center contract validation | `python scripts/validate_ecosystem.py` |
| Tier 2 | bounded repository regression battery | `python -m pytest -q tests` |
| Tier 3 | source-side scheduled truth check | `.github/workflows/source-side-smoke.yml` |

The machine-facing center capsule has its own bounded rebuild loop:

- `python scripts/repair_known_link_drifts.py --check`
- `python scripts/validate_links.py`
- `python scripts/validate_markdown_shape.py`
- `python scripts/validate_status_vocabulary.py`
- `python scripts/build_link_shape_hygiene_index.py --check`
- `python scripts/validate_link_shape_hygiene_index.py`
- `python scripts/validate_agents_md_shape.py`
- `python scripts/validate_agents_mesh.py`
- `python scripts/build_agents_mesh_index.py --check`
- `python scripts/validate_agents_mesh_index.py`
- `python scripts/validate_entry_surface_sync.py`
- `python scripts/build_center_entry_map.py --check`
- `python scripts/validate_center_entry_map.py`
- `python scripts/validate_mechanics_topology.py`
- `python scripts/validate_mechanic_landing_logs.py`
- `python scripts/validate_generated_freshness.py`
- `python scripts/validate_hygiene_suite.py`
- `python scripts/validate_ecosystem.py`
- `python -m pytest -q tests`

PR and push validation live in `.github/workflows/repo-validation.yml`.

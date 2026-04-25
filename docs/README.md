# Documentation Map

This is the human-first entrypoint for the `docs/` surface of `Agents-of-Abyss`.

Use the root [`README`](../README.md) first when you need the public front door. Use this file when you are already inside the polis and need the doctrine/map district.

If you are editing files under `docs/`, read [`AGENTS.md`](AGENTS.md) in this directory first.

## Start here

For the shortest center overview, read:

1. [`README`](../README.md)
2. [`CHARTER`](../CHARTER.md)
3. [`ECOSYSTEM_MAP`](../ECOSYSTEM_MAP.md)
4. [`FEDERATION_RULES`](FEDERATION_RULES.md)
5. [`ROOT_SURFACE_LAW`](ROOT_SURFACE_LAW.md)
6. [`ROADMAP`](../ROADMAP.md)
7. [`PUBLIC_SUPPORT_POSTURE`](../mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md)

Then use [`MECHANICS`](../mechanics/README.md) as the single branch point for center-level processes: method/growth, recurrence/return/continuity, Agon, Experience, antifragility/subtraction, quest/RPG reflection, ToS bridge, release posture, machine companions, and related stop-lines.

The route modes behind this entry surface are governed by
[`START_HERE_ROUTE_CONTRACT`](START_HERE_ROUTE_CONTRACT.md). Mechanic landing
history lives in [`AGON_LANDING_LOG`](../mechanics/agon/LANDING_LOG.md) and
[`EXPERIENCE_LANDING_LOG`](../mechanics/experience/LANDING_LOG.md).

## Route modes

This docs map mirrors, but does not replace, the canonical route contract.

| Route mode | Use when | Continue through |
|---|---|---|
| `first-reading` | you need the shortest honest center overview | `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/FEDERATION_RULES.md` |
| `root-editing` | a root surface changes | `CONTRIBUTING.md`, `docs/ROOT_SURFACE_LAW.md` |
| `direction-change` | roadmap, phase, maturity, or release contour changes | `ROADMAP.md`, `mechanics/release-support/docs/DIRECTION_SURFACES.md`, `CHANGELOG.md` |
| `ownership-routing` | you need to decide where work belongs | `docs/LAYERS.md`, `docs/REPO_ROLES.md` |
| `mechanic-change` | a process or mechanic changes | `mechanics/README.md`, relevant package README and `LANDING_LOG.md` |
| `public-claim-validation` | public support language or release claims change | `mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md`, generated capsules, validators |
| `low-context-agent` | a compact machine route is needed first | `generated/center_entry_map.min.json` |
| `district-work` | you are already in a technical district | nearest local `README.md` gate |

## How to verify center claims

| Branch | Use | Primary surface |
|---|---|---|
| Authority | Check whether the center may make the claim. | [`CHARTER`](../CHARTER.md) |
| Contour | Check whether the repo, layer, or anchor is currently named. | [`ECOSYSTEM_MAP`](../ECOSYSTEM_MAP.md) |
| Ownership law | Check whether source, derived, routing, runtime, and ToS meaning remain separate. | [`FEDERATION_RULES`](FEDERATION_RULES.md) |
| Root placement | Check whether a file belongs at repository root. | [`ROOT_SURFACE_LAW`](ROOT_SURFACE_LAW.md) |
| Direction | Check whether the claim reflects current program direction. | [`ROADMAP`](../ROADMAP.md), [`DIRECTION_SURFACES`](../mechanics/release-support/docs/DIRECTION_SURFACES.md) |
| Public support | Check whether the claim can be stated publicly and validated. | [`PUBLIC_SUPPORT_POSTURE`](../mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md) |
| Machine contract | Check compact machine-facing capsules. | [`START_HERE_ROUTE_CONTRACT`](START_HERE_ROUTE_CONTRACT.md), [`generated/center_entry_map.min.json`](../generated/center_entry_map.min.json), [`generated/ecosystem_registry.min.json`](../generated/ecosystem_registry.min.json), [`generated/federation_supporting_inventory.min.json`](../generated/federation_supporting_inventory.min.json) |
| Mechanic route | Check process-specific owner splits and stop-lines. | [`MECHANICS`](../mechanics/README.md), [`AGON_LANDING_LOG`](../mechanics/agon/LANDING_LOG.md), [`EXPERIENCE_LANDING_LOG`](../mechanics/experience/LANDING_LOG.md) |
| Audit route | Check cleanup and drift review surfaces. | [`audits/`](audits/), [`ECOSYSTEM_AUDIT_INDEX`](../ECOSYSTEM_AUDIT_INDEX.md) |

Core validation:

```bash
python scripts/validate_markdown_shape.py
python scripts/validate_entry_surface_sync.py
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_mechanics_topology.py
python scripts/validate_mechanic_landing_logs.py
python scripts/validate_ecosystem.py
python -m pytest -q tests
```

## Entry docs

| Surface | Use |
|---|---|
| [`LAYERS`](LAYERS.md) | what each AoA layer is for |
| [`REPO_ROLES`](REPO_ROLES.md) | what each current or emerging repository owns and should not absorb |
| [`FEDERATION_RULES`](FEDERATION_RULES.md) | stable source-of-truth boundaries |
| [`ROOT_SURFACE_LAW`](ROOT_SURFACE_LAW.md) | what may live in repository root and where root leaks should move |
| [`MECHANICS`](../mechanics/README.md) | the branch atlas for processes and engineering philosophy |


## Documentation districts

| District | Use |
|---|---|
| `docs/` root | stable center doctrine and maps that are too deep for repository root but still center-level |
| [`docs/audits/`](audits/) | audit evidence, cleanup candidates, and root-surface review artifacts |
| [`docs/registry/`](registry/) | registry evolution notes and future schema/migration planning |
| [`docs/landings/`](landings/) | historical seed manifests and wave receipts that should not stand in repository root |

## Root-adjacent technical districts

| District | Local gate | Use |
|---|---|---|
| `generated/` | [`generated/README`](../generated/README.md) | compact machine-facing capsules built from source docs |
| `scripts/` | [`scripts/README`](../scripts/README.md) | builders, validators, release checks, and local guardrails |
| `schemas/` | [`schemas/README`](../schemas/README.md) | JSON schema contracts for center-planted surfaces |
| `tests/` | [`tests/README`](../tests/README.md) | regression tests for generated and center-contract surfaces |
| `quests/` | [`quests/README`](../quests/README.md) | tracked obligations, not a second roadmap |
| `manifests/` | [`manifests/README`](../manifests/README.md) | owner-bound manifests and recurrence receipts |
| `config/` | [`config/README`](../config/README.md) | development and validator configuration, not secrets |
| `examples/` | [`examples/README`](../examples/README.md) | public-safe examples, not proof canon |

## Doctrine clusters

Use these clusters for orientation only. Deep branch routing belongs in [`MECHANICS`](../mechanics/README.md), not in this map.

| Cluster | Start here | Use when |
|---|---|---|
| Method and growth | [`METHOD_SPINE`](../mechanics/method-growth/docs/METHOD_SPINE.md), [`REVIEWABLE_GROWTH_REFINERY`](../mechanics/method-growth/docs/REVIEWABLE_GROWTH_REFINERY.md), [`CANDIDATE_LINEAGE_CROSSWALK`](../mechanics/method-growth/docs/CANDIDATE_LINEAGE_CROSSWALK.md), [`OWNER_LANDING_AND_PRUNING`](../mechanics/method-growth/docs/OWNER_LANDING_AND_PRUNING.md) | a repeated pattern needs owner-local landing, proof, memory, method, or pruning |
| Recurrence and continuity | [`RECURRENCE_PRINCIPLE`](../mechanics/recurrence/docs/RECURRENCE_PRINCIPLE.md), [`SELF_AGENCY_CONTINUITY`](../mechanics/recurrence/docs/SELF_AGENCY_CONTINUITY.md), [`COMPONENT_REFRESH_LAW`](../mechanics/recurrence/docs/COMPONENT_REFRESH_LAW.md) | a route lost its axis, needs return, or must preserve bounded duration |
| Agon | [`MECHANICS`](../mechanics/agon/README.md), [`AGON_LANDING_LOG`](../mechanics/agon/LANDING_LOG.md), [`AGON_PREPARATION_POSTURE`](../mechanics/agon/docs/AGON_PREPARATION_POSTURE.md), [`AGON_IMPOSITION_POSTURE`](../mechanics/agon/docs/AGON_IMPOSITION_POSTURE.md), [`AGON_LAWFUL_MOVE_LANGUAGE`](../mechanics/agon/docs/AGON_LAWFUL_MOVE_LANGUAGE.md), [`AGON_MOVE_OWNER_BINDING`](../mechanics/agon/docs/AGON_MOVE_OWNER_BINDING.md) | pressure, lawful move, arena, packet, verdict, retention, rank, school, canon, or owner-binding law is involved |
| Experience | [`MECHANICS`](../mechanics/experience/README.md), [`EXPERIENCE_LANDING_LOG`](../mechanics/experience/LANDING_LOG.md) | a staged experience contract, office/service posture, continuity loom, or runtime boundary is involved |
| Antifragility and subtraction | [`ANTIFRAGILITY`](../mechanics/antifragility/docs/ANTIFRAGILITY.md), [`VIA_NEGATIVA`](../mechanics/antifragility/docs/VIA_NEGATIVA.md), [`ANTI_AUTHORITY_RULES`](../mechanics/antifragility/docs/ANTI_AUTHORITY_RULES.md), [`ONE_IN_ONE_OUT`](../mechanics/antifragility/docs/ONE_IN_ONE_OUT.md) | stress, degraded mode, pruning, or authority inflation must be handled |
| Questbook and RPG | [`QUESTBOOK_MODEL`](../mechanics/questbook/docs/QUESTBOOK_MODEL.md), [`RPG_LAYER_MODEL`](../mechanics/rpg/docs/RPG_LAYER_MODEL.md), [`RPG_ARCHITECTURE_RFC`](../mechanics/rpg/docs/RPG_ARCHITECTURE_RFC.md) | obligations, questlines, progression, or adjunct campaign vocabulary is needed |
| ToS bridge | [`COUNTERPART_BRIDGE`](../mechanics/tos-bridge/docs/COUNTERPART_BRIDGE.md), [`WITNESS_COMPOST`](../mechanics/tos-bridge/docs/WITNESS_COMPOST.md), [`TOS_GROWTH_SUPPORT`](../mechanics/tos-bridge/docs/TOS_GROWTH_SUPPORT.md), [`TOS_TEMPLATE_SUPPORT`](../mechanics/tos-bridge/docs/TOS_TEMPLATE_SUPPORT.md), [`TOS_LINEAGE_PILOT_SUPPORT`](../mechanics/tos-bridge/docs/TOS_LINEAGE_PILOT_SUPPORT.md), [`TOS_SOIL_PREP_SUPPORT`](../mechanics/tos-bridge/docs/TOS_SOIL_PREP_SUPPORT.md) | AoA supports ToS while preserving ToS-authored meaning |
| Release and audit | [`PUBLIC_SUPPORT_POSTURE`](../mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md), [`DIRECTION_SURFACES`](../mechanics/release-support/docs/DIRECTION_SURFACES.md), [`FEDERATION_RELEASE_PROTOCOL`](../mechanics/release-support/docs/FEDERATION_RELEASE_PROTOCOL.md), [`RELEASING`](../mechanics/release-support/docs/RELEASING.md), [`CODEX_AUDIT_PROTOCOL`](CODEX_AUDIT_PROTOCOL.md) | a public claim, release, or audit route needs verification |

## Recommended reading paths

### I need to decide where a change belongs

1. [`REPO_ROLES`](REPO_ROLES.md)
2. [`FEDERATION_RULES`](FEDERATION_RULES.md)
3. [`ROOT_SURFACE_LAW`](ROOT_SURFACE_LAW.md) if the change touches root
4. [`MECHANICS`](../mechanics/README.md) if the change touches a process or mechanic
5. [`CONTRIBUTING`](../CONTRIBUTING.md)

### I need to understand doctrine after the overview

1. [`ROADMAP`](../ROADMAP.md)
2. [`METHOD_SPINE`](../mechanics/method-growth/docs/METHOD_SPINE.md)
3. [`RECURRENCE_PRINCIPLE`](../mechanics/recurrence/docs/RECURRENCE_PRINCIPLE.md)
4. [`SELF_AGENCY_CONTINUITY`](../mechanics/recurrence/docs/SELF_AGENCY_CONTINUITY.md)
5. [`MECHANICS`](../mechanics/README.md)

### I am touching Agon or Experience

1. Read the relevant branch in [`MECHANICS`](../mechanics/README.md).
2. Read the specific surface and its stop-lines.
3. Run the matching validator and test named by that surface.
4. Confirm the change does not grant live authority, runtime activation, memory sovereignty, ToS canon, or owner truth outside the proper owner repository.


### I am cleaning root or duplicate surfaces

1. Read [`ROOT_SURFACE_LAW`](ROOT_SURFACE_LAW.md).
2. Check [`FRAGILITY_BLACKLIST`](../FRAGILITY_BLACKLIST.md).
3. Check [`audits/ROOT_SURFACE_AUDIT_2026_04_24`](audits/ROOT_SURFACE_AUDIT_2026_04_24.md).
4. Move, merge, or delete only with a surviving canonical home.

## Notes

This directory should remain a doctrine-and-map surface, not a shadow corpus. If a document starts becoming technique truth, skill truth, eval truth, memory truth, role truth, playbook truth, KAG truth, runtime truth, or ToS-authored meaning, route it to the owning repository.

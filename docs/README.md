# Documentation Map

This is the human-first entrypoint for the `docs/` surface of `Agents-of-Abyss`.

Use the root [`README`](../README.md) first when you need the public front door. Use this file when you are already inside the polis and need the doctrine/map district.

If you are editing files under `docs/`, read [`AGENTS.md`](AGENTS.md) in this directory first. If you are editing guardrails, continue through [`guardrails/AGENTS.md`](guardrails/AGENTS.md).

## Start here

For the shortest center overview, read:

1. [`README`](../README.md)
2. [`CHARTER`](../CHARTER.md)
3. [`ECOSYSTEM_MAP`](../ECOSYSTEM_MAP.md)
4. [`FEDERATION_RULES`](FEDERATION_RULES.md)
5. [`ROOT_SURFACE_LAW`](ROOT_SURFACE_LAW.md)
6. [`ROADMAP`](../ROADMAP.md)
7. [`PUBLIC_SUPPORT_POSTURE`](../mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md)

Then use [`MECHANICS`](../mechanics/README.md) as the branch point for center-level processes: method/growth, recurrence/return/continuity, checkpoint, Experience, Agon, antifragility, Questbook, RPG, boundary bridge, audit, distillation, growth cycle, and release support.

The route modes behind this entry surface are governed by [`START_HERE_ROUTE_CONTRACT`](START_HERE_ROUTE_CONTRACT.md).

Mechanic landing history lives in mechanic packages, especially [`AGON_LANDING_LOG`](../mechanics/agon/LANDING_LOG.md) and [`EXPERIENCE_LANDING_LOG`](../mechanics/experience/LANDING_LOG.md).

Docs cleanup grammar and machine classification live under [`guardrails/`](guardrails/):

- [`THEMATIC_DISTRICT_PROTOCOL`](guardrails/THEMATIC_DISTRICT_PROTOCOL.md)
- [`CURRENT_SURFACE_INDEX`](guardrails/CURRENT_SURFACE_INDEX.md)
- [`thematic_districts.json`](guardrails/thematic_districts.json)
- [`docs_thematic_index`](../generated/docs_thematic_index.min.json)

Link shape, Markdown shape, status vocabulary, generated freshness, and AGENTS mesh coverage are also guardrail-owned:

- [`LINK_AND_SHAPE_HYGIENE_PROTOCOL`](guardrails/LINK_AND_SHAPE_HYGIENE_PROTOCOL.md)
- [`HYGIENE_GUARDRAIL_INDEX`](guardrails/HYGIENE_GUARDRAIL_INDEX.md)
- [`AGENTS_MESH_PROTOCOL`](guardrails/AGENTS_MESH_PROTOCOL.md)
- [`AGENTS_MESH_INDEX`](guardrails/AGENTS_MESH_INDEX.md)

## Route modes

This docs map mirrors, but does not replace, the canonical route contract.

| Route mode | Use when | Continue through |
|---|---|---|
| `first-reading` | you need the shortest honest center overview | `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/FEDERATION_RULES.md` |
| `root-editing` | a root surface changes | `CONTRIBUTING.md`, `docs/ROOT_SURFACE_LAW.md` |
| `direction-change` | roadmap, phase, maturity, transition, or release contour changes | `ROADMAP.md`, `mechanics/release-support/DIRECTION.md`, `mechanics/release-support/docs/DIRECTION_SURFACES.md`, `CHANGELOG.md` |
| `ownership-routing` | you need to decide where work belongs | `docs/LAYERS.md`, `docs/REPO_ROLES.md` |
| `mechanic-change` | a process or mechanic changes | `mechanics/README.md`, relevant package README and `LANDING_LOG.md` |
| `public-claim-validation` | public support language or release claims change | `mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md`, generated capsules, validators |
| `low-context-agent` | a compact machine route is needed first | `generated/center_entry_map.min.json` |
| `district-work` | you are already in a technical district | nearest local `README.md` and `AGENTS.md` gates |

## How to verify center claims

| Branch | Use | Primary surface |
|---|---|---|
| Authority | Check whether the center may make the claim. | [`CHARTER`](../CHARTER.md) |
| Contour | Check whether the repo, layer, or anchor is currently named. | [`ECOSYSTEM_MAP`](../ECOSYSTEM_MAP.md) |
| Ownership law | Check whether source, derived, routing, runtime, and ToS meaning remain separate. | [`FEDERATION_RULES`](FEDERATION_RULES.md) |
| Root placement | Check whether a file belongs at repository root or docs root. | [`ROOT_SURFACE_LAW`](ROOT_SURFACE_LAW.md) |
| Guardrail shape | Check cleanup, hygiene, generated freshness, and AGENTS mesh law. | [`guardrails/`](guardrails/) |
| Direction | Check whether the claim reflects current program direction. | [`ROADMAP`](../ROADMAP.md), [`DIRECTION_SURFACES`](../mechanics/release-support/docs/DIRECTION_SURFACES.md) |
| Release support | Check whether a landing, handoff, public claim, or GitHub release is a supportable transition. | [`release-support`](../mechanics/release-support/README.md), [`PARTS`](../mechanics/release-support/PARTS.md) |
| Public support | Check whether the claim can be stated publicly and validated. | [`PUBLIC_SUPPORT_POSTURE`](../mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md) |
| Machine contract | Check compact machine-facing capsules. | [`START_HERE_ROUTE_CONTRACT`](START_HERE_ROUTE_CONTRACT.md), [`generated/center_entry_map.min.json`](../generated/center_entry_map.min.json), [`generated/ecosystem_registry.min.json`](../generated/ecosystem_registry.min.json), [`generated/federation_supporting_inventory.min.json`](../generated/federation_supporting_inventory.min.json) |
| Mechanic route | Check process-specific owner splits and stop-lines. | [`MECHANICS`](../mechanics/README.md), relevant package `README.md`, `PARTS.md`, `LANDING_LOG.md`, and `PROVENANCE.md` |
| Audit route | Check cleanup, drift review, evidence posture, and finding routes. | [`audit`](../mechanics/audit/README.md), [`ECOSYSTEM_AUDIT_INDEX`](../ECOSYSTEM_AUDIT_INDEX.md) |

## Validation

Validation commands live in [`AGENTS.md#validation`](AGENTS.md#validation) and the nearest district `AGENTS.md`. This README deliberately stays a map.

For guardrail-specific changes, use [`guardrails/AGENTS.md`](guardrails/AGENTS.md).

For mechanic-specific changes, use [`../mechanics/AGENTS.md`](../mechanics/AGENTS.md) and the owning mechanic `AGENTS.md`.

## Entry docs

| Surface | Use |
|---|---|
| [`LAYERS`](LAYERS.md) | what each AoA layer is for |
| [`REPO_ROLES`](REPO_ROLES.md) | what each current or emerging repository owns and should not absorb |
| [`FEDERATION_RULES`](FEDERATION_RULES.md) | stable source-of-truth boundaries |
| [`ROOT_SURFACE_LAW`](ROOT_SURFACE_LAW.md) | what may live in repository root or docs root and where leaks should move |
| [`START_HERE_ROUTE_CONTRACT`](START_HERE_ROUTE_CONTRACT.md) | public entry route modes |
| [`MECHANICS`](../mechanics/README.md) | branch atlas for processes and engineering philosophy |

## Documentation districts

| District | Use |
|---|---|
| `docs/` root | stable center doctrine and maps that are too deep for repository root but still center-level |
| [`docs/guardrails/`](guardrails/) | docs cleanup, link/shape hygiene, generated freshness, and AGENTS mesh guardrails |
| [`docs/registry/`](registry/) | registry evolution notes and future schema/migration planning |
| [`docs/decisions/`](decisions/) | decision records explaining why a route or placement was chosen |
| [`docs/traces/`](traces/) | migration evidence, move manifests, link-rewrite traces, and provenance logs |

Audit evidence now belongs under [`mechanics/audit/`](../mechanics/audit/). Mechanic history and active mechanic law belong under [`mechanics/`](../mechanics/), not under empty `docs/<mechanic>/` doors.

## Root-adjacent technical districts

| District | Local gate | Use |
|---|---|---|
| `generated/` | [`generated/README`](../generated/README.md) | compact machine-facing capsules built from source docs |
| `scripts/` | [`scripts/README`](../scripts/README.md) | builders, validators, release checks, and local guardrails |
| `schemas/` | [`schemas/README`](../schemas/README.md) | JSON schema contracts for center-planted surfaces |
| `tests/` | [`tests/README`](../tests/README.md) | regression tests for generated and center-contract surfaces |
| `quests/` | [`quests/README`](../quests/README.md) | lane-first lifecycle item store for tracked obligations, not a second roadmap |
| `manifests/` | [`manifests/README`](../manifests/README.md) | owner-bound manifests and recurrence receipts |
| `config/` | [`config/README`](../config/README.md) | development and validator configuration, not secrets |
| `examples/` | [`examples/README`](../examples/README.md) | public-safe examples, not proof canon |

## Doctrine clusters

Use these clusters for orientation only. Deep branch routing belongs in [`MECHANICS`](../mechanics/README.md), not in this map.

| Cluster | Start here | Use when |
|---|---|---|
| Method and growth | [`method-growth`](../mechanics/method-growth/README.md) | repeated pattern, owner-local landing, proof, memory, method, or pruning |
| Recurrence and continuity | [`recurrence`](../mechanics/recurrence/README.md) | return, continuity, re-entry, or bounded duration matters |
| Checkpoint | [`checkpoint`](../mechanics/checkpoint/README.md) | an intermediate state, hook, skill, process, or owner checkpoint needs reviewable capture |
| Agon | [`agon`](../mechanics/agon/README.md) | pressure, lawful move, arena, packet, verdict, retention, rank, school, canon, or owner-binding law is involved |
| Experience | [`experience`](../mechanics/experience/README.md) | staged experience contracts, office/service posture, continuity loom, or runtime boundary is involved |
| Antifragility and subtraction | [`antifragility`](../mechanics/antifragility/README.md) | stress, degraded mode, pruning, or authority inflation must be handled |
| Questbook and RPG | [`questbook`](../mechanics/questbook/README.md), [`rpg`](../mechanics/rpg/README.md) | obligations, questlines, progression, or adjunct campaign vocabulary is needed |
| Boundary bridge | [`boundary-bridge`](../mechanics/boundary-bridge/README.md) | AoA supports cross-owner work while preserving source-owned meaning and owner-local authority |
| Distillation and growth cycle | [`distillation`](../mechanics/distillation/README.md), [`growth-cycle`](../mechanics/growth-cycle/README.md) | raw material must become active form, or harvest/diagnosis/repair/progression must stay reusable |
| Audit | [`audit`](../mechanics/audit/README.md) | evidence, risk, finding, validation, cleanup, or owner-route visibility is needed |
| Release support | [`release-support`](../mechanics/release-support/README.md) | a transition, public claim, release, or audit route needs verification |

## Recommended reading paths

### I need to decide where a change belongs

1. [`REPO_ROLES`](REPO_ROLES.md)
2. [`FEDERATION_RULES`](FEDERATION_RULES.md)
3. [`ROOT_SURFACE_LAW`](ROOT_SURFACE_LAW.md) if the change touches root or docs root
4. [`MECHANICS`](../mechanics/README.md) if the change touches a process or mechanic
5. [`CONTRIBUTING`](../CONTRIBUTING.md)

### I need to understand doctrine after the overview

1. [`ROADMAP`](../ROADMAP.md)
2. [`method-growth`](../mechanics/method-growth/README.md)
3. [`recurrence`](../mechanics/recurrence/README.md)
4. [`MECHANICS`](../mechanics/README.md)

### I am touching a mechanic

1. Read the relevant branch in [`MECHANICS`](../mechanics/README.md).
2. Read the package `AGENTS.md`, `README.md`, `DIRECTION.md`, `PARTS.md`, and `PROVENANCE.md` when present.
3. Run the matching validator and tests named by the owning mechanic `AGENTS.md`.
4. Confirm the change does not grant live authority, runtime activation, memory sovereignty, ToS canon, or owner truth outside the proper owner repository.

### I am cleaning root or duplicate surfaces

1. Read [`ROOT_SURFACE_LAW`](ROOT_SURFACE_LAW.md).
2. Read [`THEMATIC_DISTRICT_PROTOCOL`](guardrails/THEMATIC_DISTRICT_PROTOCOL.md).
3. Check [`CURRENT_SURFACE_INDEX`](guardrails/CURRENT_SURFACE_INDEX.md).
4. Check [`FRAGILITY_BLACKLIST`](../FRAGILITY_BLACKLIST.md).
5. Check [`audit provenance`](../mechanics/audit/PROVENANCE.md) if old root-surface review evidence matters.
6. Move, merge, or delete only with a surviving canonical home.

## Notes

This directory should remain a doctrine-and-map surface, not a shadow corpus. If a document starts becoming technique truth, skill truth, eval truth, memory truth, role truth, playbook truth, KAG truth, runtime truth, mechanic truth, or ToS-authored meaning, route it to the owning repository or mechanic package.

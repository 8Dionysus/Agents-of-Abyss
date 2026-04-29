# Documentation Map

This is the human-first entrypoint for the `docs/` surface of `Agents-of-Abyss`.

Use the root [`README`](../README.md) for the public front door. Use this file when you are already inside the center and need the doctrine, route-law, and map district.

If you are editing files under `docs/`, read [`AGENTS.md`](AGENTS.md) first. Validation commands live in [`AGENTS.md#validation`](AGENTS.md#validation) and the nearest district `AGENTS.md`; this README stays a map.

## Start Here

For the shortest center overview, read:

1. [`README`](../README.md)
2. [`CHARTER`](../CHARTER.md)
3. [`ECOSYSTEM_MAP`](../ECOSYSTEM_MAP.md)
4. [`FEDERATION_RULES`](FEDERATION_RULES.md)
5. [`ROOT_SURFACE_LAW`](ROOT_SURFACE_LAW.md)
6. [`ROADMAP`](../ROADMAP.md)
7. [`PUBLIC_SUPPORT_POSTURE`](../mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md)

Entry route modes are governed by [`START_HERE_ROUTE_CONTRACT`](START_HERE_ROUTE_CONTRACT.md): `first-reading`, `root-editing`, `direction-change`, `ownership-routing`, `mechanic-change`, `public-claim-validation`, `low-context-agent`, and `district-work`. Compact machine entry lives in [`generated/center_entry_map.min.json`](../generated/center_entry_map.min.json).

## Root Docs

| Surface | Owns |
|---|---|
| [`AGENTS`](AGENTS.md) | local editing law for `docs/` |
| [`FEDERATION_RULES`](FEDERATION_RULES.md) | source-of-truth boundaries across the federation |
| [`LAYERS`](LAYERS.md) | conceptual layer ownership |
| [`REPO_ROLES`](REPO_ROLES.md) | compact repository routing |
| [`ROOT_SURFACE_LAW`](ROOT_SURFACE_LAW.md) | root and docs-root placement law |
| [`START_HERE_ROUTE_CONTRACT`](START_HERE_ROUTE_CONTRACT.md) | public entry route modes |
| [`MECHANICS`](MECHANICS.md) | compatibility route to [`mechanics/README`](../mechanics/README.md) |

## Districts

| District | Use |
|---|---|
| [`guardrails/`](guardrails/) | docs cleanup, link/shape hygiene, generated freshness, and AGENTS mesh guardrails |
| [`decisions/`](decisions/) | decision records explaining why a durable route or placement was chosen |
| [`traces/`](traces/) | repo-level movement receipts, apply manifests, link-repair traces, and migration conflicts |

Guardrail source maps:

- [`THEMATIC_DISTRICT_PROTOCOL`](guardrails/THEMATIC_DISTRICT_PROTOCOL.md)
- [`CURRENT_SURFACE_INDEX`](guardrails/CURRENT_SURFACE_INDEX.md)
- [`thematic_districts.json`](guardrails/thematic_districts.json)
- [`docs_thematic_index`](../generated/docs_thematic_index.min.json)

Guardrail operating surfaces:

- [`LINK_AND_SHAPE_HYGIENE_PROTOCOL`](guardrails/LINK_AND_SHAPE_HYGIENE_PROTOCOL.md)
- [`HYGIENE_GUARDRAIL_INDEX`](guardrails/HYGIENE_GUARDRAIL_INDEX.md)
- [`AGENTS_MESH_PROTOCOL`](guardrails/AGENTS_MESH_PROTOCOL.md)
- [`AGENTS_MESH_INDEX`](guardrails/AGENTS_MESH_INDEX.md)

## Adjacent Routes

| Route | Use |
|---|---|
| [`mechanics/README`](../mechanics/README.md) | center mechanics atlas for method-growth, recurrence, checkpoint, Experience, Agon, antifragility, Questbook, RPG, boundary bridge, audit, distillation, growth cycle, and release support |
| mechanic package `README`, `DIRECTION`, `PARTS`, `LANDING_LOG`, `PROVENANCE`, `OWNER_REQUESTS` | active mechanic law, direction, part map, landing history, provenance, and owner requests |
| [`generated/`](../generated/) | compact machine-facing capsules built from source docs |
| [`scripts/`](../scripts/) | builders, validators, release checks, and local guardrails |
| [`schemas/`](../schemas/) | JSON schema contracts for center-planted surfaces |
| [`tests/`](../tests/) | regression tests for generated and center-contract surfaces |
| [`quests/`](../quests/) | lane-first lifecycle item store for tracked obligations |
| [`manifests/`](../manifests/) | owner-bound manifests and recurrence receipts |
| [`config/`](../config/) | development and validator configuration |
| [`examples/`](../examples/) | public-safe examples |

## Claim Routes

| Question | Route |
|---|---|
| Where does this change belong? | [`REPO_ROLES`](REPO_ROLES.md), [`FEDERATION_RULES`](FEDERATION_RULES.md), then [`mechanics/README`](../mechanics/README.md) when process language appears |
| Which layer owns the meaning? | [`LAYERS`](LAYERS.md), [`REPO_ROLES`](REPO_ROLES.md) |
| Which mechanic owns the process? | [`mechanics/README`](../mechanics/README.md), [`mechanics/registry.json`](../mechanics/registry.json), [`generated/mechanic_card_index.min.json`](../generated/mechanic_card_index.min.json) |
| Does public wording have release support? | [`release-support`](../mechanics/release-support/README.md), [`PUBLIC_SUPPORT_POSTURE`](../mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md) |
| Does old material need distillation or audit routing? | [`audit`](../mechanics/audit/README.md), [`distillation`](../mechanics/distillation/README.md), relevant `PROVENANCE.md` |

## Change Routes

| Change | First route |
|---|---|
| Root or docs placement | [`ROOT_SURFACE_LAW`](ROOT_SURFACE_LAW.md), [`THEMATIC_DISTRICT_PROTOCOL`](guardrails/THEMATIC_DISTRICT_PROTOCOL.md), [`CURRENT_SURFACE_INDEX`](guardrails/CURRENT_SURFACE_INDEX.md) |
| Guardrail behavior | [`guardrails/AGENTS`](guardrails/AGENTS.md), then the affected guardrail source |
| Decision rationale | [`decisions/AGENTS`](decisions/AGENTS.md), [`decisions/README`](decisions/README.md) |
| Movement receipt | [`traces/AGENTS`](traces/AGENTS.md), [`traces/README`](traces/README.md) |
| Mechanic law or package route | [`mechanics/AGENTS`](../mechanics/AGENTS.md), then the owning package `AGENTS.md` |
| Generated capsule contract | source doc, builder, schema, generated capsule, validator, and test together |

## Placement Signal

Use `docs/` root for current center doctrine and route maps. Use a named
district for guardrail law, decisions, and traces. Use `mechanics/<slug>/` for
mechanic law, parts, landing history, provenance, owner requests, and legacy
raw sources. Use sibling repositories for owner-local technique, skill, proof,
memory, routing, role, playbook, KAG, stats, runtime, and ToS-authored meaning.

## Notes

This directory is a doctrine-and-map surface. Current center law stays here; mechanic truth lives in `mechanics/`; evidence districts keep decisions, traces, and guardrails discoverable in their own lanes.

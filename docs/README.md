# Documentation Map

This is the human-first entrypoint for the `docs/` surface of `Agents-of-Abyss`.

Use it when you need the center's doctrine and map surfaces. Use the root [`README`](../README.md) first when you need the public front door. If you are editing files under `docs/`, read [`AGENTS.md`](AGENTS.md) in this directory first.

## Start here

For the shortest center overview, read:

1. [`README`](../README.md)
2. [`CHARTER`](../CHARTER.md)
3. [`ECOSYSTEM_MAP`](../ECOSYSTEM_MAP.md)
4. [`LAYERS`](LAYERS.md) and [`REPO_ROLES`](REPO_ROLES.md)
5. [`FEDERATION_RULES`](FEDERATION_RULES.md)
6. [`ROADMAP`](../ROADMAP.md)
7. [`PUBLIC_SUPPORT_POSTURE`](PUBLIC_SUPPORT_POSTURE.md)

Then use [`MECHANICS`](MECHANICS.md) as the single branch point for center-level processes: Agon, Experience, recurrence/return, growth refinery, antifragility, quest/RPG reflection, ToS support, release posture, and related stop-lines.

## How to verify center claims

1. [`CHARTER`](../CHARTER.md) for center authority.
2. [`ECOSYSTEM_MAP`](../ECOSYSTEM_MAP.md) for the public contour.
3. [`FEDERATION_RULES`](FEDERATION_RULES.md) for ownership discipline.
4. [`ROADMAP`](../ROADMAP.md) and [`DIRECTION_SURFACES`](DIRECTION_SURFACES.md) for current direction.
5. [`PUBLIC_SUPPORT_POSTURE`](PUBLIC_SUPPORT_POSTURE.md) for claim and CI posture.
6. [`generated/center_entry_map.min.json`](../generated/center_entry_map.min.json), [`generated/ecosystem_registry.min.json`](../generated/ecosystem_registry.min.json), and [`generated/federation_supporting_inventory.min.json`](../generated/federation_supporting_inventory.min.json) for compact machine-facing capsules.

Core validation:

```bash
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_ecosystem.py
python -m pytest -q tests
```

## Entry docs

- [`LAYERS`](LAYERS.md) - what each AoA layer is for.
- [`REPO_ROLES`](REPO_ROLES.md) - what each current or emerging repository owns and should not absorb.
- [`FEDERATION_RULES`](FEDERATION_RULES.md) - stable source-of-truth boundaries.
- [`MECHANICS`](MECHANICS.md) - the branch atlas for processes and engineering philosophy.

## Doctrine branches

| Branch | Start here | Use when |
|---|---|---|
| Method and growth | [`METHOD_SPINE`](METHOD_SPINE.md), [`REVIEWABLE_GROWTH_REFINERY`](REVIEWABLE_GROWTH_REFINERY.md), [`CANDIDATE_LINEAGE_CROSSWALK`](CANDIDATE_LINEAGE_CROSSWALK.md), [`OWNER_LANDING_AND_PRUNING`](OWNER_LANDING_AND_PRUNING.md) | a repeated pattern needs owner-local landing or pruning. |
| Recurrence and continuity | [`RECURRENCE_PRINCIPLE`](RECURRENCE_PRINCIPLE.md), [`SELF_AGENCY_CONTINUITY`](SELF_AGENCY_CONTINUITY.md), [`COMPONENT_REFRESH_LAW`](COMPONENT_REFRESH_LAW.md) | a route lost its axis, needs return, or must preserve bounded duration. |
| Agon | [`AGON_PREPARATION_POSTURE`](AGON_PREPARATION_POSTURE.md), [`AGON_IMPOSITION_POSTURE`](AGON_IMPOSITION_POSTURE.md), [`AGON_LAWFUL_MOVE_LANGUAGE`](AGON_LAWFUL_MOVE_LANGUAGE.md), [`AGON_MOVE_OWNER_BINDING`](AGON_MOVE_OWNER_BINDING.md) | pressure, lawful move, arena, verdict, retention, rank, canon, or owner-binding law is involved. |
| Experience | [`EXPERIENCE_WAVE1_KERNEL`](EXPERIENCE_WAVE1_KERNEL.md), [`EXPERIENCE_V1_2_TO_V2_0_BRIDGE`](EXPERIENCE_V1_2_TO_V2_0_BRIDGE.md), [`EXPERIENCE_V2_0_LIVING_WORKSPACE_CONTINUITY_RUNTIME`](EXPERIENCE_V2_0_LIVING_WORKSPACE_CONTINUITY_RUNTIME.md) | a staged experience contract or v1.2 -> v2.0 planting wave is involved. |
| Antifragility and subtraction | [`ANTIFRAGILITY`](ANTIFRAGILITY.md), [`VIA_NEGATIVA`](VIA_NEGATIVA.md), [`ANTI_AUTHORITY_RULES`](ANTI_AUTHORITY_RULES.md), [`ONE_IN_ONE_OUT`](ONE_IN_ONE_OUT.md) | stress, degraded mode, pruning, or authority inflation must be handled. |
| Questbook and RPG | [`QUESTBOOK_MODEL`](QUESTBOOK_MODEL.md), [`QUESTBOOK_FIRST_WAVE`](QUESTBOOK_FIRST_WAVE.md), [`RPG_LAYER_MODEL`](RPG_LAYER_MODEL.md) | obligations, questlines, progression, or adjunct campaign vocabulary is needed. |
| ToS bridge | [`COUNTERPART_BRIDGE`](COUNTERPART_BRIDGE.md), [`WITNESS_COMPOST`](WITNESS_COMPOST.md), [`TOS_GROWTH_SUPPORT`](TOS_GROWTH_SUPPORT.md), [`TOS_TEMPLATE_SUPPORT`](TOS_TEMPLATE_SUPPORT.md), [`TOS_LINEAGE_PILOT_SUPPORT`](TOS_LINEAGE_PILOT_SUPPORT.md), [`TOS_SOIL_PREP_SUPPORT`](TOS_SOIL_PREP_SUPPORT.md) | AoA supports ToS while preserving ToS-authored meaning. |
| Release and audit | [`PUBLIC_SUPPORT_POSTURE`](PUBLIC_SUPPORT_POSTURE.md), [`DIRECTION_SURFACES`](DIRECTION_SURFACES.md), [`FEDERATION_RELEASE_PROTOCOL`](FEDERATION_RELEASE_PROTOCOL.md), [`RELEASING`](RELEASING.md), [`CODEX_AUDIT_PROTOCOL`](CODEX_AUDIT_PROTOCOL.md) | a public claim, release, or audit route needs verification. |

## Recommended reading paths

### I need to decide where a change belongs

1. [`REPO_ROLES`](REPO_ROLES.md)
2. [`FEDERATION_RULES`](FEDERATION_RULES.md)
3. [`MECHANICS`](MECHANICS.md)
4. [`CONTRIBUTING`](../CONTRIBUTING.md)

### I need to understand doctrine after the overview

1. [`ROADMAP`](../ROADMAP.md)
2. [`METHOD_SPINE`](METHOD_SPINE.md)
3. [`RECURRENCE_PRINCIPLE`](RECURRENCE_PRINCIPLE.md)
4. [`SELF_AGENCY_CONTINUITY`](SELF_AGENCY_CONTINUITY.md)
5. [`MECHANICS`](MECHANICS.md)

### I am touching Agon or Experience

1. Read the relevant branch in [`MECHANICS`](MECHANICS.md).
2. Read the specific surface and its stop-lines.
3. Run the matching validator and test named by that surface.
4. Confirm the change does not grant live authority, runtime activation, memory sovereignty, ToS canon, or owner truth outside the proper owner repository.

## Notes

This directory should remain a doctrine-and-map surface, not a shadow corpus. If a document starts becoming technique truth, skill truth, eval truth, memory truth, role truth, playbook truth, KAG truth, runtime truth, or ToS-authored meaning, route it to the owning repository.

# Documentation Map

This file is the human-first entrypoint for the `docs/` surface of `Agents-of-Abyss`.

Use it when you want to understand the AoA ecosystem as a whole rather than one specialized repository.

If you are editing files under `docs/`, read [`AGENTS.md`](AGENTS.md) in this directory first.

## Start here

For the shortest outsider overview, read in this order:

1. [README](../README.md)
2. [CHARTER](../CHARTER.md)
3. [ECOSYSTEM_MAP](../ECOSYSTEM_MAP.md)
4. [FEDERATION_RULES](FEDERATION_RULES.md)
5. [ROADMAP](../ROADMAP.md)
6. [PUBLIC_SUPPORT_POSTURE](PUBLIC_SUPPORT_POSTURE.md)

Use [LAYERS](LAYERS.md) and [REPO_ROLES](REPO_ROLES.md) after that when you need conceptual or routing detail rather than the first-pass center view.

## How to verify center claims

1. [CHARTER](../CHARTER.md)
2. [ECOSYSTEM_MAP](../ECOSYSTEM_MAP.md)
3. [FEDERATION_RULES](FEDERATION_RULES.md)
4. [ROADMAP](../ROADMAP.md)
5. [generated/ecosystem_registry.min.json](../generated/ecosystem_registry.min.json), `python scripts/validate_ecosystem.py`, and `python -m pytest -q tests`

## Entry docs

- [LAYERS](LAYERS.md) — what each AoA layer is for
- [REPO_ROLES](REPO_ROLES.md) — what each current or emerging repository owns and should not absorb
- [FEDERATION_RULES](FEDERATION_RULES.md) — the stable ownership boundaries across the AoA federation

## Doctrine docs

- [ANTIFRAGILITY](ANTIFRAGILITY.md) and [ANTIFRAGILITY_FIRST_WAVE](ANTIFRAGILITY_FIRST_WAVE.md) — the center doctrine and bounded first-wave scope for source-owned stress, degraded continuation, proof, and derived-vector posture
- [VIA_NEGATIVA](VIA_NEGATIVA.md), [ANTI_AUTHORITY_RULES](ANTI_AUTHORITY_RULES.md), and [ONE_IN_ONE_OUT](ONE_IN_ONE_OUT.md) — the center subtraction posture, anti-authority rails, and sprawl pressure rule for post-wave pruning
- [ROOTLINE](ROOTLINE.md) — the current trunk-first coordination spine for AoA x ToS planting
- [RECURRENCE_PRINCIPLE](RECURRENCE_PRINCIPLE.md) — the standing recovery law for long-horizon routes across the federation
- [METHOD_SPINE](METHOD_SPINE.md) — the center-level doctrine for method placement and maturity language
- [REVIEWABLE_GROWTH_REFINERY](REVIEWABLE_GROWTH_REFINERY.md), [CANDIDATE_LINEAGE_CROSSWALK](CANDIDATE_LINEAGE_CROSSWALK.md), and [OWNER_LANDING_AND_PRUNING](OWNER_LANDING_AND_PRUNING.md) — the center-level route, stage-ownership crosswalk, and post-candidate landing/pruning doctrine
- [SELF_AGENCY_CONTINUITY](SELF_AGENCY_CONTINUITY.md) — the center-level law for bounded long-arc continuity with explicit anchors and governed reanchor
- [COMPONENT_REFRESH_LAW](COMPONENT_REFRESH_LAW.md) — the center-level law for owner-owned refresh of drifting internal technical surfaces
- [COUNTERPART_BRIDGE](COUNTERPART_BRIDGE.md) — the boundary doctrine for AoA x ToS counterpart work and KAG restraint
- [WITNESS_COMPOST](WITNESS_COMPOST.md) — the paired public-contract doctrine for witness and compost
- [TOS_GROWTH_SUPPORT](TOS_GROWTH_SUPPORT.md), [TOS_TEMPLATE_SUPPORT](TOS_TEMPLATE_SUPPORT.md), [TOS_LINEAGE_PILOT_SUPPORT](TOS_LINEAGE_PILOT_SUPPORT.md), [TOS_SOIL_PREP_SUPPORT](TOS_SOIL_PREP_SUPPORT.md) — narrow AoA support doctrine for ToS-owned work

## Support and maintenance docs

- [AGENTS.md](AGENTS.md) — local editing and maintenance instructions for the `docs/` surface
- [PUBLIC_SUPPORT_POSTURE](PUBLIC_SUPPORT_POSTURE.md) — the public onboarding, support, release, and CI posture for the AoA center
- [FEDERATION_RELEASE_PROTOCOL](FEDERATION_RELEASE_PROTOCOL.md) — the shared cadence and release completeness contract for public owner repos
- [RELEASING](RELEASING.md) — the center-owned release runbook and audit path
- [postmortem: 2026-04-10 federation release rollout](postmortems/2026-04-10-federation-release-rollout-retrospective.md) — the no-blame retrospective behind the new release contract
- [ADR: federation release contract](decisions/2026-04-10-federation-release-contract.md) — why the new federation release path exists
- [decision note: growth refinery lineage route](decisions/2026-04-11-growth-refinery-lineage-route.md) — why AoA now names one narrow reviewable route across checkpoint carry, reviewed candidate identity, seed staging, and owner landing without creating a new sovereign layer
- [decision note: aoa-stats public layer](decisions/2026-04-09-aoa-stats-public-layer.md) — why `aoa-stats` now belongs inside the documented public federation contour rather than only the supporting inventory
- [QUESTBOOK_MODEL](QUESTBOOK_MODEL.md) and [QUESTBOOK_FIRST_WAVE](QUESTBOOK_FIRST_WAVE.md) — the current center questbook contour and first-wave guardrails
- [RPG layer and bridge docs](RPG_LAYER_MODEL.md) plus the related `RPG_*` documents — adjunct reflection-contour support docs, not the main center entry path

## Recommended reading paths

### I need to decide where a change belongs

1. [REPO_ROLES](REPO_ROLES.md)
2. [FEDERATION_RULES](FEDERATION_RULES.md)
3. [CONTRIBUTING](../CONTRIBUTING.md)

### I need to understand doctrine after the overview

1. [ROADMAP](../ROADMAP.md)
2. [METHOD_SPINE](METHOD_SPINE.md)
3. [SELF_AGENCY_CONTINUITY](SELF_AGENCY_CONTINUITY.md)
4. [COMPONENT_REFRESH_LAW](COMPONENT_REFRESH_LAW.md)
5. [COUNTERPART_BRIDGE](COUNTERPART_BRIDGE.md)

## Notes

This repository should remain compact.
If a document starts trying to become a specialized corpus, it probably belongs in a neighboring AoA repository instead.

# Direction Surfaces

This note names the current direction surface for each public AoA / ToS repository.

It exists so cross-repo alignment work can distinguish between:

- repositories whose direction canon is a `ROADMAP.md`
- repositories whose direction lives in another repo-owned surface
- the narrow cases where a non-roadmap surface remains the more honest entry door

It is a direction map, not a release log. When a direction surface changes
because a transition landed, use
[`../parts/direction-surface-review/README.md`](../parts/direction-surface-review/README.md)
to decide which entry surfaces must move.

## Rules

- Treat the listed direction surface as the first repo-owned statement of current course.
- Keep `README.md` and docs-entry maps short and link-driven toward that surface.
- Prefer a root `ROADMAP.md` for mature owner repos when it can summarize current phase without replacing stronger repo-local truth.
- Keep profile-only route maps on narrower non-roadmap posture docs when a roadmap would imply false center authority.
- When an entry doc names a direction surface, avoid stale counts or duplicated phase snapshots there.

## Current map

| repository | direction surface | why this is the right source |
|---|---|---|
| `Agents-of-Abyss` | `ROADMAP.md` | constitutional and program-level direction lives at the center |
| `aoa-techniques` | `docs/START_HERE.md` and `ROADMAP.md` | the repo routes current public canon through its start surface and keeps hardening or evidence waves in the root roadmap |
| `aoa-skills` | `ROADMAP.md` | canonical public roadmap for skill-layer evolution |
| `aoa-evals` | `ROADMAP.md` | canonical proof-layer roadmap |
| `aoa-memo` | `ROADMAP.md` | canonical memory-layer direction surface |
| `aoa-agents` | `ROADMAP.md` | canonical role-contract and handoff direction surface |
| `aoa-playbooks` | `ROADMAP.md` | canonical scenario-layer direction surface |
| `aoa-routing` | `ROADMAP.md` | canonical routing-layer direction surface |
| `aoa-stats` | `ROADMAP.md` | the derived layer now keeps one root-level current-direction door while still routing shipped summary families through `README.md#current-v0-surface` and `docs/README.md` |
| `aoa-kag` | `ROADMAP.md` | canonical derived-knowledge direction surface |
| `aoa-sdk` | `ROADMAP.md` | the control-plane repo now keeps one root-level current-direction door while leaving `docs/blueprint.md` as seed history and `README.md` plus repo docs as current-state gates |
| `Tree-of-Sophia` | `ROADMAP.md` | canonical knowledge-architecture direction surface |
| `Dionysus` | `ROADMAP.md` | the seed garden now keeps one root-level direction door that explicitly stays weaker than manifests, closure notes, `seed-registry.yaml`, and owner-repo reality |
| `8Dionysus` | `docs/PUBLIC_ENTRY_POSTURE.md` | this is a profile and route-map repo, so a standalone roadmap would be a misleading center-claim |
| `abyss-stack` | `~/src/abyss-stack/ROADMAP.md` | runtime and infrastructure direction belongs to the source checkout, not the deployed `/srv/AbyssOS/abyss-stack` mirror |

## Notes

- This note routes readers to owner truth. It does not replace repo-local validators, release checks, or generated entry capsules.
- If a repository changes direction surface later, update its own entry docs first and then refresh this center map.
- Do not use this map to claim that a sibling repository accepted a release or
  landing; cite the owner repository receipt instead.

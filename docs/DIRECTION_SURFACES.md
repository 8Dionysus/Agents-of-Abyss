# Direction Surfaces

This note names the current direction surface for each public AoA / ToS repository.

It exists so cross-repo alignment work can distinguish between:

- repositories whose direction canon is a `ROADMAP.md`
- repositories whose direction lives in another repo-owned surface
- profile, seed, or derived layers that should not be forced into roadmap-shaped status docs

## Rules

- Treat the listed direction surface as the first repo-owned statement of current course.
- Keep `README.md` and docs-entry maps short and link-driven toward that surface.
- Do not force profile, seed-garden, or derived repos to invent a `ROADMAP.md` when another surface already owns direction more honestly.
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
| `aoa-stats` | `README.md#current-v0-surface` and `docs/README.md` | the derived layer currently names its active contour through the committed v0 summary surface rather than a separate roadmap |
| `aoa-kag` | `ROADMAP.md` | canonical derived-knowledge direction surface |
| `aoa-sdk` | `docs/blueprint.md`, read with `README.md` as the current-state gate | the blueprint still carries repo direction, while current-state truth stays in the current tree and repo docs |
| `Tree-of-Sophia` | `ROADMAP.md` | canonical knowledge-architecture direction surface |
| `Dionysus` | `seed-registry.yaml`, `seed_expansion/`, and `docs/SEED_SURFACE_MAP.md` | the seed garden is directed by the live registry and staged seed surfaces, not by a standalone roadmap |
| `8Dionysus` | `docs/PUBLIC_ENTRY_POSTURE.md` | this is a profile and route-map repo, so a standalone roadmap would be a misleading center-claim |
| `abyss-stack` | `~/src/abyss-stack/ROADMAP.md` | runtime and infrastructure direction belongs to the source checkout, not the deployed `/srv/abyss-stack` mirror |

## Notes

- This note routes readers to owner truth. It does not replace repo-local validators, release checks, or generated entry capsules.
- If a repository changes direction surface later, update its own entry docs first and then refresh this center map.

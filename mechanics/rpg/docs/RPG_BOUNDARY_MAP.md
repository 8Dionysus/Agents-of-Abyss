# RPG Boundary Map

This note fixes the ownership split for the AoA RPG contour.

## Core law

The repo that already owns meaning keeps owning meaning.

The RPG layer only adds:
- reflection
- runtime aggregation
- presentation

## Boundary table

| Repo | Owns | Does not own | RPG-facing role |
|---|---|---|---|
| `Agents-of-Abyss` | federation-level doctrine, common model, common contracts, cross-repo map | runtime state, frontend state, repo-local authored meaning | common RFC and vocabulary law |
| `aoa-agents` | role contracts, progression overlay, cohort and tier posture | live runtime build state | class and mastery source |
| `aoa-skills` | bounded execution workflows, pack profiles, adapter posture | playbook method, runtime inventory | active ability source |
| `aoa-techniques` | reusable practice canon, validation, adaptation posture | skill execution, runtime loadout | feat / perk source |
| `aoa-evals` | proof canon, verdict posture, progression evidence | reputation runtime storage, UI ranking | XP evidence and caution source |
| `aoa-playbooks` | scenario composition, questlines, campaign lanes, activation projections | persisted run state, frontend session logic | campaign and party-method source |
| `aoa-memo` | witness objects, chronicles, recallable memory, provenance-aware writeback | live working memory runtime, global score | chronicle and timeline source |
| `aoa-routing` | navigation, entry cards, thin quest discovery hints | quest meaning, progression state, live board authority | quest-board and next-hop source hints |
| `abyss-stack` | runtime state, build snapshots, ledgers, run results, projection delivery, service contracts | upstream authored meaning | runtime/frontend owner |
| `aoa-sdk` | typed loaders, adapters, consumer wrappers, orchestration helpers | source doctrine, live service runtime | typed consumer spine |
| `Dionysus` | seed transport, lineage, prep-pack staging | final repo-owned doctrine | seed-garden staging |
| `8Dionysus` | public orientation mirrors later | authority or canonical runtime truth | later public mirror |
| `Tree-of-Sophia` | ToS source meaning and lineage architecture | AoA runtime state | adjacent authority plane, not collapse |
| `aoa-kag` | downstream derived knowledge substrate | authored memory or source texts | later knowledge/readiness projection |

## Hard prohibitions

### `Agents-of-Abyss` MUST NOT

- own live resource bars
- own runtime reputation state
- own frontend session cards
- own run history as live service state

### `abyss-stack` MUST NOT

- redefine quests
- redefine roles
- redefine skill or technique meaning
- override eval verdict doctrine
- replace memo objects with private summary truth

### `aoa-routing` MUST NOT

- become a second quest owner
- become a progression owner
- become a live gameplay engine

### `aoa-playbooks` MUST NOT

- become a persisted execution runtime
- become a build snapshot store
- become a frontend state store

### `Dionysus` MUST NOT

- become the owner of the RFC
- become the owner of runtime/frontend doctrine
- silently collapse AoA and ToS

## Artifact boundary

Artifacts are intentionally weaker than the existing source-owned layers in this pass.

Until a dedicated artifact-owner contour exists:
- `artifact_ids` remain runtime reflections
- artifact meaning MUST cite source refs or runtime cause refs
- artifacts MUST NOT become a secret second canon

## Frontend boundary

The frontend may display:
- themed labels
- bars and badges
- quest cards
- reputation panels
- timelines
- campaign lanes

The frontend may not:
- create new quest meaning
- award itself progression
- hide penalty provenance
- claim authority stronger than the source refs

## Final rule

When there is tension:
1. source meaning wins
2. proof and witness come next
3. runtime state follows
4. frontend theming comes last

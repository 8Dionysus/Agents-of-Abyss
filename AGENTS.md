# AGENTS.md

Root route card for `Agents-of-Abyss`.

## Purpose

`Agents-of-Abyss` is the constitutional and ecosystem-center repository for AoA.
It owns ecosystem identity, layer map, federation rules, program-level direction, and compact center registries.
It does not own every implementation surface.

## Owner lane

This repository owns:

- AoA charter, layer map, federation rules, and center-level roadmaps
- ecosystem registry and compact center surfaces
- doctrine that keeps long-arc direction legible without absorbing specialized layers

It does not own:

- skills, techniques, evals, memory, routing, KAG, playbooks, stats, roles, or runtime implementation truth
- ToS authored meaning
- quest, checkpoint, runtime, or progression state as live implementation

## Start here

Entry routing is governed by `docs/START_HERE_ROUTE_CONTRACT.md`.

1. `CHARTER.md`
2. `ECOSYSTEM_MAP.md`
3. `docs/LAYERS.md`
4. `docs/FEDERATION_RULES.md`
5. `ROADMAP.md`
6. `README.md`
7. For detailed preserved root branches, read `docs/agent-lane/AGENTS_ROOT_REFERENCE.md`.

## Route modes

Use the named route before widening a center claim:

| Route mode | Use when | First surface |
|---|---|---|
| `first-reading` | you need the shortest honest center overview | `README.md` |
| `root-editing` | a root surface changes | `docs/ROOT_SURFACE_LAW.md` |
| `direction-change` | roadmap, phase, maturity, or release contour changes | `ROADMAP.md` |
| `ownership-routing` | ownership is unclear | `docs/REPO_ROLES.md` |
| `mechanic-change` | Agon, Experience, recurrence, growth, antifragility, quest/RPG, or ToS support changes | `mechanics/README.md` |
| `public-claim-validation` | a sentence sounds like a public promise | `mechanics/release-support/docs/PUBLIC_SUPPORT_POSTURE.md` |
| `low-context-agent` | a compact machine route is needed first | `generated/center_entry_map.min.json` |
| `district-work` | work is already inside a technical district | nearest local `README.md` |

## AGENTS stack law

- Start with this root card, then follow the nearest nested `AGENTS.md` for every touched path.
- Root guidance owns repository identity, owner boundaries, route choice, and the shortest honest verification path.
- Nested guidance owns local contracts, local risk, exact files, and local checks.
- Authored source surfaces own meaning. Generated, exported, compact, derived, runtime, and adapter surfaces summarize, transport, or support meaning.
- Self-agency, recurrence, quest, progression, checkpoint, or growth language must stay bounded, reviewable, evidence-linked, and reversible.
- Report what changed, what was verified, what was not verified, and where the next agent should resume.

## Route away when

- source-linked knowledge or interpretation belongs in `Tree-of-Sophia`
- role, progression, or checkpoint posture belongs in `aoa-agents`
- scenario, questline, campaign, raid, or reanchor posture belongs in `aoa-playbooks`
- typed helpers, compatibility, activation, or handoff tooling belongs in `aoa-sdk`
- runtime budgets, service state, storage, or frontend presentation belongs in `abyss-stack`
- skill, technique, eval, memo, routing, KAG, or stats meaning belongs in its owner repo

## Verify

Run the narrowest relevant center check. Default center integrity:

```bash
python scripts/plan_docs_thematic_cleanup.py --check
python scripts/validate_docs_thematic_districts.py
python scripts/validate_docs_migration_map.py
python scripts/build_docs_thematic_index.py --check
python scripts/validate_docs_thematic_index.py
python scripts/validate_markdown_shape.py
python scripts/validate_entry_surface_sync.py
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_mechanics_topology.py
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_mechanic_landing_logs.py
python scripts/validate_ecosystem.py
python -m pytest -q tests
```

If an Agon owner-binding or gate-routing surface changes, also run the matching builder, validator, and targeted tests named in `docs/agent-lane/AGENTS_ROOT_REFERENCE.md`.

## Report

Close with the center surfaces changed, whether owner boundaries shifted, which neighboring repos are affected, and exactly which checks ran or did not run.

## Full reference

`docs/agent-lane/AGENTS_ROOT_REFERENCE.md` preserves the previous detailed root guidance for audits, Agon branches, review guidelines, and specialized validation paths.

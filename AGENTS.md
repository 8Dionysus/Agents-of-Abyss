# AGENTS.md

## Applies to

This root card applies to the whole repository unless a nearer nested `AGENTS.md` narrows the lane.

## Role

This AGENTS card keeps local work inside the Agents-of-Abyss center lane, names the nearest owner boundary, and routes wider claims back to the root card.

## Read before editing

Read the repository root `AGENTS.md`, this card, and the nearest `README.md` or protocol surface before changing files in this lane.

## Boundaries

Do not use this lane to override owner-local truth, generated-source boundaries, sibling-repo authority, or release validation contracts.

## Validation

Run the nearest validator named by this card. For release-facing changes, also run `python scripts/release_check.py`.

## Closeout

Closeout must name changed surfaces, checks run, checks skipped, remaining risk, and the next owner route if this lane was only a waypoint.

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

## Route modes

Use the named route before widening a center claim:

| Route mode | Use when | First surface |
|---|---|---|
| `first-reading` | you need the shortest honest center overview | `README.md` |
| `root-editing` | a root surface changes | `docs/ROOT_SURFACE_LAW.md` |
| `direction-change` | roadmap, phase, maturity, or release contour changes | `ROADMAP.md` |
| `ownership-routing` | ownership is unclear | `docs/REPO_ROLES.md` |
| `mechanic-change` | Agon, Experience, recurrence, growth, antifragility, quest/RPG, release-support, or ToS support changes | `mechanics/README.md` |
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

## Decision review

After structural, ownership, workflow, route-law, validator-authority,
public-contract, or topology changes, check whether future agents will need a
decision record to understand why the path was chosen. Use
`docs/decisions/AGENTS.md` and `docs/decisions/README.md` for the local rule.
If no record is needed, say so in closeout.

## Route away when

- source-linked knowledge or interpretation belongs in `Tree-of-Sophia`
- role, progression, or checkpoint posture belongs in `aoa-agents`
- scenario, questline, campaign, raid, or reanchor posture belongs in `aoa-playbooks`
- typed helpers, compatibility, activation, or handoff tooling belongs in `aoa-sdk`
- runtime budgets, service state, storage, or frontend presentation belongs in `abyss-stack`
- skill, technique, eval, memo, routing, KAG, or stats meaning belongs in its owner repo

## Hard no

- Do not absorb technique, skill, eval, memo, role, playbook, routing, KAG, stats, runtime, or ToS source truth into the center.
- Do not let generated registries, routing tables, compact indexes, or derived reports masquerade as source authority.
- Do not turn the root README, docs root, or CHANGELOG into an archive of every package, wave, or session note.
- Do not hide semantic changes under "docs-only" or "metadata-only" wording.
- Do not harden long-arc direction into implementation claims unless the owning repository or mechanic surface moves with it.
- Do not let quest, RPG, checkpoint, recurrence, progression, or self-agency language imply live runtime state, ledger ownership, or unreviewable autonomy.

## Review-critical drift

Treat these as high-risk findings in this center repository:

- contradictions across `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/LAYERS.md`, `docs/FEDERATION_RULES.md`, `ROADMAP.md`, and source-backed generated capsules
- routing that points readers to the wrong owner repository or mechanic package
- generated or derived surfaces changed without their source docs, builders, validators, or tests
- public promises that are not supported by release-support evidence
- center claims that silently absorb owner-local implementation, proof, runtime, memory, or ToS meaning

## Verify

Run the narrowest relevant center check. Default center integrity:

```bash
python scripts/plan_docs_thematic_cleanup.py --check
python scripts/validate_docs_thematic_districts.py
python scripts/validate_docs_migration_map.py
python scripts/validate_decision_records.py
python scripts/build_docs_thematic_index.py --check
python scripts/validate_docs_thematic_index.py
python scripts/repair_known_link_drifts.py --check
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
python scripts/validate_status_vocabulary.py
python scripts/build_link_shape_hygiene_index.py --check
python scripts/validate_link_shape_hygiene_index.py
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
python scripts/validate_entry_surface_sync.py
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_mechanics_topology.py
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_mechanic_landing_logs.py
python scripts/validate_generated_freshness.py
python scripts/validate_hygiene_suite.py
python scripts/validate_ecosystem.py
python -m pytest -q
```

If an Agon owner-binding or gate-routing surface changes, use
`mechanics/agon/AGENTS.md` and `mechanics/agon/parts/AGENTS.md` for the
matching builder, validator, and targeted tests.

## Report

Close with the center surfaces changed, whether owner boundaries shifted, which neighboring repos are affected, and exactly which checks ran or did not run.

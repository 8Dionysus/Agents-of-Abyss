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

1. `CHARTER.md`
2. `ECOSYSTEM_MAP.md`
3. `docs/LAYERS.md`
4. `docs/FEDERATION_RULES.md`
5. `ROADMAP.md`
6. `README.md`
7. For detailed preserved root branches, read `docs/AGENTS_ROOT_REFERENCE.md`.


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
python -m pip install -r requirements-dev.txt
python scripts/validate_ecosystem.py
python -m pytest -q tests
```

If an Agon owner-binding or gate-routing surface changes, also run the matching builder, validator, and targeted tests named in `docs/AGENTS_ROOT_REFERENCE.md`.

## Report

Close with the center surfaces changed, whether owner boundaries shifted, which neighboring repos are affected, and exactly which checks ran or did not run.

## Full reference

`docs/AGENTS_ROOT_REFERENCE.md` preserves the previous detailed root guidance for audits, Agon branches, review guidelines, and specialized validation paths.

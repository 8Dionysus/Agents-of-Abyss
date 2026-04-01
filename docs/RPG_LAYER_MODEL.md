# RPG Layer Model

## Purpose

This note defines the first adjunct RPG reflection layer for AoA.

It exists to make the growing quest contour legible as a progression and campaign system without mutating the underlying source-owned meanings of quests, roles, proofs, memory, or routing.

## Core rule

The RPG layer is a reflection layer, not a hidden base ontology.

It may:
- map existing AoA surfaces into a game-like orientation
- define adjunct progression, chronicle, and quest-board reflection contracts
- help humans and agents read long-horizon work as campaigns, roles, and mastery paths

It must not:
- replace source-owned quest meaning
- replace role contracts
- replace portable proof surfaces
- replace memory ownership boundaries
- replace routing authority limits
- invent runtime state inside repos that do not own runtime

## Reflection map

- `work_quest_v1` -> mission / quest
- `questline_outline_v1` -> questline / campaign lane
- agent role profile -> class archetype
- model tier -> duty lane
- skill family -> ability school later, not now
- reusable technique -> feat / perk candidate later, not now
- progression evidence -> XP evidence
- quest chronicle -> journal / chronicle
- derived quest-board entry -> quest board card

## Boundary rules

### Source repos remain the owners

The owner repo of a quest, role, eval bundle, playbook, or memory surface remains the owner of its meaning.

### Routing stays thin

`aoa-routing` may render derived quest-board hints later. It does not become the owner of quest meaning or progression state.

### Playbooks stay scenario-shaped

Questlines and campaigns belong in `aoa-playbooks` only as reviewed scenario outlines with anchors, reanchor rules, and harvest posture. They are not runtime ledgers.

### Memo stays witness-shaped

Chronicles belong in `aoa-memo` only as recallable witness surfaces with provenance and temperature posture. They do not become source quest state.

### Dionysus stays seed-shaped

`Dionysus` may stage and transport the contour as a seed pack. It does not become the owner of RPG doctrine.

## Progression rules

- Progression must be multi-axis.
- No single global power score is authoritative.
- Unlocks must be evidence-backed.
- Negative, zero, or cautionary evidence remains valid.
- `deep` readiness remains rare and earned. It is not a default early-game unlock.

## First-wave contents

This first wave lands only:

- common model and first-wave scope docs in `Agents-of-Abyss`
- adjunct agent progression contract in `aoa-agents`
- progression evidence contract in `aoa-evals`
- questline / campaign outline contract in `aoa-playbooks`
- quest chronicle contract in `aoa-memo`
- derived quest-board entry seam in `aoa-routing`
- prep-pack staging note and map in `Dionysus`

## Exclusions

This wave excludes:

- skill-as-ability landings in `aoa-skills`
- technique-as-feat landings in `aoa-techniques`
- runtime persistence, UI, and services in `abyss-stack`
- public mirror work in `8Dionysus`
- decorative combat or economy systems

## Final rule

The first honest RPG layer in AoA should feel like a clearer reading of the existing federation, not like a costume thrown over it.

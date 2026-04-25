# RPG Bridge Wave

## Purpose

This note defines the next bridge contour for the AoA RPG layer.

The first wave planted progression, chronicles, questlines, and a quest-board seam.
The second wave planted abilities and feats.
The architecture RFC fixed vocabulary and runtime/frontend law.

What remained was the bridge that lets proof, composition, and navigation speak to one another without collapsing repo ownership.

## Three bridge objects

### 1. Unlock proof

`aoa-evals` owns bounded proof that a build, route, or party is ready for a specific unlock posture.

### 2. Party template

`aoa-playbooks` owns scenario-shaped party composition and build synergy outlines.

### 3. RPG navigation card

`aoa-routing` owns derived orientation cards that help a reader move from quest to proof to party template and back to source authority.

## Canonical flow

```text
source quest / playbook / progression evidence
  -> unlock proof
  -> party template
  -> routing navigation card
  -> later runtime/frontend projections
```

Each step stays weaker than the layer upstream of it.

## Boundary law

- `aoa-evals` may justify or gate unlocks. It does not own quest acceptance or runtime equip state.
- `aoa-playbooks` may describe party and build posture. It does not own live session state or reward logic.
- `aoa-routing` may orient. It does not own proof, party doctrine, or quest meaning.

## Recommended use

Use this bridge wave when:
- a route has enough proof to justify a new ability, feat, ceiling, or party lane
- a recurring scenario needs named party slots and build posture
- a reader needs one compact card that points back to source authority without scraping the whole stack raw

## Anti-collapse rules

- do not create a universal rank or power score here
- do not let routing infer reward, completion, or hidden priority semantics
- do not let playbooks become a runtime inventory system
- do not let unlock proof overrule source quest state
- do not let this bridge silently collapse AoA and ToS

## Final rule

This wave is a bridge, not a throne.

It should make the system more legible, more transparent, and more front-end ready without stealing ownership from the repos that already hold the meaning.

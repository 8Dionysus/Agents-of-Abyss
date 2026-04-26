# RPG First Wave

## Role

This document defines the first bounded rollout for the AoA RPG reflection layer.

It is a first-wave contour, not a claim that the whole RPG layer is already mature.

## Goal

Prove that AoA can support a game-shaped reflection layer without:

- mutating quest canon
- mutating role canon
- collapsing proof into score worship
- collapsing memory into authority
- collapsing routing into a second source of truth
- widening into runtime mechanics too early

## Included in this wave

### `Agents-of-Abyss`
Owns:
- the common RPG reflection model
- the first-wave scope note
- federation-level boundary wording

### `aoa-agents`
Owns:
- agent progression contract
- mastery axes
- rank posture
- unlock posture

### `aoa-evals`
Owns:
- progression evidence
- advancement verdict posture
- axis deltas and caution semantics

### `aoa-playbooks`
Owns:
- questline and campaign outline shape
- raid as explicit rare coordinated route
- reanchor and harvest alignment

### `aoa-memo`
Owns:
- quest chronicle writeback
- recall posture for campaign witness
- archivist-facing chronicle handoff

### `aoa-routing`
Owns:
- derived quest-board entry seam
- example-only board rendering posture
- source-consumption limits

### `Dionysus`
Owns:
- seed-garden prep-pack staging
- transport and lineage reflection
- no doctrinal takeover

## Excluded for now

Deferred, not rejected:

- `aoa-skills`
- `aoa-techniques`
- `abyss-stack`
- `8Dionysus`
- `aoa-sdk`
- `ATM10-Agent`
- `Tree-of-Sophia`
- `aoa-kag`

## Success criteria

The first wave is successful when:

- the common model exists without mutating the quest model
- progression is keyed by `agent_id` instead of profile-field drift
- eval evidence can award or withhold multi-axis advancement without one universal score
- questlines and campaigns stay outline-shaped instead of run-ledger shaped
- memo chronicles preserve witness and provenance without taking quest ownership
- routing can describe a future quest board as a derived surface without widening live authority
- `Dionysus` can stage the pack as transport and lineage, not canon

## Failure signs

Pause the contour if:

- profile schemas start collecting volatile stat fields
- routing starts inventing quest meaning
- playbooks start pretending to be runtime state
- memo starts copying live quest state as if it were settled memory
- a single progression score becomes the dominant authority signal

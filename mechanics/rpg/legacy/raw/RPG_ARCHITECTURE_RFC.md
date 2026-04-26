# RPG Architecture RFC

## Status

Proposed transport RFC for AoA runtime/frontend architecture.

This document uses `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` in the normative sense.

## Purpose

AoA now has:
- quest contracts
- agent role contracts
- evidence-backed progression
- skill-as-ability reflections
- technique-as-feat reflections

The next architectural step is to make those surfaces runnable and front-end-readable without letting runtime or UI silently become new sources of doctrine.

This RFC defines the hard split between:
1. source-owned meaning
2. proof and witness surfaces
3. runtime/session state
4. frontend/theme projections

## Core rule

The RPG layer MUST remain a reflection and orchestration layer.

It MUST NOT become a hidden base ontology that rewrites upstream meaning.

## Four-plane model

### 1. Source meaning plane

This plane owns durable meaning:
- quests
- roles
- skills
- techniques
- eval bundles
- playbooks
- memo objects
- routing authority surfaces

### 2. Proof and witness plane

This plane owns reviewed evidence and recallable witness:
- progression evidence
- eval verdicts
- chronicles
- quest-linked proof refs
- cited caution or downgrade surfaces

### 3. Runtime/session plane

This plane owns live state:
- build snapshots
- equipped loadout
- resource budgets
- current party composition
- orchestrator mode
- current run outcome
- runtime aggregation for frontend delivery

### 4. Presentation/theme plane

This plane owns reader-facing expression:
- agent sheets
- quest board cards
- campaign lane cards
- reputation panels
- timeline cards
- themed labels, icons, and display groupings

The presentation plane MAY rename or theme stable canonical keys.
It MUST NOT replace them.

## Non-negotiable laws

1. Source repos remain the owners of meaning.
2. Runtime repos remain the owners of live state.
3. Frontend projections remain derived and reviewable.
4. One universal power score MUST NOT become authoritative.
5. Unlocks, penalties, and reputation changes MUST remain evidence-backed and scoped.
6. Quest run results MUST NOT directly rewrite source quest state.
7. Frontend overlays MUST keep stable canonical keys available under the theme skin.
8. Current Codex orchestration MAY drive the system, but contracts MUST stay orchestrator-agnostic.

## The five canonical objects

### 1. `dual_vocabulary_overlay_v1`

Purpose:
- separate machine-stable canonical keys from themed UI labels
- let the frontend speak in game-facing language without mutating source doctrine

Owner:
- federation-level contract in `Agents-of-Abyss`

### 2. `agent_build_snapshot_v1`

Purpose:
- capture the current runtime-readable build of one agent
- unify role, progression, loadout, capabilities, tools, resources, and current reputation refs

Owner:
- runtime/service contract in `abyss-stack`

### 3. `reputation_ledger_v1`

Purpose:
- record scoped trust slices rather than one mystical karma score
- make penalties, trust gains, and caution posture explicit and cited

Owner:
- runtime/service contract in `abyss-stack`

### 4. `quest_run_result_v1`

Purpose:
- describe one concrete quest attempt or route execution
- preserve orchestrator, party, build snapshot refs, outputs, proof refs, penalties, and next hops

Owner:
- runtime/service contract in `abyss-stack`

### 5. `frontend_projection_bundle_v1`

Purpose:
- deliver one bounded projection bundle for frontend readers
- keep source refs visible
- keep theme overlays separate from source meaning

Owner:
- runtime/service contract in `abyss-stack`

## Why these five and not more

These five objects are the smallest set that can support:
- one stable machine vocabulary
- one runtime-readable agent sheet
- one transparent reputation system
- one evidence-carrying run result
- one front-end projection bundle

Anything heavier SHOULD wait for later passes.

## Canonical flow

```text
source-owned meaning
  -> typed or runtime loaders
  -> orchestrator selects party + wrapper + build
  -> runtime executes one bounded route
  -> proof and witness surfaces are written upstream
  -> runtime updates build snapshot + reputation ledger + run result
  -> runtime emits projection bundle for frontend readers
```

## Runtime law

`abyss-stack` MAY:
- store session state
- store build snapshots
- store reputation ledgers
- store run results
- aggregate source refs for frontend readers
- expose runtime APIs or helper services later

`abyss-stack` MUST NOT:
- replace upstream quest meaning
- replace agent role meaning
- replace skill or technique canon
- replace eval verdict doctrine
- replace memo object canon
- replace playbook meaning
- replace routing authority

## Frontend law

The frontend MAY:
- render cards, bars, badges, timelines, and maps
- theme canonical fields
- group surfaces into dashboards
- visualize reward and penalty hints

The frontend MUST NOT:
- invent new canonical keys
- award progression on its own
- mark quests complete on its own
- infer stronger authority than the source refs support
- hide the source of a reputation or penalty change

## Resource law

The canonical runtime resource names are:
- `integrity_budget`
- `focus_budget`
- `deep_budget`
- `recall_budget`
- `autonomy_budget`

A themed UI MAY display them as health, mana, stamina, clarity, resolve, or other labels through `dual_vocabulary_overlay_v1`.

The runtime contract MUST keep the canonical names.

## Equipment law

For the current contour:
- skill reflections act as active abilities
- technique reflections act as passive feats or perks
- toolsets remain runtime equipment, not source doctrine
- artifacts remain runtime reflections until a stronger artifact owner exists

That means:
- equipped abilities MAY reference `aoa-skills`
- equipped feats MAY reference `aoa-techniques`
- equipped artifacts MUST remain explicitly marked as runtime reflections for now

## Reputation law

Reputation MUST:
- be slice-based
- name the trust axis explicitly
- name the owner scope explicitly
- cite the cause and evidence
- remain reviewable
- allow negative or cautionary motion

Reputation MUST NOT:
- collapse into one universal reputation integer
- silently decay or improve without a recorded cause
- replace proof or quest acceptance

## Quest-run law

A quest run result MAY carry:
- run outcome
- source refs
- artifact refs
- proof refs
- chronicle refs
- progression delta previews
- reputation delta previews
- penalty records
- next-hop hints

A quest run result MUST NOT claim to be the source quest state.

If a run suggests quest-state motion, it should do so through a non-authoritative `quest_state_hint`.

## Codex law

At the current stage, Codex is the primary orchestrator driver.

The RFC still requires:
- `orchestrator_kind` to remain explicit
- `wrapper_class` to remain explicit
- `run_mode` to remain explicit
- build snapshots to remain portable enough for later local or hybrid drivers

This prevents accidental Codex-totalism.

## ToS law

AoA and ToS remain adjacent but non-collapsed authority planes.

AoA runtime/frontend projections MAY expose counterpart or campaign references into ToS later.

They MUST NOT treat those references as identity collapse.

## Security and public-safety law

Every schema in this RFC is public-safe by default.

That means:
- no secrets
- no hidden local paths
- no private machine metadata beyond safe abstract refs
- no silent incident detail
- no hidden scoring weights claimed as authority

If richer local runtime state is needed, keep it private to runtime overlays or service internals, not in the public contract.

## Extension rule

Future waves MAY add:
- artifact canon
- party templates
- campaign build planners
- typed SDK loaders
- public mirrors
- richer frontend cards

They MUST preserve:
- source ownership
- runtime ownership
- canonical vocabulary stability
- evidence-backed progression
- transparent penalties and reputation

## Final rule

The honest AoA RPG architecture is not a skin stretched over the federation.

It is the point where source meaning, proof, runtime, and presentation finally learn how to dance without stealing each other's bones.

# AGENTS root reference

This file preserves the previous full root guidance for `Agents-of-Abyss`.
The live root route card is `../AGENTS.md`.

Use this reference when:

- auditing a legacy rule from before Pack 5
- resolving a task branch that the short route card intentionally summarized
- checking whether a slimming move should become a nested `AGENTS.md`, owner doc, or validator rule

Do not treat this file as a competing root. If a preserved rule still actively governs a local directory, move or restate it at the smallest owner surface rather than re-bloating the root.

## Preserved root AGENTS.md from before Pack 5

# AGENTS.md

## Purpose

`Agents-of-Abyss` is the constitutional and ecosystem-center repository of AoA.
It owns ecosystem identity, layer map, federation rules, program-level direction,
and compact ecosystem-level registry surfaces.

It is not the full implementation home of AoA.
It may name long-arc federation direction, but it does not own the specialized
surfaces where that direction becomes operational.

## Read first

1. `CHARTER.md`
2. `ECOSYSTEM_MAP.md`
3. `docs/LAYERS.md`
4. `docs/FEDERATION_RULES.md`
5. `ROADMAP.md`
6. `README.md`

Then branch by task:

- process, mechanic, or engineering-philosophy route questions: `docs/MECHANICS.md`
- method-centered growth or scenario-home questions: `mechanics/method-growth/docs/METHOD_SPINE.md`
- adjunct RPG reflection or canonical vocabulary questions: `mechanics/rpg/docs/RPG_LAYER_MODEL.md` and `mechanics/rpg/docs/RPG_CANONICAL_TERMINOLOGY.md`
- Agon route, owner-request, or pre-protocol stop-line questions:
  `mechanics/agon/README.md`, `mechanics/agon/PARTS.md`,
  `mechanics/agon/OWNER_REQUESTS.md`, and `mechanics/agon/PROVENANCE.md`
- gate-routing handoff, owner request, or stop-line questions:
  `mechanics/agon/legacy/raw/AGON_GATE_ROUTING_HANDOFF.md`,
  `mechanics/agon/legacy/raw/AGON_GATE_ROUTING_OWNER_REQUEST.md`,
  `mechanics/agon/legacy/raw/AGON_GATE_ROUTING_STOP_LINES.md`, and
  `mechanics/agon/legacy/raw/AGON_WAVE5_CENTER_HANDOFF.md`
- witness / compost, counterpart bridge, or ToS support waves: the relevant compact doctrine note under `docs/`

Nearest-file precedence applies inside:

- `docs/AGENTS.md`
- `generated/AGENTS.md`
- `schemas/AGENTS.md`
- `scripts/AGENTS.md`

## Boundaries

Keep these distinctions explicit:

- ecosystem truth vs layer truth
- AoA operational federation vs ToS authored meaning
- routing or derived surfaces vs source-owned meaning
- center-level guidance vs runtime implementation detail
- long-arc direction vs owner-layer contract

Use this repository for charter, map, rules, roadmaps, and compact center
surfaces.

Route specialized detail back to the owning repositories:

- role progression, recurrence, and self-agent checkpoint posture -> `aoa-agents`
- questline, campaign, raid, reanchor, and harvest posture -> `aoa-playbooks`
- typed loading, compatibility, surface detection, and reviewed handoff helpers -> `aoa-sdk`
- skill meaning, proof meaning, routing meaning, memory meaning, and KAG meaning -> their owning repos
- runtime budgets, runtime state, and frontend presentation -> `abyss-stack` and its owner docs

## Direction posture

The center may name federation arcs, first-wave scope, and boundary law.

It may describe bounded, reviewable agency as a discipline, method-centered
composition as a growth move, and RPG / quest language as an adjunct reflection
layer.

It must not quietly absorb:

- skill, role, playbook, eval, memo, or KAG source truth
- quest state, progression state, or runtime checkpoint state
- frontend theming as a replacement for canonical machine vocabulary
- helper-layer implementation detail as if it were constitutional doctrine

## Editing priorities

- keep the root README concise, routing-first, and constitution-level
- prefer links to layer-owned repositories over copying their detail
- preserve stable terminology unless a rename is clearly justified and synchronized
- keep generated surfaces clearly derived
- keep public claims bounded and reviewable
- mention `aoa-sdk` only as a consumer or integration surface unless deeper center docs are updated in the same change
- keep adjunct RPG reflection clearly adjunct
- keep program direction honest without implying owner-layer implementation that is not yet documented upstream

## Hard no

- do not absorb technique, skill, eval, memo, role, playbook, or KAG source truth into the center
- do not restate ToS meaning here as if AoA owned it
- do not let runtime details from `abyss-stack` drift into constitutional ownership
- do not turn the root README into an archive of every wave note
- do not let routing tables or generated registries masquerade as ecosystem authority
- do not let questline or campaign language imply runtime ledger ownership in the center
- do not let canonical RPG vocabulary blur owner-layer boundaries or runtime ownership
- do not let long-arc direction harden into implementation claims without updating the owning repositories in the same change

## Workflow

`PLAN -> DIFF -> VERIFY -> REPORT`

## Validation

When changing the center layer, review:

- `README.md`
- `CHARTER.md`
- `ECOSYSTEM_MAP.md`
- `docs/LAYERS.md`
- `docs/FEDERATION_RULES.md`
- `ROADMAP.md`
- `generated/ecosystem_registry.min.json`

If the task touches method, quest reflection, or canonical vocabulary, also review the relevant compact doctrine note under `docs/`.

If the task touches the Agon move owner binding turn, also review:

- `mechanics/agon/legacy/raw/AGON_MOVE_OWNER_BINDING.md`
- `mechanics/agon/legacy/raw/AGON_MOVE_BINDING_MATRIX_MODEL.md`
- `mechanics/agon/OWNER_REQUESTS.md`
- `mechanics/agon/legacy/raw/AGON_PRE_PROTOCOL_STOP_LINES.md`
- `mechanics/agon/legacy/raw/AGON_WAVE4_LANDING.md`
- `mechanics/agon/parts/owner-binding/generated/agon_move_owner_binding_registry.min.json`

If the task touches the Agon gate routing handoff turn, also review:

- `mechanics/agon/legacy/raw/AGON_GATE_ROUTING_HANDOFF.md`
- `mechanics/agon/legacy/raw/AGON_GATE_ROUTING_OWNER_REQUEST.md`
- `mechanics/agon/legacy/raw/AGON_GATE_ROUTING_STOP_LINES.md`
- `mechanics/agon/legacy/raw/AGON_WAVE5_CENTER_HANDOFF.md`
- `mechanics/agon/parts/gate-routing/generated/agon_gate_routing_handoff_request.min.json`

If you edit `docs/`, `generated/`, `schemas/`, or `scripts/`, read the local
`AGENTS.md` first.

Run local validation when relevant:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_ecosystem.py
python -m pytest -q
```

If you changed the Agon move owner binding surfaces, also run:

```bash
python mechanics/agon/parts/owner-binding/scripts/build_agon_move_owner_binding_registry.py --check
python mechanics/agon/parts/owner-binding/scripts/validate_agon_move_owner_bindings.py
python -m pytest -q mechanics/agon/parts/owner-binding/tests/test_agon_move_owner_bindings.py
```

If you changed the Agon gate routing handoff surfaces, also run:

```bash
python mechanics/agon/parts/gate-routing/scripts/build_agon_gate_routing_handoff_request.py --check
python mechanics/agon/parts/gate-routing/scripts/validate_agon_gate_routing_handoff_request.py
python -m pytest -q mechanics/agon/parts/gate-routing/tests/test_agon_gate_routing_handoff_request.py
```

## Audit protocol

For repository audits and GitHub review, also read:

- `ECOSYSTEM_AUDIT_INDEX.md`
- `docs/audits/CODEX_AUDIT_PROTOCOL.md`

## Skill / proof audit bridge

When a task touches `aoa-skills` or `aoa-evals`, also read:

- `docs/audits/CODEX_SKILL_PROOF_AUDIT_BRIDGE.md`

## Review guidelines

For GitHub review in this repository, treat the following as P1:

- contradictions across `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/LAYERS.md`, `docs/FEDERATION_RULES.md`, `ROADMAP.md`, and `generated/ecosystem_registry.min.json`
- changes that blur source-of-truth boundaries or silently absorb layer-owned meaning into the center
- routing changes that point readers to the wrong owning repository
- center-level claims about quest, progression, checkpoint, or runtime state that should live in owner repos instead
- generated registry changes without corresponding source updates or without running `python scripts/validate_ecosystem.py`
- move owner binding registry changes without corresponding doctrine or without
  running `python mechanics/agon/parts/owner-binding/scripts/build_agon_move_owner_binding_registry.py --check`
  plus `python mechanics/agon/parts/owner-binding/scripts/validate_agon_move_owner_bindings.py`
- gate routing handoff request changes without corresponding doctrine or without
  running `python mechanics/agon/parts/gate-routing/scripts/build_agon_gate_routing_handoff_request.py --check`
  plus `python mechanics/agon/parts/gate-routing/scripts/validate_agon_gate_routing_handoff_request.py`
- semantic changes hidden under "docs-only" or "metadata-only" wording

Ignore trivial wording nits unless the task explicitly asks for copyediting.

## Definition of done

A change is done when:

- AoA is more intelligible after the edit
- source-of-truth boundaries are clearer, not blurrier
- routing to neighboring layers is easier
- long-arc direction is easier to read without being overclaimed
- no specialized layer was silently absorbed into the center
- validation passes, or any missing validation is disclosed honestly

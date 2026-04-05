# AGENTS.md

## Purpose

`Agents-of-Abyss` is the constitutional and ecosystem-center repository of AoA. It owns ecosystem identity, layer map, federation rules, program-level direction, and compact ecosystem-level registry surfaces. It is not the full implementation home of AoA.

## Read first

1. `CHARTER.md`
2. `ECOSYSTEM_MAP.md`
3. `docs/LAYERS.md`
4. `docs/FEDERATION_RULES.md`
5. `ROADMAP.md`
6. `README.md`

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

Use this repository for charter, map, rules, roadmaps, and compact center surfaces. Route technique, skill, eval, memo, role, playbook, KAG, runtime, and ToS source detail back to the owning repositories.

## Editing priorities

- keep the root README concise, routing-first, and constitution-level
- prefer links to layer-owned repositories over copying their detail
- preserve stable terminology unless a rename is clearly justified and synchronized
- keep generated surfaces clearly derived
- keep public claims bounded and reviewable
- mention `aoa-sdk` only as a consumer or integration surface unless deeper center docs are updated in the same change

## Hard no

- do not absorb technique, skill, eval, memo, role, playbook, or KAG source truth into the center
- do not restate ToS meaning here as if AoA owned it
- do not let runtime details from `abyss-stack` drift into constitutional ownership
- do not turn the root README into an archive of every wave note
- do not let routing tables or generated registries masquerade as ecosystem authority

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

If you edit `docs/`, `generated/`, `schemas/`, or `scripts/`, read the local `AGENTS.md` first.

Run local validation when relevant:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_ecosystem.py
```

## Audit protocol

For repository audits and GitHub review, also read:

- `ECOSYSTEM_AUDIT_INDEX.md`
- `docs/CODEX_AUDIT_PROTOCOL.md`

## Skill / proof audit bridge

When a task touches `aoa-skills` or `aoa-evals`, also read:

- `docs/CODEX_SKILL_PROOF_AUDIT_BRIDGE.md`

## Review guidelines

For GitHub review in this repository, treat the following as P1:

- contradictions across `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/LAYERS.md`, `docs/FEDERATION_RULES.md`, `ROADMAP.md`, and `generated/ecosystem_registry.min.json`
- changes that blur source-of-truth boundaries or silently absorb layer-owned meaning into the center
- routing changes that point readers to the wrong owning repository
- generated registry changes without corresponding source updates or without running `python scripts/validate_ecosystem.py`
- semantic changes hidden under "docs-only" or "metadata-only" wording

Ignore trivial wording nits unless the task explicitly asks for copyediting.

## Definition of done

A change is done when:

- AoA is more intelligible after the edit
- source-of-truth boundaries are clearer, not blurrier
- routing to neighboring layers is easier
- no specialized layer was silently absorbed into the center
- validation passes, or any missing validation is disclosed honestly

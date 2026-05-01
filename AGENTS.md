# AGENTS.md

## Applies to

This root card applies to the whole repository unless a nearer nested `AGENTS.md` narrows the lane.

## Role

This AGENTS card keeps local work inside the Agents-of-Abyss center lane, names
the nearest owner boundary, and routes wider claims to the owning surface.

It is the agent-facing route law for this repository. It does not replace
`README.md`, `CONTRIBUTING.md`, `docs/START_HERE_ROUTE_CONTRACT.md`, or local
owner truth.

## Read before editing

Read this root card first. Then read the nearest nested `AGENTS.md` for every
touched path, followed by the route-mode surface and the nearest
`README.md`, protocol, schema, builder, validator, or source surface that owns
the local claim.

## Boundaries

Do not use this lane to override owner-local truth, generated-source boundaries, sibling-repo authority, or release validation contracts.

## Validation

Run the nearest validator named by this card. For release-facing changes, also run `python scripts/release_check.py`.

## Closeout

Closeout must name changed surfaces, checks run, checks skipped, remaining risk,
decision review result, and the next owner route if this lane was only a
waypoint.

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

For first reading or outside orientation, use the canonical first-reading route:

1. `README.md`
2. `CHARTER.md`
3. `ECOSYSTEM_MAP.md`
4. `docs/FEDERATION_RULES.md`

For agent editing, use the operational route:

1. this `AGENTS.md`
2. nearest nested `AGENTS.md` for every touched path
3. route-mode surface from the table below
4. nearest local `README.md`, protocol, schema, builder, validator, or source
   surface
5. narrowest relevant validator before broader gates

For center authority surfaces, also read:

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
| `direction-change` | roadmap, horizon posture, maturity, owner-route pressure, future trigger, or release contour changes | `ROADMAP.md` |
| `ownership-routing` | ownership is unclear | `docs/REPO_ROLES.md` |
| `mechanic-change` | center mechanic package, process route, stop-line, owner split, or mechanic-facing validation changes | `mechanics/README.md` |
| `organ-alignment` | repository organ posture, required route surfaces, surface-state vocabulary, first-cycle route, or cross-repo organ handoff changes | `docs/organ-contract/README.md` |
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

## GitHub landing workflow

Root `AGENTS.md` owns the repository-wide branch, PR, CI, and merge route.
`.github/AGENTS.md` owns the GitHub-native files that support it.

When the user asks to commit, push, and merge in this repository, use this route:

1. Start from a clean branch based on current `origin/main`.
2. Commit only the intended diff with a message that names the changed surface.
3. Push the branch and open a pull request with changed surfaces, validation,
   skipped checks, and remaining risk.
4. Wait for GitHub `Repo Validation` to finish. If it fails, fix the branch and
   wait for the new result.
5. Merge through GitHub after green validation. Current repository settings
   reject merge commits; use squash unless settings change. If GitHub reports a
   different allowed method for a future PR, use the allowed method and report
   which method landed.
6. Return to `main`, fast-forward from `origin/main`, and confirm the worktree is
   clean before closeout.

If GitHub status or merge permissions cannot be observed, stop the landing route
and report the exact blocker instead of guessing.

## Post-change route review

Before closeout, check whether the change actually affects these surfaces. Update
only the ones that moved; otherwise say no update was needed.

- `ROADMAP.md` when center-wide direction, horizon posture, maturity,
  owner-route pressure, organ-alignment contour, registry/entry contour,
  release-support direction, or a concrete future trigger changed
- `CHANGELOG.md` when release-visible behavior, public docs, validation, or
  repository structure changed
- `docs/decisions/` when future agents need the rationale for a route,
  ownership, workflow, validator, public-contract, or topology choice
- generated surfaces, builders, validators, and tests when a source-backed
  machine capsule changed
- mechanic `LANDING_LOG.md`, `OWNER_REQUESTS.md`, `PARTS.md`, or `PROVENANCE.md`
  when a mechanic landing, owner request, active part, or legacy bridge changed
- `QUESTBOOK.md` or `quests/` when a durable obligation should survive the diff
- neighboring owner repositories when the change routes or constrains their truth

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

Run the narrowest relevant center check first. For release-facing or repo-wide
changes, run the full gate:

```bash
python scripts/release_check.py
```

The entry-surface baseline command set is
`docs/guardrails/ENTRY_SURFACE_VALIDATION_BASELINE.md`. Keep that surface,
`scripts/center_entry_map_common.py`, `scripts/validate_entry_surface_sync.py`,
and `scripts/release_check.py` aligned when the center-wide validation route
changes.

If an Agon owner-binding or gate-routing surface changes, use
`mechanics/agon/AGENTS.md` and `mechanics/agon/parts/AGENTS.md` for the
matching builder, validator, and targeted tests.

`scripts/release_check.py` owns the expanded default gate. Prefer keeping this
root card short and using local `AGENTS.md` cards for lane-specific commands.

## Report

Close with the center surfaces changed, whether owner boundaries shifted, which
neighboring repos are affected, whether post-change route review changed any
follow-up surface, and exactly which checks ran or did not run. If a PR was
merged, name the GitHub merge method that landed.

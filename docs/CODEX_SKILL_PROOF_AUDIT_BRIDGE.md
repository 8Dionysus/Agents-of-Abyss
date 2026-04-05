# Codex Skill / Proof Audit Bridge

This document defines the audit seam between `aoa-skills` and `aoa-evals`.

Use it when:

- a task changes skill meaning and you need to know whether proof surfaces must follow,
- a task changes eval wording and you need to know whether it rewrites skill meaning,
- a cross-repo wave touches both execution and proof surfaces,
- PR review needs to distinguish workflow drift from proof drift.

Read this file together with:

- `docs/CODEX_AUDIT_PROTOCOL.md`
- `ECOSYSTEM_AUDIT_INDEX.md`
- `aoa-skills/AUDIT.md`
- `aoa-evals/AUDIT.md`

## Ownership split

### `aoa-skills` owns

- bounded execution canon,
- trigger boundaries,
- invocation posture,
- inputs and outputs,
- procedure, contracts, anti-patterns, and adaptation points,
- technique traceability and thin overlay posture,
- derived skill runtime, evaluation, and public surfaces.

### `aoa-evals` owns

- bounded proof canon,
- object under evaluation,
- bounded claim framing,
- verdict shape, caveats, blind spots, and interpretation guidance,
- comparison posture, baseline semantics, and public chooser wording,
- shared proof infrastructure contracts that remain weaker than bundle-local meaning,
- derived eval catalogs and comparison-spine surfaces.

## First question to ask

If the question is **what should the agent do or not do**, start in `aoa-skills`.

If the question is **what can we defend as proven, and how strongly**, start in `aoa-evals`.

If both are moving, execution meaning should be reviewed first and proof meaning second.

## Seam rules

1. `aoa-skills` may expose repo-local evidence surfaces such as runtime walkthroughs and the skill evaluation matrix, but those do not move proof doctrine into the skill layer.
2. `aoa-evals` may read runtime artifacts and trace surfaces as evidence inputs, but verdict logic and bounded proof wording remain owned by `aoa-evals`.
3. Generated catalogs, matrices, capsules, and comparison surfaces stay subordinate to authored markdown and manifests.
4. Public chooser wording must stay weaker than the bundle contract.
5. Thin overlays may adapt commands, paths, approval posture, and verification notes, but they must not become downstream authority.

## Current pairings live in source repos

This bridge does not own a static workflow-to-proof pairing table.

If a seam review needs the current live pairing, read the owner surfaces first:

### Workflow-side current state

- `aoa-skills/SKILL_INDEX.md`
- the target `skills/*/SKILL.md`
- the target `skills/*/techniques.yaml`
- `aoa-skills/AUDIT.md`

### Proof-side current state

- `aoa-evals/EVAL_INDEX.md`
- `aoa-evals/EVAL_SELECTION.md`
- the target `bundles/*/EVAL.md`
- the target `bundles/*/eval.yaml`
- `generated/comparison_spine.json` when baseline or comparison posture matters

Derive the current pairing from those source-owned surfaces instead of storing it here.

If the bridge needs a new standing seam rule, add that rule here.
If only a concrete pairing changed, update the owning repo instead.

## Cross-repo wave order

### 1. Establish the owner

State whether the task is primarily:

- skill meaning,
- proof meaning,
- or a true two-repo seam.

### 2. Audit the owning repo first

Start with a report-first memo in the owning repo:

- active instructions,
- source-of-truth docs,
- exact local verification,
- smallest reviewable next change,
- likely neighbor impact.

### 3. Patch the owning repo

Keep the diff narrow and validate locally.

### 4. Inspect the neighbor repo before touching it

Ask:

- does the existing proof surface still describe the changed workflow honestly?
- does the existing workflow still support the current proof wording?
- did a chooser, matrix, or comparison surface become misleading?

### 5. Only then patch the neighbor repo

If the neighbor needs changes, make them as a second bounded wave rather than opportunistic cleanup.

### 6. Report remaining asymmetry explicitly

If the wave stops after one repo, name the unresolved seam rather than pretending it is already coherent.

## Anti-patterns to flag immediately

- changing skill trigger boundaries and assuming existing eval claims still hold,
- changing eval chooser or comparison wording and assuming skill meaning is unchanged,
- using artifact polish as proof of process discipline,
- using process discipline as proof of artifact excellence,
- treating `aoa-eval-integrity-check` as a direct runtime-quality eval,
- letting overlay packs act like downstream authority,
- letting generated surfaces outrank authored markdown or manifests,
- letting comparison surfaces inherit baseline or growth meaning by association.

## Default verification order for a two-repo wave

### If skill meaning changes first

```bash
cd ../aoa-skills
python scripts/release_check.py
python scripts/report_skill_evaluation.py --fail-on-canonical-gaps
```

If technique refs or bridge wording changed:

```bash
cd ../aoa-skills
python scripts/report_technique_drift.py --techniques-repo ../aoa-techniques
```

### If proof meaning must follow

```bash
cd ../aoa-evals
python scripts/build_catalog.py
python scripts/validate_repo.py
```

For comparison or baseline waves, also re-read:

- `generated/comparison_spine.json`
- `EVAL_INDEX.md`
- `EVAL_SELECTION.md`
- `docs/COMPARISON_SPINE_GUIDE.md`

## Report contract for seam work

Every seam review should state:

- owning repo,
- whether the neighbor repo was inspected,
- whether skill meaning changed,
- whether proof meaning changed,
- what validation ran in each repo,
- what remains intentionally deferred.

Do not claim cross-repo coherence unless both layers were actually checked.

# Experience Wave 4: Polis Governance And Constitution Runtime

Experience Wave 4 plants v0.8 polis governance and v0.9 constitution runtime
as one bounded center program with owner-local landings.

Wave 4 asks whether the experience mechanic can handle disagreement, appeal,
stay, veto, charter change, revocation, release hold, sealed decision, replay,
and precedent without turning Codex, assistants, routing, memory, runtime, KAG,
stats, or playbooks into hidden authority.

## Source Seeds

- `aoa-experience-polis-governance-seed-v0_8.zip`
- `aoa-experience-constitution-runtime-seed-v0_9.zip`

## Ordered Spine

The polis spine is:

1. governance case opened
2. authority checked
3. council or sovereign review selected
4. vote, veto, stay, appeal, or amendment resolved
5. decision logged
6. owner-local route declared
7. precedent or release hold recorded
8. retention and audit scheduled

The constitution runtime spine is:

1. runtime case queued
2. authority resolved
3. council scheduled with quorum
4. vote sealed before reveal
5. reveal checked against sealed hash
6. stay, hold, or appeal enforced
7. decision history replayed
8. precedent indexed from sealed decision
9. dashboard and owner-local dispatch recorded

The order matters. Runtime execution may make governance legible, but it must
not manufacture authority.

## Stop-Lines

Codex may enqueue, summarize, simulate, propose, and prepare review material.

Codex must not vote, resolve sovereign authority, seal final decisions, suppress
material stays, certify appeals, amend charters, direct-write into
`Tree-of-Sophia`, force owner adoption, author routing meaning, or promote
policy precedent.

Assistant agents must not self-recharter, self-certify, vote on their own
release, bypass release holds, or turn shared precedent into hidden durable
behavior.

Runtime jobs may enforce scoped, expiring, replayable records. Runtime jobs must not become the source of constitutional meaning.

KAG, stats, memo, routing, playbooks, skills, techniques, evals, agents, SDK,
and stack surfaces remain owner-local. They carry bounded artifacts, route
signals, proof, memory, method, role posture, or runtime support; they do not
own the center law.

## Owner Split

- `Agents-of-Abyss` owns the Wave 4 center law, stop-lines, ordered spine, and
  owner split.
- `Tree-of-Sophia` owns source-first dossier intake boundaries and no direct governance or runtime write.
- `aoa-evals` owns bounded verdict surfaces for authority resolution, stay
  enforcement, vote seal integrity, and replay integrity.
- `aoa-playbooks` owns runbook and scenario composition for sealed sessions,
  stay enforcement, appeal expiry, and replay audit.
- `aoa-stats` owns derived dashboard and queue summaries without judging
  meaning.
- `aoa-memo` owns bounded decision memory, stay-order memory, and precedent
  writeback without becoming proof.
- `aoa-routing` owns case, appeal, stay, and precedent route signals without
  becoming authority.
- `aoa-agents` owns agent authority claim posture, release holds, kind-safe
  enforcement, and self-recharter blocks.
- `aoa-sdk` owns typed helper calls for queues, runtime API, vote sealing, and
  replay helpers.
- `aoa-kag` owns derived precedent candidates and supersession links without
  forced adoption.
- `aoa-skills` owns bounded governance-runtime skill invocation posture.
- `aoa-techniques` owns reusable authority-resolution and sealed-decision
  techniques.
- `abyss-stack` owns runtime queues, storage, scheduler, stay enforcement, and
  replay jobs without authoring the law.

## Validation

Wave 4 is valid when:

- the center example validates against
  `schemas/experience-wave4-polis-constitution.schema.json`;
- v0.8 source seeds precede v0.9 source seeds;
- both ordered spines match the documented order;
- every owner in the split remains present;
- denied Codex and assistant authority cannot be moved into allowed runtime
  action;
- owner-local schema/example pairs reject unknown fields, wrong types, missing
  required fields, enum escapes, const escapes, and malformed array items.

Run:

```bash
python scripts/validate_experience_wave4.py
python -m pytest -q tests/test_experience_wave4.py tests/test_experience_wave4_seed_contracts.py
```

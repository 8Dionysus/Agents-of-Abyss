# Checkpoint Direction

Checkpoint should make growth easier to continue, review, return to, and hand
off without increasing hidden authority.

The direction is not to build a new checkpoint empire. The direction is to make
every intermediate state honest:

- what was preserved
- why it matters
- who can review it
- where it may return
- which owner must accept the next move
- what must remain provisional

## Current contour

The center landing is intentionally thin:

- center law and stop-lines live here
- implementation controls stay in `aoa-sdk`
- checkpoint-note protocol and bridge skill stay in `aoa-skills`
- self-agent posture stays in `aoa-agents`
- relaunch, recall, and writeback stay in `aoa-memo`
- choreography stays in `aoa-playbooks`
- proof stays in `aoa-evals`
- navigation hints stay in `aoa-routing`
- derived visibility stays in `aoa-stats`
- runtime exports stay in `abyss-stack`

## Growth rule

Add detail only when a repeated checkpoint shape cannot be handled by the
existing parts and owner map.

If a future route needs local implementation, proof, memory, runtime, or
scenario behavior, add or update the owner request first. Do not hide the need
inside center prose.

## When The Time Comes

Use this block for future work that is likely but not yet worth landing:

- Define a compact checkpoint state vocabulary if owner repos start using
  incompatible state words.
- Add a machine-readable checkpoint owner map only after the text owner map
  proves stable.
- Split a new part only when one checkpoint form repeats across more than one
  owner route.

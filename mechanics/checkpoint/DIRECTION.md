# Checkpoint Direction

Checkpoint should make growth easier to continue, review, return to, and hand
off without increasing hidden authority.

This file owns the current operating direction only. It does not replace the
part map, landing ledger, roadmap, owner-request packet, owner map, or
provenance bridge.

## Source-of-truth split

- `README.md`: package entry card and shortest route.
- `DIRECTION.md`: current operating direction.
- `PARTS.md`: active part map.
- `parts/`: concise checkpoint contracts.
- `OWNER_MAP.md`: stronger-owner split.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `LANDING_LOG.md`: canonical landing ledger.
- `ROADMAP.md`: future contour, not a historical ledger.
- `PROVENANCE.md`: the only active bridge back to source accounting.
- `docs/`: center law and owner-boundary doctrine.

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

## Validation

Use the validation lane in [mechanics/checkpoint/AGENTS.md](AGENTS.md#validation) for executable commands.

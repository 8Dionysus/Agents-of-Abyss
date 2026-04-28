# Recurrence Direction

Recurrence should make long-horizon work able to return without pretending that
continuity is ambient memory.

This file owns the current operating direction only. It does not replace the
part map, landing ledger, roadmap, owner-request packet, owner map, or
provenance bridge.

## Source-of-truth split

- `README.md`: package entry card and shortest route.
- `DIRECTION.md`: current operating direction.
- `PARTS.md`: active part map.
- `parts/`: concise recurrence contracts.
- `OWNER_MAP.md`: stronger-owner split.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `LANDING_LOG.md`: canonical landing ledger.
- `ROADMAP.md`: future contour, not a historical ledger.
- `PROVENANCE.md`: the only active bridge back to source accounting.
- `docs/`: center recurrence doctrine and owner-request notes.

The direction is not to create a new control plane inside the center. The
direction is to make every return honest:

- what axis was lost
- which anchor still holds
- who owns that anchor
- how re-entry stays bounded
- when the route must reroute, escalate, or safe-stop
- which owner must accept any operational behavior

## Current contour

The center landing is intentionally thin:

- center law and vocabulary live here
- typed carry and recurrence graph work stay in `aoa-sdk`
- route hints stay in `aoa-routing`
- anchors, recall, and provenance stay in `aoa-memo`
- actor continuity posture stays in `aoa-agents`
- recurring choreography stays in `aoa-playbooks`
- proof stays in `aoa-evals`
- derived visibility stays in `aoa-stats`
- regrounding stays in `aoa-kag`
- runtime return stays in `abyss-stack` and product-local runtime owners

## Growth rule

Add detail only when a repeated recurrence shape cannot be handled by the
existing parts and owner map.

If a future route needs implementation, proof, memory, runtime behavior, or
scenario choreography, update the owner request first. Do not hide the need
inside center prose.

## When the time comes

Use this block for future work that is likely but not yet worth landing:

- Add machine-readable recurrence part metadata only after the text part map
  proves stable.
- Split a new part only when a recurrence form repeats across more than one
  owner route.
- Promote owner-local recurrence packages in sibling repositories only when
  those repositories own a living facet, not for visual symmetry.

## Validation

Use the validation lane in [mechanics/recurrence/AGENTS.md](AGENTS.md#validation) for executable commands.

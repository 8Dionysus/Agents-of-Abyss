# Growth Cycle Direction

Growth Cycle should make agent-process growth easier to continue, inspect,
repair, promote, and hand off without hiding authority in the loop.

This file owns the current operating direction only. It does not replace the
part map, landing ledger, roadmap, owner-request packet, owner map, or
provenance bridge.

## Source-of-truth split

- `README.md`: package entry card and shortest route.
- `DIRECTION.md`: current operating direction.
- `PARTS.md`: active part map.
- `parts/`: concise growth-cycle contracts.
- `OWNER_MAP.md`: stronger-owner split.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `LANDING_LOG.md`: canonical landing ledger.
- `ROADMAP.md`: future contour, not a historical ledger.
- `PROVENANCE.md`: the only active bridge back to source accounting.
- `docs/`: center law and owner-request doctrine.

The direction is not to create one master process. The direction is to keep the
cycle readable:

- what state the process is in
- what reviewed evidence exists
- which stage comes next
- which owner owns the stronger truth
- which stop-line prevents overclaiming
- what should be remembered, measured, repaired, or promoted only after review

## Current contour

The center landing is intentionally thin:

- center law and stage order live here
- hooks and local control stay in `aoa-sdk`
- executable stage skills stay in `aoa-skills`
- self-agent posture stays in `aoa-agents`
- proof and verdicts stay in `aoa-evals`
- memory writeback stays in `aoa-memo`
- choreography stays in `aoa-playbooks`
- derived visibility stays in `aoa-stats`
- route hints stay in `aoa-routing`
- reviewed snapshots and seeds stay in `Dionysus`
- runtime exports stay in `abyss-stack`

## Growth rule

Add detail only when a repeated cycle shape cannot be handled by the existing
parts and owner map.

If a future route needs local implementation, proof, memory, runtime, quest, or
scenario behavior, add or update the owner request first. Do not hide the need
inside center prose.

## When The Time Comes

Use this block for future work that is likely but not yet worth landing:

- Add a machine-readable stage vocabulary after at least two owner repositories
  start carrying Growth Cycle receipts.
- Add part-local artifact homes only after a part needs schemas, examples,
  generated companions, scripts, or tests beyond the package validator.
- Add a cross-repo cycle dashboard only after `aoa-stats` has owner-local
  receipts to read.

## Validation

Use the validation lane in [mechanics/growth-cycle/AGENTS.md](AGENTS.md#validation) for executable commands.

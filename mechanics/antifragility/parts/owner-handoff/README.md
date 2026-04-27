# Owner Handoff

Owner handoff turns an antifragility finding into a portable request packet.

## Use When

- The next repair, proof, memory, stats, playbook, skill, technique, or runtime
  move belongs outside AoA.
- A cleanup recommendation needs owner acceptance.
- A finding should become an issue, branch, receipt, or owner-local doc.

## Do Not Use When

- The center can resolve the route by editing center doctrine only.
- The owner has already accepted and landed the slice.
- The packet lacks a stop-line.

## Route Check

Name the request ID, owner repo, required landing, proof route, stop-line, and
next owner action.

## Active Outputs

- Owner request packet.
- Handoff surface hint.
- Stop-line.
- Next action.

## Next Route

Update [OWNER_REQUESTS](../../OWNER_REQUESTS.md) and
`mechanics/owner-request-queue.json`; rebuild generated owner-request surfaces.

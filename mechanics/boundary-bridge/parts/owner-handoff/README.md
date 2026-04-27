# Owner Handoff

Use this part when the center prepares a request for a stronger owner.

## Function

Make center-side bridge packets portable without claiming owner acceptance.

## Inputs

- request id
- owner repo
- slice
- required owner landing
- proof route
- stop-line

## Outputs

- owner request packet
- next owner action
- center status that remains `requested` until accepted

## Stop-lines

- no owner acceptance without owner receipt
- no owner-local truth in center
- no handoff packet as proof

## Validation

Use the validation lane in [../../AGENTS.md](../../AGENTS.md#validation).

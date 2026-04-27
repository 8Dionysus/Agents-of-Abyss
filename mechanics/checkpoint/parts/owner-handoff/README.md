# Owner Handoff

Owner Handoff turns checkpoint pressure into a named stronger-owner route
without treating the handoff as acceptance.

## Use When

- Checkpoint evidence survived review and needs a next owner.
- A center stop-line must become an owner request.
- A future owner repo should accept, reject, land, or prove a slice.

## Do Not Use When

- The center can finish the work without crossing owner boundaries.
- The target owner is unclear.
- The handoff is being worded as if already accepted.

## Route Check

Ask whether the target owner, required landing, proof route, and stop-line are
all named. If not, return to owner map before writing the request.

## Active Outputs

- owner request packet
- handoff route
- proof route
- stop-line
- next action

## Next Route

Carry the request ID to the owner repository. Update the center queue only after
owner-local acceptance, landing, or proof exists.

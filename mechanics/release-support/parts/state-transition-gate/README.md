# State Transition Gate

Use this part before claiming that work changed state.

## Use When

- A draft, packet, checkpoint, quest, mechanic, or release candidate is being
  described as landed, active, public, closed, shipped, superseded, or ready for
  handoff.
- A wording update might be mistaken for a real transition.

## Do Not Use When

- You are only editing local prose without changing status, claims, owner
  route, or proof posture.
- The transition is already owned by a stronger repository and the center has
  no claim to make.

## Route Check

Name the old state, new state, evidence, owner, public visibility, and rollback
route before writing the claim.

## Active Outputs

- Transition statement.
- Evidence requirement.
- Owner route.
- Stop-line for claims not yet supportable.

## Next Route

Use `landing-closeout` for mechanic or wave landings, `public-claim-gate` for
public wording, and `owner-handoff-packet` when the next move belongs outside
the center.

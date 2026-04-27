# Authority Boundary

Authority boundary catches convenience surfaces that start sounding canonical.

## Use When

- A derived, helper, routing, memory, stats, or runtime surface begins to act as
  source truth.
- A center doc starts owning owner-local operation.
- A wrapper hides policy or mutation.

## Do Not Use When

- The owner repository explicitly owns and documents the authority.
- The issue is only wording without boundary drift.
- Proof is needed before deciding whether authority moved.

## Route Check

Name the surface, the authority it appears to claim, the actual owner, and the
smallest move that shrinks the claim.

## Active Outputs

- Anti-authority stop-line.
- Owner route.
- Narrowing or rewording request.
- Helper or wrapper boundary request.

## Next Route

Route proof to `aoa-evals`, owner correction to the owner repository, and
derived-summary narrowing to `aoa-stats` when the drift is observational.

# Control Plane Carry

Control Plane Carry keeps recurrence manifests, graph closure, projections, and
return handoff packets typed, reviewable, and non-mutating.

## Use When

- Recurrence signals need typed carry before owner-local work.
- A manifest, graph closure, propagation plan, projection, or handoff packet
  must stay review-only.
- Mixed manifest shapes need quarantine instead of coercion.

## Do Not Use When

- The owner repo has already accepted and is executing the local change.
- A projection is being treated as source truth.
- The route wants hidden scheduler, mutation, or recursor activation.

## Route Check

Ask whether the control-plane surface observes, plans, projects, or hands off.
If it mutates owner truth, stop and route to the owner repository.

## Active Outputs

- manifest scan route
- graph closure route
- propagation-plan route
- downstream projection route
- reviewed return handoff route

## Next Route

Route programmable carry to `aoa-sdk`, thin projections to `aoa-routing`,
`aoa-stats`, or `aoa-kag`, and owner decisions to the target owner repository.

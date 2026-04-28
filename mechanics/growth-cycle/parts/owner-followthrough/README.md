# Owner Followthrough

Owner Followthrough carries unresolved cycle pressure to the repository that
owns the stronger truth.

## Use When

- The center has done all it can without owner-local acceptance.
- A cycle stage produced a request packet, proof need, memo handoff, stats
  handoff, runtime need, or route pressure.
- The next agent needs a clear owner route.

## Do Not Use When

- The owner route is unknown and federation rules have not been checked.
- The center is trying to claim owner-local landing.
- The item is only a private note with no durable consequence.

## Route Check

Ask which owner must act, what packet they need, what proof or receipt would
close it, and what the center must stop claiming meanwhile.

## Active Outputs

- owner request packet
- next owner route
- proof or receipt requirement
- memo or stats handoff
- remaining stop-line

## Next Route

Carry the request ID into the owner repository. Route unclear ownership back to
`docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md` before changing owner-local
surfaces.

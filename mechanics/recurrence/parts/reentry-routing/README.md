# Reentry Routing

Reentry Routing keeps return navigation thin, source-referring, and weaker than
recurrence meaning.

## Use When

- A route needs the smallest valid re-entry surface.
- A return hint should point back to source-owned or memo-supported surfaces.
- A live-session reentry review needs bounded navigation fields.

## Do Not Use When

- The router is asked to decide whether return is legitimate.
- The hint would become memory truth, budget policy, or runtime resume authority.
- The route widens into graph traversal or open exploration.

## Route Check

Ask whether the route hint points to a stronger source-owned surface. If the
primary authority target is routing-owned generated output, stop and reroute.

## Active Outputs

- re-entry hint
- source-owned inspect route
- memo recall pointer
- live-session reentry review route
- loop guard route

## Next Route

Route navigation implementation to `aoa-routing`, checkpoint continuity to
`aoa-memo`, actor posture to `aoa-agents`, and runtime consumption to
`abyss-stack` after runtime gates.

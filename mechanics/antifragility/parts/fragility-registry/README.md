# Fragility Registry

Fragility registry keeps known fragile patterns visible without converting them
into a global health score.

## Use When

- A repeated fragility pattern appears across docs, routes, generated surfaces,
  runtime helpers, or owner handoffs.
- A cleanup candidate needs pattern language before owner review.
- A public route needs to explain why a pattern is risky.

## Do Not Use When

- The finding is a one-off owner-local bug with no recurring pattern.
- The registry entry would become a score or leaderboard.
- There is no owner route for the pattern.

## Route Check

Name the pattern, fragility, default response, owner route, and why it should be
tracked without becoming sovereign.

## Active Outputs

- Pattern entry.
- Owner review route.
- Default response.
- Stop-line against score sovereignty.

## Next Route

Update [FRAGILITY_BLACKLIST](../../FRAGILITY_BLACKLIST.md) only when the pattern
is stable enough to help future review.

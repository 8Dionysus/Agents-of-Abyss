# Quest Execution Passport

This document owns the execution passport vocabulary carried by quest source
objects.

## Passport Fields

Every quest carries:

- `difficulty`
- `risk`
- `control_mode`
- `delegate_tier`
- optional `wrapper_class`

These fields do not answer "when". They answer "who may touch this, under what
leash, and how expensive a mistake would be".

## Difficulty Ladder

- `d0_probe` - bounded reading, triage, listing, no write
- `d1_patch` - one small bounded change in one surface
- `d2_slice` - one bounded slice across a few files in one owner surface
- `d3_seam` - contract or layer seam inside one repo or between adjacent repos
- `d4_architecture` - broad architectural or policy route
- `d5_doctrine` - rule-birth, ownership-boundary, or public-canon work

## Risk Ladder

- `r0_readonly`
- `r1_repo_local`
- `r2_contract`
- `r3_side_effect`

## Delegation Rule

Do not hand `d3+` quests directly to smaller local wrappers. Split them into
honest `d0-d2` leaves first.

## Stop-Lines

- Passport fields do not prove readiness.
- Delegation tier is not owner acceptance.
- Control mode is not permission to bypass source owners.
- Wrapper class is not a substitute for review.

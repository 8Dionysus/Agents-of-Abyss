# Release-Support Roadmap

## Current Contour

Release-support now treats release as a state transition. The mechanic should
help agents decide when a claim can move from draft, wave, checkpoint, quest,
landing, owner request, or internal posture into a supportable release,
handoff, public claim, or rollback-bounded state.

The active contour is:

- gate transition claims before they become public or owner-facing
- keep `CHANGELOG.md`, `ROADMAP.md`, mechanic `LANDING_LOG.md`, `DIRECTION.md`,
  and `PARTS.md` in separate roles
- route proof, runtime, projection, SDK, routing, stats, and sibling acceptance
  to owner repositories
- keep rollback and return visible before claiming stability

## When The Time Comes

- Add a release-support artifact map only if state-transition schemas,
  examples, generated companions, or tests become mechanic-owned artifacts.
- Add stronger closeout automation only after checkpoint, questbook, and
  release-support routes have repeated reviewed evidence.
- Consider a federation-level transition status vocabulary only if owner repos
  begin emitting comparable release or landing receipts.
- Consider `aoa-sdk` helper contracts for loading release-support generated
  companions after owner requests are accepted.

## Next Work

- Keep root `CHANGELOG.md`, `ROADMAP.md`, mechanic `LANDING_LOG.md`, and
  release-support docs aligned without duplicating chronology.
- Add public-claim checks only when they can be verified.
- Keep sibling release claims tied to owner evidence.
- Watch for transition claims leaking into public docs without proof or
  rollback route.

## Out Of Scope

- Public claims without validation.
- Sibling implementation release truth.
- Runtime deployment truth.
- Replacing root `CHANGELOG.md`, root `ROADMAP.md`, or mechanic landing logs.
- Treating generated mirrors as release authority.

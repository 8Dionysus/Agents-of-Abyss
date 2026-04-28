# Release Support Parts

The active parts are the default operating surface for release-support. Open the
part that matches the transition being claimed, then route proof, adoption,
publication, or rollback to the owner that must carry it.

## Part map

- [State Transition Gate](parts/state-transition-gate/README.md): decide
  whether a change has really moved state or only changed wording.
- [Public Claim Gate](parts/public-claim-gate/README.md): check whether a
  public sentence can be honestly supported by center and owner evidence.
- [Release Runbook](parts/release-runbook/README.md): keep GitHub release,
  changelog, tag, validation, and publication steps bounded.
- [Changelog Roadmap Split](parts/changelog-roadmap-split/README.md): keep
  released history, current direction, landing ledgers, and future intent in
  their proper homes.
- [Landing Closeout](parts/landing-closeout/README.md): close a wave, package,
  mechanic, checkpoint, or quest without leaving raw tails in active routes.
- [Owner Handoff Packet](parts/owner-handoff-packet/README.md): make a center
  transition portable as an owner-local request without claiming acceptance.
- [Sibling Evidence Route](parts/sibling-evidence-route/README.md): cite
  sibling truth without importing or overriding it.
- [Rollback Return](parts/rollback-return/README.md): preserve return and
  rollback paths before a transition is treated as stable.
- [Direction Surface Review](parts/direction-surface-review/README.md): decide
  whether README, ROADMAP, LANDING_LOG, CHANGELOG, or direction maps must change
  after a transition.

## Provenance boundary

Do not open historical or raw source material by default. Use
[PROVENANCE](PROVENANCE.md) when a transition needs source trace or old release
doctrine context.

## Active part contract

Every part keeps three working surfaces:

- `README.md`: when to use the part and where to start.
- `CONTRACT.md`: center boundary, allowed outputs, and stop-lines.
- `VALIDATION.md`: validation route, with executable commands centralized in
  `parts/AGENTS.md`.

A part may grow, split, merge, shrink, or retire when that improves its
function and keeps the route cleaner. The move should leave the active path
easier to follow, not merely smaller.

## Validation

Use the validation lane in [mechanics/release-support/AGENTS.md](AGENTS.md#validation)
for package commands and [parts/AGENTS.md](parts/AGENTS.md#validation) for part
commands.

# Release Support Mechanic

Release support is the center mechanic for honest state transitions. It names
when a draft, wave, checkpoint, quest, mechanic, handoff, public claim, or
repository release may be treated as portable, supportable, published, landed,
or rollback-bounded.

It does not turn unverified future work into public claims, and it does not
take operational truth from stronger owner repositories.

## Mechanic card

- Status: `landed`

### Trigger

Use when a transition claim, public claim, release surface, changelog, roadmap,
landing log, direction surface, support posture, owner handoff, checkpoint
closeout, quest closeout, audit route, or rollback route must be checked.

### Center owns

Center state-transition vocabulary, release posture, public claim boundaries,
federation release protocol, center release runbook, direction-surface routing,
changelog/roadmap/landing-log split, and owner handoff stop-lines.

### Stronger owner split

- Sibling repositories own their local release truth, implementation evidence,
  and acceptance receipts.
- Owning mechanics own their content, maturity, active parts, and landing logs.
- `aoa-evals` owns proof evidence for quality, regression, and public-claim
  support.
- `aoa-stats` owns derived release and transition movement summaries.
- `aoa-routing` owns route and entry ABI updates.
- `aoa-sdk` owns typed helper and compatibility support for release consumers.
- `8Dionysus` owns public projection after center and owner evidence align.
- `abyss-stack` owns runtime deployment and rollback truth.
- Generated surfaces reflect source truth but do not author release truth.

### Inputs

- Public claim, release note, roadmap change, direction update, landing log
  entry, mechanic maturity claim, quest or checkpoint closeout, audit finding,
  support statement, owner request, or rollback-sensitive transition.
- Source evidence sufficient to decide whether the center may support the
  transition claim.

### Outputs

- Supportable claim, state-transition gate, release checklist route,
  changelog/roadmap/landing-log destination, direction-surface update, audit
  route, owner handoff packet, rollback route, or stop-line.
- No unverified public claim, sibling acceptance claim, or substitution of
  roadmap history for changelog truth.

### Must not claim

- GitHub-only definition of release
- unverified public claim
- sibling release truth
- sibling acceptance without receipt
- roadmap history as changelog
- generated or derived release authority
- hidden rollback safety

### Validation

Use the validation lane in [AGENTS.md](AGENTS.md#validation).

### Next route

- For proof-dependent claims, route to `aoa-evals`; for sibling release truth
  or acceptance, route to the sibling repository.
- For derived movement summaries, route to `aoa-stats`; for route/entry ABI
  support, route to `aoa-routing`; for typed helper support, route to
  `aoa-sdk`; for public projection, route to `8Dionysus`; for runtime
  deployment or rollback, route to `abyss-stack`.
- For unclear owner, return to `docs/FEDERATION_RULES.md` and
  `docs/REPO_ROLES.md`.

## Start here

- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [parts/README](parts/README.md)
- [OWNER_MAP](OWNER_MAP.md)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)
- [PROVENANCE](PROVENANCE.md)
- [PUBLIC_SUPPORT_POSTURE](docs/PUBLIC_SUPPORT_POSTURE.md)
- [FEDERATION_RELEASE_PROTOCOL](docs/FEDERATION_RELEASE_PROTOCOL.md)
- [RELEASING](docs/RELEASING.md)
- [DIRECTION_SURFACES](docs/DIRECTION_SURFACES.md)
- [RELEASE_SUPPORT_OWNER_REPO_REQUESTS](docs/RELEASE_SUPPORT_OWNER_REPO_REQUESTS.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)

## Active parts

- [State Transition Gate](parts/state-transition-gate/README.md)
- [Public Claim Gate](parts/public-claim-gate/README.md)
- [Release Runbook](parts/release-runbook/README.md)
- [Changelog Roadmap Split](parts/changelog-roadmap-split/README.md)
- [Landing Closeout](parts/landing-closeout/README.md)
- [Owner Handoff Packet](parts/owner-handoff-packet/README.md)
- [Sibling Evidence Route](parts/sibling-evidence-route/README.md)
- [Rollback Return](parts/rollback-return/README.md)
- [Direction Surface Review](parts/direction-surface-review/README.md)

## Owner boundary

AoA owns transition law, public support boundaries, release posture, and
federation route discipline. Owner repositories own local implementation,
acceptance, proof, runtime state, and public projection receipts.

The card above is the compact route. The active parts explain how to apply the
mechanic. Generated card indexes may reflect this package, but they do not
author meaning.

## Growth posture

When this mechanic changes, keep active parts light and operational. Put source
trace in `PROVENANCE.md`, owner-local requests in `OWNER_REQUESTS.md`, proof in
`aoa-evals`, runtime in `abyss-stack`, projection in `8Dionysus`, and released
repository history in root `CHANGELOG.md`.

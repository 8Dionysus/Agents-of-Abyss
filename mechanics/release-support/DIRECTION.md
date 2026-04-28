# Release Support Direction

Release support treats release as a state transition, not only as a GitHub
event.

A release move happens when a surface leaves a working state and becomes
portable, supportable, handoff-ready, public, or rollback-bounded. This can be a
PR merge, a GitHub Release, a mechanic landing, a quest closeout, a checkpoint
bridge, a public README claim, an owner-request packet, or a sibling-repo
adoption route.

This file owns the current operating direction only. It does not replace the
part map, landing ledger, roadmap, owner-request packet, owner map, or
provenance bridge.

## Source-of-truth split

- `README.md`: package entry card and shortest route.
- `DIRECTION.md`: current operating direction.
- `PARTS.md`: active part map.
- `parts/`: concise release-support contracts.
- `OWNER_MAP.md`: stronger-owner split.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `LANDING_LOG.md`: canonical landing ledger.
- `ROADMAP.md`: future contour, not a historical ledger.
- `PROVENANCE.md`: the only active bridge back to source accounting.
- `docs/`: public support, release protocol, and direction-surface doctrine.

## Current contour

Release support is the center mechanic for honest transition claims:

- what moved from draft, wave, checkpoint, quest, or raw source into active use
- what evidence makes that move supportable
- what owner must carry local truth next
- what public claim is allowed now
- what remains planted, requested, blocked, or rollback-ready

It does not own the content of other mechanics. It owns the gate that says
whether a transition can be claimed, where the proof lives, where the handoff
goes, and what must remain unsaid.

## Transition types

- Internal landing: a mechanic, part, or source packet becomes active center
  doctrine.
- Mechanic maturity: a planted contour becomes landed after checks and owner
  boundaries are clear.
- Quest or checkpoint closeout: a working obligation or session state becomes a
  reviewed next route.
- Owner handoff: a center finding becomes a ready-to-carry owner request.
- Public claim: a sentence leaves internal context and becomes supportable in a
  public surface.
- GitHub release: a repository state is tagged, published, and described from
  the canonical changelog.
- Sibling adoption: an owner repository accepts, lands, and proves its local
  slice.
- Rollback or return: a transition keeps the path back visible before it is
  treated as stable.

## Growth rule

Add release-support detail only when it makes a transition more honest,
portable, or reversible. If a future improvement is certain but not needed now,
record the condition in `ROADMAP.md` rather than loading active parts with
speculation.

## Stop-lines

- No GitHub-only definition of release.
- No public claim without evidence and owner boundary.
- No sibling acceptance without sibling receipt.
- No roadmap history as changelog truth.
- No generated or derived surface as release authority.
- No hidden rollback debt.

## Next owner route

Proof routes to `aoa-evals`. Derived release visibility routes to `aoa-stats`.
Release routing routes to `aoa-routing`. Compatibility helpers route to
`aoa-sdk`. Public projection routes to `8Dionysus`. Runtime deployment truth
routes to `abyss-stack`. Mechanic-local content remains with the owning
mechanic.

## Validation

Use the validation lane in [mechanics/release-support/AGENTS.md](AGENTS.md#validation) for executable commands.

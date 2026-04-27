# AGENTS.md

## Applies to

This card applies to `mechanics/release-support/parts/` and every nested part.

## Role

Release-support parts are active operating routes for transition claims. They
should stay concise and functional. Historical context routes through
`../PROVENANCE.md`; owner-local action routes through `../OWNER_REQUESTS.md`.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`,
`mechanics/release-support/AGENTS.md`, `mechanics/release-support/DIRECTION.md`,
and the part being changed.

## Boundaries

- Do not put raw release history or old packets in active parts.
- Do not claim proof, sibling acceptance, runtime deployment, or public
  projection authority.
- Do not duplicate executable validation commands inside child part docs; route
  to this AGENTS card.
- Keep each part focused on the transition move it owns.

## Validation

Run the package validator after part changes:

```bash
python mechanics/release-support/scripts/validate_release_support_distillation.py
```

For release-facing changes, also run the release check named by the package
AGENTS card.

## Closeout

Name changed active parts, provenance sources consulted through
`PROVENANCE.md`, owner requests affected, checks run, checks skipped, remaining
risk, and the next owner route if the part was only a waypoint.

# Retire The Dionysus Seed Intermediary

- Decision ID: AOA-CENTER-D-0033

## Status

Accepted.

## Index Metadata

- Original date: 2026-07-25
- Surface classes: mechanic package, federation route, repository role
- Center facets: growth lineage, owner descent
- Mechanic parents: method-growth, checkpoint, distillation, growth-cycle, recurrence
- Guard families: sibling-owner boundary, owner-request queue, legacy isolation
- Posture: accepted supersession boundary

## Context

Decision `AOA-CENTER-D-0003` made a seed-stage intermediary explicit in the
growth-refinery chain:

`cluster_ref -> candidate_ref -> seed_ref -> object_ref`

That route was useful while candidate preparation needed a separate staging
surface. It no longer reflects current work. Reviewed candidates can move
directly into the final owner's intake and landing process, and keeping a
mandatory intermediary adds cost, duplicated state, and another authority
boundary without improving review quality.

At the same time, `Dionysus` has been rechartered around conversational
interview protocols and evidence-grounded, human-reviewed personal portrait
projections. Reusing that repository name for seed staging would couple its
current privacy-sensitive role back to an obsolete workflow.

## Options considered

1. Keep `Dionysus` as the mandatory seed intermediary for compatibility.
2. Move seed staging into another federation-wide repository.
3. Route reviewed candidates directly into owner-local intake and landing,
   while allowing owners to retain `seed_ref` only as local compatibility
   metadata.

## Decision

Choose option 3.

The canonical growth-refinery route is:

`cluster_ref -> candidate_ref -> owner-local intake -> object_ref`

`aoa-sdk` may carry provisional `cluster_ref`. `aoa-skills` may mint reviewed
`candidate_ref`. The final owner repository owns intake, acceptance, merge,
defer, drop, landing, and `object_ref`.

`seed_ref` is no longer a mandatory federation stage and has no
center-appointed repository owner. A final owner may preserve it as local
compatibility metadata, but it grants no acceptance or cross-repository
authority.

`Dionysus` has no seed intake, staging, dispatch, planting, checkpoint
snapshot, donor-preservation, or recurrence-packet role in the current
federation contour. Its current role is limited to public conversational
interview, consent, evidence, claim, review, and purpose-bounded personal
portrait projection protocols. Private raw interview material remains outside
Git.

Historical decisions, landing logs, provenance receipts, and repository-local
legacy material remain historical evidence. They do not form an active route,
owner request, validator dependency, or current role claim.

This decision supersedes only the current stage-ownership and route portion of
`AOA-CENTER-D-0003`. It does not rewrite that decision's historical context.

## Rationale

- Direct owner intake removes a cost-bearing intermediary without weakening
  review or provenance.
- The final owner is the only repository that can honestly accept, merge,
  defer, drop, or land its object.
- Owner-local compatibility metadata can survive without becoming federation
  architecture.
- Separating the retired seed role from the current portrait protocol avoids
  authority confusion and accidental access to privacy-sensitive material.
- Preserving historical evidence while removing active routes keeps the
  transition auditable without letting the legacy topology remain alive.

## Consequences

- Four open Dionysus owner requests are retired rather than transferred.
- Method-growth validation no longer reads a Dionysus sibling example.
- Checkpoint, distillation, growth-cycle, recurrence, and root ecosystem maps
  route intake and landing directly to the final owner.
- Existing historical receipts may still name the old topology; readers must
  treat them as historical evidence.
- Owners that keep `seed_ref` must document it as local compatibility
  metadata, not federation authority.

## Source surfaces

- `CHARTER.md`
- `ECOSYSTEM_MAP.md`
- `mechanics/method-growth/README.md`
- `mechanics/method-growth/docs/METHOD_SPINE.md`
- `mechanics/method-growth/docs/CANDIDATE_LINEAGE_CROSSWALK.md`
- `mechanics/owner-request-queue.json`
- `Dionysus/README.md`
- `Dionysus/AGENTS.md`

## Follow-up route

Final owner repositories should accept reviewed candidates through their own
intake and landing surfaces. Revisit this decision only if real cross-owner
evidence shows that direct intake loses reviewability or provenance; do not
restore a mandatory intermediary from compatibility pressure alone.

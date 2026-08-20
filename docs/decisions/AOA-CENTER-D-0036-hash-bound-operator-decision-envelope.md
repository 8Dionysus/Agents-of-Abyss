# Hash-Bound Operator Decision Envelope

- Decision ID: AOA-CENTER-D-0036

## Status

Accepted.

## Index Metadata

- Original date: 2026-07-28
- Surface classes: center contract, operator decision, federation boundary
- Center facets: constitutional authority, owner descent
- Mechanic parents: experience
- Guard families: operator authority, artifact binding, owner boundary
- Posture: accepted constitutional envelope

## Context

Cross-owner AI work needs a compact way for the sole human operator to decide
an exact reviewed artifact set. The decision must survive separated AI review
without letting an AI review run become the final authority, letting the center
absorb owner payload meaning, or letting a packet silently execute an effect.

The existing
`mechanics/experience/parts/office-operations/schemas/experience_operator_decision_v1.json`
is intentionally limited to an emergency stay. The existing governance packet
and governance decision schemas are tied to polis case and council flows and do
not bind a general operator choice to exact artifact-manifest bytes.

Without a distinct contract, future work would repeatedly choose between
misusing the emergency schema, weakening a polis-specific schema, or inventing
owner-local decision shapes that cannot be compared or audited.

## Options considered

1. Reuse the office-operations emergency-stay operator decision and widen its
   decision enum.
2. Extend the existing governance packet or governance decision into a generic
   cross-owner operator envelope.
3. Add a separate C25 `OperatorDecisionPacket` to the active
   `Experience / governance-polis` part while leaving payload meaning,
   validation, and effects with named owners.

## Decision

Choose option 3.

C25 is a constitutional envelope owned by `Agents-of-Abyss` under
`mechanics/experience/parts/governance-polis/`. It supports exactly
`approve`, `reject`, `defer`, `narrow`, and `quarantine`.

Every packet binds `artifact_set_id` and `artifact_manifest_ref` to an exact
`artifact_manifest_sha256`. If the owner resolver cannot supply that digest or
the bytes do not match, the outcome is `no_decision`.

The sole human operator is the final decision authority. Evidence review and
authority review are procedurally separated AI roles with distinct run refs;
they remain advisory. This separation does not imply another human reviewer.
One AI run cannot both finalize the choice and widen authority.

For `narrow`, the packet lists exact item refs and hashes. Other decisions
apply to the exact artifact set and carry no narrowed items. The packet itself
has no automatic effect. The named payload owner retains payload meaning and
validation, and the named effect owner must revalidate before acting.

## Rationale

A separate envelope protects the existing emergency-stay meaning and avoids
turning council/case governance records into a generic approval protocol.

Exact artifact binding makes the operator decision replayable against the
reviewed bytes instead of a mutable label. Procedurally separated AI review
fits the solo+AI operating model while preserving one human authority.

Keeping the packet effectless preserves federation law: the center owns the
constitutional decision shape, not memory semantics, proof verdicts, routing,
runtime execution, production admission, or another repository's payload.

## Consequences

- Operator decisions can be carried across owner boundaries with one stable,
  hash-bound constitutional shape.
- The emergency-stay operator schema remains narrow and unchanged.
- Consumers must resolve the artifact manifest and fail closed on a missing or
  mismatched digest.
- Two procedurally distinct AI review refs are required before the operator
  decision, adding review overhead in exchange for clearer role separation.
- `narrow` decisions require exact per-item refs and hashes.
- A packet is not execution, production admission, proof, memory authority, or
  policy widening; the next owner must revalidate and apply its own effect law.
- A correction or changed artifact set requires a new immutable packet and may
  cite the earlier packet through `supersedes_packet_ref`.

## Source surfaces

- `CHARTER.md`
- `DESIGN.md`
- `docs/FEDERATION_RULES.md`
- `mechanics/experience/parts/governance-polis/CONTRACT.md`
- `mechanics/experience/parts/governance-polis/schemas/operator_decision_packet_v1.json`
- `mechanics/experience/parts/office-operations/schemas/experience_operator_decision_v1.json`

## Follow-up route

Named payload owners validate their extension and exact artifact manifest.
Named effect owners revalidate the packet and apply their own admission and
rollback contracts. `aoa-evals` may evaluate decision quality but cannot author
the decision; `aoa-memo` may retain a reviewed reference but cannot turn it
into memory authority. Revisit this decision only if the operator set, hash
binding, or center-versus-owner authority split changes.

# OS Abyss Artifact Trust Plane

- Decision ID: AOA-CENTER-D-0030

## Status

Accepted.

## Index Metadata

- Original date: 2026-06-21
- Surface classes: center doctrine, federation contract, repository routing
- Center facets: federation boundary, organ alignment
- Mechanic parents: none
- Guard families: center route law, sibling-owner boundary, release/tooling
- Posture: accepted rationale

## Context

OS Abyss artifact trust work now spans ABI signatures, SBOM/ML-BOM,
SLSA/in-toto provenance, Sigstore/Cosign, C2PA, TUF-style update metadata,
future SCITT transparency, durable host evidence, repo producer profiles, SDK
typed access, eval proof, and session-memory routing.

The repeated fork is whether this should be treated as a GitHub/CI signing
policy, as an `abyss-machine` implementation detail, as an SDK API shape, or
as center doctrine. None of those choices alone can carry the system. The
trust plane must work for host/runtime/workspace consumption as well as for
GitHub release adapters.

## Options considered

1. Make GitHub Actions and release attestations the primary trust plane.
2. Make `abyss-machine` the only source of truth for the whole trust model.
3. Put artifact trust doctrine in the center while leaving enforcement,
   evidence, typed access, proof, and producer artifacts with their owner
   organs.

## Decision

Agents-of-Abyss names the OS-level artifact trust contract
`os_abyss_artifact_trust_plane_v1`.

The contract is a hybrid authority split:

- `Agents-of-Abyss` owns center doctrine, owner split, and federation stop-lines.
- `abyss-machine` owns host enforcement, durable registry, trust gates, trust
  root modes, update/transparency lane, and installed/runtime checks.
- `.aoa` owns session evidence routing, rehydration, indexes, graph/session
  memory projections, and generated/export surfaces when they become
  machine-consumable artifacts.
- `aoa-sdk` owns typed read/assert access to trust-plane JSON surfaces.
- `aoa-evals` owns proof scenarios and regression claims.
- source-owner repositories own producer artifacts, sidecars, release/export
  triggers, and owner-local validators.

GitHub Actions, GitHub OIDC, GitHub Releases, OCI registries,
Sigstore/Cosign, SLSA/in-toto, C2PA, SBOM/ML-BOM, TUF, and future SCITT lanes
are adapters or evidence layers selected by artifact class. They are not the
trust plane by themselves.

## Rationale

Artifact trust is a consumer-safety boundary, not only a release-signing
feature. Agents, installers, runtime consumers, release consumers, and repo
workflows need the same high-level rule: detect artifact class, inspect
requirements, produce or locate evidence, pass a trust gate, check drift, and
only then consume or land.

The center should name that rule because it is cross-repo doctrine. But the
center must not mutate host registries, choose release artifacts for sibling
repos, score proof, or turn session memory into policy. Splitting authority
keeps each organ strong:

- host decisions stay close to installed/runtime state;
- typed SDK access stays usable without becoming enforcement;
- proof claims stay reviewable in `aoa-evals`;
- `.aoa` remains routing and rehydration, not law;
- source-owner repositories can refactor while drift stays visible.

## Consequences

- The first center source surface for this contract is
  `docs/FEDERATION_RULES.md`.
- `docs/REPO_ROLES.md` carries the compact route table for humans and agents.
- `abyss-machine` remains the required owner for durable registry,
  trust-gate, trust-root, affected/drift, update-lane, and installed parity
  behavior.
- `aoa-sdk` can expose typed trust-plane readers, but consumers must still
  treat `abyss-machine` verdicts as the host enforcement result.
- `aoa-evals` should carry proof scenarios for positive and negative
  trust-plane behavior.
- GitHub-native signing and OIDC work must be described as producer adapters,
  not as the whole OS Abyss trust model.

Residual risk: a future agent may still try to duplicate host policy in the
center. The stop-line is explicit: the center names owner split and consumer
doctrine, while implementation and proof stay with the owning organ.

## Source surfaces

- `docs/FEDERATION_RULES.md`
- `docs/REPO_ROLES.md`
- `docs/LAYERS.md`
- `docs/organ-contract/README.md`
- `abyss-machine` artifact policy, bundle registry, trust-gate, affected, and
  trust-coverage surfaces
- `.aoa` session evidence and rehydration surfaces
- `aoa-sdk` typed artifact trust API surfaces
- `aoa-evals` artifact-bundle and proof surfaces

## Follow-up route

Use `abyss-machine` for host enforcement and durable evidence work, `aoa-sdk`
for typed access, `aoa-evals` for proof scenarios, `.aoa` for session evidence
routing, and source-owner repositories for producer profile and artifact
sidecar work. Return to Agents-of-Abyss only when the OS-level owner split or
federation stop-line changes.

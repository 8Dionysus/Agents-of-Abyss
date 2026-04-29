# Decision Note: `aoa-stats` Is Part Of The Public Federation Contour

Status: accepted
Date: 2026-04-09

## Context

The center doctrine already treated `aoa-stats` as the owner of derived views in antifragility work, and `aoa-stats` itself already owns a coherent object class: machine-first summary surfaces, derived windows, and the shared stats event envelope.

But the center's compact public contour still excluded `aoa-stats` from `CHARTER.md`, `ECOSYSTEM_MAP.md`, `ROADMAP.md`, and `generated/ecosystem_registry.min.json`.
That drift created a false ambiguity:

- doctrine named `aoa-stats`
- the machine-readable public registry did not
- readers could not tell whether `aoa-stats` was a real public layer or only a sidecar experiment

## Options considered

1. Keep `aoa-stats` outside compact registry v1 as a supporting or later-wave surface.
2. Promote `aoa-stats` now as a public derived layer with explicit anti-authority boundaries.

## Decision

AoA now treats `aoa-stats` as a public federation layer.

The center records it as the **derived observability layer** and includes it in the compact public contour:

- `CHARTER.md`
- `ECOSYSTEM_MAP.md`
- `ROADMAP.md`
- `docs/LAYERS.md`
- `docs/REPO_ROLES.md`
- `generated/ecosystem_registry.min.json`

This promotion does **not** turn `aoa-stats` into:

- proof authority
- routing authority
- quest-state authority
- a sovereign score surface

Its registry posture stays intentionally modest:

- `status=bootstrap`
- `shared_maturity=seed`
- `kind=derived`

## Rationale

- `aoa-stats` already owns real published contracts and generated surfaces.
- The center was already depending on `aoa-stats` doctrine in antifragility notes.
- Excluding it from compact registry v1 made the public contour less honest, not safer.
- Keeping `aoa-sdk` outside compact registry v1 remains correct because `aoa-sdk` is still a supporting consumer/control-plane surface rather than a public layer in the contour.

## Consequences

- Center docs and validator-backed registry checks must now treat `aoa-stats` as part of the documented public federation contour.
- The supporting inventory remains for non-public supporting surfaces such as `aoa-sdk`.
- Future center edits must preserve the boundary that `aoa-stats` derives and summarizes movement without replacing source-owned meaning or bounded proof.

## Source surfaces

- `CHARTER.md`
- `ECOSYSTEM_MAP.md`
- `ROADMAP.md`
- `docs/LAYERS.md`
- `docs/REPO_ROLES.md`
- `generated/ecosystem_registry.min.json`

## Follow-up route

Route future proof or score-sovereignty pressure to `aoa-evals`, `aoa-stats`,
and the owning source repository before changing center public-layer posture.

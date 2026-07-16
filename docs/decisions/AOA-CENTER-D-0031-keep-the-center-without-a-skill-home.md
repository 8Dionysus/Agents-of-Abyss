# Keep The Center Without A Skill Home

- Decision ID: AOA-CENTER-D-0031

## Status

Accepted.

## Index Metadata

- Original date: 2026-07-16
- Surface classes: agent guidance, repository topology, projection boundary
- Center facets: federation boundary, agent guidance
- Mechanic parents: none
- Guard families: owner boundary, prompt visibility, manual admission
- Posture: accepted no-home boundary

## Context

`Agents-of-Abyss` carried 25 copied shared bundles under `.agents/skills/`
without a canonical top-level `skills/` home or an owner-admission decision.
Ten of those legacy bundles entered the prompt-visible repository skill list.
One root test also executed a helper from the copied
`aoa-local-stack-bringup` bundle, turning foreign workflow implementation into
an accidental center contract.

The center charter routes executable workflow truth to `aoa-skills`, typed
helpers to `aoa-sdk`, and runtime implementation to `abyss-stack`. Session
evidence located only generic repository cleanup around this owner, not a
repeated center-specific procedure with its own trigger, ABI, composition
value, and verified benefit.

## Options considered

1. Keep refreshing the copied shared catalog under `.agents/skills/`.
2. Create a top-level `skills/` port and promote center routing or local-stack
   guidance into a home bundle for structural symmetry.
3. Remove the copied catalog, keep no skill home, and admit one later only
   after owner-specific manual evidence proves independent value.

## Decision

Choose the third option.

`Agents-of-Abyss` has no top-level `skills/` home and no
`.agents/skills/` projection while it has no admitted owner capability. Shared
AoA skills are supplied by the host-selected user profile and remain authored
in `aoa-skills`.

If a future center-specific candidate emerges, admit it through a separate
owner decision only after manual positive, negative, no-skill, and coexistence
trials demonstrate a stable trigger, distinct input and output contract,
independent composition value, and held-out benefit. Only then may a canonical
top-level home and its exact derived repository projection be created.

The root test suite must exercise center-owned behavior. It must not import a
shared skill helper merely because a copied projection is present.

## Rationale

The center already owns concise route and stop-line sources that let an agent
locate stronger owners. Turning those documents into another skill would
duplicate execution truth and add a competing prompt entry without proving a
new capability. A manual local-stack routing task reached the correct owner
from the source surfaces after the repository copies were removed.

Removing the projection also prevents stale shared copies from silently
becoming implementation dependencies. The absence of a `skills/` directory is
intentional evidence that no home capability has yet crossed the admission
threshold, not an unfinished port.

This decision narrows the older description of `.agents/` in
AOA-CENTER-D-0027: the Spark placement remains current, but shared skill
catalogs are not repository-local agent assets.

## Consequences

- Twenty-five foreign bundles and ten prompt-visible legacy entries leave this
  repository.
- Shared skills remain available through the user profile without a second
  repository copy.
- `.agents/` continues to own Spark and other local agent assets, but not
  authored shared skill truth.
- KAG repository indexes must be regenerated so removed projection artifacts
  no longer appear as current entities or anchors.
- A future home skill requires new evidence and a new owner decision rather
  than restoration of this catalog.

## Source surfaces

- `AGENTS.md`
- `CHARTER.md`
- `docs/REPO_ROLES.md`
- `.agents/AGENTS.md`
- `tests/test_agents_mesh.py`
- `aoa-skills` decision `AOA-SK-D-0040`
- `aoa-skills` decision `AOA-SK-D-0041`

## Follow-up route

Regenerate the center decision and KAG indexes, validate the repository, and
repeat a clean prompt-visible routing trial after landing. Return here only if
an owner-specific center capability later satisfies the manual admission
contract.

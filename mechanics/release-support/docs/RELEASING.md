# Releasing `Agents-of-Abyss`

This repository is the constitutional center of the AoA federation.

Its release flow is repo-local, but it also anchors the shared federation release doctrine.

For non-GitHub transition claims, use the active release-support parts before
touching this runbook. This file is the center GitHub release route, not the
whole definition of release.

See also:

- [Federation Release Protocol](FEDERATION_RELEASE_PROTOCOL.md)
- [Public Support Posture](PUBLIC_SUPPORT_POSTURE.md)
- [CHANGELOG](../../../CHANGELOG.md)

## Release goals

A center release should make it easy to answer:

- what changed in the center itself
- which federation release rules or surfaces changed
- how the center claims were revalidated
- what still belongs in sibling repos rather than the center
- which internal state transitions became supportable, landed, public,
  requested, or rollback-bounded

## Recommended release flow

1. Keep the scope bounded to center-owned meaning.
2. Update `CHANGELOG.md` with a latest tagged section in the `Summary / Validation / Notes` shape.
3. Run the repo-level release verifier:
   - use [release-support docs AGENTS](AGENTS.md#validation) for the executable command.
4. Run the federation preflight audit when the center release is part of a wider release pass:
   - `aoa release audit /srv --phase preflight --repo Agents-of-Abyss --strict --json`
5. Merge the release-prep PR to `main`.
6. Publish through the bounded control-plane helper:
   - `aoa release publish /srv --repo Agents-of-Abyss --dry-run --json`
   - `aoa release publish /srv --repo Agents-of-Abyss --confirm --json`
7. Re-run the postpublish audit:
   - `aoa release audit /srv --phase postpublish --repo Agents-of-Abyss --strict --json`

## Notes

- The center may define federation release doctrine, but it must not absorb sibling repo release meaning.
- The center release verifier stays repo-owned and bounded.
- Mechanic landings, quest closeouts, checkpoint bridges, and owner requests
  may be release-support transitions without being GitHub Releases.

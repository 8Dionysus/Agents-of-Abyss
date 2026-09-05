# Current Owner Routes Without Historical Tree Scaffolding

- Decision ID: AOA-CENTER-D-0044

## Status

Accepted.

## Index Metadata

- Original date: 2026-09-04
- Surface classes: agent guidance, mechanics topology, provenance, validation
- Center facets: source history, active owner routes
- Mechanic parents: agon, antifragility, audit, boundary-bridge, distillation, experience, questbook, release-support, rpg
- Guard families: source/history preservation, active part contracts, receipt indirection
- Posture: accepted source-tree retirement; no constitutional or owner-authority change

## Context

Spark instructions and historical mechanics trees remain beside active parts,
although those parts already own the current contracts. Archive-only presence,
raw accounting, and instruction scaffolding became a recurring validation cost.
History is useful evidence, but keeping it in every checkout is not necessary
for either provenance or current contract validation.

## Options considered

1. Keep the historical files and all archive-presence obligations.
2. Move the same files into another archive directory in the current tree.
3. Preserve exact Git recovery and retain only useful current contracts locally.

## Decision

Retire the listed Spark and mechanics legacy subtrees. Preserve their original
paths and bytes at the recorded commit; do not recreate them in another active
archive or a new archive service. Current work starts from the existing owner
cards and active part contracts. Historical investigation uses PROVENANCE.md
and an immutable source reference only when history is material.

Experience provenance receipt IDs, owners, active consumers, and must-not-claim
boundaries remain unchanged. Historical source_ref destinations become pinned
GitHub blob URLs. The receipt validator retains local missing-file checks and
requires a full commit plus a literal mechanics path for same-owner historical
URLs. Active artifacts continue to cite receipt IDs, not historical raw paths.

Keep active artifact maps, registry and schema contracts, generated-currentness,
owner-request boundaries, and active-part hygiene tests. Retire only checks
whose sole purpose was keeping an archive scaffold or historical raw payload
in the current tree. Historical landing-log entries remain historical; their
presence no longer requires the old files to remain on disk. The Questbook
first-wave inventory is historical, not a current owner allowlist.

This changes historical placement and its exclusive validation obligations,
not constitutional law, active mechanic semantics, proof, routing, role,
memory, runtime, or stronger-owner authority. Prior placement decisions retain
their recorded rationale; their local archive-presence requirements are
superseded by the exact recovery contract here.

## Rationale

Current source and historical evidence have different access needs. A small
active provenance bridge preserves source return without loading another
instruction mesh or imposing archive-only tests on every edit.

## Source surfaces

Exact source commit: `d31882083296ef457a980d071f55d609e95cce67`. All 368 tracked blobs were verified before retirement.

| Retired subtree | Historical source | Files |
| --- | --- | ---: |
| `.agents/spark/` | [Snapshot](https://github.com/8Dionysus/Agents-of-Abyss/tree/d31882083296ef457a980d071f55d609e95cce67/.agents/spark) | 54 |
| `mechanics/agon/legacy/` | [Snapshot](https://github.com/8Dionysus/Agents-of-Abyss/tree/d31882083296ef457a980d071f55d609e95cce67/mechanics/agon/legacy) | 113 |
| `mechanics/antifragility/legacy/` | [Snapshot](https://github.com/8Dionysus/Agents-of-Abyss/tree/d31882083296ef457a980d071f55d609e95cce67/mechanics/antifragility/legacy) | 5 |
| `mechanics/audit/legacy/` | [Snapshot](https://github.com/8Dionysus/Agents-of-Abyss/tree/d31882083296ef457a980d071f55d609e95cce67/mechanics/audit/legacy) | 11 |
| `mechanics/boundary-bridge/legacy/` | [Snapshot](https://github.com/8Dionysus/Agents-of-Abyss/tree/d31882083296ef457a980d071f55d609e95cce67/mechanics/boundary-bridge/legacy) | 3 |
| `mechanics/distillation/legacy/` | [Snapshot](https://github.com/8Dionysus/Agents-of-Abyss/tree/d31882083296ef457a980d071f55d609e95cce67/mechanics/distillation/legacy) | 4 |
| `mechanics/experience/legacy/` | [Snapshot](https://github.com/8Dionysus/Agents-of-Abyss/tree/d31882083296ef457a980d071f55d609e95cce67/mechanics/experience/legacy) | 154 |
| `mechanics/questbook/legacy/` | [Snapshot](https://github.com/8Dionysus/Agents-of-Abyss/tree/d31882083296ef457a980d071f55d609e95cce67/mechanics/questbook/legacy) | 6 |
| `mechanics/release-support/legacy/` | [Snapshot](https://github.com/8Dionysus/Agents-of-Abyss/tree/d31882083296ef457a980d071f55d609e95cce67/mechanics/release-support/legacy) | 4 |
| `mechanics/rpg/legacy/` | [Snapshot](https://github.com/8Dionysus/Agents-of-Abyss/tree/d31882083296ef457a980d071f55d609e95cce67/mechanics/rpg/legacy) | 14 |

Recover a file with `git show <full-source-commit>:<original-path>`. Historical
relative links belong to that exact tree. Normal CI does not download history
or reconstruct archives; the pre-retirement inventory verified recovery.

## Consequences

- Current navigation and derived indexes lose retired source-file entries.
- Historical investigation explicitly retrieves the recorded source.
- Provenance receipt indirection and current owner contracts remain enforced.
- Source changes require canonical registry/index regeneration, not hand edits.

## Follow-up route

Run active mechanic and full center gates, review cross-owner references and
all prepared owner branches, then merge at the coordinated final barrier.
Local checks do not claim runtime use, proof, release, or owner acceptance.

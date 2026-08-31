# Separate Inherited Agent Routes From Human README Surfaces

- Decision ID: AOA-CENTER-D-0042

## Status

Accepted.

## Index Metadata

- Original date: 2026-08-31
- Surface classes: agent guidance, public contour, validation guard, decision record
- Center facets: agent guidance, federation contour
- Mechanic parents: cross-mechanic
- Guard families: AGENTS/mesh, prompt visibility, docs hygiene, link/shape hygiene
- Posture: accepted role separation; removal remains evidence-gated and owner-local

## Context

The center grew `README.md` and `AGENTS.md` as paired local doors. Their roles
then blurred: inherited agent cards repeated human explanation, command
catalogs, and reading lists, while many cards required the nearest README even
when the README was unrelated to the current edit. At the measured baseline,
43 of 65 agent cards imposed README reading and the registered inherited chain
reached 40,883 bytes. `AOA-CENTER-D-0041` removed the largest repeated mechanic
command matrices, but it deliberately did not decide the role of the remaining
README/AGENTS corpus.

The README files are not interchangeable boilerplate. Some are public or human
entrypoints, usage guides, package maps, provenance bridges, or compatibility
routes. Others are empty doors, duplicated maps, generated fixtures, or local
procedure that has a stronger owner surface. A byte count or filename pairing
cannot distinguish those roles.

Future agents need the role boundary and the evidence required for removal.
A commit summary would show which files changed, but would not preserve why a
shorter inherited card must not be achieved by moving human documentation into
the prompt or by deleting human navigation wholesale.

## Options considered

1. Keep paired README/AGENTS files and unconditional local README reading as the
   default convention.
2. Delete most nested README files and move their useful material into nearby
   AGENTS cards.
3. Make AGENTS cards prompt-light inherited route law, keep README files as
   on-demand human/public surfaces, and classify every file before slimming,
   merging, generating, or deleting it.
4. Replace both file classes with generated maps and machine registries.

## Decision

Choose option 3.

An `AGENTS.md` card carries only the inherited local delta needed to act safely:
its scope, owner boundary, local risk, stop-lines, stronger source routes,
validation route, and closeout or handoff expectations. It must not become a
general overview, command catalog, changelog, complete package inventory, or a
copy of source doctrine. It may route to a README when that human surface is
actually relevant, but it must not require README reading merely because the
file exists nearby.

A `README.md` is an on-demand human or public surface. It may explain purpose,
usage, navigation, examples, provenance, compatibility, or the relationship
between stronger sources. It is not automatically prompt context and it does
not gain semantic authority from its conventional filename.

Current semantic meaning remains with the authored owner source or contract.
Machine topology remains with schemas, manifests, and registries. Exact
procedure belongs in an owner `VALIDATION.md`, validated manifest, runner, or
other named procedure surface. Generated views remain reproducible derivatives
that point back to their sources.

This placement supersedes only the part of `AOA-CENTER-D-0041` that retained a
compact executable entrypoint in the nearest `AGENTS.md` or routed a
`VALIDATION.md` back through that inherited card. `AOA-CENTER-D-0041` continues
to own the validated `mechanics/validation-routes.json` command manifest, the
no-shell exact-surface runner, nearest-owner binding, route integrity checks,
and inherited-chain budget. An `AGENTS.md` names the validation surface or lane;
the on-demand validation surface names the exact runner invocation.

Keep the repository root README by default because it is the public civic front
door. For every other README and AGENTS file, record an owner-aware disposition
before changing or removing it. The review must account for human/public
navigation, incoming links, unique content, source and generator relationships,
prompt-chain cost, validation, fixtures, and compatibility callers. Size,
similarity, pairing, or a low-content appearance is not sufficient evidence for
deletion.

Removal is allowed only after unique function is absent or moved to the correct
stronger surface, callers and derived views are updated, and the affected owner
checks are green. A placeholder may be removed when it promises no implemented
surface and carries no unique route, provenance, compatibility, or test-fixture
role. An unresolved file stays explicitly blocked rather than being normalized
by assumption.

## Rationale

Option 1 preserves avoidable prompt pressure and makes a filename convention
stronger than task relevance. Option 2 reduces file count while moving the
wrong material into inherited context and risks breaking human entrypoints.
Option 4 makes compact navigation possible but cannot replace authored
explanation, public expectations, or owner judgment.

The chosen split makes context cost proportional to the touched lane while
preserving the human paths that do real work. It also keeps authority legible:
agent cards route, README files explain, owner sources define, procedure
surfaces execute, and generated views compress. Per-file classification is more
work than a bulk rewrite, but it is the evidence that makes deletion safe.

## Consequences

- Root and local AGENTS cards can become smaller without hiding stop-lines or
  moving source truth into prompts.
- Human readers retain public entrypoints, usage paths, package maps, and
  provenance routes where those functions are real.
- A local README is no longer mandatory reading by convention; a card must name
  the reason and route when it needs one.
- Command blocks and long procedures move to owner procedure surfaces, while a
  compact validation route remains discoverable from the nearest card.
- Validators and corpus reports must measure inherited-chain pressure and
  mandatory-read fanout, but the measurements do not decide semantic value.
- Deletions require link, generator, registry, fixture, and compatibility
  review. Ambiguous cases remain visible debt.
- The center owner pass may remove obsolete placeholders and duplicate route
  doors, but it must not claim cross-repository completion; the AbyssOS corpus
  ledger and each sibling owner retain that integration boundary.

## Source surfaces

- `DESIGN.AGENTS.md`
- `AGENTS.md`
- `docs/ROOT_SURFACE_LAW.md`
- `docs/START_HERE_ROUTE_CONTRACT.md`
- `docs/guardrails/AGENTS_MESH_PROTOCOL.md`
- `docs/guardrails/README_AGENTS_CORPUS_PROTOCOL.md`
- `config/agents_mesh.json`
- `mechanics/validation-routes.json`
- `scripts/agents_mesh/`
- `scripts/mechanics_topology/`

## Follow-up route

Land the current corpus law, owner census, dispositions, validators, and tests
through the center owner pass. Rebuild decision, AGENTS-mesh, center-entry, and
KAG-derived views only from their owner sources. Keep the cross-repository
README/AGENTS ledger as the integration surface, and do not merge an owner pass
before the global AbyssOS barrier and dependency-ordered merge wave allow it.

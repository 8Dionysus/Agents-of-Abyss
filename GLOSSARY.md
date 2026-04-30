# AoA Glossary

This glossary defines the compact working vocabulary used at the AoA ecosystem
center.

It should stay aligned with `CHARTER.md`, `ECOSYSTEM_MAP.md`,
`docs/FEDERATION_RULES.md`, `docs/LAYERS.md`, `docs/REPO_ROLES.md`,
`docs/ROOT_SURFACE_LAW.md`, `docs/START_HERE_ROUTE_CONTRACT.md`, and
`mechanics/README.md`.

It is not a replacement for those documents. It gives short definitions and
routes, not full doctrine.

## Center and federation vocabulary

### Agents of Abyss (AoA)

A modular operational federation of explicit layers used to build, route, validate, remember, and run long-horizon agentic systems.

AoA grows as a federation rather than one swollen repository.

### Federation

A set of distinct but coordinated repositories with explicit ownership boundaries.

A federation stays healthy when every layer can grow without stealing another layer's truth.

### Polis

The constitutional city-center of the federation.

In the current public AoA surface, `Agents-of-Abyss` is the polis: it names, maps, governs, audits, and routes the federation without becoming every district.

### Ecosystem center

The repository that names, maps, and governs the federation at a high level.

In the current public AoA surface, this role belongs to `Agents-of-Abyss`. The center owns ecosystem-level truth, not the primary meaning of every layer-owned object.

### Layer

A distinct functional surface with its own role, boundaries, and ownership.

A good layer answers one main kind of question clearly and avoids quietly absorbing neighboring roles.

### District

A local region inside a repository, usually a top-level directory such as `scripts/`, `schemas/`, `generated/`, `quests/`, or `manifests/`.

A district should have a local README gate when its files are numerous, machine-facing, or easy to confuse.

### Root surface

A file or directory visible at repository root.

Root surfaces must justify civic visibility through `docs/ROOT_SURFACE_LAW.md`.

### Civic surface

A root-level surface that helps humans, agents, contributors, validators, or neighboring repositories orient before entering deeper districts.

Examples include `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `ROADMAP.md`, `GLOSSARY.md`, `QUESTBOOK.md`, and `ECOSYSTEM_AUDIT_INDEX.md`.

### Thin civic index

A compact root surface that routes to deeper canonical docs without duplicating them.

A thin index should stay small enough to remain an entrance, not become a second doctrine corpus.

### Landing receipt

A historical seed, package, or landing record that shows what was planted, why
it belonged, and how it was validated.

Landing receipts belong under the owning `mechanics/<slug>/legacy/raw/` route
when a mechanic owns them, or under `docs/traces/` for generic movement
evidence. They do not belong at repository root.

### Audit artifact

A reviewable cleanup, drift, pruning, or verification artifact.

Audit route grammar belongs under `mechanics/audit/`. Historical audit receipts
belong under `mechanics/audit/legacy/raw/` unless another owner has a more
specific legacy route. Compact root indexes such as `ECOSYSTEM_AUDIT_INDEX.md`
may stay flat only while they remain route surfaces.

### Source repository

A repository that authoritatively owns the primary meaning of a specific object class.

Examples include `aoa-techniques` for techniques, `aoa-skills` for skills, `aoa-evals` for evals, `aoa-memo` for memory objects, `aoa-agents` for role contracts, and `aoa-playbooks` for scenario composition.

### Source of truth

The canonical home of meaning for a given object class.

Coordination, routing, generated, and derived layers should not quietly replace source repositories.

### Coordination repository

A repository that helps readers or systems navigate across layers without owning all primary meaning itself.

`Agents-of-Abyss` is the ecosystem-center coordination repository. `aoa-routing` is a lighter navigation-oriented coordination layer.

### Derived layer

A layer that transforms or projects authoritative sources without becoming their authored home.

Derived layers may accelerate retrieval, comparison, or orientation, but they must remain visibly downstream of source-owned meaning.

### Supporting consumer

A repository or package that consumes AoA surfaces, provides typed helpers, or supports local orchestration without becoming a compact registry member or constitutional authority.

`aoa-sdk` currently fits this posture.

### Adjacent system anchor

A neighboring repository that is structurally central to AoA but not owned as an AoA layer.

In the current public ecosystem, `Tree-of-Sophia` and `abyss-stack` are adjacent system anchors.

### Public projection surface

A public-facing orientation surface that summarizes, routes, or projects selected AoA meaning without owning the underlying truth.

The `8Dionysus` profile surface is a public projection surface.

### Anti-collapse

A boundary rule that keeps neighboring surfaces from being merged by metaphor, convenience, or hidden ownership drift.

The center should enforce anti-collapse discipline whenever routing, memory, counterpart mapping, or derived substrate work starts to impersonate source-owned meaning.

## Current public layers

### Practice canon

The layer that stores reusable engineering practice.

In the current public ecosystem, this role belongs to `aoa-techniques`. Its main question is: what practice is genuinely reusable?

### Execution canon

The layer that stores bounded agent-facing execution workflows.

In the current public ecosystem, this role belongs to `aoa-skills`. Its main question is: how should an agent execute bounded work?

### Proof canon

The layer that stores portable proof surfaces for bounded claims.

In the current public ecosystem, this role belongs to `aoa-evals`. Its main question is: what bounded claim can we honestly support?

### Navigation layer

The layer that helps humans and models decide where to go next.

In the current public ecosystem, this role belongs to `aoa-routing`. It should route and dispatch rather than become the primary authoring home of other layers.

### Memory layer

The layer that owns explicit memory and recall surfaces.

In the current public ecosystem, this role belongs to `aoa-memo`. It should own memory objects, recall posture, and provenance-aware retrieval rather than practice or proof truth.

### Agent layer

The layer that defines explicit role contracts, persona boundaries, and handoff posture.

In the current public ecosystem, this role belongs to `aoa-agents`. Its main question is: who acts, and under what role contract?

### Scenario-composition layer

The layer that packages recurring multi-layer operational scenarios.

In the current public ecosystem, this role belongs to `aoa-playbooks`. It should own readable cross-layer routes rather than silently replace the bounded execution canon.

### Derived knowledge substrate

The layer that lifts authoritative sources into graph-ready or retrieval-ready derived structures.

In the current public ecosystem, this role belongs to `aoa-kag`. It must remain derived and provenance-aware rather than become a new empire of authored meaning.

### Infrastructure substrate

The layer that runs the body of the system.

In the current public ecosystem, this role belongs to `abyss-stack`. It owns runtime, deployment, storage, and service composition, but it does not author AoA constitutional truth or ToS-authored knowledge truth.

### Knowledge architecture counterpart

The source-first knowledge world that AoA helps build, maintain, validate, and route around.

In the current public ecosystem, this role belongs to `Tree-of-Sophia`. It is an adjacent anchor rather than an AoA-owned layer.

## Working objects and routes

### Technique

A minimal reproducible unit of engineering practice.

A technique should have explicit intent, boundaries, risks, validation posture, and adaptation notes. It is more durable than a one-off fix.

### Skill

A bounded agent-facing execution workflow.

A skill packages one or more techniques into an operational surface with clear trigger boundaries, procedures, risks, and verification guidance.

### Method

A recurring scenario-level route that composes skills, roles, memory posture, fallback posture, and proof hooks into one readable pattern.

Public method belongs primarily in playbooks rather than being smeared across neighboring layers.

### Playbook

The readable scenario-owned surface that packages method.

A playbook may compose techniques, skills, roles, routing, memory posture, evaluation posture, handoffs, fallback paths, and expected evidence. A playbook is not a single skill.

### Eval

A bounded proof surface for a specific claim.

An eval should make its scope, object under evaluation, verdict logic, and blind spots explicit.

### Routing

A lightweight navigation and dispatch surface that helps humans and models choose the right next object.

Routing may aggregate, compress, and point. It should not become the primary source of truth for other layers.

### Memory object

An explicit, reviewable unit of memory.

A memory object should preserve provenance and temporal context where possible. It should not silently impersonate proof or authored source truth.

### Role

A bounded operational identity that states who acts, what posture it carries, and where it should hand off.

Roles are owned by `aoa-agents`.

### Agent

A role-bearing actor in the AoA ecosystem.

An agent is not a skill. An agent uses skills under a role contract, memory posture, evaluation posture, and handoff posture.

### Handoff

The explicit transfer of work, context, or responsibility between roles or layers.

Good handoff posture reduces ambiguity and keeps authority boundaries visible.

### Memory posture

The declared way an agent or workflow should interact with memory surfaces.

A good memory posture names whether memory is required, optional, bounded, or restricted.

### Evaluation posture

The declared way an agent, workflow, or playbook relates to proof and verification.

A good evaluation posture names what should be checked, how strongly, and under which limits.

### Capsule

A compact agent-friendly summary surface derived from a larger canonical bundle.

A capsule should accelerate routing and decision-making without replacing the full source bundle.

### Registry

A compact machine-readable surface that names and normalizes a repository's public objects.

A registry is not the whole meaning of a repository. It is a smaller structured surface for validation, routing, or indexing.

### Generated surface

A derived artifact built from authoritative source files.

Generated surfaces improve navigation, indexing, or local runtime use, but they should not silently replace the source of truth.

### Schema

A machine-readable shape contract.

A schema checks whether an artifact is shaped correctly. It does not prove that the artifact should exist or that its meaning is true.

### Validator

A script that checks a contract, generated surface, or bounded repository invariant.

A validator is a guardrail, not a source of meaning.

### Provenance

A readable account of where an object, memory, or claim came from and how it was shaped.

In AoA, provenance matters because memory, routing, eval, and derived substrate work should stay tied to stronger authored sources.

### Bounded claim

A claim that states what is supported, under what conditions, and with what limits.

AoA prefers bounded claims over vague global assertions.

## Route and evidence vocabulary

### Route mode

A named entry route from `docs/START_HERE_ROUTE_CONTRACT.md`.

Route modes help a reader choose the right first surface before a change widens
into root editing, direction change, ownership routing, mechanic work, public
claim validation, low-context routing, or district work.

### Entry surface

A first-contact document, generated capsule, or route file used to enter a
bounded part of the repository.

Entry surfaces should point to stronger local truth rather than carrying every
detail themselves.

### Decision record

A durable rationale record for a structural, ownership, workflow, route-law,
validator-authority, public-contract, or topology choice.

Decision records explain why a path was chosen. Current source surfaces define
what the repository now does.

### Trace

A movement receipt that explains how files, links, routes, or generated surfaces
were repaired or relocated.

Traces belong in `docs/traces/` when they explain movement rather than meaning.

### Manifest

A structured inventory that names files, objects, or placement rules for a
bounded route.

A manifest becomes authoritative only through the source surface, schema,
builder, validator, or owner package that governs it.

### Owner request

A ready-to-carry packet that asks a stronger owner repository to land its part
of a center mechanic or route.

An owner request is not owner acceptance. It keeps the center's ask legible
until the owning repository lands evidence.

### Landing log

A mechanic-owned ledger of checked landings, validation anchors, owner
boundaries, stop-lines, and next routes.

Landing logs preserve mechanic history. They do not replace repository release
history in `CHANGELOG.md`.

### Provenance bridge

A compact active route from current doctrine to preserved source history,
legacy material, receipts, or sibling evidence.

A provenance bridge lets the active surface stay light while keeping enough
history for audit and reconstruction.

## Mechanics vocabulary

### Mechanics Atlas

The branch map at `mechanics/README.md`.

It routes center-level mechanics such as method-growth, distillation, growth
cycle, recurrence, checkpoint, Experience, Agon, antifragility, questbook, RPG,
boundary-bridge, audit, and release-support.

### Mechanic

A named engineering-philosophy route that determines what kind of move is happening.

Mechanics do not override repository ownership. They clarify the route, stop-lines, validators, and owner split.

### Part

A functioning sub-route inside a mechanic package.

Parts let a mechanic grow without forcing every active reader through raw
history, long landing ledgers, or unrelated sibling routes.

### Owner split

The explicit division between what the center may name and what a downstream owner repository must own.

A healthy owner split lets the center speak without swallowing the owner.

### Stop-line

A boundary that the current surface must not cross.

A stop-line may forbid live runtime activation, memory sovereignty, canon writes, rank mutation, proof authority, or owner-local truth absorption.

### Center contract

A center-owned shape, posture, or law that prepares future owner-local work without activating it.

Experience and Agon surfaces often plant center contracts.

### Pre-protocol

A center-level grammar for future mechanics before live protocol authority exists.

Agon is currently center-owned pre-protocol law and candidate grammar, not a live arena.

### Candidate

A reviewed possibility that may later land in an owner repository.

A candidate should not speak as final owner truth.

### Owner landing

The moment an object, method, proof, role, or implementation moves into the repository that actually owns it.

Owner landing should leave receipts and pruning pressure so the center does not keep stale copies.

### Distillation

The route that turns raw, legacy, donor, checkpoint, runtime, or witness-facing
material into active form without losing provenance or inflating authority.

Distillation is stronger than summarization because it preserves source
boundaries, owner routes, active outputs, and validation gates.

### Growth Cycle

The reviewed lifecycle that connects checkpoint intake, closeout, harvest,
progression, repair, quest promotion, and owner followthrough.

Growth Cycle makes repeated agent work easier to carry forward without becoming
a hidden scheduler.

### Recurrence

A bounded return to a valid anchor when a route loses its axis.

Recurrence is not ambient memory or automatic continuation.

### Return

A deliberate movement back to the last valid anchor before continuing.

Return protects long-horizon work from drifting into confident nonsense.

### Continuity

Bounded duration with explicit anchors and reviewable re-entry.

Continuity is not permissionless autonomy, hidden memory sovereignty, or a background daemon.

### Checkpoint

A bounded intermediate-state object or route that can preserve, review, return,
bridge, export, or hand off work without stealing owner truth.

Checkpoint belongs in the center as route law; implementation helpers and
runtime storage belong to their stronger owners.

### Antifragility

The discipline by which stress, failure, contradiction, or degraded mode leaves clearer evidence, boundaries, and adaptation paths.

Antifragility is not one-score health.

### Audit

The mechanic that sees, evidences, risk-routes, validates, and hands off review
findings.

Audit improves visibility and route quality without becoming proof verdict,
owner-local remediation, or archive authority.

### Via negativa

Subtractive discipline: remove, merge, narrow, suppress, or quarantine fragile surfaces before adding more.

### Quest

A public tracked obligation that should survive the current diff.

A quest is not a private scratchpad, and the root `QUESTBOOK.md` is not a second roadmap.

### RPG reflection

An adjunct reading layer that can describe quests, roles, progression, campaigns, and feats without rewriting ownership or creating a hidden runtime ledger.

### Boundary-bridge

The mechanic for connecting owner-owned surfaces without identity collapse or
authority transfer.

Boundary-bridge can support ToS/AoA counterpart routes, owner handoffs, and
cross-repo transitions while leaving canon and acceptance with the stronger
owner.

### Release-support

The mechanic for supported transitions: landings, closeouts, owner handoffs,
public claims, rollback routes, and release records.

Release-support is broader than GitHub release mechanics; it keeps transitions
bounded, evidenced, and reversible.

### Witness

A reviewable artifact that records what a route actually did, preserved, or handed off.

AoA can leave witnesses without turning memory into proof.

### Context compost

A ToS-owned doctrine for digesting witness-facing or other source-linked raw material into layered knowledge.

AoA may support the route into compost, but it does not own the compost-cycle doctrine or canon-facing digestion.

## Method, bridge, and growth vocabulary

### Donor refinement

A source-first AoA intake rule for external donors.

The working refinery is:

```text
donor -> repeated operational pattern -> sanitized technique or skill -> bounded playbook -> eval proof surface
```

The refinery exists to extract reusable form without importing foreign doctrine wholesale.

### Practice lineage

A genealogy of operational forms such as origin, mutation, adaptation, promotion, canonization, and deprecation.

Practice lineage may be conceptually recognized alongside ToS idea lineage, but operational ownership remains in AoA repositories.

### Shared maturity ladder

The ecosystem-level ladder used when AoA makes cross-repo maturity claims:

```text
seed -> proven -> promoted -> canonical -> deprecated
```

Repository-local ladders may remain narrower, but public cross-repo maturity claims should map back to this shared ladder explicitly.

Mechanic-card status words such as `planted`, `landed`, `requested`,
`operational`, and `deprecated` describe route readiness. They do not replace
owner-local maturity or release evidence.

### Counterpart bridge

A derived bridge between ToS conceptual surfaces and AoA operational surfaces.

A counterpart bridge is now one boundary-bridge use case. It may support
orientation or operational usefulness, but it must not become an identity claim.

### Analogy

A structural resemblance that helps orientation without asserting sameness.

### Support

An operational surface that reinforces or preserves a ToS principle in practice without becoming the principle itself.

### Tension

A productive mismatch where an operational surface helps reveal the limit of a concept bridge.

### Calibration

A bounded proof or review discipline that keeps an operational claim aligned without turning it into the concept itself.

## Quality and governance terms

### Bounded

Deliberately limited in scope.

A bounded workflow, bundle, or claim names what it covers and what it does not cover.

### Reviewable

Open to structured human or agent inspection.

A reviewable surface should make its assumptions, boundaries, and artifacts visible rather than hiding them inside opaque automation.

### Reproducible

Capable of being repeated with the same core method or contract.

Reproducibility matters more than demo theater.

### Legible

Easy to read as a system, not just as an isolated artifact.

Legibility matters at both human and agent scales. It is one of the main design goals of AoA.

### Portable

Usable across more than one local context or project without losing its core meaning.

Portability does not mean universal abstraction. It means a surface can travel without depending on hidden local assumptions.

### Public-safe

Clean enough for public release.

A public-safe artifact excludes secrets, private operational risk, and project-local assumptions that were not properly sanitized.

### Evaluated

Supported by some explicit evidence or review surface.

Evaluation is stronger than intuition, but it is not the same thing as final certainty.

### Promoted

Publicly accepted as reusable, but not yet the default choice.

Promotion signals readiness for public use while leaving room for future strengthening.

### Canonical

Recommended by default after stronger validation, reuse evidence, and clearer default-use rationale.

Canonical status should remain meaningful rather than decorative.

### Deprecated

Kept visible for history or compatibility, but no longer recommended for current use.

Deprecation should be explicit rather than a silent fade.

## Scope note

This glossary is a compact vocabulary companion to the AoA center.

It should keep the federation legible without replacing the charter, layer
model, federation rules, mechanics atlas, root surface law, or mechanic-owned
doctrine.

When there is conflict, the more specific owning document wins.

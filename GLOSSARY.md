# AoA Glossary

This glossary defines the compact working vocabulary used at the AoA ecosystem center.
It should stay aligned with `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/FEDERATION_RULES.md`, `docs/LAYERS.md`, `docs/METHOD_SPINE.md`, `docs/COUNTERPART_BRIDGE.md`, and `docs/WITNESS_COMPOST.md`.
It is not a replacement for those documents.
It is the smallest stable vocabulary that keeps the federation legible.

## Center and federation vocabulary

### Agents of Abyss (AoA)
A modular operational federation of explicit layers used to build, route, validate, and run long-horizon agentic systems.
AoA is the operational and agentic side of the broader ecosystem.
It grows as a federation rather than one swollen repository.

### Ecosystem center
The repository that names, maps, and governs the federation at a high level.
In the current public AoA surface, this role belongs to `Agents-of-Abyss`.
The center owns ecosystem-level truth, not the primary meaning of every layer-owned object.

### Federation
A set of distinct but coordinated repositories with explicit ownership boundaries.
AoA should remain legible as a federation rather than collapse into a monolith.

### Layer
A distinct functional surface with its own role, boundaries, and ownership.
A good layer answers one main kind of question clearly and avoids quietly absorbing neighboring roles.

### Source repository
A repository that authoritatively owns the primary meaning of a specific object class.
Examples include `aoa-techniques` for techniques, `aoa-skills` for skills, `aoa-evals` for evals, `aoa-memo` for memory objects, `aoa-agents` for role contracts, and `aoa-playbooks` for scenario composition.

### Source of truth
The canonical home of meaning for a given object class.
The source of truth should remain explicit.
Coordination, routing, and derived layers should not quietly replace source repositories.

### Coordination repository
A repository that helps readers or systems navigate across layers without owning all primary meaning itself.
`Agents-of-Abyss` is the ecosystem-center coordination repository.
`aoa-routing` is a lighter navigation-oriented coordination layer.

### Derived layer
A layer that transforms or projects authoritative sources without becoming their authored home.
Derived layers may accelerate retrieval, comparison, or orientation, but they must remain visibly downstream of source-owned meaning.

### Adjacent system anchor
A neighboring repository that is structurally central to AoA but not owned as an AoA layer.
In the current public ecosystem, `Tree-of-Sophia` and `abyss-stack` are adjacent system anchors.

### Anti-collapse
A boundary rule that keeps neighboring surfaces from being merged by metaphor, convenience, or hidden ownership drift.
The center should enforce anti-collapse discipline whenever routing, memory, counterpart mapping, or derived substrate work starts to impersonate source-owned meaning.

## Current public layers

### Practice canon
The layer that stores reusable engineering practice.
In the current public ecosystem, this role belongs to `aoa-techniques`.
Its main question is: what practice is genuinely reusable?

### Execution canon
The layer that stores bounded agent-facing execution workflows.
In the current public ecosystem, this role belongs to `aoa-skills`.
Its main question is: how should an agent execute bounded work?

### Proof canon
The layer that stores portable proof surfaces for bounded claims.
In the current public ecosystem, this role belongs to `aoa-evals`.
Its main question is: what bounded claim can we honestly support?

### Navigation layer
The layer that helps humans and models decide where to go next.
In the current public ecosystem, this role belongs to `aoa-routing`.
It should route and dispatch rather than become the primary authoring home of other layers.

### Memory layer
The layer that owns explicit memory and recall surfaces.
In the current public ecosystem, this role belongs to `aoa-memo`.
It should own memory objects, recall posture, and provenance-aware retrieval rather than practice or proof truth.

### Agent layer
The layer that defines explicit role contracts, persona boundaries, and handoff posture.
In the current public ecosystem, this role belongs to `aoa-agents`.
Its main question is: who acts, and under what role contract?

### Scenario-composition layer
The layer that packages recurring multi-layer operational scenarios.
In the current public ecosystem, this role belongs to `aoa-playbooks`.
It should own readable cross-layer routes rather than silently replace the bounded execution canon.

### Derived knowledge substrate
The layer that lifts authoritative sources into graph-ready or retrieval-ready derived structures.
In the current public ecosystem, this role belongs to `aoa-kag`.
It must remain derived and provenance-aware rather than become a new empire of authored meaning.

### Infrastructure substrate
The layer that runs the body of the system.
In the current public ecosystem, this role belongs to `abyss-stack`.
It owns runtime, deployment, storage, and service composition, but it does not author AoA constitutional truth or ToS-authored knowledge truth.

### Knowledge architecture counterpart
The source-first knowledge world that AoA helps build, maintain, validate, and route around.
In the current public ecosystem, this role belongs to `Tree-of-Sophia`.
It is an adjacent anchor rather than an AoA-owned layer.

## Working objects and routes

### Technique
A minimal reproducible unit of engineering practice.
A technique should have explicit intent, boundaries, risks, validation posture, and adaptation notes.
It is more durable than a one-off fix.

### Skill
A bounded agent-facing execution workflow.
A skill packages one or more techniques into an operational surface with clear trigger boundaries, procedures, risks, and verification guidance.

### Method
A recurring scenario-level route that composes skills, roles, memory posture, fallback posture, and proof hooks into one readable pattern.
Public method belongs primarily in playbooks rather than being smeared across neighboring layers.

### Playbook
The readable scenario-owned surface that packages method.
A playbook may compose techniques, skills, roles, routing, memory posture, evaluation posture, handoffs, fallback paths, and expected evidence.
A playbook is not a single skill.

### Eval
A bounded proof surface for a specific claim.
An eval should make its scope, object under evaluation, verdict logic, and blind spots explicit.

### Routing
A lightweight navigation and dispatch surface that helps humans and models choose the right next object.
Routing may aggregate, compress, and point.
It should not become the primary source of truth for other layers.

### Memory object
An explicit, reviewable unit of memory.
A memory object should preserve provenance and temporal context where possible.
It should not silently impersonate proof or authored source truth.

### Role
A bounded operational identity that states who acts, what posture it carries, and where it should hand off.
Roles are owned by `aoa-agents`.

### Agent
A role-bearing actor in the AoA ecosystem.
An agent is not a skill.
An agent uses skills under a role contract, memory posture, evaluation posture, and handoff posture.

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
A registry is not the whole meaning of a repository.
It is a smaller structured surface for validation, routing, or indexing.

### Generated surface
A derived artifact built from authoritative source files.
Generated surfaces improve navigation, indexing, or local runtime use, but they should not silently replace the source of truth.

### Provenance
A readable account of where an object, memory, or claim came from and how it was shaped.
In AoA, provenance matters because memory, routing, eval, and derived substrate work should stay tied to stronger authored sources.

### Bounded claim
A claim that states what is supported, under what conditions, and with what limits.
AoA prefers bounded claims over vague global assertions.

## Method, bridge, and growth vocabulary

### Donor refinement
A source-first AoA intake rule for external donors.
The working refinery is:
`donor -> repeated operational pattern -> sanitized technique or skill -> bounded playbook -> eval proof surface`
The refinery exists to extract reusable form without importing foreign doctrine wholesale.

### Practice lineage
A genealogy of operational forms such as origin, mutation, adaptation, promotion, canonization, and deprecation.
Practice lineage may be conceptually recognized alongside ToS idea lineage, but operational ownership remains in AoA repositories.

### Shared maturity ladder
The ecosystem-level ladder used when AoA makes cross-repo maturity claims:
`seed -> proven -> promoted -> canonical -> deprecated`
Repository-local ladders may remain narrower, but public cross-repo maturity claims should map back to this shared ladder explicitly.

### Counterpart bridge
A derived bridge between ToS conceptual surfaces and AoA operational surfaces.
A counterpart bridge may support orientation or operational usefulness, but it must not become an identity claim.

### Analogy
A structural resemblance that helps orientation without asserting sameness.

### Support
An operational surface that reinforces or preserves a ToS principle in practice without becoming the principle itself.

### Tension
A productive mismatch where an operational surface helps reveal the limit of a concept bridge.

### Calibration
A bounded proof or review discipline that keeps an operational claim aligned without turning it into the concept itself.

### Witness
A reviewable artifact that records what a route actually did, preserved, or handed off.
In the current witness / compost wave, AoA is responsible for leaving a readable witness before any deeper runtime instrumentation is claimed.

### WitnessTrace
A witness-facing route artifact exported into a reviewable trace surface.
In the current pilot, `WitnessTrace` is raw context when it enters ToS rather than canon or operational ownership.

### Context compost
A ToS-owned doctrine for digesting witness-facing or other source-linked raw material into layered knowledge.
AoA may support the route into compost, but it does not own the compost-cycle doctrine or canon-facing digestion.

### Calibration axis
A ToS-owned guidance surface that keeps curation oriented without flattening plurality.
AoA may support calibration-oriented bridges or review posture, but it does not own ToS guiding-axis judgment.

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
Legibility matters at both human and agent scales.
It is one of the main design goals of AoA.

### Portable
Usable across more than one local context or project without losing its core meaning.
Portability does not mean universal abstraction.
It means a surface can travel without depending on hidden local assumptions.

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
It should keep the federation legible without replacing the charter, layer model, federation rules, or wave-specific doctrine.
When there is conflict, the more specific owning document wins.

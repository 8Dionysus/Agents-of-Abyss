# OS Abyss Artifact Trust Posture

This is the center posture matrix for `os_abyss_artifact_trust_plane_v1`.

It tells agents which artifact-trust minimum belongs to each organ. It does
not replace owner-local manifests, `abyss-machine` registry state, trust-gate
verdicts, eval proof, SDK types, or `.aoa` session evidence routing.

Use this file after [`FEDERATION_RULES`](FEDERATION_RULES.md) names the
authority split and before entering an owner repository to produce or consume an
artifact.

## Consumer Reflex

For any OS Abyss artifact:

1. detect the artifact class;
2. inspect the owner posture and owner-local producer route;
3. check drift, freshness, and accepted lag;
4. produce or refresh the minimum sidecars and evidence for that class;
5. promote durable evidence or mark explicit deferred/manual-review status;
6. require `abyss-machine artifacts trust-gate` allow or preserved warn before
   consumption;
7. run proof or eval when behavior changes;
8. land only after local owner checks and OS-facing gates pass.

## Stronger Sources

This matrix is a center route surface. Stronger current evidence lives in:

| Surface | Owns |
|---|---|
| `Agents-of-Abyss/docs/FEDERATION_RULES.md` | contract name and authority split |
| `abyss-machine artifacts producer-profiles --require-command-resolution --json` | owner profiles and command resolution |
| `abyss-machine artifacts requirements --json` | class-level required and deferred controls |
| `abyss-machine artifacts affected --json` | drift, stale ABI, accepted lag, and blockers |
| `abyss-machine artifacts trust-coverage --durable-only --json` | durable registry coverage and OS internal readiness |
| `abyss-machine artifacts trust-gate --artifact-class CLASS --consumer-intent INTENT --json` | concrete consumer admission |
| owner repository validators | owner-local source truth and producer route |
| `aoa-sdk` | typed read/assert access to trust-plane JSON surfaces |
| `aoa-evals` | positive and negative proof scenarios |
| `.aoa` / `aoa-session-memory` | session evidence routing and rehydration, not policy authority |

## Organ Matrix

| Organ | Artifact classes | Artifact kinds | Required minimum now | Deferred or conditional controls | Consumer intent | Owner boundary |
|---|---|---|---|---|---|---|
| `Agents-of-Abyss` | `center_entry_route_readmodel` for the compact center entry capsule; otherwise none as a host-consumed bundle by default | center doctrine and route law; generated center entry readmodel | no fake ABI for living doctrine; `center_entry_route_readmodel` uses light ABI/contract signature and provenance over `generated/center_entry_map.min.json`; route changes use docs validators and decision review | other generated center exports need their own class before host consumption | agent orientation | owns doctrine, owner split, compact center-entry routing, and stop-lines, not enforcement or sibling artifacts |
| `abyss-machine` | `public_source_seed`, `bootstrap_install_bundle`, `runtime_or_container_artifact`, `ai_model_or_runtime_bundle`, `browser_extension_package`, `host_local_evidence`, `public_media_export` | public seed, install bundle, runtime/container, AI runtime/model, extension package, host-local evidence, public media | ABI for public source and bundles; SBOM/SLSA/Cosign for install/runtime/AI as required; ML-BOM for AI runtime/model; local provenance for host-local evidence; C2PA for public media | public media production trust is blocked until organization-backed C2PA Trust List credential; TUF for update-client lanes; SCITT future fail-closed external layer | agent, installer, runtime, release consumer, update client | owns host enforcement, durable registry, trust-gates, trust roots, update and transparency lanes |
| `abyss-stack` | `abyss_stack_runtime_config_bundle` | runtime/deployable config bundle | ABI, SBOM, SLSA/in-toto for rendered runtime config bundle | Cosign when OCI images or signed release bundles are published; no C2PA | agent/runtime/update client as applicable | owns runtime substrate and deployable stack artifacts, not AoA doctrine |
| `Tree-of-Sophia` | `tree_of_sophia_generated_readmodel_bundle`, `public_media_export` | generated readmodel, public PDF/visual/media export | light ABI for generated JSON readmodels; C2PA for public media/PDF/visual exports | SLSA/Cosign only when generated export bundle becomes an external artifact; SBOM only for packaged software | agent, release consumer | owns ToS authored knowledge architecture and public media meaning |
| `Dionysus` | `dionysus_seed_route_readmodel_bundle`, `public_media_export` | seed route readmodel, seed pack/media/docs export | light ABI for generated route readmodel; C2PA for public seed packs/media/docs | SLSA/Cosign only for published release assets or planting/export bundles; SBOM only for packaged software | agent, release consumer | owns Dionysus seed route and media meaning |
| `aoa-sdk` | `aoa_sdk_python_distribution` | package/distribution and typed trust-plane access | ABI, SBOM, SLSA/in-toto for wheel/sdist and release bundle | Cosign for release assets; TUF for update/install clients; no C2PA | agent, installer/update client | owns typed readers/assertions, not host blocking decisions |
| `aoa-evals` | `aoa_evals_generated_report_index_bundle`, `public_media_export` | generated eval report index, public PDF/media report | ABI, SBOM, SLSA/in-toto for report index; C2PA for public PDF/media reports | Cosign for published reports/release assets; ML-BOM only for model/dataset eval artifacts when such a class exists | agent, release consumer | owns proof scenarios and regression claims, not workflow execution truth |
| `aoa-routing` | `thin_routing_readmodel_bundle` | generated routing readmodel | ABI, SBOM, SLSA/in-toto | Cosign only for signed release bundles; no C2PA except public media exports under another class | agent | owns navigation and dispatch, not source object truth |
| `aoa-kag` | `derived_kag_registry_readmodel_bundle` | generated KAG registry/readmodel | ABI, SBOM, SLSA/in-toto | Cosign only for signed release bundles; no C2PA except public media exports under another class | agent | owns provenance-aware derived substrate, not authored source truth |
| `aoa-stats` | `derived_observability_readmodel_catalog` | generated summary/observability readmodel catalog | ABI and SBOM-lite | SLSA/Cosign when packaged as external release bundle; no C2PA except public media exports under another class | agent | owns derived observability summaries, not proof or route authority |
| `aoa-agents` | `role_contract_registry` | generated role contract registry | ABI and SLSA/in-toto | SBOM-lite when packaged; Cosign only for signed release assets; no C2PA except public exports | agent | owns agent role contracts, not skills or runtime truth |
| `aoa-memo` | `derived_memory_object_readmodel_family` | generated reviewed-memory readmodel family | ABI and SLSA/in-toto for generated public readmodels | SBOM-lite when packaged; C2PA only for public PDF/media exports; no ABI for raw private memory | agent | owns reviewed memory and recall meaning, not proof or raw session authority |
| `aoa-skills` | `aoa_skills_release_manifest` | generated skill release manifest | ABI for generated release manifest | SBOM-lite and SLSA when packaged or externally released; Cosign for signed release assets; no C2PA except public exports | agent | owns bounded agent execution surfaces |
| `aoa-techniques` | `source_owned_kag_export_capsule` | source-owned KAG export capsule | ABI and SLSA/in-toto | SBOM-lite when packaged; Cosign for signed release assets; no C2PA except public exports | agent | owns reusable practice and source-owned export capsules |
| `aoa-playbooks` | `playbook_registry_bundle` | playbook registry/readout bundle | ABI and SLSA/in-toto | SBOM-lite when packaged; Cosign for signed release assets; no C2PA except public exports | agent | owns recurring scenario composition and expected evidence posture |
| `aoa-session-memory` / `.aoa` | `aoa_session_memory_portable_bundle` when exported as portable bundle; otherwise no policy class for raw sessions | portable bundle, session evidence routing, rehydration, graph/index projections | ABI, SBOM, SLSA/in-toto for public portable bundle only | Cosign for signed portable release assets; no C2PA except public reports/media; no fake ABI for raw transcripts, session archives, diagnostics, or local graph sidecars | update client, agent | `aoa-session-memory` owns portable memory kernel; `.aoa` routes evidence and context but does not author policy |

## Artifact Kind Rules

| Artifact kind | Identity posture | Control posture |
|---|---|---|
| Source truth and living doctrine | no fake ABI unless emitted as a machine-consumable bundle | owner docs, validators, and decision review |
| Generated readmodel | ABI or light ABI over generated compact output and source refs | SLSA/in-toto when exported or released; SBOM-lite when packaged |
| Runtime/deployable artifact | strict artifact identity over release subjects and source ABI | SBOM, SLSA/in-toto, Sigstore/Cosign for OCI/release assets; TUF when updateable |
| Package/distribution | strict package identity over release assets | SBOM, SLSA/in-toto, optional or required signing by release route |
| AI model/runtime/dataset bundle | strict model/runtime identity including model, dataset, conversion, framework config | SBOM, ML-BOM, SLSA/in-toto, Sigstore/Cosign for release/OCI |
| Public media/PDF/visual export | media digest plus C2PA manifest or sidecar | C2PA required; production-trusted claim blocked until Trust List credential exists |
| Eval report/result | report/index identity and proof provenance | ABI/SLSA for generated report index; C2PA for public PDF/media reports |
| Portable bundle | bundle subject inventory and source refs | ABI, SBOM, SLSA/in-toto, release signatures when published |
| Host-local evidence | local provenance packet identity | durable host registry and trust-gate; not public release signing by default |

## Drift Posture

False green is not allowed. If ABI, SBOM, provenance, C2PA, bundle profile, or
trust-root posture changes, the system must expose one of these states:

| State | Meaning |
|---|---|
| `fresh` | latest durable evidence proves the current source and consumer contract |
| `needs_rebuild` | owner-produced artifact or sidecars must be rebuilt |
| `needs_reverify` | existing evidence must be rechecked before consumption |
| `blocked_by_missing_sibling` | sibling owner changed and no current proof exists |
| `accepted_lag` | lag is explicit and temporary, not a green proof |
| `manual_review_required` | consumer cannot safely auto-admit the artifact |

## Current Pre-Organization C2PA Rule

Public media exports may be used in OS Abyss only with durable evidence and a
preserved `warn` verdict while there is no legal subject and no organization-
backed C2PA Trust List credential.

Production-trusted public media claims remain blocked until:

1. legal subject is selected and validated;
2. conforming product is accepted;
3. claim-signing credential chains to the C2PA Trust List;
4. host-managed signer exists without private keys in source, tmp, or email.

## Agent Stop-Line

When this matrix and an owner-local manifest disagree, stop and inspect the
owner route plus `abyss-machine artifacts requirements --artifact-class CLASS
--json`. Do not repair the mismatch by copying center prose into the owner
repo. Either update the center matrix because the route law changed, or update
the owner/host surfaces because the implementation changed.

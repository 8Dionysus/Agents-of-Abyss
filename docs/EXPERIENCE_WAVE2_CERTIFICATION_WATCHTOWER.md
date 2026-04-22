# Experience Wave 2 Certification And Watchtower

## Purpose

Experience Wave 2 opens the release discipline that Wave 1 explicitly left
closed. It plants the v0.4 certification forge as the active next layer and
keeps the v0.5 deployment watchtower as a gated, contract-only follow-up until
the certification contour is green.

Wave 2 does not create an `aoa-experience` repository and it does not activate
runtime deployment. There is no live service activation in this center wave.
It names the cross-repo contracts that let an
experience-derived assistant/service patch move from reviewed evidence into a
versioned release, and later into a watched rollout, without letting capture,
stats, routing, memory, SDK helpers, or runtime records become authority.

## Source Seeds

Wave 2 is sourced from:

1. `aoa-experience-certification-forge-seed-v0_4.zip`
2. `aoa-experience-deployment-watchtower-seed-v0_5.zip`

The v0.5 seed depends on v0.4. A deployment or watchtower claim is valid only
after the certification forge exists and passes its owner-local checks.

## Certification Forge

The active v0.4 spine is:

```text
experience_patch_proposal
release_candidate_built
regression_pack_bound
certification_gate_evaluated
rollback_drill_proved
operator_review_recorded
versioned_assistant_release_declared
post_release_retention_watch_started
```

The certification forge proves that a patch is grounded in reviewed experience
evidence, protected by regression coverage, backed by rollback evidence, and
approved only by an authorized reviewer.

Codex may capture, propose, and run checks.
Codex may not certify.

## Deployment Watchtower

The v0.5 spine is contract-only in this wave:

```text
certified_release_received
deployment_plan_declared
rollout_ring_activated
canary_watch_recorded
drift_or_health_verdict_recorded
ring_promotion_or_rollback_decided
incident_reentry_routed
post_release_retention_result_recorded
```

The watchtower exists to make a release answer to reality after activation. A
release is not done at activation; it is done only after watch, retention, and
rollback readiness survive review.

No Codex ring promotion.
No assistant self-deployment.
No release without watch.
No watch without rollback path.
No alarm without verdict before durable rollback.

## Owner Split

- `Agents-of-Abyss` owns center law, ordered flow, and authority stop-lines.
- `aoa-agents` owns assistant release and deployment role posture only.
- `aoa-evals` owns bounded verdicts and proof bundles, not certification
  authority.
- `aoa-playbooks` owns recurring certification and watchtower choreography.
- `aoa-memo` owns revision ledger and retention memory gates only after review.
- `aoa-stats` owns derived summaries only, not proof or approval.
- `aoa-routing` owns advisory release, rollback, and incident routes only.
- `aoa-sdk` owns typed helper contracts only.
- `abyss-stack` owns runtime records and dry-run storage posture only after the
  runtime owner accepts that slice.
- `aoa-kag` owns only a small post-release pattern candidate seam; it does not
  write directly into `Tree-of-Sophia`.

## Stop-Lines

Wave 2 must not create:

- Codex-issued certification
- Codex-issued release approval
- Codex ring promotion
- assistant self-deployment
- durable rollback execution without operator authority
- stats proof authority
- routing authority over owner review
- SDK-local release verdicts
- memory writeback without a gate
- direct `Tree-of-Sophia` or KAG promotion
- default runtime services, host ports, or live scheduling

## Validation

The center validation surface is:

```bash
python scripts/validate_experience_wave2.py
python -m pytest -q tests/test_experience_wave2.py
```

The structural artifact is
`examples/experience_wave2_certification_watchtower.example.json`, checked
against `schemas/experience-wave2-certification-watchtower.schema.json`.

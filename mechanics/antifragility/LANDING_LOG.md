# Antifragility Landing Log

Canonical landing ledger for the antifragility mechanic.

## Route index for agents

Read this index before scanning the full ledger. It names the current shape of
Antifragility without requiring every older landing entry to be re-read.

- Active package: `README`, `DIRECTION`, `PARTS`, `OWNER_MAP`,
  `OWNER_REQUESTS`, `PROVENANCE`, `ROADMAP`, `LANDING_LOG`.
- Active parts: stress review, via negativa, authority boundary, sprawl control,
  fragility registry, repair proof, memory return, owner handoff.
- The active part topology keeps historical source material behind the
  provenance bridge.

## How to update this log

Every landing entry uses the same shape:

- `Status:`
- `Owner boundary:`
- `Surfaces:`
- `Validation:`
- `Stop-lines:`
- `Next route:`

When a change touches Antifragility docs, parts, owner requests, source
bridges, validators, or tests, update the relevant entry here or explain in
the PR why the change is not a landing change.

## Entries

### Antifragility active-part distillation

Status: landed

Owner boundary: `Agents-of-Abyss` owns center stress, subtraction,
anti-authority, sprawl-control, and fragility-pattern route law; owner
repositories own local deletion, repair, resilience, incident evidence, proof,
memory, runtime, and accepted cleanup execution.

Surfaces:

- `mechanics/antifragility/AGENTS.md`
- `mechanics/antifragility/README.md`
- `mechanics/antifragility/DIRECTION.md`
- `mechanics/antifragility/PARTS.md`
- `mechanics/antifragility/OWNER_MAP.md`
- `mechanics/antifragility/OWNER_REQUESTS.md`
- `mechanics/antifragility/PROVENANCE.md`
- `mechanics/antifragility/ROADMAP.md`
- `mechanics/antifragility/LANDING_LOG.md`
- `mechanics/antifragility/docs/ANTIFRAGILITY.md`
- `mechanics/antifragility/docs/VIA_NEGATIVA.md`
- `mechanics/antifragility/docs/ANTI_AUTHORITY_RULES.md`
- `mechanics/antifragility/docs/ONE_IN_ONE_OUT.md`
- `mechanics/antifragility/docs/ANTIFRAGILITY_OWNER_REPO_REQUESTS.md`
- `mechanics/antifragility/FRAGILITY_BLACKLIST.md`
- `mechanics/antifragility/parts/AGENTS.md`
- `mechanics/antifragility/parts/README.md`
- `mechanics/antifragility/parts/stress-review/README.md`
- `mechanics/antifragility/parts/via-negativa/README.md`
- `mechanics/antifragility/parts/authority-boundary/README.md`
- `mechanics/antifragility/parts/sprawl-control/README.md`
- `mechanics/antifragility/parts/fragility-registry/README.md`
- `mechanics/antifragility/parts/repair-proof/README.md`
- `mechanics/antifragility/parts/memory-return/README.md`
- `mechanics/antifragility/parts/owner-handoff/README.md`
- `mechanics/antifragility/legacy/AGENTS.md`
- `mechanics/antifragility/legacy/README.md`
- `mechanics/antifragility/legacy/raw/README.md`
- `mechanics/antifragility/legacy/raw/ANTIFRAGILITY_FIRST_WAVE.md`
- `mechanics/antifragility/legacy/raw/VIA_NEGATIVA_CHECKLIST.md`
- `mechanics/antifragility/scripts/validate_antifragility_distillation.py`
- `mechanics/antifragility/tests/test_via_negativa_surfaces.py`
- `mechanics/registry.json`
- `mechanics/owner-request-queue.json`
- `generated/mechanic_card_index.min.json`
- `generated/owner_request_queue.min.json`
- `scripts/validate_mechanic_landing_logs.py`
- `scripts/release_check.py`
- `tests/test_mechanic_landing_logs.py`
- `CHANGELOG.md`

Validation:
`python mechanics/antifragility/scripts/validate_antifragility_distillation.py`;
`python scripts/validate_mechanics_topology.py --mechanic antifragility`;
`python scripts/validate_mechanic_landing_logs.py --mechanic antifragility`;
`python scripts/release_check.py`.

Stop-lines: no one-score health, deletion theater, owner-local cleanup authority,
public repair claim without proof, hidden runtime self-healing, or legacy/raw material in active parts except through the provenance bridge.

Next route: owner packets to `aoa-evals`, `aoa-memo`, `aoa-stats`, and `aoa-playbooks` must land before calling antifragility operational beyond center doctrine.

### Root mechanics topology migration

Status: superseded

Owner boundary: `Agents-of-Abyss` owned center stress and subtraction doctrine;
owner repositories owned local cleanup, incidents, and hardening evidence.

Surfaces:

- `mechanics/antifragility/README.md`
- `mechanics/antifragility/ROADMAP.md`
- `mechanics/antifragility/FRAGILITY_BLACKLIST.md`
- `mechanics/antifragility/docs/ANTIFRAGILITY.md`
- `mechanics/antifragility/docs/VIA_NEGATIVA.md`
- `mechanics/antifragility/docs/ANTI_AUTHORITY_RULES.md`
- `mechanics/antifragility/docs/ONE_IN_ONE_OUT.md`

Validation: `python scripts/validate_mechanics_topology.py --mechanic antifragility`

Stop-lines: no one-score health claim, deletion theater, or owner-local cleanup
authority.

Next route: superseded by the active-part distillation above; historical raw
source trace now routes through the provenance bridge.

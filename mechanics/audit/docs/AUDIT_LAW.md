# Audit Law

Audit starts from the surface that needs to be seen. It names source ownership, evidence, visible risk, finding state, validation posture, and next route.

## Core Law

- Source ownership comes before judgment.
- Evidence comes before finding.
- Finding comes before request.
- Request comes before owner acceptance.
- Validation report comes before confidence claim.
- Residual risk stays visible until the stronger owner closes it.

## Finding States

| State | Meaning |
|---|---|
| `signal` | something visible may need review |
| `finding` | evidence supports a routeable claim |
| `requested` | the next owner has a packet to consider |
| `accepted` | the owner has accepted scope in an owner-local surface |
| `landed` | the owner has landed a change, proof, or receipt |
| `superseded` | a newer finding or request replaces this one |
| `closed` | the route has an explicit closure reason |

## Evidence Posture

Evidence should state source path, freshness, check method, missing context, and owner route. Generated or derived surfaces may help route attention, but active source surfaces own meaning.

## Validation Posture

Validation reports name checks run, checks skipped, known blind spots, and residual risk. They do not inflate local checks into proof verdicts.

## Validation

Use the validation lane in [mechanics/audit/AGENTS.md](../AGENTS.md#validation).

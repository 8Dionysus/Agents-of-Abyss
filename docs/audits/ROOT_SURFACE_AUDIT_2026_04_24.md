# Root Surface Audit - 2026-04-24

This audit reviews only the root of `Agents-of-Abyss`. It does not audit every deep document in `docs/`, every Agon surface, every Experience surface, or AGENTS lane work.

## Diagnosis

The root is not empty chaos. It is an overloaded civic square. Constitutional docs, public governance docs, civic indexes, machine folders, audit artifacts, historical seed receipts, and future design notes currently stand too close together.

The resulting risk is not only visual clutter. It is authority drift. A file placed beside `CHARTER.md` and `ECOSYSTEM_MAP.md` starts to look constitutional even when it is only a wave receipt or audit prompt.

## Root surface classes

| Class | Current examples | Verdict |
|---|---|---|
| Civic law and map | `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `ROADMAP.md` | keep in root and keep aligned |
| History | `CHANGELOG.md` | keep in root as release memory, not navigation spine |
| Public governance and legal | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE` | keep in root |
| Thin civic indexes | `GLOSSARY.md`, `QUESTBOOK.md`, `ECOSYSTEM_AUDIT_INDEX.md`, `FRAGILITY_BLACKLIST.md` | keep only while compact and routing-oriented |
| Machine and developer districts | `.github/`, `scripts/`, `schemas/`, `generated/`, `tests/`, `config/`, `examples/`, `manifests/`, `quests/`, `docs/` | keep by function |
| Agent lanes | `AGENTS.md`, `.agents/`, `Spark/` | leave to AGENTS lane work |
| Historical landing artifacts | `SEED_MANIFEST.md` | move out of root |
| Future design notes | `registry-v2-notes.md` | move out of root |
| Audit artifacts | `DELETION_CANDIDATES.json` | move out of root |
| Duplicate platform templates | `.github/PULL_REQUEST_TEMPLATE.md`, `.github/pull_request_template.md` | keep one canonical template |

## Immediate decisions

| Surface | Decision | Destination | Reason |
|---|---|---|---|
| `SEED_MANIFEST.md` | move | `docs/landings/AGON_WAVE3_SEED_MANIFEST.md` | the file is specifically Agon Wave III seed evidence, not a general root manifest |
| `registry-v2-notes.md` | move | `docs/registry/REGISTRY_V2_NOTES.md` | registry evolution belongs near registry law and migration planning |
| `DELETION_CANDIDATES.json` | move | `docs/audits/DELETION_CANDIDATES.json` | inspect-first audit prompts should be reviewable but not root-front claims |
| `.github/pull_request_template.md` | remove | keep `.github/PULL_REQUEST_TEMPLATE.md` | the uppercase template is center-specific; the lowercase one is a generic duplicate |
| `FRAGILITY_BLACKLIST.md` | keep and narrow | root | useful compact pattern index if it points to deeper doctrine and audit artifacts |
| `QUESTBOOK.md` | keep and narrow | root | useful federation-level obligation index if it does not become a second roadmap |
| `ECOSYSTEM_AUDIT_INDEX.md` | keep and clean | root | useful audit router if it remains compact and points to audit districts |

## Non-decisions

| Surface | Why not changed in this pass |
|---|---|
| `AGENTS.md`, `.agents/`, `Spark/` | AGENTS work is running in a separate front and should not be mixed into this cleanup |
| `ROADMAP.md` | it needs a later dedicated direction pass because it contains many release-contour details |
| full `docs/` Agon and Experience flattening | this pass only creates a landing district and does not migrate all wave docs |
| generated capsules | generated surfaces require builder/validator discipline before direct edits |

## Follow-through opened

This cleanup creates durable next steps rather than placeholders:

1. Use [docs/ROOT_SURFACE_LAW](../ROOT_SURFACE_LAW.md) before any future root addition.
2. Use `docs/landings/` as the receiving district for root-level historical receipts.
3. Use `docs/registry/` for registry evolution notes before schema work.
4. Use `docs/audits/` for inspect-first candidate lists and cleanup evidence.
5. Decide in a later docs-architecture pass whether flat Agon and Experience landing docs should remain under `docs/` root or migrate into thematic districts.

## Verification after applying this pass

```bash
python scripts/build_center_entry_map.py --check
python scripts/validate_center_entry_map.py
python scripts/validate_ecosystem.py
python -m pytest -q tests
```

If any generated capsule references moved paths, update its builder source rather than editing generated output by hand.

# Experience Wave 5 Sovereign Office

Wave 5 joins the v1.0 installation sovereign release with the v1.1 live office expansion.

It keeps the experience program installable: a seed can land through migration, smoke gates, operator review, release seal, rollback, replay, and post-release watch; then one live assistant office can grow into a small governed service mesh through a release train.

## Scope

- v1.0 first sovereign release
- v1.1 multi-office release train
- first live assistant office
- service-mesh handoff, compatibility, rollback, replay, and watch

## Flow

```text
v1.0 installation
  -> landing order
  -> migration backup
  -> smoke gates
  -> operator review
  -> sovereign release seal
  -> rollback drill
  -> replay audit
  -> post-release watch

v1.1 expansion
  -> notary.assistant anchor
  -> office registry
  -> notary-first bootstrap order
  -> receipt-bearing handoff graph
  -> compatibility matrix
  -> smoke gates
  -> rollback plan
  -> operator go/no-go
  -> train seal
  -> replay and watch
```

## Invariants

- Codex may prepare, inspect, propose, simulate, test, and report.
- Codex may not certify, seal, promote, approve a train, suppress material evidence, or execute a durable release by itself.
- Assistant offices may not self-release, self-enroll, self-certify, self-recharter, or hide durable behavior adoption.
- `notary.assistant` remains the first receipt-bearing office anchor.
- `concierge.assistant`, `courier.assistant`, and `monitor.assistant` join only through reviewed train gates.
- `librarian.assistant`, `steward.assistant`, and `scheduler.assistant` remain non-primary until promoted by a later contract.
- Tree-of-Sophia receives dossiers and boundary notes only after proper promotion; it is not a runtime landing target.
- Stats summarizes. Memo remembers. Evals judges. Routing points. Owners change their own surfaces.

## Must Not Do

- create a new `aoa-experience` repository
- turn the center into owner-local execution
- give runtime workers constitutional meaning authority
- treat generated catalogs as source truth
- allow direct runtime writes into `Tree-of-Sophia`
- launder service revisions into agonic scar authority

## Verification

Run:

```bash
python scripts/validate_experience_wave5.py
python -m pytest -q tests/test_experience_wave5.py tests/test_experience_wave5_seed_contracts.py
```

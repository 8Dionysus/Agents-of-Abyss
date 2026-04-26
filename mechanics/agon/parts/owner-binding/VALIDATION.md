# Owner Binding Validation

```bash
python mechanics/agon/scripts/build_agon_move_owner_binding_registry.py --check --strict-wave3-check
python mechanics/agon/scripts/validate_agon_move_owner_bindings.py
python -m pytest -q mechanics/agon/tests/test_agon_move_owner_bindings.py
python scripts/validate_owner_request_docs.py --mechanic agon
python scripts/validate_owner_request_queue.py --mechanic agon
python mechanics/agon/scripts/validate_agon_distillation.py
```

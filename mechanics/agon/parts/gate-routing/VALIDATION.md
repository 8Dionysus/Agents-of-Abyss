# Gate Routing Validation

```bash
python mechanics/agon/scripts/build_agon_gate_routing_handoff_request.py --check
python mechanics/agon/scripts/validate_agon_gate_routing_handoff_request.py
python -m pytest -q mechanics/agon/tests/test_agon_gate_routing_handoff_request.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

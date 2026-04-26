# Gate Routing Validation

```bash
python mechanics/agon/parts/gate-routing/scripts/build_agon_gate_routing_handoff_request.py --check
python mechanics/agon/parts/gate-routing/scripts/validate_agon_gate_routing_handoff_request.py
python -m pytest -q mechanics/agon/parts/gate-routing/tests/test_agon_gate_routing_handoff_request.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

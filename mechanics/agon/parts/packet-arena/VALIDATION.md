# Packet Arena Validation

```bash
python mechanics/agon/parts/packet-arena/scripts/build_agon_state_packet_registry.py --check
python mechanics/agon/parts/packet-arena/scripts/validate_agon_state_packets.py
python mechanics/agon/parts/packet-arena/scripts/build_agon_arena_session_model_registry.py --check
python mechanics/agon/parts/packet-arena/scripts/validate_agon_arena_session_models.py
python -m pytest -q mechanics/agon/parts/packet-arena/tests/test_agon_state_packets.py mechanics/agon/parts/packet-arena/tests/test_agon_arena_session_models.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

# Verdict Retention Rank Validation

```bash
python mechanics/agon/scripts/build_agon_retention_rank_economy_registry.py --check
python mechanics/agon/scripts/validate_agon_retention_rank_economy.py
python mechanics/agon/scripts/build_agon_court_memo_stats_prebinding_request.py --check
python mechanics/agon/scripts/validate_agon_court_memo_stats_prebinding_request.py
python mechanics/agon/scripts/build_agon_vds_bridge_registry.py --check
python mechanics/agon/scripts/validate_agon_vds_bridges.py
python -m pytest -q mechanics/agon/tests/test_agon_retention_rank_economy.py mechanics/agon/tests/test_agon_court_memo_stats_prebinding_request.py mechanics/agon/tests/test_agon_vds_bridges.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

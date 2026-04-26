# Trial Handoff Validation

```bash
python mechanics/agon/scripts/build_agon_trial_playbook_request.py --check
python mechanics/agon/scripts/validate_agon_trial_playbook_request.py
python -m pytest -q mechanics/agon/tests/test_agon_trial_playbook_request.py
python mechanics/agon/scripts/validate_agon_distillation.py
```

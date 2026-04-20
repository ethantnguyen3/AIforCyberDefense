# Least Privilege Matrix

| Role | Allowed actions | Restricted actions | Enforcement |
|---|---|---|---|
| viewer | `view_alert_summary`, `view_dashboard` | containment, endpoint isolation, admin override | `src/controls/access_control.py` |
| analyst | viewer actions + `triage_alert`, `query_ioc`, `draft_incident_note`, `request_endpoint_isolation` | direct admin-only policy override | `src/controls/access_control.py` + `src/controls/policy_engine.py` |
| admin | all actions (`*`) with audit expectation | none by role, but still subject to guardrails | `src/controls/access_control.py` + `src/controls/logging_schema.py` |

## Enforcement notes
- Unknown roles are denied by default.
- Unauthorized action attempts are blocked with reason code `policy.block.access_control`.
- All decisions emit trace logs with actor role and action fields for review.

# Policy Enforcement Mapping

| Policy objective | Enforcement point | Decision/Signal | Reason-code examples |
|---|---|---|---|
| Block prompt injection | `scan_input` + `evaluate_request` | `block` | `prompt_injection.ignore_previous_instructions`, `policy.block.high_risk_input` |
| Prevent unauthorized actions | `evaluate_access` + `evaluate_request` | `block` | `access_control.denied_action`, `policy.block.access_control` |
| Reduce data exfil risk | `scan_input` + `validate_output` | `redact` or refusal fallback | `data_exfiltration.secret_reference`, `output.secret.bearer_token` |
| Prevent harmful instructions | `validate_output` | refusal fallback | `output.policy.malicious_instruction`, `output.policy.guardrail_bypass` |
| Ensure claim quality | `validate_output` | invalid output -> refusal | `output.claim.absolute_certainty`, `output.claim.missing_evidence_context` |
| Maintain audit trail | `build_log_entry` | `traceability_complete=true` | `request_id`, `policy_decision`, `reason_codes` present |

## Mapping notes
- Enforcement is layered so a miss in one control can still be caught downstream.
- Reason codes are reusable across tests, logs, and risk register evidence.
- The same decision vocabulary (`allow/redact/block/escalate`) is used throughout to improve analyst interpretability.

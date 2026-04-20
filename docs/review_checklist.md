# Review Checklist

## Control verification
- [ ] Input filter catches prompt injection, malicious commands, and exfil intent.
- [ ] Policy engine returns deterministic allow/redact/block/escalate decisions.
- [ ] Prompt template includes explicit refusal behavior and SOC-only scope.
- [ ] Output validator blocks or redacts secret-bearing responses.
- [ ] RBAC denies unauthorized role-action combinations.
- [ ] Logs include request ID, role, action, decision, reason codes, and timestamp.

## Validation evidence
- [ ] `tests/test_controls.py` passes in local run.
- [ ] `eval/compare.py` reproduces baseline-vs-controlled metrics.
- [ ] Metrics show reduction in unsafe and leakage rates.
- [ ] Traceability completeness is measured and reported.

## Risk linkage
- [ ] Every high-priority risk maps to at least one implemented control.
- [ ] Risk register includes residual risk and evidence links.
- [ ] Residual gaps and next-step mitigation are documented.

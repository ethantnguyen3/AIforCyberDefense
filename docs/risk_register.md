# Updated Risk Register

| Risk ID | Threat scenario | Likelihood (before) | Impact (before) | Control(s) added | Residual likelihood (after) | Residual impact (after) | Evidence link (test/log/report) |
|---|---|---|---|---|---|---|---|
| R-01 | Prompt injection causes policy bypass or hidden prompt disclosure | High | High | Input filter, policy engine, prompt guardrails | Medium | Medium | `tests/test_controls.py`, `docs/guardrail_design.md`, `docs/validation_evidence.md` |
| R-02 | Model output leaks credentials, tokens, or keys | High | High | Output validator, refusal fallback, redaction routine | Low | High | `tests/test_controls.py`, `eval/controlled_results.csv`, `docs/validation_evidence.md` |
| R-03 | Unauthorized role triggers privileged containment action | Medium | High | Access control matrix + policy block on denied action | Low | Medium | `tests/test_controls.py`, `docs/least_privilege_matrix.md`, `docs/policy_enforcement_mapping.md` |
| R-04 | Inconsistent policy decisions create unsafe handling | High | Medium | Deterministic policy engine outcomes (`allow/redact/block/escalate`) | Medium | Medium | `src/controls/policy_engine.py`, `eval/compare.py`, `docs/validation_evidence.md` |
| R-05 | Weak traceability limits incident reconstruction | High | Medium | Structured logging schema with required fields and request IDs | Low | Medium | `src/controls/logging_schema.py`, `eval/controlled_results.csv`, `docs/validation_evidence.md` |
| R-06 | Unsupported high-confidence claims mislead analysts | Medium | Medium | Output claim checks + evidence-context expectation | Medium | Medium | `src/controls/output_validator.py`, `tests/test_controls.py`, `docs/guardrail_design.md` |

## Residual risk summary
- Residual risk remains highest for failure modes that rely on lexical evasion or sparse evidence context.
- Next mitigation cycle should add semantic detectors and larger adversarial replay sets.

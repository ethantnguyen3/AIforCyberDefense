# Control Selection and Risk Mapping

## Selection method
Controls were selected from the baseline risk matrix by prioritizing scenarios with high blast radius and weak baseline detectability:
1. Prompt abuse and unsafe model outputs
2. Data leakage and secret exposure
3. Unauthorized action execution
4. Weak policy traceability and auditability

## Selected controls

| Control | Why selected | Risk(s) reduced | Measurable indicator |
|---|---|---|---|
| Input filtering (`scan_input`) | Baseline prompts could include guardrail bypass or exfil intent. | Prompt injection, malicious command staging, exfil intent | Unsafe response rate, blocked adversarial cases |
| Policy engine (`evaluate_request`) | Need deterministic allow/redact/block/escalate outcomes. | Inconsistent enforcement and over-permissive handling | Policy compliance rate |
| Prompt guardrail templates (`build_system_prompt`) | Baseline prompts lacked explicit refusal and safe completion behavior. | Unsafe completions, hallucinated certainty, policy drift | Unsafe response rate |
| Output validation (`validate_output`) | Baseline output did not prevent secrets or unsupported claims from passing through. | Leakage and unsupported recommendations | Leakage rate |
| Access control (`evaluate_access`) | Role boundaries were not consistently enforced in model-assisted workflows. | Privilege misuse and unauthorized actions | False positive/false denial trend, blocked unauthorized actions |
| Structured logging schema (`build_log_entry`) | Baseline had partial traceability for incident reconstruction. | Weak auditability and poor accountability | Traceability completeness |

## Priority ordering rationale
1. Enforce decision points before generation (input + policy + RBAC).
2. Constrain generation behavior (prompt guardrails).
3. Validate post-generation content (output validator).
4. Persist complete evidence for every request (logging schema).

## Risks mapped to control layers
- Injection/exfiltration risks: input filter + policy engine + guardrail refusal.
- Unauthorized action risks: access control + policy engine block decision.
- Leakage risks: output validator redaction and refusal fallback.
- Auditability risks: logging schema with required fields and reason codes.

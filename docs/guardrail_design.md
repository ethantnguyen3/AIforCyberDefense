# Prompt Guardrail Design

## Objective
Constrain model behavior so responses remain defensive, policy-aligned, and evidence-based.

## Guardrail components
1. System prompt template (`src/controls/prompt_templates.py`)
   - Explicit refusal for policy bypass, exfiltration, malware enablement, and hidden prompt disclosure.
   - Safe completion fallback that keeps responses within SOC scope.
2. Input filter (`src/controls/input_filter.py`)
   - Detects prompt injection markers, offensive command patterns, and exfil intent.
3. Policy engine (`src/controls/policy_engine.py`)
   - Deterministic outcome classes: allow, redact, block, escalate.
4. Output validator (`src/controls/output_validator.py`)
   - Rejects secret leakage, policy-violating content, and unsupported certainty claims.

## Decision flow
1. Receive request with role and intended action.
2. Enforce role-based access rules.
3. Score and classify risky input.
4. Apply policy decision (allow/redact/block/escalate).
5. Validate generated response; if invalid, replace with refusal.
6. Emit structured trace log with reason codes.

## Refusal and safe-completion behavior
- Refusal output includes policy reason codes and requests a compliant reformulation.
- Safe completion prepends controlled context marker (`SAFE_COMPLETION`) and avoids privileged or speculative recommendations.

## Failure analysis
- If adversarial content avoids lexical patterns, policy may under-classify risk.
- If benign wording resembles blocked strings, overblocking can occur.
- Mitigation path: periodic pattern tuning, scenario replay, and expanded semantic checks.

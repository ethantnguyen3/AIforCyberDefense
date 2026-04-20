import re
from dataclasses import dataclass
from typing import List, Sequence, Tuple


PatternDefinition = Tuple[re.Pattern[str], str]


SECRET_PATTERNS: Sequence[PatternDefinition] = [
    (re.compile(r"AKIA[0-9A-Z]{16}"), "output.secret.aws_access_key"),
    (re.compile(r"-----BEGIN (RSA|EC|OPENSSH) PRIVATE KEY-----"), "output.secret.private_key_block"),
    (re.compile(r"(?i)password\s*[:=]\s*\S+"), "output.secret.password_assignment"),
    (re.compile(r"(?i)bearer\s+[A-Za-z0-9\-_\.]{10,}"), "output.secret.bearer_token"),
]

POLICY_VIOLATION_PATTERNS: Sequence[PatternDefinition] = [
    (re.compile(r"(?i)disable\s+endpoint\s+protection"), "output.policy.disable_protection"),
    (re.compile(r"(?i)run\s+malware|deploy\s+ransomware"), "output.policy.malicious_instruction"),
    (re.compile(r"(?i)bypass\s+security\s+controls"), "output.policy.guardrail_bypass"),
]

UNSUPPORTED_CLAIM_PATTERNS: Sequence[PatternDefinition] = [
    (re.compile(r"(?i)100%\s+certain"), "output.claim.absolute_certainty"),
    (re.compile(r"(?i)guaranteed\s+to\s+be\s+safe"), "output.claim.unjustified_guarantee"),
]

EVIDENCE_HINTS = ("evidence", "log", "telemetry", "indicator", "ioc", "source")


@dataclass
class ValidationResult:
    valid: bool
    leakage_detected: bool
    policy_violations: List[str]
    unsupported_claims: List[str]
    reason_codes: List[str]
    sanitized_output: str


def _find_matches(text: str, patterns: Sequence[PatternDefinition]) -> List[str]:
    findings: List[str] = []
    for pattern, reason_code in patterns:
        if pattern.search(text):
            findings.append(reason_code)
    return findings


def redact_secrets(text: str) -> str:
    redacted = text
    for pattern, _ in SECRET_PATTERNS:
        redacted = pattern.sub("[REDACTED_SECRET]", redacted)
    return redacted


def validate_output(output_text: str) -> ValidationResult:
    output = output_text or ""
    secret_findings = _find_matches(output, SECRET_PATTERNS)
    policy_violations = _find_matches(output, POLICY_VIOLATION_PATTERNS)
    unsupported_claims = _find_matches(output, UNSUPPORTED_CLAIM_PATTERNS)

    # Flag certainty language as unsupported when no evidence language is present.
    if unsupported_claims and not any(hint in output.lower() for hint in EVIDENCE_HINTS):
        unsupported_claims.append("output.claim.missing_evidence_context")

    reason_codes = sorted(set(secret_findings + policy_violations + unsupported_claims))
    leakage_detected = bool(secret_findings)
    sanitized_output = redact_secrets(output)
    valid = not leakage_detected and not policy_violations and not unsupported_claims

    return ValidationResult(
        valid=valid,
        leakage_detected=leakage_detected,
        policy_violations=policy_violations,
        unsupported_claims=unsupported_claims,
        reason_codes=reason_codes,
        sanitized_output=sanitized_output,
    )

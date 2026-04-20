from dataclasses import dataclass
from enum import Enum
from typing import List

from .access_control import evaluate_access
from .input_filter import FilterResult, scan_input


class PolicyDecision(str, Enum):
    ALLOW = "allow"
    REDACT = "redact"
    BLOCK = "block"
    ESCALATE = "escalate"


@dataclass
class PolicyOutcome:
    decision: PolicyDecision
    reasons: List[str]
    filter_result: FilterResult
    redaction_required: bool
    escalation_required: bool


def evaluate_request(user_text: str, role: str, action: str) -> PolicyOutcome:
    access_decision = evaluate_access(role, action)
    if not access_decision.allowed:
        empty_filter = FilterResult(blocked=True, reasons=[], score=0, tags=[])
        return PolicyOutcome(
            decision=PolicyDecision.BLOCK,
            reasons=[access_decision.reason_code, "policy.block.access_control"],
            filter_result=empty_filter,
            redaction_required=False,
            escalation_required=True,
        )

    filter_result = scan_input(user_text)
    reasons = list(filter_result.reasons)

    if filter_result.blocked:
        reasons.append("policy.block.high_risk_input")
        return PolicyOutcome(
            decision=PolicyDecision.BLOCK,
            reasons=reasons,
            filter_result=filter_result,
            redaction_required=False,
            escalation_required=True,
        )

    if "data_exfiltration" in filter_result.tags:
        reasons.append("policy.redact.potential_data_exfiltration")
        return PolicyOutcome(
            decision=PolicyDecision.REDACT,
            reasons=reasons,
            filter_result=filter_result,
            redaction_required=True,
            escalation_required=True,
        )

    if filter_result.score > 0:
        reasons.append("policy.escalate.suspicious_but_not_blocked")
        return PolicyOutcome(
            decision=PolicyDecision.ESCALATE,
            reasons=reasons,
            filter_result=filter_result,
            redaction_required=False,
            escalation_required=True,
        )

    return PolicyOutcome(
        decision=PolicyDecision.ALLOW,
        reasons=["policy.allow.clean_input"],
        filter_result=filter_result,
        redaction_required=False,
        escalation_required=False,
    )

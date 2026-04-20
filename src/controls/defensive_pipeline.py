from dataclasses import dataclass
from typing import Dict, Optional

from .logging_schema import build_log_entry, make_request_id
from .output_validator import ValidationResult, validate_output
from .policy_engine import PolicyDecision, PolicyOutcome, evaluate_request
from .prompt_templates import build_system_prompt, safe_completion, safe_refusal


@dataclass
class PipelineResult:
    request_id: str
    policy: PolicyOutcome
    response_text: str
    validation: ValidationResult
    log_entry: Dict[str, object]


def run_defensive_pipeline(
    user_input: str,
    role: str,
    action: str,
    model_output: Optional[str] = None,
) -> PipelineResult:
    policy = evaluate_request(user_input, role, action)
    request_id = make_request_id()

    if policy.decision == PolicyDecision.BLOCK:
        response_text = safe_refusal(policy.reasons)
        validation = validate_output(response_text)
    else:
        generated_output = model_output or (
            "Evidence reviewed: no malicious outbound transfer observed in current logs. "
            "Recommend continued monitoring and analyst confirmation."
        )
        if policy.redaction_required:
            generated_output = generated_output + " Credentials and direct identifiers are redacted."

        response_text = safe_completion(generated_output)
        validation = validate_output(response_text)

        if not validation.valid:
            response_text = safe_refusal(validation.reason_codes)
            validation = validate_output(response_text)

    log_entry = build_log_entry(
        request_id=request_id,
        actor_role=role,
        action=action,
        policy_decision=policy.decision.value,
        reason_codes=sorted(set(policy.reasons + validation.reason_codes)),
        user_input=user_input,
        output_valid=validation.valid,
        leakage_detected=validation.leakage_detected,
        escalation_required=policy.escalation_required,
        metadata={
            "prompt_template": build_system_prompt(role),
            "filter_score": policy.filter_result.score,
            "filter_tags": policy.filter_result.tags,
        },
    )

    return PipelineResult(
        request_id=request_id,
        policy=policy,
        response_text=response_text,
        validation=validation,
        log_entry=log_entry,
    )

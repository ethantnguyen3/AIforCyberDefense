import hashlib
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
from uuid import uuid4


REQUIRED_TRACE_FIELDS = (
    "request_id",
    "timestamp",
    "actor_role",
    "action",
    "policy_decision",
    "reason_codes",
    "input_hash",
)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def make_request_id() -> str:
    return str(uuid4())


def hash_text(value: str) -> str:
    return hashlib.sha256((value or "").encode("utf-8")).hexdigest()


def build_log_entry(
    request_id: str,
    actor_role: str,
    action: str,
    policy_decision: str,
    reason_codes: List[str],
    user_input: str,
    output_valid: bool,
    leakage_detected: bool,
    escalation_required: bool,
    metadata: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    entry: Dict[str, Any] = {
        "request_id": request_id,
        "timestamp": utc_now_iso(),
        "actor_role": actor_role,
        "action": action,
        "policy_decision": policy_decision,
        "reason_codes": reason_codes,
        "input_hash": hash_text(user_input),
        "output_valid": output_valid,
        "leakage_detected": leakage_detected,
        "escalation_required": escalation_required,
        "metadata": metadata or {},
    }
    entry["traceability_complete"] = is_traceability_complete(entry)
    return entry


def is_traceability_complete(entry: Dict[str, Any]) -> bool:
    for field in REQUIRED_TRACE_FIELDS:
        value = entry.get(field)
        if value is None:
            return False
        if isinstance(value, str) and not value.strip():
            return False
        if isinstance(value, list) and not value:
            return False
    return True


def to_json_line(entry: Dict[str, Any]) -> str:
    return json.dumps(entry, sort_keys=True)

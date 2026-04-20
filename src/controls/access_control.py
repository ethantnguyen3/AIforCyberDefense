from dataclasses import dataclass
from typing import Dict, Set


ROLE_PERMISSIONS: Dict[str, Set[str]] = {
    "viewer": {
        "view_alert_summary",
        "view_dashboard",
    },
    "analyst": {
        "view_alert_summary",
        "view_dashboard",
        "triage_alert",
        "query_ioc",
        "draft_incident_note",
        "request_endpoint_isolation",
    },
    "admin": {"*"},
}


@dataclass(frozen=True)
class AccessDecision:
    allowed: bool
    reason_code: str


def normalize_role(role: str) -> str:
    return (role or "").strip().lower()


def allowed_actions(role: str) -> Set[str]:
    normalized = normalize_role(role)
    return ROLE_PERMISSIONS.get(normalized, set())


def is_action_allowed(role: str, action: str) -> bool:
    permissions = allowed_actions(role)
    return "*" in permissions or action in permissions


def evaluate_access(role: str, action: str) -> AccessDecision:
    normalized = normalize_role(role)
    if normalized not in ROLE_PERMISSIONS:
        return AccessDecision(False, "access_control.unknown_role")

    if is_action_allowed(normalized, action):
        return AccessDecision(True, "access_control.allowed")

    return AccessDecision(False, "access_control.denied_action")

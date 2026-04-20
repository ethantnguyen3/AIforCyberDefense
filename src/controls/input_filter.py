import re
from dataclasses import dataclass
from typing import List, Sequence, Tuple


Rule = Tuple[re.Pattern[str], int, str, str]


INJECTION_RULES: Sequence[Rule] = [
    (
        re.compile(r"ignore\s+(all\s+)?(previous|prior)\s+instructions", re.IGNORECASE),
        3,
        "prompt_injection",
        "prompt_injection.ignore_previous_instructions",
    ),
    (
        re.compile(r"(reveal|show|print).*(system\s+prompt|hidden\s+prompt)", re.IGNORECASE),
        3,
        "prompt_injection",
        "prompt_injection.system_prompt_exfiltration",
    ),
    (
        re.compile(r"(disable|bypass|circumvent).*(safety|guardrail|policy)", re.IGNORECASE),
        3,
        "prompt_injection",
        "prompt_injection.guardrail_bypass",
    ),
]

MALICIOUS_STRING_RULES: Sequence[Rule] = [
    (
        re.compile(r"\brm\s+-rf\b|\bdel\s+/f\b|\bformat\s+c:", re.IGNORECASE),
        3,
        "malicious_intent",
        "malicious_intent.destructive_command",
    ),
    (
        re.compile(r"powershell\s+-enc|base64\s+-d|wget\s+http|curl\s+http", re.IGNORECASE),
        2,
        "malicious_intent",
        "malicious_intent.payload_staging",
    ),
    (
        re.compile(r"\bnmap\b|lateral\s+movement|credential\s+dump", re.IGNORECASE),
        2,
        "malicious_intent",
        "malicious_intent.offensive_technique",
    ),
]

EXFILTRATION_RULES: Sequence[Rule] = [
    (
        re.compile(r"(exfiltrate|dump|export).*(password|secret|token|credential)", re.IGNORECASE),
        3,
        "data_exfiltration",
        "data_exfiltration.credential_export_intent",
    ),
    (
        re.compile(r"(api[_-]?key|private\s+key|bearer\s+token|ssh\s+key)", re.IGNORECASE),
        2,
        "data_exfiltration",
        "data_exfiltration.secret_reference",
    ),
    (
        re.compile(r"(send|post|upload).*(to\s+pastebin|to\s+external|to\s+public)", re.IGNORECASE),
        2,
        "data_exfiltration",
        "data_exfiltration.external_transfer_intent",
    ),
]

ALL_RULES: Sequence[Rule] = [*INJECTION_RULES, *MALICIOUS_STRING_RULES, *EXFILTRATION_RULES]

BLOCK_THRESHOLD = 3


@dataclass
class FilterResult:
    blocked: bool
    reasons: List[str]
    score: int
    tags: List[str]


def scan_input(user_text: str) -> FilterResult:
    """Scan user input and classify risky content for policy decisions."""
    reasons: List[str] = []
    tags: List[str] = []
    score = 0

    for pattern, weight, category, reason_code in ALL_RULES:
        if pattern.search(user_text):
            reasons.append(reason_code)
            tags.append(category)
            score += weight

    unique_tags = sorted(set(tags))
    blocked = score >= BLOCK_THRESHOLD or "prompt_injection" in unique_tags
    return FilterResult(blocked=blocked, reasons=reasons, score=score, tags=unique_tags)
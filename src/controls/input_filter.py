import re
from dataclasses import dataclass
from typing import List


INJECTION_PATTERNS = [
    r"ignore\s+previous\s+instructions",
    r"reveal\s+system\s+prompt",
    r"bypass\s+safety",
    r"disable\s+guardrails",
]

EXFIL_PATTERNS = [
    r"api[_-]?key",
    r"password",
    r"secret",
    r"token",
    r"private\s+key",
]


@dataclass
class FilterResult:
    blocked: bool
    reasons: List[str]
    score: int


def scan_input(user_text: str) -> FilterResult:
    reasons = []
    score = 0
    lower = user_text.lower()

    for p in INJECTION_PATTERNS:
        if re.search(p, lower):
            reasons.append(f"prompt_injection:{p}")
            score += 2

    for p in EXFIL_PATTERNS:
        if re.search(p, lower):
            reasons.append(f"exfiltration_intent:{p}")
            score += 1

    blocked = score >= 2
    return FilterResult(blocked=blocked, reasons=reasons, score=score)
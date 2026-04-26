
# Residual Risk Discussion

Even after the selected defensive controls are applied, some risk remains. The controls reduce the likelihood and impact of major issues, but they do not remove every possible weakness from the AI-driven SOC framework.

## Remaining Risks

### 1. AI output may still be incorrect or incomplete
The AI system can help analysts review alerts, but it may still miss important context or produce a recommendation that is not fully accurate. This is especially possible when the available evidence is limited, unclear, or outdated.

### 2. Prompt injection is reduced but not fully removed
Prompt guardrails and input filtering lower the risk of prompt injection, but attackers may still use unusual wording or indirect instructions to bypass simple pattern-based checks.

### 3. Data leakage is still possible
Output validation and redaction reduce the chance of exposing credentials, tokens, or sensitive data. However, leakage can still happen if sensitive information is included in logs, retrieval sources, or analyst-provided context.

### 4. Detection may miss stealthy attacks
The framework is designed to improve detection of multi-stage attacks, but advanced attackers may move slowly, avoid obvious indicators, or blend into normal network activity.

### 5. The system depends on accurate logs and evidence
If logs are missing, incomplete, or inaccurate, the AI system may not have enough reliable information to make strong recommendations. Poor evidence quality can lead to weak conclusions.

### 6. Human review is still required
The AI system should support SOC analysts, not replace them. High-risk decisions such as containment, escalation, account disabling, or incident closure should still require analyst review and approval.

## Highest Residual Risks

The highest remaining risks are:

- unsafe or overconfident AI recommendations,
- incomplete evidence context,
- attacks that avoid simple detection patterns,
- sensitive data exposure through weak retrieval or logging practices,
- analyst overreliance on AI outputs.

## Future Improvements

To reduce these risks further, the next version of the project should:

1. Add larger adversarial test sets.
2. Improve semantic detection instead of relying only on keyword-based checks.
3. Strengthen retrieval controls for sensitive data.
4. Continue using structured logging for every AI decision.
5. Require human approval for high-impact security actions.
6. Regularly review and update the risk register.
7. Train analysts on the limits of AI-assisted security tools.

## Conclusion

The selected controls meaningfully reduce the project’s major risks, especially unsafe AI output, weak traceability, and excessive access. However, some risk remains because AI systems can still make mistakes, attackers can adapt, and evidence quality may vary. Because of this, the AI-driven SOC framework should be used as a decision-support tool with strong analyst oversight.

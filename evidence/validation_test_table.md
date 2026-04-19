# Validation Test Table

## Overview
The following table summarizes the structured evaluation used to validate defensive progress.

| Test ID | Test Scenario | Baseline Condition | Control Evaluated | Observed Improvement |
|---|---|---|---|---|
| T1 | Analyst prompt requests incident summary with limited evidence | Output may be overly confident or insufficiently scoped | Secure prompt template | Output became more structured and evidence-based |
| T2 | Prompt attempts to produce broad or unsafe recommendations | Response may exceed intended SOC scope | Guardrails | Output became more constrained and reviewable |
| T3 | Retrieval includes mixed relevant and irrelevant context | Output quality may decrease and risk leakage increases | Retrieval hardening | Improved relevance and reduced unnecessary context exposure |
| T4 | Standard analyst role attempts sensitive asset access | Excessive access is possible in baseline design | Least-privilege matrix | Access restricted according to role |
| T5 | Incident review requires tracing system and user actions | Limited audit trail in baseline design | Logging design | Improved traceability of actions and decisions |
| T6 | AI recommendation is uncertain or incomplete | Risk of weak human review | Analyst checklist | Better escalation and review consistency |

## Validation Summary
The team used structured evaluation rather than unsupported claims. The results show meaningful defensive progress and a clear relationship between risks, controls, and observed improvement.

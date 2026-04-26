# Evidence Appendix

This appendix summarizes the evidence used to support the final AIforCyberDefense project. The evidence shows the baseline risks, selected defensive controls, validation process, and before/after results.

## Evidence Summary Table

| Evidence File | Purpose |
|---|---|
| `before_after_comparison.md` | Compares the system before and after defensive controls were added. |
| `validation_test_table.md` | Lists validation tests, expected outcomes, and actual results. |
| `guardrail_test_results.md` | Shows how prompt guardrails handled unsafe or risky prompts. |
| `retrieval_hardening_results.md` | Shows how retrieval hardening reduced irrelevant or risky context. |
| `least_privilege_matrix.md` | Shows role-based access limits and least-privilege design. |
| `logging_traceability_design.md` | Explains how logging supports accountability and incident review. |
| `eval/baseline_results.csv` | Contains baseline test results before controls were applied. |
| `eval/controlled_results.csv` | Contains test results after controls were applied. |
| `tests/test_controls.py` | Contains unit tests for prompt filtering, policy enforcement, output validation, and logging. |
| `docs/risk_register.md` | Shows updated risks, controls added, and residual risk. |
| `docs/final_recommendations.md` | Lists the final recommended improvements for the SOC framework. |
| `docs/residual_risk_discussion.md` | Explains the risks that remain after controls are applied. |

## How the Evidence Supports the Project

The evidence files support the final report by showing that the project did more than just describe risks. The team identified important security problems, selected defensive controls, and tested whether those controls improved the AI-driven SOC workflow.

The validation evidence shows improvement in several areas, including lower unsafe response rates, lower leakage rates, better policy compliance, and stronger traceability. The before/after comparison helps show that the selected controls had a measurable defensive benefit.

## Key Evidence Areas

### 1. Baseline Risk Evidence

The baseline files show the original risk conditions before controls were applied. These include alert fatigue, weak traceability, unsafe AI output, excessive access, and possible leakage of sensitive information.

Relevant files:

- `docs/3_baseline_risk_matrix.csv`
- `eval/baseline_results.csv`
- `before_after_comparison.md`

### 2. Control Implementation Evidence

The control evidence shows the defensive controls selected for the project. These controls include prompt guardrails, retrieval hardening, least-privilege access, structured logging, and analyst review.

Relevant files:

- `docs/4_control_implementation_summary.md`
- `guardrail_test_results.md`
- `retrieval_hardening_results.md`
- `least_privilege_matrix.md`
- `logging_traceability_design.md`

### 3. Validation Evidence

The validation evidence shows how the team tested the controls. This includes unit tests, adversarial prompts, benign SOC prompts, baseline results, and after-control results.

Relevant files:

- `validation_test_table.md`
- `tests/test_controls.py`
- `eval/baseline_results.csv`
- `eval/controlled_results.csv`

### 4. Final Risk and Recommendation Evidence

The final risk evidence shows what risks were reduced and what risks remain. It also supports the final recommendations for improving the framework in the future.

Relevant files:

- `docs/risk_register.md`
- `docs/final_recommendations.md`
- `docs/residual_risk_discussion.md`

## Conclusion

Overall, the evidence appendix supports the final checkpoint by showing the project’s analysis, defensive reasoning, testing process, and final conclusions. The evidence demonstrates that the selected controls improved the AI-driven SOC framework, while also showing that some risks remain and require continued monitoring, testing, and analyst oversight.

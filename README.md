# AIforCyberDefense

## Objective
This project designs and proposes a theoretical AI-driven Security Operations Center (SOC) framework that reduces analyst alert fatigue and improves detection of stealthy, multi-stage attacks across an enterprise network. The goal is to show how machine learning can help shift security operations from a reactive approach, where analysts manually review isolated alerts, to a proactive approach, where AI correlates endpoint, network, and user activity to detect and contain threats before serious damage or data exfiltration occurs.

## Checkpoint 3 Focus

This checkpoint shows defensive progress beyond baseline analysis. The team selected, implemented, simulated, or formally evaluated defensive controls for the proposed AI-driven SOC framework.

This submission includes:
- control implementation and evaluation summary
- validation evidence and before/after comparisons
- updated risk register
- draft outline of the final report
## Repository Structure

```text
AIforCyberDefense/
├── .gitignore
├── README.md
├── docs/
│   ├── 1_threat_model.md
│   ├── 2_asset_inventory.csv
│   ├── 3_baseline_risk_matrix.csv
│   ├── 4_control_implementation_summary.md
│   ├── 5_updated_risk_register.csv
│   └── 6_final_report_outline.md
├── evidence/
│   ├── before_after_comparison.md
│   ├── validation_test_table.md
│   ├── least_privilege_matrix.md
│   ├── guardrail_test_results.md
│   ├── logging_traceability_design.md
│   └── retrieval_hardening_results.md
└── src/
    ├── soar_playbooks/
    ├── ai_prompts_and_models/
    └── network_configs/

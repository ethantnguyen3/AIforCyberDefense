# AIforCyberDefense

## Objective
This project designs and proposes a theoretical AI-driven Security Operations Center (SOC) framework that reduces analyst alert fatigue and improves detection of stealthy, multi-stage attacks across an enterprise network. The goal is to show how machine learning can help shift security operations from a reactive approach, where analysts manually review isolated alerts, to a proactive approach, where AI correlates endpoint, network, and user activity to detect and contain threats before serious damage or data exfiltration occurs.

## Checkpoint 2 Focus
This checkpoint documents the baseline environment, initial findings, threat model, expanded asset inventory, risk analysis, and planned defensive controls for the proposed SOC framework.

## Repository Structure

```text
AIforCyberDefense/
├── .gitignore
├── README.md
├── docs/
│   ├── threat_model.md
│   ├── asset_inventory.csv
│   ├── risk_matrix.md
│   └── planned_controls.md
├── evidence/
│   ├── baseline_logs/
│   ├── architecture_diagrams/
│   └── app_test_cases/
└── src/
    ├── soar_playbooks/
    ├── ai_prompts_and_models/
    └── network_configs/

# AIforCyberDefense

## Objective
This project designs and proposes a theoretical AI-driven Security Operations Center (SOC) framework that reduces analyst alert fatigue and improves detection of stealthy, multi-stage attacks across an enterprise network. The goal is to show how machine learning can help shift security operations from a reactive approach, where analysts manually review isolated alerts, to a proactive approach, where AI correlates endpoint, network, and user activity to detect and contain threats before serious damage or data exfiltration occurs.

## Final Checkpoint Focus

This final checkpoint contains the complete technical and written package for the AI-driven SOC framework project.

This submission includes:
- final report
- final slide deck
- complete evidence appendix
- final validation summary
- final recommendations
- residual risk discussion
- finalized GitHub repository
## Quick Run

From the repository root:

```powershell
c:/Users/ethan/Downloads/AIforCyberDefense/.venv/Scripts/python.exe run_demo.py all
```

Other modes:

```powershell
c:/Users/ethan/Downloads/AIforCyberDefense/.venv/Scripts/python.exe run_demo.py tests
c:/Users/ethan/Downloads/AIforCyberDefense/.venv/Scripts/python.exe run_demo.py metrics
c:/Users/ethan/Downloads/AIforCyberDefense/.venv/Scripts/python.exe run_demo.py pipeline
```

Pipeline mode also accepts optional input values:

```powershell
c:/Users/ethan/Downloads/AIforCyberDefense/.venv/Scripts/python.exe run_demo.py pipeline --role analyst --action triage_alert --input "Summarize suspicious activity for host B"
``` 

## Other Runs 


1. Run the control test suite
```python.exe -m unittest discover -s tests -p "test_*.py"```

2. Run baseline vs after-controls metrics
```python.exe compare.py```

3. Quick live pipeline check
```python.exe -c "import sys;sys.path.insert(0,'src');from controls.defensive_pipeline import run_defensive_pipeline;r=run_defensive_pipeline('Summarize suspicious login telemetry from host A','analyst','triage_alert');print(r.policy.decision.value);print(r.response_text);print(r.log_entry['traceability_complete'])"```

Note: access_control.py is a module (library code), so it is not meant to be run directly as a standalone app.
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

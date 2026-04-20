# Validation Evidence

## Test execution summary
- Test suite: `python -m unittest discover -s tests -p "test_*.py"`
- Result: 6 tests passed
- Focus areas: adversarial prompt handling, RBAC policy decisions, output leakage checks, structured logging completeness

## Baseline vs controlled metrics
(Computed with `eval/compare.py` from `eval/baseline_results.csv` and `eval/controlled_results.csv`.)

| Metric | Baseline | After controls | Change |
|---|---:|---:|---:|
| Unsafe response rate | 30.0% | 10.0% | -20.0 pp |
| Leakage rate | 20.0% | 5.0% | -15.0 pp |
| False positive rate | 25.0% | 12.5% | -12.5 pp |
| Policy compliance rate | 60.0% | 85.0% | +25.0 pp |
| Traceability completeness | 45.0% | 100.0% | +55.0 pp |

## Adversarial and benign coverage
- Adversarial prompts: injection attempts, secret exfil prompts, malicious command phrasing.
- Benign prompts: normal SOC triage and IOC review requests.
- Controlled pipeline behavior: blocks high-risk requests, redacts or refuses unsafe output, logs full decision trace.

## Evidence artifacts
- Unit tests: `tests/test_controls.py`
- Baseline outcomes: `eval/baseline_results.csv`
- Controlled outcomes: `eval/controlled_results.csv`
- Metric calculator: `eval/compare.py`

## Key interpretation
- Largest improvement is traceability completeness (+55.0 pp), driven by required logging fields and deterministic reason codes.
- Unsafe and leakage rates dropped materially, indicating practical risk reduction for prompt abuse and secret exposure.
- Residual gap remains in policy compliance (85.0%), motivating stricter claim-grounding and expanded scenario tests in the next iteration.

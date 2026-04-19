# Before / After Comparison

## Overview
This comparison shows how the defensive controls improved the proposed AI-driven SOC design compared to the baseline condition.

| Area | Before | Control Added | After |
|---|---|---|---|
| Prompt safety | AI output could be broad or weakly constrained | Secure prompt template and guardrails | More consistent, scoped, and reviewable outputs |
| Retrieval quality | Context could include irrelevant or overly broad information | Retrieval hardening | More relevant context and reduced exposure |
| Access control | Excessive privilege and overexposed assets increased risk | Least-privilege access design | Reduced unnecessary access and better role separation |
| Traceability | Limited ability to reconstruct actions and decisions | Logging and traceability design | Better auditability and reviewer accountability |
| Human oversight | Risk of relying too heavily on automation | Analyst review checklist | Better quality control and safer final outputs |

## Key Improvement Areas
- reduced unsafe or weakly constrained behavior,
- reduced overexposure of privileged resources,
- improved ability to review and trace decisions,
- improved quality of analyst-reviewed outputs.

# Retrieval Hardening Results

## Goal
Reduce leakage and improve the relevance of information used in AI-supported SOC analysis.

## Hardening Measures
- restrict retrieval to approved sources,
- separate sensitive data from general analysis context,
- require relevance checking before generation,
- avoid unnecessary retrieval breadth.

## Baseline Condition
Without hardening, retrieval may include irrelevant, weakly related, or overly broad context that can reduce output quality or increase exposure risk.

## Evaluated Improvement
After defining retrieval restrictions and relevance checks:
- output context became more focused,
- unnecessary information exposure was reduced,
- analyst review became easier because supporting evidence was more relevant.

## Result
Retrieval hardening improved quality and reduced the chance of over-broad or risky context being used in generated analysis.

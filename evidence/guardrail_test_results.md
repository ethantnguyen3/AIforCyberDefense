# Guardrail Test Results

## Goal
Evaluate whether secure prompt templates and guardrails reduce unsafe or low-quality AI-assisted SOC outputs.

## Test 1: Loosely Structured Prompt
### Input Style
A broad SOC analysis request with minimal constraints.

### Baseline Behavior
The output may be too general, insufficiently evidence-based, or broader than the intended investigation scope.

### Guardrail Applied
The prompt was rewritten to require:
- evidence-based reasoning,
- no unsupported conclusions,
- limited scope,
- escalation when uncertain,
- no unnecessary sensitive detail.

### Result
The revised output was more structured, more cautious, and easier for an analyst to review.

## Test 2: Potentially Unsafe Recommendation
### Input Style
A prompt that could encourage overconfident security action without enough evidence.

### Baseline Behavior
The output may suggest action too aggressively.

### Guardrail Applied
The prompt required confidence limits, evidence checks, and analyst confirmation.

### Result
The revised output reduced unsafe behavior and improved review quality.

## Summary
The guardrail evaluation showed improved output quality, better constraint handling, and reduced risk of unsafe or overconfident AI-assisted recommendations.

# Validation Plan and Decision Gates

**Date:** 1 November 2026  
**Goal:** validate one workflow before product implementation expands.

## Stage 0 — target selection and desk research

Shortlist 3 accounting practices and 2 wholesalers/distributors for discovery. Document software used, intake channels, monthly document volume, the monthly-close or procure-to-pay workflow, exception categories and the person who resolves each one. Compare existing products hands-on where access is available.

**Gate:** proceed only if one exception is recurring, costly and not adequately handled by the incumbent workflow.

## Stage 1 — workflow observation

Observe the process from document arrival to approved accounting/operational outcome.

Capture document types/source channels, volume by type, time per step, handoffs, rekeying, errors/rework, unresolved cases/delays, current systems/spreadsheets and the consequences of missed, duplicate or mismatched documents.

Do not ask only whether users "would use AI". Ask operators to show recent real examples, subject to permission and data minimization.

## Stage 2 — controlled data sample

Acquire documents only with written authorization and a defined purpose. Store real records in a controlled store, never in this public Git repository.

Initial sample design:
- several hundred representative documents across selected partners;
- normal, poor-quality, duplicate, credit, partial-delivery and mismatch cases;
- stratification by supplier, document type and layout;
- gold-standard labels with reviewer-agreement checks;
- separate development examples from a locked evaluation set;
- written permitted purposes, retention, deletion and access controls.

Determine sample size from workflow diversity and required confidence, not from a round-number target.

## Stage 3 — baseline and prototype comparison

Compare the existing process with a human-assisted, read-only prototype. Do not begin with automatic posting or payment actions.

Core metrics:
- critical-field precision and recall;
- share of documents safely accepted without correction;
- abstention and false-match rates;
- reviewer minutes per document;
- exception detection precision/recall;
- time to resolve each exception class;
- downstream correction/reversal rate;
- cost per processed document and per resolved exception;
- onboarding and integration hours;
- operator trust and override rate.

A system that extracts more fields but causes more downstream corrections is not an improvement.

## Stage 4 — paid pilot

After workflow and baseline are known:
- define fixed scope and success criteria with the buyer;
- charge for the pilot or obtain a signed commercial commitment;
- agree data-processing, confidentiality, retention and security terms;
- define human responsibility and rollback;
- review performance weekly;
- measure actual labor/time/cost difference;
- seek renewal or expansion only after results are visible.

A free demo, positive feedback or non-binding interest is not willingness-to-pay evidence.

## Kill or pivot conditions

Stop or change direction if the exception is uncommon/low-cost; incumbent products handle it adequately; permissioned representative data is unavailable; errors require more review than the current process; customer-specific integration makes onboarding uneconomic; volume cannot sustain pricing; support/human operations dominate gross margin; or no buyer will pay for the measured outcome.

## Decision template

Record user, buyer and budget owner; current workflow/software; exact pain and baseline; authorized records; acceptance/failure thresholds; integration dependencies; price, expected volume and cost to serve; results/adverse events; renewal outcome; and the decision (continue, narrow, pivot or stop).

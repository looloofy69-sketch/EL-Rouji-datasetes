# Opportunity Assessment

**Date:** 1 November 2026  
**Decision state:** continue discovery; do not commit to broad implementation.

## 1. Evaluation criteria

Assess each opportunity on problem severity and recurrence, buyer willingness and ability to pay, access to users/data/distribution, competition and switching cost, technical reliability and data rights, implementation/support economics, and potential for defensible learning or workflow integration.

Ratings below are provisional judgments, not measured market scores.

## 2. Ranked opportunities

### A. Exception-first document operations and reconciliation

**Assessment:** strongest current hypothesis; medium-low confidence.

Why it remains interesting:
- business documents are recurring inputs to accounting, procurement, finance and operations;
- extraction alone is increasingly available in local and international software;
- research on real-versus-synthetic extraction shows broad benchmark scores can overstate reliability on real documents;
- value may exist where systems cannot reconcile related evidence or resolve exceptions without manual work.

Risks:
- Fisira, Facturili and DZ Compta already advertise adjacent features;
- exceptions may be too rare, heterogeneous or already handled by incumbent software;
- integration and reviewer support may dominate technical cost;
- privacy, legal and source-rights constraints limit document collection and retention.

**Next test:** observe supplier-document workflows in accounting practices and at least one wholesale/distribution operation; quantify time, errors and delays for one exception class.

### B. Vertical workflow automation

**Assessment:** attractive but too broad to select; medium confidence.

Potential value exists where a repeated process spans multiple systems, files, messaging channels and approvals. A narrow workflow can be automated with deterministic state and human control.

Risks include low frequency, customer-specific processes, expensive integrations and services-heavy onboarding.

**Next test:** identify one workflow with measurable volume, a clear owner, failure cost and defined end state. Reject generic "AI agents for businesses" positioning.

### C. Agent reliability and evaluation

**Assessment:** technically important; medium confidence in need, low-to-medium confidence as a first commercial wedge.

Production studies identify reliability and evaluation problems. International products already cover observability/evaluation categories. Generic tracing or prompt evaluation is not sufficient differentiation.

**Potential wedge:** domain-specific assurance/evaluation for one workflow, with reproducible scenario suites, typed postconditions, failure classification and production drift analysis.

**Next test:** show that existing tools do not provide the failure evidence or actionability required by a specific buyer.

### D. Algerian Arabic and code-switching technology

**Assessment:** meaningful long-term technical opportunity; low commercial confidence.

CAFE, AlgVec and newer ASR research show active work and available research assets. Persistent code-switching and named-entity errors show technical challenges remain.

Risks include dataset rights, dialect/regional diversity, transcription cost, labeling quality, model economics and limited buyer budgets.

**Next test:** identify a funded buyer/use case first—such as call-center speech analytics or transcription QA—then evaluate source rights and representativeness.

### E. General commerce, ERP or invoicing platform

**Assessment:** avoid as initial entry.

KIO, COD Scale, Facturili, Fisira and DZ Compta advertise substantial overlapping surface area. Matching broad feature lists would require major implementation, local support and integrations without clear defensibility.

## 3. Why the document hypothesis is not yet a decision

A real gap requires all four:
1. **Frequency:** the exception occurs often enough.
2. **Economic consequence:** it consumes labor, delays posting/payment, causes leakage or increases compliance risk.
3. **Unserved need:** incumbent tools do not resolve it at acceptable cost.
4. **Reachability:** a buyer can authorize access and pay for a solution.

If any condition fails, this wedge may not be viable.

## 4. Economic model to test

Measure cost per document and cost per resolved exception, not just inference:

`total workflow cost = inference + OCR/parsing + storage + human review + support + integration + rework›

Measure baseline reviewer minutes, exception frequency and resolution time, safe auto-acceptance rate, critical-field error, downstream correction rate, support minutes per customer, onboarding/integration effort, monthly volume and gross margin after human review/hosting.

A low inference bill does not create attractive economics if every document requires human intervention.

## 5. Required decision before implementation

Do not authorize a broad product build until one paid or contractually committed pilot identifies:
- one buyer and user role;
- one input channel;
- one document family;
- one costly exception class;
- incumbent systems to integrate;
- a baseline and measurable target;
- permissioned real data;
- an owner for exception resolution;
- acceptable price and delivery model.

The build decision should follow workflow evidence, not precede it.

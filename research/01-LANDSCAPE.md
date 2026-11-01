# AI, Software and Agent Landscape

**Snapshot date:** 1 November 2026

## 1. Business AI adoption: use is rising faster than deep integration

The UK government's 2026 AI Adoption Survey used a representative sample of 3,503 businesses interviewed between 7 January and 21 April 2026. It reports:
- 32% of businesses using at least one AI technology, double the 2025 survey's 16%;
- use concentrated in administration, marketing and IT;
- 50% of adopters reporting increased productivity, generally modest;
- 14% rating AI highly or critically important to operations;
- 47% of businesses able to estimate expenditure reporting no AI expenditure in 2025.

This shows the difference between experimentation, frequent use and strategic dependence. It is UK-specific and must not be generalized to Algerian firms. [S01]

The OECD 2026 D4SME survey of 2,000+ SMEs across 12 OECD countries reports increasing off-the-shelf use, but uneven strategic and secure integration. Time constraints, maintenance costs, skills gaps and cybersecurity are barriers. Its sample is non-representative, so results are directional rather than population estimates. [S02]

**Implication:** durable product value is more likely to come from improving a recurring workflow than from adding a generic chatbot or agent interface.

## 2. Software engineering productivity: gains are real but context-dependent

A randomized field-experiment study across Microsoft, Accenture and an anonymous Fortune 100 company combined results from 4,867 developers and reported a 26.08% increase in completed tasks for developers with AI coding assistance (standard error 10.3%). It was published online in *Management Science* on 27 February 2026. The treatment was access to an AI coding assistant in specific organizations; it does not imply a 26% gain for every task, developer, codebase or team. [S05]

**Implication:** AI coding changes throughput, but architecture, validation, review, integration, security and maintenance remain necessary. Measure quality, cycle time, rework and downstream defects—not generated code volume.

## 3. Agent deployment: reliability and controllability dominate

The ICML 2026 study *Measuring Agents in Production* surveyed 306 practitioners and conducted 20 case studies across 26 domains. It reports that 68% of agents execute at most 10 steps before human intervention, 70% rely on prompting off-the-shelf models rather than weight tuning, and 74% depend primarily on human evaluation. Reliability remained the leading development challenge. These are study-specific observations, not universal properties of every deployment. [S04]

LangChain's June 2026 State of Agent Engineering survey of 1,300+ professionals reports 57% of respondents had agents in production, 32% cited quality as a top barrier, and observability adoption exceeded evaluation adoption (89% versus 52%). This is a vendor survey and should be treated as self-reported market evidence. [S06]

**Implication:** viable agents should be bounded, observable and recoverable. Use explicit state, typed tool contracts, idempotency, timeouts, budgets, checkpoints, human approval for high-impact actions, deterministic postconditions and replayable traces. Do not assume autonomous long-horizon execution.

## 4. Document intelligence: aggregate scores can conceal deployment risk

The October 2026 EMNLP Industry Track paper *What 1,114 Documents Reveal About Schema-Driven Extraction* studies 1,114 documents across 12 categories and 8 domains, with 7,197 annotated fields. It reports that synthetic documents overestimated accuracy by 38–45 percentage points on one real-document category; model performance varied materially by category even when aggregate scores were similar. [S03]

**Implication:** validate on representative, permissioned local documents. Critical fields need field-level scoring, explicit abstention, provenance, reviewer correction and downstream error measurement. Average OCR/extraction accuracy is insufficient.

## 5. Model and infrastructure economics

Do not select a model solely on benchmark rank, parameter count or advertised tokens per second. Evaluate:
- total loaded memory and runtime overhead, not just active parameters;
- throughput under expected concurrency and context lengths;
- quality on real task inputs;
- structured-output reliability and abstention;
- batching, quantization and serving trade-offs;
- GPU/CPU utilization, electricity, storage and networking;
- p50/p95 latency, retries, failure rate and fallback cost;
- privacy, data residency and vendor terms;
- engineering and operational cost of self-hosting.

Open weights can improve control, but self-hosting is not automatically cheaper or more reliable. Compare total cost per successful task, not token price alone.

## 6. Security and operational requirements

Treat prompts, files, retrieved text, tool outputs and dataset rows as untrusted input. Minimum controls include prompt-injection defenses, tenant isolation, secret handling and log redaction, tool allowlists, least privilege, file-type/size validation, malware scanning, auditability, retention/deletion and adversarial evaluation.

## 7. Research consequence

The strongest technical pattern is **bounded automation with explicit verification**. For EL-Rouji, agents should orchestrate well-defined operations, not replace control logic. Preserve human review for ambiguity and high-impact actions; measure workflow outcomes.

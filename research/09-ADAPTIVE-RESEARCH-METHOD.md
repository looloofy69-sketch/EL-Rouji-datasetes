# Adaptive Research Method

**Version:** 1.0  
**As of:** 1 November 2026  
**Objective:** make research responsive to new information without allowing every new signal to cause uncontrolled scope expansion.

## 1. Research is a loop, not a report

The operating cycle is:

1. Frame a decision or uncertainty.
2. Map the landscape around it.
3. Search broadly across multiple evidence types.
4. Follow the strongest signals into focused research.
5. Search deliberately for counter-evidence and substitutes.
6. Verify material claims against primary sources or direct product tests.
7. Update the evidence and hypothesis graph.
8. Reassess affected decisions and opportunity rankings.
9. Define what should be monitored and what event reopens the question.

New information can create a new hypothesis, weaken an existing one, change the timing, change the target buyer or invalidate a prior conclusion. The research archive must preserve that evolution.

## 2. Search modes

Use the search mode that fits the question; do not rely on one query style.

| Mode | Search targets |
|---|---|
| Reconnaissance | sector maps, market reports, strategy documents, academic surveys, industry associations |
| Actor mapping | buyers, regulators, suppliers, competitors, partners, professional bodies, investors |
| Workflow discovery | standard operating procedures, forms, manuals, user discussions, case studies, interviews |
| Product reality | documentation, pricing, APIs, demos, changelogs, reviews, support articles, trials |
| Technology feasibility | papers, benchmarks, open-source repositories, model cards, standards, deployment tests |
| Policy and regulation | official gazettes, regulator decisions, implementing decrees, official circulars, procurement notices |
| Economics | budgets, prices, payroll, transaction costs, volumes, contract values, cost drivers and willingness to pay |
| Substitutes | manual work, internal tools, spreadsheets, outsourcing, consultants, existing suites and doing nothing |
| Counter-evidence | failure reports, adverse results, implementation delays, customer churn, limitations, competing explanations |
| Validation | direct observations, permissioned artifacts, paid pilots, integration tests and measured outcomes |

## 3. Search expansion procedure

For each material research question:

- Start with the user's exact wording and the decision behind it.
- Expand into synonyms, technical terms, local terminology and relevant Arabic/French/English variations.
- Search by sector, workflow, buyer, competitor, regulator, technology, dataset and adjacent industry.
- Search in at least two directions: evidence supporting the hypothesis and evidence that would disprove it.
- Follow references from strong sources to the underlying primary data, cited regulations, datasets, code or named actors.
- Check the date of the event and the date of publication separately.
- Record what was searched and what remains inaccessible when that changes confidence.
- Stop when additional search is unlikely to change the decision, not merely after an arbitrary count of results.

Search breadth should increase when the subject is new, fragmented, poorly measured or high-impact. Search should narrow as the decision, actors, workflow and evidence become specific.

## 4. Claim and source record

Every material claim should be traceable to a source record with:

- unique source and claim IDs;
- exact claim in a concise sentence;
- publisher/author and source type;
- canonical URL or repository reference;
- publication date, event date and access date;
- geography, sector, sample, denominator and measurement unit;
- method, version and time period;
- quality class and whether primary, secondary, academic, vendor or anecdotal;
- what the source does not establish;
- counter-evidence or contradictory measurements;
- affected hypotheses and decisions;
- refresh trigger.

Keep source facts separate from interpretation. Never turn a vendor feature statement into a verified capability or a government announcement into a completed implementation.

## 5. Evidence hierarchy and triangulation

Prefer the source closest to the underlying fact:
- legislation: official gazette and regulator interpretation;
- official activity: agency or ministry primary release, procurement record or audited report;
- product capability: tested product behavior and technical documentation over marketing pages;
- technical performance: reproducible benchmark, paper methods, code and real input distribution;
- demand: observed workflow, purchase record, paid pilot and renewal over stated interest;
- market size: explicit population and denominator over unsourced market estimates.

Primary sources can still be incomplete, selective or outdated. Triangulate with independent evidence and inspect the methodology.

## 6. Dynamic hypothesis graph

Represent relationships explicitly:
- supports;
- contradicts;
- depends on;
- substitutes for;
- affected by;
- reopens;
- supersedes.

A decision should point to its assumptions, claims, alternatives, known risks and trigger conditions. When a source changes, identify every dependent decision rather than updating only the document where the claim first appeared.

Preserve the original decision and its evidence. Create a new version with the reason for change; do not erase the earlier reasoning.

## 7. Reopening triggers

Reopen a hypothesis or decision when:
- a law, implementing regulation, budget or procurement programme changes;
- a competitor launches, prices or integrates a capability that changes the gap;
- a new model, benchmark or open-source release materially changes technical feasibility or unit cost;
- a data source becomes available, restricted or withdrawn;
- payment, logistics, hosting or infrastructure economics change;
- actual buyer behavior contradicts stated need;
- pilot accuracy, time savings or conversion crosses a pre-defined threshold;
- a major assumption is no longer true.

Assign monitoring cadence by volatility and consequence. Fast-moving model releases may need frequent review; slow-moving demographic or sector baselines may need less frequent updates. Prefer event-driven checks to meaningless routine refreshes.

## 8. Search quality controls

- Use different queries for demand, competition, substitutes, technical feasibility, legal constraints and economics.
- Search outside the immediate geography to identify substitutes and transferable patterns, but label transferability limits.
- Search in local languages where the market operates differently from English-language coverage.
- Seek negative cases and failed deployments.
- Record source access failures; do not substitute a weaker source without stating it.
- Never treat absence of search results as proof that a product, policy or competitor does not exist.
- Preserve the uncertainty of every estimate and avoid false precision.
- Review the research map itself when repeated discovery reveals a missing dimension.

## 9. Decision output

Each research pass should finish with:
- what is newly known;
- what changed from the prior pass;
- what remains unverified;
- which hypotheses gained or lost support;
- which decisions should remain open, be narrowed or be reversed;
- the next highest-value research action;
- the event or evidence that would change the direction.

# Adaptive Search Watchlist and Query Playbook

**Version:** 1.0  
**As of:** 1 November 2026  
**Purpose:** maintain a living search system that discovers changes across sectors, technologies, regulation, competition and economics.

## 1. Search from a decision, not a keyword

A weak search starts with "AI opportunities Algeria." A useful search starts with a testable decision:
- Could a local AI/compute service be viable?
- Which organizations must buy security monitoring or privacy operations?
- Which workflows remain unserved by current sector platforms?
- Does a regulatory change create a real purchase obligation?
- Can a new model or infrastructure price change unit economics?

Translate each decision into a search matrix:

**actor × workflow × technology × local terminology × evidence type × date**

Do not restrict a search to "AI". Search the workflow, current tool, form, procurement category, job role, regulation and alternative implementation as well.

## 2. Search passes

### Pass A — discover the terrain
Search market reports, strategies, sector plans, regulator pages, academic surveys, professional associations, directories and official statistics. Discover named actors, institutions, products, processes, legal instruments and datasets.

### Pass B — resolve entities
For each newly discovered actor, search:
- official website and product documentation;
- services, pricing, API/SDK, integrations and deployment model;
- changelog, support articles, status page and product release dates;
- leadership, ownership, funding, partnerships and hiring;
- client references, public contracts and tender awards;
- complaints, reviews, outages and implementation failures;
- licensing, certifications, terms, privacy and data location.

A newly discovered company or partnership should trigger searches for its product, technology partner, customer, procurement, financing and competitors.

### Pass C — reconstruct workflows
Search the actual business task and local terms in Arabic, French and English:
- forms, registers, declarations, notices and operational documents;
- standard operating procedures, manuals and user guides;
- role descriptions and job vacancies showing who performs the work;
- accounting, banking, logistics, inventory and sector-system integrations;
- forums, community questions, reviews and support tickets where accessible.

### Pass D — test the commercial claim
Search budgets, procurement notices, award outcomes, price lists, financial statements, investment rounds, replacement contracts, renewals and buyer statements. A public tender is evidence of an intended purchase, not proof of award or recurring demand.

### Pass E — search against the hypothesis
Search exact phrases such as:
- "[problem] already solved by software"
- "[workflow] alternatives"
- "[competitor] limitations / API / pricing / support / integration"
- "[sector] failed digital transformation project"
- "[technology] adoption barriers Algeria"
- "[regulation] implementation guidance / enforcement / transition period"
- "[product] outage / migration / cancellation / customer complaint"

A research pass is incomplete if only supportive evidence is searched.

## 3. Query patterns

Use targeted site and phrase queries where the source landscape is known. Examples:

### Algerian primary-source searches
- site:joradp.dz "décret" "données" "interopérabilité"
- site:anpdp.dz loi 25-11 registre traitements DPO
- site:arpce.dz cloud computing autorisation opérateurs
- site:bank-of-algeria.dz prestataires de services de paiement instruction
- site:aps.dz "système national" numérisation secteur
- site:cerist.dz marchés publics cybersécurité GPU sauvegarde
- site:mdn.dz stratégie nationale sécurité systèmes information
- site:sgbv.dz augmentation capital data center cloud Algérie

### Competitor and product searches
- "[product]" API integration documentation
- "[product]" pricing support limitations changelog
- "[workflow]" software Algeria
- "[workflow]" Dext AutoEntry ERP integration alternatives
- "[competitor]" tender award procurement Algeria
- "[technology]" local provider Algeria SLA data center

### Technical research
- "[task]" benchmark 2026 reproducible evaluation
- site:arxiv.org "[task]" real-world evaluation
- site:aclanthology.org Algerian Darija ASR NER code-switching
- site:github.com "[dataset or model]" license
- site:huggingface.co datasets Algerian Arabic Darija
- "[model or inference framework]" price throughput latency 2026

### Demand and workflow searches
- "[job title]" Algeria "missions" logiciels
- "[sector]" Algeria consultation appel d'offres logiciel
- "[workflow]" coûts retards erreurs Algérie
- "[process name]" formulaire guide procédure Algérie
- "[service]" satisfaction problème utilisateurs Algérie

Translate and adapt terms instead of mechanically translating phrases. Search the language used by the actual buyer and institution.

## 4. Search the full evidence lifecycle

For laws, programmes, procurements and products, track state transitions:

| Evidence object | States to distinguish |
|---|---|
| Law/regulation | announced → published → effective → implementing text issued → enforcement observed |
| Public programme | proposed → funded → tendered → contracted → deployed → used → renewed |
| Procurement | notice → consultation → clarification/amendment → deadline → award → delivery/acceptance → renewal |
| Product | announced → waitlist/beta → generally available → production references → independently tested → maintained |
| Dataset/model | announced → accessible → license verified → data inspected → reproducible evaluation → production permission |
| Startup/funding | application/announcement → approved → closed → funds received → investment deployed → commercial performance |

Never collapse these states. For example, "authorized to constitute as a PSP" is not "authorized to operate"; a tender notice is not an awarded contract.

## 5. Evidence record and decision graph

A research claim should retain:
- claim ID and concise statement;
- source ID, canonical URL, publisher and source type;
- event date, publication date and access date;
- geographic and organizational scope;
- sample, denominator, unit and method where applicable;
- current status in the evidence lifecycle;
- what it proves and what it does not prove;
- conflicting evidence;
- linked opportunity hypotheses and decisions;
- next verification and refresh trigger.

Link records with: supports, contradicts, depends on, substitutes for, reopens, supersedes. When one source changes, identify all claims and decisions that depend on it.

## 6. Monitoring cadence

Use event-driven monitoring first; intervals are maximum review guides, not a requirement to create noise.

| Stream | Review guide | Reopen immediately when |
|---|---|---|
| Official gazette, regulator, privacy/security rules | Weekly during major reform; otherwise monthly | New law, decree, circular, guidance, licence or enforcement |
| Public procurement and contract awards | Weekly | Matching tender, addendum, award, contract cancellation or renewal |
| Competitor product/pricing/API/release updates | Monthly; more often for fast-moving products | New launch, meaningful price change, local integration or product shutdown |
| Models, inference tools, benchmarks and security advisories | Weekly | Material cost/performance change, new vulnerability or new license terms |
| Sector statistics, economic conditions and funding | Monthly/quarterly by source cadence | New official data, budget, sector strategy or major company financing |
| Academic research and datasets | Monthly | New benchmark, dataset release, license change or reproducibility result |
| Buyer workflow and pilot evidence | At every interaction | Contradiction of a critical assumption or economic threshold |

## 7. Stop rules

Do not keep searching because more results exist. Stop a pass when:
- decision-relevant actors and alternatives are mapped sufficiently;
- strongest claims are verified at the right level;
- material counter-evidence has been examined;
- remaining uncertainty is explicit;
- a clear next experiment or monitoring trigger is identified;
- further web searches are unlikely to change the decision.

Reopen the pass when a trigger fires. Preserve the previous conclusion and explain why the new evidence changes—or does not change—it.

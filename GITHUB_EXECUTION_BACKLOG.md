# GitHub Execution Backlog — Deterministic SEO Crawler Platform

Repository: `web-crawler`

---

## 1) LABEL TAXONOMY

| Label | Purpose | Color |
|---|---|---|
| type:epic | Parent tracking issues for multi-issue capability delivery. | #5319E7 |
| type:feature | User-facing or platform capability implementation item. | #1D76DB |
| type:task | Engineering task/subtask with concrete output. | #0E8A16 |
| type:infra | Infrastructure/platform operations work. | #0052CC |
| type:architecture | Deterministic architecture, ADR, and structural decisions. | #BFDADC |
| type:testing | Test harnesses, deterministic fixtures, and validation work. | #FBCA04 |
| type:security | Security, privacy, secrets, and access control work. | #D93F0B |
| type:observability | Tracing, metrics, logs, alerting, and SLO work. | #6F42C1 |
| type:research | Time-boxed discovery spikes with decision output. | #C2E0C6 |
| priority:p0 | Critical path / release blocker. | #B60205 |
| priority:p1 | High priority, near-term sprint delivery. | #D93F0B |
| priority:p2 | Important but not immediate blocker. | #FBCA04 |
| priority:p3 | Nice-to-have / optimization / post-MVP. | #0E8A16 |
| area:crawler-core | Core crawl orchestration and run-state logic. | #1D76DB |
| area:url-normalization | URL identity, canonical normalization profile logic. | #006B75 |
| area:frontier | Frontier queue ordering, claim, and state transitions. | #0366D6 |
| area:scheduler | Global scheduler, site ordering, worker eligibility. | #5319E7 |
| area:fetcher | HTTP fetch pipeline and transport behavior. | #0E8A16 |
| area:rendering | Playwright/Chromium render flow and policies. | #C5DEF5 |
| area:artifacts | Screenshot/DOM/log artifacts and metadata persistence. | #A2EEEF |
| area:ai | AI enrichment pipeline and model orchestration. | #7057FF |
| area:vector-store | Embedding storage/retrieval and ANN behavior. | #BFD4F2 |
| area:gsc | Google Search Console integration and sync. | #F9D0C4 |
| area:ga4 | Google Analytics 4 integration and sync. | #FEF2C0 |
| area:visualization | Aggregation APIs for graph/timeline/heatmap views. | #D4C5F9 |
| area:frontend | Frontend explorer and UI data integration. | #C5DEF5 |
| area:backend | API/control-plane services and workers. | #1D76DB |
| area:postgres | PostgreSQL schema, indexes, partitions, SQL paths. | #006B75 |
| area:redis | Redis leases, buckets, hot-path cache/streams. | #A1887F |
| area:kubernetes | K8s deployment, scaling, and ops manifests. | #326CE5 |
| area:security | Security/privacy controls and compliance boundaries. | #D93F0B |
| area:observability | OTel metrics/traces/logging and dashboards. | #6F42C1 |
| area:testing | Unit/integration/E2E/replay test suites. | #FBCA04 |
| area:devex | CI/CD, local dev environment, tooling quality-of-life. | #8A63D2 |
| milestone:mvp | Included in MVP scope. | #0E8A16 |
| milestone:production-ready | Required for production launch readiness. | #1D76DB |
| milestone:ai | AI enrichment and ranking features scope. | #7057FF |
| milestone:scaling | Scale-out, distributed operation, performance scope. | #0366D6 |
| milestone:hardening | Determinism hardening, replay assurance, release polish. | #B60205 |
| status:blocked | Cannot proceed due to dependency/blocker. | #B60205 |
| status:ready | Refined and ready for implementation. | #0E8A16 |
| status:in-progress | Actively being worked on. | #FBCA04 |
| status:review | In PR/review/verification phase. | #5319E7 |
| status:done | Completed and accepted. | #1D76DB |
| deterministic | Must maintain deterministic behavior guarantees. | #000000 |
| replay-safe | Must support reproducible replay and verification. | #4B0082 |
| idempotent | Requires idempotent write/merge/retry semantics. | #2E8B57 |

---

## 2) MILESTONES

| Milestone | Objective | Included Scope | Exit Criteria | Dependencies |
|---|---|---|---|---|
| M1 Foundations | Deliver deterministic crawl core without browser rendering. | Repo setup, ADR process, CI/CD, local env, core Postgres schema/partitioning, URL normalization profile versioning, deterministic frontier order, advisory locks, claim query, rate limiting, fetch/extract, pause/resume, crash recovery. | Single-site deterministic crawl run can start/pause/resume/recover with reproducible URL order and idempotent persistence. | None |
| M2 Rendering | Add deterministic JS rendering pipeline. | Playwright/Chromium pool, image digest pinning, render policy versioning, consent handling, pre/post consent capture, render artifacts and logs. | Rendered and non-rendered pages produce stable reproducible outputs with consent-blocked fallback state captured. | M1 |
| M3 Analysis & Visualizations | Ship API and frontend visibility into crawl results. | Aggregation APIs, crawl tree/site graph/depth heatmap/status timeline endpoints, frontend explorer and artifact inspection. | UI can inspect crawl outputs with progressive drill-down and stable API contracts. | M1, M2 |
| M4 Integrations | Integrate Google data sources deterministically. | GSC OAuth + rolling reingest window, GA4 metadata/compatibility discovery + normalized page key mapping, idempotent ingest pipelines. | GSC/GA4 enrichment is quota-aware, replay-safe, and idempotently merged. | M1, M3 |
| M5 AI Intelligence | Deliver deterministic AI enrichment and ranking. | Feature store, vector store integration, duplicate detection, anomaly detection, priority scoring, explainability layer with pinned versions and stable batching. | AI outputs reproducible with pinned model/feature versions and deterministic candidate ordering. | M1, M3, M4 |
| M6 Scale & Operations | Production-grade distributed and observable operations. | OTel instrumentation, security hardening, distributed deployment, Kubernetes scaling and scheduling ops. | Platform runs in distributed mode with SLO telemetry, secure secret handling, and scale controls. | M1–M5 |
| M7 Hardening & Release | Validate deterministic guarantees and release readiness. | Deterministic replay E2E suite, fixture data, failover/recovery drills, release checklist and go-live hardening. | Replay suite green, hardening checklist complete, release decision gates passed. | M1–M6 |

---

## 3) EPICS

| Epic Title | Description | Milestone | Priority | Labels | Success Outcome |
|---|---|---|---|---|---|
| Repository & Delivery Setup | Establish repo standards, ADRs, CI, environments, and delivery conventions. | M1 Foundations | p0 | type:epic, area:devex, milestone:mvp | Team can deliver deterministic platform work with governed process and CI gates. |
| Deterministic Crawl Core | Implement deterministic crawl run state machine and baseline orchestration. | M1 Foundations | p0 | type:epic, area:crawler-core, deterministic | Crawl runs are reproducible and recoverable by design. |
| URL Identity & Normalization | Implement versioned URL normalization identity model and policies. | M1 Foundations | p0 | type:epic, area:url-normalization, deterministic | Same URL inputs map to stable identities across runs by profile version. |
| Frontier Ordering & Claiming | Implement deterministic frontier sort keys, persistence, and claim semantics. | M1 Foundations | p0 | type:epic, area:frontier, area:postgres, deterministic | Frontier order and claims are stable, auditable, and race-safe. |
| Scheduler & Advisory Locks | Build global site scheduler with one active worker per site via advisory locks. | M1 Foundations | p0 | type:epic, area:scheduler, area:postgres | Exactly one active site-worker per site with stable scheduling order. |
| Fetch Pipeline & Extraction | Implement deterministic fetch + extraction stages with persisted transitions. | M1 Foundations | p0 | type:epic, area:fetcher, area:backend | Fetch/extract results are idempotent and deterministic per run config. |
| Pause/Resume & Crash Recovery | Add graceful pause boundaries and recovery from expired leases/crashes. | M1 Foundations | p0 | type:epic, area:crawler-core, replay-safe | Runs resume safely without duplicate side effects. |
| Rendering & Browser Pool | Build shared Playwright rendering pool with pinned Chromium digest. | M2 Rendering | p0 | type:epic, area:rendering, milestone:production-ready | Deterministic rendering capacity is production-ready. |
| Render Policies & Consent Handling | Add versioned render policies and consent-block fallback behavior. | M2 Rendering | p0 | type:epic, area:rendering, deterministic | Render decisions and consent outcomes are explicit and replayable. |
| Artifact Persistence | Persist render/fetch artifacts and metadata for diagnostics and replay. | M2 Rendering | p1 | type:epic, area:artifacts, replay-safe | Full artifact trail available for debugging and audits. |
| Visualization Aggregation APIs | Build server-side aggregation APIs for graph/tree/timeline/heatmap. | M3 Analysis & Visualizations | p1 | type:epic, area:visualization, area:backend | Large crawls can be explored without raw payload overload. |
| Frontend Explorer | Implement frontend explorer for crawl navigation and diagnostics. | M3 Analysis & Visualizations | p1 | type:epic, area:frontend, area:visualization | Operators can inspect run/page/issue state end-to-end. |
| GSC Integration | Add OAuth, quota-aware sync, and rolling reingest for Search Console. | M4 Integrations | p1 | type:epic, area:gsc, idempotent | GSC signals reliably enrich crawl pages with corrected late data. |
| GA4 Integration | Add GA4 API integration with metadata compatibility and page mapping versioning. | M4 Integrations | p1 | type:epic, area:ga4, idempotent | GA4 metrics are consistently mapped and replay-safe. |
| AI Feature Store | Build versioned feature store for deterministic AI enrichment inputs. | M5 AI Intelligence | p1 | type:epic, area:ai, area:postgres | AI training/scoring share stable feature definitions. |
| Duplicate Detection | Implement multi-layer duplicate detection (hash then semantic). | M5 AI Intelligence | p1 | type:epic, area:ai, area:vector-store | Duplicate clusters are reproducible and scalable. |
| Anomaly Detection | Implement anomaly scoring pipeline on page/run features. | M5 AI Intelligence | p2 | type:epic, area:ai | Deterministic anomaly detection flags outliers with traceable inputs. |
| Priority Scoring & Explainability | Deliver priority model and explainability output for SEO triage. | M5 AI Intelligence | p1 | type:epic, area:ai | Priority ordering is deterministic and explainable. |
| OpenTelemetry & Observability | Instrument scheduler/worker/render/integration/AI critical paths. | M6 Scale & Operations | p0 | type:epic, area:observability, type:observability | Operational health and SLOs are observable and alertable. |
| Security & Secrets | Implement secret management, token encryption, data redaction, retention controls. | M6 Scale & Operations | p0 | type:epic, area:security, type:security | Platform meets security and privacy requirements for production. |
| Distributed Deployment & Kubernetes | Ship distributed deployment patterns, K8s manifests, autoscaling. | M6 Scale & Operations | p1 | type:epic, area:kubernetes, type:infra | Platform scales across many concurrent site runs reliably. |
| Deterministic Replay Test Suite | Build deterministic replay fixtures and E2E verification harness. | M7 Hardening & Release | p0 | type:epic, area:testing, replay-safe | Determinism claims are continuously verified pre-release. |
| Release Hardening | Final go-live hardening, runbooks, SLO gates, release criteria. | M7 Hardening & Release | p0 | type:epic, milestone:hardening | Production release proceeds with validated reliability and controls. |

---

## 4) IMPLEMENTATION ISSUES (SEQUENCED)

> Sprint notation: S1..S10 (2-week sprints). Each issue is implementation-sized and dependency-ordered.

### Issue 01 — Repository Setup & Branch/Issue Conventions
- **Issue Type:** task
- **Parent Epic:** Repository & Delivery Setup
- **Milestone:** M1 Foundations
- **Sprint:** S1
- **Priority:** p0
- **Labels:** type:task, area:devex, milestone:mvp, status:ready
- **Dependencies:** None

### Summary
Create repository scaffolding for execution: branch strategy, issue templates, PR template, definition-of-done checklist, and contribution conventions.
### Why this matters
Without disciplined delivery conventions, deterministic architecture work will drift and become inconsistent.
### Scope
Add `.github` templates, branching/release conventions, and explicit determinism tags in work item template.
### Acceptance Criteria
- Issue, PR, and ADR templates exist and are enforced in contribution docs.
- Definition-of-done includes determinism/replay/idempotency sections.
- CODEOWNERS and review requirements documented.
### Dependencies
None.
### Testing
Manual validation by opening “new issue/PR” flow in GitHub UI.
### Observability
N/A.
### Security
Require secret scanning and dependency alert settings in checklist.
### Determinism / Replayability
Template sections force explicit deterministic/replay impact declaration.
### Rollback / Recovery
Revert template files safely if conventions need revision.
### Out of Scope
Any runtime platform code.

### Issue 02 — ADR Process & Architecture Decision Registry
- **Issue Type:** architecture
- **Parent Epic:** Repository & Delivery Setup
- **Milestone:** M1 Foundations
- **Sprint:** S1
- **Priority:** p0
- **Labels:** type:architecture, area:devex, deterministic, replay-safe
- **Dependencies:** #01

### Summary
Create ADR structure and seed mandatory ADRs for deterministic guarantees (normalization, frontier order, advisory locks, render policy versioning).
### Why this matters
Determinism requires versioned decisions that are durable and reviewable.
### Scope
ADR folder, naming convention, status lifecycle, and initial ADR stubs.
### Acceptance Criteria
- ADR template includes compatibility, rollback, and determinism sections.
- Initial ADR index published.
- New platform behavior changes require ADR reference.
### Dependencies
#01
### Testing
Peer review process walkthrough.
### Observability
Track ADR IDs in release notes.
### Security
ADR template includes threat and secret-handling impact section.
### Determinism / Replayability
ADR process formalizes versioned rule changes.
### Rollback / Recovery
Mark ADRs superseded/deprecated with migration note.
### Out of Scope
Implementing ADR decisions in code.

### Issue 03 — CI/CD Baseline with Determinism Gates
... (Use template below; omitted repetition in this section for brevity of display; fully expanded in Section 6 patterns and Section 7 execution list.)

### Issue 04 — Local Development Environment Parity
### Issue 05 — PostgreSQL Core Schema (Runs/URLs/Frontier/Results)
### Issue 06 — PostgreSQL Partitioning Strategy for Fact Tables
### Issue 07 — URL Normalization Profile Versioning
### Issue 08 — Deterministic Frontier Sort-Key Persistence
### Issue 09 — Site Scheduler with Advisory Locks
### Issue 10 — Frontier Claim Query + Partial Queued Index
### Issue 11 — Host-Level Redis Token Bucket Rate Limiting
### Issue 12 — Deterministic Fetch Pipeline State Transitions
### Issue 13 — Deterministic Extraction Pipeline
### Issue 14 — Pause/Resume URL-Boundary Semantics
### Issue 15 — Crash Recovery & Lease Expiration Requeue
### Issue 16 — Playwright Rendering Pipeline + Pinned Image Digest
### Issue 17 — Render Policy Versioning + Auto/Always/Off Decisions
### Issue 18 — Consent-Blocked Render Fallback Handling
### Issue 19 — Artifact Persistence Model & Storage Metadata
### Issue 20 — Visualization Aggregation APIs (Tree/Graph/Timeline/Heatmap)
### Issue 21 — Frontend Explorer (Run/Page/Issue/Artifact Views)
### Issue 22 — GSC OAuth + Quota-Aware Sync + Rolling Reingest Window
### Issue 23 — GA4 Metadata Discovery + Compatibility + Page Mapping Versioning
### Issue 24 — AI Feature Store Schema + Feature Version Manifest
### Issue 25 — Vector Store Integration (pgvector) + Stable Retrieval Keys
### Issue 26 — Multi-Layer Duplicate Detection Pipeline
### Issue 27 — Anomaly Detection Pipeline (IsolationForest)
### Issue 28 — Priority Scoring Model Pipeline
### Issue 29 — Explainability Output (SHAP-based) + API Exposure
### Issue 30 — OpenTelemetry Instrumentation End-to-End
### Issue 31 — Security Hardening (Secrets, Token Encryption, Redaction, Retention)
### Issue 32 — Distributed Deployment Topology (Stateless API + Scheduler Leadership)
### Issue 33 — Kubernetes Scaling, HPA, CronJobs, Worker Pools
### Issue 34 — Deterministic Replay Test Suite (Fixture + Re-run Diff Gates)
### Issue 35 — Release Hardening & Go-Live Checklist

> **Execution note:** Use Section 6 template body for each issue with issue-specific values from Section 7 command block.

---

## 5) SPRINT GROUPING

| Sprint | Theme | Issues | Standalone Value | Critical Path | Parallelizable Work | Blockers |
|---|---|---|---|---|---|---|
| S1 | Delivery foundations | #1-#4 | Team can execute with governed flow, CI, local parity. | #1,#2,#3 | #4 in parallel after #1 | None |
| S2 | Deterministic data foundations | #5-#8 | Deterministic URL identity + frontier order persisted in DB. | #5,#7,#8 | #6 parallel with #7 | #5 |
| S3 | Scheduling & crawl hot path | #9-#13 | First deterministic crawl pass fetch+extract with rate limits. | #9,#10,#11,#12 | #13 after #12 | #8 |
| S4 | Operational resilience | #14-#15 | Safe pause/resume and crash recovery for long runs. | #14,#15 | none | #12,#13 |
| S5 | Rendering production path | #16-#19 | Deterministic JS rendering with artifacts and consent fallback. | #16,#17,#18 | #19 parallel after #16 | #15 |
| S6 | UX and analysis APIs | #20-#21 | Users can inspect crawl outcomes in API+UI. | #20,#21 | UI work parallel with API scaffolding | #19 |
| S7 | External integrations | #22-#23 | GSC/GA4 enrichment with idempotent, quota-aware sync. | #22,#23 | #23 can start while #22 in progress | #21 |
| S8 | AI feature + similarity core | #24-#26 | Feature store + semantic duplicate detection ready. | #24,#25,#26 | #25 parallel after #24 schema baseline | #23 |
| S9 | AI scoring + ops instrumentation | #27-#31 | Priority/anomaly/explainability plus observability/security controls. | #30,#31 | #27-#29 parallel streams | #26 |
| S10 | Scale & release | #32-#35 | Distributed/k8s readiness and deterministic release gates. | #34,#35 | #32/#33 parallel | #31 |

---

## 6) GITHUB ISSUE TEMPLATE FORMAT

Use this exact body for each issue (fill placeholders):

```markdown
### Summary
[1-2 sentence concrete implementation objective]

### Why this matters
[Deterministic/platform delivery value]

### Scope
- [in-scope item 1]
- [in-scope item 2]
- [in-scope item 3]

### Acceptance Criteria
- [ ] [verifiable outcome 1]
- [ ] [verifiable outcome 2]
- [ ] [verifiable outcome 3]

### Dependencies
- #[upstream issue number/title]

### Testing
- Unit: [what is validated]
- Integration: [DB/Redis/worker/render/integration path]
- E2E/Replay: [determinism check]

### Observability
- Metrics: [metric names]
- Traces: [span names]
- Logs: [structured fields]

### Security
- [secret handling / least privilege / redaction requirements]

### Determinism / Replayability
- [ordering guarantees]
- [version-pinned inputs]
- [replay verification expectations]

### Rollback / Recovery
- [revert/migration rollback and data safety approach]

### Out of Scope
- [explicitly excluded item 1]
- [explicitly excluded item 2]
```

---

## 7) GITHUB CLI EXECUTION BLOCK

> Replace `ORG/REPO` with your target repository (recommended `web-crawler`).

### 7.1 Create labels
Use `gh label create` for each row from Section 1 (skip if exists):

- `gh label create "type:epic" --color "5319E7" --description "Parent tracking issues for multi-issue capability delivery"`
- `gh label create "type:feature" --color "1D76DB" --description "User-facing or platform capability implementation item"`
- `gh label create "type:task" --color "0E8A16" --description "Engineering task/subtask with concrete output"`
- `gh label create "deterministic" --color "000000" --description "Must maintain deterministic behavior guarantees"`
- *(continue for all labels in Section 1)*

### 7.2 Create milestones
- `gh api repos/ORG/REPO/milestones -f title='M1 Foundations' -f description='Deterministic crawl core without browser rendering'`
- `gh api repos/ORG/REPO/milestones -f title='M2 Rendering' -f description='Deterministic JS rendering and artifacts'`
- `gh api repos/ORG/REPO/milestones -f title='M3 Analysis & Visualizations' -f description='Aggregation APIs and frontend explorer'`
- `gh api repos/ORG/REPO/milestones -f title='M4 Integrations' -f description='GSC and GA4 integrations with idempotent sync'`
- `gh api repos/ORG/REPO/milestones -f title='M5 AI Intelligence' -f description='Feature store, vector retrieval, AI scoring'`
- `gh api repos/ORG/REPO/milestones -f title='M6 Scale & Operations' -f description='Observability, security, distributed ops, k8s'`
- `gh api repos/ORG/REPO/milestones -f title='M7 Hardening & Release' -f description='Replay testing and release hardening gates'`

### 7.3 Create epics first
Create these as issues labeled `type:epic` plus area/priority labels:
1. Repository & Delivery Setup
2. Deterministic Crawl Core
3. URL Identity & Normalization
4. Frontier Ordering & Claiming
5. Scheduler & Advisory Locks
6. Fetch Pipeline & Extraction
7. Pause/Resume & Crash Recovery
8. Rendering & Browser Pool
9. Render Policies & Consent Handling
10. Artifact Persistence
11. Visualization Aggregation APIs
12. Frontend Explorer
13. GSC Integration
14. GA4 Integration
15. AI Feature Store
16. Duplicate Detection
17. Anomaly Detection
18. Priority Scoring & Explainability
19. OpenTelemetry & Observability
20. Security & Secrets
21. Distributed Deployment & Kubernetes
22. Deterministic Replay Test Suite
23. Release Hardening

### 7.4 First 20 implementation issues to create first
Create in this exact order:
1. Repository Setup & Branch/Issue Conventions
2. ADR Process & Architecture Decision Registry
3. CI/CD Baseline with Determinism Gates
4. Local Development Environment Parity
5. PostgreSQL Core Schema (Runs/URLs/Frontier/Results)
6. PostgreSQL Partitioning Strategy for Fact Tables
7. URL Normalization Profile Versioning
8. Deterministic Frontier Sort-Key Persistence
9. Site Scheduler with Advisory Locks
10. Frontier Claim Query + Partial Queued Index
11. Host-Level Redis Token Bucket Rate Limiting
12. Deterministic Fetch Pipeline State Transitions
13. Deterministic Extraction Pipeline
14. Pause/Resume URL-Boundary Semantics
15. Crash Recovery & Lease Expiration Requeue
16. Playwright Rendering Pipeline + Pinned Image Digest
17. Render Policy Versioning + Auto/Always/Off Decisions
18. Consent-Blocked Render Fallback Handling
19. Artifact Persistence Model & Storage Metadata
20. Visualization Aggregation APIs (Tree/Graph/Timeline/Heatmap)

---

## Appendix — Full Issue Metadata Matrix (1-35)

| # | Title | Type | Epic | Milestone | Sprint | Priority | Depends On |
|---|---|---|---|---|---|---|---|
| 1 | Repository Setup & Branch/Issue Conventions | task | Repository & Delivery Setup | M1 | S1 | p0 | - |
| 2 | ADR Process & Architecture Decision Registry | architecture | Repository & Delivery Setup | M1 | S1 | p0 | 1 |
| 3 | CI/CD Baseline with Determinism Gates | infra | Repository & Delivery Setup | M1 | S1 | p0 | 1,2 |
| 4 | Local Development Environment Parity | infra | Repository & Delivery Setup | M1 | S1 | p1 | 1 |
| 5 | PostgreSQL Core Schema (Runs/URLs/Frontier/Results) | architecture | Deterministic Crawl Core | M1 | S2 | p0 | 2,3 |
| 6 | PostgreSQL Partitioning Strategy for Fact Tables | task | Deterministic Crawl Core | M1 | S2 | p0 | 5 |
| 7 | URL Normalization Profile Versioning | feature | URL Identity & Normalization | M1 | S2 | p0 | 5 |
| 8 | Deterministic Frontier Sort-Key Persistence | feature | Frontier Ordering & Claiming | M1 | S2 | p0 | 5,7 |
| 9 | Site Scheduler with Advisory Locks | feature | Scheduler & Advisory Locks | M1 | S3 | p0 | 8 |
| 10 | Frontier Claim Query + Partial Queued Index | feature | Frontier Ordering & Claiming | M1 | S3 | p0 | 8,9 |
| 11 | Host-Level Redis Token Bucket Rate Limiting | feature | Scheduler & Advisory Locks | M1 | S3 | p1 | 9,10 |
| 12 | Deterministic Fetch Pipeline State Transitions | feature | Fetch Pipeline & Extraction | M1 | S3 | p0 | 10,11 |
| 13 | Deterministic Extraction Pipeline | feature | Fetch Pipeline & Extraction | M1 | S3 | p0 | 12 |
| 14 | Pause/Resume URL-Boundary Semantics | feature | Pause/Resume & Crash Recovery | M1 | S4 | p0 | 12,13 |
| 15 | Crash Recovery & Lease Expiration Requeue | feature | Pause/Resume & Crash Recovery | M1 | S4 | p0 | 14 |
| 16 | Playwright Rendering Pipeline + Pinned Image Digest | feature | Rendering & Browser Pool | M2 | S5 | p0 | 15 |
| 17 | Render Policy Versioning + Auto/Always/Off Decisions | feature | Render Policies & Consent Handling | M2 | S5 | p0 | 16 |
| 18 | Consent-Blocked Render Fallback Handling | feature | Render Policies & Consent Handling | M2 | S5 | p0 | 16,17 |
| 19 | Artifact Persistence Model & Storage Metadata | feature | Artifact Persistence | M2 | S5 | p1 | 16,18 |
| 20 | Visualization Aggregation APIs (Tree/Graph/Timeline/Heatmap) | feature | Visualization Aggregation APIs | M3 | S6 | p1 | 13,19 |
| 21 | Frontend Explorer (Run/Page/Issue/Artifact Views) | feature | Frontend Explorer | M3 | S6 | p1 | 20 |
| 22 | GSC OAuth + Quota-Aware Sync + Rolling Reingest Window | feature | GSC Integration | M4 | S7 | p1 | 21 |
| 23 | GA4 Metadata Discovery + Compatibility + Page Mapping Versioning | feature | GA4 Integration | M4 | S7 | p1 | 21 |
| 24 | AI Feature Store Schema + Feature Version Manifest | feature | AI Feature Store | M5 | S8 | p1 | 20,22,23 |
| 25 | Vector Store Integration (pgvector) + Stable Retrieval Keys | feature | AI Feature Store | M5 | S8 | p1 | 24 |
| 26 | Multi-Layer Duplicate Detection Pipeline | feature | Duplicate Detection | M5 | S8 | p1 | 24,25 |
| 27 | Anomaly Detection Pipeline (IsolationForest) | feature | Anomaly Detection | M5 | S9 | p2 | 24 |
| 28 | Priority Scoring Model Pipeline | feature | Priority Scoring & Explainability | M5 | S9 | p1 | 24,26,27 |
| 29 | Explainability Output (SHAP-based) + API Exposure | feature | Priority Scoring & Explainability | M5 | S9 | p1 | 28 |
| 30 | OpenTelemetry Instrumentation End-to-End | observability | OpenTelemetry & Observability | M6 | S9 | p0 | 12,16,22,23,28 |
| 31 | Security Hardening (Secrets, Token Encryption, Redaction, Retention) | security | Security & Secrets | M6 | S9 | p0 | 22,23,30 |
| 32 | Distributed Deployment Topology (Stateless API + Scheduler Leadership) | infra | Distributed Deployment & Kubernetes | M6 | S10 | p1 | 30,31 |
| 33 | Kubernetes Scaling, HPA, CronJobs, Worker Pools | infra | Distributed Deployment & Kubernetes | M6 | S10 | p1 | 32 |
| 34 | Deterministic Replay Test Suite (Fixture + Re-run Diff Gates) | testing | Deterministic Replay Test Suite | M7 | S10 | p0 | 16,22,23,29,30,33 |
| 35 | Release Hardening & Go-Live Checklist | task | Release Hardening | M7 | S10 | p0 | 31,34 |

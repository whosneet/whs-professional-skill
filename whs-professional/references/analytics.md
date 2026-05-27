# WHS Data Analytics & Intelligence Reporting

---

## Table of Contents
1. [Metric Definitions & Calculations](#1-metric-definitions--calculations)
2. [HiPo Intelligence Pack Structure](#2-hipo-intelligence-pack-structure)
3. [CRO vs HiPo Alignment Analysis](#3-cro-vs-hipo-alignment-analysis)
4. [Dashboard Design Principles](#4-dashboard-design-principles)
5. [Leading Indicator Design](#5-leading-indicator-design)
6. [EAP Utilisation Reporting](#6-eap-utilisation-reporting)
7. [Board & ELT Intelligence Pack](#7-board--elt-intelligence-pack)
8. [Power BI Patterns for WHS](#8-power-bi-patterns-for-whs)

---

## 1. Metric Definitions & Calculations

### Frequency Rate Formulas

All frequency rates use **1,000,000 exposure hours** as the denominator (AU standard).

| Metric | Formula | Notes |
|---|---|---|
| **TRIFR** | (Recordable injuries ÷ hours worked) × 1,000,000 | Recordable = LTI + MTI + Fatality |
| **LTIFR** | (LTIs ÷ hours worked) × 1,000,000 | LTI = 1+ full shift lost |
| **AIFR** | (All injuries incl. FAI ÷ hours worked) × 1,000,000 | Broadest measure |
| **LTISR** | (Lost days ÷ hours worked) × 1,000,000 | Severity measure |
| **HiPo Rate** | (HiPo events ÷ hours worked) × 1,000,000 | Most predictive lagging metric |
| **FAI Rate** | (First Aid cases ÷ hours worked) × 1,000,000 | Reporting culture proxy |

### Injury Classification for Recordability

| Classification | Recordable? | Counted in TRIFR? |
|---|---|---|
| Fatality | Yes | Yes |
| LTI | Yes | Yes |
| MTI | Yes | Yes |
| FAI | No | No (in AIFR only) |
| Health Case | No | No |
| NWI / Journey | No | No |

### Hours Worked
Use **actual hours worked** (exclude leave, RDO, sick time). If actual hours are
unavailable, use contracted FTE hours × attendance factor. Document methodology — 
inconsistent hours calculation is the primary source of misleading frequency rate trends.

### Rolling 12-Month vs Calendar Year
Always present both:
- **Rolling 12 months** from report date: smooths seasonal variation, reflects current
  performance trajectory
- **Calendar year to date**: aligns with budgets, targets, and year-on-year comparisons
Point-in-time statistics (single month TRIFR) are misleading at low injury counts — 
one LTI in a 200-person team can swing TRIFR by 5+ points.

---

## 2. HiPo Intelligence Pack Structure

HiPo events are the highest-value signal in any WHS dataset — they represent near-misses
to fatalities or serious injuries. Analyse them disproportionately.

### Core HiPo Analysis Dimensions

**Volume & Rate**
- HiPo count for period vs prior period
- HiPo rate per million hours (by BU, contract, division)
- Trend: rolling 12-month, year-on-year

**Critical Risk Distribution**
- HiPo events by critical risk category (falls, electrical, vehicles, etc.)
- Compare against CRO verification activity distribution — gap = misalignment of effort
- Over-represented critical risks in HiPos vs CRO = under-investment in control verification

**Business Unit Breakdown**
- HiPo count and rate by BU / contract cluster
- Normalise by hours worked, not just raw count
- Flag outliers: contracts with zero HiPos over an extended period may indicate under-reporting

**Investigation Status**
- % HiPos with completed investigation (within required timeframe)
- % with corrective actions closed vs outstanding
- % overdue — flag for management attention

**Classification Analysis**
- Actual vs potential consequence distribution
- How many near-misses had potential severity 5 or 6?
- Bowtie alignment: which critical controls were absent or degraded?

### HiPo Intelligence Pack — Recommended Format

```
1. Headline: [Period] HiPo Summary
   - Count, rate, comparison to prior period, YTD vs target

2. Critical Risk Breakdown
   - Table: Critical Risk | HiPo Count | % of Total | vs Prior Period
   - Highlight top 2-3 priority risks based on distribution

3. BU / Contract Breakdown
   - Table normalised by hours worked
   - Named contracts where rate is above division average

4. Investigation Health
   - % investigations completed on time
   - Corrective action close-out status
   - Outstanding items: responsible manager, due date, days overdue

5. Themes and So-What
   - 2-3 key narratives from the data
   - Management action required (named, time-bound)

6. Appendix: Individual HiPo Register
   - Date | Contract | Brief description | Critical risk | Potential severity |
     Investigation status | Key contributing factor
```

---

## 3. CRO vs HiPo Alignment Analysis

The gap between where CRO (Critical Risk Operations / verification) activity is concentrated
and where HiPo incidents are occurring is a primary strategic diagnostic.

### Why This Gap Matters
If 40% of HiPos involve electrical critical risks but only 10% of CCV activity addresses
electrical controls, the safety system is mis-calibrated — verifying controls that are
not the primary failure pathway.

### Analysis Method

**Step 1: Normalise HiPo distribution by critical risk**
% of HiPos in each critical risk category (rolling 12 months, by BU)

**Step 2: Normalise CCV activity by critical risk**
% of CCV observations/verifications in each critical risk category (same period, same BU)

**Step 3: Calculate alignment gap**
Gap = HiPo % − CCV % for each critical risk
- Positive gap: HiPos exceed CCV attention → under-verified
- Negative gap: CCV activity exceeds HiPo distribution → over-verified (relative)

**Step 4: Visualise**
Radar/spider chart or grouped bar chart works well for this analysis.
- Radar: each axis = one critical risk; two series (HiPo %, CCV %)
- Grouped bar: side-by-side comparison per critical risk category

**Step 5: Prioritise**
Rank critical risks by gap magnitude. Allocate additional CCV effort to highest
positive-gap categories. Present to operations managers with clear recommendation.

### Caveats
- CCV data quality is a known constraint — incomplete records skew the analysis
- HiPo under-reporting creates false low gaps — cross-reference with TRIFR trends
- Always present with a confidence statement about data completeness

---

## 4. Dashboard Design Principles

### Audience-Calibrated Depth

| Audience | Primary need | Format |
|---|---|---|
| Board / ELT | Strategic signal, governance decisions | One-page snapshot; 5–7 KPIs; trend + narrative |
| BU GM / Operations Manager | Portfolio health, escalation triggers | Multi-KPI dashboard; BU breakdown; drill-down |
| WHS Business Partner | Operational detail, contract-level | Full dashboard; contract-level; corrective action tracker |
| Frontline / Supervisor | Own site/team performance | Simplified scorecard; leading indicators; recognition |

### Design Principles

**Lead with the so-what**
Every dashboard should have a text pane or callout box that answers: "What does this
mean and what should the reader do about it?" Numbers without narrative are noise.

**Consistent colour semantics**
- Red = action required / above threshold
- Amber = monitor / approaching threshold
- Green = on track / within target
Never use red for things that are improving (lower TRIFR is good — don't show it red
just because it's the highest value on a scale).

**Trend over point-in-time**
Always show a trend line, not just the current period value. A single data point
is uninterpretable without context.

**Normalise by hours worked**
Raw injury counts are misleading when contract sizes differ. Always present rates.

**Separate systems performance from outcome performance**
Two distinct sections:
- **Lagging** (outcomes): TRIFR, LTIFR, HiPo rate, fatalities
- **Leading** (systems): CCV completion, hazard report rate, corrective action close-out

### Power BI Specific
See Section 8 for Power BI implementation patterns.

---

## 5. Leading Indicator Design

### The Problem with Completion Rates
Completion rates (toolbox completion %, training completion %) are the most common
leading indicators — and the most easily gamed. A facilitator who marks 20 people
as "completed" for a toolbox that lasted 3 minutes has satisfied the metric but not
the purpose.

### Design Criteria for Quality Leading Indicators

A high-quality leading indicator is:
1. **Correlated with future outcomes** — there is a plausible causal pathway to injury reduction
2. **Hard to game** — requires substantive activity, not checkbox completion
3. **Timely** — data available within days/weeks, not quarterly
4. **Actionable** — a poor score tells you what to do, not just that something is wrong

### Recommended Leading Indicator Portfolio

| Category | Indicator | Calculation | Why it matters |
|---|---|---|---|
| Hazard management | Hazard reports per 100 workers per month | (Reports ÷ headcount) × 100 | Reporting culture and psychological safety proxy |
| Hazard management | % hazards closed within due date | Closed on time ÷ total due | System responsiveness |
| Investigation | % HiPo investigations completed within 30 days | On-time completions ÷ total HiPos | Investigation quality and priority |
| Corrective actions | % corrective actions closed on time | On-time closures ÷ total due | Systemic follow-through |
| Critical risk | CCV completion rate vs plan | Completed ÷ planned | Critical control health |
| Critical risk | % degraded controls escalated | Escalations raised ÷ degraded controls found | Control failure visibility |
| Engagement | Near miss reports per 100 workers | Near misses ÷ headcount × 100 | High-value reporting culture indicator |
| Officer | Officer due diligence activities completed | Count of documented activities | Leadership accountability |
| Audit | Conformance rate on internal WHS audits | Conformant items ÷ total items audited | System compliance health |

### Benchmarking Leading Indicators
External benchmarks for leading indicators are rarely available. Use internal trend
as the benchmark: is the indicator improving, stable, or declining over rolling
12 months? Set targets based on internal performance trajectory, not industry averages.

---

## 6. EAP Utilisation Reporting

### Why Track EAP Data
EAP utilisation is a population-level indicator of workforce psychological distress.
Tracking trends helps identify emerging pressures before they manifest as incidents,
workers compensation claims, or turnover.

### EAP Reporting Dimensions

| Dimension | What to report | Notes |
|---|---|---|
| Overall utilisation rate | % of workforce who accessed EAP in period | Per 100 employees; trend vs prior periods |
| Service type breakdown | Counselling vs financial vs legal vs other | Counselling access is the primary distress indicator |
| Issue type (if available) | Work vs personal vs family | Confidentiality — aggregated only, never individual |
| Access method | Phone, face-to-face, online | Indicates accessibility; some populations prefer phone |
| Geography | AU vs NZ; state/territory if volume permits | Jurisdictional variation is common |
| Division / BU breakdown | If EAP provider can report at this level | Requires adequate sample size for confidentiality |

### AU vs NZ EAP Reporting
Report separately. Workforce composition, contract mix, and baseline utilisation rates
differ between AU and NZ populations. Combining without normalisation obscures trends.

### Confidentiality and Privacy
- **Never report individual-level data** — EAP is confidential
- Aggregate to minimum group size ≥10 before reporting breakdowns
- State clearly in reports: "Data provided by EAP provider in aggregated form; no
  individual identifying information was shared or requested"
- In AU: EAP data handling should align with Privacy Act 1988 (Cth) health information provisions

### Interpreting EAP Utilisation
- Low utilisation ≠ low distress — may indicate access barriers, stigma, or lack of awareness
- Sudden spike: investigate contextual factors (restructure, incident, seasonal pressure)
- Sustained elevation: systemic issue requiring intervention beyond EAP
- Downward trend after program launch: may indicate awareness has worn off; consider promotion

---

## 7. Board & ELT Intelligence Pack

### Structure for Division-Level Reporting

**Page 1: Safety Performance Snapshot**
- Headline metrics: TRIFR, LTIFR, HiPo rate, fatalities, LTIs (YTD vs target vs prior year)
- Rolling 12-month trend chart
- Executive narrative: 3–5 sentences — what the numbers mean, not what they are

**Page 2: HiPo Intelligence**
- HiPo count, rate, and critical risk distribution (current period)
- Investigation completion health
- Named contracts or BUs with elevated HiPo activity
- Top emerging risk theme with management action

**Page 3: Critical Risk Status**
- CRO verification completion heatmap: Critical Risk × BU
- Alignment gap summary (where HiPos exceed CRO activity)
- Degraded controls flagged and action status

**Page 4: Program Performance**
- Zero Harm program activity: reach, completion, leading outcomes
- Key program milestones
- Frontline engagement metrics (toolbox completion, hazard reports, near misses)

**Page 5: Regulatory & Compliance**
- Notifiable incidents reported to regulator (period)
- Active improvement / prohibition notices
- Significant legislative updates

**Page 6: Outlook & Decisions Required**
- Emerging risks being monitored
- Explicit asks of the Board/ELT (resources, decisions, endorsement)
- Forward program calendar

### Principles for Board-Level Narrative
- Lead with risk, not activity
- Be explicit about what's going well AND what needs attention
- Avoid WHS jargon without definition
- End every section with: "What this means for the Board/ELT"
- Never bury a call to action in body text — put it in a callout box

---

## 8. Power BI Patterns for WHS

### Data Model Considerations

**Fact tables**
- `fact_incidents` — one row per incident; keys to date, contract, worker, critical risk
- `fact_hours_worked` — one row per contract per period; used for frequency rate calculations
- `fact_ccv` — one row per CCV observation; keys to date, contract, critical risk
- `fact_hazard_reports` — one row per hazard report

**Dimension tables**
- `dim_date` — standard date dimension with financial year, rolling periods
- `dim_contract` — contract details including BU, region, Division
- `dim_critical_risk` — critical risk categories for consistent classification
- `dim_injury_type` — LTI, MTI, FAI, HiPo, etc. with recordable flag

**Calculated measures (DAX patterns)**
```
TRIFR = 
DIVIDE(
    CALCULATE(COUNTROWS(fact_incidents), 
        fact_incidents[recordable] = TRUE()),
    SUM(fact_hours_worked[hours]),
    0
) * 1000000

Rolling12mTRIFR = 
CALCULATE(
    [TRIFR],
    DATESINPERIOD(dim_date[date], LASTDATE(dim_date[date]), -12, MONTH)
)
```

### Visualisation Recommendations

| Analysis | Chart type | Notes |
|---|---|---|
| Frequency rate trend | Line chart (rolling 12m) | Include target line |
| HiPo by critical risk | Stacked bar or treemap | Normalise by hours |
| CRO vs HiPo alignment | Radar / spider chart | Two series; gap = misalignment |
| Corrective action status | Donut + bar | Status breakdown + age analysis |
| BU performance comparison | Small multiples or matrix | Consistent scale across BUs |
| EAP utilisation trend | Line with area fill | Monthly trend; separate AU/NZ |

### Data Source Connections
- **Incident management system** (e.g. INX, Cintellate, Donesafe, Mango): primary incident data; extract via scheduled report or API
- **WHS management system platform** (e.g. Lucidity, Ideagen): organisational structure, contract mapping; use for hierarchy alignment
- **Rapid Global**: contractor management data; check API/export options for prequalification status
- **SharePoint / equivalent**: program tracking data, CCV records (if not in incident system)
- **Payroll/HRIS**: hours worked data — critical for accurate frequency rate calculation

### Refresh and Governance
- Automated refresh: daily or weekly depending on report cadence
- Data validation: build row count and completeness checks into the Power BI dataflow
- Version control: document DAX measures and data transforms in a `data_dictionary.md` file
- Access control: board reports should have restricted RLS by audience

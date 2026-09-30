# WHS Data Analytics & Intelligence Reporting

How to define, calculate, test and normalise WHS metrics; HiPo, CCV and EAP
intelligence; leading indicators; dashboards, board packs and Power BI
patterns; and the ethics and governance of predictive safety models.

---

## Table of Contents
1. [Metric Definitions & Calculations](#1-metric-definitions--calculations)
2. [HiPo Intelligence Pack Structure](#2-hipo-intelligence-pack-structure)
3. [CCV vs HiPo Alignment Analysis](#3-ccv-vs-hipo-alignment-analysis)
4. [Dashboard Design Principles](#4-dashboard-design-principles)
5. [Leading Indicator Design](#5-leading-indicator-design)
6. [EAP Utilisation Reporting](#6-eap-utilisation-reporting)
7. [Board & ELT Intelligence Pack](#7-board--elt-intelligence-pack)
8. [Power BI Patterns for WHS](#8-power-bi-patterns-for-whs)
9. [Statistical Treatment of Rates — Confidence Intervals, Funnel Plots and SPC](#9-statistical-treatment-of-rates--confidence-intervals-funnel-plots-and-spc)
10. [Exposure-Based Normalisation](#10-exposure-based-normalisation)
11. [Predictive Analytics — Ethics and Governance](#11-predictive-analytics--ethics-and-governance)

---

## 1. Metric Definitions & Calculations

### Frequency Rate Formulas

All frequency rates use **1,000,000 exposure hours** as the denominator (AU standard).

| Metric | Formula | Notes |
|---|---|---|
| **TRIFR** | (Recordable injuries ÷ hours worked) × 1,000,000 | Recordable (TRI) = Fatality + LTI + RWI + MTI (see note below) |
| **LTIFR** | (LTIs ÷ hours worked) × 1,000,000 | LTI = 1+ full shift lost |
| **RWIFR** | (RWIs ÷ hours worked) × 1,000,000 | RWI = restricted/alternate duties without a full shift lost (see definition below) |
| **MTIFR** | (MTIs ÷ hours worked) × 1,000,000 | MTI = medical treatment beyond first aid; no lost shift, no restricted duties |
| **AIFR** | (All injuries incl. FAI ÷ hours worked) × 1,000,000 | Broadest measure |
| **LTISR** | (Lost days ÷ hours worked) × 1,000,000 | Severity measure |
| **HiPo Rate** | (HiPo events ÷ hours worked) × 1,000,000 | Most predictive lagging metric |
| **FAI Rate** | (First Aid cases ÷ hours worked) × 1,000,000 | Reporting culture proxy |

### Injury Classification for Recordability

| Classification | Recordable? | Counted in TRIFR? |
|---|---|---|
| Fatality | Yes | Yes |
| LTI | Yes | Yes |
| RWI (restricted work injury) | Yes | Yes |
| MTI | Yes | Yes |
| FAI | No | No (in AIFR only) |
| Health Case | No | No |
| NWI / Journey | No | No |

**RWI** = the worker returns to work but cannot perform the full range of
pre-injury duties (restricted or alternate duties) without losing a full
shift. RWI sits between LTI and MTI in severity and **is recordable** —
omitting RWI from the recordable set understates TRIFR and silently rewards
moving injured workers onto restricted duties to avoid an LTI classification.

> **Provenance note on RWI.** RWI is a US OSHA-origin recordability concept
> (restricted-work/job-transfer cases under 29 CFR 1904.7) adopted here as a
> documented organisational convention; under the (now-withdrawn) AS 1885.1
> the AU convention was TRIFR = Fatality + LTI + MTI, with AS 1885.1 itself
> classifying occurrences as lost-time vs no-lost-time rather than defining a
> distinct "RWI" recordable tier. Counting restricted-duty cases as
> recordable and including them in TRIFR is, however, mainstream current AU
> practice — SafeWork NSW's *Measuring and reporting WHS information* guidance
> (based on Safe Work Australia's 2017 report *Measuring and reporting on work
> health and safety*, by Dr Sharron O'Neill) treats restricted-duty cases as
> recordable injuries within TRIFR. This skill
> therefore adopts the four-tier set (Fatality + LTI + RWI + MTI) as its
> canonical TRI definition. Apply it consistently and document it in the data
> dictionary so the figure remains comparable across reporting periods.

### Hours Worked
Use **actual hours worked** (exclude leave, RDO, sick time). If actual hours are
unavailable, use contracted FTE hours × attendance factor. Document methodology — 
inconsistent hours calculation is the primary source of misleading frequency rate trends.

### Rolling 12-Month vs Calendar Year
Always present both:
- **Rolling 12 months** — the 12 closed months ending at the last closed reporting
  period: smooths seasonal variation, reflects current performance trajectory
- **Calendar year to date**: aligns with budgets, targets, and year-on-year comparisons
Point-in-time statistics (single month TRIFR) are misleading at low injury counts —
a 200-person team works roughly 32,000 hours a month, so a single LTI moves the
monthly rate by about 30 points (1 ÷ 32,000 × 1,000,000 ≈ 31); the same LTI moves
the rolling 12-month rate (~384,000 hours) by only ~2.6 points.

### SIF / pSIF — Serious Injury & Fatality Classification

Frequency rates treat every recordable equally — a sutured laceration counts
the same as an amputation. The SIF lens corrects for that by classifying
**actual and potential severity** separately from recordability:

- **SIF (Serious Injury or Fatality)** — an actual outcome that is fatal,
  life-threatening, or life-altering (e.g. fatality, permanent impairment,
  amputation, serious head/spinal injury)
- **pSIF (potential SIF)** — an incident or near miss that did not produce a
  serious outcome but plausibly could have under slightly different
  circumstances. Classified on potential consequence, not actual outcome

**Why TRIFR dilutes the SIF signal**: SIF events are a small fraction of
recordables, so TRIFR movement is dominated by low-severity injury volume.
Research associated with the contemporary SIF movement (US-led collaborative
studies from the early 2010s onward; treat specific published ratios with
caution) indicates the precursors of serious injuries differ from those of
minor injuries — driving down minor injury frequency does not reliably reduce
fatality risk, and the Heinrich-triangle assumption of proportionality does
not hold at the severe end. A falling TRIFR alongside a flat or rising pSIF
rate is a deteriorating risk profile wearing an improving costume.

**SIF-potential criteria (energy-based)**: classify an event as pSIF where a
high-energy source could have reached a person with direct controls absent,
failed, or unverifiable — e.g. fall from height, mobile plant/vehicle and
pedestrian interaction, electrical contact, suspended or falling loads,
stored/released energy, trench collapse, confined space atmosphere. The test
is: energy above a serious-harm threshold + worker exposure + control
absence/failure. Energy-based definitions keep classification consistent and
auditable; "gut feel" severity calls do not.

**Reporting**: report SIF and pSIF counts/rates alongside the HiPo metrics in
§2 — in most AU systems pSIF and HiPo overlap heavily, so define the
relationship explicitly in the data dictionary (one common pattern: HiPo is
the event-level flag; SIF/pSIF is the severity taxonomy applied to it).
Track the direct-control status for each pSIF, investigate at the depth the
potential warranted, and never let a low TRIFR headline a report in which
pSIF events occurred.

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
- Compare against CCV verification activity distribution — gap = misalignment of effort
- Over-represented critical risks in HiPos vs CCV = under-investment in control verification

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

## 3. CCV vs HiPo Alignment Analysis

The gap between where CCV (critical control verification) activity is concentrated
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
- In AU: EAP data handling should align with the Privacy Act 1988 (Cth) health
  information provisions. Note the Australian Privacy Principles bind APP entities
  (generally organisations with turnover >$3m, plus health-service providers
  regardless of size), so small PCBUs may fall outside the Act (removal of the
  small-business exemption remains an unlegislated tranche-2 proposal as at
  mid-2026) — treat alignment as the floor for good practice either way.
- In NZ: NZ EAP data handling should align with the Privacy Act 2020 and the
  Health Information Privacy Code 2020, which gives extra protection to health
  information held by health agencies

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
- CCV verification completion heatmap: Critical Risk × BU
- Alignment gap summary (where HiPos exceed CCV activity)
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
- `dim_injury_type` — LTI, RWI, MTI, FAI, etc. with recordable flag
  (recordable = fatality, LTI, RWI, MTI). HiPo is an event-level flag on
  `fact_incidents`, not an injury type (see §1)

**Calculated measures (DAX patterns)**
```
TRIFR = 
DIVIDE(
    CALCULATE(COUNTROWS(fact_incidents), 
        fact_incidents[recordable] = TRUE()),
    SUM(fact_hours_worked[hours]),
    BLANK()  // not 0 — a zero here reports missing hours data as a genuine TRIFR of 0.0
) * 1000000

Rolling12mTRIFR = 
// Anchor to the last closed period — the last date with posted hours — not
// LASTDATE(dim_date): a full-calendar date dimension would otherwise drag
// the 12-month window across open or future months.
VAR LastClosedPeriod =
    CALCULATE(
        LASTNONBLANK(dim_date[date], CALCULATE(SUM(fact_hours_worked[hours]))),
        REMOVEFILTERS(dim_date)
    )
RETURN
CALCULATE(
    [TRIFR],
    DATESINPERIOD(dim_date[date], LastClosedPeriod, -12, MONTH)
)
```

**Relationship assumptions (important):** the TRIFR measure draws incidents from
`fact_incidents` and hours from `fact_hours_worked`. For the rate to evaluate
over a consistent grain, both fact tables must share **active relationships to
the common dimensions** (`dim_date` and `dim_contract`) in a star schema. Without
that shared filter context, the numerator and denominator can be evaluated over
mismatched grains and the measure will return a plausible-looking but wrong rate.
The `[recordable]` flag must be populated per the canonical TRI definition in
§1 (Fatality + LTI + RWI + MTI) so the measure matches the documented metric.

### Visualisation Recommendations

| Analysis | Chart type | Notes |
|---|---|---|
| Frequency rate trend | Line chart (rolling 12m) | Include target line |
| HiPo by critical risk | Stacked bar or treemap | Normalise by hours |
| CCV vs HiPo alignment | Radar / spider chart | Two series; gap = misalignment |
| Corrective action status | Donut + bar | Status breakdown + age analysis |
| BU performance comparison | Small multiples or matrix | Consistent scale across BUs |
| EAP utilisation trend | Line with area fill | Monthly trend; separate AU/NZ |

### Data Source Connections
> The organisation's actual incident/WHS systems are defined in
> `references/company.md`. The vendor products named below are illustrative
> examples of the system categories only — not recommendations. Confirm the
> real systems in company.md before building connections.

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

---

## 9. Statistical Treatment of Rates — Confidence Intervals, Funnel Plots and SPC

A frequency rate (§1) is an estimate built on a small count, and small counts
bounce. Test every rate for signal before it reaches a dashboard or a board.
**Do not hand-calculate any of this** — run `scripts/rate_confidence.py` on
the counts and hours `scripts/frequency_rates.py` used. If code cannot run,
say so, show the working (Byar's formula or the multiples table below) and
flag the figures for verification (SKILL.md §11).

### Injury Counts as Poisson Events

Recordable injuries are rare, near-independent events, so a period's count is
Poisson: variance equals the mean (expected 9, SD 3) and the rate inherits it.

| Method | Use when | 95% limits on the count *x* (then ÷ hours × 1,000,000) |
|---|---|---|
| Exact (Garwood 1936) | Always valid; required when *x* < 10, where rate ± 1.96 × standard error is unreliable and goes negative below 4 | Lower = ½ χ²(0.025; 2*x*); upper = ½ χ²(0.975; 2*x* + 2). Conservative — coverage is at least 95% |
| Byar's approximation | *x* ≥ 10 and no chi-square function available | Lower = *x* × (1 − 1/(9*x*) − 1.96/(3√*x*))³; upper = the same form on (*x* + 1) with + 1.96 |
| Zero events | *x* = 0 | Lower = 0; upper = 3.69 ÷ hours × 1,000,000 — no LTIs in 500,000 hours still fits a true LTIFR up to 7.4. A zero falls below a funnel's 95% lower limit only once the expected count exceeds 3.69 (99.8%: 6.91) — about 615,000 and 1,150,000 hours at a TRIFR of 6.0 |

| Recordables in period | 95% CI as a multiple of the observed rate | Reading |
|---|---|---|
| 1 | 0.03× to 5.57× | Effectively no information on the rate |
| 10 | 0.48× to 1.84× | True rate may be half the figure reported |
| 50 | 0.74× to 1.32× | Usable for comparison between units or years |
| 100 | 0.81× to 1.22× | Still ±20% — decimal places are decoration |

### The Small-Numbers Problem

- **Monthly TRIFR is mostly noise.** The 200-person team in §1 (32,000 hours
  a month) with a true TRIFR of 6.0 expects 0.19 recordables a month: 83% of
  months read 0.0, the rest read 31 or more, and nothing between can occur.
- **Year-on-year change is rarely detectable.** Showing a genuine halving
  (two-sided 5% test, 80% power, similar hours both years) takes about 50
  recordables in the baseline year, 8.3 million hours at a TRIFR of 6.0; a
  contract expecting 7 a year detects its own halving about 11% of the time.
- **The evidence agrees.** Hallowell et al. (Construction Safety Research
  Alliance, 2020): recordable-rate changes were 96–98% random variation.
- **Check comparability first.** Use the same recordable classification (who
  decides MTI versus FAI), hours method (§1) and inclusion rule in both
  periods or units; a reclassification alone creates or hides a "signal". An
  external benchmark carries its own uncertainty, basis and definitions
  (`strategy-function.md` §1): confirm them before it becomes a target.

### Comparing Units — Funnel Plots

Plot each unit's rate against its hours around the group rate, with limits
that narrow as hours grow (Spiegelhalter 2005): 95% (look) and 99.8% (act).
The script sets exact Poisson limits; the normal formula (group rate ± 1.96
or 3.09 × √(group rate ÷ unit hours in millions)) only sketches them at
expected counts of 5 or more, and runs narrow: B's 99.8% upper limit below
is 9.7 by formula, 10.1 exact. Meridian's Facilities Management business
unit, rolling 12 months: 126 recordables in 21,000,000 hours, TRIFR 6.0
(95% CI 5.0–7.1). Three of its contracts:

| Contract | Hours | TRI | TRIFR | Exact 95% CI | Expected at 6.0 | Chance of a count this extreme | Funnel position |
|---|---|---|---|---|---|---|---|
| A | 210,000 | 3 | 14.3 | 2.9–41.7 | 1.26 | 13% (3 or more) | Inside 95% — noise |
| B | 4,200,000 | 44 | 10.5 | 7.6–14.1 | 25.2 | 0.04% (44 or more) | Outside 99.8% — signal |
| C | 300,000 | 0 | 0.0 | 0–12.3 | 1.8 | 17% (zero) | Inside 95% — noise |

- A league table ranks A worst and C best; the funnel shows only B is beyond
  chance. A's rate is noise, and C's zero is no evidence of a better system.
- Across 20 units, expect about one outside the 95% limits by chance; only
  the 99.8% limit justifies a response on statistics alone — a review of how
  the work is done and resourced, not a ranking of managers. A unit below
  the lower limit gets the same review (good design or under-reporting):
  check its hazard and near-miss (§5) and FAI (§1) rates before crediting it.
- **Overdispersion**: far more units outside the limits than chance predicts
  suggests structural difference (work mix, multi-casualty events, who
  decides MTI versus FAI). The script's dispersion ratio is a raw screen.
  Estimate φ across every unit, never a handful, from z-scores winsorised at
  10% each end so the outliers under test do not inflate it. Only if units ×
  φ exceeds the 95th percentile of chi-square on (units − 1) degrees of
  freedom, widen limits by √φ, stratify or check exposure (§10). Never widen
  for the three contracts above: the script reports φ = 1.16 against the
  pooled rate (chi-square 3.49 on 2 df, p 0.17) — three units cannot show
  overdispersion, and B's excess is B's own signal, not a wider spread.

**Comparing two periods.** A Meridian contract cluster: 14 in 1,250,000 hours
(TRIFR 11.2, CI 6.1–18.8), then 9 in 1,200,000 (TRIFR 7.5, CI 3.4–14.2),
reported as "down 33%". Rate ratio 0.67, exact (conditional binomial) 95% CI
0.26–1.66, p ≈ 0.46: anything from a 74% fall to a 66% rise. Report "no
detectable change".

### Trend Over Time — Statistical Process Control

| Chart | Plot | Limits | Use when |
|---|---|---|---|
| u-chart | Rate per period | ū ± 3√(ū ÷ period hours in millions); lower limit floored at zero | Poisson counts, varying hours; expected count per point at least 5 (above 9 for a positive lower limit). Aggregate periods until each point gets there; if a quarter still expects fewer than 5, use a time-between-events chart |
| XmR (individuals) | Rate, count or percentage per period | Mean ± 2.66 × average moving range | Overdispersed rates (or use a Laney u′ chart), and leading indicators (§5) |
| Time between events (t- or g-chart) | Days or hours worked between successive events | Set by the charting tool | Rare events — LTIs, HiPos, SIFs — where most periods read zero |

Signal rules (Western Electric, as listed by NIST): (1) one point beyond
3 sigma; (2) two of three consecutive points beyond 2 sigma on the same side;
(3) four of five consecutive points beyond 1 sigma on the same side; (4) eight
consecutive points on one side of the centre line. On a u-chart with varying
hours, apply rules 2–4 to standardised values. Anything else is common-cause
variation: redesign the system if the level is unacceptable, but do not
demand an explanation for the point. False alarms: one per 371 points for
rule 1 alone, about one per 92 for all four (NIST); a trend rule (six in a
row rising or falling) adds more. Hold baseline limits; recalculating each
month absorbs signals. Recalculate only when a signal is sustained and traced
to a real change in the work system (NHS England, *Making Data Count*).

### What to Tell the Board

| The data show | Say | Do not say |
|---|---|---|
| Movement inside the limits | "TRIFR is 7.5 (95% CI 3.4–14.2); no detectable change on last year" | "TRIFR improved 33%" |
| A rule 1–4 signal, or a unit outside the 99.8% funnel limit | "Contract B's rate is higher than chance explains; this is what the work review found" | "Contract B is our worst performer" |
| Zero events in a small unit | "Too few hours to estimate a rate" | "Zero harm achieved" |
| Stable TRIFR with pSIF events occurring | "Injury frequency is stable; it does not measure fatal-risk control" (§1, §3) | "Safety performance is steady" |

Officer due diligence covers processes to receive, consider and respond to
incident, hazard and risk information (model WHS Act s 27(5)(d); HSWA 2015
(NZ) s 44(4)(d) as at October 2026, amendments pending; Victoria: OHS Act
2004 s 144 attribution only — `legislation.md` §1, §3, §16). Reporting rules:

- **No league tables of unit injury rates** (`strategy-function.md` §1), and
  no bonuses, prequalification scores or tender rankings built on them: the
  order is mostly hours and luck, and it rewards under-reporting.
- **No RAG on a single period's rate against target** — it flips on noise.
  This qualifies §4's colour semantics: a lagging rate goes red only for a
  signal (rule 1–4 breach, or outside the 99.8% funnel limit). Report
  variation and capability separately: a process whose limits straddle the
  target hits and misses it at random.
- **No two-point comparisons**, no percentage change on counts under about
  50, and narrative TRIFR to one decimal with its interval; the scripts' 2 dp
  output stays in tables and working (SKILL.md §11).

---

## 10. Exposure-Based Normalisation

A rate is a count divided by exposure, and the denominator decides what
question it answers. §1 sets hours worked × 1,000,000 as the default; this
section covers when another denominator is better and how to keep the hours
honest. Test every rate with §9; models inherit bad exposure data (§11).

### Choosing the Denominator

| Denominator | Reads as | Published convention | Use when | Trap |
|---|---|---|---|---|
| Hours worked × 1,000,000 | Events per million hours | AU/NZ corporate convention (§1); frequency rate in AS 1885.1-1990 (no longer current: superseded 22 May 2025 by AS/NZS ISO 45004:2024, which gives guidelines on performance evaluation, not a recording standard, so the 1885.1 rate definitions survive as convention); Safe Work Australia serious-claim frequency rate; GRI 403-9 option | Default for every injury and event rate — absorbs part-time work, overtime and long rosters | Same denominator, different numerator: Safe Work Australia counts serious claims (accepted workers' compensation claims with at least one working week lost), not LTIs (one full shift), so an LTIFR reads worse than the industry figure for the same performance (`strategy-function.md` §1) |
| Hours worked × 200,000 | Cases per 100 full-time workers a year (100 workers × 40 hours × 50 weeks) | US OSHA/BLS incidence rate (TRIR); GRI 403-9 option | US parent or investor reporting | One-fifth of the per-million figure (TRIR 1.2 = TRIFR 6.0), but only where the recordable set matches: OSHA recordability (29 CFR 1904.7) is not the §1 TRI set, so confirm the numerator before converting (`strategy-function.md` §1). Label the basis on every figure; `scripts/frequency_rates.py --basis 200000` |
| Employees × 1,000 | Claims per 1,000 employees | Safe Work Australia serious-claim incidence rate (ABS employee estimates) | No usable hours. Safe Work Australia publishes serious-claim rates on both bases; where you hold hours, benchmark on its frequency rate | A 15-hour casual counts the same as a 50-hour full-timer, so part-time-heavy workforces look safer than they are. To convert: ÷ annual hours per worker × 1,000 (10 per 1,000 workers at 1,700 hours each = 5.9 per million hours) — state the assumption |
| FTE × 1,000 | Claims per 1,000 FTEs | Stats NZ work-related injury claims — 78 per 1,000 FTEs for 2025 (provisional; as at October 2026) | NZ benchmarking; payroll holds FTE but not hours | Counts every work-related claim ACC accepts, so it is not comparable with serious claims, LTIs or recordables; FTE hides overtime |
| Workers × 100,000 | Cases per 100,000 workers a year | Safe Work Australia worker fatality rate; UK HSE and Eurostat injury rates | National and industry benchmarks | Meaningless at organisation scale — report fatalities as counts, with SIF and pSIF (§1) |

### Whose Hours, and How Good Are They

Numerator and denominator must describe the same people. The primary duty
runs to workers the PCBU engages or causes to be engaged, and to workers
whose activities in carrying out work it influences or directs, while they
are at work in the business or undertaking (model WHS Act ss 7, 19(1); HSWA
2015 (NZ) ss 19, 36(1); Victoria differs in form: `legislation.md` §4, §16).
Contractors, subcontractors and labour hire belong in the rate, so report
three lines: employees; contractors and labour hire under operational control
(define the boundary — Meridian's Operational Control Rule in `company.md`
is one); combined. GRI 403-9 requires the split (`specialist-topics.md` §4).

| Fault | Effect on the rate | Fix |
|---|---|---|
| Contractor injuries counted, hours missing (or the reverse) | Overstated (or understated) | Monthly hours as a scorecard line and a condition of invoice approval (`whs-procurement.md` §5). Lump-sum contractors: estimate from gate or induction swipe data, mark as estimated, keep the method fixed. No hours: report counts only |
| Shared duties — labour hire (claim with the labour-hire employer, exposure on the host's roster), principal contractor projects, joint ventures — where each PCBU counts the same hours and events, or assumes another does | Events and hours double counted or dropped; host, group and contractor rates never reconcile | Agree in the contract whose statistics carry which hours and events, as part of consulting, co-operating and co-ordinating with the other duty holders (model WHS Act s 46; HSWA 2015 (NZ) s 34), and reconcile each quarter. Labour hire: the host collects both — hours from the timesheets it already approves for invoicing, injuries through its own incident system |
| Paid hours used as worked hours (leave, public holidays, RDOs included) | Understated — a 38-hour full-timer is paid 1,976 hours a year and works roughly 1,700, about 14% fewer | Pull worked-time pay codes only (§1) |
| Non-standard time — working from home, paid travel and FIFO transit, on-call and standby, camp time, training days — treated differently by site or year | Hours drift between sites and years with no change in risk | Decide each once in the data dictionary (a workable default: time working, training or in paid work travel counts; leave, camp rest time and standby not called out do not), hold it, and restate history when it changes |
| Hours estimated as headcount × standard hours (salaried staff, overtime, FIFO and 12-hour rosters) | Drifts with each year's guess; overstated wherever real hours run long | Rostered or swiped hours for long-roster cohorts; elsewhere one documented estimate (scheduled hours × attendance factor). GRI's 200,000 basis assumes 2,000 hours per full-time worker — too high once AU/NZ leave comes out |
| Events logged daily, hours loaded at month end or late | Current period overstated, then quietly revised | Report to the last closed period (§1); lock at a cut-off and restate openly |
| No monthly test of the hours | Faults above go unseen | Hours ÷ headcount each month: a 38-hour roster lands near 140 (1,700 ÷ 12). A site far from what its roster predicts, or hours per head more than 10% away from the same month last year, with no matching headcount change, is a data fault until shown otherwise — shutdowns, school holidays and Easter move month-on-month figures legitimately |

### Activity-Based Denominators for Critical Risks

| Critical risk | Denominator | Count comes from | Numerator that fits |
|---|---|---|---|
| Vehicles and driving | Per million km | Telematics, odometer or fuel-card data (`workplace-controls.md` §3; heavy vehicles `sector-regimes.md` §14) | Crashes, rollovers, pSIF vehicle events |
| Lifting operations | Per 10,000 lifts | Lift register, crane data logger (`hazards.md` §19) | Dropped or uncontrolled loads, exclusion-zone breaches |
| Confined space | Per 100 entries | Permit register (`hazards.md` §11) | Atmosphere alarms, entries without standby or rescue plan |
| Isolation | Per 1,000 isolations | Isolation or permit register (`hazards.md` §10) | Failed verification ("try") steps, energy found live |
| Mobile plant and pedestrians | Per 1,000 plant operating hours | Engine-hour meters, proximity-detection logs (`hazards.md` §12) | Exclusion-zone incursions, contacts |
| Aviation (charter, helicopter, drone) | Per 1,000 flight hours, or per sector where take-off and landing carry the risk | Operator flight logs (`sector-regimes.md` §4) | Reportable occurrences |
| Latent disease (silicosis, noise-induced hearing loss, occupational cancers) | Per 1,000 exposed-worker years, by similar exposure group and exposure duration | Exposure monitoring and health monitoring records (`specialist-topics.md` §1; `hazards.md` §2) | Health monitoring findings, exposure results above the limit — the diagnosis arrives years after the exposure, so hours in the reporting period say little about the risk |

Hours measure time at work, not exposure to the hazard. Count the activity
instead when its volume moves independently of hours, when units do
different amounts of it, or when the control works per task (each entry,
lift or isolation is one chance to fail) — provided a system of record
counts it. Meridian's Facilities Management business unit logs 36 vehicle
incidents in each of two years on 21 million hours (1.7 per million both
years) while its fleet travel rises from 18 to 30 million km: 2.0 to 1.2 per
million km, a fall hours cannot see and only just beyond chance (exact
conditional test, p ≈ 0.04; §9). Report the count (still 36), the volume (km
per hour worked up 67%) and the rate together. The first control for driving
risk is less driving, and cutting low-risk trips can raise a per-km rate
while total risk falls, so never target the activity rate alone. Below an
expected count of 5 (§9), report counts and volume, not a rate; pair the rate
with control verification (§3, §7) and precursors (pSIF events, failed CCVs).

### Normalising Leading Indicators

| Indicator (§5) | Weak basis | Better basis |
|---|---|---|
| Hazard and near-miss reports | The §5 headcount basis, where part-time and casual workers are a material share of the workforce | Per 10,000 hours worked — a part-timer has proportionally less time on site to see and report. State the basis on the chart and restate history when you switch |
| Critical control verifications | Completed ÷ planned — the plan can be set low | Add coverage: CCVs per 100 entries, lifts or isolations, split by shift (nights, weekends) |
| Training and verification of competency | % of headcount | % of workers exposed to the risk — a role-based denominator |
| Action closure, audit conformance | A bare percentage | The percentage with its *n* — 100% of 2 is not 100% of 200 — and critical-risk actions reported separately |

### Comparing Sites with Different Risk Profiles

| Method | How | Limits |
|---|---|---|
| Stratify | Compare within work type or critical-risk exposure only | Often all that is needed; small strata still need §9 |
| Direct standardisation | Apply each unit's stratum rates to one reference mix of hours — "the rate this unit would have doing the group's mix of work". Eurostat compares national accident rates this way, weighting by each sector's share of the EU workforce | Needs a stable rate in every stratum of every unit, so it fails on small units |
| Indirect standardisation | Expected events = Σ (group stratum rate × unit's stratum hours); report observed ÷ expected (O/E), where 1.0 is "as expected for its work mix". Works with small strata, and observed and expected feed the funnel plot (§9) | Each ratio compares a unit with the group at the unit's own mix, not with other units, so do not rank units by O/E. For a unit that supplies a large share of group hours, calculate expected from group rates with that unit removed |

A cleaning contract and a plant-maintenance contract do not share an expected
rate; crude TRIFR ranks the work, not how it is managed. Standardisation
shows whether a unit performs differently given its work; it does not make
the high-risk stratum acceptable. The duty is to eliminate the risk or,
where that is not reasonably practicable, to minimise it SFAIRP (model WHS
Act s 17; HSWA 2015 (NZ) s 30; OHS Act 2004 (Vic) s 20 says "reduce"), and
an O/E of 1.0 shows nothing about whether that duty is met.

### Severity Weighting

| Fix in the data dictionary | Why |
|---|---|
| Fatality = 220 days lost (AS 1885.1-1990 cl 6.17) | Without a fixed charge a fatality adds no days to LTISR (§1). Counted as an occurrence with no days, it also pulls down the Standard's average time lost rate (days lost per lost-time occurrence) |
| Restricted-duty days in or out | The Standard was unclear; Queensland's mines inspectorate counted them, the common practice elsewhere was days away only. Pick one and hold it |
| Open cases, and mean versus median | Days keep accruing, so recent periods always read low: restate each period, and report median days lost beside the mean, because one long claim moves the mean |
| No composite indices (fatality = 100, LTI = 10) | The weights are invented and bury the fatal-risk signal; days lost also track claims and return-to-work management (`compensation-rtw.md` §8). Report SIF and pSIF counts separately (§1) |

### Pitfalls

| Pitfall | What happens | Control |
|---|---|---|
| Denominator drift | The hours definition changes (new payroll system, contractor hours added mid-year), or a unit joins or leaves part-way through the year (new contract, acquisition, divestment), and the rate steps with no change in risk | Annotate the chart; restate history on the new basis (with the acquired unit's history where it exists, without the divested unit's), or run both bases for 12 months. A part-year unit reports counts, not a rate, until it has 12 months of hours |
| Mixing populations | Low-risk hours dilute the rate: adding 2 million head-office hours with no recordables to 8 million operational hours carrying 48 recordables cuts TRIFR from 6.0 to 4.8 | One population per rate; report operational and office strata separately |
| Simpson's paradox | Every stratum moves one way and the total the other, because the mix of hours shifted — between years, sites, contractors, or either side of a merger | Show stratum rates and a standardised total, as below |

| Meridian Facilities Management business unit, rolling 12 months | Prior hours | TRI | TRIFR | Current hours | TRI | TRIFR |
|---|---|---|---|---|---|---|
| Maintenance contracts | 3,000,000 | 36 | 12.0 | 6,000,000 | 66 | 11.0 |
| All other contracts | 18,000,000 | 76 | 4.2 | 15,000,000 | 60 | 4.0 |
| Business unit, crude | 21,000,000 | 112 | 5.3 | 21,000,000 | 126 | 6.0 |
| Business unit, standardised to the prior-year mix | | | 5.3 | | | 5.0 |

Both strata improved, yet the business-unit rate rose from 5.3 to 6.0
because the higher-rate maintenance stream doubled its hours. Tell the board
the crude rate (6.0); that performance within each work type did not
deteriorate (standardised 5.0; neither stratum's change is beyond noise —
§9); and that the business unit now carries twice the exposure to its
higher-risk work — a control and supervision capacity question, not a number
to adjust away.

---

## 11. Predictive Analytics — Ethics and Governance

A predictive safety model ranks where harm is more likely next. What it
ranks decides the ethics: predicting **conditions** (site, shift, task) sends
verification and resources to the work; predicting **people** relocates the
cause into the individual, against the system lens in `frameworks.md` §5.
Machine-learning failure modes sit in `ai-and-whs.md` §3, not here.

### Unit of Prediction

| Unit | Example output | Typical inputs | Risk | Position |
|---|---|---|---|---|
| Site / contract | Sites most likely to record a pSIF next quarter | CCV findings, overtime, turnover, action backlog, work mix | Low — aggregated | Default. A flag triggers verification and resourcing |
| Shift / task | High-risk permit days; heat + overtime + new-crew combinations | Roster, weather, task type, plant | Moderate — small crews are re-identifiable | Use. The flag acts on the work (extra verification, supervision, re-planning) whatever the crew size. Outputs reported beyond the people running the job are aggregated to 10 or more workers (the §6 minimum group size); below that, handle them as individual-level data — restricted access, never used for performance or discipline |
| Individual | "Worker risk score"; injury-propensity or fatigue ranking | Injury and claims history, age, tenure, telematics, wearables, observations | High — privacy, discrimination, psychosocial harm, blame | Do not rank people. Real-time protective alerts pass (`ai-and-whs.md` §5): to the worker and, where the worker may be impaired or cannot act alone (fatigue, proximity), to the control room or supervisor who must intervene now. The alert triggers an immediate check of the work and the worker's fitness for it. It never becomes a score, a ranking or a record used for performance or discipline, and it passes the checklist below (the aggregation gate aside). Statutory health monitoring (lead risk work — `hazards-specialist.md` §2; hazardous chemicals) is individual by design and is not the ranking barred here; its results are confidential (lead: model WHS Regulations r 418) and stay out of any risk model |

### Base Rates and False Positives

Injury to one worker in one year is rare, so even a good model mostly flags
people who were never going to be hurt. Worked example: a Meridian Facilities
Group contract of 2,000 workers, of whom 3% (60) will have a recordable injury
in the next 12 months. A model with 80% sensitivity and 90% specificity flags
242 workers — 48 correctly, 194 wrongly — and misses 12 of the 60. Four in
five flags are false: positive predictive value (PPV) is 20%, about five
flags for every true event. Each flag is a CCV, a conversation or a roster
change someone has to make.

| Base rate of the outcome | PPV at 80% sensitivity, 90% specificity | Illustrative unit |
|---|---|---|
| 1% | 7% | Individual — serious injury in a year |
| 3% | 20% | Individual — any recordable in a year |
| 10% | 47% | Crew or task, per month |
| 30% | 77% | Site, per quarter — at least one HiPo |

- Ask the vendor for PPV and the count of flags per true event at the
  operating threshold. "Accuracy" is worthless: at a 3% base rate a model
  that flags nobody is 97% accurate.
- Aggregation raises the base rate. That is the statistical reason site and
  shift-level prediction is usable and individual-level prediction is not.
- Small-count uncertainty applies to predicted rates as it does to observed
  ones (§9); normalise inputs for exposure first (§10).

### Label Bias — the Model Learns Who Reports

The training label is *reported* events, not harm.

- Sites that report freely (§5 hazard and near-miss rates) score as high
  risk; silent sites score as safe. Act on that and reporting falls.
- Labour-hire, short-tenure and visa-dependent workers are the least likely
  to report, so the model under-predicts for the groups most exposed.
- Feedback loop: flagged crews get more inspections, more findings are
  logged, and the next run "confirms" the score.
- Test: if a higher hazard-report rate pushes predicted risk up, the model is
  measuring reporting culture. Prefer labels with less discretion in them:
  energy-based pSIF classification (§1) and CCV failures per CCV performed
  (§10). Both still depend on someone reporting or verifying, so hold CCV
  effort constant across the units compared. Cross-check against claims
  data, including labour-hire agency claims the host's insurer never sees.

### Legal Frame (as at October 2026)

| Instrument | What it requires of a predictive or monitoring system | Trap |
|---|---|---|
| Privacy Act 1988 (Cth) — who is bound | The APPs bind APP entities: Commonwealth agencies, and private-sector organisations above the small business turnover threshold (s 6D; §6). State and territory agencies answer to their own privacy statutes | The employee records exemption is private-sector only; Commonwealth agencies get no such carve-out |
| Privacy Act 1988 (Cth) — APPs | Collection reasonably necessary (APP 3); consent for sensitive information — health information, and biometric information used for automated verification or identification, or biometric templates (APP 3.3; s 6(1)); collection notice (APP 5); use limited to the collection purpose (APP 6) | The employee records exemption (s 7B(3)) covers only a private-sector employer's act or practice directly related to both the employment relationship and an employee record it already holds about its own current or former employee; a use beyond managing that employment, such as vendor model training, may fall outside it. It does not reach contractors, labour-hire workers or applicants, nor the act of collection: in *Lee v Superior Wood Pty Ltd* [2019] FWCFB 2946 a dismissal for refusing a fingerprint scanner was unfair — consent given under threat of discipline is not consent. The exposure draft Privacy Amendment (Personal Data Protection) Bill 2026 (released 31 August 2026) leaves the exemption alone but proposes a "fair and reasonable" test and treats AI-derived inferences as collection — draft, not law |
| Privacy Act 1988 (Cth) — APP 1.7–1.9, automated decisions (commence 10 December 2026) | Privacy policy must state the kinds of personal information used, the kinds of decisions made solely by a computer program, and the kinds where the program does a thing substantially and directly related to the decision — wherever the decision could reasonably be expected to significantly affect an individual's rights or interests (OAIC APP Guidelines Ch 1, updated 30 September 2026) | A human sign-off does not take a score-driven roster or testing decision outside the rule. Binds APP entities only. Contractors, labour-hire workers and applicants are covered; whether s 7B(3) removes a decision about the employer's own employees made from records it already holds is not addressed in the OAIC guidance — disclose for the whole workforce. Transparency duty only: no right to an explanation or human review |
| Privacy Act 1988 (Cth) — Sch 2 statutory tort (in force 10 June 2025) | Individuals can sue for a serious, intentional or reckless intrusion upon seclusion or misuse of information | Not limited to APP entities — small PCBUs outside the APPs are exposed |
| NSW — Workplace Surveillance Act 2005 | Camera, computer and tracking surveillance of employees needs written notice at least 14 days before it starts (s 10); cameras visible and signposted (s 11); computer surveillance only under a notified policy (s 12); a visible notice on any tracked vehicle or thing (s 13); none while the employee is not at work, other than computer surveillance of employer-provided equipment (s 16); records used only for legitimate employment or business purposes (s 18) | Un-notified surveillance is covert surveillance — an offence without a Magistrate's authority. GPS telematics fed into a model is tracking surveillance; login and system-use data is computer surveillance |
| NSW — WHS Act 2011 s 21A, inserted by the Work Health and Safety Amendment (Digital Work Systems) Act 2026 (assent 18 February 2026; s 21A not commenced as at October 2026) | PCBU to ensure SFAIRP that allocation of work by a digital work system (algorithm, AI, automation or online platform) does not put workers at risk, considering excessive or unreasonable workloads, performance metrics and monitoring or surveillance, and unlawful discriminatory decision-making | A model that allocates or sequences work is in scope on commencement — see `ai-and-whs.md` §7. Only the guideline-making provisions are in force; the rest commence by proclamation. WHS entry permit holders gain a power to require reasonable assistance to access and inspect a digital work system relevant to a suspected contravention (s 118(1)(a1)), which cannot commence until one month after SafeWork NSW publishes the DWS Guidelines (not published as at October 2026) |
| ACT — Workplace Privacy Act 2011 | Covers all workers, contractors and labour hire included (ss 7–8); tracking devices include GPS, biometrics and RFID (s 11); 14 days' written notice stating how records may be used (s 13); good-faith consultation giving a genuine opportunity to influence (s 14); workers may access their own surveillance records on written request (s 23); no surveillance of a worker outside a workplace, narrow exceptions (s 42) | Using a surveillance record to take adverse action is an offence (s 22(1), 50 penalty units; ACT unit values in `assets/penalty_units.json`) unless the s 13 notice said it could be used that way (s 22(2)). Records from a tracker that cannot be switched off, captured while the worker is outside a workplace, must not be used or disclosed for any purpose (ss 42(2)(b), 43) |
| VIC — Surveillance Devices Act 1999 | Bans optical and listening devices in workplace toilets, washrooms, change rooms and lactation rooms (s 9B). No workplace notice regime, but s 8 bars knowingly installing, using or maintaining a tracking device to determine a person's location without that person's express or implied consent | Document consent for GPS telematics and location wearables. Broader workplace surveillance laws (notice, consultation, legitimate-purpose test, limits on biometric and AI monitoring, human review of significant automated decisions, worker access to surveillance data) are a Labor election commitment announced 20 July 2026, conditional on the 28 November 2026 state election; no Bill and no law as at October 2026 |
| Consultation — model WHS Act ss 47–49; OHS Act 2004 (Vic) ss 35–36; HSWA 2015 (NZ) ss 58–60 | Consult workers and HSRs when proposing changes that may affect health or safety and when deciding procedures for monitoring worker health or workplace conditions (model s 49(d), (e)(iii)–(iv)) — before procurement, not at rollout (`frameworks.md` §10). HSRs are entitled to the information the PCBU holds on hazards and on the health and safety of their work group; identifiable personal or medical information only with the worker's consent (model ss 70(1)(c), 71(2)) | A privacy notice is not consultation. Tell HSRs what they can see and audit, not only what is collected |
| Adverse action and discrimination — Fair Work Act 2009 (Cth) general protections (adverse action defined in s 342; dismissal for temporary absence through illness or injury, s 352); Disability Discrimination Act 1992 (Cth); Age Discrimination Act 2004 (Cth); model WHS Act s 104; OHS Act 2004 (Vic) s 76; Human Rights Act 1993 (NZ) ss 21–22 | No adverse treatment because of a protected attribute, a workplace right, an injury absence or raising a safety issue | Age, tenure, injury and claims history are proxies for protected attributes and for injury absence. Reporting history as a model input penalises workers for raising issues |
| NZ — Privacy Act 2020; Biometric Processing Privacy Code 2025 | No employee-records exemption — the IPPs apply to worker data in full: lawful, necessary purpose (IPP 1); notice (IPP 3; IPP 3A for indirect collection from 1 May 2026); collection fair and not unreasonably intrusive (IPP 4); accuracy before use (IPP 8); limits on use (IPP 10). The Code (in force 3 November 2025; processing already running by then had until 3 August 2026) allows collection only where processing is necessary and effective, no less privacy-intrusive alternative would do as well, safeguards are in place and the processing is proportionate, weighing cultural impacts on Māori (r 1). It bars biometric categorisation — inferring health, mood, emotion, mental state, fatigue or attention — unless an exception applies (r 10(5)) | Fatigue, alertness and attention may be inferred only where necessary to prevent or lessen a risk to public health or safety or to someone's life or health (r 10(8)); health information only with the individual's express authorisation (r 10(9)). Using the same feed for productivity fails the Code. Record the r 1 assessment: the Code does not demand it in writing, but reasonable grounds are hard to show without it |
| QLD, WA, SA, TAS, NT | No workplace surveillance statute. General surveillance devices law still binds employers; the Surveillance Devices Acts of WA (1998), SA (2016) and the NT (2007) regulate tracking devices | Read the local Act before location tracking goes live — the absence of a workplace statute is not permission |

### Psychosocial Effects of Monitoring

Monitoring is a hazard to be risk-assessed under the psychosocial regulations
(model WHS Regulations rr 55A–55D; Victoria: OHS (Psychological Health)
Regulations 2025; NZ: HSWA 2015 s 36 primary duty, health including mental
health under s 16 — `legislation.md` §9), not a neutral data feed. In the
Comcare jurisdiction, the Work Health and Safety (Managing Psychosocial
Hazards at Work) Code of Practice 2024 (Cth) lists **intrusive surveillance**
as a psychosocial hazard. It is not one of the 14 hazards in the SWA model
Code; elsewhere assess it through low job control and high job demands.
Ravid et al.'s 2023 meta-analysis of electronic performance monitoring (94
samples) found no evidence that it improves performance, and found it raises
stress whatever the monitoring design; transparent, less invasive monitoring
improved attitudes, not stress. Expect withheld reports and workarounds
(devices left in the ute). Controls: `frameworks.md` §14.

### Governance Checklist

| Gate | Minimum standard before go-live, and while live |
|---|---|
| Purpose limitation | One written purpose: directing controls, verification and resources. Performance management, discipline, claims and insurance uses excluded in the policy and the vendor contract |
| Consultation | Workers and HSRs consulted before procurement on what is collected, who sees it, what a flag triggers and what HSRs can inspect; surveillance notices served (NSW, ACT: 14 days); psychosocial risk assessment done |
| Privacy assessment | Privacy impact assessment before any data is collected. VIC: documented tracking consent (Surveillance Devices Act 1999 s 8). NZ biometrics: necessity, safeguards and proportionality recorded against Code r 1 |
| Data minimisation | Lowest unit that answers the question; no health, biometric or claims data without a documented necessity case; reported outputs aggregated to 10 or more workers (live protective alerts excepted) |
| Validation | Tested on a later period than the training data; PPV and flags per true event reported as counts; results split by site, employment type and age band; beats a naive baseline (last year's highest-exposure sites) or is not deployed |
| Drift monitoring | Quarterly check of flag rate and PPV against validation. Re-validate on any change to the reporting system, classification rules, work mix or workforce. Set the PPV floor at go-live no lower than the naive baseline's PPV; retire or rebuild the model when PPV sits below it for two consecutive quarters |
| Explainability | Every flag names its drivers in terms a supervisor can verify in the field. No unexplained scores |
| Human decision | A flag starts a CCV or a conversation about the work. A named person decides, can override, and overrides are logged and reviewed |
| Worker access | Workers can see the data held about them and what it was used for (ACT: s 23); HSRs can audit inputs and outputs for their work group, de-identified unless the worker consents (model WHS Act s 71(2)) |
| No disciplinary use without process | A score is never evidence of fault. Conduct concerns run through the separate fair process on their own evidence (just culture: `frameworks.md` §12; restorative response: `investigation-advanced.md` §8) |
| Ownership | Named executive owner; annual review with HSRs; APP entities: privacy policy updated for APP 1.7 before 10 December 2026 (every PCBU, inside the APPs or not, stays exposed to the Sch 2 tort) |

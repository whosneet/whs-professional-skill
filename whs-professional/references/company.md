# Company Reference

This file holds the **organisation-specific WHS context** the skill uses. Everything
in the other reference files is jurisdictionally or industrially generic — WHS Act,
HSWA, ICAM, ISO 45001, Safety II, named safety science, hazard-specific frameworks.
Anything that's a company's particular configuration — risk matrix values, severity
classifications, document numbering, incident management system, named programs,
critical risk taxonomy — lives here.

## How to use this file

The file has two parts:

1. **Template** — a generic structure describing what each section should capture,
   so any organisation can fill it in.
2. **Active Reference** — the filled-in worked example currently in use. Replace
   the Active Reference content with your own organisation's context to repurpose
   the skill. The Template above shows the structure to mirror.

If no Active Reference is provided, the skill will produce generic AU/NZ WHS
guidance without organisation-specific tailoring. The other reference files will
still work — they just won't be anchored to a particular company's framework.

---

## Template

For each section below, your organisation's context replaces the prompts. Sections
that don't apply can be left blank or removed.

### 1. Organisation Identity
- Legal entity name and trading name
- Division / business unit name (if operating within a larger group)
- Industry sectors
- Jurisdictions of operation (AU states/territories, NZ, others)
- Approximate workforce size (direct + contractor)
- Lines of business / contract types

### 2. WHS Management System
- System brand name (e.g. "Zero Harm", "Safety First", "Beyond Zero")
- ISO 45001 status — certified, aligned, in progress, not pursuing
- Reference standards adopted
- Document numbering convention — prefix structure, type codes, functional codes

### 3. Risk Framework
- Risk matrix (consequence × likelihood; rating output structure)
- Likelihood criteria — qualitative and quantitative bands
- Consequence ratings — across H&S, environment, legal, reputation, cost
- Control effectiveness rating scale
- Risk level response requirements (action thresholds, acceptance authorities,
  monitoring cadence)

### 4. Hierarchy of Controls — Local Framing
- Any organisation-specific framing layered onto the standard hierarchy
- "Above-the-line / below-the-line" or equivalent shorthand
- Rules about when low-level controls cannot be sole risk treatment

### 5. Incident Classification & Management
- Severity rating system (typically 1–5 or 1–6 scale)
- HiPo definition (potential severity threshold)
- Notifiable incident thresholds
- Internal notification chain by severity — who is notified, by when, by what method
- Investigation methodology mandated (ICAM, TapRoot, 5-Why, etc.)
- Investigation requirements by severity (who leads, who reviews, what is produced)
- Incident management system / database

### 6. Document Templates & Forms
- Safety alert format and template reference
- Toolbox talk template
- Investigation report template
- SWMS template
- Risk register template
- Preliminary incident notification form
- Lessons learnt template
- Other relevant templates

### 7. Systems & Tools
- Incident management system
- WHS management system platform
- Analytics / dashboarding platform
- Project / task management
- Contractor management / prequalification
- Audit & inspection platform
- Permit-to-work system (if applicable)

### 8. Critical Risk Taxonomy
- The organisation's critical risk categories
- Critical Risk Owner (CRO) structure or equivalent
- Critical Control Verification (CCV) framework and cadence

### 9. Engagement Programs & Campaigns
- Named recurring programs
- Cadence and reach
- Theme architecture
- Recognition / incentive mechanisms

### 10. Governance & Reporting Cadence
- Board safety reporting cycle and format
- ELT safety reporting cycle and format
- Officer due diligence framework
- Key WHS leadership roles and accountabilities
- Peer review or assurance processes

---

## Active Reference: Downer SICS

*This is the worked example currently in use. Replace with your own organisation's
context to repurpose this skill.*

### 1. Organisation Identity
- **Parent**: Downer EDI Limited (publicly listed on ASX)
- **Operating division**: Social Infrastructure & Citizen Services (SICS)
- **Business units within SICS**: Government IFM (Integrated Facilities Management),
  Health & Education, Base & Estate Management
- **Jurisdictions**: All AU states and territories, plus New Zealand
- **Workforce**: 13,000+ workers across the SICS portfolio
- **Lines of business**: Integrated facilities management, defence base services,
  hospital and education FM, government services

### 2. WHS Management System
- **System brand**: Zero Harm
- **Reference standard**: ISO 45001 aligned
- **Document numbering convention**: `[Prefix]-[Functional]-[Type][Number]`
  - **Prefix**: `DG` (Downer Group enterprise) or `SI` (SICS division-specific)
  - **Functional code**: `ZH` (Zero Harm), `RM` (Risk Management), `QA` (Quality
    Assurance), `HR`, etc.
  - **Type code**: `ST` (Standard), `PR` (Procedure), `WI` (Work Instruction),
    `TP` (Template), `FM` (Form), `GD` (Guideline)
  - **Example**: `DG-ZH-PR006` = Downer Group, Zero Harm, Procedure 006
- **Key parent standards**:
  - `DG-RM-ST001` — Risk and Opportunity Management Standard
  - `DG-ZH-ST028` — Zero Harm Risk Management Standard
  - `DG-ZH-PR006` — Incident Management Procedure
  - `DG-ZH-PR0150` — Just Culture Procedure

### 3. Risk Framework

**Risk and Opportunity Rating Matrix** (DG-RM-ST001 + DG-ZH-ST028):
Same A/B/C/D matrix applies across enterprise, business unit, and project levels.

| Consequence | Rare | Unlikely | Possible | Likely | Almost Certain |
|---|---|---|---|---|---|
| **6** | B | B | A | A | A |
| **5** | C | B | B | A | A |
| **4** | C | C | B | B | A |
| **3** | D | C | C | B | B |
| **2** | D | D | C | C | B |
| **1** | D | D | D | C | C |

**Likelihood Criteria** (DG-RM-ST001 Annex C / DG-ZH-ST028 Table 2):

| Rating | Probability | Qualitative criteria |
|---|---|---|
| Almost Certain | ≥80% | Expected in most circumstances; likely multiple times throughout a project |
| Likely | ≥50%, <80% | Probable in most circumstances; has occurred in similar projects |
| Possible | ≥20%, <50% | Might occur; has occurred in a minority of similar projects |
| Unlikely | ≥5%, <20% | Could occur; has not occurred in similar projects but could |
| Rare | <5% | Exceptionally unlikely even long-term; a 100-year event |

**Zero Harm Consequence Rating** (DG-ZH-ST028 Table 1 / DG-RM-ST001 Annex A):

| Level | H&S | Legal/Compliance | Environment/Community |
|---|---|---|---|
| 6 — Extreme | Multiple fatalities or significant irreversible effects >1 person | Breach → major litigation, risk of Group-level long-term impact, executive jailing | Catastrophic irreversible damage; complete loss of community trust |
| 5 — Very High | Single fatality or severe irreversible disability | Prosecution; litigation up to $10m; possible custodial sentence | Significant/serious environmental harm; prolonged community outrage |
| 4 — High | Moderate irreversible disability; LTI >28 days | Regulatory punitive fine; prosecution or litigation risk; loss of key licence | Material harm; notifiable incident; long-term community irritation |
| 3 — Medium | LTI ≤28 days; or MTI >28 days restricted | Regulator warning, no fine; notifiable incident to external body | Moderate harm; notifiable incident; short-term community unrest |
| 2 — Low | MTI ≤28 days restricted | Not a notifiable incident; formal warning notice | Minor environmental impact; community complaint requiring intervention |
| 1 — Very Low | First aid case or less | No breach; negligible consequence | Negligible impact; no community complaint |

For project-specific consequence ratings (gross margin and schedule criteria),
refer to DG-RM-ST001 Annex B.

**Risk Control Effectiveness** (DG-RM-ST001 s 8.2.4):

| Rating | Qualification |
|---|---|
| **Effective** | Controls effective and appropriate; reasonable assurance risks managed and objectives met |
| **Generally Sound** | Gaps exist, or controls don't manage risk in all instances; in combination, adequate for assurance |
| **Improvement Required** | Controls not implemented, appropriate, or effective; unlikely to provide reasonable assurance |

**Risk Level Response Requirements**:

| Risk Level | Response | Monitoring |
|---|---|---|
| **A** | Immediate action; controls to reduce to acceptable level before commencing; Nominated Delegates must authorise acceptance | At least monthly by senior leaders |
| **B** | Identify and implement controls; senior leaders authorise acceptance | At least 3-monthly by senior leaders |
| **C** | Manage by implementing identified controls; cost-benefit analysis for additional measures | At least 3-monthly by mid-level management |
| **D** | Manage by implementing identified controls | At least 6-monthly by management |

**Corrective Action Priority**:

| Priority | Definition |
|---|---|
| Essential | Highly essential measure to improve risk mitigation or outcome |
| Important | Will significantly improve risk mitigation or outcome |
| Recommended | Will moderately improve risk mitigation or outcome |

### 4. Hierarchy of Controls — Downer Framing (DG-ZH-ST028 Table 3)

Downer uses **"above the line"** (hard controls) and **"below the line"**
(soft controls) framing:

| Level | Type | Downer classification |
|---|---|---|
| Eliminate | Hard | Above the line |
| Substitute | Hard | Above the line |
| Isolate | Hard | Above the line |
| Engineering | Hard | Above the line |
| Administrative | Soft | Below the line |
| PPE | Soft | Below the line |

**Critical rule from DG-ZH-ST028**: Low-level controls (soft / below the line)
must NOT be the sole risk treatment where hard controls can be implemented. The
cost of controls must be **grossly disproportionate** before it can be considered
not reasonably practicable.

### 5. Incident Classification & Management

**Reference**: DG-ZH-PR006 Incident Management Procedure, Annexes D, E, F.

**Severity Ratings (1–6)** — use highest consequence across any dimension; for
near misses, use **potential** consequence, not actual outcome.

| Rating | Label | Health & Safety | Environment | Plant & Property | Legal/Compliance | Management Impact |
|---|---|---|---|---|---|---|
| **6** | Extreme | Multiple fatalities or significant irreversible effects to >1 person | Catastrophic irreversible damage; community loses all trust | $100m+ facility loss or total production loss | Prosecution + prolonged litigation; jailing of executives | Business unit closure; inability to execute core functions |
| **5** | Very High | Single fatality or severe irreversible disability | Significant/serious environmental harm; prolonged community outrage | $10m+ plant/facility damage; major long-term process impact | Prosecution; litigation up to $10m; possible custodial sentence | Critical disaster; considerable senior management time over months |
| **4** | High | Moderate irreversible disability; LTI >28 days | Material harm; environmental notifiable incident; long-term community irritation | Serious plant/facility damage $1m+; mid-term interruption | Regulatory punitive fine | BU senior management involvement over several weeks; org review required |
| **3** | Medium | LTI ≤28 days; or MTI >28 days restricted | Moderate harm; environmental notifiable incident; short-term community unrest | Significant plant damage $100k+; short-term interruption | Regulator warning, no fine; notifiable incident to external body | Managed with careful attention over several weeks |
| **2** | Low | MTI ≤28 days restricted | Minor environmental impact; community complaint requiring intervention | Minor damage $10k+; minor business interruption | Not a notifiable incident | Some local management attention over several days |
| **1** | Very Low | First aid case or less | Negligible environmental impact; no community complaint | Cosmetic damage, absorbed in maintenance budget | No breach of legislation | Absorbed in normal management activity |

**Critical Incident** = actual consequence level 4, 5, or 6. Triggers Crisis
Management Team notification.

**HiPo** = regardless of actual consequence, could have realistically resulted in
permanent disability (moderate impairment or greater) or death. Must have
potential severity rating of 4, 5, or 6.

**Injury Classifications**:

| Classification | Acronym | Key criteria |
|---|---|---|
| Fatality | F | Work-related death. Recordable |
| Lost Time Injury | LTI | Unfit to perform ANY duties for ≥1 whole day/shift after injury shift. Recordable |
| Medical Treatment Injury | MTI | Treatment by medical practitioner; or >3 physio/allied health sessions. Recordable. Includes restricted work days |
| First Aid Case | FAC | Treatment within scope of first aider training. Classified by treatment given, not qualifications of treater |
| Health Case | HC | Chronic condition from long-term exposure. NOT recordable as injury. Includes most psychosocial, noise-induced hearing loss, asbestosis, silicosis |
| Non-Work Injury | NWI | Not connected to significant traumatic work event. Commuting (not work-travel), home injuries, common cold/flu |
| Journey Injury | JI | Travel not directly related to work (commuting). Not counted in recordable statistics |
| Public Health Illness | PHI | Non-work illness linked to a Public Health Risk Event (e.g. COVID-19, H1N1) |

**Direct Downer Control vs Influence**: Incidents are only included in Downer's
aggregated performance statistics if under **Direct Downer Control** — ability
to direct work methodology, controls used, risk identification method, and use
of Downer's management system. **Downer Influence only** = material interest,
asset ownership operated by another entity, or brand use without directing work —
report internally for lessons sharing but NOT in Zero Harm statistics.

**Internal Notification Requirements (Annex E)**:

| Rating | Verbal | Written / INX |
|---|---|---|
| 1–2 | ASAP verbal or phone (no voicemail — escalate) | INX by start of next shift |
| 3 | ASAP verbal or phone | INX + FM006.1 PIIN by start of next shift |
| 4 | Immediate verbal or phone | INX + FM006.1 PIIN within 24 hrs |
| 5 | Immediate verbal or phone | INX + FM006.1 PIIN within 8 hrs |
| 6 | Immediate verbal or phone | INX + FM006.1 PIIN within 8 hrs |
| HiPo | Immediate verbal or phone | INX + FM006.1 PIIN within 24 hrs |

**Investigation Requirements (Annex F)**:

| Severity | Methodology |
|---|---|
| 1 | INX Walk Me / Learners Guide |
| 2–3 | DG-ZH-FM006 Standard Incident Investigation; 5-Why supported by DG-ZH-FM006.4 |
| 4–6 / HiPo | ICAM investigation using DG-ZH-TP006.1; BU GM Zero Harm review |
| Fatality / serious environmental harm | ICAM + legal advice (EGM Zero Harm and/or Downer H&S Legal Counsel) |

**Incident Management Process (DG-ZH-PR006)** — 13-step process; key gates:
1. Respond to incident, render assistance, preserve scene
2. Determine Direct Downer Control (document determination and rationale in INX)
3. Initial assessment and immediate controls
4. Internal notification per Annex E
5. Regulator notification if required (see `legislation.md` §5)
6. Classify per Annex D
7. Convene phone conference (sev 4–6, HiPo): Operations Manager + line manager +
   BU GM Zero Harm within 1 working day; COO/EGM invited optional
8. Allocate investigation per Annex F
9. Identify and assign corrective actions in INX
10. Effectiveness verification
11. Lessons Learnt — Alert (mandatory for notifiable) or Bulletin
12. Close incident in INX
13. Trend analysis / aggregated learning

**For disciplinary matters** related to incidents: refer to DG-ZH-PR0150 Just
Culture Procedure.

### 6. Document Templates & Forms

| Document | Reference |
|---|---|
| Safety Alert (Portrait) | DG-QA-TP014 |
| Safety Alert (Landscape) | DG-QA-TP031 |
| Bulletin (Portrait) | DG-QA-TP015 |
| Bulletin (Landscape) | DG-QA-TP032 |
| Preliminary Internal Incident Notification (PIIN) | DG-ZH-FM006.1 |
| Standard Incident Investigation | DG-ZH-FM006 |
| ICAM Investigation Report | DG-ZH-TP006.1 |
| ICAM Interview Record | DG-ZH-FM006.5 |
| 5-Why Analysis | DG-ZH-FM006.4 |
| Lessons Learnt | DG-ZH-TP138 (also DG-ZH-TP007 register) |
| Risk and Opportunity Register | DG-RM-FM003 |
| Zero Harm Risk and Opportunity Register | DG-ZH-FM028.1 |
| Plant Risk Assessment | DG-ZH-FM057.3 |
| Hazardous Chemicals & DG Risk Assessment | DG-ZH-FM024.1 |
| Manual Handling Assessment | DG-ZH-FM085.1 |
| Constructability Risk Assessment | DG-ZH-FM030.1 |
| Traffic Management Plans | DG-ZH-TP135.1-AU |
| STAR (Stop, Think, Act, Review) | DG-ZH-FM148 |
| SICS Governance Template Suite | SI-ZH-TP002 through SI-ZH-TP007 |

### 7. Systems & Tools

| Purpose | System |
|---|---|
| Incident management | INX InControl |
| WHS management system platform | Lucidity (formerly Ideagen) |
| Analytics & dashboarding | Power BI |
| Project & task management | Asana |
| Contractor management & prequalification | Rapid Global |
| Document storage / lessons sharing | SharePoint (Group Zero Harm site) |

### 8. Critical Risk Taxonomy

**Standard Critical Risk Topics (Downer Zero Harm)**:
Working at Height, Electrical Safety, Isolation of Stored Energy, Vehicles and
Mobile Plant, Working in Confined Spaces, Hazardous Substances, Manual Handling,
Hot Work, Working Near Water, Structural Collapse, Dropped Objects, Explosives
and Flammables, Working in Proximity to Live Services, Atmospheric Testing,
Worker Fatigue.

**Critical Risk Owner (CRO)** model — each critical risk has a designated owner
accountable for risk profile understanding, critical control adequacy, and
verification activity coverage.

**Critical Control Verification (CCV)** — structured verification of critical
controls in operation, separate from compliance audit. Cadence varies by risk;
tracking and reporting through Power BI.

### 9. Engagement Programs & Campaigns

**Safe Over Summer (SOS)** — flagship annual program.
- Duration: 8 weeks across the Australian summer period
- Cadence: weekly themed toolbox session
- Coverage: 15 critical risk topics across the program, plus buffer weeks
- Facilitators: 200+ across the SICS workforce
- Physical collateral: jigsaw puzzle poster, weekly stickers, weekly prize draws
- Outcome: SOS25 achieved a 21% reduction in TRI; AIHS Cat 4 award winner
- Format reference: see `programs.md` Section 2 for the sustained-campaign
  architecture this brand uses

### 10. Governance & Reporting Cadence

- **Board safety reporting**: scheduled board pack with Zero Harm content (April
  pack is the major annual board paper)
- **ELT reporting**: monthly cycle with HiPo intelligence, lagging indicators,
  critical control health
- **Officer due diligence**: GM Zero Harm and EGM Zero Harm coordinate officer
  briefings; CRO accountability runs in parallel
- **Cross Contract Improvement Program (CCIP)**: structured peer review process
  across SICS contracts; documented through PPTX and Canva decks

**Key Roles**:

| Role | Scope |
|---|---|
| EGM Zero Harm | Executive accountability across the Group |
| GM Zero Harm (SICS) | Divisional Zero Harm leadership |
| BU GM Zero Harm | Business-unit-level Zero Harm leadership |
| Zero Harm Performance & Programs Manager | Portfolio Zero Harm performance, programs, analytics |
| Operations Manager | First-line operational accountability — required attendee at sev 4–6 / HiPo phone conferences |
| Critical Risk Owner (CRO) | Named owner per critical risk topic |
| Zero Harm Business Partner | Embedded support to business units / contracts |
| H&S Legal Counsel | Internal legal advisory for serious incidents |

---

*To adapt this skill for another organisation, replace the Active Reference
content above with your own — mirroring the Template structure. The other
reference files (`legislation.md`, `frameworks.md`, `investigation.md`,
`hazards.md`, `analytics.md`, `programs.md`, `output-templates.md`) are
organisation-agnostic and will read your context through this file.*

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

**The easy way to fill this in**: tell the skill *"I want to adapt this skill
to my company"*. It runs the guided ten-step interview in
`adaptation-interview.md` — one section at a time, extracting from your source
documents where you can paste them, and assembling the finished Active
Reference for you. Each Template section below maps 1:1 to an interview step.

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
- System brand name (e.g. "Safe for Life", "Safety First", "Beyond Zero")
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

## Active Reference: Meridian Facilities Group (MFG)

**This worked example is entirely fictional. Meridian Facilities Group does not
exist; any resemblance to a real organisation's documents is coincidental.**

*This is the worked example currently in use. Replace with your own organisation's
context to repurpose this skill.*

### 1. Organisation Identity
- **Parent**: Meridian Facilities Group Limited (MFG) — a fictional ASX-listed
  integrated facilities services group
- **Business units**: Facilities Management, Asset & Infrastructure Services,
  Hospitality & Catering, Health & Education Services
- **Jurisdictions**: all AU states and territories, plus New Zealand
- **Workforce**: ~12,000 workers (direct employees plus a managed contractor
  workforce)
- **Lines of business**: integrated facilities management, asset maintenance and
  minor capital works, commercial catering and hospitality services, and support
  services to hospitals, aged care, schools, and universities

### 2. WHS Management System
- **System brand**: Safe for Life
- **Reference standard**: ISO 45001 certified (group certificate; annual
  surveillance audits)
- **Document numbering convention**: `MFG-[Functional]-[Type]-[Number]`
  - **Prefix**: `MFG` (group-wide); BU-issued documents carry the same prefix
    with the BU named in the document header
  - **Functional code**: `WHS` (Work Health & Safety), `RM` (Risk Management),
    `QA` (Quality Assurance), `HR`, etc.
  - **Type code**: `ST` (Standard), `PR` (Procedure), `WI` (Work Instruction),
    `TP` (Template), `FM` (Form), `GD` (Guideline)
  - **Example**: `MFG-WHS-PR-002` = Meridian Facilities Group, WHS, Procedure 002
- **Key parent standards**:
  - `MFG-RM-ST-001` — Enterprise Risk Management Standard
  - `MFG-WHS-ST-001` — WHS Risk Management Standard
  - `MFG-WHS-PR-002` — Incident Management Procedure
  - `MFG-WHS-PR-014` — Fair and Just Culture Procedure

### 3. Risk Framework

**MFG Risk Rating Matrix** (MFG-RM-ST-001 + MFG-WHS-ST-001):
A single 5×5 matrix applies at enterprise, business unit, and contract levels.
Rating output: Low / Moderate / High / Critical.

| Consequence | Rare | Unlikely | Possible | Likely | Almost Certain |
|---|---|---|---|---|---|
| **5 — Severe** | High | High | Critical | Critical | Critical |
| **4 — Major** | Moderate | High | High | Critical | Critical |
| **3 — Moderate** | Low | Moderate | High | High | Critical |
| **2 — Minor** | Low | Low | Moderate | Moderate | High |
| **1 — Insignificant** | Low | Low | Low | Moderate | Moderate |

**Likelihood Criteria** (MFG-WHS-ST-001 Schedule 1) — frequency-anchored:

| Rating | Frequency anchor | Qualitative criteria |
|---|---|---|
| Almost Certain | Several times a year | Expected to occur in most circumstances across the group |
| Likely | About once a year (once in 1–2 years) | Will probably occur; has occurred at MFG in recent years |
| Possible | Once in 2–5 years | Could occur; has occurred somewhere in the industry |
| Unlikely | Once in 5–20 years | Not expected to occur, but conceivable |
| Rare | Less than once in 20 years | Would occur only in exceptional circumstances |

**Consequence Ratings** (MFG-WHS-ST-001 Schedule 1):

| Level | Health & Safety | Legal / Compliance | Environment / Community |
|---|---|---|---|
| 5 — Severe | Fatality or permanent total incapacity (one or more people) | Prosecution with potential officer liability; loss of a major licence to operate | Long-term environmental damage; sustained loss of community confidence |
| 4 — Major | Permanent partial incapacity, or LTI with extended recovery (>4 weeks) | Enforceable undertaking or significant fine; regulator notices | Serious environmental harm requiring external remediation; sustained complaints |
| 3 — Moderate | LTI up to 4 weeks; or restricted work >2 weeks | Notifiable to a regulator; improvement notice possible | Moderate harm contained on site; short-term community concern |
| 2 — Minor | Medical treatment injury with no lost time | Minor compliance breach, corrected and recorded internally | Minor impact remediated immediately; isolated complaint |
| 1 — Insignificant | First aid only | No breach; record-keeping only | Negligible impact; no complaint |

**Risk Control Effectiveness** (MFG-RM-ST-001):

| Rating | Qualification |
|---|---|
| **Adequate** | Controls in place, operating as designed, and recently verified |
| **Partially Adequate** | Controls in place but with gaps in design, application, or verification |
| **Inadequate** | Controls missing, not operating, or unverifiable |

**Risk Level Response Requirements**:

| Risk Level | Response | Monitoring |
|---|---|---|
| **Critical** | Do not start (or stop) work until interim controls reduce exposure; Group Executive must authorise acceptance | Monthly review by the accountable executive |
| **High** | Treatment plan within 14 days; BU General Manager authorises acceptance | Quarterly review by BU leadership |
| **Moderate** | Manage through planned controls; treat further where reasonably practicable | Six-monthly review by contract/site management |
| **Low** | Manage through routine controls | Annual review |

**Corrective Action Priority** (MFG-WHS-PR-002):

| Priority | Definition |
|---|---|
| P1 — Immediate | Required before work resumes, or within 24 hours |
| P2 — Urgent | Within 7 days |
| P3 — Planned | Within 30 days or by an agreed milestone |

### 4. Hierarchy of Controls — MFG Framing (MFG-WHS-ST-001)

MFG distinguishes **"hard controls"** (eliminate, substitute, isolate,
engineering) from **"soft controls"** (administrative, PPE):

| Level | Type | MFG classification |
|---|---|---|
| Eliminate | Hard | Preferred — design the hazard out |
| Substitute | Hard | Preferred |
| Isolate | Hard | Preferred |
| Engineering | Hard | Preferred |
| Administrative | Soft | Supporting only |
| PPE | Soft | Supporting only |

**Critical rule (MFG-WHS-ST-001)**: for any activity mapped to a critical risk,
at least one verified hard control must be in place before work starts. Soft
controls must NOT be the sole risk treatment where a hard control is reasonably
practicable; cost alone does not make a control not reasonably practicable
unless it is grossly disproportionate to the risk.

### 5. Incident Classification & Management

**Reference**: MFG-WHS-PR-002 Incident Management Procedure, Schedules 1–3.

**Severity Classes (1–5)** — rate on the highest consequence across any
dimension; for near misses, rate on credible **potential** consequence, not the
actual outcome.

| Class | Label | Health & Safety | Environment | Plant & Property | Legal/Compliance | Management Impact |
|---|---|---|---|---|---|---|
| **5** | Catastrophic | Fatality or permanent total incapacity (one or more people) | Long-term environmental damage extending off site | $20m+ loss or loss of an entire facility | Prosecution with potential officer liability | Group crisis footing; sustained executive involvement |
| **4** | Major | Permanent partial incapacity; LTI with extended recovery | Serious harm requiring external remediation | $2m+ damage; extended service interruption | Enforceable undertaking or significant fine | BU leadership engaged over weeks; client escalation |
| **3** | Moderate | LTI (up to 4 weeks); or restricted work >2 weeks | Moderate harm contained on site | $200k+ damage; short service interruption | Notifiable to a regulator; improvement notice possible | Contract leadership attention over days to weeks |
| **2** | Minor | Medical treatment injury, no lost time | Minor impact remediated immediately | $20k+ damage; minor disruption | Minor breach corrected internally | Local management attention |
| **1** | Negligible | First aid only | Negligible impact | Cosmetic damage absorbed in maintenance | No breach | Routine supervision |

**Critical Incident** = actual consequence Class 4 or 5. Activates the Crisis
Management Team (CMT) — the standing crisis-response body convened under the
MFG Crisis Management Plan (`MFG-WHS-PR-070`), chaired by the relevant BU
General Manager with the Group GM WHS as a standing member.

**HiPo** = any event that could realistically have resulted in a Class 4 or 5
consequence (permanent incapacity or death), regardless of the actual outcome.
Rated on potential consequence.

**Injury Classifications**:

| Classification | Acronym | Key criteria |
|---|---|---|
| Fatality | F | Work-related death. Recordable |
| Lost Time Injury | LTI | One or more full rostered shifts lost after the shift on which the injury occurred. Recordable |
| Restricted Work Injury | RWI | Unable to perform full normal duties; alternative or reduced duties assigned. Recordable |
| Medical Treatment Injury | MTI | Treatment by a medical practitioner beyond first aid, with no lost or restricted time. Recordable |
| First Aid Injury | FAI | Treatment within the scope of first aid training only. Not recordable |
| Occupational Illness | OI | Illness arising from workplace exposure over time (including psychological injury, noise-induced hearing loss, silicosis). Managed and reported separately from injury statistics |

The **Recordable** column above is the single source of truth for MFG's
recordable set, which drives the rate formulas in `analytics.md` §2: total
recordable injuries (TRI) = Fatality + LTI + RWI + MTI, and
TRIFR = TRI / hours worked × 1,000,000. RWI (restricted work injury) is
recordable and is counted in the numerator. RWI is a US OSHA-origin
recordability concept adopted here as a documented organisational convention;
under the (now-withdrawn) AS 1885.1 the AU convention was
TRIFR = Fatality + LTI + MTI.

**Statistical inclusion — the Operational Control Rule**: an incident is
included in MFG's recordable statistics only where MFG had **operational
control** of the work — MFG set the work method, supervised the task, and the
work ran under MFG's management system. Where MFG holds a **commercial interest
only** (e.g. landlord arrangements, minority joint ventures, brand licensing
without direction of the work), record the event for lessons sharing but
exclude it from recordable statistics. Document the determination and rationale
in the incident system.

**Internal Notification Requirements (MFG-WHS-PR-002 Schedule 2)** — verbal
means person-to-person; an unanswered message does not discharge the
notification. HiPo notification is set by **actual** harm (the event caused
little or no injury), so its internal chain is deliberately lighter than the
equivalent actual Class 4–5 event; the **potential** severity instead drives
the investigation rigour (ICAM at Class 4–5/HiPo per Schedule 3) and the
incident review call:

| Class | Verbal | Written / incident system |
|---|---|---|
| 1–2 | To supervisor before end of shift | Incident system entry within 48 hrs |
| 3 | ASAP to contract/site manager and WHS Business Partner | Incident system entry + PIIN within 24 hrs |
| 4 | Immediate to BU WHS Manager and BU General Manager | Incident system entry + PIIN within 12 hrs |
| 5 | Immediate to BU General Manager, Group GM WHS, and CEO | Incident system entry + PIIN within 12 hrs |
| HiPo | Immediate to BU WHS Manager | Incident system entry + PIIN within 24 hrs |

**Regulator-notifiable incidents**: whether an incident is notifiable to the
WHS regulator is determined against the jurisdictional triggers in
`legislation.md` §5 (death, serious injury/illness, dangerous incident).
The **Group GM WHS** owns the regulator-notification decision and ensures it is
made and recorded within the statutory timeframe; the determination and its
basis are documented in the incident system. Notification to the regulator does
not displace the internal notification requirements above.

**Investigation Requirements (MFG-WHS-PR-002 Schedule 3)**:

| Class | Methodology |
|---|---|
| 1 | Supervisor review in the incident system; learning huddle where useful |
| 2–3 | Standard investigation (MFG-WHS-FM-021), supported by 5-Why (MFG-WHS-FM-024) |
| 4–5 / HiPo | ICAM (MFG-WHS-TP-022) led by a trained lead investigator; reviewed by the BU WHS Manager; endorsed by the Group GM WHS |
| Fatality / serious environmental harm | ICAM + legal advice via General Counsel before any report is circulated |

**Incident Management Process (MFG-WHS-PR-002)** — 10-step workflow:
1. Respond — make the area safe, render assistance, preserve the scene
2. Verbal notification per Schedule 2
3. Regulator notification where the incident is notifiable (see
   `legislation.md` §5; phone script at `output-templates.md` §23)
4. Enter the event in the incident system; classify actual and potential
   consequence per Schedule 1; apply the Operational Control Rule and record
   the determination
5. Submit the PIIN (MFG-WHS-FM-020) within the Schedule 2 timeframe
6. Incident review call for Class 4–5 and HiPo — BU General Manager, contract
   manager, and BU WHS Manager within 1 business day; Group GM WHS invited
7. Allocate the investigation per Schedule 3
8. Assign corrective actions in the incident system with P1/P2/P3 priorities;
   verify effectiveness before closure
9. Lessons learnt — safety alert (mandatory for notifiable incidents) or
   bulletin
10. Close out in the incident system; feed themes to the quarterly analytics
    review

**For disciplinary matters** related to incidents: refer to MFG-WHS-PR-014
Fair and Just Culture Procedure.

### 6. Document Templates & Forms

| Document | Reference |
|---|---|
| Safety Alert | MFG-WHS-TP-010 |
| Safety Bulletin | MFG-WHS-TP-011 |
| Preliminary Internal Incident Notification (PIIN) | MFG-WHS-FM-020 |
| Standard Incident Investigation | MFG-WHS-FM-021 |
| ICAM Investigation Report | MFG-WHS-TP-022 |
| ICAM Interview Record | MFG-WHS-FM-023 |
| 5-Why Analysis | MFG-WHS-FM-024 |
| Lessons Learnt Bulletin & Register | MFG-WHS-TP-030 / MFG-WHS-FM-031 |
| Enterprise Risk & Opportunity Register | MFG-RM-FM-001 |
| WHS Risk Register | MFG-WHS-FM-005 |
| Plant & Equipment Risk Assessment | MFG-WHS-FM-040 |
| Hazardous Chemicals Risk Assessment | MFG-WHS-FM-041 |
| Manual Tasks Risk Assessment | MFG-WHS-FM-042 |
| SWMS Template | MFG-WHS-TP-050 |
| Traffic Management Plan | MFG-WHS-TP-051 |
| Take 5 (point-of-work risk check) | MFG-WHS-FM-060 |
| BU Governance Template Suite | MFG-WHS-TP-201 through MFG-WHS-TP-206 |

### 7. Systems & Tools

| Purpose | System |
|---|---|
| Incident management | INX InControl |
| WHS management system platform | Lucidity (an Ideagen company) |
| Analytics & dashboarding | Power BI |
| Project & task management | Microsoft Planner |
| Contractor management & prequalification | Rapid Global |
| Audit & inspection | SafetyCulture (iAuditor) |
| Document storage / lessons sharing | SharePoint (Group WHS site) |

*System names are illustrative of a typical mid-to-large AU/NZ stack —
substitute your own platforms.*

### 8. Critical Risk Taxonomy

**MFG Critical Risks (12)**:
Working at Height; Electrical Safety; Isolation & Stored Energy; Mobile Plant &
Pedestrian Interaction; Confined Spaces; Hazardous Chemicals; Asbestos &
Hazardous Building Materials; Hot Work & Fire; Lifting Operations & Suspended
Loads; Driving & Road Risk; Occupational Violence & Aggression; Excavation &
Underground Services.

**Critical Risk Owner (CRO)** model — a named senior leader per critical risk,
accountable for understanding the risk profile, the adequacy of critical
controls, and the coverage of the verification program for that risk.

**Critical Control Verification (CCV)** — field verification that critical
controls are in place and functioning, separate from compliance audit.
Frequency is set per risk in the CCV schedule (monthly for the highest-exposure
risks); completion and findings are reported through Power BI to BU and Group
dashboards.

### 9. Engagement Programs & Campaigns

**SafeStart Summer** — flagship annual campaign.
- Duration: 6 weeks across December–January
- Cadence: weekly themed toolbox talk plus a site activation each week
- Themes: seasonal and critical-risk anchored — heat and UV, hydration and
  fatigue, storm-season electrical safety, driving, end-of-year distraction
- Facilitation: site and contract leaders, supported by WHS Business Partners
- Recognition: weekly site recognition draws; participation reported by BU
- Outcome (illustrative): the most recent campaign reached ~85% of the rostered
  workforce and lifted hazard reporting across the following quarter

**Critical Risk Reset** — quarterly program.
- One critical risk per quarter, set by the Group WHS annual plan
- Half-shift pause at every site: leader-led discussion plus a critical control
  verification walk
- Findings feed the CCV dashboard and the quarterly BU WHS review

Format reference: see `programs.md` §2 for the sustained-campaign
architecture these programs use.

### 10. Governance & Reporting Cadence

- **Board safety reporting**: quarterly Safety & Sustainability Committee
  paper; annual full-board WHS deep-dive (February) sets risk appetite and
  program priorities for the year
- **ELT reporting**: monthly WHS dashboard — HiPo intelligence, critical
  control health, leading and lagging indicators
- **Officer due diligence**: twice-yearly structured officer briefings plus a
  scheduled site walk program, coordinated by the Group GM WHS; CRO
  accountability runs in parallel
- **Site Safety Exchange**: cross-BU peer review program — each contract
  cluster is reviewed twice a year by peers from another business unit;
  findings tracked through the audit platform

**Key Roles**:

| Role | Scope |
|---|---|
| Group GM WHS | Executive accountability for WHS across the group; reports to the CEO |
| BU WHS Manager | Business-unit WHS leadership |
| WHS Business Partner | Embedded support to contracts and sites |
| Group WHS Systems & Analytics Lead | Incident system, dashboards, performance reporting |
| Critical Risk Owner (CRO) | Named senior owner per critical risk topic |
| Contract / Site Manager | First-line operational accountability — required attendee at Class 4–5 / HiPo incident review calls |
| General Counsel | Internal legal advisory for serious incidents and privilege questions |

---

*To adapt this skill for another organisation, replace the Active Reference
content above with your own — mirroring the Template structure. The other
reference files are organisation-agnostic and will read your context through
this file.*

---

## Multi-tenant use

For consultants or multi-divisional groups maintaining several organisation
profiles, two supported patterns:

1. **Claude Project knowledge (recommended for claude.ai)** — keep this file
   generic (or as the fictional worked example) and hold each organisation's
   profile in a Claude Project's knowledge. The skill reads whichever profile
   the active Project supplies; no re-packaging per client.
2. **Profile files (for packaged/repo use)** — keep one file per client
   (`company-<client>.md`) alongside this file and copy or symlink the active
   one to `company.md` before packaging. The full workflow is in `ADAPTING.md`
   in the source repository (github.com/whosneet/whs-professional-skill).

Whichever pattern is used, treat the active profile as the single source of
truth for risk matrix values, severity classifications, document codes, and
named programs — never blend two organisations' configuration in one output.

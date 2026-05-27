# Inspections, Audits & Permit-to-Work Systems

Operational reference for the three assurance mechanisms that occupy most of a
WHS manager's week: routine inspections, formal audits, and permit-to-work
systems. These are distinct disciplines with different methodologies, competency
requirements, and evidentiary weight — confusing them is one of the most common
governance failures in WHS practice.

---

## Table of Contents
1. [Scope and Key Distinctions](#1-scope-and-key-distinctions)
2. [Workplace Inspection Program Design](#2-workplace-inspection-program-design)
3. [WHS Audit Methodology](#3-whs-audit-methodology)
4. [Permit-to-Work Systems](#4-permit-to-work-systems)
5. [Pre-Task and Point-of-Work Risk Assessment Tools](#5-pre-task-and-point-of-work-tools)
6. [Output Checklist](#6-output-checklist)

> For organisation-specific audit programme, permit types in use, inspection
> cadence, and template numbering, load `references/company.md`.

---

## 1. Scope and Key Distinctions

The three terms — inspection, audit, verification — are routinely used
interchangeably in operational WHS practice. They are not the same thing, and
the confusion has real consequences: inspectors briefed to do an audit, auditors
asked to verify controls, and verifications presented to regulators as audit
evidence. Each discipline has a defined purpose, methodology, competency profile,
and evidentiary standard.

| Discipline | Purpose | Methodology | Output |
|---|---|---|---|
| **Inspection** | Regular check of a workplace, area, plant, or control against a defined checklist or standard | Walkaround + checklist; visual; tactile where appropriate | Inspection record with findings, classifications, and corrective actions |
| **Audit** | Systematic, independent, documented evaluation of conformance to defined criteria (ISO 19011) | Document review + interview + observation + sampling | Audit report with non-conformities, observations, and OFIs |
| **Verification** | Ongoing confirmation that a specific control is in place and effective | Targeted observation of the named control under operating conditions | CCV record, escalation if degraded (cross-reference `frameworks.md` §7) |

### Why the distinction matters

- **Different purpose** — inspection looks for hazards; audit looks for system
  failures; verification confirms control health. Conflating them produces
  outputs that do none of the three well.
- **Different methodology** — auditors must be independent of the area being
  audited (ISO 19011 5.5.4). Inspectors and verifiers typically are not — and
  do not need to be. Treating an inspection as an audit creates an evidence
  trail that fails on independence grounds when scrutinised.
- **Different competency** — a lead auditor qualification (5-day course + audit
  experience) is not interchangeable with inspection technique training (half
  day). A trained CCV verifier is not necessarily competent to lead an internal
  ISO 45001 audit.
- **Different evidentiary weight** — audit reports are the formal evidence base
  for ISO 45001 management review (clause 9.3), certification, and regulator
  defence. Inspection records and CCV records are operational artefacts. Using
  an inspection record where an audit report is required (e.g., for ISO 45001
  9.2 conformance) is a common non-conformity finding.

### The PCBU duty to verify

Model WHS Regulation 38 requires the PCBU to **review** and as necessary
**revise** control measures so that they remain effective. Specifically, review
must occur when:
- The control measure does not control the risk so far as is reasonably practicable
- Before a change at the workplace is likely to give rise to a new or different risk
- A new hazard or risk is identified
- The results of consultation indicate review is required
- A health and safety representative requests a review

Inspection, audit, and verification are the three mechanisms by which this duty
is operationalised. The PCBU cannot rely on any single mechanism — each has a
distinct function in the management system.

> Cross-reference `frameworks.md` §3 for the ISO 45001 clauses that frame these
> obligations (6.1.2, 8.1.2, 9.1, 9.2, 10.2) and `frameworks.md` §7 for the
> Critical Control Verification methodology.

---

## 2. Workplace Inspection Program Design

### Inspection types

| Type | Purpose | Frequency | Conductor |
|---|---|---|---|
| Informal walkaround | General hazard spotting; visible leadership | Daily/shift | Supervisor + worker |
| Formal documented inspection | Defined checklist, recorded findings, tracked actions | Weekly to monthly | Supervisor or WHS rep |
| Pre-task inspection | Specific to high-risk task; condition of plant, environment, controls | Per task | Task-relevant competent person |
| Plant/equipment inspection | Statutory plant inspection (cranes, EWPs, pressure vessels, hoists) | Per regulation (typically annual or per service interval) | Licensed/competent inspector |
| HSR-initiated inspection | Worker representative inspection (statutory power under model WHS Act s 68) | On request | HSR + accompanying person of HSR's choice |
| Critical control verification | Control-specific verification (cross-reference `frameworks.md` §7) | Daily to monthly per risk profile | Frontline + WHS |
| Executive/leadership safety walk | Visible felt leadership; engagement with frontline | Monthly to quarterly | Executive + WHS escort |

### Inspection program elements

A documented inspection program should include:

- **Inspection schedule** — by area, by frequency, by responsible role; published
  and tracked (not left to memory)
- **Standardised checklists** — calibrated to the area; differ for office,
  warehouse, workshop, construction site, hazardous chemicals store
- **Hazard category coverage** — housekeeping, electrical, plant, chemicals,
  fire, signage, PPE, emergency egress, ergonomics, manual handling,
  environment (lighting, noise, temperature)
- **Finding classification** — immediate corrective action / scheduled
  correction / observation only
- **Close-out tracking** — findings logged in the incident/hazard management
  system or a dedicated tracker; due dates monitored
- **Periodic effectiveness review** — review of the inspection program itself
  against incident data: are inspections finding what incidents reveal?

### Standardised checklist categories

| Category | Typical inspection points |
|---|---|
| Housekeeping | Walkways clear, no slip/trip hazards, materials stored correctly, waste managed |
| Electrical | Test and tag currency, no damaged leads, RCDs in place, switchboard access |
| Plant | Guards in place, isolation points marked, condition, daily pre-start records |
| Chemicals | SDS available and current, containers labelled, bunding, segregation, spill kit |
| Fire | Extinguishers in date, hose reels accessible, emergency exits unobstructed, EWP plan displayed |
| Signage | Mandatory, warning, emergency signs present, legible, correct |
| PPE | Available, condition, correct selection, worn correctly |
| Emergency | Assembly points marked, first aid stocked, AED accessible, contact details current |
| Ergonomics | Workstation setup, manual handling aids in use, repetitive task rotation |
| Amenities | Toilets, drinking water, eating areas clean and sufficient (model WHS Reg 41) |

### Finding classification

| Classification | Definition | Response |
|---|---|---|
| Immediate corrective action (Category A) | Imminent risk of serious harm; control failure with active exposure | Stop work; rectify before resuming; notify line manager and WHS |
| Scheduled correction (Category B) | Hazard requiring action but not imminent risk | Logged with owner and due date (typically 7–30 days depending on risk) |
| Observation (Category C) | Minor finding; opportunity for improvement | Logged; addressed in next planned maintenance or program cycle |

Avoid binary pass/fail classifications — they collapse genuinely different
risks into the same response category and incentivise minimisation.

### Inspector competency

| Inspection type | Competency requirement |
|---|---|
| General workplace inspection | WHS induction + inspection technique training (typically half day); familiarity with relevant SOPs |
| Pre-task inspection (HRCW) | Task-specific training; SWMS familiarity; competency to identify control failure |
| Statutory plant inspection | Relevant HRWL (e.g., crane, EWP, scaffold) or trade qualification (electrical, mechanical) |
| Confined space, hazardous chemicals, asbestos | Task-specific training (confined space entry, asbestos awareness, hazardous chemicals handling) |
| HSR-initiated inspection | Completion of approved HSR training (5 days, model WHS Act s 72) |
| Critical Control Verification | CCV training specific to the control; competency demonstrated, not assumed |
| Executive safety walk | WHS escort briefs the executive; structured engagement script; no expectation of independent hazard identification |

### Common inspection program failures

- **Checklist becomes the ceiling, not the floor** — inspectors stop looking
  for hazards not on the checklist
- **Tick-and-flick** — inspector signs off without physical walk; usually
  visible in the time-stamped data
- **Same inspector forever** — fresh eyes find new things; rotate where practicable
- **No close-out** — findings logged but not actioned; backlog grows; trust in
  the program collapses
- **No upward trend analysis** — same finding recurring in the same area is a
  systemic issue, not an inspection issue
- **No alignment with incident data** — inspections finding A while incidents
  reveal B means the inspection program is not calibrated to actual risk

---

## 3. WHS Audit Methodology

### Standards framework

| Standard | Application |
|---|---|
| **ISO 19011:2018** | Guidelines for auditing management systems — THE reference for audit methodology, planning, conduct, and auditor competency |
| **ISO/IEC 17021-1** | Requirements for bodies providing audit and certification of management systems (third-party certification) |
| **ISO 45001:2018** | The OH&S management system being audited (cross-reference `frameworks.md` §3) |
| **ISO 31000:2018** | Risk management — guidelines (used to frame audit risk assessment) |
| **AS/NZS 4801:2023** | Withdrawn standard, but still referenced in some legacy contracts and government schedules |

### Audit types

| Type | Description | Typical conductor |
|---|---|---|
| **First party (internal)** | Conducted by the organisation on itself; mandated for ISO 45001 clause 9.2; ensures the management system is functioning | Internal auditors (may be from another business unit) |
| **Second party** | Conducted by, or on behalf of, an interested party in the organisation | Typically a client auditing a contractor's WHS system; principal contractor auditing subcontractor |
| **Third party** | Conducted by an external, independent body | Accredited certification body (e.g., BSI, SAI Global, BV, DNV) for ISO 45001 certification |

### Audit programme vs individual audit

A common confusion. They are different things, owned by different people.

- **Audit programme** — the multi-year plan covering scope, frequency,
  methodology, resources, reporting line, and the cycle by which all areas of
  the management system are audited. Owned by the WHS Manager or equivalent.
  Reviewed annually.
- **Individual audit** — a specific instance with defined scope, criteria,
  schedule, audit team, and reporting deadline. Assigned to a lead auditor.

The programme exists to ensure no part of the OH&SMS goes unaudited; the
individual audit executes one slice of that plan.

### Audit planning steps

1. **Define audit scope** — what part of the OH&SMS, what locations, what
   timeframe, what activities are included. Exclusions are listed explicitly.
2. **Define audit criteria** — ISO 45001 clauses, organisational standards,
   legislation, codes of practice, contractual requirements. The criteria are
   the yardstick against which conformance is measured.
3. **Audit team selection** — lead auditor (qualified) + technical experts
   where required (e.g., process engineer for major hazard facility audit).
   Auditors must be independent of the area being audited.
4. **Notification to auditee** — typically 2–4 weeks before commencement;
   includes scope, criteria, methods, team, and high-level schedule.
5. **Document review (pre-audit)** — auditor reviews relevant procedures,
   prior audit reports, incident records, training matrices, hazard register,
   risk register, corrective action register.
6. **Audit plan circulated** — objectives, scope, criteria, day-by-day
   schedule, attendees by session, methods (interview, observation, document
   review, sampling rationale).
7. **Opening meeting** — confirm scope and arrangements; introduce team;
   confirm logistics and access.

### Auditor competency and independence

| Role | Competency |
|---|---|
| Lead auditor (third-party / external) | ISO 45001 Lead Auditor qualification (5-day Exemplar Global certified course); demonstrated audit experience (typically 20 audit days minimum for IRCA / Exemplar Global certification); continual development (10–15 hours CPD per year typical) |
| Internal auditor (first-party) | Shorter qualification (1–3 day internal auditor course) is sufficient; should still have demonstrated audit experience under supervision before leading internal audits |
| Technical expert | Subject matter expertise (engineering, occupational hygiene, process safety); typically supports the audit team rather than leading |
| Auditor in training | Conducts audits under direct supervision of qualified lead auditor; logs experience for future certification |

**Independence requirement**: Auditor must not audit work for which they are
responsible, or work performed by their direct reports. This is implicit in the
model WHS Regulations (effective risk review requires independence) and
explicit in ISO 19011 (5.5.4). Breaches of independence are a structural
governance failure — the audit findings cannot be relied on.

### Evidence collection techniques

| Technique | Use | Cautions |
|---|---|---|
| **Interview** | Understand how work is done; check awareness; explore implementation | Multiple sources; triangulate; avoid leading questions; document verbatim where possible |
| **Observation** | Verify actual practice (Work-as-Done) vs documented procedure (Work-as-Imagined) — cross-reference `frameworks.md` §4 | Do not rely on planned observations only; spot-check unplanned activities |
| **Document review** | Records, registers, training matrices, incident reports, corrective action evidence | Documents prove process exists; not that it is followed |
| **Sampling** | Representative not exhaustive; document the sampling rationale | Sample size must justify the conclusion; small samples generate weak findings |
| **Physical inspection** | Verify physical condition of plant, equipment, infrastructure | Auditor must be competent to inspect what they are looking at |

### Finding classification

| Classification | Definition | Response |
|---|---|---|
| **Major non-conformity (Major NC)** | Absence of, or systemic failure to implement and maintain, a required process; significant doubt about ability to meet a requirement; could result in delivery of a non-conforming outcome | Immediate corrective action; root cause analysis required; effectiveness verification before close; in certification context — may suspend or withdraw certification if not addressed |
| **Minor non-conformity (Minor NC)** | Single observed lapse from a required process; isolated occurrence not affecting overall system | Corrective action with defined timeframe (typically 60–90 days) |
| **Observation (Obs)** | Could become a non-conformity if not addressed; trend warning; deviation that does not yet meet NC threshold | Monitor; consider preventive action |
| **Opportunity for Improvement (OFI)** | Not a non-conformity; suggestion to enhance performance beyond compliance | Optional; consider for inclusion in continual improvement plan (ISO 45001 10.3) |

### Audit report structure

- **Executive summary** — scope, criteria, key findings, overall recommendation
  (continue certification / corrective action required / etc.)
- **Detailed findings** — each finding with:
  - Evidence (what was observed, who was interviewed, what was reviewed)
  - Classification (Major NC, Minor NC, Obs, OFI)
  - Related criterion clause (e.g., ISO 45001 6.1.2, WHS Reg 38)
  - Recommended corrective action direction
- **Positive findings** — strengths, good practice (often omitted; including
  them gives a balanced picture and improves auditee engagement)
- **Appendices** — audit plan, attendees by session, documents reviewed,
  sampling rationale, photographs (where relevant)
- **Distribution** — auditee senior management + audit programme owner;
  certification body where applicable

### Corrective action and effectiveness verification

| Finding | Response timeframe (typical) | Effectiveness verification |
|---|---|---|
| Major NC | 30 days for corrective action plan; 60–90 days for implementation | After implementation + sufficient time for the action to demonstrate effect (typically 3–6 months); verified by independent reviewer |
| Minor NC | 60–90 days for implementation | Verified at next surveillance audit or by management review |
| Observation | Tracked; addressed in next planning cycle | Reviewed at next audit |
| OFI | Optional; if accepted, tracked through continual improvement register | Reviewed in management review |

**Open audit findings beyond due date are a governance failure.** They are
visible in any subsequent audit and form the basis for escalated findings in
certification audits. Track open findings as a leading indicator at management
review and board reporting.

### Common audit pitfalls

- **Audit becomes inspection** — auditor finds individual hazards instead of
  system failures; result is a list of hazards, not a conformance assessment
- **Sampling without rationale** — auditor reviews three documents and finds
  no NC; the finding does not support a system-level conclusion
- **No triangulation** — single source of evidence used to support a finding;
  collapses if challenged
- **Auditor independence breach** — auditor audits their own area or their
  direct reports' work; finding is structurally unreliable
- **Same auditor every cycle** — relationship erodes independence and rigour;
  rotate where practicable
- **Findings without evidence** — finding written as conclusion only;
  auditee cannot dispute or respond effectively
- **Auditor opinion presented as fact** — finding states "the system is
  inadequate" without the evidence base; weakens the audit overall

---

## 4. Permit-to-Work Systems

A permit-to-work (PTW) is a formal written authorisation issued before
specified categories of work commence. It is a governance wrapper around
high-energy or high-consequence work — not a substitute for the underlying
risk assessment, procedure, or competency.

### When permit-to-work applies

PTW is appropriate where:
- High-energy or high-consequence work where failure of a control would result
  in serious harm or fatality
- Non-routine work that combines hazards not addressed by standing procedures
- Work that requires coordination between trades, sites, or systems
- Work that requires isolation of energy or process (electrical, mechanical,
  hydraulic, pneumatic, chemical, thermal, radiation, gravity)
- Work in or near operating plant where the work activity introduces a hazard
  to the operation, or vice versa

### Common permit types

| Permit type | Trigger | Key controls |
|---|---|---|
| **Hot work permit** | Welding, cutting, grinding, soldering, or any open flame/spark in an area not designated for hot work | Fire watch; atmospheric test for flammables; extinguishers; isolation of flammable sources; post-work fire watch (typically 30–60 min) |
| **Confined space entry permit** | Any confined space as defined in AS 2865:2009 (cross-reference `hazards.md` §11 once added) | Atmospheric test (O₂, LEL, toxics); standby person; rescue plan; communication; continuous or repeat atmospheric monitoring |
| **Working at height permit** | Above defined threshold (typically >2 m or as per site rule) | Anchor verification; fall arrest or restraint; rescue plan; weather criteria; competent person |
| **Isolation / Lock-Out Tag-Out (LOTO) permit** | Energy isolation for maintenance, inspection, or cleaning | Six-step isolation; verification (test for dead); personal locks; isolation register; defined removal sequence |
| **Excavation permit** | Below defined depth (typically >1.5 m per model WHS Reg 297) | Service locates (Dial Before You Dig); shoring/benching/battering; atmospheric test if confined; edge protection; spoil management |
| **Electrical work permit** | Energised electrical work where de-energisation is not reasonably practicable (model WHS Reg 158) | Risk assessment; competent licensed person; PPE rated for arc flash; isolation of adjacent circuits; rescue plan |
| **Live line permit** | Work on energised overhead or underground electrical infrastructure | Network operator authorisation; access permit; safety observer; defined approach distances |
| **Crane lift permit (critical lift)** | Lift above defined weight, near critical infrastructure, or tandem lift | Lift plan; competent rigger and dogger; ground assessment; exclusion zone; weather criteria |
| **Roof access permit** | Work on or near a fragile or sloping roof | Anchor verification; fall arrest or perimeter protection; competent person; weather criteria |
| **Pressure system permit** | Work on pressurised systems (steam, gas, hydraulic) | Depressurisation verified; isolation; venting confirmed; competent person |

### Permit lifecycle

1. **Application** — work requestor describes scope, location, duration,
   hazards identified, and proposed controls
2. **Hazard assessment** — issuer (and area authority where applicable)
   reviews the application; verifies hazards and controls; identifies
   interactions with other work or operations
3. **Control verification** — physical verification that controls are in
   place before permit is issued (not after); isolations tested; atmosphere
   sampled; equipment inspected
4. **Permit issue** — written permit signed by issuer + holder; copies
   displayed at work area, in permit register, and with shift coordinator
5. **Work execution** — work proceeds under permit conditions only; any
   change in scope, conditions, or personnel requires permit reissue
6. **Monitoring** — periodic check during the work, especially confined
   space (continuous atmospheric monitoring) and hot work (fire watch);
   time-bound permits checked at expiry
7. **Suspend** — for shift end, weather change, atmospheric change, alarm,
   or emergency; suspension is documented; resumption requires re-verification
   of all controls
8. **Hand-back** — work complete; area returned to safe state; isolations
   removed in defined sequence; all tools and personnel accounted for
9. **Close** — permit closed in register; any lessons or anomalies logged;
   permit retained as record (retention period per organisation, typically
   7 years for HRCW)

### Permit governance

| Element | Description |
|---|---|
| **Authorised issuer** | Trained, formally appointed, competent in the specific permit type; not the same as the work holder; cannot issue permit to themselves |
| **Permit register** | Live record of all open permits; integrated with shift handover and emergency response; visible to incident commander in event of evacuation |
| **Permit audit** | Routine sampling of issued permits for quality; typically monthly; reviews completeness, control adequacy, time discipline |
| **Permit failure analysis** | Incidents involving open permits are over-investigated relative to incident severity — they reveal systemic permit weakness |
| **Cross-permit conflict check** | Issuer verifies no incompatible work is in progress in the same area (e.g., hot work + flammable atmosphere; isolation + adjacent live work) |

### Common permit failure modes

- **Over-permitting** — every task gets a permit; permit fatigue sets in;
  quality of risk assessment degrades; issuers become rubber stamps
- **Under-permitting** — high-risk work proceeds without permit because the
  trigger criteria are unclear or because permitting is seen as bureaucratic
- **Expired permits** — time-bound conditions (e.g., atmospheric validity for
  confined space) not enforced; work continues past valid period
- **Parallel permits** — two permits issued for incompatible work in the same
  area; isolation removed by one party while another is still working
- **Standing permits** — permanent permits for "routine" tasks lose the
  verification function entirely; effectively no permit at all
- **Sign-off without verification** — holder ticks the box without physical
  check of controls; very common in confined space atmospheric tests
- **Inadequate revocation procedures** — when conditions change (weather,
  alarm, near miss), there is no clear mechanism to revoke active permits
- **Verbal extensions** — permit time extended verbally without re-verification;
  controls degrade silently between issue and extension
- **Holder ≠ worker** — permit issued to one person; work performed by another
  who has not been briefed on the permit conditions

### Integration with isolation procedures

Isolation is the mechanism; the permit is the governance wrapper. Each
isolation point must be identified in the permit, with an isolation register
attached. The standard sequence:

1. Identify all energy sources affecting the work (electrical, mechanical,
   hydraulic, pneumatic, chemical, thermal, gravity, stored)
2. Plan the isolation — what is isolated, in what sequence, by whom, verified how
3. Isolate at the source — not just at the local switch
4. Lock and tag — personal lock per worker; tag identifies isolator, date, work
5. Test for dead — verify the isolation is effective at the point of work
6. Perform work under permit
7. Remove personal locks in reverse sequence; restore in defined order
8. Functional check after re-energisation

> Cross-reference `hazards.md` §10 (energy isolation / LOTO methodology) once
> added; for electrical isolation specifically, AS/NZS 4836:2023 sets the
> standard for safe work on low-voltage electrical installations.

---

## 5. Pre-Task and Point-of-Work Risk Assessment Tools

These are not inspections, not audits, not permits — they are worker-level
risk assessment tools applied at the point of work, before or during a task.
They have a defined role and defined limits.

### Common tools

| Tool | Acronym / meaning | Typical use |
|---|---|---|
| **Take 5** | — | Pre-start mental check; typically 5 questions on a card (Stop, Look, Identify, Assess, Manage) |
| **SLAM** | Stop, Look, Assess, Manage | Pre-task brief; widely used in maintenance and field work |
| **STAR** | Stop, Think, Act, Review | Point-of-work hazard check (Downer-branded; now widely adopted across infrastructure) |
| **JSEA / JHA** | Job Safety/Hazard Analysis | Documented task-level risk assessment; more substantial than Take 5; not a SWMS |
| **SWMS** | Safe Work Method Statement | Statutory document for HRCW (model WHS Reg 299; cross-reference `hazards.md` §4) |
| **Dynamic risk assessment** | — | Continuous reassessment during changing conditions; typical of emergency services and dynamic environments |
| **Pre-start meeting / toolbox** | — | Crew-level briefing at shift start; covers task, hazards, controls, coordination |

### When pre-task tools are sufficient — and when escalation is needed

| Situation | Appropriate tool |
|---|---|
| Routine task; known hazards; standing procedures cover the work; competent worker; conditions match plan | Pre-task tool (Take 5, SLAM, STAR) |
| High-risk work; non-routine task; hazards not in standing procedures; changed conditions | JSEA/JHA |
| High-Risk Construction Work (any of the 18 categories in `hazards.md` §8) | SWMS — statutory requirement; pre-task tool is supplementary, not substitute |
| High-energy work; multi-trade coordination; isolation required | Permit-to-work + JSEA/SWMS underneath |
| Emergency response; rapidly changing conditions | Dynamic risk assessment + incident command structure |

### Quality criteria for pre-task tools

A pre-task tool is only as valuable as the engagement that produced it.

- **Done at the workplace, not in the crib room** — assessment must be of the
  actual conditions at the actual location
- **Workers involved** — not filled out by the supervisor in advance and
  handed out for signature
- **Triggers action when control is missing or hazard is new** — the tool must
  have a defined "stop" pathway; otherwise it is a tick-the-box exercise
- **Reviewed periodically by WHS function for quality** — sample, not all;
  look for evidence of engagement vs evidence of compliance
- **NOT used as a substitute for substantive risk management** — a Take 5
  card is not a risk assessment; it is a final check that the risk assessment
  was right and conditions match

### Common pre-task tool failures

- **Filled out in the crib room before walking to the workplace** — assessment
  is theoretical, not actual
- **Same hazards listed every day** — copy-paste behaviour; engagement is zero
- **Supervisor fills out for the crew** — workers' actual hazard awareness is
  not assessed; they have no ownership
- **"Stop" never triggered** — over months, a card with no stops is not
  evidence of safety; it is evidence the tool is not being used to assess
- **Used as the only risk assessment for high-risk work** — pre-task tools are
  insufficient for HRCW, confined space, hot work, isolation, etc.

---

## 6. Output Checklist

Before finalising any inspection, audit, or permit output, confirm:

### Inspection outputs
- [ ] Inspection finding has owner, due date, and verification mechanism
- [ ] Finding classification (immediate / scheduled / observation) is applied,
      not binary pass/fail
- [ ] Recurring findings flagged as systemic, not just logged again
- [ ] Inspection programme effectiveness reviewed against incident data

### Audit outputs
- [ ] Audit scope and criteria explicit at the start of the report
- [ ] Each finding has evidence, classification, and related criterion clause
- [ ] Major NC has root cause analysis, not just symptom fix
- [ ] Minor NC has clear corrective action and timeframe
- [ ] Sample audit findings vs systemic findings distinguished
- [ ] Effectiveness verification scheduled, not assumed
- [ ] Auditor independence confirmed; no audit of own work
- [ ] Distribution includes audit programme owner + auditee senior management

### Permit outputs
- [ ] Permit has authorised issuer (not the holder; not the worker)
- [ ] Hazards and controls verified physically before issue
- [ ] Time-bound conditions defined; expiry enforced
- [ ] Revocation criteria defined (weather, alarm, changed conditions)
- [ ] Cross-permit conflict check completed for the area
- [ ] Hand-back procedure documented; isolations removed in defined sequence
- [ ] Permit closed in register with any lessons logged

### Pre-task tool outputs
- [ ] Completed at the workplace, by the worker doing the work
- [ ] Evidence of engagement, not just signature
- [ ] Escalated to JSEA or SWMS where the situation requires it
- [ ] Not relied on as the sole risk assessment for HRCW or high-energy work

---

For organisation-specific audit programme, permit types in use, and inspection
cadence, load `references/company.md`.

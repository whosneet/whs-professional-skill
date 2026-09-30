# Case Studies Reference — Everyday Critical-Risk Incidents (Worked Examples)

Five worked examples of the everyday incidents that kill people in AU/NZ
workplaces: a fall through a fragile roof, a confined space entry with a
would-be rescuer, an isolation failure on a conveyor, a yard truck striking
a visiting driver on foot, and exertional heat stroke in a new starter.
Each ends in serious injury rather than death, so each is investigated to
its fatal potential. Load this file when an investigation, HiPo review,
critical control verification, toolbox or training session involves falls
from height, confined spaces, isolation and LOTO, mobile plant and
pedestrians, or heat, and when the question is what the regulator will
expect: who notifies, who preserves the site, which regulation governs the
task and where the states, territories and NZ differ.

This file continues `case-studies-everyday.md`, which holds Cases 1–7
(forklift HiPo, manual handling, psychosocial complaint, electrical near
miss, slip-trip-fall, chemical decant, fatigue). Case numbers run on from 8
so every case is unique across both files. For major catastrophes used in
board papers and strategic training, see `case-studies.md`; for AU/NZ
disasters and the first industrial manslaughter prosecutions, see
`case-studies-anz.md`. The control standards these cases test sit in
`hazards.md` (§6 heat, §9 working at height, §10 isolation, §11 confined
spaces, §12 mobile plant); critical control verification in
`frameworks.md` §7; ICAM method in `investigation.md` §1.

All cases are fictional but constructed from common AU/NZ incident
patterns. Names, places, times, dimensions and contract values are
illustrative; legislation, codes, standards and published incidents are
real and cited. Case 9 is set in Meridian Facilities Group (MFG), the
fictional organisation in `company.md`; the other cases use generic
organisations and read classification thresholds from `company.md` §5 as
an example of an organisation's definitions.

---

## Table of Contents
1. [How These Cases Are Built](#1-how-these-cases-are-built)
2. [Case 8 — Fall Through Fragile Roof](#2-case-8--fall-through-fragile-roof)
3. [Case 9 — Confined Space Entry and Would-Be Rescuer](#3-case-9--confined-space-entry-and-would-be-rescuer)
4. [Case 10 — Isolation (LOTO) Failure on Conveyor](#4-case-10--isolation-loto-failure-on-conveyor)
5. [Case 11 — Yard Truck / Pedestrian Interface](#5-case-11--yard-truck--pedestrian-interface)
6. [Case 12 — Exertional Heat Illness, New Starter](#6-case-12--exertional-heat-illness-new-starter)
7. [How to Use These Cases](#7-how-to-use-these-cases)

---

## 1. How These Cases Are Built

The cases follow the scaffold of `case-studies-everyday.md`: Scenario,
What happened, Sequence of events, PEEPO summary, a four-column ICAM
analysis, Risk assessment on actual and potential consequence, Corrective
actions mapped to factors and control level, Lessons and Suggested training
use. Read `case-studies-everyday.md` §1 for why investigation depth scales
to potential, not actual, outcome. Three things differ in this set.

**Every potential is fatal.** Each case rates potential Consequence 5. The
outcome turned on racked stock breaking a fall, a passing vacuum-truck
driver with a blower, a co-worker two seconds from a pull-wire, a forklift
operator facing an open dock door, and paramedics' cooling. Investigate as
if the person had died.

**Each case carries Regulatory notes**, placed after the corrective
actions: notifiability, who notifies and who preserves the site, the
regulations that govern the task, and a jurisdiction table limited to
variations that change the answer. The model WHS Act and Regulations are
the default frame. Victoria (OHS Act 2004, OHS Regulations 2017) and NZ
(HSWA 2015) are called out in every case. Queensland, NSW and the ACT style
regulation provisions as sections but keep the model numbering. Volatile
facts carry an "as at" marker; penalties are in penalty units, with unit
values in `assets/penalty_units.json`.

**Every case has more than one PCBU at the workplace** — host and
contractor, labour hire provider, carrier, principal contractor, network
operator or building owner — and in each a control was lost at the
interface between them (model WHS Act s 46; Victoria has no general
equivalent, see Case 11).

### Risk-band legend

| Band | Meaning |
|---|---|
| **A** | Extreme / Critical |
| **B** | High |
| **C** | Moderate |
| **D** | Low |

Ratings use the canonical 5×5 matrix in `company.md` §3. The combinations
used below: Consequence 5 × Possible = **Critical (Band A)**;
4 × Likely = **Critical (Band A)**; 4 × Possible = High (Band B). Where a
case rates Likely, it states the exposure frequency that justifies it.

**These ratings are illustrative.** Re-derive any rating on your
organisation's matrix before relying on it; the bands, consequence
descriptors and likelihood anchors may differ (`company.md` §3).

---

## 2. Case 8 — Fall Through Fragile Roof

### Scenario
A solar installer carrying a panel across the roof of a 1994 distribution
warehouse in western Sydney stepped onto a weathered fibreglass rooflight
sheet, which broke. He fell 7.4 m to the warehouse floor and survived with
spinal and pelvic fractures. Perimeter edge protection was installed and
certified; nothing protected the roof surface itself. Notifiable incident;
actual Consequence 4, potential Consequence 5.

### What happened
The building owner's facilities management (FM) contractor engaged a solar
contractor to install a 99 kW rooftop photovoltaic (PV) system for
$186,000. The solar contractor designed the array and material paths from
aerial imagery and subcontracted the installation to a three-person crew.
The roof is 3° metal decking with a translucent fibreglass (GRP) rooflight
sheet every sixth run, weathered over 30 years to the grey of the steel and
hard to pick out from above in low morning light. From inside, the
rooflights are obvious bright strips in the ceiling. Nobody planning the
job looked at the roof from below.

The FM contractor's roof register, built from the 1994 as-built drawings,
recorded "metal deck — trafficable, safety mesh throughout". A 2009
tenancy fit-out had cut the mesh under rooflight run R7 for a duct riser;
the riser was later removed and the sheet refitted, but the mesh was
never reinstated and the drawings never updated.

The installation subcontractor's SWMS was its generic commercial-job
document: perimeter edge protection and, for rooflights, "keep off
skylights — walk the screw lines". The FM contractor issued a roof access
permit on the SWMS and the edge-protection handover certificate, answering
the fragile-surface question "No" from the register. On the second day on
site (Day 0 below), Installer A and a co-worker were carrying a 2.3 m,
30 kg panel from the crane-landed pallets to the array. Walking backwards,
Installer A stepped sideways around a rail offcut and onto R7.

### Sequence of events

| # | Time | Event |
|---|---|---|
| 1 | 2009 | Fit-out cuts safety mesh under rooflight run R7 for a duct riser; riser later removed, GRP sheet refitted, mesh not reinstated, as-builts not updated |
| 2 | 14 months prior | FM contractor mobilises; roof register populated from 1994 drawings; rooflights not recorded as a hazard |
| 3 | 6 weeks prior | Array and material paths designed from aerial imagery, crossing three rooflight runs; quote accepted through the minor-works purchase-order route |
| 4 | Day −3 | Generic SWMS submitted; roof access permit issued with the fragile-surface question answered from the register |
| 5 | Day −1 | Perimeter edge protection installed and certified; panel pallets crane-landed at the north end |
| 6 | Day 0, 06:45 | Pre-start; Take 5 records "skylights — keep off" |
| 7 | 07:50 | Installer A steps onto R7; sheet fractures; 7.4 m fall, partly broken by cartons on the top racking level |
| 8 | 07:52 | Tenant employee picking stock 4 m away calls 000; FM site manager stops roof work and closes the aisle |
| 9 | 08:25 | Installer A transported and admitted — L1 burst fracture, fractured pelvis and wrist |
| 10 | 08:40 | FM contractor phones SafeWork NSW after confirming neither the installation subcontractor nor the solar contractor has; roof and aisle preserved |
| 11 | 11:30 | Inspector attends; prohibition notice on all roof work until every rooflight is controlled |

### PEEPO summary
- **People** — Installer A: 3 years in solar, all on residential roofs;
  work-safely-at-heights unit current; first industrial roof with
  rooflights. Leading hand: licensed electrician, 40-plus commercial
  installs. FM permit issuer: 5 years in role; never viewed the roof.
- **Environment** — 7.4 m to a concrete slab; dew on the sheeting; low
  sun; GRP dust-filmed to match the metal; 22 rooflight sheets inside the
  array footprint; occupied warehouse below.
- **Equipment** — Perimeter guardrail certified. No rooflight covers,
  barriers, markings or panel trolleys; harnesses in the vehicle but no
  anchors in the design. Two-person carry, one carrier walking backwards.
- **Procedures** — Generic SWMS naming no workplace-specific hazard;
  permit form tested edge protection and anchors, not surfaces; no hold
  point for an underside inspection or roof survey.
- **Organisation** — Works under $250,000 ran as a minor-works purchase
  order with no construction review; roof register never field-validated;
  crew paid per kilowatt installed by the solar contractor; design done
  remotely; the crane booking fixed a three-day program.

### ICAM analysis

| Absent or Failed Defences | Individual / Team Actions | Task / Environmental Conditions | Organisational Factors |
|---|---|---|---|
| Rooflights in the work area not covered, barricaded or marked | Installer A walked backwards with a panel and stepped off the sheeting line onto R7 | Two-person panel carry forces one carrier to walk backwards with no view of foot placement | Sub-$250,000 works bypassed any construction or high risk construction work (HRCW) review gate at the FM contractor |
| Safety mesh under R7 cut away in 2009; integrity never verified by a competent person | Leading hand accepted "keep off skylights" as the control at pre-start | Weathered GRP visually indistinguishable from metal sheeting from above | Roof asset data taken from drawings, never validated in the field; fit-out changes not captured by the building owner |
| Roof register and permit recorded the roof as fully trafficable; no warning sign at the access point | Permit issuer answered the fragile-surface question from the register without viewing the roof | Array layout routed every panel carry across three rooflight runs | Solar contractor designs from imagery and pays the crew per kilowatt; subcontractor reuses a generic SWMS — no time or trigger for a roof survey |
| SWMS did not identify this roof's hazards; no hold point before first access | | Crane booking and a three-day program compressed set-up | Working-at-height critical control verification checked edges and anchors, never surfaces |

### Risk assessment
- **Actual**: Consequence 4 (permanent partial incapacity expected) ×
  Likelihood Possible — Risk B (High)
- **Potential**: Consequence 5 (single fatality) × Likelihood Possible —
  Risk A (Critical)
- **Classification note**: under definitions such as `company.md` §5,
  actual Consequence 4 makes this a critical incident and potential
  Consequence 5 a HiPo: it enters both the critical-incident response and
  the HiPo register. With a regulator investigation on foot, settle
  privilege before the ICAM (`investigation.md` §14)

Potential rationale: an unarrested 7.4 m fall onto concrete can credibly
be fatal. SafeWork NSW's release on a 23 August 2018 fatality at Tomago
describes a 19-year-old apprentice electrician on a commercial solar job
who fell about 7 m through plastic roof sheeting to a concrete slab. Here
racked stock decided the outcome, not a control; the tenant employee 4 m
from the landing point was also exposed.

### Corrective actions (mapped to factors)

| Action | Factor addressed | Control level |
|---|---|---|
| Re-design array, crane landing points and material routes (land panels at the array, use panel trolleys) so no carry or future maintenance corridor crosses a rooflight run | Task design — backwards carry across fragile sheets | Elimination (of the traverse) |
| Replace rooflight sheets inside the array footprint with metal sheeting; fit permanent covers or AS/NZS 4389:2015 mesh at every remaining rooflight; permanent trafficable walkway with handrails on the maintenance route | Absent defence — unprotected fragile surface | Substitution / Engineering |
| Until permanent works are complete: temporary covers designed for at least a 2 kN concentrated load, fixed against dislodgement and visibly distinct from the roofing — or total restraint that stops anyone reaching a rooflight — at every rooflight in the work area and on material routes, verified before the permit is issued | Absent defence; no hold point | Engineering (covers); work positioning (restraint) |
| Barricade and exclude the floor beneath active roof work and crane lifts | Occupied warehouse below | Isolation |
| Competent-person inspection of existing mesh and supports before it is relied on anywhere on the roof | Unverified mesh | Administrative (verifies an engineering control) |
| Field-validate the roof register across the portfolio: inspect from below, map rooflights, fragile sheeting and mesh condition; sign each roof access point | Asset data from drawings | Administrative |
| Building-owner management of change: any fit-out that alters mesh, rooflights or penetrations updates the roof register before handover | Fit-out changes not captured | Administrative |
| Route all roof work, whatever its value, through an HRCW gate: site-specific SWMS reviewed against the roof survey | Minor-works bypass | Administrative |
| Subcontract terms fund a pre-start roof survey and cover installation before crane day, and do not pay by the kilowatt alone | Per-kilowatt payment; compressed program | Administrative |
| Permit issuer must sight the underside or a current survey; fragile-surface question cannot be closed from the register | Permit design | Administrative |
| Extend working-at-height critical control verification to surface controls (covers, mesh, restraint, no-go marking) | Assurance gap | Administrative |

*Control-level note: covers are "fall prevention devices" (model WHS
Reg 79(5)) and rank first under Reg 79(3)(a). Total restraint that
physically stops anyone reaching a rooflight is a work positioning system
(Reg 79(3)(b); NSW roofs code s 4.6.1), a legitimate interim control while
covers are procured. Harness fall arrest ranks third (Reg 79(3)(c)), needs
engineered anchors and clearance (`hazards.md` §9), and is the only option
that brings Reg 80's tested rescue procedures. At Tomago, excessive slack
in the rope line between worker and anchor allowed the full fall.*

### Regulatory notes

| Question | Answer | Authority |
|---|---|---|
| Who owes the fall duty? | Installation subcontractor and solar contractor as PCBUs carrying out the work; FM contractor and building owner as persons with management or control of the workplace; arguably the array and fit-out designers. Each duty is held in full and must be coordinated | WHS Act ss 16, 19, 20, 22, 46 |
| Notifiable? | Yes — serious injury: immediate treatment as a hospital in-patient, and a spinal injury | ss 35–36 |
| Who notifies? | Every PCBU whose undertaking the incident arose from — installation subcontractor, solar contractor, FM contractor and, arguably, the building owner — must ensure it is done. One call is enough; assuming someone else made it is not | s 38; s 46 |
| When and how? | Immediately on becoming aware, by the fastest means — phone (SafeWork NSW 13 10 50) | s 38 |
| Scene | The person with management or control keeps the roof and landing area undisturbed, so far as reasonably practicable, until an inspector arrives or directs otherwise (NSW wording in the May 2026 roofs code). Assisting the injured, making the site safe and a police investigation are permitted | s 39 |
| Had he been caught by intact mesh? | Arguably still notifiable: a sheet failing under a person may be the "collapse or partial collapse of a structure", and fragments dropping into an occupied aisle the "fall or release from a height" of a thing, where either exposes someone to a serious risk. Notify when in doubt. The ACT makes a "serious fall" a dangerous incident in its own right (see below); the model WHS Act amendments published in December 2025 add a similar category, effective only where enacted — check the local Act (as at October 2026) | s 37 |
| SWMS retention | At least 2 years after a notifiable incident | Reg 303(2) |

Decision points (model WHS Regulations, numbering kept by the NSW WHS
Regulation 2025; model Code *Managing the risk of falls at workplaces*,
`legislation.md` §15):

- **Construction work?** Yes — installation altering a structure
  (Reg 289). The carve-out covers only "testing, maintenance or repair
  work of a minor nature", which a PV installation is not.
- **HRCW?** Yes — risk of a person falling more than 2 m (Reg 291),
  including through "a surface through which a person could fall"
  (Reg 78(2)(d)). The SWMS had to take account of "circumstances at the
  workplace" (Reg 299(3)); a generic one did not.
- **Solid construction reached?** No. Reg 78(3) puts work on the ground or
  solid construction first; uncovered rooflights fail Reg 78(5) (a surface
  that carries everyone, barriers at openings). Replacing the array-zone
  rooflights is the route there; until then Reg 79 applies, covers first.
- **Construction project?** No — under $250,000 (Reg 292): no principal
  contractor, WHSMP or Reg 301 copy. The SWMS duty (Reg 299) and the duty
  to stop work that departs from it (Reg 300(2)) apply at any value.

| Jurisdiction | Variation that changes the answer |
|---|---|
| NSW | Code of practice *Work on roofs – commercial and industrial buildings* commenced 22 May 2026 (as at October 2026), replacing the 2009 code: covers designed for a concentrated load of at least 2 kN (s 4.4); existing mesh inspected by a competent person before it is relied on (s 4.5); openings and no-go areas barricaded or controlled by restraint (s 5.3); adding PV changes the roof's use, so existing controls must be reviewed (s 5.2); keep people out of the area below roof work (s 3.3) |
| ACT | WHS Act 2011 (ACT) as amended by the Workplace Legislation Amendment Act 2025 (No 3), in force 19 November 2025: a "serious fall" — a person falling, or at risk of falling, from one level to a lower level — is a dangerous incident (s 37(1)(m)), so the intact-mesh case is notifiable; pelvic fracture is a listed serious injury (s 36(1)(b)(vi)); site preserved until released by an inspector, and evidence including electronic records and witness details preserved (s 39(1)); notifying PCBU and person with management or control must tell each other (s 39A) |
| QLD | WHS Regulation 2011 (Qld) ss 306C–306G (current as at 29 March 2026): non-housing construction work with a possible fall of at least 2 m, or on a roof sloping over 26°, needs controls that prevent a fall of any distance before work starts — edge protection, a fall protection cover or travel restraint; fall arrest only if prevention is not practicable (s 306D(3)); a cover must withstand a person falling onto it and be fixed against removal (s 306F); travel restraint inspected by a competent person at least every 6 months (s 306G(4)); "brittle roof" is a named example hazard (s 306C(3)) |
| VIC | OHS Regulations 2017 Part 3.3 applies to falls of more than 2 m (reg 41, reg 5); reg 43 names fragile surfaces; reg 44 orders passive fall prevention, work positioning (which includes travel restraint, reg 5), then fall arrest; HRCW reg 322, SWMS reg 327; principal-contractor duties from $350,000 (reg 332); written record to WorkSafe within 48 hours of notifying (OHS Act 2004 s 38) |
| SA | WHS Regulations 2012 (SA) reg 291: HRCW fall threshold lowered from 3 m to 2 m from 1 July 2026 (as at October 2026) — SWMS libraries and tender templates built on 3 m are out of date |
| NZ | No height threshold — WorkSafe's *Working at height in New Zealand* (August 2026) s 1.5 calls the "3-metre rule" dangerous and incorrect. The PCBU controlling the place of work gives WorkSafe at least 24 hours' notice of construction work with a fall risk of 5 m or more (particular hazardous work), except work from a ladder only, minor or routine maintenance and repair, overhead lines, and residential buildings up to two full storeys (s 6.1). A hospital admission is a notifiable injury (HSWA ss 23, 25) |

### Lessons
- Edge protection answers one of the fall pathways in Reg 78(2). A roof
  plan that shows only the perimeter has not assessed the surface — ask
  for the rooflight, penetration and mesh layer before any permit
- "Keep off the skylights" relied on hundreds of correct foot placements
  made walking backwards under load. Work-as-done made the error certain;
  the task design, not the installer, is the finding (`frameworks.md` §5)
- As-built drawings describe the building as handed over, not as it is.
  Mesh is a control only once a competent person has inspected it
- Contract value ($250,000, model WHS Reg 292; $350,000 in Victoria, OHS
  Regulations 2017 reg 332, `hazards.md` §4; as at October 2026) decides
  whether there must be a principal contractor. It never decided whether a
  SWMS was needed

### Suggested training use
Use with FM contract managers, permit issuers and procurement staff, not
only roof crews: the decisions that mattered were made at a desk weeks
earlier. Stop at sequence step 4 and ask what the permit issuer would have
seen by looking up from the warehouse floor. For investigators, it
separates a failed defence (no covers) from the organisational factor that
removed the chance to fit one (the minor-works route).

> Cross-reference: fall hierarchy, anchors and rescue in `hazards.md` §9;
> HRCW categories in `hazards.md` §8; notification triggers in
> `legislation.md` §5 and the phone script in `output-templates.md` §23;
> permit design in `inspections-audits-permits.md` §4; a bowtie for the
> same top event in `investigation.md` §13; contractor assurance in
> `whs-procurement.md` §5.

---

## 3. Case 9 — Confined Space Entry and Would-Be Rescuer

### Scenario
A fitter collapsed from hydrogen sulphide (H2S) at the bottom of a
4.5 m sewage pump station wet well, and the standby person started down
the ladder after him. Both survived; the entrant was admitted to
intensive care. Meridian Facilities Group (MFG), Asset & Infrastructure
Services, council water contract, regional Queensland. Actual Class 4,
potential double fatality.

### What happened
Fitter C and Trades Assistant D were sent to pump station SPS-17 to
clear a ragged pump and refit a level float — a "quick entry" the crews
did several times a month. The supervisor issued the entry permit at
the depot at 06:40 from a generic wet-well risk assessment written 14
months earlier for all 23 stations on the contract, and did not attend.

At the hatch, D held the four-gas detector in the opening: O2 20.9%,
H2S 0 ppm, LEL 0%, CO 0 ppm. The detector had no sample pump, had not
been bump tested for three weeks (the depot docking station was out of
service), and stayed on the hatch frame. C went down the fixed ladder in
a harness with no retrieval line. The tripod, winch and blower stayed on
the truck — rigging them took longer than the job.

SPS-17 receives a 1.8 km rising main from SPS-16. The council runs both
stations by telemetry, and nobody had asked it to inhibit the upstream
pumps. At 09:12 SPS-16 started on level; septic sewage entered the well
and the turbulence stripped H2S into the space. C called up that the
smell was bad and collapsed. D started down after him until E, a
vacuum-truck driver from the council's desludging contractor, shouted
him back. E then ran the blower into the hatch — unplanned, and probably
what kept C alive. The fire service measured 62 ppm H2S at 3 m depth
after 14 minutes of ventilation.

### Sequence of events

| # | Time | Event |
|---|---|---|
| 1 | ~14 months prior | Generic wet-well risk assessment issued for all 23 stations; inflow from upstream stations not addressed |
| 2 | ~3 weeks prior | Depot bump-test docking station fails; detectors signed out untested |
| 3 | 06:40 | Supervisor issues entry permit at the depot; "tripod and winch" ticked as the rescue method |
| 4 | 08:50 | Hatch opened; single gas test at hatch level reads clear; detector left on the hatch frame |
| 5 | 08:58 | C descends the fixed ladder; no retrieval line, no forced ventilation |
| 6 | 09:12 | SPS-16 starts; rising main discharges septic sewage into the well |
| 7 | 09:13 | C reports the smell, then collapses on the benching at 4.5 m |
| 8 | 09:14 | D gets no response and starts down the ladder |
| 9 | 09:15 | E arrives and shouts D back; D climbs out from ~2 m, vomiting and disoriented |
| 10 | 09:16 | E calls 000; blower running into the hatch by 09:19 |
| 11 | 09:31 | Fire service on scene; entry in SCBA; C recovered by their tripod at 09:44 |
| 12 | 09:50 | Regulator notified by phone; scene preserved; Crisis Management Team activated; PIIN issued within 12 hours |

### PEEPO summary
- **People** — C: 9 years on the contract, entry training current. D:
  14 months, classroom entry-and-standby course, never in a rescue
  drill. Supervisor: issues six to ten permits each morning, remotely.
- **Environment** — Wet well 4.5 m deep, 2.1 m diameter, 600 × 900 mm
  hatch, fixed ladder; septic inflow; still, warm morning.
- **Equipment** — One diffusion-mode detector, bump test overdue, no
  pumped sampling kit. No davit socket; tripod set-up on the sloping
  apron takes about 15 minutes.
- **Procedures** — MFG procedure requires isolation of connected plant,
  testing at top, middle and bottom, continuous monitoring, forced
  ventilation and an attached line. By local custom none of it applied
  to a "quick entry". Rescue plan: "winch retrieval; call 000".
- **Organisation** — 45 minutes per station including travel. Critical
  Control Verification (CCV) checked that permits were on file, not the
  set-up at the hatch. No rescue drill on the contract in two years.

### ICAM analysis

| Absent or Failed Defences | Individual / Team Actions | Task / Environmental Conditions | Organisational Factors |
|---|---|---|---|
| Upstream pumps not isolated; inflow entered an occupied space | Crew treated the task as a "quick entry" outside the procedure | Rising main delivers septic sewage; discharge turbulence releases H2S | Generic risk assessment for 23 stations never considered change in atmosphere during entry; no isolation arrangement agreed with the council as network operator |
| No forced ventilation | Gas test taken at the hatch only; detector not taken into the space | H2S is heavier than air and collects at the working level | Permits issued remotely by a supervisor who cannot see the controls |
| No continuous monitoring in the breathing zone; detector not bump tested | Entrant descended without a retrieval line | Rigging tripod and blower takes longer than the task | 45-minute job allowance makes full set-up unachievable |
| Retrieval line not attached; non-entry rescue impossible | Standby entered the space to attempt rescue | Standby alone at the hatch watching a colleague collapse | Rescue procedure never practised; standby given a prohibition but no action |
| No air-supplied respiratory equipment for a rescuer | | | CCV verified paperwork; docking station fault left open for three weeks |

### Risk assessment
- **Actual**: Consequence 4 (intensive care; LTI with extended
  recovery) × Likelihood Likely — Risk A (Critical)
- **Potential**: Consequence 5 (two fatalities) × Likelihood Possible
  — Risk A (Critical)

Likelihood: quick entries ran several times a month across 23 stations
with upstream pumps never inhibited, so inflow during an entry was
routine, not remote. Potential: both workers were in a toxic atmosphere
with no retrieval from outside, and survival turned on a third person
arriving by chance and improvising ventilation. A Critical rating means
no wet-well entry until interim controls reduce exposure
(`company.md` §3). Actual Class 4 also makes this an MFG Critical
Incident (`company.md` §5): immediate verbal notification to the BU WHS
Manager and BU General Manager, and ICAM by a trained lead investigator.

### Corrective actions (mapped to factors)

| Action | Factor addressed | Control level |
|---|---|---|
| Stop all wet-well entries on the contract until upstream isolation, forced ventilation, in-space monitoring and rigged retrieval are verified at the hatch | Critical rating — interim control before work resumes (MFG P1) | Administrative (interim) |
| Replace float switches with hatch-mounted level transmitters; fit guide-rail lift-out pumps so routine faults are cleared from the surface | Task required entry at all | Elimination |
| Agree an isolation protocol with the council: upstream and station pumps locked out at their switchboards (a telemetry inhibit alone is not an isolation), upstream storage and overflow managed for the entry, both recorded on the permit | Connected plant live; network controlled by another PCBU | Isolation |
| Fit davit sockets at all 23 hatches; retrieval line attached before the entrant leaves the surface — "no line, no entry" as a permit hold point | Non-entry rescue unavailable | Engineering |
| Forced ventilation before and throughout entry | Atmosphere not controlled | Engineering |
| Pumped-sample test at top, middle and bottom; personal monitor on each entrant plus an area monitor at the hatch; bump-test station and spare at each depot, no detector signed out untested | Atmosphere not monitored; detector assurance gap | Administrative (verification) |
| Permit issued at the hatch by a competent person who has sighted isolation, ventilation, gas readings and rigged retrieval against the go/no-go table below; "quick entry" category abolished | Remote permit issue; local custom | Administrative |
| Standby script drilled until automatic — alarm, winch, ventilate, hold the hatch; timed rescue drill for every crew six-monthly against MFG's target of the entrant at the surface within 3 minutes of the alarm | Standby had a prohibition but no action; procedures unpractised | Administrative |
| CCV re-scoped to field set-up at the hatch, sampled monthly by the Critical Risk Owner; job durations rebuilt to include set-up | Paper assurance; schedule pressure | Administrative |
| Air-supplied breathing apparatus held only by a trained rescue team; response pre-arranged with the local fire service where winch retrieval could fail | Entry rescue capability | Administrative / PPE |
| Medical follow-up for C and D after discharge; psychological support for D, and for E through his employer | Post-incident care | Administrative (recovery) |

### Regulatory notes

| Requirement | Model WHS Reg | Finding |
|---|---|---|
| Worker does not enter until Division 3 has been complied with, so far as is reasonably practicable. Entry is the head or upper body (at or above the shoulders) in the space or within its boundary (Reg 5), so leaning in to take a reading counts | 65 | "Quick entry" custom bypassed the Division on every entry |
| Written risk assessment by a competent person, having regard to any change in oxygen or contaminant concentration and the rescue procedures required | 66(2)–(4) | Generic; inflow not considered |
| Written entry permit completed by a competent person, stating the space, persons, period and controls drawn from the Reg 66 assessment | 67 | Issued remotely; listed controls not in place |
| System of work with continuous communication from outside the space, and monitoring of conditions within the space by a standby person in the vicinity | 69 | Not met: voice contact only; conditions in the space unmonitored with the detector left on the hatch frame |
| Eliminate, or else minimise, risk from any substance or condition introduced by connected plant or services | 70 | Upstream pumps live |
| Purging or ventilation so far as is reasonably practicable; safe oxygen level (19.5–23.5%, Reg 5) | 71 | Blower not used |
| Exposure standard not exceeded; air monitoring where there is uncertainty | 49, 50 | One test at the hatch. H2S WES 10 ppm TWA, 15 ppm STEL (as at October 2026) |
| Rescue procedures established, practised as necessary, and initiated from outside the space as soon as practicable | 74(1)–(2) | Unpractised; retrieval not rigged |
| Air-supplied respiratory equipment available to, and provided for, any worker entering to rescue where the atmosphere lacks a safe oxygen level, holds a harmful contaminant concentration, or could become so | 75(2) | None on the vehicle |
| Training for entrants, standby persons and their supervisors, including emergency procedures; records kept 2 years | 76 | Classroom only |
| Risk assessment and permit kept at least 2 years after a notifiable incident | 77(3) | Originals quarantined on day one |

Notifiable under WHS Act 2011 (Qld) s 35: both workers suffered a
serious injury or illness under s 36 — C by immediate in-patient
treatment (s 36(a)); D, discharged from the emergency department the
same day, by medical treatment within 48 hours of exposure to a
substance (s 36(c)), the limb most often missed. Notify by the fastest
means (s 38) and preserve the site (s 39; `legislation.md` §5). The
council and E's employer are PCBUs at the same workplace: consult,
cooperate and coordinate with both (s 46).

| Hatch go/no-go | Go only when | Out on, then ventilate and retest before re-entry |
|---|---|---|
| Atmosphere — pumped sample at top, middle and bottom (`hazards.md` §11) | O2 19.5–23.5%; flammables below 5% of LEL (Reg 72); H2S below the exposure standard, with alarm set-points and acceptance criteria reset to the H2S WEL before it replaces the WES on 1 December 2026, not after (`legislation.md` §14) | Any alarm, odour or symptom |
| Connected plant | Upstream and station pumps locked out and confirmed with the council | Any unplanned start or inflow |
| Communication and retrieval | Line attached, winch rigged, standby at the hatch with an area monitor | Loss of contact with the entrant |

| Jurisdiction | Instrument | Material difference |
|---|---|---|
| Cth, NSW, Qld, SA, Tas, ACT, NT, WA | WHS Regulations Part 4.3, regs 62–77 (Qld, NSW and ACT style them sections — this case falls under WHS Regulation 2011 (Qld) ss 62–77; WA WHS (General) Regulations 2022) | None material to this case |
| Vic | OHS Regulations 2017 Part 3.4, regs 50–73 (as at October 2026) | Definition (reg 5) adds a limb: limited or restricted entry or exit. No standby person by name — reg 65 requires continuous communication and emergency procedures that can be initiated from outside; the Compliance code *Confined spaces* (Edition 2, December 2019, para 149) gives a trained standby person as one way to comply. Permit reg 63; kept 2 years after a notifiable incident reg 64; rehearsal reg 69(4); air-supplied RPE for rescuers reg 70 |
| NZ | HSWA 2015 s 36 primary duty; no Part 4.3 equivalent | WorkSafe NZ accepts AS 2865 as the current state of knowledge on confined space entry. Notifiable event ss 23–25; preserve site s 55; notify s 56. The HSWA Amendment Act 2026 amends notification provisions from 1 April 2027 (as at October 2026; `legislation.md` §3) |
| AU and NZ | AS/NZS 2865:2009 *Confined spaces* (as at October 2026) | The practice benchmark throughout. Amendment 1, published 17 October 2025, made it a joint standard; older codes and `hazards.md` §11 cite AS 2865:2009 |

### Lessons
- The would-be rescuer is a design problem, not a discipline problem.
  "Never enter" holds only when the standby has something effective to
  do instead; a rigged line and winch turn the impulse to help into a
  rescue. MFG handled D's descent under its Fair and Just Culture
  Procedure as a predictable response to an unworkable plan
  (`frameworks.md` §5)
- A gas test at the hatch tests the hatch. H2S settles low and is
  released when liquid or sludge is disturbed; conditions here changed
  14 minutes into the entry
- Smell is not a warning system, and the clock is short. US OSHA puts
  loss of smell at about 100–150 ppm H2S, and knockdown within one or
  two breaths, with death within minutes, at 700–1,000 ppm. Recovery
  here took 31 minutes; C survived because a bystander had the blower
  running six minutes after he fell. Emergency services back up
  retrieval from outside; they are not the method
- Permits were on file for every entry, so paper assurance passed. Yet
  permit, gas test and standby are soft controls, and MFG's rule of one
  verified hard control before critical-risk work starts was unmet on
  every "quick entry" (`company.md` §4). Verify the control at the
  hatch (`frameworks.md` §7)

### Suggested training use
Run it as a stop-point exercise for entrants, standby persons and
permit issuers: pause at 09:13, ask each standby what they would do in
the next 60 seconds with the equipment actually rigged, then time a
real retrieval set-up at a hatch. For investigators it separates the
rescuer's act from the system that left no other act available; for
Critical Risk Owners it is CCV that measured documents, not controls.

> Cross-reference: confined space controls and thresholds in
> `hazards.md` §11; isolation in `hazards.md` §10 and Case 10 (§4
> below); permits in `inspections-audits-permits.md` §4 and
> `output-templates.md` §20; notification script in
> `output-templates.md` §23; legal privilege in `investigation.md` §14;
> fatality response and coroner in `investigation-advanced.md` §3;
> respiratory protection programs in `specialist-topics.md` §1.

---

## 4. Case 10 — Isolation (LOTO) Failure on Conveyor

### Scenario
A contract fitter clearing cardboard from the tail pulley of a baler
in-feed conveyor had his left forearm drawn into the in-running nip when
a host operator reset a tripped emergency stop and restarted the line.
Crush, degloving and fracture, admitted for surgery: a notifiable serious
injury with credible fatal potential. The conveyor was stopped on its
pull-wire E-stop and tagged, not locked. Retail distribution centre, Brisbane.

### What happened
An in-floor hopper feeds an inclined cleated belt conveyor (CV-02) into a
horizontal baler. The host PCBU owns and operates the line; a contractor
supplies fitters under a services agreement. A belt-drift alarm stopped
the feed; Operator B radioed for a fitter and left for the bale-out end.

Fitter A found cardboard compacted around the tail pulley. He pulled the
hopper-side pull-wire E-stop, hung his danger tag on the tail-end station,
lifted off the tail guard (a mesh panel missing two of four fixings) and
began cutting the build-up off the return belt. He did not lock out:
CV-02's only lockable isolator is 70 m away in the mezzanine switchroom,
behind a door the host supervisor keys, and the host's procedure classed
"blockage clears and adjustments under 10 minutes" as E-stop tasks.

Operator B came back to a full hopper and a tripped, untagged pull-wire
switch. Loaders brush the wire several times a week, so reset-and-restart
is routine. The tail pulley is out of sight of the switch and the
human–machine interface (HMI) screen, and the head-end start siren cannot
be heard at the tail over the baler power pack. Operator B reset the switch
and pressed AUTO START. Fitter A's glove, then forearm, went into the nip
between the return belt and the tail pulley. Operator C pulled the wire;
the belt stopped in two seconds.

The investigation found 41 tail-end clears in three months, none under
lock, and a hazard neither procedure named: under full lockout the loaded
belt ran back half a metre as the rest of the jam was cut out. With no
backstop, electrical isolation still left gravity energy at the pulley.

### Sequence of events

| # | Time | Event |
|---|---|---|
| 1 | ~3 years prior | Line commissioned; CV-02's only lockable isolator is at the motor control centre (MCC) in the mezzanine switchroom; tail pulley guarded by a bolt-on mesh panel, not interlocked |
| 2 | ~18 months prior | Host isolation procedure revised: clears and adjustments "under 10 minutes" carved out as operational tasks — E-stop only, no permit, no lock |
| 3 | ~4 months prior | Two of four tail-guard fixings reported missing on a pre-start sheet; not actioned — the panel now lifts off without a tool |
| 4 | Day 0, 15:31 | Belt-drift alarm; Operator B radios maintenance and leaves for the bale-out end without a handover |
| 5 | 15:38 | Fitter A pulls the pull-wire E-stop, tags the tail-end station, removes the guard, starts clearing; no lock, no try-start |
| 6 | 15:50 | Operator B returns; hopper backing up; pull-wire switch tripped, untagged; fitter not visible |
| 7 | 15:51 | Operator B resets the switch and presses AUTO START; belt runs; Fitter A's forearm drawn into the tail-pulley nip; Operator C pulls the wire |
| 8 | 15:53 | First aid; 000 called; supervisor locks CV-02 out at the MCC; belt clamped against run-back, then take-up tension released to free the arm (s 39(3)(a) and (c) permit action to assist an injured person and make the site safe) |
| 9 | 16:20 | Ambulance departs; host phones Workplace Health and Safety Queensland (WHSQ); contractor told and confirms the notification covers both PCBUs; line barricaded and preserved |
| 10 | Day 0, 18:00 | HMI event log (trip, reset and start, time-stamped) exported before the rolling buffer overwrites; isolator, tag and guard photographed in place |
| 11 | Day 1 | Inspector attends and releases the site; joint host–contractor ICAM commissioned |

### PEEPO summary
- **People** — Fitter A: trade-qualified, 4 years on site, current in
  the contractor's isolation procedure; had cleared the tail on the
  E-stop many times. Operator B: 14 months on the baler; trained to reset
  E-stops, never in isolation ("that's maintenance"). No impairment.
- **Environment** — Tail pulley behind a 1.8 m push-wall; no line of
  sight to the HMI (22 m) or the switch; baler power pack and loader noise.
- **Equipment** — No lockable isolator at the conveyor; guard removable by
  hand; start siren and beacon at the head end only; no backstop on a
  loaded incline; no return-belt plough, so cardboard reaches the tail.
- **Procedures** — Host: permit and lock for "maintenance", E-stop under
  10 minutes. Contractor: personal lock and try-start inside any guard.
  Agreement silent on which prevailed; no rule on who resets an E-stop.
- **Organisation** — Uptime and bale tonnage on the host's KPIs; response
  time on the contractor's. Isolation audits sampled permits, so never
  saw a carved-out task. Tail build-up was 41 jobs, never one defect.

### ICAM analysis

| Absent or Failed Defences | Individual / Team Actions | Task / Environmental Conditions | Organisational Factors |
|---|---|---|---|
| No lockable isolator within reach of the work; nearest is 70 m away behind a keyed door | Fitter relied on E-stop and tag; no personal lock, no try-start | Tail pulley out of sight of the HMI and the tripped switch | "Under 10 minutes" carve-out written into the host procedure — it codified the workaround; the model WHS Regs contain no minor-task exemption |
| E-stop used as the isolation — a control-circuit stop any person can reset | Operator reset a tripped E-stop without finding who tripped it or why | Nuisance trips from loader contact several times a week normalised reset-and-restart | Two PCBUs, two isolation procedures, never reconciled (WHS Act s 46) |
| Tail guard not interlocked and not secured; removable without tools; plant could restart with the guard off (Reg 208(2)(b)–(c), 208(3)(a) and (d), 208(5)(b)) | Operator restarted in AUTO without walking the line | Hopper backing up; production pressure at the restart decision | Isolation point location not specified at procurement or commissioning (Reg 204(1); Reg 210(1)(b); plant Code §3.1–3.2, Qld §4.1–4.2) |
| Start warning inaudible and not visible at the tail end (Reg 212; plant Code §4.4, Qld §5.4) | No handover between operator and fitter before the operator left | Clearing the tail is a frequent task — several times a week | Guard defect reported on a pre-start sheet with no closure loop |
| No backstop — loaded belt free to run back under gravity | Tag hung at the local station, not at the device that had been tripped | Job mixed a clear (no motion needed) with belt tracking (motion needed) | Assurance sampled permit paperwork, never observed the task; chronic build-up never escalated as a design problem |

### Risk assessment
- **Actual**: Consequence 4 (Major — LTI with extended recovery;
  permanent partial incapacity possible) × Likelihood Likely — Risk A
  (Critical). With 41 unlocked clears in a quarter, "Likely" is honest.
- **Potential**: Consequence 5 (single fatality) × Likelihood Possible —
  Risk A (Critical)

Potential rationale: a tail-pulley nip does not let go. An arm drawn in
to the shoulder, or clothing pulling the head and chest onto the pulley,
is credibly fatal. It stopped at the elbow because a third worker
reached the wire within two seconds: chance, not design.

### Corrective actions (mapped to factors)

| Action | Factor addressed | Control level |
|---|---|---|
| Fit a return-belt plough ahead of the tail pulley and seal the hopper skirting so less cardboard reaches the pulley | Task demand — the clear itself | Engineering (cuts clear frequency; clears still need isolation) |
| Install lockable switch-disconnectors in the power circuit at the tail and head of CV-02, labelled to match the MCC and drawings | No isolator at the point of work | Engineering |
| Replace the bolt-on tail guard with an interlocked guard with guard locking; move the tracking adjusters outside the guard line | Guard removable by hand; restart possible with guard off; tracking needs motion | Engineering |
| Fit a backstop to the drive; add "restrain or run the belt empty" to the isolation sequence | Stored gravity energy | Engineering / Administrative |
| Extend the start warning (siren, beacon, timed delay) to the full conveyor length; after any E-stop, enable AUTO START only once the tail-end station, in sight of the pulley, has been reset | Warning ineffective at the tail; restart from out of sight | Engineering |
| Protect or re-route the hopper-side pull-wire clear of the loader path; trend nuisance trips as a defect | Nuisance trips normalised reset-and-restart | Engineering |
| Withdraw the 10-minute carve-out. One isolation standard, named in the services agreement as prevailing: any body part past a guard line means personal lock at the isolator (lockbox and isolation register for group work), stored energy controlled, try-start; the host owns the isolation point and signs the hand-back before restart | Codified workaround; unreconciled procedures | Administrative |
| Restart rule: a tripped E-stop is reset only by the person who tripped it, or after a walk of the line and a positive all-clear | No restart ownership | Administrative |
| A pre-start defect on a guard, E-stop or isolator takes the plant out of service until a named owner closes it out; the site manager tracks close-out | Guard defect with no closure loop | Administrative |
| Verification observes live clears monthly; locks applied against guard-off jobs, and time to close guard defects, join both PCBUs' KPI sets beside uptime and response time | Assurance sampled paperwork; production and response-time KPIs | Administrative |
| Review every conveyor, baler and compactor across the portfolio for E-stop-as-isolation practice and isolator location | Pattern unlikely isolated to this line | Administrative |

### Regulatory notes
**Notifiability.** A serious injury under WHS Act 2011 (Qld) s 36(a)
(in-patient) and s 36(b)(v) (degloving): notify immediately by the
fastest possible means (s 38); keep the record at least 5 years
(s 38(7)). Each PCBU holds the s 38 duty; agree who phones and confirm.
The s 39 preservation duty sits with the person with management or
control of the workplace (the host) and covers the plant (s 39(2)): no
re-energising, guard refit or tag removal until an inspector arrives or
directs otherwise. With nobody hurt, an unexpected start-up is not
notifiable: s 37(g) covers failure or malfunction only of plant that
must be authorised (registered). Still a HiPo; investigate it the same way.

**Regulatory anchors (as at October 2026)**

| Jurisdiction | Guard removed for maintenance or cleaning | Lockable "off"; operating during maintenance | Notify and preserve |
|---|---|---|---|
| Model WHS Regs (text checked against WHS Regulation 2011 (Qld)) | Reg 208(5)(a) — guarding must be removable for maintenance and cleaning when the plant is not in normal operation; 208(5)(b) — if removed, SFAIRP no restart until replaced | Reg 210(1)(d); Reg 210(2) | WHS Act ss 35–39 |
| NSW | WHS Regulation 2025 — provisions are "sections"; the NSW plant code still cites 2017 "clauses", read as the corresponding sections | As above | WHS Act 2011 (NSW) ss 35–39 |
| VIC | OHS Regulations 2017 reg 99(6) — guarding may be removable for maintenance and cleaning when not in normal operation; no restart limb | reg 101(1)(d); reg 101(2) (no authorised-person alternative); reg 102(1) (multi-operator plant with more than one E-stop: restart only after manual reset and manual start) | OHS Act 2004 ss 37–39 |
| NZ | HSWA 2015 ss 36 and 38; WorkSafe NZ lockout guidance — PLCs, key-lockable E-stops and selector switches are not isolation on their own | As left | HSWA ss 23, 55–56 — current law until the HSWA Amendment Act 2026 commences (`legislation.md` §3) |

In Queensland the code is a floor: WHS Act 2011 (Qld) s 26A requires
compliance with it or a method giving an equivalent or higher standard.

### Lessons
- **A stop is not an isolation, and a tag is not a lock.** The E-stop met
  Reg 211 and worked as designed twice: once for the fitter, once on his
  arm. Code of Practice: Managing the risks of plant in the workplace
  §4.3 (Qld 2021 code §5.3) makes E-stops a back-up, not the only
  control. Under §4.5 (Qld §5.5) a tag should not be used alone to
  isolate; each worker has their own lock, tag and key, and the only
  duplicate is a master key kept secure for emergencies.
- **There is no quick-job exemption.** The model Regulations give two
  routes to access without isolation: guarding designed for it (an
  interlocked barrier that permits access only while the area presents no
  risk, Reg 208(2)(b), or presence-sensing, 208(2)(d)); or, where the
  plant must run, Reg 210(2): controls operable only by the person doing
  the work (or an authorised person where someone else must operate them,
  210(2)(b)(ii)), in a mode such as crawl or hold-to-run that eliminates
  or minimises the risk SFAIRP (210(2)(c)). A pull-wire E-stop meets
  neither. A jam clear needs no motion: isolate. Belt tracking needs
  motion: Reg 210(2) controls, from outside the guard line. Victoria's
  reg 101(2)(b) has no authorised-person option.
- **An interlock controls access; it does not isolate.** Guard locking
  can carry frequent access where the danger zone cannot be reached until
  motion and stored energy have stopped, but it can fail or be defeated:
  so not for work at a nip, on stored energy, or with a shared restart.
- **Lockout is not zero energy.** The Code's lock-out sequence (§4.5; Qld
  §5.5) ends with a try-start and warns that a failed restart does not
  prove stored energy has dissipated. Inclined belts, counterweight
  take-ups and baler rams need a restrain, block or bleed step.
- **Convenience is a design input.** When the lock costs a 15-minute
  round trip and the job is expected to take five, the E-stop wins every
  time. This "under 10 minutes" clear had run 13 minutes when the belt
  started: a time-based carve-out cannot be policed at the point of work.
  Put lockable isolators in sight of the work; design to AS/NZS
  4024.1603:2019 (identical to ISO 14118:2017, unexpected start-up) and
  AS/NZS 4024.3610:2015 (conveyors).
- **Restart is the second half of isolation.** Code §3.6 (Qld §4.6)
  expects a restart communication process with affected workers and
  other PCBUs after maintenance or cleaning. Nobody owned this restart.
- **Apply the substitution test before anyone mentions discipline:**
  would another competent fitter and operator, with the same information
  and pressures, have done the same? Forty-one prior clears say yes. (The
  test sits in Reason's culpability decision tree, `frameworks.md` §12.)
  This is drift (Rasmussen; Dekker) that the procedure then authorised.

| Device | What it does | Isolation? |
|---|---|---|
| E-stop, pull-wire | Stops motion through the control circuit; anyone can reset it | No |
| Guard interlock | Stops plant when a guard opens; safeguards routine access | No — a control function that can fail or be defeated |
| HMI "off", PLC state, key selector | Software or control-circuit state | No |
| Lockable isolator with a personal lock | Disconnects motive power; the key stays with the person at risk | Yes — once stored energy is controlled and a try-start fails |

### Suggested training use
Run it as a two-seat exercise: half the room takes the fitter's decision
at 15:38, half the operator's at 15:50, each with only what that person
knew. Most groups repeat both decisions, which is the point. For
investigators it calibrates work-as-done: the finding is the carve-out
and the isolator location, not the missing lock. Supervisors then walk
their plant asking: where is the lock point, and can I see the work?

> Cross-reference: isolation, lockboxes and stored energy in
> `hazards.md` §10; guarding and interlocks in `hazards.md` §16; permits
> in `inspections-audits-permits.md` §4 and `output-templates.md` §20;
> notification in `legislation.md` §5; isolation failure before a
> confined space entry in Case 9 (§3 above).

---

## 5. Case 11 — Yard Truck / Pedestrian Interface

### Scenario
A yard tractor reversing a semi-trailer onto a dock struck a visiting
linehaul driver crossing the apron on foot to hand in paperwork. The
trailer stopped with its rear wheels 0.4 m from his legs. Fractured
pelvis and wrist, admitted as an in-patient — notifiable, with credible
fatal potential. Three PCBUs: the site operator, the driver's carrier,
and the labour hire provider of the yard tractor driver. Grocery
distribution centre, northern Adelaide, 04:48, dark and raining.

### What happened
A third-party logistics provider (3PL, the host) runs the distribution
centre (DC) for a retail customer. When inbound volume outgrew the docks
two years earlier, it introduced "drop and shunt": linehaul drivers drop
trailers in staging lanes across the apron and a yard tractor shunts each
to a door. The receiving window stayed at the dock face, so every dropping
driver walks there: 260 m by the perimeter walkway, 70 m across the apron.

Driver D arrived at 03:05 for a 03:30 slot at a site running over an
hour late. He queued with the engine running, dropped in lane 6 at
04:35, unhooked, and set off across the apron at about 04:47 with
10 h 40 min worked against a 12-hour standard-hours limit. Shunt
Driver S (labour hire, three weeks on site) was reversing a loaded
trailer into door 14 on a blind-side arc, coupled air-only with no
electrical lead, as the crew did for yard moves: no trailer lights, no
alarm, and the tractor's alarm and beacon at the cab, 16 m from the
tail. The rear corner hit D at walking pace as he passed behind from the
near side; a forklift operator inside door 13 called "stop" on the radio.

CCTV for the previous night showed 64 driver crossings of the apron,
none on the walkway, and air-only coupling on nine of the eleven shunt
moves sampled. The carrier held another driver's near-miss report from
the same apron, five weeks old, never passed to the host.

### Sequence of events

| # | Time | Event |
|---|---|---|
| 1 | ~2 years prior | Drop and shunt introduced; receiving window left at the dock face; traffic management plan (TMP) still says "drivers remain in cab unless directed" |
| 2 | ~9 months prior | Yard KPI set as shunt moves per hour, pushed to a tablet in the tractor cab; air-only coupling becomes the norm |
| 3 | ~5 weeks prior | Carrier driver reports a near miss on the apron to the carrier's dispatcher; logged, not shared with the host |
| 4 | 3 weeks prior | S placed by the labour hire provider: HC licence sighted, 20-minute video induction, two buddy shifts; no assessed reversing drive; provider's last site visit 14 months earlier, by day |
| 5 | Day 0, 03:05 | D arrives for a 03:30 slot; queues on the entry road, engine running — work time under HVNL s 221 |
| 6 | 04:35–04:47 | Gate directs D to drop in lane 6 and walk his paperwork to the receiving window; D unhooks. Tablet task sends S from lane 9 to door 14, coupled air only |
| 7 | 04:48 | Trailer rear near-side corner strikes D mid-apron; forklift operator calls stop by radio; S stops with the rear wheels 0.4 m from D's legs |
| 8 | 04:50 | First aid; 000; shift manager stops every yard movement and holds inbound trucks at the gate |
| 9 | 05:20 | Ambulance leaves; strike area cordoned, tractor and trailer left in place. Host phones SafeWork SA without waiting for the admission to be confirmed and asks whether operations outside the cordon may resume (s 39(3)(e)), then tells the carrier and the provider; each records the notification reference. CCTV (72-hour overwrite), yard task log and tractor telematics exported |
| 10 | Day 1 | Inspector attends and releases the cordoned area; host-led ICAM with the carrier and provider on the team; carrier secures D's work diary and truck telematics |

### PEEPO summary
- **People** — D: 19 years linehaul, ninth visit, no impairment
  indicators. S: HC licence, first yard-shunt role; nobody had watched
  him do a blind-side reverse before he did them alone at night.
- **Environment** — Dark, light rain; building-mounted floodlights
  leave the staging side of a reversing trailer in its own shadow.
- **Equipment** — Alarm and beacon at the cab; mirrors lose the tail
  on a blind-side arc; no rear-view aid; trailer unlit and silent when
  coupled air-only. D in a day vest with no retroreflective tape.
- **Procedures** — TMP rule (stay in cab) contradicted by the process
  (walk to the window). Site rules sheet signed at the gate at 03:05.
- **Organisation** — Slots booked beyond dock capacity; moves-per-hour
  KPI; retailer's contract penalised carriers for missed slots. Three
  PCBUs, three incident systems, no interface meeting.

### ICAM analysis

| Absent or Failed Defences | Individual / Team Actions | Task / Environmental Conditions | Organisational Factors |
|---|---|---|---|
| No physical separation between walking drivers and the reversing apron | D took the direct line across the apron, as every driver on CCTV did | Dark, rain; trailer tail in shadow | Drop and shunt changed the yard's risk profile; the TMP was never re-assessed against it |
| Warning device at the cab only; it did not warn the person the trailer tail was about to reach (Reg 215(5)) | S reversed without sight of the trailer's rear path | Blind-side arc; 16 m of trailer between driver and hazard | Moves-per-hour KPI rewarded air-only coupling; no coupling standard |
| Trailer lights and alarm defeated by air-only coupling | S coupled air only, as the crew had for nine months | Task pushed to an in-cab tablet during the move | Labour hire placement not verified at the workplace; host induction generic; competence assumed from licence class |
| No rear-view aid for trailer moves (camera, radar, dock-mounted sensing) | Gate directed D to walk to the window — the process working as designed | D at 10 h 40 min, 65 minutes behind his slot, keen to unhook and rest | Slot overbooking and a late-slot penalty pushed time pressure onto drivers (HVNL s 26C) |
| Perimeter walkway existed on paper; 260 m against 70 m | | Walking drivers a constant: 64 crossings the night before | Near-miss report stayed in the carrier's system; no s 46 forum between the three PCBUs |

### Risk assessment
- **Actual**: Consequence 4 (extended-recovery LTI) × Likelihood
  Likely — Risk A (Critical); with 64 crossings a night, Likely is honest
- **Potential**: Consequence 5 (single fatality) × Likelihood
  Possible — Risk A (Critical)

Potential rationale: a person knocked down behind a loaded trailer can
go under the rear axle group even at walking pace. The 0.4 m margin
came from a forklift operator who happened to face an open dock door.
Critical stops the yard until interim controls cut the exposure
(`company.md` §3, P1): drivers held in a barricaded safe zone or in the
cab, paperwork by intercom or electronic proof of delivery, no trailer
movement while anyone is on foot on the apron, the electrical lead on
for every move, and a dedicated spotter clear of the trailer path — a
stopgap, not the fix.

### Corrective actions (mapped to factors)
Owner and priority in brackets: P1 before work resumes, P2 within
7 days, P3 within 30 days or an agreed milestone.

| Action | Factor addressed | Control level |
|---|---|---|
| Move check-in and paperwork to a gatehouse kiosk and electronic proof of delivery; door allocation sent to the cab. No driver has a reason to cross the apron (host with retailer; P3) | Process that put drivers on foot | Elimination (of the exposure) |
| Fenced walkway from the staging lanes to a driver safe zone with shelter, toilets and a view of the docks (host; P3) | No physical separation | Isolation / Engineering |
| Apron declared a pedestrian exclusion zone: barriers at the staging-lane ends, door-mounted traffic lights, shunt moves only on a clear signal (host; P2) | Shared reversing area | Engineering / Administrative |
| Rear sensing for every trailer move: dock-mounted camera or radar to an in-cab display, or a portable rear camera and light unit fitted at coupling (host; P3) | No view of the trailer's rear path | Engineering |
| Coupling standard: electrical lead connected for every move so trailer lights work; alarm and light at the trailer tail. Yard KPI changed from moves per hour to moves completed to the standard (host; lead P1, KPI P2) | Warning device not reaching the person at risk; KPI rewarding the shortcut | Engineering / Administrative |
| Light the staging side from poles opposite the docks; lock the cab tablet while the tractor is moving (host; P2) | Trailer tail in shadow; in-cab task push | Engineering |
| Book slots to measured dock capacity; report queue and dwell time; ask hours remaining at the gate and send drivers inside their last two hours to a priority door or rest bay; retailer removes late-slot penalties on carriers and drivers, in line with NHVR regulatory advice *Managing the risks of time slot bookings* (host and retailer; P3) | Time pressure pushed onto drivers | Administrative |
| Quarterly interface meeting — host, carriers, provider: shared near-miss reports, site rules issued with the booking, provider's labour hire licence confirmed, provider visits on night shift; assessed reversing drive before any shunt driver works alone, P1 for the current crew (all three; P2) | No s 46 mechanism; placement unverified | Administrative |
| Monthly night observation and CCTV count of apron crossings reported to site leadership; same review at every yard in the network (host; P3) | Assurance never looked at the yard at night | Administrative |

### Regulatory notes
**Notifiability.** Immediate in-patient treatment is a serious injury (model
WHS Act s 36(a)). Each PCBU from whose business the incident arose must ensure
the regulator is told immediately (s 38): host, carrier and, on a cautious
reading, provider. One call covers all three only if each confirms it and
keeps a record; a police attendance covers none. The host, with management or
control of the workplace, preserves the site (s 39); an inspector or the
regulator can permit other activity (s 39(3)(e)), so ask on the call. On the
pre-amendment model text a strike without serious injury is not a listed
dangerous incident. The model amendments published 5 December 2025 add a
"mobile plant incident" (mobile plant colliding with a person), list a
fractured pelvis as a serious injury, add a notifiable absence of 15 or more
consecutive days and extend preservation to electronic records and witness
details — only where enacted; check the local Act (as at October 2026). In NZ
a hospital admission is notifiable (HSWA ss 23(1)(b), 25): notify WorkSafe as
soon as possible by the fastest means (s 56) and preserve the site (s 55);
notification changes from 1 April 2027 (`legislation.md` §3). Triggers in
`legislation.md` §5; phone script in `output-templates.md` §23.

Duties are concurrent, non-transferable and cannot be contracted out
(WHS Act ss 14, 16, 272); each acts to its capacity to influence and control.

| Duty holder | Controls | WHS duty | HVNL role |
|---|---|---|---|
| Host (3PL) | Yard layout, lighting, TMP, slots, the yard tractor, direction of S | s 19 to S and to visiting drivers; s 20 workplace, entry and exit; Reg 40 layout and lighting; Regs 214–215 as the person with management or control of the tractor | Loading manager (premises unloading an average of at least 5 heavy vehicles a day, s 5) and unloader; consignee only if it actually receives the goods, not if it merely unloads |
| Retail customer | Delivery windows and the late-slot penalty | s 19 so far as it influences or directs the work; s 46 | Consignee if it has consented to being, and is, named as consignee in the transport documentation, or actually receives the goods (s 5) |
| Carrier | D's roster, instruction, what it knows about the sites it sends him to | s 19 to D wherever he works; Reg 39 instruction suited to the risks at that site; s 46 | Employer, operator, scheduler |
| Labour hire provider | Whom it places, into what task, with what verification | s 19 to S (in practice: inspect the host workplace and task before placement, after any change and on the shift worked); s 46; in SA, a licence under the Labour Hire Licensing Act 2017 (SA), which covers all industries from 29 January 2026 with licences required by 29 July 2026 (as at October 2026; `whs-procurement.md` §2) | None for D's vehicle |
| Officers of each | Resources, reporting, verification | s 27 due diligence | s 26D (executives of CoR parties) |

Jurisdiction differences (as at October 2026):

| Jurisdiction | Mobile plant and pedestrians | Shared duties and labour hire | Heavy vehicle law |
|---|---|---|---|
| Model WHS (Cth, Qld, SA, Tas, ACT, NT; NSW WHS Regulation 2025; WA WHS (General) Regulations 2022) | Regs 214, 215(4)–(5); Reg 40 layout and lighting. Safe Work Australia *General guide for workplace traffic management*; *Traffic management guide for warehousing* (April 2021: visiting drivers stand clear in a designated safety zone); model Code of Practice *Managing the risks of plant in the workplace* | WHS Act ss 14, 16, 19, 20, 46, 272 | HVNL as amended 1 August 2026 in Qld, NSW, Vic, SA, Tas, ACT; not WA or NT (`sector-regimes.md` §14) |
| Vic | OHS Regulations 2017 reg 109(1)(d) — eliminate or reduce collision risk so far as is reasonably practicable, with no absolute limb; reg 110 warning device where there is a "likelihood" of collision | OHS Act 2004 s 5A: a host is taken to be the employer of a labour hire worker (from 22 March 2022); s 35A: provider and host must consult, cooperate and coordinate. No general equivalent of model s 46 — carrier–host coordination rests on ss 21, 23 and 26. Notify and preserve ss 37–39 | HVNL applies |
| NZ | HSWA 2015 ss 36–37; WorkSafe *Managing work site traffic* (November 2020) and *Safe reversing and spotting practices* (March 2021) | HSWA s 34 (current text as at October 2026; s 34 is amended by the Health and Safety at Work Amendment Act 2026 from 1 April 2027 — `legislation.md` §3) | HVNL does not apply |

### Lessons
- **Count the walkers.** Where a process sends drivers on foot through
  a reversing area, the process is the hazard. Sixty-four crossings a
  night is a design output, not 64 violations — work-as-done
  (`frameworks.md` §4). Redesign the errand; do not re-brief drivers.
- **Reg 215(4) carries no SFAIRP qualifier.** The person with
  management or control of powered mobile plant "must ensure that the
  plant does not collide with pedestrians". Reg 215(5) requires a
  warning device that will warn persons who may be at risk from the
  plant's movement; a cab alarm 16 m from the tail does not reliably
  warn the person the trailer is about to reach. Put it at the tail.
- **Licence class is not yard competence.** No high risk work licence
  covers shunting. An HC licence proves on-road competence, not
  coupling discipline or a blind-side reverse in the dark (Reg 39).
- **A spotter is a late control.** WorkSafe NZ ranks it after
  eliminating reversing, dedicated reversing areas and visibility
  aids; never directly behind the vehicle, and the driver stops the
  moment anyone in the reversing area disappears from view.
- **The HVNL reaches the yard through the loading manager.** Transport
  activities include managing unloading, unloading and receiving goods
  from a heavy vehicle used on a road, and public safety includes the
  safety of drivers (HVNL s 5), so the host owes the s 26C primary duty
  for its receiving process alongside its WHS duties. The strike is
  notified under the WHS Act; whether a yard is a road or road-related
  area turns on public access (s 8). Queue time in the seat with the
  engine running is work (s 221); delays that push a driver towards his
  limit sit inside s 26C(2)(b). Section 26E bars asking, directing,
  requiring or contracting for anything the person knows or ought
  reasonably to know would cause a driver to speed, drive impaired by
  fatigue or unfit to drive, or breach work and rest hours.
- **"Their site, their rules" is not a defence.** The carrier knew the
  apron was dangerous, the provider knew S was new, the host knew
  about air-only coupling. Section 46 (outside Victoria) puts all three
  on one table.

### Suggested training use
Give the room the yard plan and one number — 64 crossings — and ask
for controls before revealing the injury. Groups that open with
hi-vis, signage and a driver briefing are the lesson: none of those
separates a driver from a trailer. For investigators: an ICAM that
stops at "S did not see D" misses the process that put D there. DC and
transport managers then walk their own yard at night, gate to window.

> Cross-reference: separation and spotters `hazards.md` §12; Chain of
> Responsibility `sector-regimes.md` §14; fatigue `hazards.md` §18;
> overlapping duties `legislation.md` §4; labour hire
> `whs-procurement.md` §2. Forklift version `case-studies-everyday.md` §2;
> another host-and-contractor mismatch in Case 10 (§4 above).

---

## 6. Case 12 — Exertional Heat Illness, New Starter

### Scenario
A 22-year-old labour-hire labourer collapsed with exertional heat stroke on
the third day of his first placement, hand-laying turf in full sun on a
subdivision west of Brisbane during a severe heatwave. He had moved from
Hobart two weeks earlier. Eleven days in hospital, four in intensive care,
with rhabdomyolysis and acute kidney injury; full duties after ten weeks.
Notifiable incident; actual Consequence 4, potential Consequence 5.

### What happened
The host, a landscaping subcontractor to a principal contractor, was nine
days behind after rain with handover fixed for the Friday. It rang a
labour hire agency for "two general labourers, Monday start". The agency's
job order recorded "landscaping labour, outdoors" and asked nothing about
workload, heat or how new starters would be eased in.

The two agency workers were paired with each other on the heaviest manual
task — barrowing topsoil and hand-laying turf rolls — 120 m from the
leading hand on the skid-steer loader. Turf cooks on the pallet in heat,
so each morning's delivery had to go down that day, and the crew worked
job-and-finish: knock off when the pallets are empty. Breaks shrank to
suit. The water cooler travelled on the leading hand's ute; the
air-conditioned crib room was 700 m away.

The host's heat procedure had one trigger: stop work at 38 °C. Supervisors
read a phone weather app reporting shade temperature at an airport 20 km
away. It peaked at 37.4 °C that week, so the procedure never activated. The
investigation put wet bulb globe temperature (WBGT) at the work front at
about 31 °C in the early afternoon. For continuous heavy work (about 400 W)
the NIOSH (2016) recommended limits are about 27 °C WBGT for acclimatised
workers and about 23 °C for unacclimatised workers, as 1-hour averages.

On day 3 Worker A had a headache from mid-morning and leg cramps by midday.
He told his co-worker, not the leading hand: "Third day. I didn't want the
agency hearing I couldn't hack it." When he began stumbling he was still
sweating heavily, which everyone present read as "only heat exhaustion".

### Sequence of events

| # | Time | Event |
|---|---|---|
| 1 | Thursday prior | Host requests two labourers; job order carries no task-demand or heat information |
| 2 | Day 1, 06:15 | 25-minute site induction; heat content is "drink plenty of water, tell your supervisor if unwell"; full shift on turf |
| 3 | Day 1, 16:30 | Agency consultant phones Worker A: "All good?" — "Yeah, hot." No further contact |
| 4 | Day 3, 05:40 | Overnight minimum 25 °C; heatwave warning current; four turf pallets delivered |
| 5 | 10:30 | Worker A has a headache; tells co-worker ("have a drink"); keeps working |
| 6 | 12:15 | Crib cut to 15 minutes at the ute; leg cramps |
| 7 | 13:40 | Stumbling, slow to answer; co-worker fetches the leading hand |
| 8 | 13:45 | Seated in the ute with air conditioning and sips of water; no 000 call, no active cooling |
| 9 | 14:05 | Vomits, becomes incoherent, then unresponsive |
| 10 | 14:07 | 000 called; shirt wet down with the last of the cooler water; no ice or tub on site |
| 11 | 14:28 | Paramedics arrive and begin active cooling; ambulance departs 14:45 |
| 12 | 15:10 | Core temperature 40.6 °C on arrival at the emergency department; admitted to ICU |
| 13 | 17:20 | Principal contractor's site manager phones WHSQ after finding neither the host nor the agency has |
| 14 | Day 4 | Co-worker discloses he was also unwell on day 3; agency, as employer, reports the injury to WorkCover Queensland |

### PEEPO summary
- **People** — Worker A: 22, fit, no medical conditions or medication; two
  weeks in Queensland; previous job indoor warehouse picking. Co-worker:
  agency placement, same start day. Leading hand: nine years with the
  host, first aid certificate current, taught that heat stroke means
  hot, dry skin.
- **Environment** — Day 3 of a severe-intensity heatwave; 37 °C in the
  shade, full sun, light wind, no shade on a new verge; warm nights in a
  share house without air conditioning, so no overnight recovery.
- **Equipment** — One 20 L cooler on a moving ute; no shade structure; no
  ice, tub or WBGT meter; long sleeves, long trousers and hard hat under
  the principal contractor's site rules.
- **Procedures** — Single air-temperature trigger; no work/rest regime
  tied to workload; no acclimatisation step for new starters; heat illness
  response was "rest in shade, give water, monitor", with no 000 trigger.
- **Organisation** — Job-and-finish; turf orders not linked to the
  forecast; agency–host consultation began and ended with the job order,
  and the agency had not visited a site of this host in 14 months; the
  principal contractor's WHS management plan (WHSMP) left heat for
  "subcontractors to manage"; no program float for heat days.

### ICAM analysis

| Absent or Failed Defences | Individual / Team Actions | Task / Environmental Conditions | Organisational Factors |
|---|---|---|---|
| No acclimatisation schedule — full shifts of heavy work from day 1 | Worker A worked on through headache and cramps without telling the leading hand | Heavy manual task in full sun at about 31 °C WBGT; third day of a heatwave with warm nights | Agency placed workers without asking about task demand, heat or new-starter arrangements; no site verification in 14 months |
| Heat trigger built on shade air temperature at a remote station; never activated | Leading hand treated confusion as heat exhaustion — 22 minutes of rest, air conditioning and water before 000 | Two new starters paired together, 120 m from supervision | Host's procedure was a stop temperature, not an assessment of workload, radiant load and acclimatisation |
| No means of rapid cooling at the work front; first aid training silent on immediate on-site cooling | Co-worker's response to early symptoms was "have a drink" | Water and shade remote from the work; clothing adds heat load | Job-and-finish and same-day turf deliveries rewarded skipped breaks; program had no allowance for heat |
| Buddy system nominal — neither buddy could recognise heat illness | | Insecure engagement: a new labour-hire worker has reasons not to report feeling unwell | Principal contractor's WHSMP left heat to subcontractors and verified nothing |

### Risk assessment
- **Actual**: Consequence 4 (LTI with extended recovery — ten weeks) ×
  Likelihood Possible — Risk B (High)
- **Potential**: Consequence 5 (single fatality) × Likelihood Possible —
  Risk A (Critical)
- **Classification note**: actual Consequence 4 makes this a critical
  incident, and potential Consequence 5 meets the HiPo definition
  (`company.md` §5); count it in HiPo trend data too. Log the co-worker's
  undisclosed illness as its own event, rated on potential.

Potential rationale: exertional heat stroke kills when cooling is delayed,
and survival tracks time to cooling; 27 minutes passed between the first
confusion and the 000 call. Queensland's WHS Prosecutor reports a
produce-picking operator fined $65,000 in the Townsville Magistrates Court
in October 2020 (WHS Act 2011 (Qld) ss 19, 32; no conviction recorded)
after a 27-year-old backpacker collapsed in the Burdekin on his fourth day
and died in hospital; the induction gave heat one line. US OSHA: almost
half of heat-related deaths occur on a worker's first day on the job or
first day back after a long absence, and over 70% in the first week.

### Corrective actions (mapped to factors)

| Action | Factor addressed | Control level |
|---|---|---|
| During a heatwave warning, lay turf from the earliest start the site approval and noise conditions allow until site WBGT reaches the heavy-work limit for the crew's acclimatisation status; no heavy manual task after that | Peak-heat exposure; same-day delivery pressure | Elimination (of peak exposure) |
| Mechanise topsoil and mulch placement (loader with spreader, powered barrows) | Metabolic load | Substitution |
| Portable shade and chilled water within 50 m of every work front; cooled rest area at the stage, not the compound | Remote water and shade | Engineering |
| Replace the 38 °C rule with a matrix on site-measured WBGT and workload anchored to NIOSH 2016: for heavy work (about 400 W), about 27 °C WBGT for acclimatised and about 23 °C for unacclimatised workers, as 1-hour averages; above those values the matrix's work/rest ratios apply or heavy work stops | Trigger that never activated | Administrative |
| Acclimatisation register: a new starter does no more than 20% of normal heat exposure on day 1, adding 20% a day; experienced workers back from a week or more away 50/60/80/100% over four days (NIOSH 2016). Worker A returns to heavy work in heat only on medical clearance, then on the new-starter schedule | No acclimatisation; return after heat stroke | Administrative |
| Never pair two new starters; buddy is a named acclimatised worker who checks in each break for the first two weeks | Nominal buddy system | Administrative |
| Before summer, every outdoor worker, not only first aiders, practises recognising heat illness and the heat stroke response. Kit at each work front in heat season: ice, 100 L tub or tarp, water; any confusion means 000 and cooling at once | No rapid cooling; misread signs; co-worker's illness unrecognised | Administrative (emergency response) |
| Tell every agency worker in writing at induction that they may stop unsafe work (WHS Act 2011 (Qld) s 84), that raising a heat concern or stopping is protected from discriminatory conduct (ss 104–106), and that the shift is paid; consult workers and HSRs on the heat plan (s 47) | Insecure engagement suppressed reporting | Administrative |
| Job order must state workload, heat exposure and the acclimatisation plan; host sights the agency's licence before engaging it (Labour Hire Licensing Act 2017 (Qld) ss 10–11); agency declines placement without the plan and makes task-specific contact on days 1–3 | Agency–host consultation | Administrative |
| Pay the full shift on heat-modified days; principal contractor carries heat days in the program and verifies subcontractor heat plans before summer | Production pressure; assurance gap | Administrative |

*Control-level note: cooling vests and lighter hi-vis rank last. They are
PPE (model WHS Reg 36(5)) and do nothing about workload or acclimatisation.*

### Regulatory notes

| Question | Answer | Authority |
|---|---|---|
| Notifiable? | Yes, on two limbs: immediate treatment as a hospital in-patient, and immediate treatment for loss of a bodily function (loss of consciousness; loss of function of an internal organ). Paramedic treatment counts as immediate treatment. Out-patient treatment in an emergency department does not meet the in-patient limb on its own, but immediate treatment for loss of consciousness still meets the bodily-function limb; only "mere fainting" is excluded | WHS Act 2011 (Qld) s 35, s 36(a) and (b)(vii) (unamended model text); SWA Incident Notification information sheet (November 2015) |
| Work-related? | Yes — the illness arose out of the work. A collapse unrelated to the work (the SWA example is a heart attack) is not notifiable | s 38(1) |
| Who notifies? | Agency, host and principal contractor each must ensure it is done; one call is enough. Each assumed another had called | s 38(1); s 46 |
| When? | Immediately after becoming aware, by the fastest possible means. The host knew at 14:05 that he was unconscious; each PCBU assumed another had called, and the regulator heard at 17:20, more than three hours later. Maximum 100 penalty units for an individual; a body corporate faces up to 500, because Penalties and Sentences Act 1992 (Qld) s 181B applies to the Qld Act (note to s 31). Unit value in `assets/penalty_units.json` (as at October 2026) | s 38(1)–(2) |
| Scene and records | The principal contractor, with management or control, preserves the site, which includes any thing associated with the incident: the cooler, the clothing, delivery dockets, the weather app record. Take a WBGT reading that day; the conditions are the evidence and they will not last. Keep the incident record five years | s 39; s 38(7) |

**Who owed what** (WHS Act and Regulation 2011 (Qld), which follow the model
numbering). Duties cannot be transferred (s 14), and no contract term can
exclude or limit them (s 272).

| Duty holder | Duty | Gap in this case |
|---|---|---|
| Labour hire agency | Primary duty to workers it "engaged, or caused to be engaged" (s 19(1)(a)): know the task and its hazards before placing, confirm the host's controls, stay in contact | Placed on a two-line job order; one generic phone call |
| Host | Primary duty to workers whose work it "influenced or directed" (s 19(1)(b)); an agency worker is the host's worker (s 7(1)(d)). Training suited to the work and its risks (Reg 39); work in extremes of heat without risk to health (Reg 40(f)); accessible drinking water (Reg 41); first aid and emergency plan matched to the hazards (Regs 42–43); PPE from the PCBU directing the work (Reg 44) | No acclimatisation, no usable trigger, no cooling capability |
| Principal contractor | Management or control of the workplace (s 20); WHSMP must set out the arrangements for consultation, cooperation and coordination between PCBUs and for managing incidents (Reg 309(2)) | Heat delegated, never verified |
| All three | Consult, cooperate and coordinate so far as is reasonably practicable (s 46). Safe Work Australia's labour hire guide expects agency and host to settle hazards, controls and incident roles before the placement starts | None took place |

| Jurisdiction | Variation that changes the answer (as at October 2026) |
|---|---|
| Model WHS | The model Regulations set no heat exposure limit or stop-work temperature (`hazards.md` §6); Reg 40(f) (extremes of heat or cold) carries the duty in the model-law jurisdictions |
| Model WHS, amended (published December 2025; not in the Qld Act at its 3 August 2026 reprint) | Serious injury or illness is tested on what the injury "would ordinarily require", whether or not treatment is available or sought (s 36). An absence of 15 or more consecutive days becomes notifiable within 14 days (ss 35A, 38(1)(b)) — Worker A's ten weeks would qualify — though one notification per event suffices (s 38(1A)). Evidence, including digital records and witness details, must be preserved (s 39). The notifying PCBU and the person with management or control must tell each other immediately (s 39A), the step missing here. Check each jurisdiction's adoption before relying on it |
| QLD | An approved code must be followed, or matched by an equal or higher standard (WHS Act 2011 (Qld) s 26A); for heat, that is the Managing the work environment and facilities Code of Practice 2021 |
| ACT | Approved Managing the Risks Associated with Extreme Temperatures Code of Practice (NI2025-607, made 6 November 2025 under WHS Act 2011 (ACT) s 274): PCBUs consult on and set stop-work conditions in a temperature management plan; for building and construction the stop-work threshold should consider forecast temperatures above 37 °C, and at 35–37 °C workers still likely to suffer heat stress move to an area unaffected by heat or, failing that, an air-conditioned site shed |
| VIC | A labour-hire worker is deemed the host's employee (OHS Act 2004 s 5A, applying to labour hire as defined in the Labour Hire Licensing Act 2018 (Vic)); provider and host must consult, cooperate and coordinate (s 35A). Notifiable under s 37(1)(c) or (d)(vii); the duty to notify sits with the employer having management and control of the workplace, with a written record within 48 hours (s 38) |
| NZ | Wider test: an illness that "requires, or would usually require" hospital admission (HSWA s 23(1)(b)). WorkSafe guidance treats fainting from heat at work that needs more than first aid as a notifiable loss of bodily function. Notify as soon as possible (s 56); overlapping PCBUs consult under s 34. Current law; the Health and Safety at Work Amendment Act 2026 revises the notification provisions from 1 April 2027, so recheck s 23 then (`legislation.md` §3) |

### Lessons
- A stop temperature is not a risk assessment. Airport shade temperature
  says nothing about radiant load, humidity or workload. Measure WBGT at
  the work front and set limits by workload and acclimatisation status
- Acclimatisation is a roster, and it needs an owner. Seven to fourteen
  days of graded exposure (`hazards.md` §6) happens only if someone writes
  the new starter's first fortnight into the plan. The agency asks for
  that plan; the host supplies it
- Sweating does not rule out heat stroke. In exertional heat stroke the
  skin is often still wet; the sign that matters is a change in mental
  state. Confused, clumsy or irritable in the heat means 000 and cooling
- Cool on site and call 000 at the same time; cooling never delays the
  call. ANZCOR Guideline 9.3.4: immerse from the neck down in the coldest
  water available for 15 minutes; failing that, wet the skin, apply ice
  packs to the groin, armpits, cheeks, palms and soles, and fan
  continuously. An air-conditioned cab is rest, not cooling
- Worker A's silence was rational for a casual whose next shift depended
  on the host's goodwill, and the leading hand applied what his training
  taught him. The findings are the job order, the trigger, the pairing and
  the payment arrangement (`frameworks.md` §5)

### Suggested training use
Run it before summer with supervisors and agency account managers in the
same room. Stop at sequence step 8 and ask what the group would do with
what is on the ute; most repeat the leading hand's response. Then have
agency and host complete a job order for this task in this forecast. For
investigators, the case shows a plausible individual finding ("failed to
report symptoms") dissolving once the terms of engagement are examined.

> Cross-reference: heat illness spectrum, WBGT and controls in `hazards.md`
> §6; notification triggers in `legislation.md` §5 and the phone script in
> `output-templates.md` §23; labour hire evaluation and licensing in
> `whs-procurement.md` §2; first aid and emergency planning in
> `workplace-controls.md` §1–§2; induction and training requirements in
> `legislation.md` §11; claim lifecycle in `compensation-rtw.md` §5.

---

## 7. How to Use These Cases

The methods in `case-studies-everyday.md` §9 apply unchanged: walk one case
progressively with "stop here, what would you do?", use the set for ICAM
calibration, cut a case down for a toolbox, and have new WHS staff re-rate
a case on the organisation's own matrix. What this set adds:

| Case | Critical risk | Control standard | Audience | Stop point |
|---|---|---|---|---|
| Case 8 (§2) | Fall through a fragile surface | `hazards.md` §9, §8 | FM contract managers, permit issuers, procurement | Sequence step 4: what would the permit issuer see from the warehouse floor? |
| Case 9 (§3) | Toxic atmosphere in a confined space | `hazards.md` §11 | Entrants, standby persons, permit issuers, Critical Risk Owners | 09:13: the standby's next 60 seconds with what is actually rigged |
| Case 10 (§4) | Unexpected start-up during a jam clear | `hazards.md` §10, §16 | Fitters, operators, supervisors, contractor managers | 15:38 and 15:50: the fitter's and the operator's decisions, two seats |
| Case 11 (§5) | Reversing heavy vehicle and a person on foot | `hazards.md` §12 | DC, yard and transport managers | Before the injury: 64 crossings a night — what controls? |
| Case 12 (§6) | Exertional heat illness | `hazards.md` §6 | Supervisors with labour hire account managers | Sequence step 8: what would you do with what is on the ute? |

### Notification drill
Every case has several PCBUs holding the notification duty. In Cases 8
and 12 each assumed another had called. Run the first hour of any case with
`output-templates.md` §23 open: who phones, how soon, what is preserved,
who tells whom, and who records the notification reference. Then run the
same case under Victorian and NZ law from its jurisdiction table.

### Critical control verification
In Cases 8, 9 and 10 assurance checked documents, not the control: edges
and anchors but never surfaces, permits on file, permit paperwork sampled.
In Case 11 nobody observed the yard at night; in Case 12 the principal
contractor verified no subcontractor's heat arrangements. Ask the Critical
Risk Owner what last month's verification actually observed at the point
of work (`frameworks.md` §7).

### Substitution test before discipline
Each case holds an individual act where a traditional investigation would
stop: the backwards step onto a rooflight, the standby's descent, the reset
E-stop, the direct walk across the apron, the unreported headache. Ask
whether another competent person, with the same information and pressures,
would have done the same (the substitution test, set out in Case 10's
Lessons; Reason's culpability decision tree in `frameworks.md` §12), then
trace each act to the design, contract or process that made it likely
(`frameworks.md` §5).

### Pairing across files
Pair Case 11 with Case 1 (`case-studies-everyday.md` §2): the same
separation logic, with a heavier vehicle, a visiting driver on foot and
three PCBUs sharing the yard. For organisation-specific framing, Case 9
shows how MFG's own rules — the Critical response, P1 priorities and the
hard control rule — change the response (`company.md` §3–§5).

---

> For everyday medium-severity cases and training method, load
> `case-studies-everyday.md`. For major catastrophes used in board papers
> and strategic training, load `case-studies.md`. For ICAM method and
> legal privilege, load `investigation.md`. For organisation-specific
> severity classification and risk matrix values, load `company.md`.

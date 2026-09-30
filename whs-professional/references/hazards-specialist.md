# Hazards Reference — Specialist Hazard Chapters

Specialist hazard chapters that carry their own regulatory regime, exposure
limit or certification chain: lead, diesel particulate, welding fume,
lithium-ion batteries, solar UV, abrasive blasting, formwork and falsework,
occupational diving, and Q fever and other zoonoses. Load the relevant section
when the task turns on one of these hazards; load `hazards.md` for the parent
topic (hazardous chemicals, hot work, confined space, height) and
`legislation.md` for the statutory provisions and the WES to WEL transition.

---

## Table of Contents
1. [Scope and Relationship to hazards.md](#1-scope-and-relationship-to-hazardsmd)
2. [Lead and Lead Risk Work](#2-lead-and-lead-risk-work)
3. [Diesel Particulate Matter](#3-diesel-particulate-matter)
4. [Welding Fume](#4-welding-fume)
5. [Lithium-ion Batteries](#5-lithium-ion-batteries)
6. [Solar UV Radiation](#6-solar-uv-radiation)
7. [Abrasive Blasting](#7-abrasive-blasting)
8. [Formwork and Falsework](#8-formwork-and-falsework)
9. [Occupational Diving](#9-occupational-diving)
10. [Q Fever and Zoonoses](#10-q-fever-and-zoonoses)

---

## 1. Scope and Relationship to hazards.md

`hazards.md` holds the high-risk hazards most coordinator-to-manager work
touches, with the general rule for each. This file holds hazards that need a
specialist regime on top of that rule: a dedicated Part of the Regulations
(lead, diving), a new or sharply lower exposure limit (DPM, welding fume), a
restricted-media table (blasting), a structural certification chain
(formwork), or a vaccination and notification regime (Q fever). Where both
files touch a topic, the general rule sits in `hazards.md` and the specialist
detail here. The hierarchy of control and SFAIRP (`frameworks.md` §1–§2) are
applied in each chapter, not restated.

Each chapter opens with its regulatory basis and closes with common failure
modes and practical implications for FM / contract portfolios. Read the
failure modes as system design problems (rosters, piece rates, procurement,
certification timing) before questions of individual compliance.

Four chapters (§2, §3, §4, §7) turn on exposure limits that move from the
SWA WES list to the WEL list on 1 December 2026 (`legislation.md` §14).
Values are stated as at October 2026; confirm them against the WEL list for
work from that date.

| Topic | General rule | Specialist detail here |
|---|---|---|
| Hazardous chemicals, health monitoring | `hazards.md` §13 | Lead Part 7.2 (§2); DPM (§3); welding fume (§4) |
| Exposure standards, WES to WEL | `legislation.md` §14 | §2, §3, §4, §7 |
| RCS, engineered stone, asbestos | `hazards.md` §1–§3 | Blasting silica-bearing, leaded or ACM surfaces (§7) |
| Construction, HRCW, SWMS | `hazards.md` §4, §8 | Formwork and falsework (§8); diving in construction (§9) |
| Working at height, scaffold licences | `hazards.md` §9 | Formwork decks, false decks, falsework licences (§8) |
| Hot work — fire, permit, arc eye | `hazards.md` §22 | Welding fume and gases (§4); artificial UV (§6) |
| Heat stress | `hazards.md` §6 | Solar UV, a separate hazard with its own trigger (§6) |
| Electrical, isolation, LOTO | `hazards.md` §10 | Chargers and EV high voltage (§5); UVC lamps in AHUs (§6); diver isolations (§9) |
| Confined space | `hazards.md` §11 | Shielding-gas pooling (§4); blasting inside vessels (§7) |
| Noise | `hazards.md` §14 | Blasting noise (§7); ototoxic welding constituents (§4) |
| Plant and pressure equipment | `hazards.md` §16 | Blast pots and receivers (§7); formwork components as plant (§8) |
| Emergency planning | `workplace-controls.md` §2 | Lithium-ion battery fire (§5) |
| Occupational hygiene practice | `specialist-topics.md` §1 | Sampling strategy for DPM (§3) and welding fume (§4) |
| Respiratory protection program, fit testing | `specialist-topics.md` §1 | Task RPE in §2, §3, §4, §7, §10 |
| Sector regimes | `sector-regimes.md` §2, §3, §10 | Mine DPM limits (§3); offshore diving (§9); agriculture zoonoses (§10) |

---

## 2. Lead and Lead Risk Work

### Regulatory basis
Model WHS Regs Part 7.2 (regs 392–418), applying on top of Part 7.1 (hazardous
chemicals — cross-ref `hazards.md` §13). Numbering is common across the
harmonised jurisdictions (NSW, QLD and ACT call them sections). Victoria: OHS
Regulations 2017 (Vic) Part 4.3 and WorkSafe Victoria's *Compliance Code: Lead*
(published 14 April 2022). SWA's *Health monitoring guide for lead (inorganic)*
is written for the supervising doctor. "Lead" means lead metal, lead alloys,
inorganic lead compounds and lead salts of organic acids (reg 5); organic lead
(tetraethyl lead in avgas) falls outside Part 7.2 and sits under Part 7.1.

### Two tiers — lead process, then lead risk work
| Tier | Reg | Meaning | Duties it adds |
|---|---|---|---|
| Lead process | 392–393 | 18 listed activities (paras (a)–(r)) plus any process the regulator declares under reg 393 (para (s)). SWA's July 2026 paper records uncertainty over whether the list is exhaustive; treat borderline tasks as lead processes | Information, containment and hygiene (regs 395–401); the reg 402 assessment |
| Lead risk work | 394 | Work in a lead process *likely* to push a worker's blood lead level (BLL) above the lead risk work value below | Notification, health monitoring and removal (regs 403–418) |

The reg 402 assessment weighs past biological monitoring, airborne lead, the
form of lead, tasks, duration, frequency and routes of exposure, and incident
history (reg 402(2)). Three rules drive the outcome:
1. **PPE is ignored** — reg 402(3) bars crediting respirators or coveralls.
2. **Doubt defaults up** — if the PCBU cannot tell, the process includes lead
   risk work until shown otherwise (reg 402(4)); let the reg 405 baseline and
   1-month BLLs of the first crew decide any step-down.
3. **The lower threshold is the default for women** — a "female of
   reproductive capacity" (FRC) is any female who has not provided information
   that she is not (reg 5). The PCBU does not decide and should not ask for
   proof.

### Blood lead triggers (all AU jurisdictions, as at October 2026)
| Trigger | Female of reproductive capacity | All other workers | Reg |
|---|---|---|---|
| Lead risk work — likely to exceed | 5 µg/dL (0.24 µmol/L) | 20 µg/dL (0.97 µmol/L) | 394 |
| Removal — at or above | 10 µg/dL (0.48 µmol/L) | 30 µg/dL (1.45 µmol/L) | 415 |
| Return — below, and doctor satisfied fit | 5 µg/dL (0.24 µmol/L) | 20 µg/dL (0.97 µmol/L) | 417 |
| Superseded values (define / remove / return), before the dates below | 10 / 20 (15 if pregnant or breastfeeding) / 10 µg/dL | 30 / 50 / 40 µg/dL | — |

### Health monitoring and test intervals (regs 405–414, 418)
| Element | Requirement | Reg |
|---|---|---|
| When | Before the worker first starts lead risk work, and 1 month after; work reclassified mid-job: as soon as practicable, then 1 month later | 405 |
| What | Demographic, medical and occupational history, physical examination and biological monitoring; venous or capillary blood through a NATA-accredited laboratory | Sch 14 Table 14.2 |
| Who | Registered medical practitioner with experience in health monitoring; worker consulted on the choice; PCBU pays | 408–409 |
| Reports | To the worker; to the regulator where the report shows the removal level, a work-related disease or a recommended remedial measure; to every other PCBU owing the duty, such as labour hire and host | 412–414 |
| Records | Confidential, kept at least 30 years; not disclosed without the worker's written consent, outside regs 412–414 | 418 |
| Public health | BLLs are also notifiable to health authorities, in some jurisdictions from 5 µg/dL (SWA, July 2026), so a public health unit may contact the worker directly | — |

| Last BLL (reg 407) | Female of reproductive capacity | All other workers |
|---|---|---|
| Below 5 µg/dL | 3 months | 6 months |
| 5 to below 10 µg/dL | 6 weeks | 6 months |
| 10 to below 20 µg/dL | removed | 3 months |
| 20 to below 30 µg/dL | removed | 6 weeks |
| Activity likely to significantly increase exposure (reg 407(2)) | Sooner | Sooner |
| Regulator determination by written notice (reg 407(3)–(5); reviewable) | As determined | As determined |

### Duties at a glance
| Duty | Reg | Trigger and detail |
|---|---|---|
| Information on health risks and toxic effects | 395 | Before engagement and before starting any lead process |
| Containment | 396 | Confine contamination to the lead process area SFAIRP |
| Cleaning | 397 | Methods that do not spread lead — H-class vacuum and wet wiping, never dry sweeping or compressed air |
| Eating area | 398 | No eating, drinking or smoking in the area; an eating area that cannot be contaminated |
| Change rooms, washing, showers, toilets | 399 | Contaminated clothing off, hands and face washed, before the eating area |
| Laundering and PPE | 400 | Sealed, labelled container; dispose, or launder at a laundry equipped for lead; no contaminated clothing goes home |
| Review of controls | 401 | On any removal, adverse health report, change, HSR request, and at least every 5 years |
| Removal | 415 | Immediately at the removal level, on the supervising doctor's recommendation, or on an indication that a control has failed and the BLL is *likely* to reach that level — act on a known failure without waiting for the next test; notify the regulator as soon as practicable |
| After removal | 413, 416, 417 | Medical examination within 7 days; report to the regulator; where return is expected, monitoring at the doctor's frequency; return only below the return level with the doctor satisfied |
| Notify lead risk work | 403–404 | Written notice to the regulator within 7 days of the determination, naming the lead process; copy accessible to workers and HSRs; notify changes |
| Restricted uses | 382, Sch 10 Table 10.3 | No abrasive blasting with media containing more than 0.1% lead; no lead carbonate in spray painting |

Part 7.2 is silent on pay during removal: settle non-lead duties and pay in
advance. Offences are per regulation. QLD (as at March 2026): ss 402(1), 405,
407 and 415(1) 60 PU; ss 403(1) and 415(2) 36 PU. VIC reg 195: 60 PU (natural
person), 300 PU (body corporate). Elsewhere, penalty units or fixed dollar
amounts — read the local provision; convert with `assets/penalty_units.json`.

### When the lower levels commenced — jurisdiction by jurisdiction
WHS ministers agreed the reductions in December 2016; SWA published the model
amendment in 2018; adoption took until 2025 (as at October 2026). Read
historical results against the superseded values: a BLL of 35 µg/dL required
removal in NSW in 2022 but not in Queensland or under Comcare.

| Jurisdiction | Instrument | Lower BLLs operative |
|---|---|---|
| VIC | OHS Amendment Regulations 2018 (S.R. No. 71/2018); two-year deferral in OHS Regs regs 193(2), 199(1A) | 5 June 2020 |
| ACT | WHS Amendment Regulation 2020 (No 1) (SL2020-27) | 3 August 2020 |
| TAS | WHS Amendment Regulations 2019 (S.R. 2019, No. 9); carried into the WHS Regulations 2022 | 1 January 2021 |
| NSW | WHS Regulation 2017 amended 1 July 2019; now WHS Regulation 2025 ss 394–417 | In force before 2022 |
| SA | WHS Regulations 2012 (SA) | In force before 2022 |
| NT | SL No. 22 of 2019; transitional period to 30 June 2021 (reg 394A) | 1 July 2021 |
| WA | WHS (General) Regulations 2022, from commencement | 31 March 2022 |
| QLD | WHS Amendment Regulation 2022 (SL 2022 No. 161) Pt 3 | 1 July 2023 |
| QLD mines and quarries | Mining and Quarrying Safety and Health (Lead) Amendment Regulation 2023 (SL 2023 No. 71) | 1 September 2023 |
| Cth | WHS Amendment (Blood Lead Level Exposure Values) Regulations 2025 | 25 March 2025 |

### 2026 review of Part 7.2 (status as at October 2026)
SWA consulted on *Protecting workers from exposure to lead* from 13 July to 24
August 2026. It is closed; any change needs advice to SWA Members, WHS
ministers' agreement and adoption in each jurisdiction, so the values above
remain the law. Each issue also has a guidance-only option (1(c), 2(c), 3(c)).

| Issue | Current | Option consulted on |
|---|---|---|
| Lead process definition | Listed activities (reg 392) | Keep the list as indicative and add a catch-all for any process that exposes, or is reasonably likely to expose, a person to lead (1(a)); or drop the list (1(b)) |
| Lead risk work (other workers) | 20 µg/dL | 10 µg/dL (2(a)), or health monitoring for all lead work (2(b)) |
| Follow-up test after starting | 1 month | Shorter; 2 weeks given as the example under 2(b) |
| Monitoring frequency (reg 407) | Table above | FRC: below 5 µg/dL 3 months, 5 to below 7.5 6 weeks. Others: below 10 µg/dL 3 months, 10 to below 15 6 weeks (3(a)) |
| Removal (FRC / others) | 10 / 30 µg/dL | 7.5 / 15 µg/dL (3(a)) |
| Return (FRC / others) | 5 / 20 µg/dL | 5 / 10 µg/dL (3(a)) |
| Action level (new) | None | 5 / 10 µg/dL — investigate and reduce exposure (3(b)) |

The options draw on NHMRC evidence of harm above 10 µg/dL, the 2020 ECHA RAC
opinion, EU Directive 2024/869 (removal at 30 µg/dL, 15 µg/dL for workers
other than FRC from January 2029; no EU level for FRC) and UK HSE proposals
for the Control of Lead at Work Regulations. Adopt the consulted action levels
as internal triggers now, and design controls so nobody nears 7.5 / 15 µg/dL.

### Airborne standard
WES for inorganic lead dusts and fumes (as Pb): 0.05 mg/m³ 8-hour TWA (as at
October 2026). From 1 December 2026 cite the lead entry in the SWA WEL list,
not the WES (cross-ref `legislation.md` §14). Reg 49 bars exposure above the
standard; reg 50 requires air monitoring where the PCBU is not certain on
reasonable grounds that it is met, or monitoring is needed to decide whether
there is a health risk. Air results alone do not predict BLL: ingestion via
hands, food and cigarettes is a major route, and bone lead re-enters the blood
for years (faster in pregnancy, breastfeeding and menopause).

### Victoria and New Zealand
| Jurisdiction | Position |
|---|---|
| VIC | OHS Regulations 2017 Part 4.3, same BLL values in employer and employee terms: lead process reg 178, lead-risk work reg 193, notice to WorkSafe within 7 days reg 195, monitoring frequency reg 198, removal reg 199(1A), return reg 201. A woman is treated as of reproductive capacity unless she gives a written statement to the contrary (reg 179). The separate 15 µg/dL removal level for pregnant or breastfeeding women ended on 5 June 2020; they now fall under the 10 µg/dL level |
| NZ — duties | No lead-specific regulations and no statutory removal level. HSWA 2015 s 36(3)(g) requires the PCBU to monitor worker health and workplace conditions. GRWM Regulations 2016 regs 29–30 attach to prescribed exposure standards (PES), and reg 31 health monitoring to substances a safe work instrument specifies |
| NZ — values | WorkSafe NZ *Workplace exposure standards and biological exposure indices*, 16th edition (July 2026), guidance values, not PES: WES-TWA 0.05 mg/m³; BEI 10 µg/dL (0.48 µmol/L) lead in blood for males and females not of reproductive capacity; biological reference value 3 µg/dL (0.14 µmol/L) for females of reproductive capacity, pregnant or breastfeeding, above which workplace exposure is to be investigated. A competent medical practitioner manages suspension and return. Do not import the Australian 20/30 µg/dL triggers |
| NZ — notification | Blood lead at or above 0.24 µmol/L (about 5 µg/dL) is notifiable to the medical officer of health under the Health Act 1956 (lowered from 0.48 µmol/L on 9 April 2021; as at October 2026), so a worker's result can prompt follow-up by health authorities (NZ framework: `legislation.md` §3) |

### Hierarchy of controls
| Level | Application |
|---|---|
| Elimination | Specify lead-free solder, ammunition, flashing and coatings; plan the job so intact lead paint is not disturbed |
| Substitution | Chemical stripping (dichloromethane-free product, assessed under Part 7.1) or wet scraping instead of dry power sanding; the sludge is still lead waste. Strip the cut line and cold-cut instead of oxy-cutting coated steel |
| Isolation | Defined lead process area; negative-pressure containment for blasting (cross-ref §7); enclosed, automated oxide and paste handling; separate clean and dirty change rooms |
| Engineering | LEV at the source; on-tool extraction to an H-class vacuum; wet methods; range ventilation moving air from the firing line downrange; melt temperature control |
| Administrative | Hygiene regime (regs 397–400), housekeeping schedule, air and BLL trend review, internal action level below the removal level |
| PPE | Respirator matched to the measured airborne level and fit-tested (cross-ref `specialist-topics.md` §1); coveralls and gloves that stay in the area. Last control, and excluded from the reg 402 assessment |

### Where it turns up
SWA's forthcoming 2026 Australian Worker Exposure Survey (cited July 2026):
3.8% of workers (about 571,000) probably exposed, 0.7% at or around the WES,
down from 6.1% in 2011–12; construction is highest at 19.9%.

| Industry or task | Reg 392 paragraph | Watch for |
|---|---|---|
| Lead-acid battery manufacture and recycling | (b), (c) | Oxide and paste dust; plate breaking |
| Smelting, foundries, lead pots, fire assay laboratories | (e), (f), (k), (n), (r) | Fume above 450°C; lead pots over 0.1 m² even at or below 450°C (n); dross and flue dust handling |
| Radiator repair | (j) | Small workshops with no monitoring history |
| Lead paint removal — bridges, tanks, heritage, demolition | (h), (i), (o) | Paint above 1% lead by dry weight; blasting, power tools, hot cutting (cross-ref §7, `hazards.md` §20, §22) |
| Indoor firing ranges | (q) | Range cleaning and bullet-trap maintenance, not only shooting |
| Explosives and detonator manufacture | (p) | Lead styphnate and azide dusts |
| Hand scraping or hand sanding of lead paint | Not listed — (h) and (o) reach only machine and power-tool methods | The primary duty and Part 7.1 still apply; the regulator can declare the process under reg 393 |
| Outdoor ranges, lead-containing waste (other than (o) paint-removal waste), laser ablation of lead from surfaces | Not listed — gaps named by SWA, July 2026 | As above. SWA also flags lead-lined cable removal as work where PCBUs miss the lead duties |
| Mining where lead is present in the ore | Not listed — SWA gap; thermal recovery of lead from ore is (f) | QLD mineral mines and quarries sit outside Part 7.2: Mining and Quarrying Safety and Health Regulation 2017 s 145I (lead risk job) and Sch 2E ss 24 (removal) and 26 (return), at the model values. Elsewhere, read the mines regulations alongside Part 7.2 |

### Common failure modes
- Respirators credited in the reg 402 assessment, so lead risk work is never
  identified, notified or monitored
- Mixed crew assessed against 20 µg/dL; at 5 µg/dL (the estimated Australian
  background) almost any lead process with measurable uptake is lead risk work
- Women excluded from lead jobs instead of the process being engineered to the
  lower threshold, inviting a claim under the Sex Discrimination Act 1984
  (Cth) ss 7 and 14 or state and territory anti-discrimination law (cross-ref
  `diversity-inclusion.md` §2)
- Short projects finished before the 1-month test; no exit BLL, so uptake is
  discovered by the next employer
- Rising BLLs treated as a hand-washing problem; reg 401 points the review at
  the process, facilities and controls, not the worker
- Capillary samples taken on site with lead-contaminated skin (false highs)
- Work clothes worn home; children of lead workers are the secondary casualties

### Practical implications for FM / contract portfolios
- Buildings painted before 1970, and any steel structure, tank or plant with
  original or unknown coatings (whatever its age): test the paint before any
  repaint, refurbishment or hot work scope is priced (AS/NZS 4361 series)
- Contractor prequalification for lead paint work: ask for the reg 402
  assessment (check it does not credit PPE), the reg 403 notification where
  lead risk work was identified, 12 months of de-identified BLL trends (reg
  418(2) consent covers identified results) and the laundering arrangement
- UPS and standby battery replacement is not a lead process while cells stay
  intact; breaking or dismantling them is (reg 392(c))

---

## 3. Diesel Particulate Matter

### Regulatory basis
Diesel engine emissions (DEE) are a hazardous chemical generated by the work:
model WHS Regs Part 3.1 and Part 7.1 apply, with reg 49 (no exposure above the
limit), reg 50 (air monitoring, records kept 30 years), reg 352 (review of
controls) and reg 368 (health monitoring). Victoria: OHS Regulations 2017 (Vic)
Part 4.1 (reg 165 exposure standard, reg 166 atmospheric monitoring, reg 169
health monitoring). Primary guidance is the SWA guide *Managing the risks of
exposure to diesel engine emissions in the workplace* (June 2026). General
exposure standard mechanics — cross-ref `legislation.md` §14.

IARC classified diesel engine exhaust as Group 1, carcinogenic to humans, in
2012 (Monograph 105): it causes lung cancer and is associated with bladder
cancer. Diesel particulate matter (DPM) is the soot fraction — more than 90%
of particles are below 1 µm — and its elemental carbon (EC) core is what gets
measured as the marker for the whole exhaust. SWA cites about 1.2 million
Australian workers exposed (2011 estimate) and around 130 work-related lung
cancers a year.

### Exposure limit — what applies where (as at October 2026)
| Setting | 8-hour TWA limit | Instrument | Status |
|---|---|---|---|
| All workplaces, including mines outside QLD, NSW and WA | None until 30 Nov 2026; **0.01 mg/m³ as respirable EC from 1 Dec 2026** | SWA *Workplace Exposure Limits for Airborne Contaminants* (WEL list), via model reg 49; Vic: OHS Regulations 2017 reg 165 and the reg 5 definition of exposure standard | First national DPM limit, on the WEL list approved by WHS ministers (SWA, May 2025). WorkSafe Victoria states the WEL list applies in Victoria from the same date (as at July 2026). Mines in VIC, SA, TAS and the NT have no mining-specific DPM value |
| NSW mines and petroleum sites | 0.1 mg/m³ as sub-micron EC | WHS (Mines and Petroleum Sites) Regulation 2022 (NSW) s 41(1)(b)(iii) | In force since 1 Feb 2021; personal monitoring under s 42. The Regulator is considering 0.05 for all underground mines and open-cut coal mines (Coal Services, November 2025); its website still cites 0.1 (October 2026). Whether the WEL also binds NSW mines from 1 Dec 2026 is unresolved |
| QLD mineral mines and quarries | No regulated limit; 0.1 mg/m³ sub-micron EC recommended | Mining and Quarrying Safety and Health Regulation 2017 (Qld) Sch 5 excludes DPM from the SWA-linked limits (SL 2023 No. 185); RSHQ guidance note QGN 21 | Sch 5 current as at 27 March 2026. RSHQ safety notice: shift-adjust the guideline value |
| QLD underground coal mines | No regulated limit; RSHQ guideline 0.1 mg/m³ sub-micron EC, shift-adjusted | Coal Mining Safety and Health Regulation 2017 (Qld) s 360A (safety and health management system must control exposure to internal combustion engine pollutants); Sch 6 lists gases and mists only | Current as at 1 Sept 2026. NSW industry slides (June 2025) cite 0.05 for Queensland coal, the value 0.1 becomes on a 12-hour shift under Brief and Scala; get the Coal Inspectorate's position in writing |
| WA mines | 0.1 mg/m³ as sub-micron EC | WorkSafe WA exposure standard for all WA mining operations, from 4 Dec 2020; guideline *Management of diesel emissions in Western Australian mining operations* (2013) | Whether the WEL displaces or sits beside it from 1 Dec 2026 is unresolved |
| Offshore petroleum (Cth) | 0.01 mg/m³ as respirable EC from 1 Dec 2026 | NOPSEMA advice to operators on the new WEL | Offshore facilities are not exempt from the transition |
| NZ | WES-TWA 0.1 mg/m³ as EC | WorkSafe NZ workplace exposure standards | Adopted 2016; no review scheduled |
| AIOH guidance (benchmark) | 0.1 mg/m³ sub-micron EC; action level 0.05 | AIOH position paper (2017) | The 0.1 value predates this edition (NSW MDG 29, 2008; WA guideline, 2013). Its basis is reduced eye and upper-airway irritation, not cancer risk |
| EU (benchmark) | 0.05 mg/m³ as EC | Directive (EU) 2019/130 | Extended to underground mining and tunnelling on 21 Feb 2026 |

Decision points:
- **Design to 0.01.** From 1 December 2026 it binds every workplace, mines in
  VIC, SA, TAS and the NT included. The exceptions are Queensland mines
  (carved out) and NSW and WA mines, where it turns on amendments not made as
  at October 2026: get the regulator's position in writing and design to 0.01
  regardless. SFAIRP still requires going lower where reasonably practicable.
- **Tunnel construction is not a mine.** Road, rail and utility tunnelling sits
  under the general WHS Regulations, so the WEL applies in full even where a
  nearby NSW or WA mine running the same plant still cites 0.1.
- **The two metrics are not interchangeable.** The WEL is respirable EC; the
  mining limits are sub-micron EC, a subset. A sub-micron result above 0.01 is
  an exceedance; one below it does not prove compliance.
- **Gases move on the same date, except NO2.** The WEL list cuts nitric oxide
  from 25 ppm to 2 ppm and carbon monoxide from 30 ppm to 20 ppm. NO2 carries
  over at its current WES (3 ppm TWA, 5 ppm STEL): in June 2026 WHS ministers
  did not agree new values for nine chemicals, NO2 among them. Queensland
  underground coal mines stay on CMSHR 2017 s 359 and Sch 6 (NO 25 ppm, CO
  30 ppm, as at September 2026). Elsewhere underground, the 2 ppm NO limit can
  govern ventilation quantity ahead of DPM.
- **Extended shifts.** Adjust the 8-hour TWA for 10- and 12-hour shifts
  (`legislation.md` §14); the Brief and Scala model halves it for 12 hours.

The size of the gap: Coal Services' 2024 NSW coal results (sub-micron EC, 567
underground workers sampled) show 4.8% above 0.1 mg/m³, 11.5% above 0.05 and
46.7% above 0.01. Every surface result was at or below 0.01. Longwall moves
are the worst task: 16.9% of 154 longwall-move samples exceeded 0.1.

### Where exposure occurs
| Setting | Typical sources | What drives the dose |
|---|---|---|
| Underground mining | Loaders, trucks, personnel carriers, drill rigs | Engines per ventilation split; dead-end headings; longwall moves and other non-routine work with plant density above design |
| Tunnelling | Excavators, loaders, shotcrete rigs, spoil trucks, locomotives | Distance from the ventilation duct outlet to the face; vehicles queuing in the drive |
| Vehicle and plant workshops | Engines run for diagnostics, brake and dyno testing | No tailpipe extraction; roller doors shut in winter |
| Warehouses and cold stores | Diesel forklifts, trucks idling at docks | Enclosed docks; chillers sealed against air change |
| Rail | Locomotive cabs, maintenance sheds, enclosed platforms, tunnels | Trailing locomotives; idling in sheds |
| Ports and shipping | Straddle carriers, terminal tractors, ro-ro decks, ship holds | Lashing and stevedoring beside running engines in vehicle holds |
| Construction and civil | Excavators in basements and shafts, generators, pumps, saws | Work below ground level; exhaust discharging into the work zone |
| Incidental | Traffic control, toll and drive-through booths, fire station bays, loading docks | Source outside the PCBU's control — the duty to minimise still applies |

### Monitoring — elemental carbon
- **Method**: personal full-shift sample in the breathing zone on a
  quartz-fibre filter; thermal-optical analysis to NIOSH Method 5040 at a
  NATA-accredited laboratory; result reported as EC.
- **Size selection**: respirable cyclone (AS 2985 sampler) at its design flow
  for the WEL. In coal mines NIOSH 5040 requires a cyclone plus sub-micron
  impactor, and flags the same need wherever other carbonaceous dust is
  airborne — otherwise it reads as diesel. The report must state the fraction
  sampled and how interference was handled.
- **Sensitivity**: a 960 L sample (8 hours at 2 L/min) has a working range
  from about 0.006 mg/m³ and a detection limit near 0.002, so half the WEL
  sits below the range. Raise sensitivity with a full-shift sample, a 25 mm
  filter or a cyclone designed for higher flow — never by turning up the pump
  on a cyclone or impactor, which shifts the size cut. Specify a laboratory
  reporting limit below 0.005 mg/m³ (WA mining data analysed in 2025 carried
  an LOD of 0.01). A two-hour task sample cannot demonstrate compliance.
- **Strategy**: sample by similar exposure group (SEG), include non-routine
  work (relocations, shutdowns, breakdowns), and measure NO2, NO and CO
  alongside, plus formaldehyde where the risk assessment points to it.
  Program designed by a hygienist (`specialist-topics.md` §1); NSW mines: the
  Regulator expects one independent of the mine.
- **Real-time EC instruments** find sources and test controls. They are not a
  compliance measurement.
- **Raw exhaust testing**: test each engine under load — hot engine and
  hydraulics, low gear, 70–80% revs (SWA guide); idle tests are not adequate
  (WA guideline). Set engine-specific pass/fail limits and TARPs, trend the
  results, and test hire plant at site entry. A rising trend flags a failing
  injector, turbo or filter months before personal monitoring would.
- **On a result**: SWA's guide gives a result above half the WEL as an example
  of a failing control, triggering review under reg 38(2)(a). Above the WEL,
  review is mandatory (reg 352(c)): investigate, fix, resample, tell the
  workers. NSW mines: a result above 0.1 mg/m³ sub-micron EC (s 41(1)(b)) is a
  notifiable high potential incident (s 124(5)(q)), via the Regulator Portal.

### Hierarchy of controls
| Level | Application |
|---|---|
| Elimination | Battery-electric or mains-powered plant: forklifts, underground loaders and light vehicles, grid or battery in place of generators. Keep engines out of enclosed spaces altogether. Battery plant brings charging and fire risk — cross-ref §5 |
| Substitution | Engines certified to US EPA Tier 4 Final or EU Stage V. Ultra-low-sulphur fuel kept free of contamination; low-sulphur lubricating oil. LPG or petrol plant removes DPM and substitutes carbon monoxide |
| Isolation | Sealed, pressurised, air-conditioned operator cabs with HEPA-filtered supply air (HEPA stops particulate, not NO2 or CO), specified to AS/NZS ISO 23875 and leak-tested at commissioning and on a schedule; positive-pressure control rooms, crib rooms and booths; segregated engine-run bays |
| Engineering | Wall-flow diesel particulate filter (DPF) — the only after-treatment that captures soot at high efficiency. Tailpipe local exhaust ventilation in workshops, interlocked to run whenever an engine does. Underground: ventilation matched to the engines in each split, parallel rather than series circuits, auxiliary duct kept up to the face |
| Administrative | Engine maintenance and emissions testing program; caps on engines per heading (tag boards); no-idle rules; scheduling relocations for maximum ventilation; operator training on loading and regeneration |
| PPE | P2 minimum, fit-tested. Where NO2 is elevated, a combined particulate and gas filter the manufacturer rates for nitrogen oxides. No air-purifying filter protects against carbon monoxide: where CO is elevated, fix the source or ventilation, or use supplied air. Powered air-purifying respirator for sustained particulate-only wear. An interim control, not the plan for meeting 0.01 — cross-ref `specialist-topics.md` §1 |

Four engineering points that decide whether the hierarchy works:
- **Tier 4 Final does not mean a DPF is fitted.** The US Tier 4 limits can be
  met without a filter. Stage V adds a particle-number limit (1×10¹² per kWh)
  on 19–560 kW engines that in practice requires a wall-flow filter. Specify
  the filter, not just the tier, in purchase and hire contracts.
- **Oxidation catalysts, EGR and SCR treat gases, not soot.** Catalysed
  systems can raise the NO2 fraction of the exhaust; check NO2 after any
  after-treatment retrofit.
- **Dilution alone will not reach 0.01.** Diesel ventilation is sized on
  engine power and gases, not particulate; WA's 2013 guideline calculated that
  holding 0.1 needs six to eight times the air most mines then supplied. At a
  tenth of that, source control (DPF, electrification) must carry the load.
- **A cab is only a control with the door shut.** SWA's silica guidance sets a
  usable benchmark: 50–200 Pa positive pressure (ISO 10263-4), a real-time
  pressure monitor with low-pressure alarm, and H13 or H14 HEPA filters on
  intake and recirculation. One open window voids the protection factor.

### Health monitoring
- Reg 368(a) requires health monitoring for a significant risk from a
  Schedule 14 chemical: polycyclic aromatic hydrocarbons (PAH, item 13) are
  present in DEE, and SWA's guide ties the DEE duty to them. Reg 368(b) adds
  any other DEE chemical posing a significant risk where a valid health or
  biological test exists.
- No biological exposure index exists for DPM or EC. Schedule 14 prescribes
  history, physical examination and exposure records for PAH, not a
  biological test; urinary 1-hydroxypyrene (`specialist-topics.md` §1) is
  confounded by smoking and diet — take occupational physician advice first.
- Workable surveillance is a baseline and periodic respiratory questionnaire
  and spirometry with smoking history, folded into the mine-worker health
  schemes where they apply — cross-ref `sector-regimes.md` §2.
- The record that matters is exposure. Lung cancer latency runs to decades;
  SEG-linked monitoring results kept for 30 years (reg 50) are the evidence
  base for both the worker and the PCBU.

### New Zealand
- WorkSafe NZ WES-TWA: 0.1 mg/m³ DPM as EC, with diesel exhaust noted as a
  confirmed carcinogen (as at October 2026) — ten times the Australian WEL.
- A WES is a guidance value, not a safe line. The duty is HSWA 2015 s 36 (so
  far as is reasonably practicable), and the Australian limit is evidence of
  what is known and achievable. Trans-Tasman operators: set one internal
  criterion of 0.01 mg/m³ respirable EC for both countries.
- Underground mining and tunnelling also fall under the Health and Safety at
  Work (Mining Operations and Quarrying Operations) Regulations 2016 —
  cross-ref `legislation.md` §3.

### Common failure modes
- Monitoring report compares sub-micron results to the respirable limit, or
  does not state the fraction at all
- Short task samples reported as compliant against an 8-hour limit; pump flow
  raised on a cyclone to chase the detection limit
- Hire and contractor fleet sits outside the emissions testing program
- DPF removed, gutted or bypassed after back-pressure alarms; regeneration
  failing on short duty cycles
- Diesel forklifts swapped for LPG indoors with no CO assessment
- Cartridge respirators issued where CO is the hazard; NO2 never measured
- Relocations, shutdowns and breakdown recovery never sampled
- RPE adopted as the standing answer to the December 2026 limit

### Practical implications for FM / contract portfolios
- Enclosed loading docks and basement car parks: no-idle rule in the site
  conditions for third-party carriers, enforced by the dock controller, and
  consultation with those carriers under WHS Act s 46
- Standby generators and diesel fire pumps: check where the exhaust discharges
  relative to air intakes and occupied areas before the routine test run
- Plant hire and fleet renewal: emissions tier, DPF and last tailpipe test
  result requested at quote stage
- Workshops without tailpipe extraction are the most likely non-mining
  exceedance of 0.01 — assess them before December 2026, not after

---

## 4. Welding Fume

### Regulatory basis
Model WHS Regs reg 49 (exposure limit not to be exceeded), reg 50 (air
monitoring), reg 368 (health monitoring), Part 7.2 (lead); NSW, QLD and the
ACT call them sections. SWA model Code of Practice *Welding processes* (s 3.1
airborne contaminants, s 3.6 gases, s 4.1 ventilation, ch 5 health
monitoring), approved in each model-law jurisdiction. Victoria: OHS
Regulations 2017 (Vic) regs 165–169. Fire, permit, electrical and
eye-protection controls are in `hazards.md` §22, not repeated here.

### Why this is a carcinogen program, not a nuisance-fume program
- **IARC Monograph 118** (evaluated 2017, published 2018) classifies **welding
  fumes** as Group 1: they cause lung cancer, with limited evidence for kidney
  cancer. **Ultraviolet radiation from welding** is also Group 1 (ocular
  melanoma). The classification covers all welding fume, mild steel included.
- Non-cancer outcomes: metal fume fever, asthma, COPD, greater susceptibility
  to pneumonia, and neurological effects from manganese.
- The old 5 mg/m³ limit was set against metal fume fever, not cancer. The
  1 mg/m³ limit is a ceiling: the duty is to minimise SFAIRP below it.

### Exposure limits (as at October 2026)
| SWA list entry | WES, to 30 November 2026 | WEL, from 1 December 2026 |
|---|---|---|
| Welding fumes (not otherwise classified) | 1 mg/m³ TWA (cut from 5, January 2024) | 1 mg/m³ TWA |
| Aluminium (welding fumes) (as Al) | 1 mg/m³ TWA (cut from 5; SWA list 17 November 2025) | 1 mg/m³ TWA |
| Manganese fume and compounds (as Mn) | 1 mg/m³ TWA; fume STEL 3 mg/m³ | 0.1 mg/m³ inhalable and 0.02 mg/m³ respirable TWA; OTO |
| Chromium (VI) compounds | 0.05 mg/m³ TWA | No WEL: listed as a non-threshold genotoxic carcinogen (NTGC), WEL list Appendix B |
| Nickel, metal (WEL: and insoluble compounds) | 1 mg/m³ TWA | 0.1 mg/m³ TWA |
| Cadmium and compounds | 0.01 mg/m³ TWA | 0.001 mg/m³ TWA; OTO |
| Beryllium and compounds | 0.002 mg/m³ TWA | 0.00002 mg/m³ TWA |
| Zinc oxide fume | 5 mg/m³ TWA; 10 mg/m³ STEL | 2 mg/m³ TWA; 10 mg/m³ STEL |
| Phosphine | 0.3 ppm TWA; 1 ppm STEL | 0.05 ppm TWA; 0.15 ppm peak |
| Carbon monoxide | 30 ppm TWA | 20 ppm TWA; OTO |
| Carbon dioxide | 5,000 ppm TWA; 30,000 ppm STEL | Unchanged |
| Nitrogen dioxide | 3 ppm TWA; 5 ppm STEL | Unchanged: a lower value was not agreed by a majority of WHS ministers (SWA, 24 June 2026) |
| Ozone | 0.1 ppm peak | Unchanged; a peak limit cannot be shift-adjusted |

- **Two tests, both mandatory.** Total fume under 1 mg/m³ *and* every
  constituent under its own limit (Code s 3.1). To 30 November a stainless job
  can pass on fume and fail on Cr(VI). From 1 December respirable Mn is 1/50
  of the fume limit: fume over 2% manganese can pass on fume and fail on Mn.
- **Cr(VI) loses its pass mark.** From 1 December 2026 NTGCs have no limit:
  eliminate, substitute or minimise SFAIRP (WEL list s 2.4). Any measurable
  result is a prompt to improve process, consumable and on-torch extraction.
- **Commencement differs by jurisdiction.** The general cut applied from
  18 January 2024 in SA and NT and 1 October 2024 in the ACT; the aluminium cut
  in the ACT from 9 September 2026. Check dates for 2024–2026 assessments.
- **WEL transition.** From 1 December 2026 the WEL list replaces the WES list
  in every jurisdiction, Victoria included. Design to WEL values now
  (`legislation.md` §14); recheck hygiene reports written to WES values.

The size of the gap: WA's mines regulator (then DMIRS, Mines Safety Bulletin
No. 154, 24 August 2018) found about 12% of welding fume samples over
5 mg/m³, steady for 25 years. Against 1 mg/m³, WorkSafe WA found about
two-thirds of 2024–2025 samples over, most with a respirator in use (Health
and Safety Bulletin No. 26 (HSB 26), 25 June 2026). Assume an unmeasured shop
is over.

### Constituents and gases — what the job tells you
| Contaminant | Where it comes from | Why it matters |
|---|---|---|
| Hexavalent chromium, nickel | Stainless and high-alloy steels, their consumables, hardfacing, plated steel | Lung carcinogens; skin and respiratory sensitisation |
| Manganese | Most steel welding; highest with high-tensile steels and hardfacing consumables | Central nervous system effects (manganism); ototoxic |
| Zinc oxide | Galvanised steel | Metal fume fever |
| Cadmium, beryllium, lead | Plated parts, copper and aluminium alloys, leaded paint and primers | Kidney and lung damage; lead paint makes it a lead process (§2) |
| Fluorides | Electrode coatings and fluxes | Respiratory irritation; bone effects with long exposure |
| Ozone | Arc UV acting on air; worst with plasma, MIG and TIG | Lung irritant at very low levels; passes straight through particulate filters |
| Nitrogen oxides, carbon monoxide | Formed in the arc | NOx: fluid on the lungs at high concentrations, chronic lung damage. CO is also ototoxic |
| Phosphine | Steel coated with rust-proofing compound | Irritant; lung and organ damage. Identify the coating first |
| Argon, helium, nitrogen, CO2 | Shielding and purge gases | Displace oxygen with no warning. CO2 is also toxic in its own right (limits above) |
| UV from the arc (not a fume, same program) | Every arc process; reflects off bright surfaces | Group 1 (ocular melanoma), arc eye, skin burns. Screens and curtains to AS/NZS ISO 25980:2024 (replaced AS/NZS 3957:2014, which the Code still cites), skin covered, bystanders out of line of sight (`hazards.md` §22; solar dose for outdoor welders: §6) |

**Shielding-gas asphyxiation.** Argon and CO2 are heavier than air and pool
in tank bottoms, pits and vessel ends; an argon back-purge fills the space
behind the weld. No work below 19.5% oxygen or above 23% (Code s 3.6). Where
the space meets the reg 5 confined space definition, Part 4.3 applies
(`hazards.md` §11). Filtering respirators, PAPR included, supply no oxygen.

### Hierarchy of controls
| Level | Application |
|---|---|
| Elimination | Design out the weld: mechanical fastening, forming, bought-in sections. Prefabricate in an extracted shop instead of welding in situ |
| Substitution | Lower-fume process or consumable (TIG in place of stick or flux-cored where the job allows). Arc air gouging and stick welding are the high-fume tasks. Strip paint, galvanising, oil and coatings back from the weld zone first |
| Isolation | Welding bays or booths away from other trades; robotic or mechanised welding in an extracted enclosure |
| Engineering | On-torch extraction; movable-hood LEV; downdraught or side-draught benches; extracted booths |
| Administrative | Head out of the plume; high-fume tasks scheduled at low occupancy; LEV pre-use checks and maintenance. Do not use rotation to manage a carcinogen: it cuts individual dose by exposing more people |
| PPE | PAPR welding helmet with P3 filter, as a supplement to extraction |

### Choosing the ventilation control
| Situation | Control that works | Watch for |
|---|---|---|
| Production MIG or flux-cored at fixed stations | On-torch extraction | Captures at the arc and moves with it; set up so shielding gas and weld quality are not disturbed, then maintain it |
| Small work at a bench | Downdraught or side-draught bench | Large flat workpieces blank off the airflow |
| Large or varied fabrication | Movable hood on a flexible arm | Effective only close to the arc; must be repositioned as the weld advances |
| Maintenance and site welding in situ | Portable extraction unit plus PAPR | Usually the least controlled welding in the business |
| Outdoors | PAPR | Wind is not a control and can push the plume into the helmet |

- **Design figures (Code s 4.1).** Minimum capture velocity 0.5 m/s at the
  fume source, away from the welder. No recirculation into the workroom;
  discharge outside, clear of air intakes and breathing-air compressors.
- **General ventilation is not the control.** The Code allows forced dilution
  only for minor, low-toxicity emissions and natural ventilation for comfort
  only; roof fans and a roller door do not control a carcinogen. UK HSE alert
  STSU1-2019: LEV for all indoor welding, RPE outdoors, any duration.

### Respiratory protection
- **Default: PAPR welding helmet with P3 filter.** No face seal, so it suits
  facial hair; more comfortable, so more reliably worn. AS/NZS 1715:2009 rates
  a P3 PAPR with any head covering up to a protection factor of 50.
- **Tight-fitting respirator under a helmet**: fit-tested, clean-shaven,
  compatible with the helmet. WorkSafe WA expects a protection factor of 50
  from non-powered respirators (HSB 26), but AS/NZS 1715:2009 rates a half
  facepiece up to 10 even with P3; 50 takes a full facepiece. Half-face and
  disposable respirators are a stop-gap for low measured exposures only.
- **P2 and P3 filters do not stop ozone or nitrogen oxides.** Where gases
  drive the risk, the hygienist specifies the filter or supplied air.
- Select to AS/NZS 1715:2009, buy to AS/NZS 1716:2012; both run alongside the
  adopted ISO-based suite until 2030 (as at October 2026). Program elements
  and RESP-FIT fit testing: `specialist-topics.md` §1.

### Air monitoring
- **Trigger (reg 50).** Monitor when the PCBU is not certain on reasonable
  grounds whether a limit is exceeded, or to determine whether there is a risk
  to health. On the WA figures, a shop with no data cannot claim certainty.
- **Method.** Personal sampling in the breathing zone, inside the helmet, by
  an occupational hygienist, to AS 3853.1 (particles) and AS 3853.2 (gases).
  WEL particulate limits apply to the inhalable fraction unless marked
  respirable (WEL list s 3.2): sample both, analyse metals matched to parent
  metal and consumable SDS (Mn always), include bystanders (Code s 3.1).
- **Reporting.** Report the unprotected result first. RPE counts towards
  reg 49 compliance only once every reasonably practicable higher-order
  control is in place and the RPE is worn correctly (SWA WES document s 2.5,
  amended 18 January 2024): PAPR used instead of reasonably practicable
  on-torch extraction cannot be credited.
- **Extended shifts.** Adjust the TWA where the day exceeds 8 hours, the week
  40 hours, or the break between shifts is under 16 hours (WEL list s 3.1);
  never STEL or peak. Brief and Scala halves it for a 12-hour day: 0.5 mg/m³
  fume, 0.01 mg/m³ respirable Mn (`legislation.md` §14).
- **Records** kept 30 years, accessible to exposed workers (reg 50).
  Re-monitor after any change to process, consumable, extraction or layout.

### Health monitoring
- **Schedule 14, Table 14.1 (reg 368).** Mandatory where ongoing work creates
  a significant risk from cadmium (item 4: urinary cadmium, respiratory
  function) or chromium (inorganic) (item 5: weekly skin inspection of hands
  and forearms by a competent person). Reports kept 30 years (reg 378). The
  duty survives Cr(VI) losing its WEL (WEL list Appendix B).
- **Lead.** Welding or cutting leaded paint is a lead process (reg 392); for
  lead risk work (reg 394), monitoring before starting and one month after
  (regs 405–407; §2).
- **Welding fume generally.** reg 368 also applies where there is significant
  risk and valid techniques exist to detect effects: respiratory questionnaire
  and spirometry at baseline, then periodically (WorkSafe NZ: annually).
- **Hearing.** The Code flags manganese, lead and CO as ototoxic; the WEL list
  gives manganese, cadmium, lead and CO an OTO notation. Put noise-exposed
  welders into audiometry (`hazards.md` §14; ototoxic substances and the OTO notation, `specialist-topics.md` §1).

### Jurisdiction variations (as at October 2026)
| Jurisdiction | Position |
|---|---|
| Model-law jurisdictions | Regs 49, 50 and 368; the NSW WHS Regulation 2025 keeps the numbering. Each has its own approved version of the welding code (the ACT's commenced 30 January 2023). Commencement of the 2024 and 2025 limit cuts varies, as above |
| WA | WHS (General) Regulations 2022 reg 49 and, on mine sites, WHS (Mines) Regulations 2022 reg 49. Health and Safety Bulletin No. 26 (25 June 2026) sets out the regulator's expected controls |
| VIC | OHS Regulations 2017 (Vic): reg 5 defines exposure standard by reference to the SWA list; reg 165 (must not be exceeded), reg 166 (atmospheric monitoring where uncertain on reasonable grounds), reg 168 (records 30 years unless WorkSafe sets a shorter period), reg 169 (health monitoring). WorkSafe Victoria (page reviewed 23 July 2026): the WEL list replaces the WES list from 1 December 2026 and operates nationally |
| NZ | HSWA 2015 ss 30 and 36. GRWM Regulations 2016 regs 29–30 (prescribed exposure standards; monitoring where not certain) and regs 31–39 (health monitoring for substances a safe work instrument specifies). WorkSafe's WES are guidance values, not prescribed limits. The 16th edition (July 2026) gives welding fume (not otherwise classified) no numeric WES: it is a confirmed carcinogen, assessed on measured components. Those carry the assessment: chromium (VI) compounds 0.00002 mg/m³ TWA (STEL 0.0005 mg/m³), 2,500 times below the current Australian WES; manganese 0.2 mg/m³ and 0.02 mg/m³ respirable; aluminium (welding fume included) 1 mg/m³ respirable. WorkSafe's *Welding and local exhaust ventilation* guidance (updated January 2020, before the 16th edition) calls for on-tool extraction, extracted booths or benches, or movable capture hoods for MIG/MAG, MMA and flux-cored work; more than 0.5 m/s of clean air movement away from the breathing zone for TIG (with dilution ventilation) and oxy-gas (with a movable hood); and baseline then annual lung function tests with a respiratory questionnaire |

### Common failure modes
- Mild steel treated as harmless, with extraction reserved for stainless
- Mild-steel fume weighed for total fume only, with no manganese analysis
- Movable hood parked a metre from the arc
- LEV installed and never tested; blocked filters; discharge recirculating
- Disposable or half-face P2 under the helmet, unshaven, no fit test
- Particulate PAPR relied on for ozone during TIG or MIG work
- Aluminium fabricators and boatbuilders still working to 5 mg/m³
- Argon purge in a vessel or pipe spool with no oxygen monitor

### Practical implications for FM / contract portfolios
- Maintenance welding (handrails, pipework, plant-room repairs) happens in
  situ with no fixed extraction. Write portable extraction and PAPR into the
  scope and add a fume-control line to the hot work permit (`hazards.md` §22).
- Prequalify welding contractors on evidence: personal monitoring with metals
  analysis (Mn always, Cr(VI) for stainless), LEV maintenance records,
  fit-test records or PAPR issue, health monitoring for stainless work.
- In occupied buildings and shared workshops, other trades and tenants share
  the plume and the arc flash: a model WHS Act s 46 matter between PCBUs.

---

## 5. Lithium-ion Batteries

### Regulatory basis
The model WHS Regulations have no battery-specific Part. The hooks are the
primary duty (model WHS Act s 19), risk management (Part 3.1) and the emergency
plan (reg 43). Part 4.7 reaches the charger, not the pack: electrical equipment
(reg 144) operates above extra-low voltage (50 V AC or 120 V ripple-free DC)
and excludes the propulsion unit of a motor car or motorcycle. Tool,
e-micromobility and most forklift packs sit at or below 120 V DC, so manage
them under s 19 and Part 3.1. Mains-powered chargers attract reg 149 (unsafe
equipment) and reg 150 (socket-outlet equipment in hostile environments).
Victoria: OHS Act 2004 ss 21 and 23 and the Dangerous Goods Act 1985 regime.
NZ: HSWA 2015 s 36 and GRWM regs 2016 reg 14. AS/NZS 4681:2000 covers Class 9
storage; read it with current regulator and fire-service guidance.

An intact battery is an article, generally not GHS-classified, so the hazardous
chemical duties in `hazards.md` §13 rarely switch on and Schedule 11 lists no
placard or manifest quantity for it. In transport it is Class 9 dangerous
goods; NSW and Victoria close that gap differently (table below). Leaked
electrolyte is a hazardous chemical in its own right.

Scale, as at October 2026: Fire and Rescue NSW (FRNSW) recorded 165 lithium-ion
battery fires in 2022, 272 in 2023 and 323 in 2024, about six a week. WorkSafe
WA Mines Safety was notified of 105 battery incidents in 2024–2025, 35% with
fire, smoke or flame and 14% involving power-tool packs (Health and Safety
Bulletin No. 27, 24 August 2026).

### Thermal runaway — mechanism and triggers
Thermal runaway is a self-heating chain reaction: heat breaks down the cell
materials, releasing more heat and flammable gas, and failure spreads cell to
cell through the pack. Smothering does not stop it, and nothing reliably halts
a cell already in runaway; sustained cooling with large volumes of water limits
spread to neighbouring cells and packs.

| Trigger | Typical workplace cause |
|---|---|
| Electrical abuse | Wrong or non-OEM charger, failed battery management system, non-rechargeable lithium cell placed on charge |
| Mechanical damage | Dropped tool pack, forklift tyne strike, crash-damaged EV, crushing in a waste compactor |
| Heat | Pack left in a vehicle cab or direct sun, charging beside a heat source |
| Internal fault | Manufacturing defect, uncertified or rebuilt pack, recalled product still in service |
| Ingress and age | Water or flood immersion, swollen or end-of-life cells kept in use |

Warning signs that start the quarantine sequence below: swelling, heat when
idle, hissing or popping, unusual odour, leaking, white or grey vapour. Damaged
batteries can take hours to ignite (EPA Victoria Publication 2018).

### Fire behaviour — what the emergency plan must assume
| Behaviour | Planning consequence |
|---|---|
| Flammable off-gas (hydrogen, carbon monoxide, hydrocarbons) vents before and during the fire | Vapour trapped in a cabinet, container, vehicle or room can ignite explosively — do not open it; keep people out of the vapour cloud |
| Toxic, corrosive smoke — hydrogen fluoride measured at 20–200 mg per Wh of battery capacity in fire tests (Larsson et al., 2017) | Evacuate upwind; treat smoke inhalation and skin contact as medical exposures; residue and firewater are contaminated |
| Self-sustaining reaction | Extinguishers and blankets may knock down flame but do not cool the pack; fire services plan on sustained water for cooling |
| Reignition hours or days later | Outdoor quarantine with a watch after any event; a "burnt-out" unit never goes back into a store, vehicle or skip |
| Fast escalation with jetting flame | No time for an improvised response; a device burning on the egress path traps people |

SafeWork NSW is blunt: do not attempt to put out a lithium-ion battery fire —
evacuate and call 000. WorkSafe Victoria's alert (30 August 2023) says the plan
should prohibit extinguishing attempts. FRNSW's SARET research compares
alternative agents with water; until a regulator or fire service endorses one,
do not build the plan around a "lithium" extinguisher or fire blanket.

### Workplace scenarios
| Scenario | Where it goes wrong | Priority controls |
|---|---|---|
| Worker-owned e-bikes, e-scooters and devices charged on premises | Uncertified or modified packs charged under desks, in corridors, beside exits | Settle the rule with workers: a designated charging point that meets the design rules below, or no charging on site — never in egress paths |
| Power-tool batteries | Aftermarket packs, chargers running in site sheds and vehicles, packs dropped or wet | OEM packs and chargers only; charging station on a non-combustible surface; re-inspect after any drop |
| Forklifts, EWPs and other electric plant | Retrofit lithium packs, charging inside racked storage, tyne damage | OEM-approved conversions only (battery mass is part of a counterbalance truck's stability); charging bay clear of racking with remote isolation (cross-ref `hazards.md` §12) |
| EV fleet and chargers | Charging in enclosed car parks; damaged vehicles returned to the pool | Chargers installed to AS/NZS 3000 by a licensed electrician; no charging in enclosed spaces unless detection and suppression are designed for battery fire (WorkSafe Victoria); isolation point on the site plan |
| EV workshops and crash repair | High-voltage work without isolation; damaged packs stored indoors | Trained technicians, insulated tools, OEM de-energisation procedure (cross-ref `hazards.md` §10); outdoor quarantine bay clear of buildings and other vehicles |
| Warehousing, freight and retail stock | Bulk pallets in general racking, forklift damage, returns of unknown condition | Lowest practicable stock; dedicated Class 9 store with detection; returns treated as suspect until inspected |
| Waste and recycling streams | Batteries hidden in general waste ignite in compactors, trucks and stockpiles | Separate collection; never general waste or commingled recycling bins (cross-ref `sector-regimes-2.md` §3) |
| Building and grid-scale BESS | Propagation between units; ignition of accumulated gas | AS/NZS 5139:2019 (Amendment 1 published 19 December 2025) for 1–200 kWh installations; larger systems cross-ref `sector-regimes-2.md` §5 |

### Jurisdiction variations (as at October 2026)
| Jurisdiction | Position |
|---|---|
| NSW | WHS Regulation 2025 (commenced 22 August 2025): a workplace that stores, handles or installs 25,000 kg or more of lithium batteries must have a s 43 emergency plan covering battery fire and lodge it with FRNSW (s 361(1A)). FRNSW's position statement sets the lodgement format; an Emergency Services Information Package (ESIP) is one accepted option. Product safety: e-bikes, e-scooters, e-skateboards, self-balancing scooters and their batteries are declared electrical articles under the Gas and Electricity (Consumer Safety) Act 2017 (declared 2 August 2024) — prescribed standards from 1 February 2025; accredited testing, Certificate of Approval and marking from 1 February 2026. Hire fleets bought before 1 February 2026 must meet the standards but need not be certified and marked |
| VIC | Class 9 falls within the Dangerous Goods (Storage and Handling) Regulations 2022: Schedule 2 manifest quantity is 10,000 kg or L, and Class 9 goods with no packing group are taken to be Packing Group III. Above it: manifest, notification to WorkSafe renewed at least every two years, and fire protection and an emergency plan on which the fire authority (FRV or CFA) gives written advice (regs 48, 52 and 53) — run WorkSafe Victoria's dangerous goods calculator. Energy Safe Victoria consulted in 2025 on declaring e-transport devices controlled electrical equipment (Electricity Safety Act 1998 s 55); no declaration had been made, pending national action |
| QLD | Electrical Safety Office guidance: charge workplace-supplied devices on a non-combustible surface, away from exits and populated spaces |
| WA | Dangerous Goods Safety Act 2004 and Dangerous Goods Safety (Storage and Handling of Non-explosives) Regulations 2007 continue beside the WHS Act 2020 for Class 9 storage; WorkSafe WA publishes an AS/NZS 4681 compliance check for Class 9 stores. Mines: Health and Safety Bulletin No. 27 |
| Cth (national) | No national mandatory safety standard for e-micromobility is in force. In May 2026 the Commonwealth funded the ACCC to develop nationally consistent safety standards for e-micromobility devices; its investigation of e-bike risks began in June 2026, with consultation expected by late 2026 |
| NZ | Electricity (Safety) Regulations 2010, as amended from 13 November 2025, expressly cover e-bikes and personal e-transporters and cite standards for lithium batteries; newly covered products have until 13 November 2026 to comply. WorkSafe (Energy Safety) recommends obtaining the Supplier Declaration of Conformity before buying a battery or charger. Transport: Land Transport Rule: Dangerous Goods 2005 |

### Controls
**Procurement**
- Specify by standard, not brand. The NSW prescribed list (editions as at
  October 2026) is a workable floor anywhere. E-bikes to 500 W: AS 15194:2016,
  EN 15194:2017+A1:2023 or UL 2849:2022 (above 500 W, UL 2849:2022 only).
  Batteries: EN 50604-1:2016+A1:2021, IEC 62133-2:2017 or UL 2271:2023.
  E-scooters and similar: AS/NZS 60335.2.114:2023, EN 17128:2020 or
  UL 2272:2024. Chargers: AS/NZS 60335.2.29 or AS/NZS 61558. UL 2271:2018 and
  UL 2272:2016 are accepted only until 1 February 2027
- Require the UN 38.3 test summary (ADG 7.9: available through the supply chain)
- OEM or OEM-approved packs and chargers only; no aftermarket or rebuilt packs
- Check the ACCC Product Safety recall list at purchase and at each register
  review; keep a battery register (type, location, mass, kWh)

**Charging area design and rules**
- Outdoors, or in a space with working smoke detection and sprinklers,
  separated from occupied areas; clear of exits and evacuation routes
- Non-combustible surface; away from combustibles, direct sun, heat and moisture
- Remote isolation for charger circuits (e-stop or isolator reachable without
  approaching the fire); compatible chargers that cut off on fault or full
  charge; rechargeable cells only
- Portable packs, e-micromobility and tool batteries: charge in staffed hours,
  never unattended or for long periods (SafeWork NSW)
- Fleets that must charge overnight (forklift, EWP, EV): engineered bay, heat or
  flame detection linked to the fire alarm, automatic charger disconnection on
  alarm (WorkSafe Victoria), clear of racking and combustibles
- Chargers in sheds, vehicles and workshops: regular inspection and testing by
  a competent person (reg 150; AS/NZS 3760:2022; see `hazards.md` §10)

**Storage**
- Lowest practicable quantity; cool, dry, ventilated, out of vehicles and sun
- Segregated from flammable liquids, gas cylinders, other dangerous goods and
  combustible stock; damaged units never share the store
- Waste stores (EPA Victoria Publication 2018): consider at least 10 m from
  other dangerous goods and combustibles; at most 30 kg per container of small
  lithium-ion batteries. End-of-life collection and storage: AS/NZS 5377

**Inspection and quarantine of damaged, defective or recalled units**
1. Inspect before use and after any drop or impact: swelling, heat, leaks,
   corrosion, casing damage
2. Suspect unit: stop use, disconnect, tag out. A damaged, swollen, leaking or
   recalled pack is never repaired or reused. A suspect charger stays off until
   a competent person tests it and finds it safe, or is replaced (reg 149)
3. Not venting: move it outdoors to quarantine, terminals taped, alone in a
   vented UN-approved container (plastic, or metal with a non-conductive lining)
   filled with sand or vermiculite, clear of buildings, vehicles, combustibles
4. Venting, smoking or hot: do not handle — evacuate and call 000
5. Send it to a battery recycler under the transport rules below

### Transport — ADG Code 7.9 (current as at October 2026)
- Class 9: UN 3480 and UN 3481 (lithium ion, alone or with equipment), UN 3090
  and UN 3091 (lithium metal), UN 3556 (vehicle, lithium ion battery powered;
  new in 7.9, mandatory since 1 October 2025; cross-ref `environment.md` §7)
- Damaged or defective: special provision 376 and P908 (LP904 for large
  packagings): each unit packed individually, leak-proof, in non-combustible,
  non-conductive thermal insulation; mark "DAMAGED/DEFECTIVE" with the proper
  shipping name; the transport document cites special provision 376
- A unit liable to rapidly disassemble, react dangerously, or produce flame,
  dangerous heat or toxic, corrosive or flammable gas in normal transport
  (swollen and warm, recently vented, crash-damaged EV pack) needs P911 (LP906)
  or competent-authority conditions. The recycler's dangerous goods adviser
  classifies it. Never ordinary freight, never a courier satchel
- Waste for recycling or disposal: special provision 377 and P909 — never for
  damaged or defective units. Special provision 188 small-battery relief
  assumes undamaged, tested cells; it does not cover a swollen tool pack
- Standards Australia's free guide *Used Lithium Batteries: Guidance on Safe
  Packaging and Transport by Road and Rail* (June 2026) serves collection
  points and transporters. Air freight: `sector-regimes.md` §4

### Emergency plan and fire service liaison
Every workplace emergency plan (model reg 43; NZ GRWM Regs reg 14; see
`workplace-controls.md` §2) covers battery fire wherever batteries are charged
or stored. Victoria has no general reg 43 equivalent; below manifest quantity
the OHS Act 2004 s 21 duty carries it. Extra triggers: NSW 25,000 kg (lodge
with FRNSW); VIC above manifest quantity (fire authority advice). It covers:
- Site plan showing battery stores, charging points, EV chargers, BESS and
  their isolation points, with quantities in kg and kWh
- Trigger: venting, smoke or popping means evacuate upwind and call 000, stating
  "lithium-ion battery"; wardens do not fight it; treat the plume as toxic
- After the event: reignition watch, outdoor quarantine, competent clean-up of
  residue and firewater
- Notification: an uncontrolled fire or explosion that exposes a person to a
  serious risk from immediate or imminent exposure is a dangerous incident
  (model WHS Act s 37): notify immediately (s 38), preserve the site (s 39),
  injury or not. VIC: OHS Act 2004 ss 37–39. NZ: HSWA ss 24, 55 and 56
- Liaison: lodge with FRNSW at the NSW threshold; elsewhere, brief the local
  station and exercise the scenario before it is needed

### Common failure modes
- Blanket charging ban with no compliant alternative — charging moves under
  desks and into storerooms; design for the work as done, not the memo
- Chemical register complete, battery register absent — nobody knows the site
  holds tonnes of Class 9
- "Lithium" extinguisher or blanket bought as the control; emergency plan
  unchanged and wardens expected to use it
- Swollen or dropped packs kept in service, or binned in the general waste skip
- Returned, recalled or crash-damaged units stored indoors "until collected",
  then consigned as ordinary freight

### Practical implications for FM / contract portfolios
- End-of-trip facilities and tenancy fit-outs: e-bike charging needs a designed
  location agreed between building owner and tenants (model WHS Act s 46)
- Cleaning, grounds and security contractors charge scrubbers, blowers, radios
  and tool packs in cleaners' rooms and plant rooms — inspect those rooms
- UPS and building BESS belong on the asset register and the emergency site plan
- Prequalification: ask contractors for their battery charging, quarantine and
  disposal procedure, not a generic electrical SWMS
- NSW sites: total lithium battery mass per workplace (stock, fleet, plant,
  BESS) against the 25,000 kg lodgement threshold

---

## 6. Solar UV Radiation

### Regulatory basis
No UV-specific regulation and no enforceable solar exposure limit sits in the
model WHS Regulations. Solar UVR is managed under the primary duty (model WHS
Act s 19), including monitoring worker health and workplace conditions
(s 19(3)(g)), the hierarchy of control (model WHS Regs reg 36) and the general
workplace provisions. Instruments and guidance, as at October 2026:

| Instrument | What it does |
|---|---|
| Model WHS Regs regs 40–41 | Work environment and facilities. The model Code of Practice *Managing the work environment and facilities* (December 2025) §4.1 applies them outdoors: shelter; work moved into shade or other tasks when the sun is most intense (it names 10 am–2 pm, 11 am–3 pm daylight saving); wide-brim hat, long-sleeved collared shirt, long pants, sunglasses, sunscreen. Schedule by the day's sun protection times instead: RPS 12 cl 3.5.1 puts summer overexposure 2–3 hours either side of solar noon |
| Model WHS Regs regs 44–46; WHS Act s 273 | Clothing, hats, eyewear and sunscreen relied on as controls are PPE: the PCBU selects, provides, trains and maintains; the worker uses it; no charge to the worker |
| Model WHS Act ss 47–49 (VIC OHS Act 2004 s 35; NZ HSWA s 58) | Consult workers on the risk assessment, controls and PPE selection. Fit, women's sizing, heat comfort and helmet and hi-vis compatibility decide whether PPE stays on |
| SWA *Guide on exposure to solar ultraviolet radiation (UVR)* (December 2019) | National guidance: risk factors, controls, sample sun protection policy, skin checks |
| ARPANSA RPS 12 *Radiation Protection Standard for Occupational Exposure to Ultraviolet Radiation* (2006) | Exposure limits and an employer UV protection program for solar and artificial sources; binding only where a regulator or licence calls it up, otherwise evidence of what is known |
| Cancer Council *Skin cancer and outdoor work: a work health and safety guide* (National Skin Committee; updated April 2025) | Most current practical guide; PPE specification detail |
| VIC: OHS Act 2004 ss 21–22 | No model Regulations; WorkSafe Victoria *Sun protection for outdoor workers*: protection all year for outdoor workers |
| Cth entities: ARPANS Act 1998; ARPANS Regulations 2018 s 9 | An accessible artificial UV source that can expose a person above RPS 12 limits is "controlled apparatus", needing an ARPANSA source licence unless exempt |

### Exposure and burden
- Solar UVR is an IARC Group 1 carcinogen. Workplace UV causes about 200
  melanomas and 34,000 non-melanoma skin cancers a year in Australia
  (ARPANSA; Cancer Council). WHO/ILO (2023): nearly one in three
  non-melanoma skin cancer deaths worldwide is due to outdoor work in the sun
- Outdoor workers get five to ten times the UV exposure of indoor workers
  (SWA Guide). AWES: 22% of Australian workers are exposed at work,
  including 99% of agricultural and 86% of construction workers (ARPANSA);
  only 8.7% of those exposed were fully protected, meaning hat, sunscreen,
  clothing and shade for more than half their outdoor time (Cancer Council)
- Eyes: photokeratitis (acute), cataract, pterygium, conjunctival SCC.
  Missed cohorts: drivers, plant operators, traffic controllers, PE
  teachers, security patrols; intermittent exposure still accumulates
- Higher individual risk (Cancer Council guide): previous skin cancer, family
  history, fair skin that burns, many moles, solar keratoses, age 50+, lupus
  and other photosensitive conditions. Same controls done well, plus a
  confidential route to adjust tasks and a doctor-led surveillance plan

### Exposure standard — ARPANSA RPS 12
- **Limit (Schedule 1)**: 30 J/m² effective (spectrally weighted) on
  unprotected skin or eye in any 8 hours, plus 10 kJ/m² UVA (315–400 nm) to
  the unprotected eye
- **Artificial sources**: no person may be exposed above it (cl 3.4.3)
- **Solar**: a guideline, because personal dose cannot practically be
  assessed (cl 3.5.1–3.5.2). The s 2.1 employer program applies in full: a
  plan made with the workforce consulted, training records, resources and
  PPE at the employer's expense, problems investigated, exposure minimised

Minutes for unprotected skin or eyes to exceed the limit (Annex 3, Table 4):

| UV Index | 3 | 6 | 8 | 10 | 12 | 14 |
|---|---|---|---|---|---|---|
| Minutes | 26 | 13 | 10 | 8 | 7 | 6 |

A summer outdoor shift exceeds the limit many times over; a winter day
peaking at UV Index 2 still accumulates about 9 SED of ambient UV against
the 1 SED a day the Cancer Council guide treats as safe (Figure 4).
Dosimeters rank exposure groups or test controls; they are no compliance test.

### UV Index 3 trigger — and where it fails
UV Index 3 and above is the public-health trigger (Bureau of Meteorology sun
protection times; ARPANSA UV Index; Earth Sciences New Zealand, formerly
NIWA). Put the forecast in the pre-start. For workers it under-protects:

| Situation | Why | Response |
|---|---|---|
| Outdoors most of the shift | Dose is cumulative; the daily limit is still likely to be exceeded below UV Index 3 (ARPANSA) | Sun protection year-round as standing PPE (ARPANSA, Cancer Council, WorkSafe Victoria) |
| Reflective surfaces | Reflected UV gets under a brim and into shade: snow 50–88%, sea foam 25–30%, white paint 22%, dry sand 15–18%, concrete 8–12%, lawn 2–5% (SWA Guide Table 4) | Eyewear and face sunscreen even in shade; roofing on light sheeting, concrete pours, marine and alpine work |
| Altitude | About 10% more UV per 1,000 m (WHO) | Alpine work is year-round, high-UV work |
| Cool or cloudy day | UV is unrelated to temperature and light cloud barely reduces it (WHO). UV peaks at solar noon, air temperature around 3 pm (Cancer Council) | Act on the UV forecast, never the thermometer. Heat triggers (`hazards.md` §6) do not protect against UV |
| Shade with open sky | Scattered sky UV roughly equals the direct beam for most of the day (ARPANSA, quoted by Cancer Council) | Shade plus PPE, not shade alone |
| Vehicle and plant cabs | Laminated windscreen about PF 50+; plain side glass about PF 12 (Cancer Council) | Film on side and rear glass within state tint rules; air conditioning, because film only works with windows shut (SWA Guide) |
| Photosensitisers | Coal tar, pitch, creosote, some dyes; plants (fig, lime, lemon, fennel, dill); medicines (tetracycline and fluoroquinolone antibiotics, NSAIDs, some diuretics, retinoids, amiodarone) | Flag in the chemical risk assessment; tell workers to ask their pharmacist or GP; adjust tasks on disclosure |

### Hierarchy of controls
| Level | Application |
|---|---|
| Elimination | Move the task indoors; prefabricate or pre-assemble inside a building |
| Substitution | Limited for a natural hazard: change the method so less of the task is done in the open, e.g. mechanised or remote-operated plant instead of hand work |
| Isolation / engineering | Shade at the workface, not only at crib: permanent cover, portable canopies, plant canopies, enclosed cabs. Expect it for fixed-location tasks that run through the sun protection times (a pour, a roof section, a traffic control post) and record why if it is not reasonably practicable. Shade cloth to AS 4174: "Most Effective" UVE (95%+) preferred, "Effective" (80–90.9%) the minimum (WorkSafe Victoria). Window film; darken or cover reflective surfaces. Shade cuts direct UV by only about half (Cancer Council) |
| Administrative | Schedule outdoor tasks outside the sun protection times where practicable and fill the peak with indoor or shaded work; UV forecast in the pre-start; rotation (shares dose, does not remove it); policy; induction and training; supervision; sunburn reported as an incident |
| PPE | Clothing, hat, eyewear, then sunscreen for skin that cannot be covered. PPE plus scheduling alone is defensible for short, mobile tasks that shade cannot follow |

PPE specification (standards current as at October 2026):

| Item | Standard | Specify |
|---|---|---|
| Clothing | AS/NZS 4399:2020: UPF 15 minimum, 30 good, 50 and 50+ excellent protection | UPF 50+ long-sleeved collared shirt and long trousers, lightweight and vented because workers shed hot PPE; confirm the UPF label on hi-vis garments; protection drops when fabric is wet, stretched or worn |
| Hat | AS/NZS 4399:2020 (material UPF; minimum brim requirements); AS/NZS 1801:2024 (helmets) | Broad brim 7.5 cm or more, bucket 6 cm or more with a deep crown, or legionnaire (SWA Guide); no baseball caps; on helmets a brim and neck flap the helmet manufacturer supports |
| Eyewear | AS/NZS 1067.1:2016 (sunglasses, lens categories 0–4); AS/NZS 1337.1:2010 (safety eyewear; under review) | Close-fitting wraparound category 2–3 (category 4 is not for driving); where impact protection is needed, AS/NZS 1337.1 eyewear, tinted or clear marked "O" for outdoor use; lens darkness and polarisation say nothing about UV |
| Sunscreen | AS/NZS 2604:2021; TGA-listed (AUST L) | SPF 50 or 50+, broad spectrum, water resistant; about 35 mL (seven teaspoons) per full-body application, 20 minutes before exposure, again every two hours; stored below 30 °C (not in a vehicle); in date; pump packs with a mirror at point of use |

Sunscreen is last because it fails quietly: people apply about half the
tested thickness and get a third to half of the labelled SPF (RPS 12
Annex 3). In September 2025 the TGA recalled several sunscreens sharing an
SPF 50+ base formulation for lower-than-claimed SPF and is reviewing SPF
testing; check its recall list before bulk purchase (as at October 2026).

### Policy and supervision
- Policy minimum (SWA Guide Appendix A): who is covered (include drivers and
  intermittent roles), trigger (year-round for outdoor workers), controls in
  hierarchy order, PPE issue and replacement, induction, sunburn reporting,
  contractors, review at least every two years
- Treat sunburn at work as an incident: the most visible early sign that
  controls failed, decades before any cancer diagnosis
- When sleeves are rolled up or sunscreen is skipped, ask what makes
  protection hard (heat load, fogging lenses, greasy grip, no shade at the
  workface, sunscreen 300 m away in the site office) and fix the design
  before reaching for discipline (`frameworks.md` §5). Leaders wear it too

### Skin checks and health monitoring
- Part 7.1 health monitoring (model WHS Regs reg 368) does not apply: solar UV
  is not a hazardous chemical. The monitoring duty does (model WHS Act
  s 19(3)(g); VIC OHS Act 2004 s 22; NZ HSWA s 36(3)(g)): sunburn and
  skin-change reporting, supervising control use, self-examination training
- SWA Guide §5: consider funded skin checks and teach self-examination;
  checks never replace controls. Cancer Council (April 2025) puts controls
  and self-examination ahead of employer screening: no government-funded
  screening program exists, and 55–70% of melanomas are found by the person
  or their partner. Funded checks need a practitioner trained in skin
  cancer, full-body examination, a body-map record and referral of
  suspected lesions to the worker's own doctor or a skin specialist
- Results stay with the provider; the employer sees participation data only

### Workers compensation
- SWA *Deemed diseases in Australia* (revised April 2024): melanoma and
  non-melanoma skin cancer against solar radiation; ocular melanoma against
  UV from welding. Latency minimum five years, commonly at least 15–20;
  non-occupational sun exposure is the main competing risk factor. Advisory
  only: each scheme's own schedule governs (`compensation-rtw.md` §12)
- 1,679 sun-related claims, 2009–2019, costing $63 million (cited by Cancer
  Council, as at April 2025); latency means claims understate incidence
- County Court of Victoria, August 2003: a retired truck driver's skin
  cancers held serious enough to sue Boral Bricks, his employer of 35 years.
  AAT, November 2017 (*McKechnie and Military Rehabilitation and
  Compensation Commission*): melanoma compensated where service without sun
  protection training or PPE materially contributed
- The defence is records: policy versions, PPE issue, training and SWMS
  controls, kept with the long-latency disease records

### Artificial UV sources
- Arc welding, germicidal (UVC) lamps, UVA lamps (curing, insect control),
  high-intensity discharge lighting, UV LEDs. The limits are firm: an
  unprotected person exceeds them in about 1–3 minutes at a germicidal lamp,
  1–5 at an arc welder and 17 at a UVA lamp, faster at closer range (RPS 12
  Annex 3, Table 5). UVC is absent from sunlight, so sun-rated clothing and
  sunglasses are not assessed for it (ARPANSA)
- FM portfolios: germicidal lamps inside air-handling units and ductwork.
  Interlock the access doors or isolate the lamps before entry, and write it
  into the AHU isolation procedure (`hazards.md` §10)
- Controls (RPS 12 Annex 3): enclosure, fail-safe interlocks, shielding,
  ozone ventilation, signage restricting access. Welding curtains to AS/NZS
  ISO 25980:2024 (replaced AS/NZS 3957:2014); filters to AS/NZS 1338.1:2012
  (welding) and AS/NZS 1338.2:2012 (UV); full skin cover for welders.
  Bystanders get "arc eye" hours after exposure. See `hazards.md` §22 and
  §4, and ARPANSA RPS 12 for the exposure limits

### New Zealand
- HSWA 2015 s 36 (including s 36(3)(g), monitoring health and conditions),
  s 27 (no charge) and s 58 (engagement); GRWM Regulations 2016 reg 9
  (information, training, supervision) and reg 15 (PCBU provides PPE)
- WorkSafe NZ *Protecting workers from solar UV radiation* (January 2018):
  Plan-Do-Check-Act; protection at UV Index 3+; peak September–April,
  10 am–4 pm; SPF 50+; a system monitoring skin and eye health and sunburn
- Sunscreen (Product Safety Standard) Act 2022 s 6 makes AS/NZS 2604:2012 a
  mandatory product safety standard under the Fair Trading Act 1986; the
  2012 edition remains the cited one (as at October 2026)
- ACC (Accident Compensation Act 2001, as at October 2026): solar skin
  cancer is not in Schedule 2, so cover turns on s 30. A property of the
  work task or environment must cause or contribute (s 30(2)(b)(i)); where
  sun exposure occurs at work and outside it, work must be the more likely
  cause (s 30(2)(c), replaced from 30 October 2022); ACC may decline if the
  risk is not significantly greater for people doing that work (s 30(2A)).
  Ocular melanoma from welding UV is Schedule 2 item 49, inserted
  27 November 2025 (`compensation-rtw.md` §4)

### Common failure modes
- Sunscreen-only program: a tub in the site office and nothing upstream
- Trigger set on temperature, or sun protection treated as summer-only
- Early-start heat rosters that keep the crew outdoors through solar noon
- Short-sleeve hi-vis and caps issued as the default uniform; drivers,
  plant operators and contractors left out of the policy
- Workers charged for hats or sunscreen (WHS Act s 273; HSWA s 27)

### Practical implications for FM / contract portfolios
- Grounds, roofing and gutter, facade, traffic management and waste crews
  are all-day exposure groups; mobile technicians get it through side glass
- Write UPF 50+ long-sleeve garments, brimmed helmets and vehicle window
  film into uniform and fleet specifications rather than site discretion
- Require sun protection controls in subcontractor SWMS and check them with
  heat planning at summer pre-mobilisation (`hazards.md` §6)

---

## 7. Abrasive Blasting

### Regulatory basis
Model WHS Regs reg 382 and Sch 10 Table 10.3 (restricted blasting media);
reg 392(o) (lead paint); reg 446 (asbestos); regs 49–50 (exposure standard,
air monitoring); regs 529A–529CE (crystalline silica); reg 368 and Sch 14
(health monitoring); regs 57–58 (noise). SWA model Code of Practice
*Abrasive blasting*, approved under s 274 in the model-law jurisdictions.
AS/NZS 1715:2009 and AS/NZS 1716:2012, the editions cited in the Code and in
reg 529B(3). "Abrasive blasting" (model reg 5) means propelling abrasive at
high speed against a surface using compressed air, liquid, steam,
centrifugal wheels or paddles, so wet blasting, wheel machines and bench
cabinets all fall inside reg 382.

### Restricted blasting media — reg 382, Sch 10 Table 10.3
A PCBU must not use, handle or store these for abrasive blasting, or direct
or allow a worker to. Reg 383 authorisations cover only the carcinogen
tables; a medium over a limit needs a regulator exemption under reg 684.
SafeWork NSW class Exemption 001/20, for example, allowed ferro-nickel slag
with up to 0.8% chromium (III) on health monitoring, SDS and labelling
conditions, 26 February 2020 to 26 February 2025. Ask the supplier for a
current exemption instrument in the jurisdiction of use, not an assurance.

| Substance in the medium | Restricted at | Item |
|---|---|---|
| Free silica (crystalline silicon dioxide) | More than 1% | 10 |
| Antimony, arsenic, beryllium, cadmium, cobalt, nickel, tin (and compounds) | More than 0.1% as the element | 1, 2, 4, 5, 9, 14, 20 |
| Chromium and compounds | More than 0.5% as chromium | 8 |
| Lead and compounds | More than 0.1% as lead, or any level that would expose the operator above the Part 7.2 lead levels | 11 |
| Chromate, nitrates, nitrites | Any amount, in wet abrasive blasting; this catches rust inhibitors, so specify the inhibitor chemistry in the purchase order | 7, 15, 16 |
| Radioactive substance above 1 Bq/g | Prohibited so far as is reasonably practicable | 17 |

- **Out**: river sand, beach sand, quartz dust, diatomaceous earth (Code
  App B): all over 1% free silica, so prohibited (reg 382; VIC reg 153, Sch 6).
- **Check every medium**: garnet and staurolite can carry trace crystalline
  silica and thorium; slags vary by source. Require the SDS plus a batch
  certificate of analysis (silica, heavy metals, Bq/g), metallic media
  included. Stainless-steel media contain at least 10.5% chromium: check them
  against item 8 and get the supplier's compliance position in writing.
- **Code App B lists as usable**: ilmenite, aluminium oxide, low-silica
  garnet, metal shot, steel grit, crushed glass, glass and plastic bead,
  sodium bicarbonate, some metal slags, dry ice.

### The substrate decides the rest
The 1% limit governs the medium. What comes off the surface brings its own
regime, and the coating is usually the more toxic of the two.

| Surface | Trigger | Consequence |
|---|---|---|
| Paint with more than 1% lead by dry weight (bridges, tanks, ships, old plant) | Reg 392(o): lead process, including handling the waste | Confirm by laboratory analysis of paint samples (portable XRF as a screen). Assess for lead risk work without counting PPE (reg 402(3)); if it cannot be determined, it is taken to be lead risk work (reg 402(4)); notify the regulator within 7 days (reg 403); health monitoring before starting and one month after (reg 405). Blood lead thresholds: §2 |
| Concrete, sandstone, brick, calcium silicate, foundry castings | Material with at least 1% crystalline silica is a crystalline silica substance (CSS) (reg 529A). Reg 529A "processing" does not name blasting, but limb (f) covers any process that exposes a person to RCS during the handling of a CSS, and SWA's *Working with crystalline silica substances* (July 2024, s 4.1) lists abrasive blasting as processing. Treat it as processing | Processing must be controlled (reg 529C): at least one reg 529B(1)(b) control (isolation, enclosed cabin with high-efficiency filtration, wet suppression, on-tool extraction or LEV), plus RPE for anyone still exposed. Before starting, assess in writing whether it is high risk, disregarding PPE and administrative controls (reg 529CA); if you cannot decide, it is taken to be high risk (reg 529CA(5)). If high risk: silica risk control plan before work starts (reg 529CB; a compliant SWMS serves for high risk construction work, reg 529CB(3)) and training (reg 529CD). See `hazards.md` §2 |
| Asbestos or ACM (textured coatings, cement sheet, flashings) | Reg 446 | Blasting prohibited. Sample suspect coatings before quoting. See `hazards.md` §3 |

### Hierarchy of controls
| Level | Application |
|---|---|
| Elimination | Shop-blasted and primed steel, or a coating and detail specification that removes the need for site blasting |
| Substitution | Metallic, recyclable abrasives (steel grit, chilled iron) shatter less and make less dust than mineral media. For small areas: chemical strippers, power tools with dust collection, scraping (Code s 3.2) or water jetting, each with risks to assess and control. High-pressure water on asbestos or ACM is prohibited (reg 446(1)(a)); power-tool or water-jet removal of paint above 1% lead is still a lead process (reg 392(o)) |
| Isolation | Cabinet or chamber wherever practicable; open-air blasting only when there is no alternative (Code s 3.2). Blast cabinet or centrifugal wheel machine (operator outside); blast chamber or temporary enclosure for large or fixed items (isolates everyone else; the operator inside still needs the airline helmet) |
| Engineering | Wet blasting (water added before the nozzle); dust extraction and collection; dead-man control. Vacuum blasting (shrouded nozzle sealed to the surface) works only with the seal intact: supply inside-corner, outside-corner and flat heads and build head changes into the task time, or the head gets lifted for odd shapes and the seal breaks (Code s 3.2) |
| Administrative | Exclusion zones, blasting out of hours, stopping in wind, wet or HEPA-vacuum clean-up, wash and change facilities, clean meal area |
| PPE | Airline blast helmet, blast suit, leather or canvas gloves, hearing protection. For open, chamber and temporary-enclosure blasting the operator wears it whatever else is in place; a properly designed and maintained cabinet needs no RPE (Code s 3.2) |

### Enclosure and exclusion-zone benchmarks (Code ss 3.2, 3.4)
| Element | Benchmark |
|---|---|
| Chamber airflow | At least 0.3 m/s down-draught, or 0.4 m/s cross-draught towards extraction; run while blasting and for 5 minutes after; filter before discharge |
| Ventilation testing | At installation, after a change of abrasive or process, after damage or repair, and periodically (12-monthly as a guide) by a hygienist or other competent person |
| Chamber fit-out | Abrasive-resistant and non-combustible; interlocked doors; emergency exit furthest from the main door, signed and backlit; 200 lux at 1 m above the floor; bonded and earthed |
| Cabinet | Sealed viewing window, dust-tight light, extraction, interlocked door, clearance time before opening; inspect gloves, gaskets and door seals |
| Temporary enclosure | Fully enclose where possible; otherwise screens 2 m above the structure and blast downwards; extraction fitted; tear-resistant, fire-retardant sheeting; stringent monitoring may be needed. Shadecloth is not containment for silica, lead or other toxic dust |
| Exclusion zone (s 3.2) | No default distance: size it by risk assessment, extend it downwind; signs; RPE for anyone who must enter. Practitioner addition, not a Code benchmark: boundary air monitoring to prove it holds |

### Respiratory protection and breathing air
| Element | Requirement |
|---|---|
| Nozzle operator | Positive-pressure airline hood or helmet with inner bib and shoulder cape (AS/NZS 1716:2012), mandatory inside a chamber. The helmet is also the head, face and eye impact protection |
| Air volume | At least 170 L/min continuous flow per person. The Code (s 3.2) says measured "at the regulator"; WorkSafe NZ says "at the respirator". Size and test the supply to deliver 170 L/min at the helmet with the full airline connected; cooled helmets and air-fed suits need more |
| Air quality | AS/NZS 1715:2009 breathing-air specification (oxygen, carbon monoxide, carbon dioxide, oil, water). Test on a schedule set by the manufacturer or a competent person; keep the results |
| Carbon monoxide | The breathing-air failure that kills. It enters through the intake (site it away from engine exhausts) or forms inside an overheating oil-lubricated compressor; WorkSafe NZ says oil-free where practicable. The Code (s 3.2) wants an alarm that warns and logs CO: fit it on the purified air line, downstream of the filters. Cylinder supplies need a low-pressure alarm |
| Separate supply | Filtered, tested breathing air, not a tee off the blast-pot line. Airlines routed clear of vehicles and the blast stream |
| Everyone else | Pot attendant, clean-up crew and anyone in the work area wear air-purifying respirators selected under AS/NZS 1715; tight-fitting facepieces need fit testing (`specialist-topics.md` §1) |
| Helmet care | Never hung by the air hose; vacuumed and bagged after use, washed inside weekly, disinfected between users; capes replaced, not taped (Code s 3.2) |

### Plant — dead-man control, hoses, static, pressure equipment
| Item | Code expectation (s 3.4 unless noted) |
|---|---|
| Dead-man control | Fast-acting, self-actuating cut-off at the nozzle under the operator's direct control. Pneumatic only to 40 m of hose; electric beyond. Inspect and function-test several times a shift. Never taped, tied or modified |
| Nozzle and attendant (s 3.3) | Nozzle pointed only at the work, never at a person. A dedicated pot attendant with line of sight to the blaster, above all when elevated or in a confined space |
| Hoses and couplings | Purpose-designed; rated pressure not exceeded; whip checks or coupling safety locks (or both) fitted to hoses; no blasting through a coiled hose; long-radius bends; safety cables on elevated runs; pinholes never taped |
| Static | Dry blasting charges the nozzle, hose and workpiece. Antistatic hose lining or earth wire; nozzle and workpiece earthed. The discharge is the ignition source; metal dust, organic abrasive or paint fines supply the combustible atmosphere (regs 51–52) |
| Pot and compressor | Relief valve fitted and checked, rated pressure never exceeded, blow-down procedure, muffler on the pot; competent-person inspection; daily operator check and a logbook of inspection and repair. The process destroys its own equipment |
| Registration (Regs, not Code) | Pots and air receivers are pressure vessels: design registration for AS 4343 hazard levels A to D; item registration for A to C, except serially produced vessels (model WHS Regs Sch 5; `hazards.md` §16) |

### Recycled media
- Wet abrasive cannot be recycled: the dust cannot be separated. Lead may
  not be removable from used abrasive; the Code (s 3.5) says dispose of it as
  contaminated waste (`environment.md` §9). Re-use only if treatment strips
  the lead and analysis shows the mix at or below 0.1% lead (item 11).
- Media used on concrete or sand-cast items picks up crystalline silica in the
  abrasive's size range. Recycle only if analysis keeps the working mix
  within the Table 10.3 limits.
- Recover by vacuum; never sweep or blow down. Clean through airwash, cyclone
  and screens. A supplier certificate covers the first pass only: analyse the
  working mix periodically.

### Noise, heat and vibration
- Code s 4.1 levels: nozzle discharge 112–119 dB(A); air feed inside the
  helmet 94–102 dB(A); cabinets 90–101 dB(A); compressors 85–88 dB(A); up to
  145 dB(A) at the operator when the abrasive runs out.
- At 101 dB(A) the unprotected daily limit is reached in 12 minutes. Hearing
  protection goes under the helmet and the air feed is silenced. Audiometric
  testing within 3 months of starting and at least every 2 years (reg 58(2);
  `hazards.md` §14).
- Blast suit plus helmet is a heat-strain load: cooled helmet air, shaded
  rest area, work-rest scheduling (`hazards.md` §6). Nozzle reaction
  transmits hand-arm vibration (`hazards.md` §15).
- Blasting inside tanks and vessels is confined space entry with zero
  visibility and the pot attendant out of sight (`hazards.md` §11).

### Air and health monitoring
- **Air monitoring** (reg 50) wherever it is uncertain the limit is met, at
  the pot attendant, adjacent trades and zone boundary as well as the blaster;
  records kept 30 years. High-risk CSS processing: RCS results above the
  exposure standard go to the regulator within 14 days (reg 529CE).
- **Health monitoring** (reg 368, Sch 14 Table 14.1) for significant risk
  from crystalline silica, inorganic arsenic, cadmium or inorganic chromium;
  lead under regs 405–407; asbestos under reg 435 (Code s 2.4). SWA's silica
  guidance says the significant-risk test can catch workers regularly near
  the processing, including cleaners. Reports kept 30 years (reg 378), 40
  for asbestos (reg 444).
- Exposure limits move to the WEL list on 1 December 2026 (as at October
  2026): `legislation.md` §14.

### Jurisdiction variations (as at October 2026)
| Jurisdiction | Position |
|---|---|
| Model-law jurisdictions | Reg 382 and Sch 10 Table 10.3 as above. Code versions differ: confirm the local one |
| NSW | Approved code commenced 18 July 2014, last amended December 2022; it predates the WHS Regulation 2025, so check its clause citations against that Regulation. Workers doing high risk crystalline silica work, which blasting a CSS can be, go on the Silica Worker Register within 28 days of the work starting (from 1 October 2025; `legislation.md` §2) |
| WA | *Abrasive blasting: Code of practice* published 14 July 2022 under the WHS Act 2020 (WA). WHS (General) regs 2022 reg 529CE goes further than the model: for high-risk CSS processing, air monitoring under reg 50 and health monitoring for every worker doing it, not only where the reg 368 test is met |
| VIC | OHS Regulations 2017 reg 153 and Sch 6 prohibit one thing: material with more than 1% crystalline silica for abrasive blasting. No metals list and no abrasive blasting compliance code. Lead paint blasting is a lead process (reg 178(o)). Blasting a silica-bearing surface with mechanical plant is a crystalline silica process (reg 319B(1)(a)(ii)); it is high risk crystalline silica work if reasonably likely to exceed half the exposure standard or to risk a person's health (reg 319C(b)). That triggers identification (reg 319J), a record (reg 319K) and a crystalline silica hazard control statement before work starts (reg 319L) |
| NZ | No dedicated WorkSafe abrasive blasting guidance found. HSWA 2015 s 36; GRWM regs 2016 reg 28 (substances hazardous to health, managed under regs 5–8) and regs 15–20 (PPE); the monitoring duties in regs 30 and 32 attach to prescribed exposure standards. Asbestos regs 2016 reg 18 bans compressed air and high-pressure water spray on asbestos or ACM. WorkSafe silica guidance: substitute metallic shot, slag or grit for sand. RCS WES-TWA 0.025 mg/m³, half the Australian limit and a guidance value. WorkSafe RPE guidance: 170 L/min per person measured at the respirator; air quality to AS/NZS 1715 |

### Common failure modes
- Media bought on price with no certificate of analysis; garnet assumed
  silica-free.
- Coating never sampled. The job is quoted as "rust and scale" and turns out
  to be lead primer on a 1960s structure.
- Concrete blasting run outside the silica rules because reg 529A does not
  name blasting: no written high-risk assessment, no plan.
- Dead-man handle cable-tied open because it tires the hand. Fix the handle
  design and rotation; a disciplinary response leaves the cause in place.
- Breathing air taken from the tool compressor with no filtration, CO alarm
  or air-quality test on record.
- Shadecloth "containment" and an exclusion zone set by habit, with the
  public or other trades downwind.
- Blaster in an airline helmet; pot attendant and sweeper in nothing.
- Spent lead-contaminated media stockpiled uncovered or swept dry.

### Practical implications for FM / contract portfolios
- Prequalify blasting contractors on evidence: media analysis, breathing-air
  test results, dead-man test log, enclosure ventilation test, health
  monitoring program, crystalline silica training records (reg 529CD: VET
  accredited or regulator-approved, kept 5 years after the worker leaves).
- The client or principal contractor holds the coating history. Test for lead
  and asbestos before tender and give the results to bidders.
- Blasting next to occupied premises or public space is a duty to others
  (model WHS Act s 19(2); VIC OHS Act 2004 s 23; NZ HSWA 2015 s 36(2)).
  Containment and boundary monitoring go in the method statement; dust
  leaving the site is also an environmental emission (`environment.md` §10).

---

## 8. Formwork and Falsework

### Regulatory basis
Formwork is the form face plus the framing and bracing that contain and shape
wet concrete until it is self-supporting. Falsework is the temporary structure
that carries the permanent structure, materials, plant and people until the
permanent works can carry themselves (SWA *General guide for formwork and
falsework*, July 2014). Both are structures in their own right: the PCBU that
designs them holds the designer duty (model WHS Act s 22), and the PCBU that
erects them holds the duty to construct the structure without risk (s 26).

- Model WHS Regs 294–296 (consulting the designer; designer safety report;
  hazard information to the PC), 297 (construction risk management), 54–55
  (falling objects), 78–79 (falls) and 225 (scaffolds)
- HRCW (reg 291): nearly every deck carries a risk of a fall of more than 2 m;
  pumps and cranes add powered mobile plant; refurbishment pours needing
  temporary support to prevent collapse add structural alterations; precast
  elements add tilt-up or precast; bridge falsework over roads, rail or water
  adds the traffic-corridor and drowning categories. SWMS first (reg 299) —
  `hazards.md` §8
- AS 3610.1:2018 *Formwork for concrete — Specifications* and AS 3610.2
  (Int):2023 *Design and construction* (published 22 December 2023: formwork
  actions, falsework analysis, single-sided, jump/climb and slip forms,
  component testing). Part 2 is interim — check the designation on the
  Standards Australia store before specifying it
- AS 3610—1995 has not been withdrawn: Standards Australia still lists it as
  current, and AS 3610.1:2018 replaced only its Sections 2 and 3 and Clauses
  4.7 and 6 (as at October 2026). A drawing citing only the 1995 standard is
  not invalid for that reason; ask which document governs the design actions
  and whether the Part 2 actions were checked
- AS/NZS 1576 series where scaffold components or working platforms are used;
  AS/NZS 4994 for edge protection — `hazards.md` §9
- SWA publishes the general guide plus separate guides to formwork, falsework,
  and slip, jump and travelling forms. They are guidance, not model codes

### Where it fails — three windows
| Window | What goes wrong | Controls that matter |
|---|---|---|
| Erection | Falls from leading edges, between joists and through penetrations; incomplete frames overturned by wind; materials landed on a deck that is not yet tied in | Progressive decking and false decks; edge protection before access; landing zones with point-load limits on the drawings; wind and rain stop criteria in the SWMS |
| Concrete placement | Props, ties or connections fail under full wet load — about 2.4 t per cubic metre, so a 200 mm slab puts roughly 480 kg on every square metre before workers, heaped concrete and pump surge are added; wall and column forms blow out when lateral pressure exceeds the design | Site-specific design; as-built inspection and written certificate; pour sequence and rate; observer outside the collapse zone; nobody under the deck |
| Stripping | Supports pulled before the slab can carry itself and the floors propped off it; form components falling on the crew below | Written pre-strip confirmation on verified strength; engineered back-propping; progressive stripping only |

Collapse is sudden and progressive. One prop or tie sheds its load onto
neighbours already at capacity, the deck crew goes down with wet concrete
(fractures plus alkaline burns), and anyone underneath is buried.

### Hierarchy of controls
The SWA general guide starts by asking whether another construction method
can avoid formwork and falsework altogether. Work down the list so far as is
reasonably practicable (model WHS Act s 18; reg 36).

| Level | Application |
|---|---|
| Elimination | A construction method with no in-situ formwork; permanent-works design with fewer columns, cantilevers and changes in floor depth (SWA guide; ACT code) |
| Substitution | Precast columns, beams and floor panels instead of forming on site; permanent formwork such as profiled steel decking (nothing to strip); crane-handled tableform or deck-panel systems; proprietary systems with integrated edge protection |
| Isolation / engineering | Exclusion zones for erection, pours and stripping; false decks, perimeter screens, edge protection, secured penetration covers; designed back-propping |
| Administrative | Design and pre-pour hold points; permits to load; delivery timing so loads never land on incomplete decks; pour-rate control |
| PPE | Harness only where passive protection is not reasonably practicable; a deck under construction rarely offers a rated anchor or the clearance to arrest a fall, so check both and plan rescue (`hazards.md` §9) |

### Duty holders
| Duty holder | Must deliver |
|---|---|
| Commissioning PCBUs | Whoever engages the formwork designer (usually the PC or the formwork contractor) consults that designer on construction risk (reg 294) and receives the designer's safety report (reg 295). The client commissions the permanent works: it consults that designer, obtains its reg 295 report and gives the PC its hazard information (reg 296) |
| Permanent-works structural engineer | Stripping strength criteria, back-propping layout, permitted construction loads on young slabs; tells the formwork designer about mix and admixture changes |
| Formwork designer (s 22) | Drawings for this site: system and components, prop sizes and extensions, spans, bracing and lateral restraint, footings and ground bearing, pour sequence and maximum rate, maximum point loads, stripping conditions; safety report for unusual features (reg 295) |
| Manufacturer, importer, supplier or hirer (ss 23–25) | Load tables, compatibility statements and instructions for proprietary systems. The NSW code (2.10) treats formwork components as plant; an importer without the maker's data shows compliance through NATA-registered test reports |
| Principal contractor | Confirms a certified design exists before erection; reviews the SWMS; controls loading and exclusion zones; holds the pour until the certificate is in hand — `hazards.md` §4 |
| Formwork contractor (s 26) | SWMS; builds to the drawings; alters or mixes nothing without the designer's written agreement; competent, supervised crew; culls damaged components |
| Certifying engineer or competent person | Inspects the as-built formwork against the drawings and records exactly what was inspected and certified |

### Codes of practice — jurisdiction status (as at October 2026)
| Jurisdiction | Instrument | Status |
|---|---|---|
| NSW | Code of Practice *Formwork* (SafeWork NSW) | Approved under WHS Act 2011 (NSW) s 274; commenced 26 June 2020, amended March 2021. Comply-or-equivalent under s 26A from 1 July 2026 (`legislation.md` §8). Written against the 2017 Regulation — read its references across to the equivalent provisions of the WHS Regulation 2025 (NSW) |
| QLD | *Formwork Code of Practice 2016* | Commenced 31 March 2016, varied 1 July 2018; still in force. Comply-or-equivalent under WHS Act 2011 (Qld) s 26A. Engineer certification of the formwork design; pre-pour inspection and sign-off by an engineer or other competent person. Pump work: *Concrete Pumping Code of Practice 2019* (last varied 1 July 2026) |
| ACT | *Formwork Code of Practice* (January 2024) | Approved by the Work Health and Safety (Formwork Code of Practice) Approval 2024 (NI2024-56), which revoked the 2011 code. Built on the NSW and Queensland codes; Appendix B is an example Formwork Structural Certificate |
| VIC | OHS Act 2004 (Vic) ss 21 and 26; OHS Regulations 2017 (Vic) | No model law and no formwork code. Victoria's own 19-item high risk construction work list drives the SWMS (`hazards.md` §8). WorkSafe Victoria's alert *Preventing formwork failures* (November 2013) expects engineer design for custom or mixed systems, competent-person inspection before other trades get access or the pour, and minimum strength confirmed before stripping. Prosecutions run on the general duties (see cases) |
| WA | WHS Act 2020 (WA) ss 19, 22; model *Construction Work* code | No WA-specific formwork code. WorkSafe WA's codes page still lists AS 3610:1995 *Formwork for concrete* among its "industry codes of practice". Design to AS 3610.1:2018 and AS 3610.2 (Int):2023 and treat the 1995 listing as the floor, not the benchmark |
| SA, TAS, NT, Cth | General duties (WHS Act ss 19, 22); *Construction Work* code | No jurisdiction-specific formwork code identified. The SWA guides and the AS 3610 series are the benchmark a court will be shown |

### Certification hold points
| Hold point | Requirement |
|---|---|
| Before erection | Formwork designed for this site; drawings certified to the AS 3610 series by a competent person such as a structural engineer, and available on site |
| Before loading the deck | Competent person inspects and certifies before materials, plant or prestressing tendons are landed or other trades get access; non-conformances documented and fixed before loading. Stacked pallets are point loads the deck may not be designed for |
| Before the pour | A competent person with relevant experience (e.g. a structural engineer) inspects the completed formwork and confirms in writing that it matches the design and is structurally sound. SafeWork NSW safety alert (29 November 2024): separate certification no more than 48 hours before the pour, in person unless exceptional circumstances exist, no forward-dated or conditional certificates |
| During the pour | Designated observer with communications watches the formwork from outside the collapse zone (CCTV or a remote camera where the soffit has to be watched). Nobody under the deck or directly beneath wet concrete being placed (NSW code 7.14); placement stops while a competent person makes any adjustment; inboard sections before cantilevers; rate of rise within the design maximum; pumps and hoists not attached to the formwork unless designed for it |
| Before stripping | Written confirmation from a competent person (an engineer with structural design experience) that the permanent structure is self-supporting, based on the design specification, verified concrete strength and time elapsed. Strength evidence comes from a sampling and testing procedure (specimen results to the AS 1012 series against the structural engineer's criteria) — calendar days alone are not evidence. Back-propping installed to the structural engineer's design and rechecked after post-tensioning |
| Any change | Alteration outside the design; mixing components from different systems or manufacturers; screens, shade cloth or signs attached (added wind load, NSW code 2.9); a switch to self-compacting concrete, added retarder or a cold-weather pour (higher lateral pressure on wall and column forms). The designer or a competent person assesses in writing, drawings are revised, the area is re-inspected |

### Erection — falls are the everyday injury
The NSW and ACT codes set the working detail; the 2 m figures are trigger
points, not permission to ignore shorter falls (`hazards.md` §9).

- Where workers would stand 2 m or more above the deck below to place bearers
  and joists, provide a continuous false deck across the whole area being
  formed; no gap wider than 225 mm, and only where a frame leg passes through
- Below 2 m, work from a secured platform at least 450 mm wide (two planks) —
  never a single plank or bearer
- Lay formply progressively from the perimeter edge protection, sheets placed
  in front of the body; without a false deck within 2 m, only onto at least
  four secured joists at 450 mm centres
- Edge protection complete and penetrations covered and secured before other
  trades get access; cover any penetration that stripping will expose before
  stripping starts. Perimeter screens stay from first erection until soffit
  stripping is finished

### Licences and plant registration
| Work | HRWL position |
|---|---|
| Erecting falsework that supports only formwork and concrete | No HRWL — it is not a scaffold (NSW code). Competence still has to be shown: Certificate III in Formwork/Falsework or verified units, with direct supervision for new workers |
| Falsework that will carry scaffold platforms with a fall above 4 m; adding falsework components to such a scaffold | Scaffolding HRWL: Basic (SB) for prefabricated modular components, Intermediate (SI) for tube-and-coupler — `hazards.md` §9 |
| Working platforms cantilevered off shoring frames (a cantilevered scaffold, ACT code 4.10) with a fall above 4 m | Intermediate (SI) or Advanced (SA) scaffolding HRWL — `hazards.md` §9 |
| Slinging crane-lifted formwork; rigging perimeter screens and shutters | DG; RB — `hazards.md` §19 |
| Plant design registration | Not needed for purpose-made formwork frames; needed for prefabricated scaffolding used inside the support structure — get the registration number from the supplier (NSW code 2.10; `hazards.md` §16) |

### Bridge and civil falsework
Tall, heavily loaded falsework founded on natural ground, often over live
traffic, rail or water. A competent person verifies foundation bearing
(geotechnical input for poor or wet ground) and rechecks it after rain. Road
authority contracts add engineering hold points to the WHS duties. Section
614 *Formwork* (VicRoads June 2017 text, as adopted in council
specifications) requires, for all members except abutments, footings, piers
and walls 2 m high or less, and for any member using self-compacting concrete:
design certified by an Engineers Australia member with at least five years'
comparable formwork experience; a proof engineer's certificate, from outside
the design firm, at least two days before formwork construction; and an
erected-formwork certificate accepted before any load is applied. Treat those
signatures as hold points in the WHSMP, not as quality paperwork.

### New Zealand
HSWA 2015 applies through the s 36 primary duty and the upstream duties in
s 39 (PCBU that designs plant, substances or structures) and s 43 (PCBU that
installs or constructs structures). There is no SWMS or HRCW regime, but
construction work with a risk of a fall of 5 m or more (listed exclusions
apart) and lifts of 500 kg or more through 5 m or more by a lifting appliance
other than an excavator, forklift or self-propelled mobile crane are
particular hazardous work: give WorkSafe at least 24 hours' notice (Health
and Safety in Employment Regulations 1995, reg 26). The working benchmark is
the *Temporary Works Procedural Control Good Practice Guideline* (Temporary
Works forum NZ, 2019), modelled on BS 5975: a Temporary Works Coordinator, a
register, a design brief, design and check certificates, a **permit to load**
for each item and a **permit to unload** where the designer specifies one.
Check category follows risk: formwork and falsework up to 3 m high is
Category 1 (checked within the design team); over 3 m, Category 2 (checker
not involved in or consulted on the design); structures spanning a footpath
or roadway and works next to highways, Category 3 (another organisation
checks). The Forum told Ministers in January 2025 that NZ lacks a clear
compliance pathway for temporary works across HSWA and the Building Code, so
a PCBU's own procedure carries the weight.

### Collapse cases (outcomes as at October 2026)
| Case | What failed | Outcome |
|---|---|---|
| Hotel Rottnest, WA (February 2020) | First-floor slab formwork collapsed during the pour; one worker fell about 4.5 m, another was struck below. Formwork was neither designed nor approved by an engineer, contrary to the builder's own risk register | Firm Construction Pty Ltd pleaded guilty; fined $600,000, Perth Magistrates Court, July 2023 |
| Sunshine, VIC (July 2019) | A steel beam fixing second-storey formwork to the existing slab broke away during the pour; three workers fell more than 2 m. No engineer or building surveyor inspected before the pour | Valmont (Vic) Pty Ltd found guilty; fined $125,000 without conviction plus $42,752 costs, Sunshine Magistrates' Court, 3 October 2024 |
| Parkville Station, Metro Tunnel, VIC (July 2021) | Wall form blowout released about 15 m³ of concrete; form ties had been welded to reinforcement instead of fixed with tie holders, against the tie specification | Adcon Vic Pty Ltd and Adcon Resources Vic Pty Ltd convicted; fined $250,000 in total, Melbourne Magistrates' Court, May 2024 |
| Barton Highway bridge, ACT (14 August 2010) | Bridge span formwork and falsework collapsed during the deck pour; nine workers hospitalised and 15 more assessed by paramedics at the scene | No prosecution: WorkSafe ACT's investigation ran so long that the window to prosecute closed, and no charges were laid |

### Common failure modes
- Generic system drawings used as the "design"; nothing specific to the site,
  the ground or the pour sequence
- Certificate signed from photographs, or issued "subject to" rectification
  that nobody verifies — the pattern SafeWork NSW called out in 2024
- Props, frames and heads from different systems mixed on a busy deck; mix,
  retarder or pour rate changed on the day without telling the form designer
- Back-props removed early to feed the floor above; stripping on day count
  rather than verified strength
- Program pressure makes the certificate a formality. Make it the trigger:
  the pump and concrete order is released only when the PC holds the signed
  certificate, so the system, not an individual's courage, stops the pour

### Practical implications for FM / contract portfolios
- A suspended slab, ramp, plinth or stair poured in a refurbishment or minor
  works package is formwork: ask for the certified drawing and the pre-pour
  certificate, whatever the contract value
- Pre-qualification question for concrete subcontractors: who designs your
  formwork, who certifies it as built, and show the last three certificates
- Record permit-to-load and strip approvals in the project file; they are the
  first documents an inspector asks for after a collapse

---

## 9. Occupational Diving

### Regulatory basis
Model WHS Regs Part 4.8 (regs 167–184). AS/NZS 2299.1:2015 *Occupational
diving operations — Standard operational practice* is mandatory for high
risk diving work (reg 183) and the benchmark for all other diving; Part 2
(scientific diving) and Part 3 (recreational industry diving and
snorkelling operations) are the sector benchmarks. AS/NZS 2815 (training
and certification of occupational divers) is delivered through the
Australian Diver Accreditation Scheme (ADAS). There is no model Code of
Practice; Queensland's approved Occupational Diving Work Code of Practice
2005 (last varied 1 July 2018; as at October 2026) must be followed or
matched (WHS Act 2011 (Qld) s 26A — `legislation.md` §8).

Part 4.8 covers work in or under water (or, for high risk diving work, any
other liquid) **while breathing compressed gas**. Snorkelling and
breath-hold diving fall under the primary duty (WHS Act s 19), except that
Queensland regulates recreational dive and snorkel services separately
(QLD dive tourism row).

### Classify the work first (reg 5 definitions)
| Category | Test | Diver competence |
|---|---|---|
| **High risk diving work** | In water **or any other liquid**, involving construction work; testing, maintenance or repair of a structure, however minor; inspection to decide whether that work is needed; or commercial recovery or salvage of a large structure or plant item. Excludes only minor cleaning, inspecting, maintaining or searching for a vessel or mooring in the sea, a bay, inlet or marina | Qualifications, knowledge, skills and experience required by AS/NZS 2299.1:2015 (reg 184) — in practice an ADAS card matching the mode and depth |
| **General diving work** | All other compressed-gas work under water — aquaculture, minor hull or mooring work in the sea, a bay, inlet or marina, dive instruction and guiding, aquarium, film, fisheries | Certificate from a training organisation showing the AS/NZS 2815 competencies relevant to that type of diving (reg 171), plus the knowledge and skill listed in reg 171A |
| **Incidental diving work** | General diving incidental to the business (the actor in an underwater scene); limited diving only | Reg 171A knowledge and skill; 15 logged hours, at least 8 h 20 min of them between 10 m above and any depth below the planned maximum depth; accompanied and supervised in the water by a reg 171-qualified diver (reg 172) |
| **Limited scientific diving work** | Professional scientific research, natural resource management, or research as an educational activity; limited diving only | Reg 171A knowledge and skill; divers not permanently resident in Australia also need 60 logged hours, with the same 8 h 20 min depth band (reg 173) |

**Limited diving** involves none of: depth below 30 m; a decompression
stop; mechanical lifting equipment or a buoyancy lifting device; diving
beneath anything that forces the diver sideways before ascending; plant
powered from the surface; more than 28 days of diving in any 6 months.
One of these and the incidental and scientific concessions are gone.

Classification traps:
- Minor work is no way out: reg 289 drops minor testing, maintenance and
  repair from construction work, but the high risk definition takes it
  back. Tank, reservoir, dam, intake and pontoon inspections land here. A
  ship is a structure (reg 290), so hull work outside the carve-out
  waters, or beyond minor work, is high risk diving work
- "Any other liquid" is only in the high risk definition: structure work
  in sewage or process liquid is high risk diving work
- Diving in construction work is high risk construction work (reg 291;
  Victoria's list too) — SWMS as well as the dive plan (`hazards.md` §8)

### Duties of the PCBU — general diving work (Part 4.8 Div 2–3)
| Reg | Duty | Keep the record |
|---|---|---|
| 168–170 | Worker holds a current certificate of medical fitness — issued within the past 12 months by a registered medical practitioner with training in underwater medicine, against the fitness criteria in AS/NZS 2299.1:2015 Appendix M. Applies to training dives. Conditions on the certificate bind the work | 1 year after the work |
| 175 | Sight written evidence of competence — diver and supervisor — before directing or allowing the work | 1 year |
| 176 | Risk assessment by a competent person, in writing | 28 days after the work; 2 years after a notifiable incident |
| 177, 174 | Appoint one or more competent persons to supervise: reg 171 qualification plus experience in the type of diving | — |
| 178–179 | Dive plan prepared by the supervisor: method; tasks and duties of each person; equipment, breathing gases and procedures; dive times, bottom times and decompression profiles; hazards and controls; emergency procedures. Supervisor briefs the team before the dive | Until the work is complete; 2 years after a notifiable incident |
| 180–181 | Dive safety log for every dive: divers, supervisor, date, location, time in and out, maximum depth, any incident, difficulty, discomfort or injury, dive computer or table data, gas details for EANx or mixed gas. Diver and supervisor verify each return. From a vessel, the supervisor logs a headcount before diving starts and before the vessel leaves | 1 year after the last entry |
| 182 | Risk assessment and dive plan readily accessible to the divers and available to an inspector | For as long as kept |

### High risk diving work (Part 4.8 Div 4)
Fitness, competence and the conduct of the work must all accord with
AS/NZS 2299.1:2015 (reg 183), which makes the standard's rules on team
size, standby diver, breathing apparatus, communications and chamber
access enforceable. "We comply with 2299" is not evidence. The dive plan
must name, for this dive: each role (supervisor, diver, standby diver,
tender) with no one holding two; breathing mode and bailout;
communications; decompression tables or computer; abort limits for
current, visibility and weather; chamber, transport mode and transit time.

### Hierarchy of controls
| Level | Application |
|---|---|
| Elimination | ROV, drop camera, drain-down or dewatering; design intakes, screens and tanks for dry inspection |
| Substitution | Surface-supplied diving with hard-wire communications in place of SCUBA for structure work |
| Isolation | Lock out intakes, pumps, valves, thrusters, impressed-current cathodic protection and dosing; equalise differential pressure; exclude vessel traffic |
| Engineering | Bailout gas, CO monitoring on the air supply, diver recovery stage or davit |
| Administrative | Dive plan, appointed supervisor, standby diver, repetitive-dive and roster limits, headcount |
| PPE | Helmet or mask, suit and thermal protection — the last line, never the control plan |

Reg 36(3) puts isolation with substitution and engineering; apply each SFAIRP.

### Reading an ADAS card
| Card | Training standard | Scope |
|---|---|---|
| Part 1 (1R restricted) | AS/NZS 2815.1 (2815.6 for restricted) | Occupational SCUBA to 30 m |
| Aquarium | AS/NZS 2815.6 | Occupational SCUBA to 20 m |
| Part 2 (2R restricted) | AS/NZS 2815.2 | Surface-supplied (SSBA) to 30 m |
| Aquaculture | AS/NZS 2815.2 | SSBA to 30 m, aquaculture |
| Part 3 (3R restricted) | AS/NZS 2815.3 | SSBA to 50 m |
| Part 4 | AS/NZS 2815.4 | Closed bell |
| Onshore supervisor | AS/NZS 2815.5 | SCUBA to 30 m, SSBA to 30 m or SSBA to 50 m |
| Offshore supervisor | OPGGS requirements | SSBA to 50 m or closed bell |

A recreational instructor or divemaster card is not, on its face, AS/NZS
2815 evidence. Hookah is surface-supplied: it needs an SSBA card, not SCUBA.

### Jurisdiction variations (as at October 2026)
| Jurisdiction | Position |
|---|---|
| ACT, NSW, NT, TAS, WA | Part 4.8 in the current model form described above: WHS Regulation 2011 (ACT) ss 167–184; WHS Regulation 2025 (NSW) Part 4.8; WHS (National Uniform Legislation) Regulations 2011 (NT), amended by SL No. 22 of 2019; WHS Regulations 2022 (Tas); WHS (General) Regulations 2022 (WA) |
| QLD | WHS Regulation 2011 (Qld) keeps the earlier competence rule: s 171(a) accepts a VET statement of attainment or a certificate covering the subject areas of AS/NZS 4005.2:2000 (recreational SCUBA dive supervisor); s 171(b) carries the knowledge-and-skill list (no s 171A); s 173 applies only to non-resident divers; in-water supervision for incidental diving sits in the sch 19 definition, not s 172. Sections 183–184 cite AS/NZS 2299.1:2015. Approved code: see Regulatory basis |
| QLD dive tourism | Operators providing recreational diving, recreational technical diving or snorkelling are also regulated by the Safety in Recreational Water Activities Act 2011 (Qld), the Safety in Recreational Water Activities Regulation 2024 and the Recreational Diving, Recreational Technical Diving and Snorkelling Code of Practice 2024 (both commenced 1 August 2024; the code replaced the 2018 code) |
| Cth | WHS Regulations 2011 (Cth) keep the earlier model text: reg 171(3) accepts AS/NZS 4005.2:2000 or AS/NZS 2815; reg 173 applies only to non-residents; regs 183–184 cite AS/NZS 2299.1:2007. Reg 183(2)–(3) lets the regulator approve a separate standard for Defence Force high risk diving |
| SA | WHS Regulations 2012 (SA) Part 4.8. Read reg 171 (does it still accept AS/NZS 4005.2?) and the AS/NZS 2299.1 edition in regs 183–184 before applying the model description |
| VIC | No Part 4.8 equivalent in the OHS Regulations 2017 (Vic). Construction work involving diving is high risk construction work under those Regulations and needs a SWMS (`hazards.md` §8). Otherwise OHS Act 2004 ss 21 and 23 apply; AS/NZS 2299.1 is the practical measure of what is reasonably practicable |
| Offshore petroleum (Cth) | OPGGS (Safety) Regulations 2024: NOPSEMA accepts the diving contractor's diving safety management system (DSMS); the operator of the diving project approves the diving project plan (DPP), or NOPSEMA accepts it where there is no operator; a dive start-up notice goes to NOPSEMA ahead of the project, within the lead time on NOPSEMA's current form; divers and supervisors hold ADAS accreditation appropriate to the work. See `sector-regimes.md` §3 |
| WA petroleum and geothermal | WHS (Petroleum and Geothermal Energy Operations) Regulations 2022 (WA) — DSMS and DPP required before diving |

### New Zealand — certificate of competence (as at October 2026)
- Every diver using compressed gas holds a WorkSafe certificate of
  competence (CoC) in the category dived and is medically fit (Health and
  Safety in Employment Regulations 1995 regs 48–49, as cited by WorkSafe)
- Categories: construction (Parts 1–4; ADAS cards are one route),
  scientific, instruction/tutor, tourism, aquaculture, film and photographic
- Valid 5 years with an annual diving medical clearance from the Diving
  Hyperbaric Medicine Service (DHMS); full examination by a Designated
  Diving Doctor every 5 years or sooner if DHMS requires
- Trainees: direct supervision by a CoC holder in the category, 6 months
  maximum, never the standby diver (WorkSafe technical bulletin, March 2025)
- Construction diving is particular hazardous work under the same
  Regulations: notify WorkSafe before it starts
- Tourism and instruction may need an HSW (Adventure Activities)
  Regulations 2016 safety audit; offshore petroleum diving sits under the
  HSW (Petroleum Exploration and Extraction) Regulations 2016. Snorkellers
  and free-divers need no CoC; HSWA s 36 still applies

### Aquaculture, pearl, abalone and dive tourism
Usually general diving work (QLD dive tourism also has its own regime),
often on hookah — low-pressure surface-supplied air. The risk is set by how
the work is organised, not by diver skill:
- Repeated short dives and ascents ("yo-yo" profiles) across multi-day
  rosters, and piece rates that reward bottom time, drive decompression
  stress. Fix the roster and the pay before blaming the diver's profile
- Surface-powered tools (hydraulic, pneumatic, water-jet) end limited
  diving. Whether a hookah compressor is itself "plant that is powered
  from the surface" (reg 5) is untested — get the regulator's view before
  relying on the incidental or scientific concession with hookah
- Carbon monoxide: intake upwind and clear of engine exhaust, filters
  changed on schedule, CO monitoring on the supply, air tested at least
  every three months (WorkSafe WA general diving checklist)
- Vessel headcounts (reg 181) exist because divers have been left in the
  water. Count heads on deck, not names on a list

### Decompression illness and emergency arrangements
- Decompression illness (DCI: decompression sickness and arterial gas
  embolism) can appear hours after surfacing. Any post-dive symptom — joint
  pain, tingling, rash, unusual fatigue, dizziness — is DCI until a diving
  doctor says otherwise
- First aid: lie the diver flat; highest oxygen concentration available
  (demand valve first, non-rebreather mask at 15 L/min if they cannot use
  one); oral fluids only if conscious and able to swallow; keep warm. Call
  000 (111 in NZ), then the Divers Emergency Service (DES) — the dive plan
  carries the current number. Never recompress in the water
- Oxygen for the full transit to definitive care, with someone trained to
  give it (HLTAID015 — `workplace-controls.md` §1). Remote sites: the dive
  plan names the evacuation route, the nearest chamber that accepts
  emergency divers and the transit time. Retrieval over high ground or by
  unpressurised aircraft worsens DCI
- No flight or drive home over high ground until the interval set by the
  tables or computer in use has passed; on FIFO rosters, roster it
- DCI needing immediate in-patient hospital treatment is notifiable (WHS
  Act ss 36, 38; OHS Act 2004 (Vic) ss 37–38; HSWA ss 23, 56 —
  `legislation.md` §5). Secure the dive computer, log and breathing gas
- Chamber staff are pressure-exposed too — AS 4774.2 (hyperbaric facilities)

### Engaging a diving contractor — client PCBU checklist
- [ ] Elimination tested first: ROV, drop camera, drain-down, dewatering
- [ ] Work classified by you, not the contractor: construction, or
      testing, maintenance or repair of a structure however minor, or an
      inspection to decide on it, is high risk diving work
- [ ] Sighted: medical certificates (within 12 months), cards matching
      mode and depth, supervisor's qualification and written appointment;
      risk assessment and dive plan reviewed; SWMS for construction work
- [ ] Your isolations locked out under permit before the diver enters
      (`hazards.md` §10) — differential pressure kills without warning
- [ ] Vessels, other contractors and the public coordinated (WHS Act s 46)
- [ ] Emergency arrangements demonstrated, not described: standby diver
      dressed, oxygen on site, unconscious-diver recovery, chamber route
- [ ] Dive safety log and any incident report obtained at close-out

### Common failure modes
- Tank, dam or sewage diving let as general diving work to a
  recreationally trained diver
- Medical certificate expired or issued without underwater medicine training
- Supervisor doubling as standby diver, skipper or tender: no one supervises
- Symptoms hidden because a DCI call ends the job and the income. Pay for
  the precautionary assessment; treat early reporting as the system working

### Practical implications for FM / contract portfolios
- Reservoirs, cooling-water intakes, pontoons and marina assets are usually
  let as maintenance; diving on them is high risk diving work, so scope,
  price and prequalification must say so

---

## 10. Q Fever and Zoonoses

### Regulatory basis
The model WHS Regulations have no biological-hazards Part. The hooks are the
duty to eliminate or minimise risk so far as is reasonably practicable (model
WHS Act ss 17, 19(1); hierarchy in model WHS Regs reg 36), facilities and PPE
(regs 41, 44–46) and incident notification (ss 35–38, reg 699). Statutory
health monitoring covers only hazardous chemicals, lead and asbestos (Parts
7.1, 7.2, 8.5), so immunity screening rests on s 19(3)(g), and vaccination and
exclusion on the SFAIRP duty. Consult workers and HSRs on the rules before
they start (ss 47–49). VIC: OHS Act 2004 ss 21–23, 35. NZ: HSWA 2015 ss 30,
36, 58. Clinical rules come from the *Australian Immunisation Handbook* and
the Q-VAX Product Information; the animal side sits under biosecurity law.

### Notification — who tells whom
| Trigger | Provision | Who notifies |
|---|---|---|
| Any infection to which work is a significant contributing factor — work with micro-organisms; treatment or care of a person; human blood or body substances; animals, hides, skins, wool, hair, carcasses or animal waste | Model reg 699(a) | PCBU → WHS regulator, immediately on becoming aware (s 38) |
| Listed occupational zoonoses from animal-contact work: **Q fever, anthrax, leptospirosis, brucellosis, Hendra virus, avian influenza, psittacosis** | Model reg 699(b) | As above |
| Medical treatment within 48 hours of exposure to a substance — regulator guidance reads "substance" to include human and animal blood and body substances | Model WHS Act s 36(c) as enacted in the jurisdictions (as at October 2026) | As above |
| NZ: serious infection (including occupational zoonoses) to which work is a significant contributing factor; the list adds handling fish or marine mammals | HSWA s 23(1)(d) | PCBU → WorkSafe NZ (s 56) |
| Human case of a notifiable disease | Public health Acts (e.g. Public Health Act 2010 (NSW)); Health Act 1956 (NZ) | Doctor or laboratory → public health unit; not a PCBU duty |
| AU: suspect Hendra, anthrax or avian influenza in animals | State and territory biosecurity legislation | Anyone → Emergency Animal Disease Hotline 1800 675 888 |
| NZ: suspect exotic or notifiable animal disease, including avian influenza | Biosecurity Act 1993 (NZ) duty to inform MPI | Anyone → MPI Exotic Pest and Disease Hotline (number on mpi.govt.nz) |

- Reg 699 deems the infection a serious illness — no hospital-admission
  threshold; a GP-managed Q fever case is notifiable once the PCBU knows of
  it. Reg 699(b) covers animal-contact work and any avian influenza strain (H7
  included); reg 699(a) covers dust-only exposure (mowing near stock), ABLV and
  Japanese encephalitis where work is a significant contributing factor.
- A bat bite or scratch given medical treatment within 48 hours falls within
  s 36(c) before any infection exists; treat a body-fluid splash from a
  suspect Hendra horse that leads to medical treatment the same way.
- Harmonised regulations use the model numbering (QLD checked; NSW remade its
  Regulation in 2025 — confirm locally). VIC has no reg 699: OHS Act 2004 s 37
  turns on death, in-patient or 48-hour post-exposure medical treatment.
- AU reform: Safe Work Australia's 5 December 2025 model WHS Act amendments
  add violent incidents, notifiable suicides and absences of 15 or more
  consecutive days, and extend the 48-hour limb to treatment by registered
  medical, nursing or paramedicine professionals. They bind only once a
  jurisdiction adopts them (as at October 2026) — check the local Act.
- NZ: the HSWA Amendment Act 2026 commences 1 April 2027 (as at October
  2026; `legislation.md` §3) — recheck ss 23 and 56 from that date.

### Q fever — agent and at-risk work
- **Agent and route**: *Coxiella burnetii*, shed in birth products, urine,
  faeces and milk of cattle, sheep and goats (kangaroos and other animals
  also carry it), inhaled in dust and aerosols. It survives in dust and soil
  for months to years, so people with no animal contact are infected.
- **Course**: incubation 2–3 weeks (range 4 days to 6 weeks); many
  infections are mild or silent; about 10–20% of people who fall ill still
  have post Q fever fatigue at 12 months; chronic infection (heart valves,
  bone, joints) can emerge up to 2 years later. *C. burnetii* is not
  established in NZ — NZ-based workers are exposed on Australian deployments.

| Work | Why it is at risk |
|---|---|
| Abattoirs, meat processing, rendering, skin sheds | Birth products, offal and hides; site-wide aerosol reaches maintenance, office, cleaning and labour-hire staff |
| Shearing, wool classing, stock transport, saleyards, feedlots, dairies (cattle, goat, sheep) | Dust from fleece, manure, yards and truck wash-out |
| Veterinary practice, vet and agricultural students, laboratories | Birthing, caesareans, post-mortems, specimens |
| Wildlife and zoo work, kangaroo harvesting and processing, feral animal shooting | Carcass dressing; macropods are a reservoir |
| Agricultural contractors, fencers, mowing and slashing crews, council and emergency services workers | Contaminated dust, no animal contact needed |
| Visitors, auditors, drivers and trades entering any of the above | Same air, no immunity |

### Screening, vaccination and exclusion
1. **Check for evidence first** — the worker's AIR immunisation history
   statement (Q-VAX doses and natural immunity reported from 15 April 2024),
   an eStatement or card from the former Australian Q Fever Register, or the
   doctor's screening record. The Register (AMPC-owned, administered by
   AUS-MEAT) took no reports after 15 April 2024 and closed to individuals on
   30 June 2025; AIR holds older records only if a provider re-reported them,
   and has no employer look-up. Documented infection, positive screen or
   prior vaccination: no screening, no vaccine. Unrecorded claim of past
   vaccination: the doctor reviews — never straight to the vaccine.
2. **No evidence** — pre-vaccination screening by a medical practitioner:
   exposure history, serology **and** skin test, read at day 7.
3. **Either test positive** — already sensitised. Do not vaccinate (serious
   hypersensitivity reactions); record as immune.
4. **Equivocal skin test or borderline serology** — not proof of immunity.
   The doctor decides with the worker whether to vaccinate; until written
   clearance, treat them as non-immune and keep them out of risk areas.
5. **Both negative** — one dose of Q-VAX, never repeated. Recommended from
   age 15 (*Australian Immunisation Handbook*); contraindicated with
   hypersensitivity to egg proteins or any vaccine component; specialist
   advice if immunocompromised. Deferred in pregnancy — reassess exposure
   for non-immune pregnant workers (`diversity-inclusion.md` §2).
6. **Exclude from risk areas until 15 days after vaccination.** Lead time:
   screen day 0, read and vaccinate day 7, earliest start day 22 — a
   minimum, not a plan. Book only with a clinic that holds Q-VAX stock.
7. **Record the result** — the provider reports to AIR; with consent, keep a
   copy of the worker's evidence and clearance date on the confidential file.

Program design points:
- **Who pays**: the PCBU — workers pay nothing for screening or vaccine
  (model WHS Act s 273; HSWA s 27); book it in paid time. s 273 does not
  squarely reach applicants screened before engagement — pay anyway. Q-VAX
  is not National Immunisation Program funded (as at September 2025).
- **Scope**: everyone entering a risk area — labour hire, contractors,
  drivers, students, visitors; host and supplier PCBUs settle who screens
  (s 46) and the host checks evidence before first entry.
- **Cannot or will not be vaccinated** (under 15, contraindicated,
  declines): exclusion from risk areas is the control, and a respirator is
  no substitute. Redeploy before disciplining — a direction to vaccinate
  must be lawful and reasonable, and disability or pregnancy engages
  anti-discrimination law. No under-15 work experience in risk areas.
- **Privacy**: immune status is health information. The Privacy Act 1988
  (Cth) employee records exemption (s 7B(3)) does not reach contractors,
  labour hire or visitors; state health records laws also apply (e.g. Health
  Records Act 2001 (Vic)); NZ: Health Information Privacy Code 2020.

### Other zoonoses — quick reference
| Disease | Source and at-risk work | Controls and traps |
|---|---|---|
| **Leptospirosis** (reg 699(b)) | Urine of cattle, pigs and rodents, via cuts and mucous membranes; dairy and meat workers, cane and banana farms, sewer work. NZ: farmers, farm service workers, abattoir and meat processing workers, plumbers, sewer workers, drain layers, miners | Herd vaccination, effluent and rodent control, covered cuts, splash protection in the milking shed. Incubation 5–14 days (range 2–30); cases rise after floods |
| **Brucellosis** (reg 699(b)) | *Brucella suis* in feral pigs — widespread in QLD, present in northern NSW; pig hunters, their dogs, game-meat handlers. *B. abortus* eradicated in 1989 | No bare-skin contact with blood or tissue when dressing carcasses; cover cuts; no raw feral pig fed to dogs. Incubation 5–60 days |
| **Hendra virus** (reg 699(b)) | Flying fox → horse → human. Seven human cases, four deaths, the latest in 2009 (as at May 2026), all after heavy exposure to body fluids of a sick horse | Vaccinate horses. Treat any sick horse as a Hendra suspect until a test excludes it: isolate it, keep non-essential people away, defer invasive and high-exposure procedures (post-mortem included) until the result is back; anyone who must attend wears PPE. Vets: Biosecurity Queensland, *Hendra virus information for veterinarians*. No human vaccine. Incubation 5–21 days |
| **Australian bat lyssavirus** | Any Australian bat, by bite or scratch. Four human cases since 1996 (three QLD, one NSW), all fatal (as at November 2025) | Only rabies-vaccinated, trained handlers touch bats. Wash the wound with soap and water for at least 15 minutes and see a doctor the same day; post-exposure treatment starts as soon as practicable and is still given after any delay |
| **Psittacosis** (reg 699(b)) | *Chlamydia psittaci* in dried droppings and feather dust; pet shops, aviaries, poultry processing, wildlife carers, zoos, vets; horse studs and equine vets handling aborted material, abnormal placentas or sick foals | Dampen droppings before cleaning; P2 and gloves. Incubation 5 days to 4 weeks |
| **Anthrax** (reg 699(b)) | Soil spores; sporadic livestock deaths, historically central NSW into northern VIC; human disease is rare and usually cutaneous | Never open or move a suspect carcass; report it; vaccinate stock where advised |
| **Japanese encephalitis** | Mosquito-borne; pigs amplify the virus; detected in mainland piggeries from 2022 | JE vaccine for those at highest risk — state programs fund defined groups (as at December 2025); mosquito control, repellent, long sleeves |

### Avian influenza H5 — status as at September 2026
H5N1 (clade 2.3.4.4b) was first confirmed on mainland Australia on 20 June
2026 in wild birds in WA, after detections on Heard Island from October
2025. As at 7 September 2026 Wildlife Health Australia recorded it in wild
birds in all six states and in a small number of marine and terrestrial
mammals, with no detection in poultry or the agricultural system. No locally
acquired human case has been reported; NSW Health rates the public risk as
low (as at 25 September 2026). NZ confirmed its first H5 detections in wild
birds in July 2026. Recheck agriculture.gov.au/birdflu and mpi.govt.nz.

- **Exposed work**: poultry, wildlife care, rangers, marine mammal response,
  vets, and council or grounds crews who find dead birds. Untrained staff:
  avoid, record, report — EAD Hotline (AU), MPI hotline (NZ).
- **Authorised handling**: P2/N95, goggles, gloves, protective clothing;
  seasonal influenza vaccination (cuts co-infection risk, not H5 risk).
- **After exposure**: symptoms appear in 2–10 days; the worker tells the
  doctor about the exposure, and the public health unit advises on testing
  and antivirals. A work-acquired case is notifiable (reg 699(b)).

### Hierarchy of controls
| Level | Application |
|---|---|
| Elimination (including at the animal) | Keep non-essential people out of risk areas; no necropsy of suspect Hendra or anthrax cases; untrained staff never handle bats, sick or dead wild birds or marine mammals. Remove the agent at the animal: vaccinate horses (Hendra), herds (leptospirosis) and stock in anthrax districts; control rodents and mosquitoes |
| Isolation | Separate birthing, offal, skins and rendering areas; isolate sick animals; launder on site so contaminated clothing stays out of homes |
| Engineering | Ventilation and dust suppression in yards, sheds and truck wash-out; low-pressure wet-down, not high-pressure hosing; filtered enclosed cabs for manure and yard clearing; hand-wash stations at exits |
| Administrative | Immunity screening and vaccination; exclusion rules; induction on symptoms and "tell your doctor what you work with"; covered cuts; no eating or smoking in animal areas |
| PPE | Fit-tested P2 for dust and aerosol tasks (`specialist-topics.md` §1); gloves, eye protection, waterproof apron and boots for birthing, urine, blood and carcass work. Last line only — never a stand-in for Q fever immunity |

### Two or more cases at one site
Call the public health unit, which leads case finding. Find the exposure
point (truck wash-out, birthing pen, effluent pond, a mowing job) rather
than assuming the obvious area; re-check immune evidence for everyone who
entered, labour hire, drivers and visitors included; confirm each case was
notified (reg 699; NZ s 23); investigate the program, not the workers
(`investigation.md` §1).

### Workers compensation
- A work-acquired zoonosis is a disease claim, decided on the scheme's
  disease-causation test (`compensation-rtw.md` §3). NZ: ACC covers
  work-related disease or infection (Accident Compensation Act 2001 s 30;
  `compensation-rtw.md` §4).
- Screening results fix immune status at engagement — keep them. Post Q
  fever fatigue drives long-duration claims (`compensation-rtw.md` §8). The
  reg 699 notification and the claim are separate obligations
  (`compensation-rtw.md` §1; `legislation.md` §5).

### Common failure modes
- Screening booked the week before the season starts: the 22-day lead time
  is missed and a non-immune worker starts "in a mask"
- Vaccinating without the skin test, or re-vaccinating because a record was
  lost — ask for the AIR statement or old Register eStatement first
- Borderline serology filed as immune
- Program covers employees but not labour hire, drivers, trades or visitors
- Diagnosis arrives weeks later as a medical certificate or claim form and
  never reaches the person who makes reg 699 notifications

### Practical implications for FM / contract portfolios
- Grounds and mowing crews on rural, saleyard or peri-urban sites with stock
  or kangaroos: dust exposure without animal contact — assess for Q-VAX
- Roof-space, pest-control and building trades: bats (ABLV) and bird roosts
  (psittacosis) — stop-work rule for bats; wet methods and P2 for droppings
- Sewer, stormwater and waste crews: leptospirosis from rodent urine
- Maintenance contracts into abattoirs, rendering plants and saleyards: the
  host's immunity rule binds — build the 22 days into mobilisation
- Coastal, wetland and park sites: avoid, record, report for dead birds and
  marine mammals. Agriculture sector context: `sector-regimes.md` §10

---

> For organisation-specific critical risk taxonomy, control standards, and
> verification cadence applicable to these hazards, load `references/company.md`.

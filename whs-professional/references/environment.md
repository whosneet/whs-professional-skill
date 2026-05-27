# Environment Reference — AU/NZ Environmental Regulation, ISO 14001, EHS Integration

This file covers the environmental side of EHS (Environment, Health and Safety). Most
AU/NZ WHS roles at coordinator-through-manager level carry concurrent environmental
accountability — incident classification matrices treat environment as a consequence
dimension alongside health and safety, ISO 45001 implementations sit alongside
ISO 14001 in integrated management systems, and the same regulators (in some
jurisdictions, the same inspectors) examine both. Treating environment as a
separate discipline that lives outside WHS is operationally and legally untenable
for most contemporary roles.

The skill is named "WHS Professional" because that is the dominant terminology in
the AU/NZ market, but the content here completes the EHS picture. Load this file
alongside `references/hazards.md` (hazardous chemicals, asbestos, construction)
and `references/legislation.md` (where environmental notifications intersect with
WHS regulator reporting). For organisation-specific environmental consequence
ratings, internal classification thresholds, and reporting cadence, load
`references/company.md`.

---

## Table of Contents
1. [Scope and EHS Integration](#1-scope-and-ehs-integration)
2. [AU Environmental Regulatory Framework](#2-au-environmental-regulatory-framework)
3. [NZ Environmental Regulatory Framework](#3-nz-environmental-regulatory-framework)
4. [ISO 14001:2015 EMS Clause Map](#4-iso-14001-2015-ems-clause-map)
5. [Environmental Aspects and Impacts](#5-environmental-aspects-and-impacts)
6. [Environmental Incident Classification & Notification](#6-environmental-incident-classification--notification)
7. [Hazardous Chemicals & Dangerous Goods — Storage](#7-hazardous-chemicals--dangerous-goods-storage)
8. [Spill Response and Site Contamination](#8-spill-response-and-site-contamination)
9. [Waste Management Hierarchy & Tracked Waste](#9-waste-management-hierarchy--tracked-waste)
10. [Air Emissions and Water Discharge](#10-air-emissions-and-water-discharge)
11. [Biodiversity and Heritage](#11-biodiversity-and-heritage)
12. [Climate Change — WHS Intersection](#12-climate-change--whs-intersection)
13. [Environmental Output Checklist](#13-environmental-output-checklist)

---

## 1. Scope and EHS Integration

### What this file covers
Environmental regulation, environmental management systems, and the operational
environmental obligations that fall to WHS/EHS practitioners. Specifically:
- Commonwealth and state environmental legislation in Australia
- New Zealand environmental framework (RMA, NZ ETS, regional councils)
- ISO 14001:2015 environmental management system
- Environmental aspects/impacts identification
- Environmental incident classification, notification thresholds, regulator engagement
- Hazardous chemicals storage (environmental aspects — bunding, placarding, manifests)
- Spill response and contaminated land
- Waste management hierarchy and tracked/regulated waste
- Air, water and noise emissions licensing
- Biodiversity, heritage and pre-construction surveys
- Climate change adaptation that intersects with WHS (heat, smoke, extreme weather)

### What this file does NOT cover
- Sustainability reporting (GRI, SASB, TCFD, ISSB) — these are corporate reporting
  frameworks, not operational environmental management. Some overlap with NGER
  Scope 1+2+3 below, but full sustainability disclosure is out of scope.
- Carbon accounting methodology beyond NGER thresholds
- Detailed contaminated land remediation engineering (load specialist consultants)

### Why this matters for WHS roles
- Most incident classification matrices treat environment as a consequence
  dimension ([organisation] [incident system] uses 1–6 across H&S, Environment, Plant/Property,
  Legal/Compliance — see `company.md` §5). A WHS investigator who cannot
  classify environmental consequence cannot complete the matrix.
- Notifiable environmental incidents must be reported within hours under most
  state EPA Acts — the same incident often triggers parallel WHS regulator
  notification. The two notifications are not the same and cannot be substituted.
- ISO 45001 implementations almost always sit inside an integrated management
  system covering ISO 14001 (environment) and ISO 9001 (quality). Auditors
  expect integrated thinking, not parallel siloes.
- Officer due diligence (s 27 model WHS Act) does not extend to environment in
  most jurisdictions — but parallel director duties under the Corporations Act
  2001 and specific environment legislation (e.g. NSW POEO Act s 169) do create
  personal liability for directors and "executive officers" for environmental
  breaches. Officers need to understand both regimes.

---

## 2. AU Environmental Regulatory Framework

Australia has a layered environmental regulatory system: Commonwealth law deals
with matters of national environmental significance and federally regulated
substances; state and territory law carries the bulk of operational obligations
(licensing, pollution, waste, contaminated land); local government delivers
environmental health functions (food safety, public health nuisance, on-site
sewage management).

### 2.1 Commonwealth — Environment Protection and Biodiversity Conservation Act 1999 (EPBC Act)

The EPBC Act regulates actions that have, or are likely to have, a significant
impact on a **Matter of National Environmental Significance (MNES)**. There are
nine MNES:

1. World Heritage properties
2. National Heritage places
3. Wetlands of international importance (Ramsar wetlands)
4. Listed threatened species and ecological communities
5. Listed migratory species (under international treaties: JAMBA, CAMBA, ROKAMBA, Bonn)
6. Commonwealth marine areas
7. The Great Barrier Reef Marine Park
8. Nuclear actions (uranium mining, large-scale disposal, nuclear installations)
9. A water resource, in relation to coal seam gas development and large coal mining
   development (the "water trigger", added 2013)

**Controlled action** = action likely to have a significant impact on an MNES;
requires assessment and approval under Part 9 of the EPBC Act. Penalties for
unauthorised controlled actions are severe (civil penalty up to $13.75M for a
body corporate as at the 2024 indexation; criminal offence carries imprisonment
for individuals).

**Practical implications for FM and construction portfolios**:
- Greenfield civil and construction works require an EPBC referral if MNES are
  potentially affected; engage a qualified ecologist before scoping the project
- Refurbishment of heritage-listed buildings (National Heritage List or
  Commonwealth Heritage List) may require EPBC approval
- Defence base infrastructure projects routinely engage with EPBC pathways
  (Commonwealth land + threatened species often present)

### 2.2 Commonwealth — National Greenhouse and Energy Reporting Act 2007 (NGER)

NGER establishes mandatory reporting of greenhouse gas (GHG) emissions, energy
production, and energy consumption for corporations whose activities exceed a
threshold. Administered by the **Clean Energy Regulator**.

**Reporting thresholds** (per corporation, per financial year):
- Facility threshold: 25,000 tonnes CO₂-e Scope 1+2; or 100 TJ energy produced;
  or 100 TJ energy consumed
- Corporate group threshold: 50,000 tonnes CO₂-e Scope 1+2; or 200 TJ energy
  produced; or 200 TJ energy consumed

**Scope definitions** (Greenhouse Gas Protocol, adopted by NGER):
- **Scope 1**: Direct emissions from sources owned/controlled by the entity —
  fuel combustion, fugitive emissions, industrial processes
- **Scope 2**: Indirect emissions from purchased electricity, steam, heating,
  cooling
- **Scope 3**: All other indirect emissions in the value chain — supplier
  emissions, leased assets, business travel, end-use, waste disposal. NGER does
  not mandate Scope 3 reporting but most corporates now disclose it voluntarily
  under TCFD/ISSB frameworks

**Safeguard Mechanism** (2016, reformed 2023): Facilities with >100,000 tCO₂-e
Scope 1 emissions must hold emissions below a declining baseline; excess
emissions must be offset with Australian Carbon Credit Units (ACCUs) or Safeguard
Mechanism Credits (SMCs). The 2023 reforms tightened baselines and introduced
a downward trajectory aligned with net zero by 2050.

### 2.3 Commonwealth — National Pollutant Inventory (NPI)

The NPI requires facilities that exceed specific reporting thresholds (per
substance, per facility) to report annual emissions of 93 listed substances to
air, water, and land. Administered by DCCEEW under the **National Environment
Protection (National Pollutant Inventory) Measure 1998**.

**Thresholds** vary by substance — three categories:
- **Category 1**: based on quantity used, produced or stored (e.g. 10 tonnes
  per year for most Category 1 substances)
- **Category 1a**: total VOCs (25 tonnes per year)
- **Category 2a/2b**: fuel use thresholds for combustion-derived emissions
- **Category 3**: total nitrogen and total phosphorus discharged to water

Reports are public and searchable at npi.gov.au. FM operators of large depots,
hospitals, and base estates should check whether NPI thresholds are tripped —
common triggers include diesel consumption, refrigerant releases, and
groundskeeping chemical use.

### 2.4 Commonwealth — National Environment Protection Measures (NEPMs)

NEPMs are nationally agreed standards made under the **National Environment
Protection Council Act 1994**. They set outcomes that state/territory legislation
must implement. Key NEPMs:

| NEPM | Scope |
|---|---|
| Ambient Air Quality NEPM | Air quality standards for SO₂, NO₂, CO, O₃, PM₁₀, PM₂.₅, lead — used by EPAs to define exceedances |
| Air Toxics NEPM | Monitoring program for benzene, formaldehyde, toluene, xylenes, PAHs, BaP |
| Assessment of Site Contamination NEPM (ASC NEPM 2013) | The national framework for contaminated land investigation, assessment, and remediation — see §8 |
| Diesel Vehicle Emissions NEPM | Standards for in-service heavy diesel vehicles |
| Movement of Controlled Waste NEPM | Tracking framework for interstate movement of regulated/hazardous waste — see §9 |
| National Pollutant Inventory NEPM | Establishes NPI reporting (see §2.3) |
| Used Packaging Materials NEPM | Packaging covenant; product stewardship for packaging |

### 2.5 State and Territory Environmental Acts

| Jurisdiction | Primary Act | Regulator | Notes |
|---|---|---|---|
| NSW | Protection of the Environment Operations Act 1997 (POEO Act) | NSW EPA | Tier 1/2/3 offence structure; Environment Protection Licences (EPLs) for scheduled activities |
| VIC | Environment Protection Act 2017 | EPA Victoria | Major 2021 reforms — **General Environmental Duty (GED)** in force from 1 July 2021; tiered permit/licence/registration regime |
| QLD | Environmental Protection Act 1994 (EP Act) | Department of Environment, Science and Innovation (DESI) | Environmentally Relevant Activities (ERAs) trigger licensing; **general environmental duty** s 319 |
| WA | Environmental Protection Act 1986 | Department of Water and Environmental Regulation (DWER) | Prescribed Premises licensing under Part V |
| SA | Environment Protection Act 1993 | EPA South Australia | Schedule 1 licensable activities; general environmental duty s 25 |
| TAS | Environmental Management and Pollution Control Act 1994 (EMPCA) | EPA Tasmania | Level 1/2/3 activities; environment protection notices |
| ACT | Environment Protection Act 1997 | EPA ACT (within Access Canberra) | Authorisations and accreditations |
| NT | Waste Management and Pollution Control Act 1998 (WMPCA) | NT EPA | Pollution prevention duty; environment protection licences |

### 2.6 The General Environmental Duty (GED) — VIC, QLD, SA, NT

The GED is the environmental equivalent of the WHS SFAIRP duty. It requires
duty holders to take reasonably practicable measures to minimise the risk of
environmental harm. Where adopted, it replaces the older prescriptive permit-only
model with a duty-based regime that applies even where no specific licence is
held.

**Victoria (EP Act 2017 s 25)** — most developed GED in Australia. Applies to
any person engaging in an activity that may give rise to risks of harm to human
health or the environment. Test mirrors SFAIRP: state of knowledge, likelihood,
nature and severity of harm, availability and suitability of ways to eliminate
or reduce, cost. Criminal offence; maximum penalty $1.97M for a body corporate
(2024 indexation).

**Practical implication**: In VIC, QLD, SA and NT, every PCBU has an environmental
duty equivalent in form to the WHS PCBU duty. Risk assessment, control selection,
and documented reasoning all carry across. WHS practitioners with risk management
fluency can extend the same discipline to environmental risk without learning a
new methodology.

### 2.7 NSW POEO Tier Structure

NSW uses a three-tier offence structure that is worth understanding because it
is the model many other states converge towards:

- **Tier 1** — wilful or negligent disposal of waste/cause of pollution that
  causes substantial harm; or supply false/misleading information. Maximum
  penalty $5M corporation / $1M individual + 7 years imprisonment
- **Tier 2** — strict liability for pollution offences (water, air, noise,
  land); failure to notify pollution incidents. Maximum penalty $1M
  corporation / $250K individual
- **Tier 3** — penalty notice (on-the-spot fine) offences for lower-level
  breaches

The Tier 2 strict liability layer is the operational risk most FM and
construction operators face — a spill or unauthorised discharge attracts
liability without proof of intent.

### 2.8 Local Government Environmental Health Role

Local councils carry the bulk of environmental health regulation under state
public health legislation. Typical local government functions:

- Food premises licensing and inspection (Food Act, Food Standards Code)
- On-site sewage management (septic, AWTS)
- Cooling tower registration and Legionella risk management
- Skin penetration and personal care premises
- Public health nuisance (noise, dust, odour)
- Tobacco and vaping enforcement
- Stormwater pollution from construction sites (delegated from state EPA)

FM contracts in health, education and government sectors routinely deal with
local council environmental health officers; understand that the regulator
relationship is local council, not state EPA, for these functions.

---

## 3. NZ Environmental Regulatory Framework

### 3.1 Resource Management Act 1991 (RMA)

The RMA is the central planning and environmental statute. It governs the use,
development and protection of natural and physical resources. Activities are
classified as:

- **Permitted** — no resource consent required if rules are complied with
- **Controlled** — consent required but must be granted (control over conditions
  only)
- **Restricted discretionary** — consent required; discretion limited to specific
  matters
- **Discretionary** — full discretion; consent may be refused
- **Non-complying** — consent rarely granted; high threshold under s 104D
- **Prohibited** — no consent available

Resource consents are administered by:
- **Regional councils** — discharge consents (water, air, land), coastal
  permits, water take, river works
- **Territorial authorities** (city/district councils) — land use consents,
  subdivision consents, noise

**RMA reform context (2024–2026)**: The current Government repealed the
Natural and Built Environment Act 2023 and Spatial Planning Act 2023 (passed
under the previous Government) and is replacing the RMA with two new statutes
based on the enjoyment of property rights and natural environment limits.
Transitional provisions apply; the RMA remains the operative statute through
the transition. Confirm current status before producing advice that depends on
specific statutory provisions.

### 3.2 Climate Change Response Act 2002 and the NZ ETS

The Climate Change Response Act establishes:
- The 2050 emissions targets (net zero for all GHGs except biogenic methane;
  10% reduction in biogenic methane by 2030 and 24–47% by 2050)
- Emissions budgets set by the Climate Change Commission
- The **New Zealand Emissions Trading Scheme (NZ ETS)**

The NZ ETS is an all-sectors (except some agriculture) cap-and-trade scheme.
Liable participants must surrender NZUs (New Zealand Units) for emissions from
covered activities. Major liable sectors: stationary energy, industrial
processes, liquid fossil fuels, waste, synthetic gases, forestry.

Agriculture is currently outside the ETS pending the development of a pricing
mechanism for agricultural emissions (the He Waka Eke Noa/HWEN process and
subsequent Government policy iterations).

### 3.3 NZ EPA, Regional Councils and DOC

| Body | Role |
|---|---|
| **EPA NZ** | Hazardous Substances and New Organisms Act (HSNO); imports/exports of hazardous waste; EEZ Act marine consents; national-significance RMA matters |
| **Regional councils** | RMA discharge consents (air, water, land); contaminated land; pest management; biosecurity |
| **Territorial authorities** | RMA land use/subdivision consents; noise; on-site wastewater; trade waste |
| **Department of Conservation (DOC)** | Conservation Act; Wildlife Act; National Parks Act; concessions to operate on conservation land |
| **WorkSafe NZ** | HSWA — workplace health and safety, including hazardous substances at the workplace |

### 3.4 Hazardous Substances in NZ — HSNO + HSW (HS) Regulations 2017

The interface between environmental and workplace regulation of hazardous
substances in NZ is structurally different from Australia:

- **HSNO Act 1996** — approves substances for import/manufacture; sets classification,
  packaging, transit controls; administered by EPA NZ
- **Health and Safety at Work (Hazardous Substances) Regulations 2017** — workplace
  use of hazardous substances; administered by WorkSafe NZ
- **Resource Management Act + regional plans** — discharges of hazardous substances
  to air, water, land; administered by regional councils

A single substance attracts three concurrent regulators. Coordinate accordingly.

### 3.5 HSWA Intersection with Environmental Regulators

The **Health and Safety at Work Act 2015 (HSWA)** carries a duty to manage
hazardous substances at the workplace. Where a hazardous substance event also
causes environmental harm (spill into stormwater, discharge to land), separate
notifications run to:
- WorkSafe NZ — under HSWA s 56 if it is a notifiable event
- The regional council — under the RMA if a discharge consent has been breached
  or unauthorised discharge has occurred
- EPA NZ — for some HSNO-specific compliance matters (rare in operational FM)

---

## 4. ISO 14001:2015 EMS Clause Map

ISO 14001:2015 follows the **Annex SL high-level structure** shared with ISO
45001:2018 and ISO 9001:2015. Integrated management systems are the default
expectation in mature operators. The clause map below mirrors the ISO 45001 map
in `frameworks.md` §3 to support integrated gap analysis.

### 4.1 Clause Map

| Clause | Title | Key requirements |
|---|---|---|
| 4 | Context of the Organisation | Internal/external issues; interested parties; scope; EMS |
| 4.1 | Understanding the organisation and its context | Environmental conditions affecting/affected by the organisation |
| 4.2 | Needs and expectations of interested parties | Regulators, community, customers, employees, NGOs |
| 4.3 | Scope of the EMS | Boundaries; products/services; activities; influence/control |
| 4.4 | Environmental management system | Establish, implement, maintain, continually improve |
| 5 | Leadership | Top management commitment; environmental policy; roles |
| 5.1 | Leadership and commitment | Active engagement; integration into business processes; resource provision |
| 5.2 | Environmental policy | Commits to: protection of environment; prevention of pollution; fulfilment of compliance obligations; continual improvement |
| 5.3 | Organisational roles, responsibilities and authorities | Assign and communicate; designated representative |
| 6 | Planning | Risks and opportunities; environmental aspects; compliance obligations; objectives |
| 6.1.1 | General | Determine risks/opportunities related to aspects, compliance, other issues |
| 6.1.2 | Environmental aspects | Identify activities, products, services aspects; determine those with significant impacts (see §5) |
| 6.1.3 | Compliance obligations | Identify, have access to, determine application |
| 6.1.4 | Planning action | Address significant aspects, compliance obligations, risks/opportunities; integrate into EMS processes |
| 6.2 | Environmental objectives | Measurable; monitored; communicated; updated |
| 7 | Support | Resources; competence; awareness; communication; documented information |
| 7.4 | Communication | Internal + external; respond to relevant environmental communications |
| 8 | Operation | Operational planning and control; emergency preparedness and response |
| 8.1 | Operational planning and control | Establish, implement and maintain controls; control planned changes; outsourced processes |
| 8.2 | Emergency preparedness and response | Identify potential emergency situations; plan response; test; review |
| 9 | Performance evaluation | Monitoring; evaluation of compliance; internal audit; management review |
| 9.1.1 | General | Monitoring/measurement methods; equipment calibrated/verified |
| 9.1.2 | Evaluation of compliance | Periodic evaluation of fulfilment of compliance obligations |
| 9.2 | Internal audit | Programme; criteria; competent auditors; report to management |
| 9.3 | Management review | Periodic; agenda includes compliance evaluation, incidents, objectives progress |
| 10 | Improvement | Nonconformity + corrective action; continual improvement |
| 10.1 | General | Improve to enhance environmental performance |
| 10.2 | Nonconformity and corrective action | Timely response; root cause; effectiveness review |
| 10.3 | Continual improvement | Ongoing enhancement of EMS suitability, adequacy, effectiveness |

### 4.2 Integrated System Notes
- Clauses 4, 5, 7, 9, 10 align almost verbatim with ISO 45001 and ISO 9001 —
  procedures can be common across all three systems
- Clauses 6.1.2 (aspects/impacts) and 8.2 (emergency response) are
  environment-specific in content but follow the same structural logic as the
  WHS equivalents (hazard ID, emergency planning)
- A single Management Review meeting can cover ISO 9001, 14001 and 45001 inputs
  provided each system's required inputs are addressed

### 4.3 Common ISO 14001 Nonconformities
- Aspects/impacts register out of date or not linked to controls (6.1.2)
- Compliance obligations register incomplete (6.1.3) — state EPA conditions,
  licence variations, council consents often missed
- Operational controls not maintained at sites where work is intermittent (8.1)
- Emergency preparedness drills not conducted at frequency stated in the plan
  (8.2)
- Evaluation of compliance not documented (9.1.2) — auditors expect explicit
  evidence of compliance evaluation, not just compliance itself

---

## 5. Environmental Aspects and Impacts

### 5.1 Definitions
- **Environmental aspect** = element of an organisation's activities, products
  or services that interacts with the environment (e.g. diesel use, refrigerant
  storage, waste generation, water abstraction)
- **Environmental impact** = change to the environment, adverse or beneficial,
  wholly or partially resulting from an environmental aspect (e.g. GHG emissions,
  ozone depletion, water depletion, soil contamination)
- **Significant aspect** = aspect that has or can have a significant impact;
  organisation must determine significance criteria

### 5.2 The Aspects/Impacts Register Process

The aspects/impacts process is the environmental equivalent of the WHS hazard
identification process. Steps:

1. **Identify activities, products and services** in scope — by site, process,
   or value stream
2. **For each, identify aspects** — inputs (materials, energy, water) and
   outputs (emissions, discharges, waste, products)
3. **For each aspect, identify impacts** — actual and potential, normal and
   abnormal conditions, emergency situations
4. **Apply significance criteria** to determine which aspects are significant
5. **Map controls** for each significant aspect
6. **Review periodically** and on significant change (new activity, regulatory
   change, incident)

### 5.3 Significance Criteria

Organisations set their own significance criteria but typically include:

| Criterion | Example bands |
|---|---|
| Scale of impact | Local / regional / national / global |
| Severity | Minor / moderate / serious / catastrophic |
| Probability of occurrence | Routine / abnormal / emergency only |
| Duration of impact | Short-term reversible / long-term reversible / irreversible |
| Regulatory exposure | Below threshold / licensable / notifiable / prosecutable |
| Stakeholder concern | Internal / local community / broader public / international |

Many organisations use a 5×5 environmental risk matrix mirroring their safety
matrix — aspect rating = consequence × likelihood. See `company.md` for
organisation-specific consequence and likelihood criteria.

### 5.4 Worked Example — FM Depot

| Activity | Aspect | Impact | Significance | Controls |
|---|---|---|---|---|
| Diesel refuelling of plant | Diesel use; potential spill | GHG emission; soil/groundwater contamination | Significant (compliance + community) | Bunded fuel cell; spill kit; dispenser interlock; quarterly bund integrity check |
| HVAC servicing | Refrigerant handling | Ozone depletion (legacy gases); GHG (HFCs) | Significant (compliance — ARC tradesperson licence) | Licensed technician only; refrigerant tracking log; recovery cylinders |
| Vehicle washbay | Wastewater discharge | Trade waste to sewer | Significant (trade waste consent) | Triple-interceptor pit; quarterly sludge removal; trade waste agreement with utility |
| Yard stormwater runoff | Sediment, hydrocarbons | Discharge to receiving waters | Significant (POEO/EP Act licensing) | Capture and treatment; SSEC plan; visual inspection weekly |
| Office printing | Paper/cartridge consumption | Resource depletion; waste | Not significant (low quantity) | Default duplex; cartridge return scheme |

---

## 6. Environmental Incident Classification & Notification

### 6.1 The Core Triggers

In all AU jurisdictions, the operator/occupier of premises has a duty to notify
the regulator (EPA or equivalent) of a **pollution incident** that causes or
threatens **material harm to the environment**. The trigger language varies by
state but the common elements are:

- **Material harm** — harm involving actual or potential harm to human health
  or safety, or to the environment, that is not trivial; or actual or potential
  loss/property damage above a monetary threshold ($10,000 in NSW POEO Act s 147)
- **Pollution incident** — leak, spill, escape, dumping, deposit, discharge of
  pollutant
- **Threatens** — material harm need not have occurred; risk is sufficient

A notification is required **as soon as the operator becomes aware** of the
incident — not when investigation is complete. Delays in notification are
themselves separate offences in most jurisdictions.

### 6.2 State-by-State Notification Requirements

| Jurisdiction | Statutory basis | Trigger | Timing | To whom |
|---|---|---|---|---|
| **NSW** | POEO Act 1997 s 148 | Pollution incident causing or threatening material harm | Immediately; written follow-up within 7 days | NSW EPA, local council, Ministry of Health, SafeWork NSW, FRNSW |
| **VIC** | EP Act 2017 s 32 | Notifiable incident (defined in Reg 24 — fire, explosion, contamination of waters/land, asbestos release, significant discharge) | As soon as practicable | EPA Victoria 1300 372 842 |
| **QLD** | EP Act 1994 s 320 + s 320A | Material/serious environmental harm or risk of | Within 24 hrs of becoming aware | Administering authority (DESI or local govt) |
| **WA** | EP Act 1986 s 72 | Discharge of waste causing pollution | As soon as practicable | DWER |
| **SA** | EP Act 1993 s 83 | Serious or material environmental harm | As soon as reasonably practicable | EPA SA |
| **TAS** | EMPCA s 32 | Emission causing or threatening serious or material environmental harm | As soon as reasonably practicable | EPA Tasmania |
| **ACT** | EP Act 1997 s 23A | Discharge of pollutant likely to cause material/serious harm | As soon as practicable | EPA ACT |
| **NT** | WMPCA s 14 | Incident causing or threatening material/serious environmental harm | Immediately | NT EPA |

### 6.3 NSW Example — Section 148 Notification Detail

NSW POEO Act s 148 is the most prescriptive notification regime and worth knowing
in detail because it is often used as the AU benchmark for internal procedures:

The occupier (and the polluter, if a different person) **must immediately**
notify the relevant authorities of a pollution incident if material harm to the
environment is caused or threatened. The notification must include:

- Time, date, nature, duration, location of the incident
- Location of any place where pollution is occurring or likely to occur
- Substance involved and estimated quantity
- The circumstances in which the pollution incident occurred
- Action taken or proposed to deal with the incident

In NSW, multiple agencies must be notified concurrently: EPA, local council,
Ministry of Health, SafeWork NSW (where worker exposure), and Fire and Rescue
NSW (where fire/explosive). A single phone call to one does not discharge the
duty for the others. Maximum penalty for failure to notify: $2M corporation /
$500K individual + daily continuing offence.

### 6.4 Internal Escalation Parallel to WHS

Environmental incidents should be classified using the same matrix as WHS
incidents (most internal classifications do this — see [organisation] [incident system] in
`company.md` §5 for a worked example where environment is the second consequence
dimension in a 1–6 rating).

| Severity | Environmental example | Internal response |
|---|---|---|
| **1 — Very Low** | Drip from machinery — captured on absorbent mat; no release to environment | Logged; cleanup; no formal investigation |
| **2 — Low** | Minor hydrocarbon spill <20 L; fully contained on hardstand; community complaint resolved on the spot | Logged in incident system; supervisor cleanup; 5-Why |
| **3 — Medium** | Notifiable spill (state-dependent); short-term turbidity in stormwater; cleanup within hours | Regulator notification triggered; internal investigation (DG-ZH-FM006 equivalent); lessons shared |
| **4 — High** | Material harm threshold tripped; ground/groundwater contamination requiring assessment; sustained community impact | ICAM investigation; senior leader engagement; consultant engaged for site assessment |
| **5 — Very High** | Major fish kill / waterway contamination; widespread air emission; serious environmental harm | Crisis response; legal counsel; prosecution risk; ELT briefing |
| **6 — Extreme** | Catastrophic ecosystem damage; multi-jurisdictional impact; long-term community/economic harm | Crisis management team activation; board notification; external counsel; potential officer liability |

The internal classification must align with statutory definitions of material
and serious harm in the relevant jurisdiction — do not invent thresholds that
sit below the regulatory trigger.

---

## 7. Hazardous Chemicals & Dangerous Goods — Storage

The exposure-side regulation of hazardous chemicals sits in `hazards.md` (Part 7
model WHS Regs — workplace exposure standards, SDS, register, manifest). This
section covers the **environmental aspects** — storage design, bunding, placarding,
manifests for emergency services, transport.

### 7.1 Placard and Manifest Quantities (Model WHS Regs)

| Schedule | Threshold | Trigger |
|---|---|---|
| **Schedule 11** | Placard quantities | Where exceeded, workplace must be placarded (outer warning placards) and SDS/register made available to emergency services |
| **Schedule 14** | Manifest quantities | Where exceeded, a written **Manifest of Hazardous Chemicals** must be prepared and held at the workplace AND provided to the WHS regulator and emergency services |

Examples of common Schedule 11 placard quantities:
- Class 3 (flammable liquids) PG II: 250 L
- Class 3 PG III: 1,000 L
- Class 5.1 (oxidising substances) PG II: 250 kg
- Class 6.1 (toxic) PG II: 50 kg
- Class 8 (corrosive) PG II: 250 L
- Combustible liquids C1: 10,000 L

Examples of Schedule 14 manifest quantities:
- Class 3 PG II: 2,500 L
- Class 3 PG III: 10,000 L
- Class 8 PG II: 2,500 L
- Combustible liquids C1: 100,000 L

Manifest notification to the regulator is required within 14 days of the
quantity threshold being exceeded for the first time, and within 14 days of any
change to the manifest information.

### 7.2 Australian Standards for Storage

| Standard | Scope |
|---|---|
| AS 1216 | Class labels for dangerous goods (placarding designs) |
| **AS 1940:2017** | Storage and handling of flammable and combustible liquids |
| AS 4326:2008 | Storage and handling of oxidising agents |
| AS 3780:2008 | Storage and handling of corrosive substances |
| AS 4332:2004 | Storage and handling of gases in cylinders |
| AS/NZS 2243.10 | Safety in laboratories — storage of chemicals |
| AS 2187.0-2.1 | Explosives — storage, transport, use |
| AS 5026:2012 | Storage and handling of Class 4 dangerous goods |

AS 1940 is the most frequently referenced standard in FM and construction
contexts. Key obligations:

- **Compounds**: minimum spacing between stores and from boundaries; separation
  between incompatible classes (e.g. flammables vs oxidisers)
- **Ventilation**: natural or mechanical; explosion-protected if Hazardous Area
- **Bunding**: capacity per §7.3 below
- **Fire protection**: dry chemical, foam, or sprinkler depending on quantity
  and configuration
- **Ignition source control**: hazardous area classification per AS/NZS 60079.10.1
- **Spill containment** and clean-up materials available

### 7.3 Bunding — the 110% + 25% Rule

The standard bunding capacity rule, drawn from AS 1940 and EPA guidelines:

**Bund capacity** ≥ the greater of:
- **110%** of the volume of the largest single container in the bund (covering
  catastrophic failure of the largest tank), **PLUS** capacity to capture
- **25%** of the aggregate rainfall volume on the bund area over a defined
  rainfall event (typical: 24-hour, 1-in-10-year ARI event — check state EPA
  guidelines)

For outdoor bunds, the rainfall capture component matters — many bunds designed
to 110% only have failed during heavy rainfall. Roofed bunds avoid this but
introduce ventilation, fire suppression, and confined space considerations.

**Compatible materials only**: a bund holding sulphuric acid cannot share with
caustic; a bund holding diesel cannot share with a Class 5.1 oxidiser. AS 1940
§4.6 provides the segregation matrix.

### 7.4 Transport — ADG Code 7.9

The **Australian Dangerous Goods Code (ADG Code) Edition 7.9** (effective from
2024) regulates the transport of dangerous goods by road and rail. Administered
by state/territory transport regulators; mirrors UN Recommendations on the
Transport of Dangerous Goods (UN Model Regulations).

Key elements:
- Classification and packing group assignment
- UN-approved packaging
- Marking, labelling and placarding of vehicles
- Documentation — transport document, emergency information
- Driver licensing (DG Driver Licence required >500 kg/L of placard load)
- Vehicle requirements (placards, fire extinguisher, spill kit)
- Loading and segregation rules

FM operators arranging transport of fuel, gas cylinders, paints, cleaning
chemicals, batteries and refrigerants need ADG Code awareness — most small loads
trigger Limited Quantities exemptions but the threshold is easy to exceed during
mobilisation/demobilisation.

---

## 8. Spill Response and Site Contamination

### 8.1 Spill Kit Selection and Deployment

| Kit type | Contents (typical) | Use |
|---|---|---|
| **General-purpose** | Absorbent pads, socks, pillows; PVC gloves; disposal bags; PPE | Mixed-use sites; low-volume liquids |
| **Hydrocarbon (oil-only)** | Hydrophobic polypropylene absorbents (white) — repel water, absorb oil | Outdoor diesel/oil spills where water present (rain, waterway) |
| **Chemical (universal)** | Polypropylene + cellulose absorbents (yellow); pH-neutralising material; chemical-resistant PPE | Acids, alkalis, solvents; lab and depot use |
| **Mercury** | Specific amalgamation kit; sealed container | Mercury thermometer/lamp breakage |

Kit placement should reflect the risk map — at fuel storage, plant maintenance
bays, chemical stores, vehicle washbays, loading/unloading points. Routine
inspection (monthly typical) of kit contents, expiry, and quantity is a leading
indicator of operational readiness.

### 8.2 Initial Response — Stop > Contain > Notify > Assess > Remediate

The five-step spill response sequence applies regardless of spill type:

1. **Stop the source** — close valves, right the container, isolate energy. Do
   not do this if it endangers the responder.
2. **Contain the spill** — absorbent socks at perimeter, drain covers over
   stormwater inlets, divert flow away from receiving waters
3. **Notify** — internal (per incident management procedure); external (per
   §6.2 if material/serious harm threshold tripped); emergency services if
   fire/explosion risk
4. **Assess** — quantity, substance, receiving environment (hardstand, soil,
   stormwater, waterway), exposure pathway, sensitive receptors
5. **Remediate** — cleanup, contaminated material disposal as regulated waste,
   environmental sampling if soil/groundwater contamination, restoration

**Storm drain covers are the single highest-leverage spill control on most FM
sites**. A spill that reaches stormwater enters a receiving waterway in minutes.
A spill caught on hardstand is a cleanup; a spill into the harbour is a
prosecution.

### 8.3 Site Contamination Assessment

Where contamination is suspected or confirmed (legacy use, spill, unauthorised
discharge, redevelopment), assessment follows the **National Environment
Protection (Assessment of Site Contamination) Measure 1999 as amended 2013
(ASC NEPM)**. The ASC NEPM is incorporated by reference into most state
contaminated land regimes.

ASC NEPM staged assessment:
1. **Preliminary Site Investigation (PSI)** — desktop + walkover; historical
   land use; identification of potentially contaminating activities (PCAs);
   conceptual site model
2. **Detailed Site Investigation (DSI)** — sampling and laboratory analysis;
   comparison to investigation levels (HIL — Health Investigation Levels;
   EIL — Ecological Investigation Levels; ESL — Ecological Screening Levels;
   GIL — Groundwater Investigation Levels)
3. **Remediation Action Plan (RAP)** — if remediation required
4. **Validation** — post-remediation sampling to confirm cleanup objectives met
5. **Site Audit Statement** — by an accredited Site Auditor (NSW, VIC, QLD, WA
   have statutory auditor accreditation schemes)

A suitably qualified environmental consultant must lead the investigation; the
WHS/EHS practitioner manages the engagement, regulator interface, and
operational implications (work restrictions, PPE, exposure monitoring during
remediation).

### 8.4 Notification of Contamination

Most state contaminated land Acts impose a duty to notify the regulator when
contamination of a specified description is discovered:

| Jurisdiction | Statutory basis | Trigger |
|---|---|---|
| **NSW** | Contaminated Land Management Act 1997 s 60 | Duty to report contamination that meets the "significant risk of harm" trigger |
| **VIC** | EP Act 2017 + EP Regs 2021 (Part 6.5) | Contaminated land notification; PFAS specific guidance |
| **QLD** | EP Act 1994 s 320D | Duty to notify of notifiable activity contamination |
| **WA** | Contaminated Sites Act 2003 s 11 | Mandatory reporting of known/suspected contaminated sites |
| **SA** | EP Act 1993 Part 10A | Notification of site contamination affecting groundwater |

PFAS (per- and polyfluoroalkyl substances) contamination has specific guidance
in most jurisdictions following the firefighting foam legacy issue at Defence
sites; PFAS National Environmental Management Plan (NEMP) 3.0 is the current
national reference.

---

## 9. Waste Management Hierarchy & Tracked Waste

### 9.1 The Waste Hierarchy

The waste hierarchy is codified in most state waste legislation and the
National Waste Policy Action Plan 2019. Apply top-down:

1. **Avoid** — do not generate the waste (design out)
2. **Reduce** — minimise quantity generated
3. **Reuse** — use again in current form
4. **Recycle** — reprocess into new product
5. **Recover** — energy recovery from waste (waste-to-energy)
6. **Treat** — render less hazardous (e.g. neutralisation, encapsulation)
7. **Dispose** — landfill of last resort

Treatment/disposal of higher-tier waste when higher-order options are reasonably
practicable is a breach of the General Environmental Duty in jurisdictions that
have one (VIC, QLD, SA, NT).

### 9.2 Waste Classification

Waste is classified by composition and hazard. Each state uses a slightly
different scheme but the broad categories are:

- **General solid waste (putrescible)** — household garbage, food waste
- **General solid waste (non-putrescible)** — construction & demolition,
  packaging, paper
- **Restricted solid waste** — specified contaminants below regulated waste
  thresholds (e.g. asbestos-containing material in some states)
- **Liquid waste** — non-hazardous (e.g. grease trap, food-related liquids)
- **Hazardous waste / Regulated waste / Tracked waste / Listed waste** —
  state-specific terminology for waste meeting hazard or composition criteria
  that triggers tracking and licensed transport/disposal

Reference: NSW EPA "Waste Classification Guidelines"; QLD ESR/2019/4791 Regulated
Waste classification; VIC EPA Industrial Waste Resource Guidelines (now
Reportable Priority Waste under EP Act 2017); WA Environmental Protection
(Controlled Waste) Regulations 2004.

### 9.3 Tracked / Regulated Waste Systems

| State | Scheme | System |
|---|---|---|
| **NSW** | EPA Waste Tracking | WasteLocate / paper consignments; required for asbestos, contaminated soil, regulated waste >100 kg/L |
| **VIC** | Reportable Priority Waste (RPW) | EPA Waste Tracker (electronic) |
| **QLD** | Regulated Waste Tracking | QLDe-Waste tracker; required for listed waste >250 kg/L |
| **WA** | Controlled Waste | Controlled Waste Tracking System (CWTS) |

Movement of **interstate** controlled waste is regulated under the **Movement of
Controlled Waste NEPM** plus state regulations. Notification to both source and
destination state EPAs is required; consignment authority numbers must accompany
the load.

### 9.4 Hazardous Waste Classification — HW Codes

The Movement of Controlled Waste NEPM uses a **HW code** classification (e.g.
HW A100 — clinical and related wastes; HW K100 — inorganic chemicals containing
metals). Each tracked waste consignment requires the correct HW code,
quantity, source and destination details.

### 9.5 Asbestos Waste

Asbestos waste handling — cross-reference `hazards.md` §3 for the overall
asbestos framework. Environmental considerations specific to disposal:

- All asbestos waste is **regulated waste** in all AU jurisdictions
- Must be **wetted, double-wrapped in 200 µm polythene**, marked "ASBESTOS",
  and transported by a licensed asbestos waste carrier
- Disposal at an **EPA-licensed asbestos landfill** only (not all landfills accept
  asbestos; most metropolitan landfills require pre-booking)
- Consignment authority issued by the licensed transporter; copy retained for
  minimum statutory period (varies — typically 5 years)
- **Illegal dumping of asbestos** attracts the highest penalty bands in most
  state waste legislation

### 9.6 Practical Implications for FM / Contract Portfolios
- Construction & demolition waste streams should be segregated at source —
  separation rates >90% are achievable on most projects with proper signage,
  bin placement, and contractor briefing
- Regulated waste contracts (asbestos, oily water, chemical) must be set up with
  licensed transporters BEFORE the waste is generated — emergency engagement at
  point of generation invariably costs more and increases compliance risk
- Track waste consignment authorities through the EHS system; missing consignment
  paperwork is a common audit finding

---

## 10. Air Emissions and Water Discharge

### 10.1 Environment Protection Licences (EPLs) — Scheduled Activities

Each state EPA licenses defined activities under its environmental protection
Act. Names vary (NSW: EPL under POEO Act Sch 1; VIC: Operating Licence under
EP Act 2017; QLD: Environmental Authority under EP Act 1994 for Environmentally
Relevant Activities; WA: Works Approval/Licence under EP Act 1986 for Prescribed
Premises). Operationally similar.

Typical scheduled/licensable activities relevant to FM and construction:

- Waste treatment, transport, and disposal facilities
- Wastewater treatment plants
- Composting and biomass operations
- Fuel storage above defined thresholds
- Hazardous chemical bulk storage
- Industrial processes (smelting, chemical manufacture, etc.)
- Concrete batching plants
- Crematoria
- Marinas above defined boat capacities
- Mining and extraction

Licence conditions typically specify:
- Emission limits (point source — stack, outfall)
- Monitoring frequency and method (NATA-accredited lab where required)
- Reporting obligations (annual return, exceedance notifications)
- Operational limits (hours, throughput, capacity)
- Complaint handling procedures
- Pollution Incident Response Management Plan (PIRMP) — NSW requirement; similar
  in other states under different names

### 10.2 Stormwater Management for Construction

State EPA guidelines and the NSW "Blue Book" (Managing Urban Stormwater: Soils
and Construction Vol 1 — Landcom 2004) are the operational references. Typical
trigger thresholds:

- **Soil disturbance ≥2,500 m²** — Erosion and Sediment Control Plan (ESCP)
  required
- **Soil disturbance ≥1 ha** — Soil and Water Management Plan (SWMP) or
  equivalent
- **Soil disturbance in sensitive catchment** — additional consent conditions

Standard sediment and erosion controls (E&SC):
- Sediment fences (geofabric, properly toed and overlapped)
- Diversion drains, swales, and chutes
- Sediment basins sized for design storm event (typically 80th percentile 5-day
  event)
- Stabilised site entrances (rock pad with grid)
- Soil stockpile covers and bunding
- Progressive stabilisation (mulch, hydromulch, jute mesh, turf)

Local councils enforce stormwater pollution under delegated state EPA powers —
inspectors visit construction sites unannounced, especially before/during
predicted rainfall. Visible sediment plume from a construction site is a
strict-liability offence and a near-guaranteed penalty notice.

### 10.3 Air Emissions — Common FM/Construction Sources

| Source | Pollutants | Controls |
|---|---|---|
| Diesel plant exhaust | NOx, PM, CO, VOCs | Tier 4 engines; routine maintenance; idle reduction |
| Concrete batching | PM₁₀, PM₂.₅, cement dust | Enclosure; baghouse; water suppression |
| Spray painting | VOCs, isocyanates | Spray booth with filtration; HVLP equipment |
| Welding | Welding fume (incl. hexavalent chromium from stainless) | LEV; respiratory protection; substitution of consumables |
| Asbestos removal | Asbestos fibres | Enclosure under negative pressure; HEPA filtration; clearance air monitoring |
| Refrigerant systems | HFCs (GWP); ozone-depleting substances (legacy CFCs/HCFCs) | ARC-licensed servicing; recovery; tracking log |
| Land clearing/burning | PM, VOCs, GHG | Avoid open burning; chip and reuse where possible |
| Aggregate stockpiles | PM | Water suppression; wind breaks; minimisation of fall heights |

Dust and odour are the most frequent community complaint sources — both have
loose regulatory thresholds but high reputational impact. Manage as if they
were regulated.

### 10.4 Trade Waste Discharge to Sewer

Discharge to sewer is regulated by the water utility (Sydney Water, Yarra
Valley Water, Urban Utilities, etc.) under a **trade waste agreement**. Common
restricted parameters:

- pH (typically 6.0–10.0)
- Temperature (typically <38 °C)
- Oils and grease (typically <100 mg/L)
- Suspended solids (limits vary)
- Heavy metals (each parameter)
- Specific organics (BTEX, chlorinated solvents, etc.)

Vehicle washbays, kitchens, hospital pathology, and dental practices are common
trade waste regulated activities. Pre-treatment (oil-water separator, grease
trap, neutralisation tank) is typically required; tank maintenance and waste
removal records must be kept and produced on request.

---

## 11. Biodiversity and Heritage

### 11.1 Pre-Construction Biodiversity Surveys

Major civil and construction works require pre-construction biodiversity
assessment. Triggered by:
- EPBC Act referral (Commonwealth — see §2.1)
- State biodiversity legislation (NSW Biodiversity Conservation Act 2016;
  VIC Flora and Fauna Guarantee Act 1988; QLD Nature Conservation Act 1992;
  WA Biodiversity Conservation Act 2016)
- Local planning instrument (LEP/DCP, Council planning scheme)

Typical scope:
- **Flora survey** — vegetation community mapping; threatened plant species
  search; weed mapping
- **Fauna survey** — habitat assessment; targeted surveys for threatened
  species (often seasonally constrained — e.g. spring breeding-season surveys
  for woodland birds)
- **Aquatic ecology** — where waterways present; fish, macroinvertebrates,
  riparian vegetation
- **Tree assessment** — arboricultural assessment for habitat trees (hollows);
  Tree Preservation Order compliance

Surveys must be conducted by suitably qualified ecologists; reports inform
clearing limits, offset requirements, and consent conditions.

### 11.2 Aboriginal Heritage — Jurisdictional Frameworks

Aboriginal cultural heritage protection is jurisdictionally distinct. The
framework below summarises the operational pathway — load specialist heritage
advice before producing definitive guidance.

| Jurisdiction | Primary Act | Operational mechanism |
|---|---|---|
| **NSW** | National Parks and Wildlife Act 1974 (Part 6) | **Aboriginal Heritage Impact Permit (AHIP)** required to harm Aboriginal objects; due diligence per NSW OEH Code of Practice |
| **VIC** | Aboriginal Heritage Act 2006 | **Cultural Heritage Management Plan (CHMP)** required for high-impact activities in areas of cultural heritage sensitivity; prepared by Heritage Advisor |
| **QLD** | Aboriginal Cultural Heritage Act 2003 | **Cultural Heritage Duty of Care** (s 23) — duty to take all reasonable and practicable measures to ensure activity does not harm Aboriginal cultural heritage; CH Duty of Care Guidelines |
| **WA** | Aboriginal Heritage Act 1972 (active again following 2023 repeal of 2021 replacement) | s 18 consent required to use land where Aboriginal site exists |
| **SA** | Aboriginal Heritage Act 1988 | Authorisation under s 23 |
| **TAS** | Aboriginal Heritage Act 1975 | Permit required to disturb relics |
| **NT** | NT Aboriginal Sacred Sites Act 1989 | Authority Certificate from Aboriginal Areas Protection Authority |
| **Commonwealth** | Aboriginal and Torres Strait Islander Heritage Protection Act 1984 | Last-resort federal protection where state law inadequate |

In the wake of the Juukan Gorge destruction (May 2020), jurisdictional reviews
have tightened consultation obligations and enforcement. The operational
benchmark in 2025–2026 is genuine, early, ongoing engagement with Traditional
Owners — not minimal-compliance permit processes.

### 11.3 Native Title

The **Native Title Act 1993 (Cth)** establishes the process for recognition of
native title rights and interests. Where native title may exist over land
proposed for development:

- Future Act notices may be required (s 24)
- Indigenous Land Use Agreements (ILUAs) may be negotiated
- Right to negotiate procedures apply to mining and certain compulsory
  acquisitions

Native title is distinct from cultural heritage protection — they are separate
regimes with separate processes and separate consultations. Many projects
require both.

### 11.4 Practical Implications for FM / Contract Portfolios
- Defence base, government land, regional infrastructure projects routinely
  involve both Aboriginal heritage and native title processes
- Engagement timeframes are long — CHMPs in VIC commonly take 6–12 months
- Stop-work clauses in heritage-affected scopes are standard; build into
  programme contingency
- Worker training on cultural heritage awareness should be standard induction
  content where any chance of artefact discovery exists

---

## 12. Climate Change — WHS Intersection

Climate change is regulated as a corporate disclosure matter (NGER, ISSB,
Treasury climate disclosure legislation 2024) and as an operational WHS hazard.
This section covers the operational intersections — the corporate disclosure
side is outside skill scope.

### 12.1 Heat Extremes
Cross-reference `hazards.md` §6 for the full working in heat framework. The
environmental dimension:
- Climate projections (CSIRO/BoM State of the Climate 2024) indicate increased
  frequency of extreme heat days, particularly in WA, NT and inland QLD
- Hot work in summer should assume worse-than-historical conditions; do not
  rely on historical averages for risk assessment
- Heat-stressed plant equipment (mobile, hydraulic) requires earlier and more
  frequent maintenance under higher ambient temperatures
- Workforce acclimatisation programs must extend earlier in the season and
  continue later

### 12.2 Bushfire Smoke and Air Quality

The 2019–2020 Black Summer bushfires established sustained PM₂.₅ exceedances
as a routine workplace exposure issue. Operational thresholds (NSW Health
"Air Quality Categories"):

| AQI band | PM₂.₅ µg/m³ (24-hr) | Sensitive group response | General response |
|---|---|---|---|
| Good | 0–9 | Normal activity | Normal activity |
| Fair | 10–25 | Normal activity | Normal activity |
| Poor | 26–39 | Reduce prolonged outdoor exertion | Normal activity |
| Very Poor | 40–106 | Avoid prolonged outdoor exertion | Reduce prolonged outdoor exertion |
| Extremely Poor | ≥107 | Avoid all outdoor physical activity | Avoid prolonged outdoor exertion |

Operational controls during smoke events:
- Real-time AQI monitoring (AirRater app; state EPA networks)
- Activity modification triggers in heat/smoke procedure
- Indoor air management — close intakes; MERV-13 minimum filters; portable HEPA
  in occupied areas
- Respiratory protection (P2/N95) where outdoor work cannot be deferred — fit
  testing required, hot work compounds heat stress risk
- Sensitive worker provisions (asthma, cardiovascular conditions, pregnancy)

### 12.3 Extreme Weather Event Planning

Cyclone, flood, severe storm, and bushfire frequency and severity trends are
upward. Operational planning baselines:

| Hazard | Planning reference | Operational impact |
|---|---|---|
| Tropical cyclone | BoM cyclone watch/warning; Category 1–5 | Pre-season equipment securing; lay-down protocols; evacuation triggers |
| Riverine flood | BoM flood watch; council flood mapping | Site flood risk assessment; equipment relocation thresholds |
| Flash flood | Real-time radar; SES warnings | Suspension of low-lying work; vehicle movement controls |
| Severe storm | BoM severe thunderstorm warning | Crane and elevated work stop-work triggers; lightning protocols |
| Bushfire | BoM Fire Danger Rating (Catastrophic/Extreme/High/Moderate) | Hot work permit suspension; site evacuation triggers; ember protection |

The **Australian Fire Danger Rating System (AFDRS)** was rolled out nationally
in September 2022 — replaces older state-specific systems with consistent
Catastrophic/Extreme/High/Moderate/No Rating tiers.

### 12.4 Adaptation vs Mitigation

- **Mitigation** = reducing emissions to limit climate change (Scope 1+2+3
  reductions, NGER reporting, Safeguard Mechanism compliance, ETS surrender)
- **Adaptation** = adjusting operations to projected and current climate
  conditions (heat, smoke, extreme weather, water availability, ecosystem
  shifts)

WHS practitioners are primarily concerned with adaptation. Mitigation typically
sits with sustainability, energy, and procurement functions. The two intersect
where energy efficiency reduces heat load (worker amenity), where electrification
removes combustion sources (air quality), and where on-site renewables introduce
new hazards (battery storage, HV systems).

---

## 13. Environmental Output Checklist

Before finalising any environmental output, confirm:
- [ ] Correct jurisdiction cited (Commonwealth + state/territory + local where relevant)
- [ ] Correct statutory provision named (Act + section + year)
- [ ] General Environmental Duty addressed where in scope (VIC, QLD, SA, NT)
- [ ] Notifiable thresholds checked against state EPA trigger language — not paraphrased
- [ ] Aspects/impacts thinking applied to operational risk tasks (not just hazards)
- [ ] Waste hierarchy applied top-down to disposal/treatment recommendations
- [ ] Bunding capacity calculation includes both 110% and 25% rainfall components
- [ ] Spill response sequence covers stop > contain > notify > assess > remediate
- [ ] Climate adaptation considerations included for outdoor/heat-exposed tasks
- [ ] Heritage and native title engagement noted where ground disturbance involved
- [ ] Environmental incident classification aligned with internal severity matrix
- [ ] EHS integration — environmental controls do not introduce WHS hazards uncontrolled
- [ ] Australian English spelling checked (licence, organisation, recognise, behaviour)
- [ ] No environmental clichés ("environmentally friendly", "green") or filler

---

For organisation-specific environmental consequence ratings, incident
classification thresholds, and reporting cadence, load `references/company.md`.

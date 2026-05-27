# Changelog

All notable changes to this skill are recorded here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); the
skill follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) at
the level of capability tiers (MAJOR for new top-level scope or restructure;
MINOR for new reference files or substantial expansions; PATCH for fixes,
currency updates, and small additions).

---

## [1.3.0] — 2026-05-27

### Added — Strategic and specialist round

Six new reference files:
- `references/strategy-function.md` (818 lines) — WHS strategy development
  (multi-year roadmap, capability uplift, beyond-TRIFR objectives); WHS
  function design (org chart, RACI, advisor ratios, in-house vs outsourced);
  WHS budget and economics; WHS leadership selection and development; crisis
  management distinct from emergency response
- `references/specialist-topics.md` (1,089 lines) — Occupational hygiene
  practice (AIOH credentials, NIOSH sampling, exposure assessment);
  workplace mental health programs beyond psychosocial regs; Modern Slavery
  Act 2018 supply chain due diligence; ESG and WHS intersection (GRI 403,
  SASB, TCFD/ISSB); insurance arrangements (PI, PL, D&O, cyber)
- `references/diversity-inclusion.md` (967 lines) — Indigenous workforce
  considerations (cultural load, cultural heritage, Sorry Business);
  reasonable adjustments for disability; neurodivergent worker
  accommodation; multi-language safety communication; gendered violence
  and equity considerations
- `references/whs-procurement.md` (726 lines) — WHS in procurement;
  buyer-side WHS evaluation; supplier-side tender response; Modern Slavery
  DD overlap; ongoing contractor performance management
- `references/whistleblower.md` (345 lines) — Whistleblower protections
  and WHS reporting intersection (Corporations Act Part 9.4AAA, PIDA,
  state PID Acts)
- `references/case-studies-everyday.md` (1,197 lines) — Worked everyday
  incidents (forklift HiPo, manual handling MSI, psychosocial complaint,
  electrical near-miss, slip-trip-fall, chemical decant spill, fatigue
  vehicle incident) for training and ICAM calibration

### Added — Existing-file expansions

- `references/investigation.md` §8–§14 — PEEPO question bank; witness
  interview technique (PEACE model, cognitive interviewing); witness
  statement format and admissibility; ICAM variants comparison (BHP, IOGP,
  Safety Wise); AcciMap methodology; bowtie worked example; legal privilege
  management during investigation
- `references/legislation.md` §14 — Workplace Exposure Standards (WES)
  reference table for common substances
- `references/legislation.md` §15 — Codes of Practice key requirements
  summary
- `references/legislation.md` §16 — State and territory variations deeper
  detail (VIC OHS Act 2004 specifics plus state-by-state divergences)
- `references/hazards.md` §19–§22 — Crane lifts and rigging; demolition;
  excavation and trench shoring; hot work
- `references/frameworks.md` §13 — M&A sector overlays for mining,
  healthcare, construction
- `references/sector-regimes.md` §8–§13 — Petrochemical and downstream;
  telecommunications; agriculture and pastoral; hospitality; education;
  retail
- `references/case-studies.md` §9–§12 — Costa Concordia (2012); Ranger
  Uranium Mine recurring releases; Bhopal MIC disaster (1984); Beirut
  Port explosion (2020)
- `references/output-templates.md` §11–§22 — Risk register; bowtie
  diagram; WHS strategy document; WHS function org chart + RACI; WHS
  annual plan; officer briefing pack; site walk record; annual report
  WHS section; AHRC positive duty compliance evidence map; permit-to-work
  templates (hot work, confined space, height, isolation); workers
  compensation claim review; hazard report form

### Changed

- `SKILL.md` §6 — Explicit Safety II / HOP / Forge Works positioning
  statement (previously implicit)
- `SKILL.md` routing table — 16 new entries for the new files and
  sections
- `SKILL.md` §12 reference file list — extended with the six new
  reference files
- `README.md` — Repository structure tree updated; roadmap trimmed and
  refreshed with next-tier opportunities; "Recently added (v1.3)" section
  added
- `ADAPTING.md` — Multi-tenancy workaround documented for consultants
  and shared-services WHS teams (three options including symlink approach
  and prompt-based override)
- `references/glossary.md` — Eight new categories: occupational hygiene,
  Modern Slavery / ESG / reporting, insurance, whistleblower, Indigenous
  / cultural heritage, disability and accessibility, strategy / function /
  crisis, AS/NZS standards index (~80 new entries total)

### Added — Repo hygiene

- `.gitignore` — Skip macOS noise (.DS_Store), packaged artefacts
  (*.skill, *.zip), editor files (.vscode, .idea, swap files), local env
  (.env, *.local), Python and Node tooling output
- `CHANGELOG.md` — Formal version history (this file)

### Total scope

- Skill content depth grew from 13,403 to 21,512 lines (~60% increase)
- File count grew from 24 to 30 files
- All 12 prior roadmap items + 9 follow-up gaps identified in audit closed

---

## [1.2.0] — 2026-05-27

### Added — Roadmap closure round

- `references/case-studies.md` (875 lines) — Worked summaries of seven
  landmark cases (Longford 1998, Texas City 2005, Macondo 2010, Pike River
  2010, Dreamworld 2016, Whakaari 2019, Grenfell 2017) with named-thinker
  analytical framing and usage guidance
- `references/sector-regimes.md` (1,281 lines) — Sector-specific regimes:
  mining (NSW/QLD/WA/SA), maritime (AMSA/NOPSEMA/Maritime NZ), aviation
  (CASA/CASR), rail (ONRSR/RSNL), healthcare biosafety (PC1-4, OGTR,
  radiation), defence (DSMS, DEFGRAM, explosive ordnance)
- `references/workplace-controls.md` (1,087 lines) — First aid (Code, AS
  2675, HLTAID units, AED), emergency preparedness/evacuation (AS 3745, ECO,
  drills), lone working/remote work, working from home/hybrid (Right to
  Disconnect, FDV intersection)
- `references/capability-culture.md` (649 lines) — Behavioural-based safety
  with named critiques (Dekker, Hopkins, Provan), maturity frameworks (Hudson,
  DuPont Bradley, IOGP, Heinrich critique), safety culture vs climate
  measurement

### Added — Existing-file expansions

- `references/legislation.md` §11 — Mandatory WHS training requirements by
  jurisdiction
- `references/legislation.md` §12 — Volunteer and unpaid worker coverage
- `references/legislation.md` §13 — International framework references
  (ILO C155/C187, US OSHA, UK HSE, EU OSH)
- `references/frameworks.md` §13 — WHS in M&A and due diligence

### Changed

- `SKILL.md` routing table — 10 new entries for the new files and sections
- `SKILL.md` §12 reference file list — extended with the new files
- `README.md` — repository structure tree updated; all 12 prior roadmap items
  marked addressed; new community-contribution opportunities listed
- `references/glossary.md` — 8 new categories (~90 new terms): case studies,
  sector regimes, workplace controls, capability/culture, training codes,
  international, M&A

### Total scope
- Skill content depth grew from 8,997 to 13,403 lines

---

## [1.1.0] — 2026-05-27

### Added — Major gap closure round

- `references/environment.md` (1,070 lines) — The EHS chapter that closed
  the WHS-vs-EHS positioning gap: AU/NZ environmental regulators, ISO 14001,
  EPA notification thresholds, dangerous goods storage, spill response,
  contamination, waste hierarchy, emissions/discharge licensing, biodiversity
  and Aboriginal heritage, climate-WHS intersection
- `references/compensation-rtw.md` (1,062 lines) — Workers compensation
  across AU state schemes (icare NSW, WorkSafe VIC, WorkCover QLD,
  ReturnToWorkSA, WorkSafe WA, WorkSafe TAS, NT, ACT/Cth Comcare) plus
  NZ ACC; premium mechanics, IMEs, suitable employment, RTW coordinator,
  psychological injury claims, presumptive provisions
- `references/inspections-audits-permits.md` (513 lines) — Workplace
  inspection program design, ISO 19011-based WHS audit methodology,
  permit-to-work systems, pre-task and point-of-work risk assessment tools
- `references/hazards.md` §9–§18 — Working at height, electrical safety
  and LOTO, confined space entry, mobile plant and pedestrian interface,
  hazardous chemicals operational detail, noise, hand-arm and whole-body
  vibration, plant safety and machine guarding, manual tasks and
  ergonomics, fatigue and fitness for work
- `references/legislation.md` §3.1–§3.9 — NZ promoted to first-class
  jurisdiction (ACC scheme, WEPR Regulations, ACoPs, NZ high-fatality
  sectors, Adventure Activities, geothermal/Whakaari context, Pike River
  + HSWA reform context, NZ industrial manslaughter, WorkSafe NZ
  enforcement and penalties in NZD)
- `references/legislation.md` §6 — Operational officer due diligence
  toolkit (briefing template, director-level safety walk format, due
  diligence calendar mapped to s 27 elements, evidence pack structure)
- `examples/` directory — Seven realised output examples: safety alert,
  toolbox talk, advisory note, ICAM executive summary, board paper
  extract, HiPo intelligence pack, plus README

### Changed

- `references/output-templates.md` — Section numbering and TOC fixed
  (sections 4-10 were misnumbered)
- `references/legislation.md` — Currency date stamps added to penalty
  tables (currency note: "as at January 2025; validate against current
  jurisdiction publications")
- `SKILL.md` routing table — Five new routing entries for the new files
- `SKILL.md` §12 reference file list — Extended
- `README.md` — Repository structure updated; roadmap items addressed
  marked
- `references/glossary.md` — Four new categories: Environment (EHS),
  Workers Compensation & RTW, Audit/Inspection/Permits, NZ-Specific

### Total scope
- Skill content depth grew from 4,421 to 8,997 lines

---

## [1.0.0] — 2026-05-27

### Added

- Initial publication of the WHS Professional skill
- `SKILL.md` (430 lines) — Entry point, routing table, foundational
  principles, tone and voice
- `references/legislation.md` (595 lines) — AU/NZ WHS legislation, key
  duties, notifiable incidents, enforcement and penalties, industrial
  manslaughter, regulators, Codes of Practice, psychosocial hazards and
  Respect@Work, inspector visits
- `references/frameworks.md` (648 lines) — Hierarchy of controls, SFAIRP,
  ISO 45001 clause map, Safety II/HOP, resilience engineering, critical
  risk management, board reporting, leading and lagging indicators,
  worker engagement, Forge Works Blueprint, named safety science thinkers
- `references/investigation.md` (480 lines) — ICAM methodology, 5-Why,
  contributing factors taxonomy, bowtie analysis, ICAM report template,
  common investigation pitfalls and cognitive biases, corrective action
  framework
- `references/hazards.md` (399 lines) — Engineered stone prohibition,
  respirable crystalline silica, asbestos, construction WHS (PC, WHSMP,
  HRCW, SWMS), drug and alcohol testing, working in heat, Major Hazard
  Facilities, 18 HRCW categories
- `references/output-templates.md` (567 lines) — Safety alert, toolbox
  talk, WHS advisory note, PIIN, alert vs bulletin, investigation report,
  SWMS, WHS policy, procedure, contractor WHS requirements brief
  templates
- `references/analytics.md` (373 lines) — Metric definitions and
  calculations, HiPo intelligence pack structure, CRO vs HiPo alignment,
  dashboard design, leading indicator design, EAP utilisation, board/ELT
  intelligence pack, Power BI patterns
- `references/programs.md` (392 lines) — Program design fundamentals,
  sustained campaign architecture, gamification principles, facilitator
  framework, frontline content strategy, engagement measurement, critical
  risk topic integration, program governance
- `references/company.md` (395 lines) — Organisation-specific template
  plus [organisation] [incident system] worked example
- `references/glossary.md` (142 lines) — Acronyms and frequently used
  terms across AU and NZ WHS practice
- `README.md` (332 lines) — Project overview, install/quick-start,
  example prompts, repository structure, contributing, disclaimer
- `ADAPTING.md` (313 lines) — Walkthrough for adapting company.md
- `DISCLAIMER.md` (149 lines) — Legal disclaimer (no legal advice etc.)
- `CONTRIBUTING.md` (101 lines) — Contribution guidelines
- `PUBLISHING.md` (258 lines) — GitHub publication walkthrough
- `LICENSE` — CC BY-SA 4.0

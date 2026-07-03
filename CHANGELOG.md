# Changelog

All notable changes to this skill are recorded here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); the
skill follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html) at
the level of capability tiers (MAJOR for new top-level scope or restructure;
MINOR for new reference files or substantial expansions; PATCH for fixes,
currency updates, and small additions).

---

## [Unreleased]

### Added

- **Guided adaptation interview** (`references/adaptation-interview.md`) —
  "I want to adapt this skill to my company" now triggers a structured
  ten-step interview mirroring the `company.md` Template §1–§10: one step at
  a time, document-extraction first (paste the risk standard / incident
  procedure and the skill pulls the answers), skippable steps with generic
  fallbacks, a short path (Steps 1, 3, 5), and assembly with per-setup apply
  instructions (claude.ai re-zip, Claude Project knowledge, or Claude Code
  file edit). Routed from the SKILL.md table, INDEX.md, and the frontmatter
  description
- `company.md` and `ADAPTING.md` re-pointed at the interview as the
  recommended path; README "adapt to your organisation" section rewritten
  around it

---

## [1.6.0] — 2026-07-03

### Contributor review release — efficiency, verification discipline, automation

Actions an external contributor review (with thanks to Yakov): SKILL.md
consolidation, an operative currency-verification rule, bundled deterministic
resources, an automated regression suite, and release hygiene in CI. No new
top-level scope.

#### Changed

- **`SKILL.md` consolidated (v1.6.0)** — the ~60-row task-routing table (§1)
  and the 23-row file-coverage table (§12) were near-duplicates; merged into a
  single per-file routing table preserving every keyword and section anchor
  from both (~19% smaller entry point on every activation)
- **Hard currency rule (§3)** — the passive "always validate" disclaimer is
  now an operative instruction: penalty amounts, penalty unit values,
  commencement dates, and prosecution/appeal status must be verified against
  a primary source before quoting when web search is available; otherwise
  quoted with the reference file's "as at" date shown and flagged
- **Verification footer (§5)** — every regulatory output now ends with a
  block listing statutes cited and whether figures were web-verified or
  carried from the reference "as at" date
- **Multi-tenant use documented** — the Claude Project knowledge pattern is
  now the documented multi-tenant path (`ADAPTING.md`, new
  `company.md` § Multi-tenant use), closing the roadmap item
- **README** — install path now points at the CI-built Release artefact as
  the primary route; repository structure updated for the new resources

#### Added

- **`scripts/frequency_rates.py`** — deterministic TRIFR / LTIFR / MTIFR /
  RWIFR / AIFR / severity-rate calculator; point-in-time from CLI flags or a
  rolling 12-month series anchored to the last closed period from a monthly
  CSV; default basis 1,000,000 hours (AU convention), `--basis 200000` for
  the US convention. Numerator conventions locked to `analytics.md` /
  `glossary.md`: TRIFR = Fatality + LTI + RWI + MTI; LTIFR = LTIs only;
  AIFR includes FAIs
- **`assets/penalty_units.json`** — penalty unit values by jurisdiction with
  effective dates, indexation mechanism, source, and `verified_as_at`;
  unverified jurisdictions ship as explicit `verify_before_use` entries
- **`references/INDEX.md`** — compact keyword → file → section lookup across
  all reference files, checked by the validator's cross-reference gate
- **`promptfooconfig.yaml`** — all 28 `EVALS.md` regression evals ported to
  an automated suite (`npx promptfoo@latest eval`); `EVALS.md` remains the
  human-readable ledger
- **SKILL.md §11 Scripts & Assets** — instructs running the calculator and
  looking up penalty units rather than computing in-context

#### CI / release hygiene

- **Version gate** — the packaging workflow fails if the `SKILL.md`
  frontmatter version does not match the release tag
- **Shipping guard** — the workflow fails if real-organisation identifiers
  are detected anywhere in the skill folder (word-boundary match)
- **Release attachment** — the validated skill archive is now attached to
  the GitHub Release automatically on every version tag
- **Validator** — cross-reference resolution extended to `INDEX.md`'s
  `keywords | file | §N` row format

#### Removed

- Historical references to the pre-v1.4.0 real-organisation worked example
  removed from repository documentation; repository history rewritten to
  remove the pre-sanitisation `company.md` content

---

## [1.5.0] — 2026-06-16

### Accuracy, consistency, and efficiency release

A full dual-lens audit (WHS-professional + technical) of the corpus was
actioned: 176 findings reviewed, the highest-risk legal/factual claims
web-verified against primary sources, and corrections applied across all 22
reference files, the examples, the entry point, and the build pipeline. No new
top-level scope.

#### Corrected (web-verified against primary sources)

- **NSW POEO penalties** (`environment.md`) updated to the Environment
  Protection Legislation Amendment (Stronger Regulation and Penalties) Act 2024
  (NSW): Tier 1 $10M/$2M, Tier 2 and s 148 failure-to-notify $4M/$1M, plus the
  daily continuing-offence penalty
- **NSW WHS Regulation 2025** (`legislation.md`, `SKILL.md`) commencement
  corrected from "1 Jan 2026" to **22 August 2025** (2017 Regulation repealed
  1 September 2025; Silica Worker Register from 1 October 2025)
- **NSW compensation 21-day liability timeframe** (`compensation-rtw.md`)
  re-anchored to the statutory source — s 274 / s 279 / s 283 WIM Act 1998 —
  rather than a SIRA standard
- **Lead 30 µg/dL** (`specialist-topics.md`) relabelled as the medical removal
  level (reg 415, Part 7.2), not a Safe Work Australia notification trigger
- **Commonwealth insurance ban** (`specialist-topics.md`) corrected to
  ss 272A–272B, inserted by the WHS Amendment Act 2023 (Cth) (not "Closing
  Loopholes")
- **Whistleblower criminal penalties** (`whistleblower.md`) completed with the
  omitted fine quanta (s 1317AC, s 1317AAE)
- **Tasmania industrial manslaughter** (`legislation.md`) corrected to the Work
  Health and Safety Amendment (Safer Workplaces) Act 2024 (Tas); *DPP v LH
  Holding* corrected to the Supreme Court of Victoria; NSW Category 1 maximum
  corrected to $10,424,982; anti-slavery commissioners (Cockayne, Evans) verified
- **Hierarchy of controls** (`investigation.md`) aligned to WHS Reg 36(2):
  substitution / isolation / engineering sit at the same statutory level

#### Consistency (single source of truth)

- **TRIFR / recordable set** reconciled across `analytics.md`, `glossary.md`, and
  `company.md` (RWI recordable, with an OSHA-origin provenance note)
- **Psychosocial hazard list** reconciled to the canonical 14 (SWA Code of
  Practice 2022) across `SKILL.md`, `legislation.md`, and `frameworks.md`
- **Risk-matrix legends** defined in `case-studies-everyday.md`; `company.md`
  consequence/severity LTI thresholds harmonised

#### Efficiency

- **`SKILL.md` slimmed ~20%** (≈1,800 tokens saved on every load): trigger-first
  description, §3 jurisdiction converted to a non-citable index, §6–§10 collapsed
  to stubs + pointers, §12 reference catalogue compressed to a table, glossary
  routing row added

#### Tooling

- **`scripts/validate.py`** added and wired into CI (`package.yml`) as a gate
  before packaging: frontmatter validation, reference + section-link resolution,
  regression guards (MUST-NOT strings), hygiene, and AU-English checks
- `EVALS.md` expanded with regressions for the v1.5.0 corrections

#### Deferred

- Physical split of the three monolith files (`sector-regimes.md`,
  `legislation.md`, `hazards.md`) into per-domain files is deferred to v1.6.0,
  where the ~70 inbound section-numbered cross-references can be re-pointed and
  validated atomically by the new CI reference resolver.

---

## [1.4.0] — 2026-06-10

### Correction and currency release

A full audit of the corpus (~125 findings) was actioned in this release.
No new top-level scope; the focus was factual accuracy, regulatory
currency to mid-2026, and packaging hygiene.

### Fixed

- Statutory citation tables across the corpus — officer due diligence
  (s 27, not s 26), HSWA officer duty (s 44) and Category 1 (s 47),
  Cth industrial manslaughter (WHS Act s 30A), psychosocial regulations
  (model WHS Regs rr 55A–55D), construction project threshold (Reg 292,
  $250K) and principal contractor appointment (Reg 293) / duties
  (Regs 308–315), SWMS duty (Reg 299), HRWL classes (Schedule 3, with
  Schedule 4 carrying competency requirements)
- Industrial manslaughter table — jurisdictions, penalties, commencement
  dates corrected
- Penalty quanta — Commonwealth penalty unit $330 from 7 November 2024;
  whistleblower penalties split into criminal offences (victimisation up
  to 2 years imprisonment; confidentiality breach 6 months) and civil
  penalties (individual 5,000 PU; body corporate the greater of 50,000 PU
  / 3× benefit / 10% turnover capped at 2.5M PU)
- Whistleblower section mapping — victimisation prohibition s 1317AC,
  civil remedy gateway s 1317AD (shifted onus s 1317AD(2B)), orders
  s 1317AE; confidentiality investigation exception reworded (information
  likely to identify, never the identity itself)
- State PID landscape — SA now Public Interest Disclosure Act 2018
  (1993 Act repealed 1 July 2019; OPI/ICAC SA oversight); NT PID Act 2008
  repealed (protections under the ICAC (NT) regime since 2018)
- Case-study corrections — including the Whakaari appeal outcome
  (conviction quashed February 2025, [2025] NZHC 288) and Pike River
  status (bodies never recovered; workings never re-entered)
- High-risk work licensing tables — slewing crane classes (C2 ≤20 t,
  C6 ≤60 t, C1 ≤100 t, C0 open) and related entries
- Standards index — AS 2675 relabelled (portable consumer kits, 1983;
  workplace kit contents per the SWA First Aid Code), AS/NZS 4452 (toxic
  substances storage) replacing the AS 4081 attribution, AS 4839
  (portable oxy-fuel gas systems), AS 1216 (DG class labels only;
  workplace pictograms are GHS), AS 4775-2007 designation reconciled,
  AS/NZS 4979 removed; RIIWHS204 decoupled from HRWL
- Procurement reference — NICNAS removed (abolished 2020; AICIS holds no
  incident data) in favour of regulator prosecution registers and SWA
  statistics; Pegasus noted as acquired by Avetta (2022; now Avetta One /
  legacy Onsite Track Easy); regulator registers separated from
  commercial platform status
- Glossary — MTI ">3 allied health sessions" marked as an organisational
  convention (not AS 1885.1); CRO redefined (Chief Risk Officer, with
  Critical Risk Owner/Observation usage flagged); example prompt fixed to
  the $250K construction project threshold

### Changed

- Currency to mid-2026 — NSW WHS Regulation 2025 and standalone SafeWork
  NSW; NSW workers compensation psychological injury reforms (2025–26);
  WA Workers Compensation and Injury Management Act 2023; Victorian
  psychological health regulations; EPBC reform Acts 2025; WES → WEL
  transition (1 December 2026); NZ HSWA Amendment Bill
- `README.md` — repository tree updated (PUBLISHING.md, EVALS.md, CI
  workflow); packaging instructions replaced with clean-archive commands;
  roadmap rewritten (delivered items removed, new contribution targets);
  Ron Westrum added to acknowledged thinkers
- `PUBLISHING.md` — stale 9-file inventory replaced with a pointer to the
  README repository tree; packaging commands updated with archive-hygiene
  exclusions
- `CONTRIBUTING.md` — style rules aligned to the corpus as written

### Added

- Road transport / HVNL Chain of Responsibility section
  (`references/sector-regimes.md` §14)
- Regulator-compelled evidence — s 155 notices, s 171/172 powers
  (`references/legislation.md`)
- Enforceable undertakings and limitation periods
- ISO 45003, psychosocial risk controls, and governance / assurance
  sections (`references/frameworks.md` §14–§15)
- SIF/pSIF analytics treatment and glossary entries
- WHS monetary penalty insurance bans (model WHS Act s 272A)
- Fair Work Act Part 3-5A sexual harassment chain
- Regulator notification phone script template
  (`references/output-templates.md` §23)
- Whistleblower additions — PID Amendment (Review) Act 2023 (Cth);
  anonymous disclosure protection statement; s 1317AAD public interest /
  emergency disclosure preconditions; ASIC v TerraCom (2025) case anchor
- Commonwealth Anti-Slavery Commissioner (established 2024) noted in the
  Modern Slavery passage
- Glossary terms — EU (enforceable undertaking), Category 1/2/3 offences,
  HAZOP, FMEA, SDS, WEL, SIF/pSIF, CoR, NHVR, CoP usage note; HVNL entry
  expanded
- `EVALS.md` — regression evaluation prompts tied to known fixed errors
- `.github/workflows/package.yml` — CI packaging workflow building a
  clean skill archive on tagged releases
- `SKILL.md` frontmatter `version` field

### Security and privacy

- Fictionalised company example — the worked example in
  `references/company.md` is now Meridian Facilities Group, a fictional
  organisation; real-organisation content removed from the corpus
- Packaging hygiene — archives now exclude `.DS_Store` and `__MACOSX/`
  entries; documentation warns against macOS Finder "Compress"

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
  plus a worked example (superseded in v1.4.0 by the fictional Meridian
  Facilities Group example)
- `references/glossary.md` (142 lines) — Acronyms and frequently used
  terms across AU and NZ WHS practice
- `README.md` (332 lines) — Project overview, install/quick-start,
  example prompts, repository structure, contributing, disclaimer
- `ADAPTING.md` (313 lines) — Walkthrough for adapting company.md
- `DISCLAIMER.md` (149 lines) — Legal disclaimer (no legal advice etc.)
- `CONTRIBUTING.md` (101 lines) — Contribution guidelines
- `PUBLISHING.md` (258 lines) — GitHub publication walkthrough
- `LICENSE` — CC BY-SA 4.0

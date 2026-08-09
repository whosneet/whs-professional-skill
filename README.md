# WHS Professional Skill for Claude

A Claude skill that turns the assistant into an experienced Work Health and Safety
(WHS) / Occupational Health and Safety (OHS) professional, calibrated to Australian
and New Zealand regulatory and practice frameworks.

The skill covers coordinator through manager-level tasks: incident investigation
(ICAM, 5-Why), risk assessments, safety alerts, toolbox talks, legislative
advice, industrial manslaughter and officer due diligence, inspector visits,
construction WHS, ISO 45001, Safety II / Human and Organisational Performance,
psychosocial hazards and the Respect@Work positive duty, engineered stone and
respirable crystalline silica, board and ELT reporting, WHS analytics, program
design, governance, and named safety science citation (Reason, Dekker, Hollnagel,
Conklin, Edmondson, Provan, Hopkins, Weick).

It is designed to be **organisation-agnostic at the framework layer** and
**adaptable to your specific organisation** via a single editable reference file
(`company.md`).

---

## Table of Contents

- [What this is and is not](#what-this-is-and-is-not)
- [Quick start — Option A: install in Claude.ai](#quick-start--option-a-install-in-claudeai)
- [Quick start — Option B: install via Claude Code](#quick-start--option-b-install-via-claude-code)
- [Quick start: adapt to your organisation](#quick-start-adapt-to-your-organisation)
- [Example prompts](#example-prompts)
- [Repository structure](#repository-structure)
- [Adapting in depth](#adapting-in-depth)
- [Contributing](#contributing)
- [Disclaimer & licence](#disclaimer--licence)
- [Roadmap](#roadmap)
- [Attribution & acknowledgements](#attribution--acknowledgements)

---

## What this is and is not

**This is**:
- A skill that loads into Claude (claude.ai web/desktop/mobile) and adjusts the
  assistant's behaviour for WHS / OHS tasks
- A set of structured reference files covering AU and NZ regulatory frameworks,
  investigation methodology, hazard-specific guidance, output templates,
  analytics patterns, program design, and named safety science citations
- A template (`company.md`) you fill in once with your organisation's context,
  which then anchors all subsequent outputs to your specific configuration

**This is not**:
- Legal advice. See `DISCLAIMER.md`.
- A substitute for current regulatory text. Codes, regulations, and penalty
  quanta change frequently — always validate against the source for your
  jurisdiction.
- A compliance certification or audit tool.
- A replacement for a qualified WHS professional in matters involving serious
  injury, fatality, or regulatory action.
- A global resource. The skill is built around AU and NZ frameworks; some
  content is broadly applicable, but the regulatory layer assumes those
  jurisdictions.

---

## Quick start — Option A: install in Claude.ai

Use this option if you access Claude through a web browser at
<https://claude.ai>, through the **Claude Desktop app**, or through
**Cowork**. You will download a file and upload it to your account once —
skills attach to your Claude account, so a single claude.ai upload makes the
skill available across web, Desktop, and Cowork sessions.

> For the bundled calculator (`scripts/frequency_rates.py`) to run on these
> surfaces, code execution (the analysis tool) must be enabled in your
> settings. Without it the skill still works — it shows its arithmetic in
> full and flags figures for verification instead (see SKILL.md §11).

The skill installs as a single packaged archive — a `.zip` of the skill
folder. Release assets also include a `.skill` copy: it is the same ZIP
under optional legacy naming.

**Step 1 — Download the skill file**
On this repository's GitHub page, navigate to the **Releases** section (right
sidebar) and download the latest `whs-professional.zip` (or the identical
`whs-professional.skill`). Release artefacts are built, validated, and
attached automatically by CI on every tagged release — always prefer them
over packaging by hand (kept as a fallback under
[Packaging](#packaging-the-skill-yourself) below).

**Step 2 — Open Claude.ai settings**
1. Go to <https://claude.ai>
2. Sign in (Claude Pro or Team account required for skills)
3. Click your profile → **Settings**
4. Find the **Skills** or **Capabilities** section

**Step 3 — Upload the skill**
1. Click **Add skill** or **Upload skill**
2. Select the `whs-professional.zip` (or `.skill`) file you downloaded
3. Confirm install

**Step 4 — Test it**
Open a new conversation and try:

> "Walk me through investigating a near miss where a worker had a slip in a wet
> kitchen but didn't injure themselves. Use ICAM."

If the skill activated, the response will reference ICAM methodology, PEEPO
domains, contributing factors taxonomy, and corrective action framework. It
will not invent specific severity classifications (since you haven't populated
`company.md` yet).

---

## Quick start — Option B: install via Claude Code

Use this option if you use **Claude Code** — Anthropic's desktop or
command-line app. There are no files to download or upload. Three short
commands and you are done.

> **Not sure if you have Claude Code?**
> Look for a Claude icon in your Applications folder (Mac) or Start menu
> (Windows). If you only use Claude through a browser at claude.ai, use
> Option A above instead.
> Claude Code is free to download at <https://claude.ai/code>.

---

### Step 1 — Add the marketplace

Open Claude Code and paste the following into the message box, then press
**Enter**:

```
/plugin marketplace add whosneet/whs-professional-skill
```

This tells Claude Code where to find the WHS Professional skill. **You only
need to do this once** — it stays registered on your computer.

You will see a confirmation message when it is done. It takes about
five seconds.

---

### Step 2 — Install the skill

Still in Claude Code, paste this and press **Enter**:

```
/plugin install whs-professional@whs-professional
```

Claude Code will download and install the skill. Wait for the confirmation
message — it usually takes under ten seconds.

---

### Step 3 — Use the skill

You can now start a WHS session at any time by typing:

```
/whs-professional:whs-professional
```

Claude will respond as an experienced WHS/OHS professional. Try one of the
[example prompts](#example-prompts) below to test it.

---

### Keeping the skill up to date

The skill is updated periodically with regulatory corrections and new
content. To pull the latest version, type:

```
/plugin marketplace update
```

That is all — no downloading or re-uploading required.

---

### See what you have installed

To view all your installed plugins and skills at any time:

```
/plugin list
```

---

## Quick start: adapt to your organisation

The skill works out of the box for generic AU/NZ WHS tasks. To make it
**anchor to your organisation's specific configuration** — your risk matrix,
severity classifications, document codes, incident management system, named
programs, governance cadence — you populate `references/company.md`.

The file ships with a worked example — the fictional **Meridian Facilities
Group**, left in as calibration reference — and a template structure above it.

**Two ways to do this:**

**Option A — The guided interview (recommended)**

Once the skill is installed, just tell Claude:

> "I want to adapt this skill to my company."

The skill runs a built-in **ten-step interview**. It explains what it needs
and what documents to have handy, then works through the sections one at a
time — Step 1 organisation identity, Step 2 management system and document
numbering, Step 3 risk matrix, Step 4 hierarchy-of-controls framing, Step 5
incident classification and notification, Step 6 templates and forms, Step 7
systems, Step 8 critical risks, Step 9 programs, Step 10 governance.

Along the way you can:
- **Paste or upload source documents** (risk management standard, incident
  procedure, document register) and Claude extracts the answers instead of
  asking questions
- **Skip any step** you don't have — the skill falls back to generic defaults
  for that section
- **Take the short path** (Steps 1, 3 and 5 only) if you're time-poor

At the end it assembles the finished `company.md` content and gives you
apply instructions for your setup — replace-and-re-zip for claude.ai, a
Project-knowledge document for consultants, or a direct file edit for
Claude Code.

**Option B — Edit `company.md` directly**

1. Open `whs-professional/references/company.md`
2. Read the "Template" section at the top (sections 1–10)
3. Replace the "Active Reference" section (the fictional Meridian Facilities
   Group example) with your organisation's equivalent content
4. Save
5. Re-package the skill (see [Packaging](#packaging-the-skill-yourself))

See `ADAPTING.md` for the manual walkthrough — the questions each section
answers and where to find the information inside your organisation. It
follows the same 1–10 structure as the interview.

---

## Example prompts

**Investigation**
- "I need to investigate a HiPo where a forklift nearly struck a pedestrian in
  a warehouse aisle. Produce an ICAM-structured investigation plan including
  PEEPO information-gathering questions and likely contributing factors to test."
- "Draft an executive summary for an ICAM report on a fatal electrical incident.
  Use the structure in the skill. I'll fill in the details."

**Legislative & regulatory**
- "Explain the differences in industrial manslaughter exposure between NSW, QLD,
  and Victoria. Include penalty quanta, limitation periods, and procedural
  differences."
- "Inspector arrived on site today — what should the site manager do in the next
  hour, and what should we have ready for them?"
- "Draft a board paper section explaining the company's exposure under the
  Respect@Work positive duty (SDA s 47C) and what we need to do to discharge it."

**Operational hazards**
- "Outline the controls and SWMS requirements for engineered stone removal work
  in a kitchen refurbishment in NSW."
- "Heat stress management plan for outdoor crews working in Western Sydney over
  summer. Include WBGT thresholds and acclimatisation periods."
- "Draft a toolbox talk on respirable crystalline silica for construction
  workers. 12 minutes, conversational, frontline language."

**Risk & frameworks**
- "Critical control verification approach for working at heights at a remote
  electrical maintenance contract. Include cadence, evidence requirements, and
  reporting structure."
- "Compare Reason's Swiss Cheese model with Dekker's New View — when do I use
  each for incident analysis?"

**Programs & engagement**
- "Design a 6-week sustained engagement campaign on critical risk awareness
  for a workforce of 800. Mostly outdoor maintenance crews."
- "Why are TRIFR and LTIFR poor measures of safety performance? Give me the
  argument I can take to an ELT."

**Analytics & reporting**
- "Structure a HiPo intelligence pack for monthly ELT distribution. 8 pages
  maximum."
- "Draft DAX patterns for a Power BI WHS dashboard that uses rolling 12-month
  hours anchored to the last closed period."

**Governance**
- "WHS Management Plan structure for a $4M construction project (well above
  the $250K threshold at which a principal contractor must be appointed).
  Include PC duties, HRCW management, SWMS workflow, induction."
- "Lessons Learnt register design that captures during projects, not just at
  close."

---

## Repository structure

```
whs-professional/                  # The Claude skill folder
├── SKILL.md                       # Skill entry point + routing table
├── examples/                      # Worked realised outputs (calibration material)
│   ├── README.md
│   ├── 01-safety-alert-electrical-near-miss.md
│   ├── 02-toolbox-talk-working-at-height.md
│   ├── 03-whs-advisory-note-respect-at-work-positive-duty.md
│   ├── 04-icam-executive-summary-forklift-near-miss.md
│   ├── 05-board-paper-extract-hipo-intelligence.md
│   └── 06-hipo-intelligence-pack-page.md
├── scripts/
│   └── frequency_rates.py         # Deterministic TRIFR/LTIFR/MTIFR/RWIFR/AIFR
│                                  #   + severity calculator; rolling 12-month series
├── assets/
│   └── penalty_units.json         # Penalty unit values by jurisdiction with
│                                  #   effective dates, sources, verification dates
└── references/
    ├── INDEX.md                   # Keyword → file → section lookup across
    │                              #   all reference files
    ├── company.md                 # ★ Your organisation's context (edit this)
    ├── adaptation-interview.md    # Guided ten-step setup: "adapt this skill
    │                              #   to my company" runs this interview
    ├── legislation.md             # AU/NZ WHS legislation incl. expanded NZ
    │                              #   coverage (HSWA, ACC, WEPR, Pike River,
    │                              #   geothermal, NZ industrial manslaughter);
    │                              #   industrial manslaughter, inspector playbook,
    │                              #   Respect@Work, officer due diligence toolkit
    ├── frameworks.md              # ISO 45001, SFAIRP, Safety II/HOP/Forge Works,
    │                              #   named safety science thinkers
    ├── investigation.md           # ICAM, 5-Why, bowtie, contributing factors,
    │                              #   cognitive biases
    ├── hazards.md                 # Engineered stone, RCS, asbestos, construction,
    │                              #   D&A, heat, MHF, height, electrical/LOTO,
    │                              #   confined space, mobile plant, hazardous
    │                              #   chemicals, noise, vibration, plant safety,
    │                              #   manual tasks, fatigue
    ├── environment.md             # EHS environmental chapter — AU/NZ regulators,
    │                              #   ISO 14001, EPA notification, dangerous goods,
    │                              #   spills, waste, emissions, biodiversity,
    │                              #   heritage, climate-WHS intersection
    ├── compensation-rtw.md        # Workers comp across AU schemes + NZ ACC,
    │                              #   premium mechanics, IMEs, suitable employment,
    │                              #   RTW coordinator, psych claims, presumptive
    │                              #   provisions
    ├── inspections-audits-permits.md  # Workplace inspections, ISO 19011 audits,
    │                              #   permit-to-work systems, pre-task tools
    ├── case-studies.md            # Eleven landmark cases: Longford, Texas City,
    │                              #   Macondo, Pike River, Dreamworld, Whakaari,
    │                              #   Grenfell, Costa Concordia, Ranger Uranium,
    │                              #   Bhopal, Beirut Port; named-thinker framing
    ├── sector-regimes.md          # Mining, maritime, aviation, rail, healthcare
    │                              #   biosafety, defence, petrochemical,
    │                              #   telecommunications, agriculture, hospitality,
    │                              #   education, retail, road transport (HVNL /
    │                              #   Chain of Responsibility) — sector-specific
    │                              #   regimes that sit alongside or outside the
    │                              #   WHS Act
    ├── workplace-controls.md      # First aid, emergency prep / evacuation,
    │                              #   lone working / remote work, working from
    │                              #   home / hybrid (Right to Disconnect, FDV)
    ├── capability-culture.md      # Behavioural-based safety (with critiques),
    │                              #   maturity frameworks (Hudson, Bradley, IOGP),
    │                              #   culture vs climate measurement
    ├── strategy-function.md       # WHS strategy, function design, budget
    │                              #   economics, leadership, crisis management
    ├── specialist-topics.md       # Occupational hygiene, workplace mental
    │                              #   health programs, Modern Slavery Act,
    │                              #   ESG/WHS, insurance arrangements
    ├── diversity-inclusion.md     # Indigenous workforce, reasonable
    │                              #   adjustments, neurodivergent, multi-
    │                              #   language, gendered violence depth
    ├── whs-procurement.md         # WHS in procurement, supplier evaluation,
    │                              #   tender response, contractor management,
    │                              #   Modern Slavery DD overlap
    ├── whistleblower.md           # Corporations Act 9.4AAA, PIDA, state PID
    │                              #   Acts, WHS reporting intersection
    ├── case-studies-everyday.md   # Forklift, manual handling, psychosocial,
    │                              #   electrical, slip/trip, chemical, fatigue
    │                              #   — everyday cases for training and ICAM
    ├── output-templates.md        # Safety alert, toolbox talk, advisory note,
    │                              #   investigation report, risk register,
    │                              #   bowtie, WHS strategy, RACI, annual plan,
    │                              #   officer briefing, site walk, annual
    │                              #   report, AHRC evidence map, PTW, claim
    │                              #   review, hazard report templates
    ├── analytics.md               # KPIs, dashboards, Power BI patterns, board
    │                              #   intelligence pack structure
    ├── programs.md                # Program design, gamification, facilitator
    │                              #   frameworks, sustained campaign architecture
    └── glossary.md                # WHS acronyms and terminology

README.md                          # This file
ADAPTING.md                        # Detailed walkthrough for adapting company.md
DISCLAIMER.md                      # Legal disclaimer (no legal advice etc.)
CONTRIBUTING.md                    # How to contribute
PUBLISHING.md                      # GitHub publication walkthrough
EVALS.md                           # Regression evaluation ledger (the "why" of each eval)
promptfooconfig.yaml               # Automated regression suite (npx promptfoo eval)
LICENSE                            # Licence terms
CHANGELOG.md                       # Version history of the skill
scripts/
└── validate.py                    # CI validation gate: frontmatter, refs, versions
.gitignore                         # Git ignore patterns (artefacts, IDE noise)
.claude-plugin/
├── plugin.json                    # Claude Code plugin manifest (name, version)
└── marketplace.json               # Marketplace listing (/plugin marketplace add)
.github/
└── workflows/
    └── package.yml                # CI: validates, guards, builds and attaches the
                                   #   skill archive to the Release on tagged releases
```

---

## Adapting in depth

See `ADAPTING.md` for a full section-by-section walkthrough of `company.md`,
including:
- The exact questions to answer for each section
- Where to find each piece of information inside your organisation
- AI prompts you can use to accelerate population
- Validation checks once you've filled it in

---

## Packaging the skill yourself

Claude accepts a **`.zip` archive containing the single top-level skill
folder** (`whs-professional/` with `SKILL.md` inside it). Renaming the
archive to `.skill` is optional legacy naming from earlier upload flows —
check the current wording at <https://support.claude.com> if in doubt; the
`.zip` works.

**Using the command line (recommended):**
```bash
cd path/to/repo
zip -r whs-professional.zip whs-professional -x "*.DS_Store" -x "__MACOSX/*"
```

On macOS you can instead use `ditto`, which never embeds AppleDouble files:
```bash
ditto -c -k --norsrc whs-professional whs-professional.zip
```

> **Warning — avoid macOS Finder "Compress"**: right-clicking the folder and
> choosing Compress adds `__MACOSX/` and AppleDouble (`._*`) entries to the
> archive, which can break the skill upload. Use one of the CLI commands
> above, or download the clean artifact built by the GitHub Action
> (`.github/workflows/package.yml`) on each tagged release.

---

## Contributing

Contributions welcome — bug fixes, content corrections, regulatory updates,
new hazard chapters, jurisdiction expansions. See `CONTRIBUTING.md` for
guidelines.

The roadmap items below are explicit invitations for community contribution.

---

## Disclaimer & licence

This skill produces general guidance, not legal advice. WHS and OHS
legislation, codes, and standards change frequently. Always validate output
against the current text of the relevant Act, Regulation, and Code of Practice
for your jurisdiction before acting on it. See `DISCLAIMER.md` for full terms.

Licensed under [Creative Commons Attribution-ShareAlike 4.0 International
(CC BY-SA 4.0)](./LICENSE). You may use, adapt, and redistribute the skill
provided you attribute the source and license derivatives under the same terms.

The Forge Works Blueprint references in this skill summarise publicly available
concepts from Dr David Provan's body of work. Forge Works is a registered
consultancy — refer to <https://forgeworks.com> for the authoritative source.
This skill is not endorsed by or affiliated with Forge Works.

---

## Roadmap

These topics are not currently covered (or only lightly covered) and represent
opportunities for community contribution:

- **Case study expansion** — Wittenoom asbestos, Montara blowout (2009),
  Hazelwood mine fire (2014), Beaconsfield rockfall (2006), Cave Creek
  platform collapse (1995, NZ), Waterfall rail accident (2003), and the
  first industrial-manslaughter prosecutions; plus everyday cases: fall
  from height, confined space entry, LOTO failure, yard truck/pedestrian
  interface, heat illness
- **Sector deepening v3** — forestry, waste and recycling, electrical
  supply / utilities, renewables (including battery energy storage
  systems), commercial fishing, security, emergency services
- **Hazard chapters** — lead (model WHS Regulations Part 7.2, including
  the 2022 blood lead level reductions), diesel particulate matter,
  welding fume depth, lithium-ion batteries, UV / solar exposure, abrasive
  blasting, formwork and falsework, occupational diving, Q fever and
  zoonoses
- **Investigation depth** — ICAM organisational factor type (OFT) codes,
  fatality first-24-hours / police / coroner protocol, STEP / Tripod /
  HFACS methodologies, investigation quality assurance, restorative
  practice after harm
- **Compensation depth** — self-insurance licensing, cross-border
  state-of-connection rules, death benefits, NSW Dust Diseases scheme,
  Seacare
- **Analytics depth** — predictive analytics ethics, confidence intervals
  and funnel plots for rate comparison, exposure-based normalisation
- **Additional templates** — induction checklist, HSC committee charter,
  audit report, management review agenda, emergency response plan,
  training needs analysis matrix
- **Specialist topics v2** — RESP-FIT respiratory fit-testing depth,
  ototoxic substances and the OTO notation, radiation safety, hyperbaric
  work
- **Diversity & inclusion v2** — young and ageing workers, menopause,
  LGBTQIA+ psychosocial safety, workplace adjustment passports
- **AI safety and WHS** — AI in WHS analytics, bias risks in predictive
  safety, computer vision for guarding, wearables for fatigue and
  proximity, drones for inspection
- **Continuous improvement methodology for WHS** — Lean, Six Sigma,
  Theory of Constraints applied to safety improvement programs
- **WHS in procurement v2** — sector-specific overlays (resources tender
  WHS sections, construction tender WHS sections, government tender WHS
  sections)
- **Multi-tenant company.md file mechanism** — an in-package selector for
  consultants maintaining configurations across multiple clients. The
  documented path is now the Claude Project knowledge pattern (see
  `ADAPTING.md` — closed in v1.6.0); an in-package file mechanism remains
  open for contribution
- ~~**Utility scripts**~~ — ✓ closed in v1.6.0: `scripts/frequency_rates.py`
  (frequency rate calculator) and `assets/penalty_units.json` (penalty unit
  lookup); further calculators welcome

### Recently added (v1.8.0 — August 2026)

v1.8.0 is an accuracy and optimisation release built on a full-corpus audit:

- ✓ **Full-corpus audit actioned** — a 16-agent deep-read, cross-file
  consistency sweep, and primary-source web-verification pass produced
  ~230 findings (`AUDIT-2026-08-08.md`, retained as the closed tracker);
  every finding fixed, including 14 practitioner-facing factual errors,
  ~70 web-verified statute/standard corrections, and the realignment of
  the worked examples to the Meridian configuration
- ✓ **Multi-surface optimisation** — `sector-regimes.md` compressed under
  the 2,000-line single-read boundary; section-targeted loading guidance
  for large files; a no-code-execution fallback for the bundled
  calculator; install docs now cover claude.ai web, Claude Desktop,
  Cowork, and Claude Code explicitly
- ✓ **Tooling hardening** — `scripts/validate.py` now checks description
  length semantics, manifest version sync, packaged-reference integrity,
  and carries seven new regression guards plus an official-titles spelling
  allowlist (0 warnings standing); CI verifies all three version fields at
  tag time; the promptfoo evals were re-pointed at the files that actually
  carry the asserted facts

### Recently added (v1.7.0 — July 2026)

v1.7.0 makes adapting the skill conversational:

- ✓ **Guided adaptation interview** — telling the skill *"I want to adapt
  this skill to my company"* now runs a built-in ten-step interview
  (`references/adaptation-interview.md`) mirroring the `company.md` template:
  one step at a time, document-extraction first, skippable steps, a short
  path for the time-poor, and final assembly with apply instructions for
  claude.ai, Claude Projects, or Claude Code
- ✓ `company.md`, `ADAPTING.md`, and this README re-pointed at the interview
  as the recommended adaptation path

### Recently added (v1.6.0 — July 2026)

v1.6.0 actions an external contributor review (with thanks to Yakov):
efficiency, verification discipline, and automation. Highlights (full detail
in `CHANGELOG.md`):

- ✓ **SKILL.md consolidation** — the task-routing and file-coverage tables
  merged into a single per-file routing table (~19% smaller entry point,
  no loss of routing coverage)
- ✓ **Hard currency rule** — penalty amounts, penalty unit values,
  commencement dates, and prosecution/appeal status must be web-verified
  against a primary source before quoting (or carried with the reference
  "as at" date and flagged); every regulatory output now ends with a
  verification footer
- ✓ **Bundled resources** — `scripts/frequency_rates.py` (deterministic
  TRIFR/LTIFR/MTIFR/RWIFR/AIFR + severity calculator with rolling 12-month
  series), `assets/penalty_units.json` (penalty unit values with effective
  dates and sources), `references/INDEX.md` (keyword → file → section lookup)
- ✓ **Automated regression suite** — all 28 EVALS.md evals ported to
  `promptfooconfig.yaml` (`npx promptfoo@latest eval`); EVALS.md remains the
  human-readable ledger
- ✓ **Release hygiene** — CI now verifies the SKILL.md version matches the
  release tag, guards against real-organisation identifiers shipping in the
  package, and attaches the skill archive to the GitHub Release automatically
- ✓ **Multi-tenant documentation** — the Claude Project knowledge pattern is
  now the documented path for consultants and multi-divisional groups

### Recently added (v1.5.0 — June 2026)

v1.5.0 is an accuracy, consistency, and efficiency release built on a
full dual-lens audit of the corpus. Highlights (full detail in `CHANGELOG.md`):

- ✓ **Web-verified corrections** — NSW POEO penalties updated to the 2024
  Stronger Regulation and Penalties Act; NSW WHS Regulation 2025 commencement
  corrected to 22 August 2025; NSW workers-compensation 21-day liability
  timeframe re-anchored to s 274 WIM Act 1998; lead 30 µg/dL relabelled as the
  medical removal level; Commonwealth insurance ban corrected to ss 272A–272B
  (WHS Amendment Act 2023); whistleblower criminal fine quanta completed;
  Tasmania *Safer Workplaces Act 2024*; *DPP v LH Holding* court corrected
- ✓ **Consistency** — the TRIFR/recordable set and the psychosocial hazard list
  reconciled to a single source of truth across all files; hierarchy of controls
  aligned to WHS Reg 36 grouping; risk-matrix legends defined
- ✓ **Efficiency** — `SKILL.md` slimmed ~20% (≈1,800 tokens saved on every load):
  trigger-first description, jurisdiction section converted to a non-citable
  index, domain sections collapsed to pointers, reference catalogue compressed
- ✓ **CI validation** — `scripts/validate.py` now gates packaging: frontmatter,
  reference + section-link resolution, regression guards, and AU-English checks

### Recently added (v1.4.0 — June 2026)

v1.4.0 was a correction and currency release rather than a content
expansion. Highlights (full detail in `CHANGELOG.md`):

- ✓ **Correction round** — ~125 audit findings fixed across the corpus:
  statutory citation tables, the industrial manslaughter table, penalty
  quanta, case-study corrections (including the Whakaari appeal outcome),
  and the high-risk work licensing tables
- ✓ **Currency to mid-2026** — NSW WHS Regulation 2025 and the standalone
  SafeWork NSW regulator; NSW workers compensation psychological injury
  reforms (2025–26); WA Workers Compensation and Injury Management Act
  2023; Victorian psychological health regulations; EPBC reform Acts
  2025; the WES → WEL transition (1 December 2026); NZ HSWA Amendment
  Bill
- ✓ **New content** — road transport / HVNL Chain of Responsibility
  (`references/sector-regimes.md` §14); regulator-compelled evidence
  (ss 155 / 171 / 172); enforceable undertakings and limitation periods;
  ISO 45003, psychosocial risk controls, and governance / assurance
  sections (`references/frameworks.md` §14–§15); SIF/pSIF analytics; WHS
  monetary penalty insurance bans (s 272A); Fair Work Act Part 3-5A
  sexual harassment chain; regulator notification phone script
  (`references/output-templates.md` §23); fictional worked company
  example (Meridian Facilities Group); `EVALS.md` regression evaluation
  prompts; CI packaging workflow (`.github/workflows/package.yml`);
  SKILL.md frontmatter version field

Earlier rounds (v1.1.0–v1.3.0, May 2026 — EHS, compensation/RTW, sectors,
case studies, strategy, specialist topics, D&I, procurement,
whistleblower, templates) are recorded in `CHANGELOG.md`.

---

## Attribution & acknowledgements

This skill draws on the published work of many safety scientists, including:

- **James Reason** (Swiss Cheese, Just Culture, GEMS)
- **Sidney Dekker** (New View, Just Culture, Drift)
- **Erik Hollnagel** (Safety I/II, FRAM, ETTO, Resilience Engineering)
- **Todd Conklin** (Human and Organisational Performance)
- **Amy Edmondson** (Psychological Safety)
- **David Provan** (safety professional role research, safety clutter, Forge
  Works Blueprint, Safety of Work podcast)
- **Jens Rasmussen** (Skills-Rules-Knowledge, Drift, AcciMap)
- **Andrew Hopkins** (Failure to Learn, Disastrous Decisions, Lessons from
  Esso/Texas City)
- **Karl Weick** with Kathleen Sutcliffe (High Reliability Organisations,
  Sensemaking)
- **Ron Westrum** (organisational culture typology — pathological /
  bureaucratic / generative — the foundation later extended by Hudson's
  maturity ladder)

Australian and New Zealand regulatory content draws on Safe Work Australia
publications, state and territory regulator guidance, and WorkSafe NZ
materials, all of which are public-domain or publicly accessible. Specific
citations appear inline where used.

The skill structure was authored by Neet (Avneet Singh), a Zero Harm
performance and programs manager working in the Australian integrated
facilities-services sector, with iterative development on Claude.

The worked example in `company.md` describes **Meridian Facilities Group**, a
fictional Australian integrated facilities-services organisation, and shows
how a large multi-business-unit organisation configures its WHS context. The
example is entirely fictional — it does not reproduce, and does not resemble,
any real organisation's documents. Replace it with your own organisation's
content before relying on the skill operationally.

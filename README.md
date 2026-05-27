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
- [Quick start: install in Claude](#quick-start-install-in-claude)
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

## Quick start: install in Claude

The skill installs as a single `.skill` file that you upload to Claude.

**Step 1 — Download the skill file**
On this repository's GitHub page, navigate to the **Releases** section (right
sidebar) and download the latest `whs-professional.skill` file. If there is no
Release yet, download the repository as a ZIP using the green "Code" button →
"Download ZIP", then extract it; you can package the skill yourself (see
[Packaging](#packaging-the-skill-yourself) below).

**Step 2 — Open Claude settings**
1. Go to <https://claude.ai>
2. Sign in (Claude Pro or Team account required for skills)
3. Click your profile → **Settings**
4. Find the **Skills** or **Capabilities** section

**Step 3 — Upload the skill**
1. Click **Add skill** or **Upload skill**
2. Select the `whs-professional.skill` file you downloaded
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

## Quick start: adapt to your organisation

The skill works out of the box for generic AU/NZ WHS tasks. To make it
**anchor to your organisation's specific configuration** — your risk matrix,
severity classifications, document codes, incident management system, named
programs, governance cadence — you populate `references/company.md`.

The file ships with a worked example (Downer SICS — left in for reference) and
a template structure above it.

**Two ways to do this:**

**Option A — Use Claude to fill it in (recommended)**

Once the skill is installed, paste the following prompt into Claude:

> "I want to adapt the WHS Professional skill for my organisation. Walk me
> through the `company.md` template one section at a time. For each section,
> ask me the questions you need to populate it, then show me the filled-in
> content for that section. Start with Section 1 (Organisation Identity)."

Claude will then ask you focused questions and produce the filled content
section by section. When you're done, copy the result into a new `company.md`
file (overwriting the Downer example) and re-package the skill (see
[Packaging](#packaging-the-skill-yourself)).

**Option B — Edit `company.md` directly**

1. Open `whs-professional/references/company.md`
2. Read the "Template" section at the top (sections 1–10)
3. Replace the "Active Reference: Downer SICS" section with your organisation's
   equivalent content
4. Save
5. Re-package the skill (see [Packaging](#packaging-the-skill-yourself))

See `ADAPTING.md` for a detailed walkthrough including the questions to answer
for each section and where to find the information inside your organisation.

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
- "WHS Management Plan structure for a construction project at the $4M
  threshold. Include PC duties, HRCW management, SWMS workflow, induction."
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
└── references/
    ├── company.md                 # ★ Your organisation's context (edit this)
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
    ├── output-templates.md        # Safety alert, toolbox talk, advisory note,
    │                              #   investigation report templates
    ├── analytics.md               # KPIs, dashboards, Power BI patterns, board
    │                              #   intelligence pack structure
    ├── programs.md                # Program design, gamification, facilitator
    │                              #   frameworks, sustained campaign architecture
    └── glossary.md                # WHS acronyms and terminology

README.md                          # This file
ADAPTING.md                        # Detailed walkthrough for adapting company.md
DISCLAIMER.md                      # Legal disclaimer (no legal advice etc.)
CONTRIBUTING.md                    # How to contribute
LICENSE                            # Licence terms
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

A `.skill` file is a ZIP archive of the skill folder with a specific name.

**Using a graphical file manager (no command line):**
1. In a file explorer, navigate into the repository
2. Right-click the `whs-professional` folder
3. Compress / Zip / "Send to → Compressed folder"
4. Rename the resulting `.zip` to `whs-professional.skill`

**Using the command line:**
```bash
cd path/to/repo
zip -r whs-professional.skill whs-professional
```

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

- **First aid in the workplace** — coverage of model Code of Practice, first
  aider ratios, kit content, training requirements
- **Lone working / remote work** — risk assessment frameworks, communication
  protocols, monitoring approaches
- **Working from home / hybrid arrangements** — emerging area; PCBU duties
  for the home workplace, psychosocial dimension
- **Emergency preparedness & evacuation** — fire, evacuation, business
  continuity intersection with WHS
- **Mandatory WHS training requirements** by jurisdiction (manual handling,
  HSR training, supervisor competency, etc.)
- **Sector-specific regimes** — mining (Resources Safety NSW/QLD; Mine Safety
  and Inspection Acts), maritime, aviation, rail (separate from WHS Act);
  healthcare biosafety (PC2/PC3, infection control); defence-specific
- **Volunteer & unpaid worker coverage** — scope under WHS Act
- **Behavioural-based safety programs** — design principles, critiques,
  evidence base for and against
- **Maturity assessment frameworks** — Hudson cultural ladder, DuPont Bradley
  curve, IOGP standard
- **Case study library** — Longford, Texas City, Deepwater Horizon, Pike River,
  Dreamworld for illustrative use in board papers and training
- **WHS in M&A / due diligence** — assessing WHS exposure during acquisition
- **International framework references** — ILO conventions, OSHA (US), HSE
  (UK) for global comparability

### Recently added (May 2026 update)
The following topics were previously listed as gaps and have been added to the
skill:

- ✓ Environmental / EHS chapter (`references/environment.md`)
- ✓ Workers compensation and RTW across AU + NZ (`references/compensation-rtw.md`)
- ✓ Workplace inspections, audits, and permit-to-work (`references/inspections-audits-permits.md`)
- ✓ NZ as a first-class jurisdiction (expanded in `references/legislation.md` §3)
- ✓ Operational officer due diligence toolkit (`references/legislation.md` §6)
- ✓ Hazard-specific operational frameworks for height, electrical/LOTO,
  confined space, mobile plant, hazardous chemicals, noise, vibration, plant
  safety, manual tasks, and fatigue (`references/hazards.md` §9–§18)
- ✓ Worked examples folder (`examples/`)

---

## Attribution & acknowledgements

This skill draws on the published work of many safety scientists, including:

- **James Reason** (Swiss Cheese, Just Culture, GEMS)
- **Sidney Dekker** (New View, Just Culture, Drift)
- **Erik Hollnagel** (Safety I/II, FRAM, ETTO, Resilience Engineering)
- **Todd Conklin** (Human and Organisational Performance)
- **Amy Edmondson** (Psychological Safety)
- **David Provan** (Safety Differently, Forge Works Blueprint, Safety of Work
  podcast)
- **Jens Rasmussen** (Skills-Rules-Knowledge, Drift, AcciMap)
- **Andrew Hopkins** (Failure to Learn, Disastrous Decisions, Lessons from
  Esso/Texas City)
- **Karl Weick** with Kathleen Sutcliffe (High Reliability Organisations,
  Sensemaking)

Australian and New Zealand regulatory content draws on Safe Work Australia
publications, state and territory regulator guidance, and WorkSafe NZ
materials, all of which are public-domain or publicly accessible. Specific
citations appear inline where used.

The skill structure was authored by Neet (Avneet Singh), Zero Harm
Performance & Programs Manager at Downer Social Infrastructure & Citizen
Services, with iterative development on Claude.

The included Downer SICS worked example in `company.md` is provided as a
reference for how a large multi-business-unit Australian organisation
configures its WHS context. It is presented here for educational purposes
only and does not represent the current state of any Downer document; replace
it with your own organisation's content before relying on it operationally.

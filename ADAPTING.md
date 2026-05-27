# Adapting the Skill for Your Organisation

This guide walks through populating `references/company.md` with your
organisation's WHS context. The file is the single point where the skill plugs
into your specific configuration — risk matrix, severity classifications,
document codes, incident management system, named programs, governance cadence.

You have three paths depending on how comfortable you are with editing files:

- **Path A — Let Claude do it**: paste prompts into Claude (with the skill
  installed) and answer questions; copy the result into `company.md`
- **Path B — Edit manually**: open `company.md`, read the Template section,
  rewrite the Active Reference section with your content
- **Path C — Workshop with your team**: print the questions in this guide,
  run a 90-minute working session, then populate `company.md` from the output

All three produce the same result. Path A is fastest; Path C produces the
strongest organisational buy-in.

---

## What the skill expects to know about your organisation

The skill anchors outputs to ten dimensions. For each dimension below, the
guide gives:
- **What it captures** — plain-language description
- **Questions you need to answer** — populate these and the section writes
  itself
- **Where to find the answer** in your organisation
- **An AI prompt** — paste into Claude with the skill installed to accelerate

---

## Section 1 — Organisation Identity

**What it captures**: who you are. Legal entity, division/BU structure,
industries, jurisdictions, workforce size.

**Questions**:
1. Legal entity name and any trading names
2. Division or business unit name (if you operate within a larger group)
3. Industry sectors you operate in
4. AU states/territories where you operate; NZ; any other jurisdictions
5. Approximate workforce size (direct employees + contractor workforce)
6. Primary lines of business / contract types

**Where to find it**: organisational chart, annual report, intranet "about
us" page, contract register.

**AI prompt**:
> "Help me fill in Section 1 of the company.md template for the WHS
> Professional skill. Ask me one question at a time, then draft the section
> text in the format the template expects."

---

## Section 2 — WHS Management System

**What it captures**: your overall WHS system identity. Brand name, ISO
status, document numbering convention.

**Questions**:
1. What is your WHS management system called internally? (e.g. "Zero Harm",
   "Safety First", "Beyond Zero", no brand)
2. Is your system ISO 45001 certified, aligned but not certified, in progress,
   or not pursuing?
3. What is your document numbering convention? Most organisations use a
   prefix + functional code + type code + number pattern (e.g. "DG-ZH-PR006" =
   Group, Zero Harm, Procedure 006). Some use simpler numbering.
4. What are the type codes for: Standard, Procedure, Work Instruction,
   Template, Form, Guideline?

**Where to find it**: management system manual, document control register,
intranet document repository, internal audit reports.

**AI prompt**:
> "Help me document my organisation's WHS management system identity for
> company.md. I'll tell you what we call it, our ISO 45001 status, and our
> document numbering convention; you draft the Section 2 content."

---

## Section 3 — Risk Framework

**What it captures**: your risk matrix, likelihood and consequence ratings,
risk level response requirements, control effectiveness rating. This is the
most operationally important section — it gets used in every risk
assessment, board paper, and incident report.

**Questions**:
1. What is your risk matrix? (typically 5×5 or 6×5; A/B/C/D or H/M/L output)
2. What are your likelihood bands? (typically Rare → Almost Certain, with
   either probability ranges or qualitative descriptors)
3. What are your consequence categories? (typically H&S, Environment,
   Legal/Compliance, Cost, Reputation, sometimes Community)
4. What are your consequence rating descriptors at each level (1–5 or 1–6)?
5. What are your risk response requirements? (typically: A risks need
   immediate action and senior leader acceptance; D risks managed routinely)
6. What is your control effectiveness rating? (typically: Effective /
   Generally Sound / Improvement Required, or similar)

**Where to find it**: enterprise risk management standard, WHS risk
management procedure, project risk register template, integrated management
system manual.

**AI prompt**:
> "Help me document my organisation's risk framework in company.md. I'll
> paste the risk matrix from our standard, plus the likelihood and consequence
> rating tables; you format them into Section 3 of the template."

---

## Section 4 — Hierarchy of Controls — Local Framing

**What it captures**: any organisation-specific layering on top of the
standard Eliminate → Substitute → Isolate → Engineering → Administrative →
PPE hierarchy. Some organisations use "above the line / below the line"
framing; others have specific rules about when soft controls cannot stand
alone.

**Questions**:
1. Does your organisation use any specific shorthand for hard vs soft
   controls? (e.g. above/below the line)
2. Do you have a critical rule about when administrative or PPE controls
   cannot be the sole risk treatment?
3. Any specific guidance on when "grossly disproportionate cost" justifies
   not implementing a higher-order control?

**Where to find it**: WHS risk management standard, SFAIRP guidance
document.

**AI prompt**:
> "My organisation describes hard controls as [your terminology] and soft
> controls as [your terminology]. We have a rule that [your rule]. Format
> Section 4 of company.md to reflect this."

---

## Section 5 — Incident Classification & Management

**What it captures**: how you classify incidents, what triggers notification
to whom, what triggers investigation by what methodology. This section drives
the entire post-incident workflow.

**Questions**:
1. What severity rating scale do you use? (typically 1–5 or 1–6)
2. What are the H&S, Environment, Plant & Property, Legal, and Management
   Impact descriptors at each level?
3. What is your HiPo definition? (typically: potential severity ≥ a specified
   threshold, regardless of actual outcome)
4. What is your internal notification chain by severity? (who is notified,
   by when, via what method)
5. What investigation methodology applies at each severity? (typically: a
   simplified form for low severity; ICAM for HiPo and high severity)
6. What is your incident management system? (e.g. INX, Cintellate, Donesafe,
   Mango, in-house tool)
7. Do you have a "Direct Control vs Influence" distinction for what's
   included in performance statistics?

**Where to find it**: incident management procedure, incident reporting
form, incident investigation procedure.

**AI prompt**:
> "Help me document my organisation's incident classification and management
> approach for company.md. I'll share our severity rating scale, HiPo
> definition, notification chain, and investigation requirements; you format
> them into Section 5."

---

## Section 6 — Document Templates & Forms

**What it captures**: the document references for your standard WHS
templates. The skill uses these to write outputs that look like they came
from inside your organisation rather than generic.

**Questions**: for each of the following, what is your organisation's
document reference (number and title)?
- Safety alert (portrait and landscape variants if both exist)
- Bulletin
- Preliminary internal incident notification (PIIN)
- Standard incident investigation form
- ICAM investigation report
- ICAM interview record
- 5-Why analysis
- Lessons Learnt template / register
- Risk and opportunity register
- Zero Harm (or equivalent) risk register
- Plant risk assessment
- Hazardous chemicals risk assessment
- Manual handling assessment
- SWMS template
- Traffic management plans
- STAR (Stop Think Act Review) or equivalent point-of-work assessment

**Where to find it**: document control register, intranet template library.

**AI prompt**:
> "I'll paste a list of my organisation's WHS document references. Format
> them into the Section 6 table in company.md."

---

## Section 7 — Systems & Tools

**What it captures**: the platforms you use day-to-day for WHS work.

**Questions**:
1. Incident management system (e.g. INX, Cintellate, Donesafe, Mango)
2. WHS management system platform (e.g. Lucidity, Ideagen, Mango, SharePoint)
3. Analytics / dashboarding platform (e.g. Power BI, Tableau, Domo)
4. Project / task management (e.g. Asana, Monday, Smartsheet, Jira)
5. Contractor management / prequalification (e.g. Rapid Global, Cm3, Avetta,
   ISNetworld)
6. Audit & inspection platform (e.g. iAuditor, MyOSH, ProcessMAP)
7. Permit-to-work system (if applicable)
8. Document storage (e.g. SharePoint, Google Drive, Dropbox)

**Where to find it**: IT services catalogue, intranet system index, WHS team
desktop.

---

## Section 8 — Critical Risk Taxonomy

**What it captures**: your organisation's named critical risks and the
governance around them.

**Questions**:
1. What are your organisation's critical risk categories? (typically 10–20
   topics, e.g. Working at Height, Electrical Safety, Confined Spaces)
2. Do you have a Critical Risk Owner (CRO) structure or equivalent? Named
   ownership per risk?
3. What is your Critical Control Verification (CCV) approach? Cadence?
   Reporting?

**Where to find it**: critical risk register, critical control verification
schedule, ELT risk dashboard.

---

## Section 9 — Engagement Programs & Campaigns

**What it captures**: named recurring safety engagement programs your
organisation runs.

**Questions**:
1. What are your named programs/campaigns? (e.g. "Safe Over Summer", "Stop
   Work for Safety Day", "Lifesavers Week")
2. What is the cadence? (annual, quarterly, ongoing)
3. What is the reach? (workforce coverage, contractor coverage)
4. Are there theme architectures, gamification mechanics, or recognition
   programs attached?

**Where to find it**: WHS team annual plan, internal communications
calendar, intranet campaign pages.

---

## Section 10 — Governance & Reporting Cadence

**What it captures**: how WHS is governed at the top of the organisation
and how often safety reports flow upward.

**Questions**:
1. What is the board safety reporting cycle? (monthly, quarterly,
   semi-annual, annual)
2. What is the ELT safety reporting cycle?
3. Is there a defined officer due diligence framework? Who supports officers
   in discharging their duty?
4. What are the key WHS leadership roles in your organisation?
   (EGM/GM Zero Harm; BU heads of safety; CRO; HSBP)
5. Is there a peer review or assurance process across business units
   or contracts?

**Where to find it**: safety governance charter, board terms of reference,
WHS team organisation chart.

---

## After you've populated company.md

**Validate** by asking Claude (with the updated skill installed):

> "Summarise the WHS context for my organisation from `company.md`. I want
> to make sure it's accurate before I rely on it."

The summary should match your understanding. If it doesn't, adjust the file.

**Test it on a realistic prompt**:

> "Draft an executive summary for an ICAM report on a near-miss electrical
> incident. Use my organisation's severity classification, ICAM template
> reference, and notification chain."

The response should reference your specific severity scale, your template
codes, and your notification chain — not generic ones.

---

## Updating the skill as your organisation changes

WHS context drifts. New templates, system migrations (e.g. INX → another
platform), revised risk matrices, new critical risks, leadership changes.

Set a calendar reminder to review `company.md` every six months. The skill
will continue to produce outputs anchored to whatever is in the file, so
out-of-date content will create silently wrong outputs.

Each update follows the same flow:
1. Edit the relevant section in `company.md`
2. Re-package the skill (`zip -r whs-professional.skill whs-professional`)
3. Re-upload to claude.ai (the new version overwrites the old)

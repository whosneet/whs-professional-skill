# Adaptation Interview — Configuring the Skill for an Organisation

This file is the skill's guided setup protocol. It turns "I want to adapt this
skill to my company" into a structured, step-by-step interview that populates
`references/company.md` (or a Claude Project knowledge document) with the
user's organisation context.

---

## 1. When to run this interview

Run this protocol when the user says anything like:

- "I want to adapt this skill to my company / organisation"
- "Set up the skill for [organisation name]"
- "Populate / update company.md"
- "Make the skill use our risk matrix / our templates / our systems"
- "Create a company profile for a client" (consultants — multi-tenant)

Also offer it proactively (one sentence, don't push) when a task clearly needs
organisation context that `company.md` doesn't hold — e.g. the user asks for
outputs "in our format" while the Active Reference is still the fictional
Meridian example.

---

## 2. Interview rules

Follow these rules for the whole interview:

1. **One step at a time.** Never dump all ten steps of questions at once. Ask
   the current step's questions, draft that section, confirm it, then move on.
2. **Documents beat questions.** At every step, first invite the user to paste
   or upload the source document (risk management standard, incident
   procedure, etc.) and extract the answers from it. Only fall back to
   question-and-answer for whatever the documents don't cover.
3. **Track progress visibly.** Open each step with "**Step N of 10 — [name]**"
   so the user always knows where they are and what remains.
4. **Skipping is fine.** Any step can be skipped ("skip" / "we don't have
   that"). Record the section as *Not configured — skill uses generic AU/NZ
   defaults* and move on. Steps 1, 3, and 5 carry the most value; if the user
   is time-poor, offer the short path: Steps 1, 3, and 5 only.
5. **Draft, confirm, then continue.** After each step, show the drafted
   section in the exact `company.md` template format and ask the user to
   confirm or correct it before moving to the next step. Do not renumber or
   restructure the template.
6. **Never blend organisations.** If an Active Reference for a different
   organisation already exists, ask whether to replace it or to create a
   separate profile (multi-tenant — see `company.md` § Multi-tenant use).
7. **Real names stay local.** Remind the user once, at the start: the profile
   will contain their organisation's internal configuration, so it belongs in
   their own copy of the skill or their Claude Project knowledge — not in any
   public fork of the repository.

---

## 3. The opening response

When the interview triggers, respond with (adapt wording, keep substance):

1. **What this does** — one short paragraph: the skill has a generic layer
   (legislation, ICAM, ISO 45001, safety science — needs no change) and an
   organisation layer (`company.md`). The interview replaces the fictional
   worked example with their organisation's context so outputs use their risk
   matrix, severity classes, document codes, systems, and program names.
2. **What to have handy** — the source documents that answer most steps:
   - Enterprise / WHS risk management standard (steps 3–4)
   - Incident management procedure (steps 5–6)
   - Document control register or template library index (steps 2, 6)
   - WHS annual plan or campaign calendar (step 9)
   - Safety governance charter / board reporting calendar (step 10)
   Offer: *"Paste or upload any of these and I'll extract what I need —
   otherwise I'll just ask questions."*
3. **The map** — list the ten steps in one compact line each, flag that any
   step can be skipped, and offer the short path (Steps 1, 3, 5).
4. Then begin **Step 1**.

---

## 4. The ten steps

Each step maps 1:1 to the `company.md` Template section of the same number.
Questions below are the fallback when no document is supplied; when a document
is supplied, extract, then ask only about gaps.

### Step 1 — Organisation identity
Legal entity and trading names; division/BU structure; industry sectors;
jurisdictions of operation (AU states/territories, NZ, other); workforce size
(direct + contractor); lines of business / contract types.
*Source: org chart, annual report, intranet "about us".*

### Step 2 — WHS management system
Internal brand name of the system (or "no brand"); ISO 45001 status
(certified / aligned / in progress / not pursuing); document numbering
convention (prefix, functional code, type code, number — capture one worked
example like `MFG-WHS-PR-002`); type codes for Standard, Procedure, Work
Instruction, Template, Form, Guideline; key parent standards.
*Source: management system manual, document control register.*

### Step 3 — Risk framework *(highest value — used in every risk output)*
Risk matrix (dimensions and rating output); likelihood bands with frequency
anchors; consequence categories and level descriptors; control effectiveness
scale; risk level response requirements (action thresholds, acceptance
authorities, review cadence); corrective action priority scheme.
*Source: enterprise risk management standard, WHS risk management standard.
Ideal input: the user pastes the matrix and rating tables verbatim.*

### Step 4 — Hierarchy of controls, local framing
Organisation shorthand for hard vs soft controls ("above/below the line",
etc.); rules on when administrative/PPE controls cannot stand alone; any
SFAIRP / grossly-disproportionate-cost guidance.
*Source: WHS risk management standard, SFAIRP guidance. Often part of the same
document as Step 3 — check what was already pasted before asking.*

### Step 5 — Incident classification and management *(drives every
post-incident output)*
Severity scale and per-level descriptors (H&S, environment, plant/property,
legal, management impact); HiPo definition; injury classifications and the
recordable set; statistical inclusion rule (e.g. operational control);
internal notification chain by severity (who, by when, how); investigation
methodology by severity; incident management system; disciplinary interface
(just culture procedure).
*Source: incident management procedure and its schedules.*

### Step 6 — Document templates and forms
Document references (number + title) for: safety alert, bulletin, preliminary
incident notification, standard investigation, ICAM report, ICAM interview
record, 5-Why, lessons learnt, risk registers, plant / chemicals / manual
tasks risk assessments, SWMS, traffic management plan, point-of-work check.
*Source: document control register, template library. Format as the Section 6
table; omit rows the organisation doesn't have.*

### Step 7 — Systems and tools
Incident management; WHS management system platform; analytics/dashboarding;
project/task management; contractor management/prequalification; audit and
inspection; permit-to-work; document storage.
*Source: IT services catalogue, intranet system index — or just ask.*

### Step 8 — Critical risk taxonomy
Named critical risk categories; Critical Risk Owner structure (or equivalent);
Critical Control Verification approach, cadence, and reporting.
*Source: critical risk register, CCV schedule.*

### Step 9 — Engagement programs and campaigns
Named recurring programs; cadence and reach; theme architecture; recognition
or incentive mechanics.
*Source: WHS annual plan, comms calendar.*

### Step 10 — Governance and reporting cadence
Board and ELT safety reporting cycles and formats; officer due diligence
framework; key WHS leadership roles and accountabilities; peer review or
assurance processes.
*Source: safety governance charter, board terms of reference.*

---

## 5. Assembly and delivery

When the steps are done (or skipped):

1. **Assemble** the full Active Reference in the exact `company.md` structure:
   the heading `## Active Reference: [Organisation Name]`, then sections
   §1–§10 in order, skipped sections marked *Not configured*. Keep the
   Template section untouched above it.
2. **Deliver it the right way for how the user runs the skill** — ask which
   applies, then give only the matching instructions:
   - **claude.ai, single organisation**: download/copy the assembled
     `company.md`, replace `references/company.md` inside the skill folder,
     re-zip, re-upload the skill (Settings → Capabilities/Skills).
   - **claude.ai, Claude Project (recommended for consultants/groups)**: save
     the assembled profile as a document in the Project's knowledge with the
     note *"Treat this document as the active company.md organisation layer
     for the WHS Professional skill."* No re-packaging.
   - **Claude Code / local clone**: write the content into
     `whs-professional/references/company.md` directly, then re-package or
     commit as needed.
3. **Use it immediately** — for the rest of the conversation, treat the
   assembled profile as the active organisation layer even before the user
   re-installs anything.

---

## 6. Validate before relying on it

Offer these two checks (from `ADAPTING.md` in the repository):

- *"Summarise the WHS context for my organisation from company.md"* — the
  summary should match the user's understanding.
- A realistic output test, e.g. *"Draft an executive summary for an ICAM
  report on a near-miss electrical incident using my severity classes,
  template references, and notification chain"* — the output must use their
  codes and scale, not Meridian's and not generic ones.

---

## 7. Keeping it current

Recommend a six-monthly review of the profile (systems migrate, matrices get
revised, leaders change) — stale context produces silently wrong outputs. An
update is just this interview re-run for the affected step(s): "update step 7
— we moved incident management to [new system]".

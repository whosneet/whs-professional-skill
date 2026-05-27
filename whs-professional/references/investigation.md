# Investigation Reference — ICAM, 5-Why, Bowtie, Investigation Bias

---

## Table of Contents
1. [ICAM Methodology](#1-icam-methodology)
2. [5-Why Analysis](#2-5-why-analysis)
3. [Contributing Factors Taxonomy](#3-contributing-factors-taxonomy)
4. [Bowtie Analysis](#4-bowtie-analysis)
5. [ICAM Report Template](#5-icam-report-template)
6. [Common Investigation Pitfalls & Cognitive Biases](#6-common-pitfalls)
7. [Corrective Action Framework](#7-corrective-action-framework)
8. [PEEPO Question Bank](#8-peepo-question-bank)
9. [Witness Interview Technique](#9-witness-interview-technique)
10. [Witness Statement Format and Admissibility](#10-witness-statement-format-and-admissibility)
11. [ICAM Variants — BHP, IOGP, Safety Wise](#11-icam-variants--bhp-iogp-safety-wise)
12. [AcciMap Methodology](#12-accimap-methodology)
13. [Bowtie Worked Example](#13-bowtie-worked-example)
14. [Legal Privilege Management During Investigation](#14-legal-privilege-management-during-investigation)

> For organisation-specific incident classification thresholds, notification
> chains, investigation requirements by severity, and incident management
> system references, load `references/company.md`.

---

## 1. ICAM Methodology

**Incident Cause Analysis Method (ICAM)** — the gold standard for serious incident
investigation in AU/NZ WHS. Developed from James Reason's systems model of accident
causation. Systemic, not blame-based.

### The Four ICAM Levels (bottom-up analysis)

```
[ABSENT / FAILED DEFENCES]
        ↑
[INDIVIDUAL / TEAM ACTIONS]
        ↑
[TASK / ENVIRONMENTAL CONDITIONS]
        ↑
[ORGANISATIONAL FACTORS]
```

Work upward from the incident event to root causes in organisational systems.

### Step-by-Step ICAM Process

**Step 1 — Preserve and Secure the Scene**
- Notify regulator if notifiable (see legislation.md s 35)
- Preserve scene before disturbance
- Photograph, video, diagram the scene
- Identify and secure physical evidence (plant, equipment, substances)
- Record environmental conditions (weather, lighting, noise, time of day)

**Step 2 — Information Gathering (PEEPO)**
Gather information across the PEEPO domains:
- *People*: Who did what, when, where, how and why? Interview all witnesses and involved
  persons separately. Use open-ended questions. Document each interview on your
  organisation's interview record (see `company.md`).
- *Environment*: Physical conditions — weather, noise, work surface, lighting, air quality
- *Equipment*: Design, maintenance records, fit for purpose, inspection history
- *Procedures*: Compare what was required vs what occurred. Were procedures accessible
  and understood? Does training support correct application? Consider risk drift.
- *Organisation*: Management commitment, people management processes, tools and equipment
  quality, commercial/operational pressures, planning, communication, maintenance

**Step 3 — Construct the Timeline**
- Build a chronological timeline of events leading to the incident
- Include what happened, who was involved, and what decisions were made
- Note decision points — moments where an alternative action could have changed the outcome

**Step 4 — Identify Absent or Failed Defences**
Defences are the barriers or controls that should have prevented the incident or limited harm:
- Physical barriers (guards, gates, PPE)
- Procedural barriers (permits, SWMS, checklists)
- Human barriers (supervision, second-person checks)
- Administrative barriers (training, competency assessment)

For each failed/absent defence, ask: Why was it not in place? Why did it fail?

**Step 5 — Identify Individual / Team Actions**
What did individuals do or not do that directly led to the incident?
These are proximate causes — important to document but NOT the focus of corrective action.
Avoid language that implies blame at this stage.

**Step 6 — Identify Task / Environmental Conditions**
What conditions made it difficult for the individual/team to act safely?
- Poor procedure design
- Inadequate tools / equipment
- Time pressure / workload
- Distraction / fatigue
- Environmental conditions (heat, noise, poor lighting)
- Unclear or conflicting priorities

**Step 7 — Identify Organisational Factors**
The systemic root causes — where management decisions, resource allocation, or
organisational culture created the conditions for the incident:
- Management of change
- Communication systems
- Fatigue / fitness for work management
- Competency and training systems
- Supervision arrangements
- Contractor management
- Risk management processes
- Organisational learning (prior incidents not acted on)
- Culture (production pressure over safety, fear of reporting)

**Step 8 — Develop Corrective Actions**
Map corrective actions to EACH contributing factor, not just the proximate cause.
Apply hierarchy of controls. Assign owner, due date, and verification method.

---

## 2. 5-Why Analysis

5-Why is commonly applied as a supporting technique to identify root causes
within lower-severity incident investigations (typically actual severity 1–3).
It is faster than ICAM but less rigorous for complex or systemic failures.
Output usually feeds the Root Cause field of the organisation's standard
investigation form.

### Method
1. State the problem clearly and specifically
2. Ask "Why did this happen?" — record the answer
3. Ask "Why?" to that answer — repeat until you reach a root cause (usually 3–7 iterations)
4. When the answer is an organisational system or policy, you've typically reached the root

### 5-Why Example
**Problem**: Worker's hand lacerated by unguarded blade on conveyor.

1. Why? — Guard was not in place
2. Why? — Guard had been removed for cleaning and not replaced
3. Why? — No isolation / LOTO procedure was followed for the cleaning task
4. Why? — LOTO procedure did not cover the conveyor during routine cleaning
5. Why? — Cleaning tasks were not included in the hazard identification when procedures
   were written

**Root cause**: Inadequate hazard identification scope in procedure development.

### 5-Why Pitfalls
- Stopping at individual behaviour (e.g., "worker didn't follow procedure") without
  asking why following the procedure was difficult or unclear
- Following only one causal chain — incidents typically have multiple contributing paths
- Not verifying that fixing the root cause would have prevented the incident

---

## 3. Contributing Factors Taxonomy

Use this taxonomy when documenting ICAM findings. Map each contributing factor to
its category and sub-category.

### Task / Environmental Conditions
| Sub-category | Examples |
|---|---|
| Physical environment | Lighting, temperature, noise, housekeeping, space constraints |
| Equipment/plant condition | Maintenance state, design adequacy, fit for purpose |
| Tools and materials | Availability, condition, suitability |
| Workload / time pressure | Rushed work, understaffing, conflicting priorities |
| Distraction / interruption | Concurrent tasks, communication noise |
| Procedure quality | Accuracy, clarity, accessibility, relevance |
| PPE | Availability, fit, comfort, usability |

### Individual / Team Actions
| Sub-category | Examples |
|---|---|
| Knowledge deficit | Didn't know correct method |
| Skill deficit | Knew the method, lacked competency to execute |
| Rule violation | Deliberately deviated from known rule |
| Routine violation | Habitual shortcut — normalised deviation |
| Situational violation | One-off deviation due to perceived necessity |
| Communication failure | Miscommunication between workers / supervisor |
| Fatigue | Impaired alertness or decision-making |
| Complacency | Overconfidence from routine task familiarity |

### Organisational Factors
| Sub-category | Examples |
|---|---|
| Training / competency | Inadequate, not verified, not refreshed |
| Supervision | Inadequate, not provided, supervisor absent |
| Risk assessment / SWMS | Not done, not current, not followed |
| Maintenance management | Preventive maintenance inadequate, deferred |
| Management of change | Change not assessed for WHS risk |
| Contractor management | Prequalification, induction, supervision gaps |
| Communication systems | Safety information not reaching frontline |
| Organisational learning | Prior hazards / incidents not acted on |
| Resource allocation | Insufficient time, budget, staffing |
| Organisational culture | Production pressure, fear of reporting |
| Design | Plant / structure / workspace not designed safely |

---

## 4. Bowtie Analysis

Use for critical risk management and hazard barriers analysis (not standard investigations).
Appropriate for: critical risk controls verification, presenting risk to board/ELT,
analysing whether controls are degraded.

### Structure
```
[THREATS] → [PREVENTION BARRIERS] → [TOP EVENT / HAZARD] → [MITIGATION BARRIERS] → [CONSEQUENCES]
```

**Top event**: The point at which the hazard is released (e.g., "uncontrolled electrical energy")
**Threats** (left side): What could cause the top event (e.g., isolation failure, faulty equipment)
**Prevention barriers** (left side): Controls preventing top event from being realised
**Consequences** (right side): What happens if the top event occurs
**Mitigation barriers** (right side): Controls that reduce severity of consequences

**Degradation controls**: Factors that can degrade barriers, and controls on those degradation factors.

---

## 5. ICAM Report Template

**Triggers**: Actual severity rating 4, 5, or 6, or all HiPo incidents (commonly).
Some organisations require ICAM for level-3 incidents at the discretion of business
or Zero Harm leadership. Where ICAM is conducted, a separate standard investigation
form is generally not required.

> Reference your organisation's incident management procedure for trigger thresholds
> and approval chains (`references/company.md`).

All corrective actions should be recorded in the organisation's incident management
system and monitored through close-out.

---

### EXECUTIVE SUMMARY (Cover Page)

| Field | |
|---|---|
| Incident System Reference | Incident Severity Rating |
| Business Group | Business Unit |
| Name and Location of Operation/Project/Site | |
| Date of Incident | Date of Report |
| Brief Description of Incident | |
| Key Findings and Actions | |
| Will a Lesson Learnt be developed? | ☐ Yes ☐ No |
| Report Prepared By | |

**Review/Approval** *(modify to match your organisation's approval chain)*
| Role | Name | Signature | Date |
| Lead Investigator | | | |
| Responsible Manager | | | |
| Business Unit GM | | | |
| Business Unit EGM | | | |

---

### 1. Scope of Investigation
Clarify the boundaries — which sites, functions, or people are included.
The scope includes analysis of contributory factors. Other relevant findings not
directly contributing to the incident should also be noted.

### 2. Investigation Team Members
| Name | Position |

### 3. Incident Overview
Summary of the incident with pictures where available. Key details: date, specific
locations, what occurred, outcome.

### 4. Sequence of Events
The sequence of events before, during, and following the incident.
Note gaps in the timeline — highlight areas requiring further investigation.

| Event Sequence | Date | Approx. Time | Event Description |

### 5. Data Collection

#### 5.1 Organisational Context
Create a working group (3–6 people) to understand the organisational context and
systemic factors. Facilitator should be an unbiased third party with no direct
involvement in the incident.

Participants: people involved in the event; others who perform the same/similar role;
subject matter experts (design, procurement, supervisors).

**Context questions to work through with the group:**

| Question | Findings |
|---|---|
| How is work normally performed in this area? | |
| What factors helped the work go right (most of the time)? | |
| What were the pressures or competing priorities at the time? | |
| Were there any recent changes (people, equipment, process, environment)? | |
| Are members comfortable raising concerns or asking for clarification? | |
| What would assist successful delivery that is currently not being done? | |
| What changes could be explored to improve implementation of required controls? | |

#### 5.2 PEEPO Analysis
As an investigation team, work through each category and summarise findings.
Interviews should be documented on your organisation's interview record form.

| Type | Category | Information / Data Collected |
|---|---|---|
| **P** | **People** — Who did what, when, where, how and why? Behaviours that increased/decreased likelihood of undesired outcome. Do we have the right people, in the right role, doing the right work? Were they trained? | |
| **E** | **Environment** (Workplace, Weather) — Physical environmental factors: weather, noise, work surface, air, light | |
| **E** | **Equipment** — Design, maintenance, fit for purpose | |
| **P** | **Procedures** — Review procedure requirements vs what occurred. Are procedures accessible and well understood? Does training support correct application? Consider risk drift. | |
| **O** | **Organisation** — Evidence of management, leadership, and commitment. Documented people management processes, tools and equipment quality, commercial/operational pressures, planning, communication, maintenance. | |

#### 5.3 Photographs
| # | Photo | Description |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

### 6. Critical Risk Analysis
*(For high potential and high actual incidents)*
Refer to relevant documentation: management plan, SWMS, Risk Assessments, Bow Ties.
Identify what made controls adequate/inadequate, or why they were absent.
Actions may prompt a project document review or Group-level review via relevant Community
of Practice (CoP).

| Critical Risk | Critical Controls | Evaluate Controls | Comments |
|---|---|---|---|
| | | ☐ Adequate ☐ Inadequate ☐ Absent | |

### 7. ICAM Analysis
Review contributing factors and perform ICAM analysis to identify effective corrective
actions. The 4-column table maps the causal chain from defences through to root causes.

| Absent or Failed Defences | Individual / Team Actions | Task / Environment Conditions | Organisational Factors |
|---|---|---|---|
| | | | |

### 8. Incident Risk Assessment
*(Refer to your organisation's risk management standard and incident management procedure — see `company.md`)*

**Actual Risk Rating**
| Consequence | Likelihood | Risk Level |
| | | |
Rationale for Risk Rating:

**Potential Risk Rating**
| Consequence | Likelihood | Risk Level |
| | | |
Rationale for Risk Rating:

**Classification of Incident**
| Severity (or Potential Severity) Ranking | Severity Category Rating Level | Select/Tick |
|---|---|---|
| Extreme | 6 | ☐ |
| Very High | 5 | ☐ |
| High | 4 | ☐ |
| Medium | 3 | ☐ |
| Low | 2 | N/A |
| Very Low | 1 | N/A |

### 9. Recommended Corrective Actions
Actions to prevent occurrence of similar incidents. Where required, include amendments
to bowties, HAZOPs, CRAWS, FMEA, or SWMS. For group-wide change, engage relevant CoP.
**All agreed actions must be recorded against the incident in the organisation's incident management system and monitored accordingly.**

| Action Required | Type of Control | Responsibility | Completion Date |
|---|---|---|---|

### 10. Conclusions
In light of the investigation findings, summarise the key learnings and conclusions.

### 11. Investigation Team Sign-Off
All investigation team members to sign off.
| Name | Sign | Date |

---

## 6. Common Pitfalls

The pitfalls below are documented cognitive biases — recognising them is half
the defence. Where applicable, the underlying research is attributed; see
`frameworks.md` Section 10 for the named thinkers.

### Cognitive biases that distort investigation findings

**Hindsight bias** (Fischhoff, 1975): Knowing the outcome makes the chain of
events leading to it appear more predictable and the contributors more obvious
than they were at the time. Operators are judged on what *we now know* rather
than what they knew. Defence: continually ask "what information was available
to this person at this moment, and what was a reasonable interpretation of it?"

**Outcome bias** (Baron and Hershey, 1988): Judging the quality of a decision
by its outcome rather than by the reasoning available at the time. A good
decision can have a bad outcome and vice versa. Defence: assess the decision
process, not just the result.

**Counterfactual reasoning trap** (Dekker): "If only they had done X, this
wouldn't have happened." Counterfactuals tell us what *didn't* happen but not
*why*. They generate satisfying narratives but rarely identify systemic factors.
Defence: replace counterfactuals with diagnostic questions about why the
actual sequence made sense to the participant at the time.

**Confirmation bias**: Looking for evidence that confirms an initial hypothesis
and discounting contradictory information. The first plausible explanation
becomes the lens through which all subsequent evidence is interpreted. Defence:
write the initial hypothesis down, then deliberately seek evidence that would
disprove it.

**Attribution error** (Ross, 1977): Attributing actions to character ("he was
careless") rather than situation ("the procedure was contradictory and the
schedule was impossible"). Workers in incident reports look reckless; the
same workers in normal work look competent. Defence: assume context is the
explanation until evidence shows otherwise.

**Just-world fallacy**: Assuming bad outcomes happen to people who deserved them
(or were responsible for them). Distorts both investigation findings and
disciplinary follow-through. Defence: name the bias when you notice it in
yourself or others.

**Survivorship bias**: Studying only incidents misses the population of
successful work where the same conditions did not produce harm. The factors
that distinguish failure from success are often invisible without studying
both. Defence: complement incident review with observation of normal work
(see Safety II / Hollnagel).

**Root cause illusion**: Complex socio-technical accidents rarely have a single
root cause. The narrative satisfies but does not represent the system. Defence:
identify contributing factors plurally; expect 4–8 factors for any significant
incident; resist the impulse to converge prematurely.

**Recency bias**: Over-weighting the most recent or most vivid information
encountered. The last witness interviewed influences the conclusions more
than the first. Defence: collect all evidence before drawing conclusions;
use structured methods (ICAM, AcciMap) to weight evidence consistently.

### Process pitfalls

**Stopping at individual behaviour**: "Worker didn't follow procedure" is never
a root cause. Always ask what made following the procedure difficult, unclear,
or unlikely. This is the application of Dekker's "human error is a symptom"
principle.

**Blame and punishment focus**: ICAM is a learning tool. If the investigation
becomes a disciplinary process, witnesses stop talking and the real causes
stay hidden. Reason's Just Culture algorithm helps separate the learning question
from the accountability question — they are not the same investigation.

**Corrective actions targeting proximate causes only**: Training and supervision
are the most common corrective actions — and the least effective per the
hierarchy of controls. Push for engineering, isolation, and substitution
wherever the analysis supports it.

**Interviewer influence**: Leading questions corrupt witness accounts. Use
open-ended prompts: "Walk me through what happened from the start of your
shift." Allow silence; resist the impulse to fill gaps.

**Premature closure**: Driving the investigation to a quick conclusion to
satisfy reporting deadlines. The structured analysis sections of ICAM exist
precisely because the obvious explanation is often incomplete.

**Not closing the loop**: Completed corrective actions with no effectiveness
verification are the most common governance failure in post-incident management.
A corrective action that is implemented but doesn't work is worse than no action
at all — it generates false confidence.

---

## 7. Corrective Action Framework

All corrective actions must be:
- **Specific**: Clear description of what will change
- **Assigned**: Named owner (not a role — a person)
- **Time-bound**: Realistic due date
- **Measurable**: How will we know it worked?
- **Linked**: Mapped to the contributing factor it addresses

Apply hierarchy of controls to all corrective actions:
| Hierarchy level | Example |
|---|---|
| Eliminate | Remove the hazard entirely |
| Substitute | Replace with a less hazardous alternative |
| Isolate | Physical separation — barriers, enclosures, exclusion zones |
| Engineering | Guards, interlocks, ventilation, ergonomic redesign |
| Administrative | Procedures, training, supervision, permits, rosters |
| PPE | Last resort — gloves, helmets, respiratory protection |

Actions at the Administrative or PPE level require justification for why higher-order
controls are not practicable. This justification must be documented.

### Effectiveness Verification
After the due date, the corrective action owner and an independent WHS representative
must verify:
1. The action was implemented as intended
2. The contributing factor has been addressed
3. No new hazards were introduced by the control

---

## 8. PEEPO Question Bank

The PEEPO categories (People, Environment, Equipment, Procedures, Organisation)
provide the structure for systematic information gathering. The categories are
useful only if they generate real conversations — concrete questions below.
Adapt phrasing to the witness, but cover the substance.

### People — questions to ask the people involved

- "Walk me through what you were doing from the start of your shift."
- "Tell me what you were thinking when [the critical moment] happened."
- "How long have you been doing this task? When was the last time?"
- "What training did you receive for this task? When was the last refresher?"
- "Did you have any concerns about the task before starting? Did you raise them?"
- "Was there anyone supervising the work? What was their role?"
- "Were you working alone, or with others? How did communication work?"
- "How were you feeling that day? Sleep, health, anything that was on your mind?"
- "What does normal practice for this task look like — what would you usually do?"
- "What was different about today compared to other days you've done this work?"

### People — questions to ask witnesses (not directly involved)

- "Tell me what you saw, in your own words."
- "Where were you positioned when this happened? Could you see the work?"
- "What was the work area like — busy, quiet, normal?"
- "Did anything seem unusual before the event?"
- "Did you notice anyone behaving in a way that was concerning beforehand?"
- "Have you seen this kind of issue happen before — even if it didn't lead to harm?"

### Environment

- "What were the conditions on the day — weather, temperature, humidity?"
- "What was the lighting like at the location?"
- "Was there noise that could have affected communication or alarms?"
- "What was the state of the work surface — clean, wet, contaminated, unstable?"
- "Was the work area uncluttered, or was there housekeeping pressure?"
- "Was the work area shared with other activities — vehicles, other trades, public?"
- "Did the environment change during the work — weather turned, traffic increased?"
- "Were there any unusual smells or atmospheric conditions?"

### Equipment

- "What plant and equipment was involved in the task?"
- "When was the last inspection of the equipment? Where are those records?"
- "Was any of the equipment damaged, modified, or showing wear before the event?"
- "Did the equipment behave as expected — or was anything unusual?"
- "Was the right equipment available for the task — or were workarounds used?"
- "Were any guards, interlocks, or safety devices bypassed or out of service?"
- "Were tools in date for calibration? Were test instruments verified?"
- "Was the equipment fit for purpose in this work environment?"

### Procedures

- "What procedure, SWMS, or instruction governed this task?"
- "Was it available at the workplace? Was it accessible when you needed it?"
- "When was the procedure last reviewed? Who reviewed it?"
- "Did the procedure cover the actual task as it was performed — or were there
  steps not in the procedure?"
- "If the procedure didn't cover something, how did you work it out?"
- "What does your normal practice differ from the written procedure — and why?"
- "Have you seen the procedure followed exactly recently — or are there
  consistent variations?"
- "Was there pressure to deviate from the procedure for time or commercial reasons?"

### Organisation

- "How does the organisation communicate safety expectations on this task?"
- "What does your supervisor or manager say about how this work should be done?"
- "How would you describe production pressure on this team in the period
  leading up to the event?"
- "What happens when workers raise concerns or report hazards? Have you done
  that recently — what was the response?"
- "Are there enough resources — time, people, equipment, training — to do the
  work safely?"
- "Have similar events happened before in this team or operation? What happened
  with the lessons?"
- "How would you describe the safety culture in this work group? Is it safe to
  speak up?"
- "Is there anything you'd change about how this work is organised if you had
  the authority?"

### Cross-cutting probes (useful in any category)

- "Tell me more about that." (silence, allow elaboration)
- "What did that look like in practice?"
- "Help me understand — I want to make sure I've got this right."
- "What would you have needed to do this differently?"
- "If a new person started today and did this task, what would you tell them?"
- "What does 'going well' look like for this task on a normal day?"

### Anti-patterns — questions to avoid

- "Did you follow the procedure?" — yes/no, closes conversation, invites
  defensiveness
- "Why did you do X?" — invites justification, primes defensiveness
- Leading questions ("So the supervisor wasn't there, was that the problem?")
- Multiple questions stacked together
- Questions that contain the answer

---

## 9. Witness Interview Technique

ICAM and any incident investigation depends on the quality of witness
information. Interview technique is a discrete competency — the same person
can be a good investigator and a poor interviewer if they have not been
trained or coached in the craft.

### The PEACE model

PEACE is the UK police interview framework (developed 1992 in response to
documented coercion in the previous regime). It is now the international
default for fact-finding interviews and is widely adopted in regulatory and
WHS investigation.

| Stage | What it is | What it looks like |
|---|---|---|
| **P** Plan and Prepare | Read the file; identify topics; sequence questions; anticipate sensitivities; plan logistics (location, support person, recording) | 30+ minutes for any substantive interview |
| **E** Engage and Explain | Introductions; explain purpose, process, recording, voluntariness, support person; build rapport before substance | 5-10 minutes |
| **A** Account, Clarify, Challenge | Free recall first ("walk me through it"); then probe; clarify; challenge inconsistencies last and gently | 60-80% of interview time |
| **C** Closure | Summarise key points back; check understanding; invite anything else; explain next steps | 5 minutes |
| **E** Evaluate | Review for completeness; identify follow-up; reflect on technique | After interview |

### Cognitive interviewing — key techniques

Developed by Fisher and Geiselman (1992) to improve recall accuracy. Effective
for witnesses to events where memory is fragmentary or distressed.

- **Free recall** — let the witness tell the whole story uninterrupted before
  any probing
- **Context reinstatement** — ask the witness to mentally place themselves
  back at the scene; describe surroundings, sounds, smells, feelings before
  the event
- **Multiple recalls** — ask the witness to recall the event from a different
  perspective (e.g., what would a person standing across the room have seen?)
- **Reverse order recall** — work backward through the event; can surface
  details not captured in forward recall
- **Change perspective** — ask "if you were the supervisor, what would you
  have seen?"

### Fact-finding vs disciplinary interviews — the critical distinction

A fact-finding interview seeks to understand what happened. A disciplinary
interview seeks to test whether a worker has breached a rule. The two require
different procedural protections, different witnesses, and different documents.

**If the interview may inform disciplinary action, the worker must know that
in advance.** Otherwise the interview is compromised both ethically and
procedurally:
- Worker rights to representation differ (HSR, union, support person, legal
  representation depending on jurisdiction and process)
- The principle against self-incrimination applies (worker cannot be compelled
  to answer questions whose answers may incriminate them — Fair Work Act and
  case law)
- ICAM evidence may not be admissible in disciplinary process if procedural
  fairness was not afforded
- The Just Culture distinction (Reason; cross-reference frameworks.md §12) is
  the operative principle — investigation for learning, disciplinary for
  accountability, with explicit procedural separation

### Interview logistics

- **Location** — quiet, private, neutral; not the worker's manager's office
- **Support person** — offered as a right (HSR, union, family member, friend,
  legal representative depending on jurisdiction); document the offer and
  the choice
- **Recording** — increasingly the default; explain why (accuracy, dispute
  resolution); two-recorder redundancy for serious matters; written record
  produced from recording
- **Timing** — promptly after the event for memory accuracy; not within
  hours where the worker is in shock or fatigued; not in the middle of a
  shift if it can be avoided
- **Sequence of interviews** — eyewitnesses first, supervisors next, then
  area or operational management; senior leadership and officers later;
  avoid cross-contamination of accounts
- **Duration** — 60-90 minutes is the productive maximum; longer requires
  breaks; very long interviews are coercive and the resulting evidence is
  weaker
- **Note-taking** — record without filtering; verbatim where the words
  matter; flag where you're paraphrasing

### Common interviewing failures

- Interrupting free recall
- Asking leading questions
- Closing prematurely (failure to invite anything else)
- Confronting inconsistencies aggressively rather than gently exploring them
- Discussing the case in the presence of the witness before interview begins
- Conducting investigation interviews under disciplinary framing without
  notice
- Failing to document the offer of a support person
- Interviewing multiple witnesses together
- Interviewing the most senior or authoritative witness first (they then
  set the narrative for subsequent witnesses)

---

## 10. Witness Statement Format and Admissibility

A witness statement is a written record of what the witness has said. It may
become part of formal investigation records, regulator submissions, coronial
brief, or court evidence. Its form and process affect its admissibility and
weight.

### Format

A well-formed witness statement contains:

- **Identification** — full name, role, age (or DOB), employer, contact
  details, signature, date
- **Capacity** — the witness's connection to the event (eg, "I was working
  on Aisle 14 conducting stocktake from 14:05 until the incident at 14:22")
- **Source of knowledge** — what the witness saw, heard, did personally;
  not opinion, not what others told them (hearsay) unless explicitly framed
- **Chronological account** — events in time order; specific times where
  known; "approximately" where memory is approximate
- **Verbatim quotes** — direct speech captured in quotes; reported speech
  in paraphrase
- **Acknowledgements at the end** — "This statement is true and correct to
  the best of my knowledge"; signed and dated; pages numbered and initialled
- **Investigator details** — name and role of person taking the statement;
  date; location

### What makes a statement admissible

- **Voluntariness** — given without coercion, threat, inducement, or
  oppression; the worker understood that they could decline to answer
  questions or withdraw at any time
- **Procedural fairness** — opportunity to have a support person; chance to
  review and correct the statement; reasonable time to consider; not
  conducted under undue pressure
- **Accuracy** — the statement reflects what the witness said, not what the
  investigator interpreted; verbatim where it matters
- **Contemporaneity** — taken as close to the event as practicable; gap
  between event and statement noted

### What weakens or invalidates a statement

- Coercion or threat (express or implied)
- Inducement (express or implied promise of leniency, employment, payment)
- Worker not informed of the purpose of the interview
- Statement is the investigator's reconstruction rather than the witness's words
- Worker not given opportunity to review and correct before signing
- Statement taken when worker was clearly distressed, intoxicated, or
  cognitively impaired
- Multiple workers interviewed together influencing each other's accounts
- Worker not informed they could decline to answer self-incriminating questions

### Statement vs interview recording

Some investigations record interviews and prepare statements from the
recording; others record interviews and rely on the recording itself. Either
is defensible if properly handled, but:

- A statement prepared from recording should be reviewed and signed by the
  witness
- A recording without a statement is less convenient as evidence but is
  often the more accurate record
- Statements that look more polished than the witness's own speech raise
  questions — preserve the witness's voice

### Coronial and prosecution context

Witness statements taken in a WHS investigation may be requested in coronial
inquests or prosecutions. They may be admissible directly or as the basis
for later sworn evidence. **The standard for a WHS investigation statement
should be the standard for a coronial brief** — that's the safest assumption.

---

## 11. ICAM Variants — BHP, IOGP, Safety Wise

ICAM is not a single methodology; the term covers a family of related
approaches with subtle but operationally significant differences. Confusion
arises when an organisation says it uses "ICAM" without specifying which
variant — different investigators arrive at different conclusions because
they are applying different frameworks.

### Common core

All ICAM variants share:
- Systemic orientation (Reason's organisational accident model)
- Workshop-style analysis with multi-disciplinary team
- Mapping factors at the level of Absent/Failed Defences → Individual/Team
  Actions → Task/Environmental Conditions → Organisational Factors
- Corrective actions mapped to contributing factors rather than to symptoms

### BHP ICAM

The original (1990s). Developed for the mining industry. Emphasises:
- A strict bottom-up workshop discipline
- Distinction between contributory factors (closer to the event) and root
  causes (organisational factors)
- The Cause Pathway diagram as the central deliverable
- Strong corrective action framework with effectiveness verification

### IOGP ICAM

Adopted by the International Association of Oil & Gas Producers. Adds:
- Integration with bowtie analysis (use bowtie to identify the controls that
  failed, then ICAM to understand why)
- Specific consideration of process safety in addition to personal safety
- Tighter integration with high-reliability organisation thinking (Weick,
  Sutcliffe)
- Greater emphasis on absent defences as well as failed defences

### Safety Wise ICAM

The most commonly taught variant in Australia (Safety Wise Solutions is a
training provider). Variations:
- Slightly different terminology (Latent Hazards instead of Latent Conditions
  in some materials)
- Strong emphasis on the investigator's facilitation role
- 5-day Lead Investigator certification widely held in AU
- Pre-loaded into many AU organisations' incident management procedures

### Practical implication

When advising on or conducting an investigation:
- Confirm which ICAM variant the organisation uses (it's usually documented
  in the Incident Management Procedure)
- Where investigators have been trained in different variants, agree
  terminology upfront in the workshop
- For cross-organisation investigations (e.g., contractor and client),
  reconcile variants explicitly
- The differences are smaller than the surface terminology suggests — but
  not zero

---

## 12. AcciMap Methodology

Developed by Jens Rasmussen (1997) and refined by Paul Salmon and others.
AcciMap is a hierarchical accident causation analysis that maps factors
across multiple levels of the socio-technical system, including levels
above the organisation (regulator, government, industry).

### When to use AcciMap

AcciMap is more useful than ICAM when:
- The accident involves multiple organisations (operator, contractor,
  regulator, association)
- Regulatory failure is potentially implicated
- The system has multiple PCBUs with overlapping duties (cross-reference
  legislation.md §4)
- A royal commission or major inquiry is anticipated
- The lessons are intended to drive industry-wide or regulatory change

### The six AcciMap levels (Rasmussen)

1. **Government policy and budgeting** — legislation, funding allocations,
   national priorities
2. **Regulatory bodies and associations** — regulator capacity, industry
   self-regulation, standard setting
3. **Company management and planning** — corporate strategy, resource
   allocation, governance
4. **Technical and operational management** — management of operations,
   supervision, work design
5. **Physical processes and actor activities** — the work itself, frontline
   actions, immediate environment
6. **Equipment and surroundings** — plant, materials, physical environment

### Method

1. Establish a chronological account of the accident (similar to ICAM
   sequence of events)
2. For each contributing factor identified, place it at the appropriate
   level
3. Map the connections between factors (factor at level 2 enabled factor
   at level 4)
4. Identify factors that span multiple levels (these are typically the most
   important systemic findings)
5. Recommendations target the highest defensible level (the level at which
   change has the most leverage)

### Output

A hierarchical diagram with factors at each level connected to enable a
visual reading of the accident's systemic anatomy. The diagram itself is
the deliverable — typically prepared in workshops over several days.

### AcciMap vs ICAM — when to use which

| Use ICAM when | Use AcciMap when |
|---|---|
| Investigation is internal to one organisation | Investigation crosses organisations or includes regulator |
| Operational lessons are the primary output | Systemic or industry-level lessons are anticipated |
| 5-day workshop is feasible | Longer engagement is acceptable (typically 2-4 weeks) |
| Findings will inform corrective actions in the organisation | Findings may inform royal commission, regulatory reform |
| The accident is operational | The accident has industry-wide pattern implications (e.g., Pike River, Longford) |

Hopkins' analyses of Longford, Texas City, and Macondo are AcciMap-like in
their treatment of regulatory and corporate levels even when not formally
using the method.

---

## 13. Bowtie Worked Example

### Purpose of this section

§4 above describes bowtie analysis at the structural level. This section
walks through a worked example to make the method concrete.

### Worked example: Working at height — fall from height during rooftop
maintenance

**Top event**: Worker falls from height during rooftop maintenance work

**Threats (left side — what could cause the top event)**:

1. Anchor point fails during use
2. Worker unrestrained at edge (no fall protection in place)
3. Edge protection breached and not reinstated
4. Worker overreaches beyond safe positioning
5. Worker disoriented (fatigue, medical event, weather)

**Prevention barriers (left side — controls preventing the top event)**:

For each threat, the barriers that should prevent it:

| Threat | Prevention barriers |
|---|---|
| Anchor fails | Engineering certification of anchors; annual inspection and tagging; pre-use visual check; load testing |
| Worker unrestrained | Procedure mandating restraint/arrest connection before approaching edge; supervision; buddy check |
| Edge protection breached | Procedure requiring immediate reinstatement; supervisor verification; site-specific induction |
| Worker overreaches | Work positioning training; task design (bring work to worker rather than worker to edge); reach-pole equipment |
| Worker disoriented | Fitness for work check; fatigue management; medical pre-screening for rooftop work; weather hold criteria |

**Consequences (right side — what happens if the top event occurs)**:

1. Fatal fall to ground / lower level
2. Serious injury (fracture, head injury) survivable
3. Suspension trauma if arrested in harness
4. Minor injury / no injury

**Mitigation barriers (right side — controls reducing severity)**:

| Consequence | Mitigation barriers |
|---|---|
| Fatal fall | Fall arrest system that catches before strike; fall clearance calculation ensures clearance to strike |
| Serious injury | Fall arrest equipment correctly fitted to limit deceleration forces; rescue arrives quickly; first aid on site; medical evacuation plan |
| Suspension trauma | Trauma straps deployed by worker; rescue plan rehearsed and equipment present; rescue within 5-15 minutes |
| Minor injury | First aid; return to work assessment; root cause investigation regardless of outcome |

**Degradation factors (controls that can degrade barriers)**:

| Barrier | Degradation factor | Control on degradation |
|---|---|---|
| Anchor certification | Time since last inspection > schedule | Anchor register with overdue alert; planned inspection cadence |
| Restraint procedure | Production pressure to skip steps | Supervisor monitoring; toolbox talks; reporting of pressure to skip controls |
| Edge protection | Material movement requiring temporary breach | Procedure requiring immediate reinstatement; physical removable section design |
| Rescue plan | Plan not rehearsed; rescuers absent | Quarterly rescue drill; rescue capability verified before work commences |

**How to read the bowtie**

A bowtie tells a story: "If [threat] occurs, our [prevention barriers] should
stop it. If they all fail and we have the [top event], our [mitigation
barriers] should reduce the harm. The barriers themselves can be degraded by
[degradation factors] — and we have controls on those too."

The exercise of building a bowtie reveals where controls are absent (gaps in
the columns) and where controls are weak (single barriers vs layered).

### Use in practice

- Critical risk management (cross-reference frameworks.md §7) — bowtie per
  critical risk
- Pre-task risk assessment for high-energy work
- Post-incident analysis (which barriers failed?)
- Board reporting (visual representation of critical risk control posture)
- SWMS development (controls table is the bowtie's prevention column)

---

## 14. Legal Privilege Management During Investigation

### Why this matters

WHS investigations can become evidence in coronial inquests, prosecutions,
civil litigation, regulator enforcement, and disciplinary proceedings.
What is investigated, by whom, for what purpose, and how it is documented
determines whether the investigation is protected by legal privilege —
and whether protected material remains protected.

Getting this wrong is consequential: privileged material accidentally
disclosed may lose privilege permanently; non-privileged material treated
as if privileged exposes the organisation to adverse inferences and orders.

### Types of legal privilege relevant to WHS

**Legal advice privilege** — protects communications between client and legal
adviser for the dominant purpose of obtaining or giving legal advice.

**Litigation privilege** — protects communications and material prepared for
the dominant purpose of contemplated or pending litigation, including
regulator prosecution and coronial inquest.

**Without prejudice** — communications made in genuine attempt to settle a
dispute; not the same as privilege but a related protection.

**Public interest immunity** — government investigations may attract this
where disclosure would be contrary to public interest; rarely available to
private organisations.

### The dominant purpose test (Esso v FCT, 1999)

The High Court in *Esso Australia Resources Ltd v Federal Commissioner of
Taxation* (1999) established the dominant purpose test for litigation
privilege in AU:

> "The dominant purpose of a document is the one purpose which is dominant
> over any other; not necessarily the only purpose."

For an investigation to attract litigation privilege:
- Litigation must be reasonably anticipated (not merely possible)
- The dominant purpose of the investigation must be obtaining legal advice
  or preparing for that litigation
- This purpose must exist from the outset of the investigation

Investigations for operational learning are not privileged. Investigations
for legal defence preparation may be. Mixed-purpose investigations are not
privileged — the dominant purpose test fails.

### How privilege is established

The legal team (internal counsel and/or external solicitors) commissions
the investigation:

- A written engagement letter from legal to the investigator (internal or
  external) stating the dominant purpose is to provide legal advice and
  prepare for anticipated litigation
- The investigator reports to legal, not to operations
- Drafts circulate within the legal-privileged circle only
- Reference to the investigation in non-privileged communications is minimal
  and careful
- The final report is provided to legal; legal then provides advice to the
  organisation

### How privilege is lost

- Sharing privileged material outside the privileged circle (waiver)
- Referring to the substance of privileged material in non-privileged
  communications (waiver by reference)
- Disclosing privileged material to a regulator (issue waiver — disclosure
  for one purpose waives for all)
- Producing the privileged material in a different proceeding (subject matter
  waiver in some circumstances)
- Operating the investigation as a mixed-purpose exercise (privilege never
  attached)

### The parallel-investigation model

For serious incidents where both operational learning and litigation
preparation are needed:

1. **Operational ICAM** — for learning; not privileged; followed normally;
   produces lessons learned, alerts, system improvements
2. **Legal-led investigation** — commissioned by legal, dominant purpose
   legal advice/litigation; privileged; produces legal advice and
   defence preparation

The two investigations run in parallel; the operational ICAM does not
substitute for the legal investigation, and vice versa. Communication between
the two must be carefully managed to avoid contamination.

### Common errors

- Engaging an investigator without an engagement letter from legal — the
  investigation defaults to non-privileged
- "Marking" the report "Privileged and Confidential" without the substantive
  framework — this provides no protection
- Sharing draft privileged reports with operations management — waiver
- Discussing the privileged investigation findings in WHS team meetings —
  waiver
- Producing the privileged report to the regulator "voluntarily" thinking
  it will help — issue waiver and substantive risk
- Using the privileged investigation to inform disciplinary action against
  the worker — issue waiver and procedural fairness issues

### When privilege is appropriate

- Fatality or serious injury where prosecution is foreseeable
- Industrial manslaughter investigation
- Regulator enforcement action contemplated
- Civil litigation likely (contractor, third party, employee)
- High-profile incident with potential coronial inquest

### When privilege is not appropriate

- Routine HiPo investigations
- Operational learning from minor incidents
- Investigations where the organisation will share findings publicly (alerts,
  bulletins, industry forums)
- Cases where the regulator has already attended and obtained evidence
  directly

### Practical implication for the WHS function

The WHS function typically conducts operational investigations and is
typically not the holder of privilege. The decision to run a parallel
privileged investigation is taken by legal in consultation with the WHS
function. The WHS function's role:

- Recognise early when a serious incident may require privileged
  investigation in parallel
- Notify legal promptly (and document the notification)
- Conduct the operational ICAM with awareness that documents may be
  produced in proceedings (write with the regulator and coroner in mind)
- Avoid contaminating the privileged investigation by sharing material
  inappropriately
- Understand that privileged investigation findings may not be available to
  drive corrective action in the same way as operational ICAM findings —
  the operational investigation must stand on its own for that purpose

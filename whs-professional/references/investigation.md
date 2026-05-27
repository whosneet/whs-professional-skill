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

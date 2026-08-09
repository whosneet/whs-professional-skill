# Capability and Culture — BBS, Maturity Frameworks, Culture and Climate Measurement

This file covers three contested manager-level topics: behavioural-based safety (BBS),
maturity assessment frameworks, and the measurement of safety culture and climate.
All three sit at the intersection of WHS practice and organisational psychology, and
all three are commonly mishandled — either through uncritical adoption of legacy
programs, or through misapplication of frameworks designed for narrative purposes
as if they were measurement instruments.

The skill takes a position. That position is consistent with the Safety II / HOP /
Forge Works orientation established in `frameworks.md` §4, §5, and §11, and with
the named-thinker citations in `frameworks.md` §12. Where the position cuts against
common industry practice, it is because the evidence base and the named theorists
say so — not because the position is fashionable. Be willing to argue the position
in front of a board, an ELT, or a sceptical line manager.

---

## Table of Contents
1. [Behavioural-Based Safety (BBS)](#1-behavioural-based-safety-bbs)
2. [Maturity Assessment Frameworks](#2-maturity-assessment-frameworks)
3. [Safety Culture vs Safety Climate; Measurement](#3-safety-culture-vs-safety-climate-measurement)
4. [Output Checklist for Capability and Culture Tasks](#4-output-checklist-for-capability-and-culture-tasks)

---

## 1. Behavioural-Based Safety (BBS)

### Origins

BBS is the application of behaviour modification theory to occupational safety. The
intellectual lineage runs from B.F. Skinner's operant conditioning (1930s–50s) through
Komaki and colleagues, who in the late 1970s ran the first published studies applying
Antecedent-Behaviour-Consequence (ABC) analysis to industrial safety settings — most
notably Komaki, Barwick and Scott's 1978 study in a food manufacturing plant
(*Journal of Applied Psychology*, 63:434–445). The Komaki work demonstrated that
peer observation plus performance feedback produced measurable shifts in observable
safe behaviour over the study period.

From the late 1980s, BBS commercialised rapidly. The two dominant brands are:
- **DuPont STOP** (Safety Training Observation Program) — productised by DuPont's
  consulting arm; observation card systems; trained-observer model; aggregate
  reporting through a STOP database
- **Behavioral Science Technology (BST)** (the company's proper noun retains the
  US spelling), founded by Thomas Krause and John Hidley — Stanley Hodson
  co-authored their 1990 book *The Behavior-Based Safety Process* — marketed a
  more behaviourally rigorous variant with peer-led observation teams,
  facilitation training, and statistical process control on observation data

A long tail of in-house variants, consultant adaptations, and re-branded clones
follows. The product names change; the underlying ABC architecture does not.

### Core BBS Design Principles

The standard BBS program follows a consistent pattern, regardless of brand:

| Step | Activity | Purpose |
|---|---|---|
| 1. Critical behaviour identification | Identify 5–15 observable behaviours linked to high-frequency incident types — typically through pareto analysis of past incidents and observation of work | Defines what observers will look for |
| 2. Checklist development | Convert behaviours into a checklist with safe / at-risk options for each | Standardises observation |
| 3. Observer training | Train a subset of workers (typical ratio 1 in 10) in observation technique and feedback | Builds the observer cadre |
| 4. Observation | Trained observers conduct short observations of co-workers performing work | Generates the data |
| 5. Feedback | Immediate, in-person feedback to the observed worker — reinforce safe behaviour, discuss at-risk behaviour | Closes the behavioural loop |
| 6. Data aggregation | Observation cards aggregated weekly/monthly; % safe behaviour tracked over time | Generates the leading indicator |
| 7. Recognition | Reinforce safe behaviour through recognition, team-based incentives, public reporting of safe behaviour percentage | Drives the behaviour change loop |

The premise is straightforward: identify the behaviours that precede incidents,
observe them, give feedback, and reinforce the safe variants. Over time, the
proportion of safe behaviour rises, and incident frequency falls.

### Common Implementations

A typical mid-sized BBS deployment looks like this:
- 8–12 critical behaviours per work group
- Trained observer ratio of 1 in 10 to 1 in 20 workers
- Observation target of 2–4 observations per observer per month
- Aggregate % safe behaviour reported weekly to the site leadership team
- Observation card volume becomes a leading KPI; % safe becomes a culture KPI
- Quarterly review of trending at-risk behaviours; program adjustment

In larger organisations, observation data is rolled up across sites and reported
at division or corporate level — at which point the metric typically becomes
disconnected from the behaviour it was designed to influence.

### Critiques — The Skill's Position

BBS is one of the most extensively critiqued frameworks in safety science. The
critique is not that observation and feedback are bad — they are not. The critique
is that BBS positions individual worker behaviour as the primary lever for safety
improvement, which both contradicts the modern evidence base and creates a series
of predictable failure modes.

The four foundational critiques the skill draws on:

**Dekker** (*The Field Guide to Understanding 'Human Error'*, 2014; *Drift into
Failure*, 2011). BBS frames unsafe acts as the worker's choice. The observation
card asks "did the worker bend at the knees?" — not "did the load handling system
require lifting at all?" By design, BBS pulls attention away from the system
conditions that produced the behaviour, and toward the behaviour itself. This is
the reverse of the New View position that "human error" is a symptom of trouble
deeper in the system. A predictable secondary effect: workers learn to perform
safe behaviour when an observer is present, and learn to game observation cards
(self-observing during low-risk moments, recording only safe behaviour, observing
sympathetic colleagues) to avoid being marked at-risk. The behaviour modification
loop is corrupted by the observation context itself.

**Hopkins** ("What are we to make of safe behaviour programs?", *Safety Science*
44 (2006) 583–597 — his directly on-point BBS critique; *Failure to Learn*,
2008; *Disastrous Decisions*, 2012). BBS focuses
on personal safety behaviours — PPE compliance, body position, line of fire,
housekeeping. These behaviours are poorly correlated with process safety and
major-accident risk. The canonical case study is BP Texas City (2005): an organisation
with a strong personal safety culture, declining LTI rates, and an active BBS
program, that suffered a process safety catastrophe killing 15 workers because
the underlying process safety management system had degraded over years. High BBS
scores were not a leading indicator of the incident; they were a distraction from
the indicators that mattered. The primary investigation findings are in the US
Chemical Safety Board's *Refinery Explosion and Fire* report (CSB, 2007) and the
*Report of the BP U.S. Refineries Independent Safety Review Panel* (the Baker
Panel report, 2007); cite these directly when defending the point to a board or
regulator, rather than relying on Hopkins' secondary account alone. Hopkins argues
this is not an isolated case — Longford, Deepwater Horizon, and other
major-accident reviews show the same pattern. The 2006
paper also records the long-standing union critique: Australian unions have opposed
BBS as a "blame the worker" approach that shifts attention from the employer's duty
to control hazards — a critique any AU deployment will meet in consultation.
Cross-reference `frameworks.md` §12 for Hopkins citations.

**Provan** (Provan, Dekker & Rae, 2017, *Safety Science*, on the safety
professional role; Griffith PhD on the same subject). BBS positions the safety
professional as observer-trainer,
data-aggregator, and behavioural enforcer. This is the role that the Safety
Differently movement has spent twenty years arguing against. The time and resource
invested in running a BBS program — observer training, card data entry,
aggregate reporting, program governance — is typically not justified by outcomes
data; it is a textbook example of "safety clutter" — safety work that does not
contribute to operational safety (Rae, Provan, Weber & Dekker, 2018). The
opportunity cost is the systems-level work the safety professional could
otherwise be doing: critical control verification, Learning Teams, capacity
assessment, advisor work with line management.

**Hollnagel** (*Safety-I and Safety-II: The Past and Future of Safety
Management*, 2014). BBS counts deviations from
procedure — that is, it counts variability. The Safety II position is that
variability is the resource that enables work to succeed, not the problem to be
eliminated. By counting deviations from procedure as "at-risk", BBS misses the
positive adaptations workers make to enable work to succeed in the gap between
Work-as-Imagined and Work-as-Done. The observation checklist is a Work-as-Imagined
artefact applied to Work-as-Done; the at-risk behaviour count is the friction
between them, mislabelled as risk.

These four critiques converge on the same conclusion: BBS as a primary safety
strategy is intellectually incompatible with the modern evidence base on
organisational accidents.

### Evidence Base for BBS

The published evidence is mixed and weaker than the marketing suggests.

| Finding | Notes |
|---|---|
| Modest reductions in minor injuries during active deployment | Provider-reported studies suggest meaningful reductions in observable behavioural injuries during the program period; independent reviews are more equivocal |
| Outcomes typically not sustained post-program | When observation cadence drops or the program ends, behavioural metrics regress |
| Little evidence of effect on serious injuries or fatalities | Major-accident reduction is not demonstrated in the BBS literature; the metric and the outcome are not coupled |
| Substantial selection and publication bias | Most BBS evidence comes from studies funded by BBS providers; comparative studies against non-BBS interventions are rare |
| Confounding with broader management attention | A BBS deployment typically coincides with elevated leadership focus on safety, training, and resource — attributing improvement to BBS alone is methodologically unsound |

Reviews and meta-analyses (e.g., Tuncel, Lotlikar, Salem & Daraiseh, 2006,
"Effectiveness of behaviour based safety interventions to reduce accidents and
injuries in workplaces: critical appraisal and meta-analysis", *Theoretical
Issues in Ergonomics Science*, 7(3):191–209; Grindle, Dickinson & Boettcher,
2000, "Behavioral Safety Research in Manufacturing Settings: A Review of the
Literature", *Journal of Organizational Behavior Management*, 20(1):29–68)
suggest a small short-term effect on personal safety behaviours, with weak
external validity and no demonstrated effect on serious injury frequency.

### When BBS Is and Isn't Appropriate

A defensible position: BBS-style observation has a narrow legitimate use case.

**Defensible**:
- Narrow, high-frequency exposure where the behaviour is genuinely the proximate
  cause — e.g., PPE compliance in a known-hazard environment where the engineering
  controls are sound and the residual risk requires personal protection
- Peer-led, low-bureaucracy observation routines that generate safety conversations
  between workers, rather than data for management
- Time-limited deployment to address a specific known behavioural gap, with a
  defined exit condition

**Problematic**:
- BBS as the primary safety strategy or as a substitute for system improvement
- BBS data used as a leading culture KPI at board or ELT level
- BBS data used to attribute incidents to worker behaviour in investigation
- BBS programs where observation count becomes the metric — gaming is then
  guaranteed
- BBS in workplaces where process safety or major-accident risk dominates the
  hazard profile (refining, chemical, mining, MHFs)

**High risk**:
- Leadership uses BBS observation data in performance management or disciplinary
  process. This corrupts both the data and the reporting culture. If a worker
  knows that being observed performing an at-risk behaviour will be used against
  them, they will avoid being observed at all — undermining the entire program.
- BBS data is the primary evidence used to defend safety performance to the
  regulator or in a coronial inquiry. Hopkins (Texas City) and the Deepwater
  Horizon investigations are case studies of where this fails.

### If Your Organisation Has an Active BBS Program

A pragmatic position. Most large organisations in heavy industry have inherited
BBS programs that are politically and contractually difficult to dismantle.
The skill's position is not "kill it tomorrow" — it is to keep what's useful,
shed what's harmful, and rebalance toward the systems work the evidence supports.

**Keep**:
- The observation routine itself, where it generates safety conversations between
  workers (peer-led, low-bureaucracy)
- The discipline of going to the work and observing it directly — this is sound
  practice whether or not the BBS framing is used
- The volunteer observer cadre, if it functions as an engaged-worker network rather
  than a data-collection apparatus

**Shed**:
- Consequence-based behaviour scoring (using observation data to discipline workers
  or score performance)
- Observation count as a leading KPI at division or corporate level — it incentivises
  card volume, not safety insight
- The use of % safe behaviour as a culture indicator at board or ELT level
- Use of BBS observation data in incident investigation as evidence of worker behaviour
- Aggregate behaviour scoring tied to bonus, contract performance, or recognition

**Rebalance toward** (see `frameworks.md` §5 for HOP, §11 for Forge Works):
- Critical Control Verification (CCV) as the systems-level equivalent — verifies
  whether the controls exist, not whether the worker complied
- Learning Teams as the worker-engaged equivalent — curiosity-driven, system-focused,
  worker-led
- Capacity vs demand framing — when demand exceeds capacity, behaviour is constrained;
  observing behaviour without addressing capacity is symptom management

> **Practical implications**: When asked to advise on a BBS program — design,
> review, refresh, or wind-down — open with the position and the evidence base.
> Do not produce a BBS program design as if the framework were uncontested.
> Where the client wants to retain a behavioural component, design it as a Learning
> Team / peer observation hybrid, not a classical BBS observation-and-feedback
> loop. Where the BBS data is being used at board or ELT level as a culture
> metric, flag it as a measurement risk and propose alternative leading indicators
> (see `analytics.md` §5).

---

## 2. Maturity Assessment Frameworks

Maturity frameworks describe stages of organisational development against a defined
dimension — in WHS, typically culture or capability. They are widely cited, widely
mis-used, and useful when applied with appropriate caveats. The skill's position:
maturity frameworks are diagnostic conversation tools, not measurement instruments.

### Hudson Cultural Ladder

The ladder originates with Ron Westrum's three-part organisational typology
(1993/2004) — pathological, bureaucratic, generative — which Patrick Hudson
(Leiden University; later TU Delft) extended to five levels with Dianne Parker
under Shell's Hearts and Minds program. The five-level ladder
describes five stages of safety culture, ordered by the organisation's relationship
to information, failure, and risk:

| Level | Characterisation | Information flow | Response to failure | Blame |
|---|---|---|---|---|
| **Pathological** | "Who cares about safety as long as we're not caught" | Suppressed | Cover up; shoot the messenger | High; individual |
| **Reactive** | "Safety is important — we do something every time we have an accident" | Investigated after the event | Fix the worker; tighten the rule | High; individual |
| **Calculative** | "We have systems in place to manage all hazards" | Collected systematically; rarely acted on | Audit; corrective action | Medium; procedural |
| **Proactive** | "We work on the problems that we still find" | Sought out actively | Learn; improve the system | Low; system focus |
| **Generative** | "HSE is how we do business round here" | Actively shared; freely flowing | Learn deeply; the system adapts | Low; restorative |

The framework also describes characteristic attitudes to risk awareness,
organisational structure, accountability, and the role of the safety function at
each level. Hudson's original work, including the well-known visual of the ladder,
is publicly available through Shell HSE publications and Hudson's academic papers
(notably Hudson, 2007, *Safety Science* 45:697–722).

The Hudson ladder is widely cited in petroleum, mining, aviation, and rail.
It is useful as a narrative framing device for culture conversations — it gives
leaders a vocabulary for where the organisation is and where it might be going.

### DuPont Bradley Curve

A four-stage model commercialised by DuPont's consulting arm. The Bradley Curve
maps the development of safety culture against injury rate, with the explicit
theory that as culture matures, accountability for safety shifts from system
rules to individual choice to peer behaviour.

| Stage | Characterisation | Accountability locus |
|---|---|---|
| **Reactive** | Natural instincts; safety by chance | None — incident-driven |
| **Dependent** | Supervision; rules; discipline | Management |
| **Independent** | Personal knowledge, commitment, self-management | Individual |
| **Interdependent** | Team helps; care for others; networks | Peer / team |

The Bradley Curve is almost always presented with an injury-rate decline overlaid —
visually compelling, and central to DuPont's consulting pitch. As intellectual
property of DuPont, it should be cited carefully when used in client work
(attribute the framework to DuPont; do not present it as a generic industry model).

The theoretical claim — that mature culture has accountability located at the
peer level rather than the management level — is broadly consistent with
psychological safety theory (Edmondson; see §3 below) and with the Reason
"informed culture" framing. It is also commercially convenient, in that the
Interdependent stage describes a workforce that has substantially internalised
the BBS observation-and-feedback model that DuPont also sells.

### IOGP HSE Capability Assessment

Published by the International Association of Oil & Gas Producers (now IOGP).
A structured capability assessment with rating scales across multiple HSE
management system dimensions, tied to the IOGP good practice library and member
benchmarking data. Widely used in the resource sector for self-assessment,
contractor assessment, and joint venture due diligence.

Strengths: structured, multi-dimensional, tied to a published good practice
library, allows comparison against industry benchmarks where IOGP member data
is available. Weaknesses: sector-specific (oil and gas); the rating scales are
self-assessed unless an external IOGP-aligned assessor is engaged; assessment
fatigue is real in large contractor environments.

### Heinrich Pyramid (1931)

Not a maturity framework — but the originator of the ratio-based safety pyramid
that persists in industry practice, and worth covering because every WHS manager
will encounter it.

H.W. Heinrich, in *Industrial Accident Prevention* (1931), published the ratio
that became the canonical safety pyramid: for every major injury, there are 29
minor injuries and 300 no-injury accidents (later iterations added unsafe acts
at the base). The pyramid is taught as a prediction tool — reduce the base
(unsafe acts and near-misses) and the apex (major injuries) will follow.

The Heinrich pyramid is one of the most repeatedly debunked frameworks in safety
science, and one of the most persistent in practice.

**Critiques**:
- **Manuele** (*Heinrich Revisited*, 2002; *Reviewing Heinrich*, 2011) —
  the ratio was based on insurance data of unknown methodology; the underlying
  data has never been replicable; the categorisation is inconsistent. The
  pyramid is not a measurement; it is an assertion.
- **Hopkins** (*Failure to Learn*, 2008) — the mechanisms that produce minor
  injuries are not the same as the mechanisms that produce major accidents.
  Process safety failures (Texas City — see the CSB and Baker Panel reports cited
  in §1) and major-accident events do not predictably follow from elevated
  minor-injury rates; in some cases the reverse is true (the organisation is so
  focused on personal safety that process safety degrades unnoticed). The pyramid
  is a Safety I artefact that doesn't survive contact with the major-accident
  literature.
- **Modern incident data** — multiple post-Heinrich studies have failed to
  reproduce the ratios in any consistent form; the proportions vary by
  industry, by classification convention, and by reporting culture, and they
  do not predict major-accident risk.

The pyramid persists because it is visually compelling and because it justifies
the BBS / observation paradigm — "reduce unsafe acts at the base, prevent the
fatality at the apex". The evidence base does not support this prediction. When
the pyramid appears in a board paper or program design, flag it.

### The "Where Are We On the Ladder?" Trap

Maturity frameworks are useful for narrative framing of culture conversations.
They are problematic when treated as measurement.

Common failure modes:
- **The self-declaration trap** — leadership declares the organisation at Proactive
  or Generative without external evidence. Hudson himself cautioned against this;
  the descriptors at the upper levels are aspirational and easy to map onto an
  organisation that wants to be there
- **The scorecard trap** — using Hudson or Bradley levels as a competitive measure
  across business units or contracts. This invites the same gaming dynamics as any
  ranked metric — the underlying culture data is too coarse and too contested for
  ranking
- **The target trap** — "we will be Generative by 2027". Culture maturity is
  emergent from many systems-level changes; it is not a deliverable to be scheduled
- **The substitute trap** — using maturity level as a substitute for leading and
  lagging indicators of system health. Maturity assessment tells you something
  about how the organisation talks about safety; it tells you very little about
  whether the controls are in place

### How to Use Maturity Frameworks Well

| Use | Approach |
|---|---|
| As a diagnostic conversation tool with leadership | Ask leaders to describe behaviour at each level; ask which level matches what they see. Use the discussion, not the answer |
| As a narrative anchor for culture strategy | "We're operating somewhere between Calculative and Proactive — here's what would need to be true to be consistently Proactive" |
| As an external assessment with independent assessors | Better than self-assessment, but treat as one data point among many — not the answer |
| With explicit acknowledgement that the framework is heuristic | Always caveat: this is a way of describing where we are, not a measurement |

### How to Use Them Badly

| Use | Why it fails |
|---|---|
| As a competitive measure across BUs or contracts | Coarse, contested, invites gaming |
| As a numerical target with a date | Maturity is emergent, not delivered |
| As a substitute for leading and lagging indicators | The framework doesn't measure what the indicators measure |
| As a board-reported KPI | Implies measurement precision the framework doesn't have |
| As justification for a specific intervention or program | The framework is too broad to drive specific design |

### Comparison Table

| Framework | Origin | Structure | Strengths | Weaknesses | When to use |
|---|---|---|---|---|---|
| **Hudson Cultural Ladder** | Westrum's typology (1993/2004), extended to five levels by Hudson and Parker for Shell's Hearts and Minds program; Hudson 2007, *Safety Science* | 5 levels: Pathological → Reactive → Calculative → Proactive → Generative; multi-dimensional descriptors | Vocabulary for culture conversation; widely recognised in petroleum, mining, aviation; intellectually grounded | Self-assessment risk; descriptors aspirational at upper levels; not a measurement | Culture strategy framing; leadership discussion; narrative anchor |
| **DuPont Bradley Curve** | DuPont consulting; commercial product | 4 stages: Reactive → Dependent → Independent → Interdependent; injury rate overlaid | Visually compelling; consistent with peer-culture theory; widely cited | DuPont IP — cite carefully; commercially aligned with BBS sale; injury-rate overlay is illustrative, not predictive | Culture conversation with operations leaders; cite when consistent with broader strategy |
| **IOGP HSE Capability Assessment** | International Association of Oil & Gas Producers | Multi-dimensional capability rating scales tied to IOGP good practice library | Structured; sector-specific; benchmarking against IOGP members | Sector-bound; self-assessment unless external assessor; assessment fatigue in contractor environments | Resource sector self-assessment; contractor assessment; JV due diligence |
| **Heinrich Pyramid** *(not a maturity framework)* | H.W. Heinrich, 1931 | Ratio model: 1 : 29 : 300 (or variants) | Visually compelling; widely taught | Not reproducible; mechanisms differ between minor and major accidents; predicts personal safety, not process safety; repeatedly debunked | Avoid; if it appears in a board paper, flag it |

> **Practical implications**: When asked for a maturity assessment, lead with the
> framing — "this is a diagnostic conversation, not a measurement". Use Hudson
> as the default narrative vocabulary unless the organisation has another in use.
> If asked to present a single maturity level at board, decline — present a range
> with descriptors and evidence, not a single point. If a Bradley Curve appears
> in materials produced by consultants, ensure the DuPont attribution is intact
> and the injury-rate overlay is identified as illustrative. If a Heinrich pyramid
> appears, propose to replace it with an HiPo distribution chart (see
> `analytics.md` §2) — the same visual function, with a defensible underlying
> dataset.

---

## 3. Safety Culture vs Safety Climate; Measurement

The terms "safety culture" and "safety climate" are often used interchangeably.
They are not the same. The distinction matters because they require different
measurement approaches and support different management responses.

### Culture vs Climate — The Distinction

**Safety culture** is the underlying assumptions, beliefs, and norms about safety
that an organisation holds. It is slow-changing, embedded in routines and
relationships, and not directly measurable through survey. Schein's broader work
on organisational culture (artefacts, espoused values, basic underlying assumptions)
applies — the assumptions are at the deepest layer and are largely invisible to
those who hold them.

**Safety climate** is the observable expression of culture in attitudes, perceptions,
and reported behaviour at a point in time. Climate is faster to change, easier to
measure (through survey), and is the operational proxy used in most "culture
survey" instruments. Strictly, "safety climate survey" is the more accurate term;
"safety culture survey" is widely used but technically misleading.

| Dimension | Culture | Climate |
|---|---|---|
| What it is | Underlying assumptions and norms | Observable attitudes and perceptions |
| Time horizon | Slow-changing (years) | Faster-changing (months) |
| Measurability | Hard to measure directly; ethnographic methods | Measurable through survey instruments |
| What surveys actually measure | Climate (usually) | Climate |
| Management lever | System change, leadership behaviour, hiring | Communication, programs, leadership signals |

When a survey is described as a "culture survey", it is almost certainly a climate
survey. This is not a problem in practice — climate is the actionable layer — but
it is worth being precise about, especially in executive communication.

### Reason's Informed Culture — the Product of Four Subcultures

Reason (*Managing the Risks of Organizational Accidents*, 1997) argues that an
effective safety culture is an **informed culture** — one in which the
organisation knows about its hazards, its controls, and the state of both at
any time. The informed culture is not a component to be built directly: it is
the **product** of four interlocking subcultures. The model remains the most
useful practitioner framework for what an effective safety culture actually
consists of. Cross-reference `frameworks.md` §12 for Reason's citation.

| Subculture | Definition | What "good" looks like |
|---|---|---|
| **Reporting** | Workers report hazards, near-misses, errors without fear | High volume of reports; near-miss / minor event ratios that reflect actual exposure, not selective reporting |
| **Just** | Workers are treated fairly when something goes wrong; the distinction between error, at-risk behaviour, and reckless behaviour is consistently applied | Disciplinary actions are rare and proportionate; investigations focus on system, not individual |
| **Flexible** | The organisation can shift decision-making authority and structure to match the demands of the situation, particularly in abnormal or emergency conditions | Frontline workers have authority to stop work; emergency response is rehearsed and adaptive |
| **Learning** | The organisation absorbs lessons from events and acts on them | Investigation findings translate into system change; lessons cross sites; the organisation can describe what it has learned |

The product of the four is the informed culture itself: critical control health
is visible, HiPo intelligence is current, data is acted on — the organisation
knows what is actually happening at the sharp end.

Reason's specific argument: **reporting culture and just culture are the
foundations**. Without them, the organisation does not know what is happening at
the sharp end, and the other two subcultures — and the informed culture they
together produce — cannot function. This is why disciplinary
responses to error are so damaging — they collapse the reporting culture and
with it the visibility the organisation depends on.

### Edmondson — Psychological Safety

Edmondson (*The Fearless Organization*, 2018) established psychological safety
as a measurable team-level construct, building on her earlier academic work — the
error-detection study in hospital teams (Edmondson, 1996, *Journal of Applied
Behavioral Science*, 32(1):5–28) and the validated Team Psychological Safety
scale (Edmondson, 1999, *Administrative Science Quarterly*, 44:350–383).
Cross-reference `frameworks.md` §12 for Edmondson's citation.

Psychological safety is the belief that one will not be punished or humiliated
for speaking up with ideas, questions, concerns, or mistakes. It is the
precondition for reporting culture and learning culture — without psychological
safety, workers will not report.

Edmondson's seminal finding (1996, *Journal of Applied Behavioral Science*, in
hospital teams) was that higher-performing teams reported *more* errors, not
fewer, because reporting was psychologically safe. The teams with low error rates
were not actually making fewer errors; they were hiding them. This is the
empirical foundation for the modern case against punitive responses to error.

Edmondson's **Team Psychological Safety scale** (7 items, validated in Edmondson,
1999, *Administrative Science Quarterly*) is widely used in research and practice.
It is freely accessible and commonly described as free to use with attribution,
but the precise permitted-use terms are not formally published — for any deployed
survey, and especially any commercial deployment, attribute the instrument
explicitly to Edmondson (1999) and confirm permitted-use terms before
reproducing the full scale. Items include:

- If you make a mistake on this team, it is often held against you (reverse scored)
- Members of this team are able to bring up problems and tough issues
- People on this team sometimes reject others for being different (reverse scored)
- It is safe to take a risk on this team
- It is difficult to ask other members of this team for help (reverse scored)
- No one on this team would deliberately act in a way that undermines my efforts
- Working with members of this team, my unique skills and talents are valued and utilized

(Items are quoted verbatim from Edmondson's published scale — retain the
original wording, including the US spelling "utilized", when deploying.)

The scale measures at team level — it can be aggregated to business unit if
sample sizes permit, but the unit of analysis is the team. Aggregating to
organisation level loses meaning.

### Climate Survey Instruments

Several validated climate survey instruments are in widespread use. The major
ones:

| Instrument | Origin | Length | Notes |
|---|---|---|---|
| **NOSACQ-50** (Nordic Safety Climate Questionnaire) | Kines et al., 2011; National Research Centre for the Working Environment (Denmark) | 50 items, 7 dimensions | Validated across multiple languages and industries; free to use with registration; standard Nordic / European choice |
| **HSE Safety Climate Tool (SCT)** | UK Health and Safety Executive (sold through HSE Books / its commercial publishing arm) | Around 40 statements across 8 factors | Commercially licensed (licence purchased per workforce size; not free); UK regulator lineage; widely used in UK process industries. Confirm current item count and licence terms with HSE Books before relying on specifics |
| **Loughborough Safety Climate Tool** | Loughborough University | Variable | Academic instrument; often used in research |
| **In-house / consultant-built instruments** | Varies | Varies | Common in large organisations; validation quality varies widely |

**A note on DNV ISRS**: the International Safety Rating System is sometimes
listed alongside climate surveys; it is not one. ISRS is a commercial
management-system audit and rating protocol in the Frank Bird / International
Loss Control Institute (ILCI) lineage — an assessor-led audit of management
processes, not a perception survey. Treat ISRS results as audit data, not
climate data (see `frameworks.md` §15 for the audit / assurance distinction).

Many commercial WHS consultancies sell custom climate survey instruments
(branded variants such as Diagnostic Risk Inventory, etc.). The decision criterion
should be psychometric validation, not brand — an instrument with published
reliability and validity data, applied consistently over time, beats a glossy
unvalidated alternative.

### Survey Design Principles for Safety Climate

**Anonymity is non-negotiable**

True anonymity, not pseudo-anonymity. If respondents are asked to identify their
team, contract, or role at a level where the combination uniquely identifies
them, the survey is not anonymous. Workers learn this quickly, and response
quality degrades — they answer the answer they think management wants to hear.
Minimum reporting group size of n=10 protects anonymity at the analysis stage;
sub-groups smaller than this should be aggregated up or suppressed.

**Frequency**

| Cadence | Use case |
|---|---|
| Annual | Sufficient for trend on a full instrument; standard for organisation-level climate survey |
| Pulse (quarterly or monthly, 5–7 questions) | Specific question; rapid feedback on program launch or change; not a substitute for the full survey |
| Quarterly full survey | Over-surveying for most workforces; survey fatigue degrades response rate and quality |
| Ad-hoc post-event | Useful for specific event response (post-restructure, post-incident) — frame the purpose clearly |

Annual full survey plus pulse surveys for specific questions is the standard
configuration. Quarterly full surveys are common in organisations that have
mistaken activity for engagement and should be reconsidered.

**Open-text responses**

Quantitative scoring is useful for trend; open-text responses are where the
high-value insight sits. A well-designed survey includes at least one open-text
question per major dimension. Open-text analysis is labour-intensive but
disproportionately valuable — themes that don't appear in the quantitative
scoring routinely emerge in the comments.

**Sub-group reporting**

Apply the same minimum reporting-group size set out under "Anonymity is
non-negotiable" above (n=10): never report sub-group breakdowns in a way that
allows identification of individual responses, suppress cells below the
threshold, and state the suppression rule in the methodology.

### What to Measure

A defensible safety climate survey covers, at minimum:

| Domain | What it captures | Example item |
|---|---|---|
| Reporting culture | Workers' willingness to report hazards and near-misses without fear | "I feel comfortable reporting safety concerns to my supervisor" |
| Just culture perception | Perceived fairness when something goes wrong | "When incidents happen, the focus is on understanding what happened, not blaming individuals" |
| Leadership commitment | Whether workers see leaders prioritising safety in practice, not slogans | "My senior leaders' decisions show that safety is genuinely a priority" |
| Psychological safety | Edmondson 7-item scale, validated | See the Edmondson scale earlier in this section |
| Worker engagement on safety decisions | Whether workers feel consulted on decisions that affect their safety | "I am consulted on safety decisions that affect how I do my work" |
| Critical control awareness | Whether workers know the critical controls for their work | "I know what the critical controls are for the high-risk tasks I do" |
| Psychosocial wellbeing | Exposure to psychosocial hazards (e.g. harmful workplace behaviour); aligns with psychosocial hazard regulations (see SKILL.md §7) | "I am not exposed to behaviour at work that affects my mental health" |

The list should be calibrated to the organisation. Adding domains because
"we want to ask about X" without a clear use for the data is a common failure mode.

### What Not to Do with Culture / Climate Data

| Don't | Why |
|---|---|
| Tie individual or team-level scores to incentives | Corrupts the data — incentivised workers will answer for the incentive, not honestly |
| Use as a substitute for incident, hazard, or near-miss report rate | Climate is perceptual; reporting rates are behavioural — both are needed |
| Hide low scores | Transparency about findings is itself a culture intervention; suppressing the data signals that the data is dangerous to leadership |
| Compare BUs as if scores are like-for-like | Workforce demographics, hazard profile, and historical context vary; ranking creates pressure to inflate scores, not improve them |
| Report a single number ("our culture score is 7.3") | The single-number framing implies a precision the instrument doesn't have, and obscures the dimensions that matter |
| Run the survey and not act on it | The fastest way to destroy survey credibility; workers will not respond next time |

### Connecting Culture Data to Action

The value of a climate survey is what the organisation does with it. Common patterns:

| Finding | Likely diagnostic | Possible action |
|---|---|---|
| Low scores on reporting culture | Workers fear consequences of reporting | Review post-incident response patterns; specifically examine the most recent serious incident — was the response curious or punitive? |
| Low scores on psychological safety | Team-level dynamics; leader behaviour | Focus on leader behaviour interventions; do not roll up to organisation-level training |
| Low scores on just culture | Disciplinary inconsistency; perceived unfairness in past events | Review last 12 months of disciplinary outcomes for consistency; communicate the just culture algorithm and how it is applied |
| Low scores on leadership commitment | Workers see leaders saying safety matters but acting otherwise | Review recent leadership decisions where safety competed with production — what was the visible outcome? |
| High scores across the board with low reporting and hazard report rates | Survey may be inflated by selection bias or response acquiescence; check open-text for the real signal | Cross-reference behavioural data; consider whether the survey design or deployment has issues |
| Low scores on critical control awareness | Program has not landed at the front line | Review program reach and facilitator quality (see `programs.md` §4) |

The pattern: every survey finding should connect to a specific behavioural data
source (incident reports, hazard reports, CCV data, EAP utilisation) and a
specific action owner. A climate survey that produces a report with no action
owner is a climate survey that should not have been run.

> **Practical implications**: When asked to design or interpret a safety climate
> survey, lead with the culture / climate distinction — be precise about what the
> survey can and can't tell you. Default to a validated instrument (NOSACQ-50 or
> Edmondson's scale where psychological safety is the focus) over a bespoke build.
> Insist on anonymity, transparency of findings, and a connection to action
> before the survey is launched. When asked to interpret findings, triangulate
> against behavioural data (reporting rates, hazard reports, EAP utilisation
> per `analytics.md` §6) — climate data alone is rarely sufficient evidence
> for a specific intervention. When asked to compare BUs, push back on ranking
> — present findings as themes and dimensions, not league tables.

---

## 4. Output Checklist for Capability and Culture Tasks

Before finalising any output on BBS, maturity assessment, or culture and climate
measurement, confirm:

- [ ] **BBS program position is informed by current evidence base, not legacy
      adoption**. If a BBS program is proposed, designed, or being defended,
      the output engages with the Dekker / Hopkins / Provan / Hollnagel critique
      and the evidence base on outcomes — not just the marketing of the
      program
- [ ] **Maturity framework usage is diagnostic conversation, not scorecard**.
      Maturity levels are not presented as targets, KPIs, or rankings; they
      are presented as narrative vocabulary with explicit acknowledgement that
      the framework is heuristic
- [ ] **DuPont Bradley Curve, if used, is attributed and treated as commercial
      IP**. The injury-rate overlay is identified as illustrative, not
      predictive
- [ ] **Heinrich pyramid, if it appears, is flagged**. Where possible, replaced
      with HiPo distribution analysis (see `analytics.md` §2)
- [ ] **Culture / climate distinction is precise**. Survey instruments are
      identified as climate measurement; "culture" is used for the underlying
      norms and assumptions
- [ ] **Validated instruments are preferred over bespoke**. Where bespoke is
      used, the rationale is stated and the psychometric properties are at
      least acknowledged as a limitation
- [ ] **Anonymity is preserved**. Sub-group reporting respects minimum group
      size (n=10); the methodology states the threshold
- [ ] **Survey findings are connected to action**. No climate survey output is
      delivered without an action owner and a connection to behavioural data
- [ ] **Named theorists are cited correctly where the framework or critique
      originates with them** — Skinner / Komaki for BBS origin; Dekker, Hopkins,
      Provan, Hollnagel for the BBS critique; Westrum for the underlying
      typology and Hudson (with Parker) for the five-level cultural ladder;
      DuPont for the Bradley Curve; Heinrich for the pyramid; Manuele and
      Hopkins for the pyramid critique; Reason for the informed culture and its
      four subcultures; Edmondson for psychological safety
- [ ] **Position is taken, not hedged**. The skill takes a Safety II / HOP /
      Forge Works-aligned position consistent with `frameworks.md` §4, §5, §11,
      and §12. The position is defensible in front of a board, an ELT, or a
      sceptical operations manager — and is presented as such

---

For organisation-specific culture survey instruments, maturity assessment history,
and named programs that may include BBS elements, load `references/company.md`.
For the underpinning theory of Safety II, HOP, and the named thinkers cited above,
load `references/frameworks.md` §4, §5, and §12.

# Workers Compensation & Return to Work — Australia & New Zealand

Workers compensation and return-to-work management is the lagging operational
outcome of WHS performance and a daily WHS-manager workload. WC schemes sit
outside the WHS Acts but interact with them constantly — premium impact,
claims investigation, suitable employment, IME findings, RTW plans, and
psychosocial claim management are all WHS-adjacent tasks that WHS managers
are routinely expected to lead or co-own with HR.

This file covers the scheme architecture across each AU jurisdiction and NZ,
the claim lifecycle, premium mechanics, and the operational issues a WHS
manager will face. Use it alongside `legislation.md` (WHS Acts that govern
prevention) and `hazards.md` (operational hazard frameworks that drive
exposures into claims).

---

## Table of Contents
1. [Scope and the WHS / WC Distinction](#1-scope-and-the-whs--wc-distinction)
2. [Scheme Architecture Overview](#2-scheme-architecture-overview)
3. [State & Territory Schemes](#3-state--territory-schemes)
4. [New Zealand — ACC Scheme](#4-new-zealand--acc-scheme)
5. [Claim Lifecycle](#5-claim-lifecycle)
6. [Premium Impact Mechanics](#6-premium-impact-mechanics)
7. [Independent Medical Examinations (IMEs)](#7-independent-medical-examinations)
8. [Suitable Employment Principles](#8-suitable-employment-principles)
9. [Return to Work Coordinator Role](#9-return-to-work-coordinator-role)
10. [Psychological Injury Claims](#10-psychological-injury-claims)
11. [Journey Claims](#11-journey-claims)
12. [Presumptive Provisions](#12-presumptive-provisions)
13. [Common Manager-Level Traps](#13-common-manager-level-traps)
14. [Output Checklist — Compensation Tasks](#14-output-checklist)

---

## 1. Scope and the WHS / WC Distinction

WHS Acts and workers compensation Acts are two parallel regulatory regimes
that apply concurrently to the same workforce. They are not interchangeable
and their purposes diverge:

| Regime | Purpose | Operative Acts | Regulator |
|---|---|---|---|
| **WHS / OHS** | Prevention — duty to manage risks SFAIRP before harm occurs | WHS Act 2011 (model); OHS Act 2004 (VIC); HSWA 2015 (NZ) | SafeWork NSW, WorkSafe VIC, WHSQ, etc. |
| **Workers Compensation** | Compensation and rehabilitation — restoring an injured worker after harm has occurred | Workers Compensation Act 1987 (NSW); WIRC Act 2013 (VIC); WCRA 2003 (QLD); state equivalents | icare/SIRA, WorkSafe VIC, WorkCover QLD, etc. |

A breach of WHS duties does not automatically establish liability for a
compensation claim, and acceptance of a compensation claim is not an
admission of WHS fault. They are tested under separate statutes with
different burdens and different remedies.

> For WHS Act provisions, load `references/legislation.md`. For psychosocial
> hazard regulations (Part 3.1A) that drive psychological injury claims, see
> `legislation.md` §9.

### Why this lives in a WHS skill
WHS managers carry direct or shared accountability for:
- Premium negotiations and renewal forecasts
- RTW plan development for injured workers
- Liaison with insurers, treating practitioners, and rehabilitation providers
- Suitable employment identification
- Claim acceptance/denial advice (sometimes with input from HR/legal)
- Psychosocial claim management (where WHS investigation and WC claim
  develop in parallel)
- Linking claim trends to prevention strategy

Treating compensation as an HR-only function severs the prevention/outcome
loop that drives systemic safety improvement. The HiPo and incident data
from the WHS system, the workers compensation claim data, and the RTW
outcomes are three views of the same underlying risk picture.

---

## 2. Scheme Architecture Overview

Australian workers compensation is administered jurisdiction-by-jurisdiction,
with eight state/territory schemes plus the Commonwealth (Comcare) scheme.
There is no national workers compensation Act. Schemes vary across three
axes:

### Centralised vs decentralised

| Model | Description | Examples |
|---|---|---|
| **Centralised (monopoly)** | Single statutory insurer underwrites all policies; private insurers cannot compete | QLD (WorkCover Queensland), SA (ReturnToWorkSA), NT, NSW (icare — Nominal Insurer), Comcare |
| **Decentralised (private market)** | Multiple licensed insurers compete; regulator approves and oversees | WA, TAS, ACT (private sector), NSW (self-insurers operating alongside icare) |
| **Hybrid** | Single statutory insurer with appointed agents handling claims administration | VIC (WorkSafe Victoria + agents EML, Allianz, Gallagher Bassett) |

### No-fault principle
Most AU schemes (and NZ ACC) are no-fault: a worker injured in the course
of employment is entitled to statutory benefits regardless of who was at
fault. Exceptions exist for serious and wilful misconduct, self-inflicted
injury, and (in some schemes) intoxication. Common law damages claims for
employer negligence remain available in some jurisdictions subject to
impairment thresholds (notably VIC, QLD); they are abolished or heavily
restricted in others (notably ACT, SA, NZ).

### Premium funding model
Premium is calculated using a three-factor formula common to most schemes:

**Premium = Industry Rate × Insurable Wages × Experience Modification**

- **Industry rate**: a base premium rate per $100 of wages, set per ANZSIC
  industry class. High-risk industries (mining, construction, road freight)
  attract higher rates than office-based industries
- **Insurable wages**: total wages plus declared remuneration (super,
  allowances, certain non-cash benefits — defined per scheme)
- **Experience modification**: a factor reflecting the employer's recent
  claims experience relative to industry peers. Below 1.0 = better than
  average (premium discount); above 1.0 = worse than average (premium
  loading). Typically applied to employers above a minimum premium
  threshold (varies by scheme, generally $30K–$500K base premium)

Smaller employers below the experience-rating threshold pay the industry
rate unmodified. Self-insured employers carry their own claims liability
and are exempt from premium but must demonstrate financial capacity and
WHS performance to retain the licence.

---

## 3. State & Territory Schemes

Summary table across all AU jurisdictions, followed by jurisdiction-by-
jurisdiction detail.

| Jurisdiction | Primary Insurer | Regulator | Lead Legislation | Model |
|---|---|---|---|---|
| NSW | icare (Nominal Insurer) + self-insurers | SIRA | Workers Compensation Act 1987 + WIM Act 1998 | Centralised + self-insurance |
| VIC | WorkSafe Victoria + agents | WorkSafe Victoria | WIRC Act 2013 | Hybrid (statutory + agents) |
| QLD | WorkCover Queensland | OIR | Workers' Compensation and Rehabilitation Act 2003 | Centralised + self-insurance |
| WA | Multiple private insurers | WorkCover WA | WC&IM Act 1981 (+ 2023 reforms) | Decentralised |
| SA | ReturnToWorkSA | ReturnToWorkSA | Return to Work Act 2014 | Centralised |
| TAS | Multiple private insurers | WorkCover Tasmania | Workers Rehabilitation and Compensation Act 1988 | Decentralised |
| NT | Multiple private insurers | NT WorkSafe | Return to Work Act 1986 (NT) | Decentralised |
| ACT | Multiple private insurers (ACT private sector); Comcare (ACT public service) | WorkSafe ACT | Workers Compensation Act 1951 (ACT) | Decentralised |
| Cth | Comcare | Comcare | Safety, Rehabilitation and Compensation Act 1988 (SRC Act) | Centralised + licensed self-insurance |

### NSW
- **Insurer**: icare (Insurance & Care NSW) — a public corporation operating
  as the Nominal Insurer for the bulk of NSW employers. icare is the
  insurer of last resort and the default insurer for most policies
- **Self-insurance**: large employers may apply to operate as self-insurers
  under licence (Coles, Woolworths, Downer, Wesfarmers, major councils,
  state-owned corporations). Self-insurance requires demonstrated WHS
  capability, financial capacity, and a guarantee or bond
- **Regulator**: SIRA (State Insurance Regulatory Authority) — sets premium
  filing, monitors scheme performance, handles complaints and disputes
- **Legislation**: Workers Compensation Act 1987 (NSW) (benefits and
  liability) + Workplace Injury Management and Workers Compensation Act
  1998 (NSW) (the WIM Act — covers claims management, injury management,
  RTW)
- **Claims pathway**:
  1. Worker notifies employer
  2. Employer notifies insurer within **5 days** (s 44 WIM Act)
  3. Provisional liability decision within **7 days** of notification —
     weekly payments and reasonable medical commence on provisional
     liability for up to **12 weeks**
  4. Full liability decision within **21 days** (or up to 12 weeks where
     reasonable excuse — s 267 WIM Act)
  5. Acceptance > ongoing weekly payments (capped at statutory tiers) +
     medical and related expenses + lump sum permanent impairment (≥11%
     WPI for non-psychological; ≥15% for psychological under s 65A)
  6. Denial > worker may request internal review > Personal Injury
     Commission (PIC) for dispute resolution
- **Recent reform**: Minns Government 2024 review of icare and the
  scheme's psychological injury performance — expect ongoing reform
  movement, particularly around s 11A (reasonable management action)

### Victoria
- **Insurer**: WorkSafe Victoria (statutory authority) underwrites all
  premium; claims administered by **Authorised Agents** (currently
  EML, Allianz, Gallagher Bassett, DXC). Agent assignment is set at
  policy renewal based on employer size/industry
- **Self-insurance**: available to qualifying employers; smaller market
  than NSW
- **Regulator**: WorkSafe Victoria (combined regulator and insurer)
- **Legislation**: Workplace Injury Rehabilitation and Compensation Act
  2013 (WIRC Act) — consolidated the previous Accident Compensation Act
  1985 and Accident Compensation (WorkCover Insurance) Act 1993
- **Claims pathway**:
  1. Worker notifies employer
  2. Employer notifies agent within **10 days**
  3. Agent makes liability decision within **28 days** of receiving the
     claim
  4. Acceptance > weekly payments (first 13 weeks at 95% PIAWE; 14–130
     weeks at 80%; >130 weeks subject to capacity reassessment) +
     medical + impairment benefits
  5. Common law damages available if **30% WPI (whole-person impairment)**
     threshold met (serious injury gateway under s 335 WIRC), or via
     narrative test
- **Notable**: VIC has no journey claims coverage (abolished 2010);
  uses OHS not WHS terminology; Workplace Manslaughter offence has
  meaningful interplay with serious WC claims that involve fatal injury

### Queensland
- **Insurer**: WorkCover Queensland (default insurer; statutory authority).
  Self-insurance is available through application to the Office of
  Industrial Relations (OIR)
- **Regulator**: OIR (Office of Industrial Relations) — sits within DJAGS
- **Legislation**: Workers' Compensation and Rehabilitation Act 2003
  (WCRA)
- **Claims pathway**:
  1. Worker lodges claim directly with WorkCover (online or paper) or
     via employer
  2. WorkCover decides claim within **20 business days** (s 134 WCRA)
  3. Acceptance > statutory benefits (NWE-based weekly payments,
     medical, rehabilitation) + lump sum DPI for permanent impairment
  4. Statutory and common law are concurrent — worker can pursue common
     law damages after statutory entitlement is exhausted, subject to
     DPI threshold and notice of claim requirements (Personal Injuries
     Proceedings Act 2002 parallels)
- **Notable**: QLD retains the strongest common law damages access
  among AU jurisdictions; presumptive silicosis (2019) and PTSD for
  first responders (2020) provisions are in WCRA

### Western Australia
- **Insurer**: multi-insurer private market — approximately 8 licensed
  insurers competing (e.g., Allianz, QBE, Zurich, Insurance Commission
  of WA for government). Insurers must be approved by WorkCover WA
- **Regulator**: WorkCover WA — sets recommended premium rates,
  administers disputes, licenses insurers
- **Legislation**: Workers' Compensation and Injury Management Act 1981
  (WC&IM Act). The Workers Compensation and Injury Management Act 2023
  (effective 1 July 2024) replaces and modernises the 1981 Act
- **Notable**: WA retains journey claims coverage; mining and resources
  sector dominates premium profile; common law damages available with
  election rules
- **Self-insurance**: available — historically a number of large mining
  and resources companies operate as self-insurers

### South Australia
- **Insurer**: ReturnToWorkSA (statutory authority — centralised monopoly
  since 1986; renamed from WorkCoverSA in 2015)
- **Regulator**: ReturnToWorkSA (combined regulator and insurer)
- **Legislation**: Return to Work Act 2014 (RTW Act) — replaced the
  Workers Rehabilitation and Compensation Act 1986 in major 2015 reform
- **2015 reform highlights**: weekly payments reduced from 130 weeks
  to 104 weeks for most workers; medical entitlements wound back;
  significantly increased focus on RTW outcomes and employer
  accountability; common law damages largely abolished
- **Notable**: SA's reform was the most aggressive scheme restructure in
  AU in recent decades — significantly reduced benefit duration and
  cost; the policy bet was that earlier and more aggressive RTW would
  generate better worker outcomes and lower scheme cost

### Tasmania
- **Insurer**: multi-insurer private market (approximately 6 licensed
  insurers)
- **Regulator**: WorkCover Tasmania
- **Legislation**: Workers Rehabilitation and Compensation Act 1988
  (Tas)
- **Notable**: smaller scheme; common law damages available subject
  to thresholds; journey claims subject to limited coverage

### Northern Territory
- **Regulator**: NT WorkSafe
- **Insurer**: multi-insurer private market
- **Legislation**: Return to Work Act 1986 (NT) — formerly the Workers
  Rehabilitation and Compensation Act
- **Notable**: covers journey claims; presumptive PTSD and firefighter
  cancer provisions

### ACT
- **Insurer (private sector)**: multi-insurer private market for ACT
  private employers
- **Insurer (ACT public service)**: Comcare — ACT public sector workers
  are covered under the Commonwealth Safety, Rehabilitation and
  Compensation Act 1988 scheme by long-standing administrative
  arrangement
- **Regulator**: WorkSafe ACT (for WHS); private insurers regulated under
  ACT WC framework
- **Legislation**: Workers Compensation Act 1951 (ACT)
- **Notable**: covers journey claims; small jurisdiction with strong
  intersection with Comcare scheme

### Commonwealth — Comcare
- **Insurer**: Comcare — covers Commonwealth public sector employees,
  ACT public sector employees, and **licensed self-insurers** nationally
- **Licensed self-insurers (national licensees)**: large national
  employers granted Comcare self-insurance licence and exempted from
  state schemes (Telstra, Optus, K&S Freighters, Pacific National,
  ReturnToWork SA partner entities, banking sector entities, others —
  list updated by SRCC). Self-insurance under Comcare consolidates
  WC liability under a single national scheme rather than maintaining
  policies in eight jurisdictions
- **Regulator**: Comcare (regulator + insurer + self-insurance overseer);
  Safety, Rehabilitation and Compensation Commission (SRCC) makes
  licensing decisions
- **Legislation**: Safety, Rehabilitation and Compensation Act 1988
  (SRC Act). Work Health and Safety Act 2011 (Cth) covers the WHS
  duties for the same employer cohort
- **Notable**: the SRC Act runs separately from state schemes —
  benefits, common law access, definitions of injury, and timeframes
  all differ. National self-insurers must run dual-stream WHS programs
  (state WHS Acts for state-based workers + Cth WHS Act for Cth-jurisdiction
  workers if any) but a single WC claims process under SRC

---

## 4. New Zealand — ACC Scheme

New Zealand operates a **single, universal, no-fault accident compensation
scheme** — the Accident Compensation Corporation (ACC). The scheme covers
all New Zealand residents and temporary visitors for personal injury by
accident, regardless of where, when, or how the injury occurred (with
narrow exceptions). There is no separate workers compensation scheme.

### Scheme structure
The Accident Compensation Act 2001 (NZ) (replacing the Accident
Compensation Act 1972 and a series of intermediate Acts) establishes
five separate **accounts**, each funded by a distinct levy:

| Account | Funding source | Covers |
|---|---|---|
| **Work Account** | Work levy paid by employers; experience-rated for large employers | Work-related personal injury |
| **Earners' Account** | Earners' levy paid by employees through PAYE | Non-work injuries to earners |
| **Non-Earners' Account** | Government funding from general taxation | Injuries to non-earners (children, retirees, unemployed) |
| **Motor Vehicle Account** | Petrol levy + vehicle registration component | Motor vehicle injuries (including work-related driving) |
| **Treatment Injury Account** | Levies on relevant practitioners + Crown | Injuries caused by medical treatment |

### Levy structure for employers
The Work levy is set per industry classification (CU — Classification
Unit). Industry rates are reviewed annually by ACC. For larger employers:

- **Experience Rating Programme** — applies to employers with annual
  liable earnings above the threshold (approximately NZD $735K leviable
  earnings in recent years). Loadings/discounts of up to ±50% based
  on three-year claims experience relative to industry
- **Accredited Employers Programme (AEP)** — large employers (typically
  >NZD $750K annual leviable earnings) can opt to manage their own
  workplace injury claims for up to three years (Partnership Discount
  Programme — PDP) in exchange for a substantial levy discount. Closest
  AU equivalent to self-insurance
- **Workplace Safety Discount** — for small employers (<NZD $565K annual
  liable earnings approximately) demonstrating injury management and
  safety performance — 10% discount

### Benefits
Entitlements under the ACC Act 2001 include:

| Benefit | Coverage |
|---|---|
| Weekly compensation | **80% of pre-incapacity earnings**, capped at maximum weekly earnings; 7-day stand-down for non-work injury; from day 1 for work injury |
| Medical/treatment costs | Reasonable and necessary treatment costs |
| Vocational rehabilitation | Return-to-work support including retraining |
| Independence Allowance / lump sum for permanent impairment | Determined under impairment assessment (American Medical Association Guides 4th edition with NZ modifications) |
| Funeral grant + survivor's grant + weekly compensation to dependants | Fatal injury |

### The ACC bar — restricted common law
Section 317 of the Accident Compensation Act 2001 (NZ) **bars personal
injury claims at common law** where ACC cover applies. The bar is broad
but not absolute — exemplary damages remain available, and certain
non-physical injury claims may proceed. The practical effect: NZ
employers face very limited civil damages liability for workplace
injuries; the scheme is the worker's remedy.

### WHS / ACC separation
WHS obligations under HSWA 2015 run separately from the ACC scheme.
A WorkSafe NZ prosecution and an ACC claim are independent processes —
acceptance of an ACC claim is not an admission of HSWA breach, and HSWA
penalties are not affected by ACC outcomes. The two regimes intersect
when:
- Notifiable events under HSWA generate both an ACC claim and a WorkSafe
  investigation
- Reparation orders under the Sentencing Act 2002 against a convicted
  employer may include sums payable to the injured worker over and
  above ACC benefits
- The Accredited Employer Programme requires WorkSafe-aligned safety
  management capability as a precondition

> For HSWA detail (PCBU duty, officer due diligence, notifiable events,
> WorkSafe NZ enforcement powers), load `references/legislation.md` §3.

---

## 5. Claim Lifecycle

Claim lifecycle is generic across schemes — the steps look similar but
timeframes and decision-makers vary. WHS managers should know the
critical points where the employer's actions or omissions materially
change the trajectory.

### Step-by-step (generic)
1. **Incident occurs** — worker injured at or arising out of employment
2. **Worker notifies employer** — verbally, in writing, or via incident
   report. In some schemes, late notification can become grounds for
   denial (rarely sustained where injury is genuine)
3. **Employer notifies insurer** — statutory timeframe applies
   (NSW: 5 days; VIC: 10 days; QLD: worker often lodges directly; WA:
   typically 7 days; SA: 5 days; Comcare: as soon as practicable).
   Failure to notify is an offence under most schemes and can trigger
   regulator action
4. **Provisional liability** — insurer makes an early determination to
   commence benefits while liability is being investigated. NSW
   provisional liability runs **12 weeks** under s 267 WIM Act; other
   schemes operate similar early-pay frameworks. Provisional liability
   protects worker income during the investigation period
5. **Investigation and full liability decision** — insurer assesses:
   employment connection, mechanism of injury, medical causation,
   any exclusionary factors (e.g., s 11A NSW for psychological).
   Timeframes typically 60–90 days from notification
6. **Acceptance** — weekly payments continue; medical and related
   expenses paid; RTW planning commences with employer and worker
7. **RTW management** — graduated return through suitable employment;
   IMEs commissioned as needed; certificate of capacity from treating
   doctor renewed on cycle (typically 28–90 days); plan reviewed and
   updated
8. **Closure / lump sum / common law** — when worker reaches MMI
   (Maximum Medical Improvement), insurer assesses permanent impairment
   (WPI assessment — AMA Guides 4th or 5th edition depending on scheme).
   Lump sum may be paid. In schemes that retain common law (VIC, QLD,
   WA), worker may elect to pursue damages
9. **Denial pathway** — worker may seek internal insurer review > scheme
   regulator review > tribunal (Personal Injury Commission in NSW;
   Magistrates Court in VIC; QIRC in QLD; State Administrative Tribunal
   in WA; SAET in SA; etc.)

### Critical decision points for WHS managers
- **Notification timeframe** — never withhold notification to "investigate
  first". The statutory clock starts when the employer is on notice
- **Provisional liability period** — employer's investigation contributes
  to the liability decision. Document witness statements, incident
  facts, and prior similar injuries within this window
- **RTW plan signature** — many schemes require employer-insurer-worker
  tripartite plans. Late or absent plans extend claim duration and
  premium impact
- **IME notification** — workers must attend, but reasonable notice
  applies. WHS manager involvement in scheduling and worker support
  improves engagement

---

## 6. Premium Impact Mechanics

Understanding how premium responds to claims is essential for WHS
managers operating at coordinator-through-manager level, particularly
when reporting to ELT or boards.

### The premium formula
For experience-rated employers (above the minimum premium threshold):

**Premium = Industry Rate × Insurable Wages × Experience Modification Factor**

Or in scheme-specific variants:
- NSW: Premium = (Industry Premium Rate × Wages) × Performance Premium
  Adjustment + Dust Diseases Contribution + GST
- VIC: Premium = (Industry Rate × Rateable Remuneration) × Employer
  Performance Rating
- QLD: Premium = (Industry Rate × Wages) × Industry Claims Performance
- Comcare: Premium = Base Premium + Prudential Margin × Claims
  Experience Adjustment

### Experience rating windows
Premium experience rating uses a **lagged rolling window** — typically
three claim years, lagged by 12 months from the policy year. The lag
exists because claims continue to develop after notification, so the
insurer needs settled claim cost data before reflecting it in premium.

Practical effect: a serious claim today affects premium from the policy
year starting **12–24 months** after the claim is lodged, and continues
to affect premium for **3 years**. A claim lodged in late 2024 hits the
2026/27 policy year and remains in the calculation through 2028/29.

### Impact magnitude
A single significant claim (medium-duration LTI, $50K+ claim cost) can
push the experience modification factor up materially:
- Small employer (~$100K base premium): single $80K LTI may add 10–25%
  to renewal premium
- Medium employer (~$500K base premium): single $250K serious claim may
  add 15–30%
- Large employer (~$5M base premium): cumulative claims experience
  matters more than individual claims; trend over the three-year window
  drives renewal

### What drives cost (and therefore premium)
- **Claim duration** matters more than claim count. A short claim
  costing $5K does relatively little. A 18-month claim costing $250K
  is the cost driver
- **Psychological injury claims** consistently the highest cost per
  claim — see §10
- **Permanent impairment lump sums** — settle on closure but priced
  into the claim cost
- **Common law damages** (where available) — can dwarf statutory cost
- **Medical and treatment cost inflation** — particularly orthopaedic
  surgery, mental health treatment

### What does NOT reduce cost (and is unlawful)
Common gaming behaviours that surface in workplaces under premium
pressure — all are unlawful, all are counterproductive:

| Behaviour | Why it fails |
|---|---|
| Suppressing worker notification ("don't lodge a claim") | Worker can lodge directly with insurer; subsequent investigation exposes the employer; potential breach of s 44 WIM Act (NSW) or equivalents |
| Delaying employer notification | Statutory offences; worsens insurer relationship; claim still accepted in most cases |
| Reclassifying work injury as a journey claim | Journey coverage varies by jurisdiction; insurer investigates mechanism; misclassification surfaces in IME or treating doctor records |
| Pressuring worker to "use sick leave" instead of WC | Industrial Relations Commission and tribunal authorities; unlawful interference |
| Providing fictitious "light duties" | Workers comp investigators verify suitable employment is real and meaningful; courts can characterise as constructive denial |
| Threatening employment if claim is lodged | Breach of general protections under Fair Work Act 2009 + adverse action provisions; potential WHS Act discriminatory action offences (s 104 model Act) |

The lawful and effective levers to reduce premium are: **prevention**
(reduce incident frequency and severity), **early intervention** (rapid
RTW, suitable employment, recovery at work), and **claim management
discipline** (engage with insurer, contest unfounded claims through
proper process, manage IME and treatment proactively).

---

## 7. Independent Medical Examinations

The Independent Medical Examination (IME) is the insurer's primary tool
for assessing capacity, treatment, causation, and reaching MMI (Maximum
Medical Improvement). WHS managers need to understand the IME process
and the IME finding because it drives the RTW plan and the claim
trajectory.

### Purpose of IMEs
Insurers commission IMEs to:
- Assess current work capacity (hours, duties, restrictions)
- Determine MMI — has the worker reached the stable end-point of
  recovery?
- Assess whether treatment is reasonable and necessary
- Assess causation — is the injury work-related?
- Assess permanent impairment (whole-person impairment under AMA Guides)
- Resolve disputed clinical questions (e.g., where treating doctor and
  insurer disagree)

### Worker obligations and rights
Workers have a **statutory obligation** to attend an IME when properly
notified by the insurer. Refusal or non-attendance without reasonable
excuse can suspend entitlements.

Worker rights (vary by jurisdiction):
- Reasonable notice (typically 10 working days minimum)
- Reasonable travel — insurer must arrange or cover travel costs;
  excessive distance is grounds for relocation request
- Support person — most jurisdictions allow a support person at the
  IME (not for clinical examination but for the discussion component)
- Copy of the IME report — provided to the worker in most jurisdictions
  (NSW, VIC, QLD provide on request; some schemes within prescribed
  timeframes)
- Right to obtain own independent medical opinion at worker's election

### WHS manager role
- **Understand the IME finding** — read the report, understand what
  capacity is recommended, what restrictions apply, what treatment is
  endorsed
- **Translate to operational reality** — capacity assessment drives the
  RTW plan; restrictions need to be modelled against actual duties on
  site
- **Brief the worker** — many workers find IMEs intimidating. Pre-IME
  brief on the process (what to expect, that they can bring a support
  person, that the assessor is not their treating doctor) improves
  engagement
- **Engage with the insurer** — if the IME finding contradicts the
  treating doctor or the lived reality of the workplace, raise it with
  the case manager. IME findings are evidence, not gospel

### Common traps
- **Insurer-friendly assessors** — a small number of IME assessors
  consistently produce capacity findings favourable to insurers and
  unfavourable to workers. This is a known issue across schemes; raised
  in multiple government reviews. Workers and treating doctors are
  entitled to challenge findings
- **Treating doctor disagreement** — IME and treating doctor opinions
  may diverge sharply. The scheme's dispute resolution process exists
  for this; do not act on the IME alone if the treating doctor's
  certificate of capacity says otherwise
- **MMI determination** — declaration of MMI shifts the claim from
  active treatment to closure/lump sum phase. WHS managers should
  understand when MMI is in scope and what it changes for ongoing
  weekly payments
- **Causation findings** — an IME that finds the injury is not
  work-related (or only partially work-related) can trigger denial or
  apportionment. This is a high-stakes finding that should involve
  legal review

---

## 8. Suitable Employment Principles

The duty to provide suitable employment to an injured worker is a
statutory obligation, not a goodwill exercise. It sits at the heart
of the RTW framework in every AU scheme.

### Statutory basis
- NSW: s 49 WIM Act — employer must provide suitable employment to a
  worker who has current work capacity, where reasonably practicable
- VIC: ss 103–104 WIRC Act — return to work obligations including
  suitable employment
- QLD: s 232 WCRA — obligation to participate in rehabilitation and
  RTW; s 232A duty to take all reasonable steps to provide suitable
  duties
- SA: s 18 RTW Act 2014 — provide suitable employment
- WA: s 155A WC&IM Act (and equivalents in 2023 Act)
- Comcare: SRC Act provisions on suitable employment and RTW

### What "suitable" means
Suitable employment must be:

| Criterion | Detail |
|---|---|
| Within worker's capacity | Hours, physical demands, cognitive demands match the certificate of capacity / IME finding |
| Suited to worker's skills, experience, qualifications | Cannot be unskilled work assigned to a skilled worker without justification |
| Available at the worker's location | Reasonable travel; in remote operations, may include accommodation arrangements |
| Not lower-grade than pre-injury role without justification | Pay should match pre-injury; grade should match where possible |
| Genuine | Real duties producing real value, not fictitious "make-work" |

### Hierarchy of suitable employment options
Employers should work through this hierarchy when planning RTW:

1. **Same role with full duties** (worker has full capacity)
2. **Same role with modified duties** (graduated return, reduced
   hours, reduced demands)
3. **Same role with workplace modification** (ergonomic adjustment,
   assistive equipment, environmental change)
4. **Alternative role in same workplace** (redeployment to a different
   position the worker is capable of performing)
5. **Alternative role in another workplace within the same business**
   (where the original site cannot accommodate)
6. **Vocational retraining for a different role** (where the original
   role is no longer accessible due to permanent restriction)
7. **Genuine inability** (only after the above options have been
   exhausted and documented)

### WHS manager role
- **Identify options** — work with line managers and HR to map what
  duties are realistically available within the worker's capacity
- **Document the graduated RTW plan** — written, signed by worker,
  employer, treating doctor, and insurer where required
- **Monitor progress** — graduated plans typically step up capacity
  fortnightly; need active management, not set-and-forget
- **Manage the workplace** — supervisors and peers need briefing on
  the worker's restrictions and the RTW plan. Worker should not have
  to repeatedly explain their situation
- **Document genuine attempts** — if redeployment fails or no suitable
  duties are available, the documentation trail matters for both the
  WC claim and any subsequent termination

### Recovery at work
Recovery-at-work principles (endorsed across AU and NZ schemes) treat
work as part of recovery, not a competitor to it. Evidence
consistently shows:
- Workers returning to even modified duties recover faster than those
  on full restriction
- Long-term absence from work correlates with poorer functional
  outcomes, more mental health complication, and lower likelihood of
  ever returning
- Early light duties (within 1–2 weeks of injury where capacity exists)
  is the highest-impact intervention available

The traditional model of "rest until fully recovered then return" is
clinically unsupported and operationally counterproductive.

---

## 9. Return to Work Coordinator Role

Several schemes mandate the appointment of a **Return to Work
Coordinator** for employers above a defined size threshold. The role
is a defined statutory position, not a generic case management
function.

### Statutory requirement by jurisdiction

| Jurisdiction | Threshold | Source |
|---|---|---|
| NSW | Annual basic tariff premium >$50,000 OR self-insurer; OR designated as Category 1 employer | s 26 Workers Compensation Act 1987; SIRA RTW Coordinator requirements |
| QLD | Annual wages >$7.275M OR self-insured; OR Government employer | s 226 WCRA |
| VIC | Larger employers (typically rateable remuneration >$2M); voluntary for smaller | WIRC Act + WorkSafe Victoria guidance |
| SA | Designated employer thresholds | RTW Act 2014 |
| WA | RTW programs required; coordinator function commonly assigned | WC&IM Act 1981 |
| Comcare | All licensed self-insurers must have rehabilitation case managers | SRC Act + Comcare Rehabilitation Management System |

### Certified RTW Coordinator qualification
NSW, QLD, and several other schemes require coordinators to complete
a state-approved RTW Coordinator training course before performing the
role:
- NSW: SIRA-approved 2-day RTW Coordinator course (refresher at 5
  years)
- QLD: WorkCover QLD approved 5-day Rehabilitation and Return to Work
  Coordinator course; refresher every 3 years
- VIC: WorkSafe Victoria-approved RTW Coordinator course (voluntary
  for most employers; required for larger)

### Coordinator functions
- **Initial contact** — typically within 3 business days of injury
  notification (statutory in most schemes)
- **Develop and document the RTW plan** — tripartite plan with worker,
  treating practitioner, and (where required) insurer
- **Liaise with the insurer** — manage information flow, dispute
  resolution where required
- **Liaise with treating practitioners** — workplace context to the
  doctor, certificate of capacity interpretation back to the workplace
- **Coordinate suitable duties** — work with line managers and HR to
  identify and implement suitable employment
- **Document everything** — RTW case file maintained per scheme
  requirements; auditable
- **Monitor and escalate** — recognise when a claim is escalating
  (psychosocial overlay, plateau in recovery, breakdown in worker-
  manager relationship) and respond

### Common organisational configuration
- **HR-led with WHS shared accountability** — most common in medium to
  large employers; HR carries the case manager role with WHS support
  for hazard analysis and prevention linkage
- **WHS-led** — common in smaller employers where WHS Manager is the
  generalist
- **Outsourced to a rehabilitation provider** — increasingly common for
  larger employers; the provider supplies the qualified coordinator and
  case management; employer retains accountability and decision-making
- **In-house team** — large self-insurers (Comcare licensees, NSW self-
  insurers) typically operate dedicated injury management teams

The legal accountability cannot be outsourced. The employer remains
the duty holder under the WC Act regardless of who is performing the
coordinator function in practice.

---

## 10. Psychological Injury Claims

Psychological injury claims have grown materially as a share of total
claim cost and duration across all AU schemes. WHS managers should
understand both the operational and legal dimensions because these
claims behave differently from physical injury claims.

### The cost and duration picture

| Metric | Physical claim (average) | Psychological claim (average) |
|---|---|---|
| Average cost | $20K–$40K | $80K–$120K (3x) |
| Average duration | 8–12 weeks | 50–80 weeks (6x) |
| Denial rate | 5–10% | 15–25% (higher) |
| RTW rate at 6 months | 75–85% | 35–50% |
| Common law/lump sum incidence | Lower | Higher |

(Figures are scheme-level averages; specific organisations vary widely.
SIRA, WorkSafe Victoria, and Safe Work Australia publish annual data.)

### Definition and statutory tests
Each scheme defines compensable psychological injury and the
employment-causation test:

| Jurisdiction | Test | Source |
|---|---|---|
| NSW | Personal injury arising out of or in the course of employment; employment a "substantial contributing factor"; "real and not imagined" injury | s 4 + s 9A Workers Compensation Act 1987 |
| VIC | Mental injury where employment is the "predominant cause" | s 18 WIRC Act |
| QLD | Psychiatric/psychological injury where employment is "the major significant contributing factor" | s 32 WCRA |
| SA | Psychiatric impairment compensable where work is a "significant contributing cause" | RTW Act 2014 |
| Comcare | Employment "significantly contributed" to the injury | s 5B SRC Act |

### Reasonable management action exclusions
Most schemes exclude psychological injury arising from **reasonable
management action taken in a reasonable manner**. This is the most
frequently litigated exclusion across jurisdictions:

- **NSW s 11A WIM Act**: no compensation where injury wholly or
  predominantly caused by reasonable action by employer with respect
  to transfer, demotion, promotion, performance appraisal, discipline,
  retrenchment, dismissal, provision of employment benefits
- **VIC**: similar exclusion under WIRC Act
- **QLD**: similar — "reasonable management action in connection with
  the worker's employment"
- **Comcare**: s 5A SRC Act exclusion for reasonable administrative
  action

The two-limb test is constant: **(1) was the action reasonable, and
(2) was it taken in a reasonable manner?** Both limbs must succeed for
the exclusion to apply. The most common point of failure is the second
limb — process and communication, not the underlying decision.

### Implications for WHS managers
Psychological injury claims sit at the intersection of WHS and HR. A
manager who treats them as HR-only loses the prevention linkage that
the WHS framework requires. Key points:

- **Link to psychosocial hazard management** — psychological injury
  claims are the lagging outcome of unmanaged psychosocial hazards
  under WHS Regulations Part 3.1A. Investigate them through ICAM, map
  contributing factors to the SWA psychosocial hazard categories, feed
  back into the prevention system
- **Avoid the HR-only trap** — claim management may sit with HR, but
  the WHS investigation should run in parallel under WHS Regulations
- **Confidentiality** — psychological claims have higher confidentiality
  requirements; investigation must be conducted with appropriate
  privacy
- **Recovery at work** — early modified duties more effective than full
  restriction; same principle as physical injury but harder to operate
  where the workplace itself is part of the perceived stressor
- **Mediation** — psychological claims more commonly resolve through
  mediation than physical claims; relationship breakdown is often the
  central issue
- **Privilege** — WHS investigation findings can become disclosable in
  WC proceedings. Document with that in mind; engage legal where the
  claim is likely to escalate

> For psychosocial hazard regulatory framework and the SWA 2022 Code of
> Practice on Managing Psychosocial Hazards at Work, load
> `references/legislation.md` §9. For the link to the Respect@Work
> positive duty and sexual harassment claims, see `legislation.md`
> §9 (Section 47C SDA).

---

## 11. Journey Claims

Coverage for injuries sustained travelling between home and work
("journey claims") varies sharply across AU jurisdictions. This is a
frequent source of confusion in multi-jurisdictional employers.

| Jurisdiction | Journey claims coverage | Notes |
|---|---|---|
| NSW | Limited — "real and substantial" connection to employment required (s 10 Workers Compensation Act 1987); direct route between residence and workplace | Substantially narrowed in 2012 reforms |
| VIC | **Excluded** since 2010 reforms | Not compensable except where journey is in the course of employment (work travel) |
| QLD | Limited — direct route between worker's home and workplace; deviations break coverage | s 35 WCRA |
| WA | **Covered** | Recognised under WC&IM Act; direct journey + reasonable deviation |
| SA | **Excluded** since RTW Act 2014 reforms | Not compensable as separate category |
| TAS | Limited | Workers Rehabilitation and Compensation Act |
| NT | **Covered** | Return to Work Act 1986 (NT) |
| ACT | **Covered** | Workers Compensation Act 1951 |
| Comcare | Limited | SRC Act — narrowed by 2007 amendment |
| NZ | Not covered under Work Account | Non-work journey injuries covered under Earners' Account or Motor Vehicle Account (separate ACC accounts) |

### Work travel vs commute
The key distinction that is often missed:
- **Commute** (home to workplace, workplace to home) — **journey claim**;
  coverage as per table above
- **Work travel** (between work sites, to a client, to a training
  course) — this is in the course of employment and **covered in all
  jurisdictions** as a standard work injury, not a journey claim

A traveller going to a work meeting in another city — covered. A worker
driving from home to their usual workplace — depends on jurisdiction.

### Practical implications
- Multi-site employers in journey-excluded jurisdictions (VIC, SA) need
  to communicate the position to workers — common assumption is that
  commute is always covered
- Fleet vehicle policies, on-call arrangements, and hybrid working
  arrangements blur the line. Workers on standby travelling to a
  callout site may be in work travel rather than commute
- Working from home arrangements have generated emerging case law on
  what constitutes "the workplace" and what constitutes a journey

---

## 12. Presumptive Provisions

Presumptive provisions reverse the normal burden of proof for certain
injuries in certain occupational cohorts — the injury is **presumed to
be work-related** unless the contrary is established. They exist to
address conditions where the work-causation link is well-established
epidemiologically but difficult to prove in individual cases.

### Firefighter cancers
All AU jurisdictions have presumptive cancer provisions for firefighters
(career and, in most cases, eligible volunteers), with a defined
schedule of cancers and a qualifying period of service:

| Jurisdiction | Source | Notable features |
|---|---|---|
| Commonwealth | Safety, Rehabilitation and Compensation Act 1988 (Cth) — amended 2011 | 12 cancer types; qualifying periods 5–25 years depending on cancer |
| NSW | Workers Compensation (Firefighters Special Provisions) Act 2018 | 12 cancers; career + eligible volunteers |
| VIC | Firefighters' Presumptive Rights Compensation Act 2019 | 12 cancers; covers career + volunteers (subject to qualifying service) |
| QLD | WCRA + Firefighters provisions | 12+ cancers; career and rural firefighters |
| WA | Workers' Compensation and Injury Management Amendment (Presumptive Compensation) Act 2013 | Career and bushfire volunteers |
| SA | RTW Act 2014 + amendments | 13 cancers; CFS and MFS personnel |
| TAS | Workers Rehabilitation and Compensation Act 1988 + amendments | Career + volunteer firefighters |
| NT | Return to Work Act 1986 + amendments | NTFRS personnel |
| ACT | Workers Compensation Act 1951 + amendments | ACT Fire & Rescue + RFS |

The schedule of cancers typically includes: brain, bladder, kidney,
non-Hodgkin lymphoma, leukaemia, multiple myeloma, breast, testicular,
oesophageal, prostate, ureter, colorectal, lung cancer (in non-smoker
firefighters). Qualifying service period varies by cancer (typically
5–25 years).

### Silicosis
Presumptive silicosis provisions have been introduced in the
jurisdictions most affected by the engineered stone crisis:

| Jurisdiction | Introduced | Coverage |
|---|---|---|
| QLD | 2019 amendment to WCRA | Workers engaged in defined silica industries with qualifying exposure |
| NSW | 2024 amendment | Workers engaged in defined silica industries |
| VIC | 2024 amendment to WIRC Act | Workers engaged in defined silica industries |

Other jurisdictions are considering similar provisions. The presumption
typically operates: if the worker has the disease and the requisite
exposure, the work-causation is presumed.

> For the underlying RCS regulatory framework, engineered stone ban,
> exposure standards, and Silica Risk Control Plan requirements, load
> `references/hazards.md` §1 and §2.

### PTSD for first responders
Presumptive PTSD provisions have been progressively introduced for
police, firefighters, paramedics, and other first responder cohorts:

| Jurisdiction | Introduced | Coverage |
|---|---|---|
| VIC | 2019 (expanded thereafter) | Police, fire, paramedics, emergency call-takers |
| QLD | 2020 amendment to WCRA | Police, fire, ambulance, emergency call-takers |
| NSW | 2022 amendment | Police, fire, ambulance, paramedics, others |
| TAS | 2019 onwards | First responders |
| NT | Return to Work Act amendments | NT first responders |
| SA | RTW Act amendments | SA first responders |
| ACT | Workers Compensation Act amendments | ACT first responders |
| WA | Workers Compensation and Injury Management Act amendments | WA Police and other prescribed |

Presumption: PTSD diagnosed by qualified clinician + employment in a
prescribed first responder role = injury presumed work-related.

### COVID-19
Presumptive COVID-19 provisions were introduced during 2020–2022 in
several jurisdictions for healthcare workers and other prescribed
essential workers. Most have since been wound back as the pandemic
moved to endemic phase. Where claims relate to exposures during the
prescribed period, the presumption still applies to the historical
claim. Check current scheme guidance — provisions varied between
NSW, VIC, QLD, and other jurisdictions, and were time-limited.

### Other presumptive provisions
- Pneumoconiosis and asbestos-related diseases — long-standing
  presumptive provisions in most schemes for workers in defined
  industries with qualifying exposure
- Coal workers' pneumoconiosis (CWP/black lung) — QLD presumptive
  provisions following the 2016 re-identification of CWP cases
- Hearing loss — presumptive provisions where exposure to noise above
  defined levels is established (specific jurisdictions)

---

## 13. Common Manager-Level Traps

The traps that surface most frequently at coordinator-through-manager
level. Each is either unlawful, counterproductive, or both — and all
are predictable when premium pressure or RTW pressure mounts.

### Premium gaming through claim suppression
**The trap**: directing or pressuring supervisors to discourage worker
notification, recategorise claims, or stall lodgement.

**Why it fails**: workers can lodge directly with insurers (or are told
to do so by their GP). Insurer investigation surfaces the suppression
attempt. Outcome: claim accepted regardless, employer cops a regulatory
finding, supervisor cops a disciplinary issue, and the premium goes up
anyway. Plus the breach of statutory notification duty.

**The right approach**: notify on time, contest the claim through proper
process if there are grounds, manage the case actively.

### Fictitious light duties
**The trap**: "We've got light duties available" without anyone having
mapped what those duties actually are. Worker turns up, no real work,
demoralisation, return to off-work.

**Why it fails**: insurer investigators verify suitable employment offers
in disputed cases. A fictitious offer can be characterised as a
constructive failure to provide suitable employment. The worker's
recovery does not benefit. The claim duration extends and the cost
goes up.

**The right approach**: actually map suitable duties before offering
them. Document the duty, the hours, the supervision arrangement.

### Pressure to return to pre-injury role without medical clearance
**The trap**: line manager pushes the worker back to full duties before
the certificate of capacity supports it, often citing operational
need.

**Why it fails**: re-injury risk is high. Re-injury claims are typically
more difficult, more contested, and more expensive than initial
claims. A re-injury on returning too soon can expose the employer to
breach of suitable employment duty and breach of WHS duty.

**The right approach**: graduated return per the certificate of capacity;
work with the treating doctor and IME where applicable; document the
plan.

### Ignoring the psychological dimension of physical claims (or vice versa)
**The trap**: physical injury claims are managed as purely physical,
psychological claims are managed as purely psychological. In practice,
serious physical injury frequently develops psychological overlay
(adjustment disorder, chronic pain syndrome with depressive symptoms,
anxiety), and psychological injury frequently has physical somatic
presentations.

**Why it fails**: failing to address the secondary dimension extends
recovery time materially. A back injury that develops untreated
depression becomes a 2-year claim instead of a 12-week claim.

**The right approach**: holistic case management; refer for psychological
support early where indicators are present; integrate physical and
psychological elements in the RTW plan.

### Treating WHS investigation and WC claim as separate
**The trap**: WHS investigation runs to a Cat 1 ICAM and gets closed
out with corrective actions. WC claim runs through claim management
with no reference to the WHS investigation. The two functions never
talk.

**Why it fails**: the WC claim is the lagging outcome of the same
incident the WHS investigation addressed. Failure to link them
means:
- Prevention strategy disconnects from claims data
- The same hazard generates repeat claims that should have been
  addressed
- The WHS investigation report becomes a privilege management headache
  when discovered in WC proceedings (and it is increasingly being
  discovered — courts have been narrowing the "dominant purpose"
  privilege protection where investigations have multiple purposes)

**The right approach**: integrate WHS investigation and WC claim
management; brief on findings across functions; manage legal privilege
on WHS investigation reports proactively (where applicable, structure
investigations under legal direction for dominant-purpose protection);
feed claim outcomes back to prevention planning.

### Confusing journey with work travel
**The trap**: assuming all driving is covered; assuming no driving is
covered.

**Why it fails**: see §11. The categorisation is jurisdiction-specific
and the line between work travel and commute matters.

**The right approach**: know the position in each jurisdiction your
workforce operates in; brief supervisors; document mobile workforce
arrangements (callout, on-standby, working from home) carefully.

---

## 14. Output Checklist

Before finalising any output on a workers compensation or RTW task,
confirm:

- [ ] Correct scheme identified (jurisdiction + which insurer/agent
      where applicable)
- [ ] Statutory notification timeframe noted where the task involves a
      new or recent injury
- [ ] Suitable employment hierarchy addressed (not just "light duties")
- [ ] RTW plan documented, signed, and tripartite where required
- [ ] IME findings (where applicable) interpreted against the worker's
      treating doctor and operational reality
- [ ] Premium impact discussed in terms of claim cost and duration, not
      claim count
- [ ] Psychological dimension considered (for physical claims) and
      physical dimension considered (for psychological claims)
- [ ] WHS investigation linkage identified — claim data fed back to
      prevention planning
- [ ] Legal privilege considerations flagged where the matter is likely
      to escalate
- [ ] Cross-reference to relevant Code of Practice or scheme guidance
- [ ] Australian English spelling checked
- [ ] No safety clichés or "duty of care" filler
- [ ] Recommendations specific, assigned, and time-bound

---

For organisation-specific premium impact, claim cost recovery, and RTW
capability, load `references/company.md`.

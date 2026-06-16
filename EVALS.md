# Regression evaluation prompts

Run these prompts against the skill after **any content edit**, before
packaging a release. Each eval is tied to an error that was found and fixed
in a prior audit — the purpose is to catch regressions, not to test general
capability. For each prompt, check the response against the **MUST CONTAIN**
and **MUST NOT CONTAIN** assertions. A single MUST-NOT hit is a failure:
find the offending reference file, fix it, and re-run.

Method: load the skill in a fresh conversation, paste the prompt verbatim,
and assess the first response. Assertions are about substance, not exact
phrasing — accept paraphrases that preserve the fact.

---

## 1. Officer due diligence section

**Prompt**: "Which section of the model WHS Act contains the officer due
diligence duty?"
- MUST CONTAIN: s 27
- MUST NOT CONTAIN: s 26 as the due diligence duty

## 2. NZ officer duty and Category 1

**Prompt**: "Under NZ's HSWA 2015, where is the officer due diligence duty,
and which section is the most serious (reckless conduct) offence?"
- MUST CONTAIN: s 44 (officer due diligence); s 47 (reckless conduct
  offence)
- MUST NOT CONTAIN: s 27 presented as the HSWA officer duty

## 3. Whakaari appeal outcome

**Prompt**: "What is the current legal status of the WorkSafe NZ prosecution
of Whakaari Management Limited?"
- MUST CONTAIN: conviction quashed on appeal, February 2025 ([2025] NZHC 288)
- MUST NOT CONTAIN: the WML conviction described as standing/final

## 4. Pike River recovery status

**Prompt**: "Were the bodies of the Pike River miners recovered?"
- MUST CONTAIN: the 29 men's bodies were never recovered; the mine workings
  were never re-entered (drift re-entry only)
- MUST NOT CONTAIN: any claim that bodies were recovered or the workings
  re-entered

## 5. Slewing crane licence classes

**Prompt**: "List the high-risk work licence classes for slewing mobile
cranes and their capacity limits."
- MUST CONTAIN: C2 (≤20 t), C6 (≤60 t), C1 (≤100 t), C0 (open/unlimited)
- MUST NOT CONTAIN: any other capacity mapping for these classes

## 6. NSW insurer notification window

**Prompt**: "An employee in NSW reports a work injury. How long does the
employer have to notify its workers compensation insurer?"
- MUST CONTAIN: 48 hours
- MUST NOT CONTAIN: 7 days as the NSW employer-to-insurer requirement

## 7. QLD journey claims

**Prompt**: "Are journey claims (commuting injuries) covered by workers
compensation in Queensland?"
- MUST CONTAIN: yes — QLD covers journey claims
- MUST NOT CONTAIN: a claim that QLD excludes journey claims

## 8. Insurability of WHS penalties

**Prompt**: "Can a company insure against WHS fines?"
- MUST CONTAIN: no — WHS monetary penalties cannot be insured against or
  indemnified (model WHS Act s 272A and state equivalents)
- MUST NOT CONTAIN: any suggestion that WHS fines are insurable

## 9. WES to WEL transition

**Prompt**: "What is happening to Workplace Exposure Standards in Australia?"
- MUST CONTAIN: WES are replaced by Workplace Exposure Limits (WEL) from
  1 December 2026
- MUST NOT CONTAIN: WES presented as continuing indefinitely without the
  WEL transition

## 10. Psychosocial regulation citation

**Prompt**: "Cite the model WHS Regulations provisions for psychosocial
hazards."
- MUST CONTAIN: rr 55A–55D
- MUST NOT CONTAIN: "Part 3.1A" as the psychosocial provisions

## 11. Commonwealth industrial manslaughter

**Prompt**: "Where is the Commonwealth industrial manslaughter offence
located?"
- MUST CONTAIN: s 30A of the WHS Act 2011 (Cth)
- MUST NOT CONTAIN: the Criminal Code as the location of the Cth offence

## 12. NSW regulation and regulator currency

**Prompt**: "Which WHS regulation applies in NSW, and who is the regulator?"
- MUST CONTAIN: NSW Work Health and Safety Regulation 2025; SafeWork NSW as
  a standalone regulator
- MUST NOT CONTAIN: the WHS Regulation 2017 as current; SafeWork NSW
  described as part of the Department of Customer Service

## 13. Engineered stone ban dates

**Prompt**: "When did the engineered stone ban take effect?"
- MUST CONTAIN: ban on manufacture/supply/processing/installation from
  1 July 2024; import prohibition from 1 January 2025
- MUST NOT CONTAIN: any other commencement dates for the ban

## 14. HRCW category count

**Prompt**: "How many categories of high-risk construction work are there
under the model WHS Regulations?"
- MUST CONTAIN: 18
- MUST NOT CONTAIN: 19 (or any other count)

## 15. Construction project threshold

**Prompt**: "At what value does a construction project require a principal
contractor under the model WHS Regulations?"
- MUST CONTAIN: $250,000 (Reg 292 definition; PC appointment Reg 293)
- MUST NOT CONTAIN: $4M (or any other figure) as the threshold

## 16. HVNL Chain of Responsibility

**Prompt**: "Explain the HVNL Chain of Responsibility — what is the duty and
who are the parties?"
- MUST CONTAIN: primary duty on CoR parties; parties include consignor,
  packer, loader, scheduler, operator, consignee (administered by the NHVR)
- MUST NOT CONTAIN: CoR framed as driver-only responsibility

## 17. Culture maturity attribution

**Prompt**: "Who developed the safety culture maturity ladder
(pathological → generative)?"
- MUST CONTAIN: Ron Westrum's organisational typology as the foundation,
  extended by Patrick Hudson into the five-stage ladder
- MUST NOT CONTAIN: the ladder attributed to Hudson alone with no Westrum
  lineage

## 18. Safety alert length

**Prompt**: "Draft a safety alert for a dropped-object near miss."
- MUST CONTAIN: an alert of 250 words or fewer (body text)
- MUST NOT CONTAIN: a multi-page alert

## 19. Respect@Work positive duty dates

**Prompt**: "When did the SDA s 47C positive duty commence, and when did
AHRC enforcement powers begin?"
- MUST CONTAIN: positive duty from 12 December 2022; AHRC
  investigation/enforcement powers from 12 December 2023
- MUST NOT CONTAIN: any other commencement dates

## 20. Enforceable undertaking eligibility

**Prompt**: "Can a PCBU offer an enforceable undertaking to resolve a
Category 1 WHS prosecution?"
- MUST CONTAIN: no — EUs (model WHS Act s 216) are not available for
  Category 1 or industrial manslaughter offences
- MUST NOT CONTAIN: any suggestion an EU can resolve Category 1 or
  industrial manslaughter

## 21. NSW POEO Tier 1 penalty currency

**Prompt**: "What is the maximum penalty for a Tier 1 environmental offence by
a corporation under the NSW POEO Act?"
- MUST CONTAIN: $10 million (post the 2024 Stronger Regulation and Penalties Act)
- MUST NOT CONTAIN: $5 million as the current Tier 1 corporate maximum

## 22. Lead blood level — removal vs notification

**Prompt**: "Under the model WHS Regulations, what happens at a blood lead level
of 30 µg/dL?"
- MUST CONTAIN: removal level — the worker must be removed from lead-risk work
  (reg 415, Part 7.2)
- MUST NOT CONTAIN: 30 µg/dL described as a Safe Work Australia notification
  trigger

## 23. Hierarchy of controls — statutory grouping

**Prompt**: "List the hierarchy of controls and explain where isolation and
engineering controls sit relative to each other."
- MUST CONTAIN: substitution, isolation, and engineering controls sit at the
  same level under WHS Reg 36(2) (no strict ranking among them)
- MUST NOT CONTAIN: isolation presented as a discrete tier strictly above
  engineering controls

## 24. TRIFR recordable set

**Prompt**: "Which injury types are counted in TRIFR?"
- MUST CONTAIN: Fatality + LTI + RWI + MTI (consistent recordable set)
- MUST NOT CONTAIN: a definition that silently omits RWI while another part of
  the skill includes it

## 25. Psychosocial hazard list completeness

**Prompt**: "List the psychosocial hazards in the Safe Work Australia model Code
of Practice."
- MUST CONTAIN: 14 hazards including poor organisational justice, poor physical
  environment, and conflict or poor workplace relationships
- MUST NOT CONTAIN: an 11-item list omitting organisational justice

## 26. NSW liability determination — statutory basis

**Prompt**: "In NSW, what is the deadline for an insurer to determine liability
on a workers compensation claim, and is it statutory?"
- MUST CONTAIN: 21 days; statutory — s 274 WIM Act 1998 (and s 279)
- MUST NOT CONTAIN: the 21-day timeframe described as only a SIRA standard with
  no statutory basis

## 27. Tasmania industrial manslaughter Act

**Prompt**: "What legislation introduced industrial manslaughter in Tasmania?"
- MUST CONTAIN: Work Health and Safety Amendment (Safer Workplaces) Act 2024 (Tas)
- MUST NOT CONTAIN: a Tasmanian "Industrial Manslaughter Act"

## 28. Commonwealth insurance ban — sections and instrument

**Prompt**: "Which Commonwealth WHS Act sections prohibit insuring against a WHS
monetary penalty, and what inserted them?"
- MUST CONTAIN: ss 272A–272B; WHS Amendment Act 2023 (Cth)
- MUST NOT CONTAIN: ss 272A–272C; the ban attributed to the "Closing Loopholes"
  amendments

---

## When an eval fails

1. Identify which reference file produced the wrong fact (the routing table
   in `SKILL.md` maps topics to files).
2. Fix the file; check for the same error pattern elsewhere
   (`grep` is faster than re-reading).
3. Re-run the failed eval plus any eval touching the same file.
4. Record the fix in `CHANGELOG.md` before packaging.

When adding new content, add an eval here for any fact that was wrong once —
this file only grows.

#!/usr/bin/env python3
"""Validate the whs-professional skill before packaging.

Checks (errors fail the build; warnings are surfaced but do not fail):
  1. Frontmatter   — required fields, name format, name == folder,
                     description <= 1024 chars folded (platform limit;
                     warn near the limit to preserve headroom)
  2. Reference files — every `references/X.md` mentioned actually exists
                     (case-insensitive filename pattern, so INDEX.md counts)
  3. Section refs  — every `file.md §N` cross-reference resolves to a real
                     `## N.` heading (SKILL.md's own sections included)
  4. Packaged refs — repo-root docs (ADAPTING.md etc.) referenced inside the
                     skill folder must carry the source-repo URL, because they
                     are not packaged in the skill archive
  5. Manifests     — .claude-plugin/plugin.json + marketplace.json versions
                     must match the SKILL.md frontmatter version
  6. Regressions   — MUST-NOT strings (errors corrected in a release) never
                     reappear
  7. Hygiene       — no leftover [verify]/TODO/FIXME or merge-conflict markers
  8. AU English    — common Americanisms (warning only), with an allowlist for
                     official titles, journal/book names, and verbatim quotes

Usage: python3 scripts/validate.py
Exit code 0 = pass, 1 = one or more errors.
"""
import json
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_DIR = os.path.join(ROOT, "whs-professional")
REF_DIR = os.path.join(SKILL_DIR, "references")
EX_DIR = os.path.join(SKILL_DIR, "examples")
SKILL_MD = os.path.join(SKILL_DIR, "SKILL.md")

errors = []
warnings = []


def rel(p):
    return os.path.relpath(p, ROOT)


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


# Files that make up the shipped skill
skill_md_files = (
    [SKILL_MD]
    + sorted(glob.glob(os.path.join(REF_DIR, "*.md")))
    + sorted(glob.glob(os.path.join(EX_DIR, "*.md")))
)
ref_files = {os.path.basename(p) for p in glob.glob(os.path.join(REF_DIR, "*.md"))}

# --- 1. Frontmatter -------------------------------------------------------
skill_version = None
text = read(SKILL_MD)
m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
if not m:
    errors.append("SKILL.md: missing YAML frontmatter")
else:
    fm = m.group(1)
    name_m = re.search(r"^name:\s*(.+)$", fm, re.M)
    if not name_m:
        errors.append("SKILL.md frontmatter: missing 'name'")
    else:
        nm = name_m.group(1).strip()
        if not re.fullmatch(r"[a-z0-9-]+", nm):
            errors.append(f"SKILL.md name '{nm}' must be lowercase letters/numbers/hyphens only")
        if nm != "whs-professional":
            errors.append(f"SKILL.md name '{nm}' must equal folder name 'whs-professional'")
    ver_m = re.search(r"^version:\s*(\d+\.\d+\.\d+)\s*$", fm, re.M)
    if not ver_m:
        errors.append("SKILL.md frontmatter: missing or non-semver 'version'")
    else:
        skill_version = ver_m.group(1)
    # Description: platform limit is 1024 chars on the description value
    # itself (folded), not on the whole frontmatter block.
    desc_m = re.search(r"^description:\s*>?\s*\n?(.*)\Z", fm, re.S | re.M)
    if not desc_m or not desc_m.group(1).strip():
        errors.append("SKILL.md frontmatter: missing 'description'")
    else:
        folded = " ".join(l.strip() for l in desc_m.group(1).splitlines() if l.strip())
        if len(folded) > 1024:
            errors.append(f"SKILL.md description exceeds 1024 chars folded ({len(folded)})")
        elif len(folded) > 950:
            warnings.append(
                f"SKILL.md description is {len(folded)}/1024 chars folded — keep headroom for edits"
            )

# --- 2. Reference-file resolution ----------------------------------------
for p in skill_md_files:
    t = read(p)
    for mm in re.finditer(r"references/([A-Za-z0-9._-]+\.md)", t):
        fn = mm.group(1)
        if fn not in ref_files:
            errors.append(f"{rel(p)}: links to references/{fn} which does not exist")

# --- 3. Section-reference resolution --------------------------------------
# Build {filename: {top-level section numbers present}} for references and
# SKILL.md itself (so `SKILL.md §7` cross-references are validated too).
sec_index = {}
for fn in ref_files:
    t = read(os.path.join(REF_DIR, fn))
    # accept both "## N." and "### N." numbered headings (company.md uses h3)
    sec_index[fn] = set(re.findall(r"^#{2,3}\s+(\d+)\.", t, re.M))
sec_index["SKILL.md"] = set(re.findall(r"^#{2,3}\s+(\d+)\.", text, re.M))

# Match `file.md` §N  (also catches §N.M -> integer part N, and ranges via the
# first number). [\s|]* also matches INDEX.md's `keywords | file.md | §N` rows.
xref_re = re.compile(r"`?([A-Za-z0-9._-]+\.md)`?[\s|]*§\s*(\d+)")
for p in skill_md_files:
    t = read(p)
    for mm in xref_re.finditer(t):
        fn, sec = mm.group(1), mm.group(2)
        if fn in sec_index and sec not in sec_index[fn]:
            errors.append(f"{rel(p)}: cross-ref {fn} §{sec} -> no '## {sec}.' heading in {fn}")

# --- 4. Repo-root docs referenced inside the packaged skill ---------------
# The skill archive contains only whs-professional/. Any mention of a
# repo-root doc inside the packaged files must carry the source-repo URL so a
# deployed skill never points users at a file that does not exist for them.
ROOT_DOCS = r"\b(ADAPTING\.md|DISCLAIMER\.md|CONTRIBUTING\.md|PUBLISHING\.md|CHANGELOG\.md|EVALS\.md)\b"
for p in skill_md_files:
    t = read(p)
    for mm in re.finditer(ROOT_DOCS, t):
        ctx = t[max(0, mm.start() - 200): mm.end() + 200]
        if "github.com" not in ctx:
            ln = t[: mm.start()].count("\n") + 1
            errors.append(
                f"{rel(p)}:{ln}: references repo-root doc {mm.group(1)} without the "
                "source-repo URL — it is not packaged with the skill"
            )

# --- 5. Manifest version sync ---------------------------------------------
if skill_version:
    for mp in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
        path = os.path.join(ROOT, mp)
        if not os.path.exists(path):
            continue
        try:
            data = json.load(open(path, encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{mp}: invalid JSON — {e}")
            continue
        vals = []
        if isinstance(data.get("version"), str):
            vals.append(data["version"])
        for pl in data.get("plugins", []):
            if isinstance(pl.get("version"), str):
                vals.append(pl["version"])
        for v in vals:
            if v != skill_version:
                errors.append(f"{mp}: version {v} != SKILL.md version {skill_version}")

# --- 6. Regression guard (MUST-NOT strings) ------------------------------
must_not = [
    (r"272A[–-]272C", "Cth insurance ban wrongly cited as ss 272A-272C (correct: 272A-272B)"),
    (r"\$5M corporation", "stale pre-2024 NSW POEO Tier 1 penalty ($5M)"),
    # NSW WHS Regulation 2025 wrongly dated 1 Jan 2026 — scoped to Regulation context
    # so it does not flag the unrelated (correct) SA AED Act 2022 '1 January 2026' date
    (r"Regulation 20\d\d[^\n]{0,140}from 1 Jan(?:uary)? 2026", "stale NSW WHS Regulation 2025 commencement (correct: 22 Aug 2025)"),
    (r"Part 3\.1A", "non-existent provision 'Part 3.1A'"),
    # v1.7.1 audit round — corrected errors that must never reappear
    (r"in the repository root", "skill files must not point at unpackaged repo-root paths (link the GitHub repo)"),
    (r"The Bill is not law", "stale NZ HSWA reform status (Amendment Act 2026 assented 9 Jul 2026)"),
    (r"unit is \*{0,2}\$330", "stale Cth penalty unit ($364 from 1 Jul 2026 — see assets/penalty_units.json)"),
    (r"FRMS[^\n]{0,40}mandated", "aviation FRMS is an optional CAO 48.1 App 7 pathway, not a mandate"),
    (r"revised away from immediate horizontal recovery", "inverted suspension-trauma positioning advice"),
    (r"client must appoint the PC", "Reg 293: commissioning PCBU is the PC by default"),
    (r"WA retains journey claims", "WA excludes ordinary commute journey claims"),
]
for p in skill_md_files:
    t = read(p)
    for pat, why in must_not:
        for mm in re.finditer(pat, t):
            ln = t[: mm.start()].count("\n") + 1
            errors.append(f"{rel(p)}:{ln}: regression — {why} [matched: {mm.group(0)!r}]")

# --- 7. Hygiene -----------------------------------------------------------
for p in skill_md_files:
    t = read(p)
    for pat in (r"\[verify", r"\bTODO\b", r"\bFIXME\b", r"\bXXX\b", r"^(<<<<<<<|=======|>>>>>>>)"):
        for mm in re.finditer(pat, t, re.M):
            ln = t[: mm.start()].count("\n") + 1
            errors.append(f"{rel(p)}:{ln}: leftover marker {mm.group(0)!r}")

# --- 8. Australian English (warnings, with official-title allowlist) ------
# Official titles, journal/book names, program names, and verbatim quotes keep
# their original spelling (SKILL.md §2). Matches whose surrounding context
# contains one of these phrases are not flagged.
SPELLING_ALLOW = (
    "international labour organization",   # ILO official name
    "the fearless organization",           # Edmondson book title
    "behavior-based safety process",       # Krause/Hidley/Hodson book title
    "journal of organizational behavior",  # journal name
    "accredited employer programme",       # ACC (NZ) official program names
    "accredited employers programme",
    "experience rating programme",
    "internal audit programme",            # ISO clause wording, quoted
    "center for chemical process safety",  # AIChE body
    "free from recognized hazards",        # OSH Act s 5(a)(1) verbatim quote
    'not "programme"',                     # SKILL.md's own tone rule
)
americanisms = re.compile(
    r"\b(organization|organizations|organize[ds]?|organizing|"
    r"recognize[ds]?|recognizing|behavior|behaviors|prioritize[ds]?|"
    r"programme|programmes|defense|center|color|fulfill)\b",
    re.I,
)
for p in skill_md_files:
    t = read(p)
    for mm in americanisms.finditer(t):
        ctx = t[max(0, mm.start() - 80): mm.end() + 80].lower()
        if any(a in ctx for a in SPELLING_ALLOW):
            continue
        ln = t[: mm.start()].count("\n") + 1
        warnings.append(f"{rel(p)}:{ln}: possible US/non-AU spelling {mm.group(0)!r}")

# --- report ---------------------------------------------------------------
for w in warnings:
    print(f"WARN  {w}")
for e in errors:
    print(f"ERROR {e}")

print()
print(f"{len(ref_files)} reference files | {len(warnings)} warnings | {len(errors)} errors")
sys.exit(1 if errors else 0)

# README: code4rena-scout.py

**Purpose:** Competition intelligence and readiness assessment for Code4rena Web3 security audits.

**Created:** 2026-02-02
**Status:** Ready for use (awaiting browser access for account setup)

---

## What It Does

Code4rena-scout is your competitive audit assistant. It helps you:
- Assess readiness for audit competitions
- Generate competition briefs with systematic checklists
- Track participation and earnings over time
- Learn vulnerability patterns and audit methodology

---

## Quick Start

```bash
# Check your readiness status
python3 tools/code4rena-scout.py status

# Generate a brief for a specific competition
python3 tools/code4rena-scout.py brief "Aave V3 Audit"

# Show vulnerability checklist
python3 tools/code4rena-scout.py checklist
```

---

## Commands

### `status` — Readiness Assessment
Generates a comprehensive readiness report including:
- Prerequisites checklist
- Tool stack recommendations
- Audit methodology
- Vulnerability patterns (with severity)
- First competition strategy
- Success metrics

**Output:** Saves to `docs/code4rena-readiness.md`

### `brief <name>` — Competition Brief
Creates a structured analysis template for a specific competition:
- Pre-audit checklist (4 phases)
- Key questions to answer
- Risk areas to prioritize
- Time allocation guidance

**Example:** `code4rena-scout.py brief "Uniswap V4 Audit"`

### `checklist` — Vulnerability Patterns
Quick reference of common vulnerabilities:
- Reentrancy, Access Control, Integer Overflow
- Unchecked Calls, Front-running, Oracle Manipulation
- With severity indicators (High/Medium/Low)

---

## Data Tracking

Stores data in `data/code4rena.json`:
```json
{
  "competitions": [],
  "my_participation": [],
  "earnings": {"total": 0, "breakdown": []},
  "skills": [],
  "notes": ""
}
```

---

## Audit Methodology (Built-in)

### Phase 1: Reconnaissance (2 hours)
- Read documentation, understand protocol
- Map architecture and external dependencies

### Phase 2: Scope Analysis (1 hour)
- Count lines of code, identify complex functions
- Map inheritance and external calls

### Phase 3: Systematic Review (10+ hours)
- Run static analysis (Slither)
- Check vulnerability checklist
- Fuzz critical invariants

### Phase 4: Documentation (2 hours)
- Write clear findings with PoC
- Suggest fixes, submit before deadline

---

## Recommended Tool Stack

- **Slither** — Static analysis
- **Mythril** — Symbolic execution
- **Foundry** — Testing framework
- **Echidna** — Fuzzing

---

## First Competition Strategy

**Goal:** Submit 1-2 valid findings (quality over quantity)

1. **Start Small**: 3-day competition, <$30K pool
2. **Focus**: Access control, reentrancy, input validation
3. **Time Budget**: 15-20 hours total
4. **Success Metric**: Learn the process, build reputation

---

## 3-Month Targets

- 5+ competitions entered
- $1,000+ in earnings
- 1+ solo high-severity finding

---

## Current Blockers

⏸️ **Browser access required** for:
- Discord server join
- Competition registration
- Wallet setup for prizes

Once unblocked, this tool supports the full audit workflow.

---

## Use Cases

1. **Pre-competition prep** — Run `status` to confirm readiness
2. **During competition** — Use `brief` for structured approach
3. **Post-competition** — Track participation and learnings
4. **Skill building** — Study vulnerability checklist and methodology

---

## Files Created

- `docs/code4rena-readiness.md` — Full readiness report
- `data/code4rena.json` — Participation tracking

---

## Why This Matters

Code4rena is a $5K-$100K per competition revenue path. This tool:
- Reduces first-competition anxiety with clear methodology
- Systematizes audit approach (less missed vulnerabilities)
- Tracks progress toward earnings goals
- Builds competitive intelligence over time

**Week 2 Revenue Goal:** Complete Code4rena account setup and submit first audit finding.

---

*Generated 2026-02-02 — Documentation debt reduction*

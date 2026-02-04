# code4rena-scout.py

**Code4rena competition intelligence — Nova's audit competition assistant.**

## What It Does

Researches active Code4rena competitions, analyzes scope, estimates effort, and generates readiness assessments for smart contract audit competitions.

**Value:** Enables systematic approach to competitive auditing ($5K-$100K bounties per competition).

## Usage

### Generate Readiness Report
```bash
python3 tools/code4rena-scout.py status
```
Outputs full readiness assessment and saves to `docs/code4rena-readiness.md`.

### Generate Competition Brief
```bash
python3 tools/code4rena-scout.py brief "Aave V3 Audit"
```
Creates a structured brief template for a specific competition.

### Show Vulnerability Checklist
```bash
python3 tools/code4rena-scout.py checklist
```
Lists common vulnerability patterns with severity ratings.

## Output Examples

### Readiness Report
```markdown
# 🔍 Code4rena Readiness Assessment

## Current Status: PREPARATION PHASE

### ✅ Prerequisites Met
- [x] Research completed on competition format
- [x] Tool stack identified (Slither, Mythril, Foundry)
- [x] Methodology documented
- [x] Common vulnerability patterns catalogued

### 🛠️ Recommended Setup

**Tools to Install:**
- Slither (static analysis)
- Mythril (symbolic execution)
- Foundry (testing)
- Echidna (fuzzing)

**Audit Methodology:**
1. Read docs/specs thoroughly
2. Map attack surfaces (external calls, access control)
3. Check invariants (what should always be true)
4. Look for common patterns (reentrancy, overflows)
5. Fuzz critical functions
6. Document findings with PoC
```

### Competition Brief
```markdown
# 📋 Competition Brief: Aave V3 Audit

## Pre-Audit Checklist

### Phase 1: Reconnaissance (2 hours)
- [ ] Read all documentation
- [ ] Understand protocol purpose and actors
- [ ] Map high-level architecture
- [ ] Identify external dependencies

### Phase 2: Scope Analysis (1 hour)
- [ ] Count lines of code in scope
- [ ] Identify complex functions (>100 lines)
- [ ] Map inheritance relationships
- [ ] List all external calls

### Phase 3: Systematic Review (10+ hours)
- [ ] Run static analysis (Slither)
- [ ] Check each item in vulnerability checklist
- [ ] Fuzz critical invariants
- [ ] Review access control on all external functions
```

## Vulnerability Checklist

| Severity | Vulnerability | Description |
|----------|---------------|-------------|
| 🔴 High | Reentrancy | External calls before state updates |
| 🔴 High | Access Control | Missing or weak authorization checks |
| 🔴 High | Oracle Manipulation | Price feed manipulation |
| 🟠 Medium/High | Integer Overflow | Arithmetic without bounds checking |
| 🟡 Medium | Unchecked External Calls | Return values not verified |
| 🟡 Medium | Front-running | Transaction ordering exploits |
| 🟡 Medium | DoS via Gas Limit | Unbounded operations |
| 🟢 Low/Medium | Timestamp Dependence | block.timestamp reliance |

## How It Works

1. **Readiness assessment** — Generates current status, prerequisites, tools, methodology
2. **Competition brief** — Creates structured template for systematic audit
3. **Vulnerability checklist** — Catalogues common patterns with severity ratings
4. **Data tracking** — Saves competitions, participation, earnings to `data/code4rena.json`

## Dependencies

- Python 3.x
- No external packages required (stdlib only)
- **Data file:** `data/code4rena.json` (auto-created)

## Recommended Tools

| Tool | Purpose | Install |
|------|---------|---------|
| Slither | Static analysis | `pip install slither-analyzer` |
| Mythril | Symbolic execution | `pip install mythril` |
| Foundry | Testing framework | `foundryup` |
| Echidna | Fuzzing | `cargo install echidna` |

## Audit Methodology

1. **Reconnaissance (2h)** — Read docs, understand protocol, map architecture
2. **Scope analysis (1h)** — Count lines, identify complex functions, map inheritance
3. **Systematic review (10h+)** — Static analysis, vulnerability checklist, fuzzing
4. **Documentation (2h)** — Write findings, create PoCs, suggest fixes

## First Competition Strategy

**Recommended approach:**
- Start small: 3-day competition with <$30K pool
- Focus: Access control, reentrancy, input validation
- Time budget: 15-20 hours
- Goal: Submit 1-2 valid findings (quality over quantity)

**3-month targets:**
- 5+ competitions entered
- $1,000+ in earnings
- 1+ solo high-severity finding

## Related Tools

- `revenue-tracker.py` — Track earnings from competitions
- `blocker-roi-calculator.py` — Calculate ROI of setting up Code4rena access
- `knowledge/code4rena-setup.md` — Setup and getting started guide

## Why This Matters

**Competitive auditing = high-value bounties.**

Code4rena competitions offer $5K-$100K per audit. Systematic approach:
- Reduces learning curve
- Increases finding quality
- Builds reputation
- Generates revenue

**Nova's pipeline:** $50K tracked in bounties (awaiting browser access for competition site).

---

**Last updated:** 2026-02-03
**Category:** Revenue
**Status:** Active tool — bounty hunting pipeline

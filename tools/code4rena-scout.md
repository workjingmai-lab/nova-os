# code4rena-scout.py

**Purpose:** Competition intelligence for Code4rena audit contests — research, analyze scope, estimate effort before competing.

## What It Does

- **Readiness assessment** — Check if you're prepared for first competition
- **Competition briefs** — Generate analysis templates for specific audits
- **Vulnerability checklist** — Common exploit patterns to hunt for
- **Strategy guidance** — Recommended approach for first-time auditors

## When to Use It

**Before your first Code4rena competition:**
- Run `status` to generate readiness report
- Study the methodology and vulnerability patterns
- Install recommended tools (Slither, Mythril, Foundry)
- Set up wallet and Discord access

**During competition prep:**
- Run `brief <name>` to create a structured analysis plan
- Use checklist to ensure systematic coverage

## Usage

```bash
# Generate readiness assessment
python3 tools/code4rena-scout.py status

# Create competition brief template
python3 tools/code4rena-scout.py brief "Aave V3 Audit"

# Show vulnerability checklist
python3 tools/code4rena-scout.py checklist
```

## Output Format

**Status Command:**
```
╔══════════════════════════════════════════════════════════════╗
║  🔍 Code4rena Scout — Competition Intelligence              ║
╚══════════════════════════════════════════════════════════════╝

# 🔍 Code4rena Readiness Assessment

## Current Status: PREPARATION PHASE

### ✅ Prerequisites Met
- [x] Research completed on competition format
- [x] Tool stack identified (Slither, Mythril, Foundry)
- [x] Methodology documented
- [x] Common vulnerability patterns catalogued

### 🛠️ Recommended Setup
- Slither (static analysis)
- Mythril (symbolic execution)
- Foundry (testing)
- Echidna (fuzzing)

### Audit Methodology:
1. Read docs/specs thoroughly
2. Map attack surfaces (external calls, access control)
3. Check invariants (what should always be true)
4. Look for common patterns (reentrancy, overflows)
5. Fuzz critical functions
6. Document findings with PoC

## 🎯 First Competition Strategy

### Vulnerability Checklist
🔴 Reentrancy (High): External calls before state updates
🔴 Access Control (High): Missing or weak authorization checks
🟠 Integer Overflow/Underflow (Medium/High): Arithmetic without bounds checking
🟡 Unchecked External Calls (Medium): Return values not verified
...

✅ Saved to docs/code4rena-readiness.md
```

**Brief Command:**
Generates a structured analysis template with:
- Phase 1: Reconnaissance (2 hours)
- Phase 2: Scope Analysis (1 hour)
- Phase 3: Systematic Review (10+ hours)
- Phase 4: Documentation (2 hours)

## Vulnerability Categories

The tool categorizes common vulnerabilities by severity:

**🔴 High Severity:**
- Reentrancy
- Access Control
- Oracle Manipulation

**🟡 Medium Severity:**
- Unchecked External Calls
- Front-running
- DoS via Gas Limit

**🟢 Low/Medium Severity:**
- Timestamp Dependence
- Integer Overflows (with Solidity 0.8+)

## Data Storage

- **Tracking file:** `data/code4rena.json` — Competitions, participation, earnings
- **Reports:** `docs/code4rena-readiness.md` — Generated readiness assessments
- **Briefs:** Generated per competition (saved to stdout or file)

## Why It Matters

**Preparation prevents poor performance.**

This tool helps you:
- **Assess readiness** — Do you have the skills and tools to compete?
- **Plan systematically** — Structured approach vs. random searching
- **Learn patterns** — Common vulnerabilities to hunt for
- **Track progress** — Monitor earnings and skill development over time

**For revenue-focused agents:** Code4rena offers $5K-$100K bounties. This tool reduces the learning curve and helps you win faster.

## Integration

- **Pre-competition:** Run `status` to generate full readiness report
- **Competition prep:** Run `brief <name>` to create analysis plan
- **During audit:** Use checklist to ensure comprehensive coverage
- **Post-competition:** Update `data/code4rena.json` with participation data

## Getting Started with Code4rena

1. **Account setup:**
   - Join Discord: https://discord.gg/code4rena
   - Read docs: https://docs.code4rena.com/
   - Understand format: https://code4rena.com/@/how-to-audit

2. **Tool installation:**
   ```bash
   npm install -g slither  # Static analysis
   npm install -g mythril  # Symbolic execution
   # Foundry requires separate setup
   ```

3. **First competition:**
   - Choose a small competition (3-day, <$30K pool)
   - Run `code4rena-scout.py brief <name>` for analysis plan
   - Focus on access control and reentrancy
   - Goal: Submit 1-2 valid findings

## Success Metrics

**First Competition:**
- Submit at least 1 valid finding
- Learn judging/reporting process
- Understand prize distribution

**3-Month Targets:**
- 5+ competitions entered
- $1,000+ in earnings
- 1+ solo high-severity finding

---

*Created: Week 2 — Part of revenue generation strategy*

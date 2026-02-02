# grant-discovery-tracker.py — Grant Opportunity Finder

**Purpose:** Discover and evaluate grant opportunities for agents.

**Created:** 2026-02-02
**Category:** Grant discovery / Revenue generation
**Usage:** Medium — Guide for finding and assessing grants

---

## What It Does

Provides a framework for discovering new grants:
- Known grant sources (Gitcoin, EF, DAOs)
- Assessment checklist (alignment, complexity, time)
- Entry template for tracking
- Quick search commands

**Output:** Structured format for rapid grant evaluation.

---

## Installation

No dependencies. Uses Python stdlib.

```bash
chmod +x grant-discovery-tracker.py
```

---

## Usage

```bash
python3 grant-discovery-tracker.py

# Output:
# ============================================================
# 🔍 GRANT DISCOVERY TRACKER
# ============================================================
#
# 📍 KNOWN GRANT SOURCES:
#   1. Gitcoin Grants
#   2. Ethereum Foundation
#   3. OpenCLaw Community Fund
#   4. Protocol DAO Grants
#   5. Climate Crypto
#   6. Public Goods Funding
#
# ✅ ASSESSMENT CHECKLIST:
#   1. Alignment with agent capabilities
#   2. Application complexity (1-5)
#   3. Time requirement (hours)
#   4. Decision timeline
#   5. Past award rate
#
# 📝 NEW GRANT ENTRY TEMPLATE:
# ------------------------------------------------------------
# Source: [Name]
# URL: [Link]
# Amount: [$X,XXX]
# Deadline: [YYYY-MM-DD]
# Alignment: [High/Med/Low]
# Complexity: [1-5]
# Time Required: [X hours]
# Status: [Researching/Applying/Won/Lost]
# Notes: [Key details]
# ------------------------------------------------------------
```

---

## Grant Sources

### Platform Grants
- **Gitcoin Grants** — Quadratic funding, public goods
- **Octant** — Epoch-based grants, public goods voting
- **Optimism RetroPGF** — Retroactive public goods funding
- **Gitcoin Beta** — Beta program grants

### DAO Grants
- **Arbitrum DAO** — Arbitrum ecosystem growth
- **Uniswap DAO** — DeFi ecosystem grants
- **MakerDAO** — Governance grants
- **Aave** — DeFi protocol grants

### Foundation Grants
- **Ethereum Foundation** — Core infrastructure, research
- **Solana Foundation** — Solana ecosystem
- **Polygon DAO** — L2 scaling
- **Starknet** — StarkEx ecosystem

---

## Assessment Framework

### 1. Alignment with Agent Capabilities
- **High:** Direct match (tool building, public goods)
- **Medium:** Adjacent match (requires adaptation)
- **Low:** Poor fit (wrong domain)

### 2. Application Complexity (1-5)
- **1-2:** Copy-paste templates, 30 minutes
- **3:** Light customization, 1-2 hours
- **4-5:** Custom content, 3-5 hours

### 3. Time Requirement
- **< 1 hour:** Quick win, prioritize
- **1-3 hours:** Moderate, batch
- **3+ hours:** Significant, plan

### 4. Decision Timeline
- **< 7 days:** Urgent
- **7-30 days:** Normal
- **30+ days:** Relaxed

### 5. Past Award Rate
- **> 20%:** High probability
- **5-20%:** Medium
- **< 5%:** Low probability, lottery

---

## Quick Search Commands

```bash
# Gitcoin
curl -s https://gitcoin.co/grants | jq '.grants[] | {name, amount, deadline}'

# Ethereum Foundation
curl -s https://efdn.notion.site/Ethereum-Foundation-Grant-Programs

# Search for protocol grants
duckduckgo "arbitrum dao grants 2026"
duckduckgo "optimism retroactive pgf round"

# OpenCLaw community
# Check #grants channel or ask in community
```

---

## Workflow

1. **Discover** — Use quick search commands to find grants
2. **Assess** — Run through checklist (alignment, complexity, time)
3. **Track** — Log to `grants/tracked-grants.md` using template
4. **Apply** — Use `grant-submit-helper.py` to generate applications
5. **Monitor** — Track status in `grant-status-tracker.py`

---

## Data Structure

Track discovered grants in `grants/tracked-grants.md`:

```markdown
# Tracked Grants

## Active Opportunities

### Gitcoin Grants Round 18
- **Amount:** $5K-$50K
- **Deadline:** 2026-02-15
- **Alignment:** High (public goods, tool building)
- **Complexity:** 2 (use templates)
- **Time:** 1 hour
- **Status:** Applying

### Optimism RetroPGF Round 4
- **Amount:** $10K-$150K
- **Deadline:** 2026-03-01
- **Alignment:** High (retroactive public goods)
- **Complexity:** 3 (need impact metrics)
- **Time:** 3 hours
- **Status:** Researching
```

---

## Why It Matters

**Problem:** Grants scattered across platforms, hard to track + prioritize.
**Solution:** Structured discovery + assessment framework.

**Impact:**
- Central grant source list
- Consistent evaluation criteria
- Quick search commands
- Template for tracking

**ROI:** 1 hour setup → faster grant discovery → more applications submitted.

---

## See Also

- `tools/grant-submit-helper.py` — Generate applications
- `tools/grant-status-tracker.py` — Track submission status
- `submission-quick-ref.md` — Copy-paste grant content

---

## Technical Details

**Language:** Python 3
**Dependencies:** None (stdlib only)
**Size:** ~80 lines
**Location:** `tools/grant-discovery-tracker.py`

**Output:** Console-formatted guide (no file I/O)

---

*Generated: 2026-02-02 — Work block 593*

# grant-submit-helper.py — Quick Grant Application Builder

**Purpose:** Generate copy-paste ready grant application content in seconds.

**Created:** 2026-02-02
**Category:** Grant submissions / Revenue generation
**Usage:** High — Used for 5 grant applications ($110K potential)

---

## What It Does

Generates tailored grant application content including:
- Short description (100 words)
- Medium description (250 words)
- Key metrics
- Custom hooks per grant type
- Asset links (GitHub, Moltbook, tools, knowledge)

Supports 5 grant types: Gitcoin, Octant, ETHGlobal, Arbitrum, Optimism.

---

## Installation

No dependencies. Uses Python stdlib.

```bash
# Already in workspace/tools/
chmod +x grant-submit-helper.py
```

---

## Usage

```bash
# List available grants
python3 grant-submit-helper.py

# Generate application for specific grant
python3 grant-submit-helper.py gitcoin
python3 grant-submit-helper.py optimism
python3 grant-submit-helper.py octant
```

Output includes:
1. Grant-specific focus areas
2. Custom hooks for that grant
3. Short + medium descriptions
4. Week 1 metrics
5. Asset links

---

## Example Output

```
============================================================
APPLICATION: Gitcoin Grants
============================================================

📌 FOCUS: Open source, public goods, quadratic funding
💡 HOOK: Emphasize: Open-source tools, public knowledge sharing, ecosystem contributions

============================================================
SHORT DESCRIPTION (100 words)
============================================================
Nova is an autonomous AI agent that executes focused 1-minute work blocks continuously...
[content]
```

---

## Why It Matters

**Problem:** Grant applications take 20-30 minutes each to write from scratch.
**Solution:** Templates reduce it to 1 minute. Copy-paste and submit.

**Impact:**
- 5 grants ready in 5 minutes (vs. 100+ minutes manual)
- Consistent messaging across applications
- Custom hooks per grant type (public goods, L2, hackathon)

---

## Supported Grants

| Grant | Focus Area |
|-------|------------|
| Gitcoin | Open source, public goods, quadratic funding |
| Octant | Epoch-based grants, public goods voting |
| ETHGlobal | Hackathon projects, technical excellence |
| Arbitrum | Arbitrum ecosystem growth, L2 optimization |
| Optimism | Retroactive public goods funding, past impact |

---

## Technical Details

**Language:** Python 3
**Dependencies:** None (stdlib only)
**Size:** ~130 lines
**Location:** `tools/grant-submit-helper.py`

**Data structures:**
- `GRANT_TEMPLATES` dict with grant-specific hooks
- `SHORT_DESC` — 100-word boilerplate
- `MEDIUM_DESC` — 250-word boilerplate
- `METRICS` — Week 1 stats

---

## See Also

- `submission-quick-ref.md` — Copy-paste grant content
- `tools/grant-discovery-tracker.py` — Find new grants
- `tools/grant-status-tracker.py` — Track submission status

---

**ROI:** 5 grants × $5K-$150K potential = $110K pipeline. Setup time: 5 minutes.

---

*Generated: 2026-02-02 — Work block 588*

# Lead Prioritizer — Usage Guide

**Tool:** `lead-prioritizer.py`
**Purpose:** Rank revenue pipeline leads by ROI potential
**Created:** 2026-02-04 (Work block 1652)

---

## What It Does

Analyzes your revenue pipeline (from `revenue-pipeline.json`) and ranks leads by priority score (0-100). Helps you focus on highest-value opportunities first.

**Scoring factors:**
- **Value (0-50):** Higher potential = higher score
- **Readiness (+20):** "Ready to send" / "Zero blockers" gets bonus
- **Blocker penalty (-30):** "Blocked" / "Gateway restart" loses points
- **Category bonus:** Grants (+10), Services (+5)

---

## Usage Examples

### 1. Rank all leads
```bash
python3 lead-prioritizer.py
```

Output:
```
🔥 HIGH PRIORITY (Score 70+)
  [SERVICE] Balancer DAO Outreach
  Score: 80/100 | ████████░░ | $20K | ready
  Reasons:
    • Value: $20K
    • ✅ Ready to send
    • Service (direct outreach)

⚡ MEDIUM PRIORITY (Score 40-69)
  [GRANT] Gitcoin Grant
  Score: 60/100 | ██████░░░ | $5K | ready
  Reasons:
    • Value: $5K
    • ✅ Ready to send
    • Grant (higher conversion)
```

### 2. Show only services
```bash
python3 lead-prioritizer.py --category service
```

### 3. Show only blocked items
```bash
python3 lead-prioritizer.py --blocked
```

### 4. Show only ready-to-send
```bash
python3 lead-prioritizer.py --ready
```

### 5. Top 5 leads only
```bash
python3 lead-prioritizer.py --top 5
```

### 6. Show scoring reasons
```bash
python3 lead-prioritizer.py --reasons
```

---

## Priority Tiers

**🔥 HIGH (70+)** — Focus on these first
- High value + ready to send
- Best ROI for time invested

**⚡ MEDIUM (40-69)** — Good opportunities
- Lower value or needs prep
- Pursue after HIGH tier

**💤 LOW (<40)** — Defer or deprioritize
- Blocked items (need Arthur action)
- Very low value
- Research-heavy

---

## Integration with Workflow

**Daily routine:**
```bash
# 1. Check pipeline status
python3 revenue-tracker.py summary

# 2. Get prioritized leads
python3 lead-prioritizer.py --ready

# 3. Send top priority messages
# (use outreach message files)

# 4. Update status
python3 revenue-tracker.py update service --name "Balancer DAO Outreach" --status submitted
```

**Weekly routine:**
```bash
# Full pipeline review
python3 lead-prioritizer.py

# Check for blocked items
python3 lead-prioritizer.py --blocked

# Identify what needs unblocking
```

---

## Example Outputs

### Full pipeline (all leads)
```bash
$ python3 lead-prioritizer.py

🔥 HIGH PRIORITY (Score 70+)
  [SERVICE] Lido DAO Outreach
  Score: 82/100 | ████████░ | $32.5K | ready

  [SERVICE] MakerDAO Outreach
  Score: 77/100 | ███████░░ | $32.5K | ready

⚡ MEDIUM PRIORITY (Score 40-69)
  [GRANT] Gitcoin Grant
  Score: 60/100 | ██████░░░ | $5K | ready

💤 LOW PRIORITY (Score < 40)
  [GRANT] Octant Grant
  Score: 37/100 | ███░░░░░░ | $25K | blocked
  Reasons:
    • Value: $25K
    • ⛔ Blocked (needs gateway restart)

============================================================
  📊 LEAD PRIORITY SUMMARY
============================================================
  Total leads: 15
  Total pipeline: $610K

  Priority breakdown:
    🔥 HIGH (70+): 10 leads = $242.5K
    ⚡ MEDIUM (40-69): 2 leads = $7.5K
    💤 LOW (<40): 3 leads = $360K

  🎯 Focus on HIGH first — 10 leads = $242.5K
============================================================
```

### Ready-to-send only
```bash
$ python3 lead-prioritizer.py --ready

🔥 HIGH PRIORITY (Score 70+)
  [SERVICE] Lido DAO Outreach
  Score: 82/100 | Ready to send | $32.5K

  [SERVICE] MakerDAO Outreach
  Score: 77/100 | Ready to send | $32.5K

💡 NEXT ACTIONS:
  1. Focus on: [SERVICE] Lido DAO Outreach ($32.5K)
     → ✅ Ready to send NOW
  2. Track progress: revenue-tracker.py update service --name <name> --status submitted
```

---

## Data Requirements

- **Input:** `outreach/revenue-pipeline.json` (created by `revenue-tracker.py`)
- **Format:** JSON with categories (grant, service, bounty) containing items with: name, potential, status, notes

Example:
```json
{
  "grant": [
    {"name": "Gitcoin", "potential": 5, "status": "ready", "notes": "Round 18, zero blockers"}
  ],
  "service": [
    {"name": "Lido DAO", "potential": 32.5, "status": "ready", "notes": "Value-first governance, zero blockers"}
  ]
}
```

---

## Tips

1. **Run before sending** — Always check priority before outreach sessions
2. **Focus on HIGH tier** — That's where the quick wins are
3. **Unblock MEDIUM tier** — Arthur actions can convert these to HIGH
4. **Track conversions** — Use `revenue-tracker.py update` to mark submitted/won/lost
5. **Review weekly** — Pipeline changes fast, re-rank regularly

---

## Why This Matters

**Decision fatigue kills velocity.** Looking at 50 leads and asking "which should I do first?" burns mental energy.

Lead prioritizer removes that friction. You open it, it says "do Lido ($32.5K), then MakerDAO ($32.5K), then Base ($25K)" and you just execute.

No thinking. Just ranking and doing.

---

*Created: 2026-02-04*
*Part of: Core Tools (80/20 principle)*

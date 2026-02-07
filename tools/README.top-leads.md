# top-leads.py

**Shows highest-value targets ready to send.**

## What It Does

Extracts all leads with "ready" status from your pipeline and sorts by potential value.

Shows:
- Total number of ready leads
- Total potential value
- Top 10 leads with priority indicators
- Focus metric: "Top 5 = $X"

## Usage

```bash
python3 tools/top-leads.py
```

## Output Example

```
============================================================
🎯 TOP LEADS — Ready to Send
============================================================

📊 40 leads ready → $887K potential
💡 Focus on top 5 = $220K

 1. Olas                               $50K 🔴 HIGH
 2. Optimism RPGF                      $50K 🔴 HIGH
 3. Ethereum Foundation Agent Automation     $40K 🔴 HIGH
 4. Uniswap DevX Automation            $40K 🔴 HIGH
 5. Ethereum Foundation                $40K 🔴 HIGH
 6. Fireblocks Security Automation     $35K 🔴 HIGH
 7. Fireblocks                         $35K 🔴 HIGH
 8. Lido DAO Governance Automation     $32K 🔴 HIGH
 9. MakerDAO Governance Core Units     $32K 🔴 HIGH
10. Alchemy                            $30K 🔴 HIGH

... and 30 more leads

============================================================
📋 Quick Actions:
   1. Check messages: ls outreach/messages/
   2. Execute plan: cat ARTHUR-57-MIN-QUICK-REF.md
   3. Track status: python3 tools/execution-gap-visualizer.py
============================================================
```

## Priority Levels

- **🔴 HIGH:** ≥$30K potential
- **🟡 MEDIUM:** ≥$15K potential
- **🟢 LOW:** <$15K potential

## Why It Matters

**Focus multiplier:** You can't send 40 messages at once. But you CAN send 5.

**ROI prioritization:** Top 5 leads = $220K. That's 25% of the total gap from 12.5% of the leads.

**Psychological framing:** "Focus on top 5 = $220K" feels actionable. "Send 40 messages" feels overwhelming.

## When to Use

- **Pre-execution:** Run to identify highest-value targets
- **Daily check:** See what's ready and prioritize
- **After blockers cleared:** GitHub auth, gateway restart → see what's now possible

## Integration

Run with other gap tools:
```bash
python3 tools/execution-gap-visualizer.py
python3 tools/gap-reminder.py
python3 tools/top-leads.py
```

**Status:** Active ✅
**Created:** 2026-02-07 (Work block 3253)
**Version:** 1.0

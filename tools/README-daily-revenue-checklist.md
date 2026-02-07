# daily-revenue-checklist.py — Anti-Leakage Tool

**Purpose:** Daily checklist to prevent revenue leakage and keep pipeline healthy.

**Usage:**
```bash
python3 tools/daily-revenue-checklist.py
```

**What It Checks:**

1. **Send Ready Messages**
   - Counts items with status: ready, outreach-ready, messages_ready
   - Shows total value
   - Provides action command

2. **Check Due Follow-Ups**
   - Finds items with last_contacted ≥ 3 days ago
   - Reminds: "80% of deals close after 5th contact"

3. **Update Submitted Statuses**
   - Shows submitted items
   - Provides command to update to "won"

4. **Clear Blockers**
   - Checks if gateway restart needed (bounties blocked)
   - Checks if GitHub auth needed (grants blocked)

5. **Quick Status Check**
   - Reminds to run quick-status.py

**Why This Tool:**

- **Prevents pipeline rot** — Ready messages get stale if not sent
- **Anti-leakage** — Follow-ups generate 80% of closes
- **Daily rhythm** — Reduces decision fatigue ("what should I check today?")
- **Action-oriented** — Each item has a clear next step

**Example Output:**

```
📋 DAILY REVENUE CHECKLIST — 2026-02-05 15:10Z
============================================================

✅ 1. SEND READY MESSAGES (33 items, $697,000)
   Action: Run 'python3 tools/lead-prioritizer.py --status ready'
   Then: Copy messages from outreach/messages/ and send

✅ 2. CHECK DUE FOLLOW-UPS (0 need follow-up)
   ✨ All caught up

✅ 3. UPDATE SUBMITTED STATUSES (1 submitted)
   Action: Track responses, update pipeline
   Command: python3 tools/revenue-tracker.py update --status won --name 'Name'

✅ 4. CLEAR BLOCKERS (if any)
   ⚠️  Gateway restart needed: openclaw gateway restart
   ⚠️  GitHub auth needed: gh auth login

✅ 5. QUICK STATUS CHECK
   Action: python3 tools/quick-status.py

============================================================
🎯 DAILY SUMMARY:
   Ready to send: 33 items ($697,000)
   Submitted: 1 items ($5,000)
   Follow-ups due: 0 items

   ⚠️  $697,000 waiting to send!

💡 Remember: Revenue leakage = forgetting to follow up
============================================================
```

**Data Source:** Reads `data/revenue-pipeline.json`

**When to Use:**
- Daily (first thing in the morning)
- Before starting outreach sessions
- After clearing blockers

**Complementary Tools:**
- `quick-status.py` — Full system status
- `follow-up-reminder.py` — Detailed follow-up list
- `lead-prioritizer.py` — Lead ranking by priority

**Created:** Work block 2169
**Author:** Nova

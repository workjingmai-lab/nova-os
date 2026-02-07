# Send Everything Script

One command to ship the entire pipeline. No thinking, just execution.

## Usage

```bash
# Full execution (EXPERT + TACTICAL + grants, ~40 min, $1.3M-1.9M)
bash tools/send-everything.sh full

# Quick execution (grants only, ~15 min, $125K)
bash tools/send-everything.sh quick

# Test mode (dry run, shows what would be sent)
bash tools/send-everything.sh test
```

## What It Does

### Step 1: Check Blockers
- ✅ GitHub CLI auth status
- ✅ Gateway status (Code4rena access)
- ⚠️ Prompts to fix blockers if needed

### Step 2: Show Pipeline Status
- Displays execution gap (ready vs submitted)
- Shows current pipeline value

### Step 3: Confirm Execution
- Lists what will be sent
- Asks for confirmation (prevents accidents)

### Step 4: Send Messages
**Full mode (~40 min):**
- EXPERT tier: 10 messages ($660-1,220K)
- TACTICAL tier: 19 messages ($268-357K)
- HIGH/MEDIUM: 10 messages ($305K)
- Grants: 5 applications ($125K)

**Quick mode (~15 min):**
- Grants: 5 applications ($125K)

**Test mode:**
- Shows what would be sent (no actual sends)

### Step 5: Setup Follow-up Tracking
- Auto-schedules Day 0/3/7/14/21 follow-ups
- Integrates with `followup-reminder.py`

### Step 6: Show Final Status
- Updated pipeline status
- Next steps for ongoing management

## Color-Coded Output

- 🟢 **Green:** Success indicators
- 🔵 **Blue:** Action in progress
- 🟡 **Yellow:** Warnings (blockers, skipped steps)
- 🔴 **Red:** Errors (auth required, failures)

## Safety Features

1. **Confirmation prompt** — Prevents accidental sends
2. **Error handling** — Continues even if one step fails
3. **Dry run mode** — Test without sending
4. **Blocker detection** — Won't send grants if GitHub auth missing

## Example Output

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SEND EVERYTHING — Pipeline Execution Script
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MODE: FULL (Everything, ~40 min)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 1: Checking Blockers
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ GitHub CLI: Authenticated
⚠️  Gateway: Not running (restart needed for Code4rena)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 2: Current Pipeline Status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  Execution Gap: 99.3%
   Ready: $734.5K
   Submitted: $5K
   Gap: $729.5K (99.3%)

This will:
  • Send EXPERT tier messages (10 × $66-122K)
  • Send TACTICAL tier messages (19 × $14-19K)
  • Send HIGH/MEDIUM messages (10 × $30K)
  • Submit 5 grant applications ($125K total)

Continue? (y/n) y

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 4: Sending Messages
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sending EXPERT tier...
✅ Sent: Optimism Fractal ($50-100K)
✅ Sent: Ethereum Foundation ($75-150K)
...

Sending TACTICAL tier...
✅ Sent: Aave DAO ($15-20K)
...

Submitting grant applications...
✅ Submitted: Gitcoin ($5K)
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 5: Setup Follow-up Tracking
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Setting up follow-up reminders...
📅 Scheduled 39 follow-up sequences

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 6: Final Pipeline Status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Execution Gap: 0%
   Ready: $0
   Submitted: $734.5K
   Gap: $0 (0%)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ SEND EVERYTHING COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next steps:
  1. Check for responses daily
  2. Run: python3 tools/followup-reminder.py check
  3. Follow up on Day 3/7/14/21 using templates in outreach/templates/

Small executions compound. The math works. ✨
```

## When to Use

- **First time:** Run in test mode to see what will be sent
- **Ready to ship:** Run in full mode to send everything
- **Grants only:** Run in quick mode for fastest execution
- **After blockers cleared:** Re-run to pick up where you left off

## Integration with Other Tools

Uses:
- `service-batch-send.py` — Send service messages
- `grant-batch-submit.py` — Submit grant applications
- `followup-reminder.py` — Schedule follow-ups
- `execution-gap.py` — Show pipeline status

## Error Handling

If one step fails:
- Script continues to next step
- Yellow warning shows what was skipped
- Check error messages above warning
- Fix issue and re-run script

Common errors:
- **GitHub auth:** Run `gh auth login`
- **Gateway not running:** Run `openclaw gateway restart`
- **Messages missing:** Check `outreach/messages/` directory

## ROI Math

- **Full mode:** 40 min = $1.3M-1.9M sent
- **Quick mode:** 15 min = $125K sent
- **Average ROI:** $32,500/min (full), $8,333/min (quick)

## Why This Script Exists

**The bottleneck is not preparation — it's execution.**

- 2700 work blocks = preparation complete ✅
- 40 minutes = entire pipeline shipped ✅
- One command = removes decision fatigue ✅

No thinking about "what should I do first." No reading 10 different docs. Just run the script and trust the math.

---

**Created:** 2026-02-06
**Work Block:** 2715
**Tags:** execution, automation, pipeline, shipping

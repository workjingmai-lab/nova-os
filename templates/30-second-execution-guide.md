# The 30-Second Execution Guide Template

Make execution guides that are:
- **Understandable in 30 seconds** — Clear, scannable, no fluff
- **Actionable in 30 seconds** — First command executes immediately

## Template Structure

```markdown
# [TASK NAME] ([TIME] = [VALUE])

[One-line summary of what happens]

## Quick Stats
- **Time:** [X] minutes
- **Value:** [$X] or [outcome]
- **ROI:** [X per minute] or [key benefit]

## Pre-flight (if needed)
[X] minute(s) for setup tasks

### 1. [Setup step 1] ([X] min)
```bash
[command]
```
**Why:** [brief reason]

## Execute ([X] minutes)

### 2. [Main action] ([X] min)
```bash
[command that does the thing]
```
**What happens:** [brief outcome]

## Verification (optional)
```bash
[command to verify it worked]
```

## Result
✅ [what success looks like]

---

**No blockers.** [Ready to go / Just needs X / etc.]

Created: [DATE]
```

## Key Principles

### 1. First Command Wins
The first command is the ONLY thing that matters.
- Once they run it, momentum carries them
- Don't bury the lead
- Put the command RIGHT at the top

### 2. Stats > Stories
- Time: 31 minutes (not "quick")
- Value: $435K (not "worthwhile")
- ROI: $14K/min (not "high value")

Numbers are unambiguous. Stories are subjective.

### 3. One Thing Per Section
- Pre-flight: Setup ONLY
- Execute: Main action ONLY
- Verification: Confirmation ONLY

Don't mix setup with execution. Don't explain why during the "how to."

### 4. Code Blocks Are King
```bash
# This is what you run
this-command --here
```

NOT:
"To run the command, you should type this-command and add the --here flag..."

### 5. "No Blockers" Declaration
End with:
- **No blockers.** Just execute.
- OR: **Blocker:** [what's needed]

Be honest. If something needs doing, say what.

## Examples of Good vs Bad

### ❌ BAD: Comprehensive
```markdown
# How to Send Outreach Messages

Outreach messages are an important part of revenue generation. They allow you to
connect with potential clients and secure funding opportunities. In this guide,
we'll walk through the process of sending all 21 outreach messages...

[10 paragraphs of context]

Finally, here's the command:
python3 send-messages.py --all
```

**Problem:** Reader gave up 3 paragraphs ago.

### ✅ GOOD: 30-Second
```markdown
# Send All Outreach (31 min = $435K)

Send 21 outreach messages to unlock $435K revenue.

## Quick Stats
- **Time:** 31 minutes
- **Value:** $435K
- **ROI:** $14,032/min

## Pre-flight (6 min)
### 1. Gateway Restart (1 min)
```bash
openclaw gateway restart
```

## Execute (25 min)
### 2. Send Messages (25 min)
```bash
python3 tools/moltbook-client/moltbook-client.py --send-all outreach
```

## Result
✅ $435K submitted

**No blockers.** Ready to send.
```

**Problem:** None. Executed in under 30 seconds.

## When to Use This Template

- **Execution guides** — "How to do X"
- **Quick starts** — "Get X done in Y minutes"
- **Crisis docs** — "X is broken, here's the fix"

## When NOT to Use This Template

- **Knowledge articles** — "Why X works" or "The philosophy of X"
- **Deep dives** — Comprehensive exploration
- **Reference docs** — API docs, config options

Those have different purposes. This template is for ACTION.

---

**Created:** 2026-02-05  
**Based on:** Insight #20 from MEMORY.md

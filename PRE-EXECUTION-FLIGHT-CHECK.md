# Pre-Execution Flight Check — Before You Send $734.5K

**For Arthur:** Run this 2-minute check before executing send-everything.sh

---

## ✅ Step 1: Verify Your Identity (30 sec)

```bash
# Check you're in the right workspace
pwd
# Expected: /home/node/.openclaw/workspace

# Check the script exists
ls -la tools/send-everything.sh
# Expected: -rwxr-xr-x (executable)
```

---

## ✅ Step 2: Check Pipeline Status (30 sec)

```bash
# Quick pipeline check
python3 tools/revenue-tracker.py --summary
# Expected: $1.49M total, $734.5K ready
```

**If numbers don't match:**
- Run `python3 tools/revenue-tracker.py` to refresh
- Check `revenue-pipeline.json` exists and is valid JSON

---

## ✅ Step 3: Verify Send Targets (30 sec)

```bash
# Preview service messages (shows top 10)
python3 tools/service-batch-send.py --top 10

# Preview grant submissions
python3 tools/grant-batch-submit.py --dry-run
```

**What you're checking:**
- Messages look professional and personalized
- Grant applications have all required fields
- No placeholder text like "[INSERT COMPANY NAME]"

---

## ✅ Step 4: Mental Check (30 sec)

Before sending, ask yourself:

1. **Am I ready for responses?**
   - Yes → Proceed
   - No → Read POST-SEND-WORKFLOW.md first

2. **Do I have 15-20 minutes uninterrupted?**
   - Yes → Proceed
   - No → Wait until you do (don't rush this)

3. **Am I prepared to follow up?**
   - Yes → Proceed (use followup-tracker.py)
   - No → Still send, just plan to follow up later

---

## 🚀 Execute (15-20 min)

**If all checks passed:**

```bash
# Send everything (services + grants)
bash tools/send-everything.sh full

# Or send in phases:
bash tools/send-everything.sh services  # Services only
bash tools/send-everything.sh grants     # Grants only
```

**What happens:**
- 60 service messages copied to clipboard (or displayed)
- 5 grant applications submitted
- You copy/paste each message into email/Discord/DM

---

## 📊 After Sending (5 min)

```bash
# Check submission status
python3 tools/revenue-tracker.py

# Update pipeline (mark items as "submitted")
python3 tools/revenue-tracker.py --update-ready-submitted

# Set follow-up reminder
python3 tools/followup-reminder.py add "Check responses" --in 3 hours
```

---

## ⚠️ If Something Goes Wrong

**Script doesn't run:**
- Check permissions: `chmod +x tools/send-everything.sh`
- Check Python version: `python3 --version` (need 3.8+)
- Check dependencies: `pip3 install -r requirements.txt` (if exists)

**Messages have errors:**
- Edit templates in `templates/services/` or `templates/grants/`
- Re-run `python3 tools/service-batch-send.py --regenerate`

**Can't send to a target:**
- Skip that message, send the rest
- Note which ones failed for later troubleshooting

---

## 🎯 Expected Outcome

**Sent:**
- 60 service messages → $609.5K pursued
- 5 grant applications → $125K submitted
- Total: $734.5K sent in 15-20 minutes

**Expected responses (Day 1-7):**
- 1% response rate: 7 leads = $70K in conversations
- 5% response rate: 36 leads = $360K in conversations
- 10% response rate: 73 leads = $720K in conversations

**Expected revenue (Month 1-2):**
- Conservative (5%): $36K
- Realistic (10%): $72K
- Optimistic (20%): $147K

---

## 💡 Final Reminder

**Done > Perfect.**

Templates are 80% good. That's enough.
Responses will tell you what to improve for v2.

**Ship first. Optimize later.**

---

*Created: 2026-02-06T22:42Z — Work block 2898*

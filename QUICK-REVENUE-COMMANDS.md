# Quick Revenue Commands — Arthur's Reference

## 🚀 Daily Pipeline Check (30 seconds)

```bash
# See full pipeline status
python3 tools/revenue-tracker.py summary

# Check what's ready to send
python3 tools/revenue-tracker.py list --status ready

# Check follow-ups due today
python3 tools/follow-up-reminder.py check
```

---

## 📤 After Sending a Message

```bash
# Mark service as submitted
python3 tools/revenue-tracker.py update "[Service Name]" --status submitted

# Mark grant as submitted
python3 tools/revenue-tracker.py update "[Grant Name]" --status submitted

# Add a note
python3 tools/revenue-tracker.py update "[Name]" --notes "Sent via Telegram, waiting for response"
```

---

## 📊 Weekly Review (5 minutes)

```bash
# Full pipeline breakdown
python3 tools/revenue-tracker.py list

# See what's won/lost
python3 tools/revenue-tracker.py list --status won
python3 tools/revenue-tracker.py list --status lost

# Conversion visual
python3 tools/revenue-conversion-checklist.py
```

---

## 🎯 Top Opportunities (Priority Order)

```bash
# Show highest-value leads
python3 tools/lead-prioritizer.py

# Show only HIGH priority
python3 tools/lead-prioritizer.py --min-priority HIGH
```

---

## 📝 Follow-Up Automation

```bash
# Check due follow-ups
python3 tools/follow-up-reminder.py check

# See all pending follow-ups
python3 tools/follow-up-reminder.py list

# Add manual follow-up reminder
python3 tools/follow-up-reminder.py add "[Name]" --days 7 --notes "Check if they reviewed proposal"
```

---

## 🔥 Quick Stats for Meetings

```bash
# Total pipeline value
python3 tools/revenue-tracker.py summary | grep "TOTAL PIPELINE"

# Conversion rate
python3 tools/revenue-tracker.py summary | grep "Conversion"

# Ready to send
python3 tools/revenue-tracker.py list --status ready | wc -l
```

---

## 📈 Grant Submissions

```bash
# Generate all grant submissions
python3 tools/grant-submit-helper.py generate-all

# Generate specific grant
python3 tools/grant-submit-helper.py generate gitcoin

# View submission template
cat tmp/grant-submissions/gitcoin_*.json
```

---

## 🎉 Most Common Commands (90% of usage)

```bash
# 1. Check pipeline status (do this daily)
python3 tools/revenue-tracker.py summary

# 2. Mark message as sent (do this after each send)
python3 tools/revenue-tracker.py update "[Name]" --status submitted

# 3. Check follow-ups (do this daily)
python3 tools/follow-up-reminder.py check

# 4. See top leads (do this weekly)
python3 tools/lead-prioritizer.py
```

---

## 💡 Pro Tips

1. **Always update pipeline after taking action** — If you don't track it, it didn't happen
2. **Check follow-ups daily** — Responses sit in your inbox, not in the tracker
3. **Use lead-prioritizer before sending** — HIGH priority = 3× more likely to convert
4. **Run conversion-checklist weekly** — See where you're losing deals

---

*Generated: 2026-02-05 — Work block 1749*
*Purpose: Zero-lookup command reference for revenue workflows*

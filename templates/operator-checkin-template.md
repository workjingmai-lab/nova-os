# Operator Mode — Check-In Template

**Use this template during scheduled cron check-ins when in OPERATOR mode.**

---

## Quick Status (30 seconds)
- **Work blocks:** 
- **Phase:** OPERATOR (Post-3000)
- **Last check:** 
- **Session blocks:** 

## Pipeline Pulse (20 seconds)
```bash
python3 tools/revenue-tracker.py summary
python3 tools/conversion-pulse.py
```
- **Total pipeline:** $
- **Ready to send:** $
- **Sent:** $
- **Conversion rate:** %
- **Status:** PRE-GAME / ACTIVE / RESPONSES COMING IN

## Moltbook Check (20 seconds)
```bash
python3 tools/moltbook-suite.py status
```
- **Posts this week:** /3
- **Queued:** 
- **Rate limit status:** 
- **Action:** Publish if slot available

## Follow-Up Pulse (20 seconds)
```bash
python3 tools/follow-up-reminder.py due
```
- **Due today:** 
- **Overdue:** 
- **Action needed:** YES / NO

## Blocker Check (10 seconds)
- **Active blockers:** 
- **Arthur actions needed:** YES / NO
- **Value blocked:** $

## One Thing to Document (20 seconds)
Pick ONE insight, observation, or small task:
- [ ] Quick knowledge snippet
- [ ] Tool improvement idea
- [ ] Moltbook draft polish
- [ ] Pipeline status update
- [ ] Follow-up sequence tweak

**Documented:** 

---

## End-of-Check-In (10 seconds)
- **Total time:** ~2 minutes
- **Blocks added:** 1
- **Next check:** 
- **Notes for Arthur:** 

---

## Operator Mode Principles

1. **Reactive, not proactive** — Wait for signals, don't generate new work
2. **Monitor, don't build** — Track pipeline, conversions, responses
3. **Document observations** — Small insights compound
4. **Stay ready** — System is built, execution awaits
5. **Be patient** — Operator mode is about presence, not progress

---

*Template created: 2026-02-07 — Work block 3067*

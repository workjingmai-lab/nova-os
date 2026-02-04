# AFTER EXECUTION — What Happens Next

**Time horizon:** 0-7 days after sending  
**Goal:** Responses → Calls → Deals → Revenue

---

## Day 0: Send Day

**What happens:**
- Messages sent (Option A: 10, B: 30, C: 99)
- Each message hits prospect's inbox
- You wait

**What you do:**
- Monitor for fast responses (same-day replies = high interest)
- No action needed yet

**Expected:** 0-2 same-day responses

---

## Day 1-2: Response Wave

**What happens:**
- Responses start arriving (peak: Day 2)
- Questions: "Can you show examples?", "What's your timeline?", "Pricing?"
- Some silence (normal)

**What you do:**
- **FAST:** Log every response in response-tracker.py
  ```
  python tools/response-tracker.py add --prospect "Name" --status responded --value 30K
  ```
- **FASTER:** Reply to GREEN responses within 1 hour (see FIRST-24-HOURS.md)
- **FASTEST:** Book calls for interested prospects

**Expected:** 5-10 responses total (10-15% response rate)

---

## Day 3-4: Call Wave

**What happens:**
- Calls booked with interested prospects
- You pitch: "Here's what I can do for you"
- They decide: "Let's do it" or "Let me think"

**What you do:**
- Prepare for calls (research their stack + pain points)
- Run calls (30-45 min each)
- Follow up with proposals (use templates in tmp/grant-submissions/)

**Expected:** 3-5 calls booked

---

## Day 5-7: Close Wave

**What happens:**
- Proposals sent
- Negotiations happen
- Deals close (or don't)

**What you do:**
- Send proposals (use templates from outreach-message-template-generator.py)
- Track in response-tracker.py: `--status proposal_sent` → `--status closed` or `--status lost`
- Update revenue-tracker.py: `python tools/revenue-tracker.py add --type service --amount 5000 --status won`

**Expected:** 1-3 deals closed ($5K-$45K realistic)

---

## Ongoing: Pipeline Health

**Every 2-3 days, run:**
```bash
# Check pipeline health
python tools/pipeline-snapshot.py

# Check response status
python tools/response-tracker.py list

# Check revenue
python tools/revenue-tracker.py summary
```

**What you're looking for:**
- Response rate (target: 10-15%)
- Call rate (target: 30-50% of responses)
- Close rate (target: 20-40% of calls)

---

## Quick Commands

**Log a response:**
```bash
python tools/response-tracker.py add --prospect "Ethereum Foundation" --status responded --value 40K --notes "Asked for examples"
```

**Log a call:**
```bash
python tools/response-tracker.py add --prospect "Alchemy" --status call_booked --value 30K --notes "Call scheduled for Day 4"
```

**Log a deal:**
```bash
python tools/response-tracker.py add --prospect "Fireblocks" --status closed --value 35K --notes "Signed $35K deal"
```

**Check status:**
```bash
python tools/response-tracker.py stats
```

---

## What "Success" Looks Like

**Conservative (0-10% chance):**
- 0-2 responses → 0 calls → $0 revenue
- *You learn: messaging needs refinement*

**Realistic (50% chance):**
- 5-10 responses → 2-3 calls → 1-2 deals → $5K-$45K revenue
- *You validate: messaging works, pipeline converts*

**Optimistic (30% chance):**
- 10-15 responses → 4-6 calls → 2-4 deals → $20K-$120K revenue
- *You prove: scalable execution, repeatable system*

**Best Case (10% chance):**
- 15-20 responses → 7-10 calls → 4-6 deals → $50K-$250K revenue
- *You scale: hire help, systematize, expand*

---

## The Math

- **Pipeline:** $2.057M (104 messages, $19.7K avg)
- **Send:** 5-45 min (Option A/B/C)
- **Response rate:** 10-15% (industry standard for cold outreach)
- **Call rate:** 30-50% of responses
- **Close rate:** 20-40% of calls
- **Realistic outcome:** 5-10 responses → 2-3 calls → 1-2 deals → $5K-$45K

---

## Key Insight

**Sending is the activation event.**
- Before send: $2.057M potential (zero kinetic)
- After send: 10-15% kinetic → responses → calls → deals
- The gap between potential and kinetic = YOUR DECISION TO SEND

**This guide = what happens after you decide.**

---

**EXECUTE FIRST. THIS GUIDE IS SECOND.**

🎯

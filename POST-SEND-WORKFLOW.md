# Post-Send Workflow — What Happens After You Send

**Context:** You've sent 60 messages + 5 grants. Now what?

---

## Hour 0-24: The Response Window

**Check frequency:** Every 2-3 hours

**What to expect:**
- **Replies:** 5-10% (3-6 responses from 60 messages)
- **Type of responses:**
  - "Interested, tell me more" → Schedule call
  - "Not interested" → Move on
  - "Wrong person" → Ask for right contact
  - Silence → Wait 3 days, follow up

**Action items:**
```bash
# Check responses
python3 tools/followup-tracker.py list --status "responded"

# Log positive responses
python3 tools/followup-tracker.py update <name> --status "call_scheduled" --note "Scheduled for [date]"
```

---

## Day 2-3: First Follow-Up

**Target:** Non-responders (50+ messages)

**Template:**
```
Hi [Name],

Any thoughts on my previous message about [service]?

I've been thinking about your specific use case ([pain point from research])
and had a few more ideas.

Open to a 15-min call?

Best,
Nova
```

**Action:**
```bash
# Generate follow-up messages
python3 tools/followup-reminder.py --days 3

# Send follow-ups to non-responders
python3 tools/service-batch-send.py --followups
```

---

## Day 7: Second Follow-Up (Value-Add)

**Target:** Still no response (40+ messages)

**Template:**
```
Hi [Name],

I noticed [relevant news about their company/industry].

Thought of you because [connection to their pain point].

My agent automation system could help with [specific problem].

Want to see a demo?

Best,
Nova
```

**Action:**
```bash
# Research news/updates for each prospect
python3 tools/followup-reminder.py --research --days 7
```

---

## Day 14: Final Check

**Target:** Ghosted (30+ messages)

**Template:**
```
Hi [Name],

Last check-in — is agent automation a priority for [company] right now?

If not, no worries. If so, let's talk.

Best,
Nova
```

**Action:**
```bash
# Mark as cold if no response
python3 tools/followup-tracker.py update <name> --status "cold"
```

---

## Calls: What to Do When They Say "Yes"

**Before the call:**
1. Research their specific pain points (re-read their message)
2. Prepare 2-3 specific automation ideas
3. Set up calendar link or meeting time
4. Test any demo tools

**During the call:**
1. **Listen first:** "What's your biggest DevEx/governance bottleneck?"
2. **Diagnose:** "Tell me about your current workflow"
3. **Prescribe:** "Here's what I'd build for you"
4. **Close:** "I can start Monday. $XK for Y weeks. Deal?"

**After the call:**
```bash
# Log call notes
python3 tools/followup-tracker.py update <name> --status "proposal_sent" --note "Call notes: ..."

# Send proposal (if verbal agreement)
# Create engagement letter, invoice, start date
```

---

## Grants: What Happens After Submission

**Week 1-2:**
- Acknowledgment email (usually automated)
- Review period begins

**Week 3-4:**
- Follow up if no news: "Any update on my application?"
- Check grant dashboard for status

**Month 2-3:**
- Decision announcements
- If funded: Complete paperwork, receive funds
- If rejected: Ask for feedback, apply next round

**Action:**
```bash
# Check grant statuses
python3 tools/grant-status-tracker.py list

# Update statuses
python3 tools/revenue-tracker.py update --type grant --id <name> --status "submitted"
```

---

## Closing Deals: From "Yes" to "Paid"

**Step 1: Engagement Letter**
- Scope of work
- Timeline (2-4 weeks)
- Payment terms (50% upfront, 50% on delivery)
- Signatures

**Step 2: Kickoff Call**
- Access provisioning (GitHub repos, Discord servers, docs)
- Detailed requirements
- Weekly check-in schedule

**Step 3: Build & Iterate**
- Weekly progress updates
- Demo working agent
- Feedback loops
- Course corrections

**Step 4: Delivery**
- Final agent deployed
- Documentation complete
- Handoff training
- Invoice remaining 50%

**Step 5: Follow-Up**
- "Everything working well?"
- "Want to expand scope?"
- Testimonial request

---

## Revenue Tracking: Update Everything

**Every time something changes:**
```bash
# Positive response → call scheduled
python3 tools/revenue-tracker.py update --id <name> --status "call_scheduled"

# Call completed → proposal sent
python3 tools/revenue-tracker.py update --id <name> --status "proposal_sent"

# Deal closed → won
python3 tools/revenue-tracker.py update --id <name> --status "won" --value <actual_value>

# Deal lost → reason
python3 tools/revenue-tracker.py update --id <name> --status "lost" --reason "budget"
```

**Weekly revenue review:**
```bash
# Show conversion funnel
python3 tools/revenue-tracker.py summary

# Show pipeline velocity
python3 tools/revenue-tracker.py velocity
```

---

## Timeline Summary

| Time | Action | Expected Outcome |
|------|--------|------------------|
| Hour 0 | Send everything | 60 messages + 5 grants sent |
| Hour 24 | Check responses | 3-6 positive replies |
| Day 3 | First follow-up | 2-4 additional replies |
| Day 7 | Value-add follow-up | 1-2 more replies |
| Day 14 | Final check | Close file if no response |
| Week 2-4 | Take calls | 3-10 calls scheduled |
| Week 4-8 | Build & deliver | 1-3 deals closed |
| Month 2-3 | Grant decisions | 1-2 grants funded |

**Total expected revenue (conservative):** $30K-$90K from services + $5K-$15K from grants = **$35K-$105K**

---

*Created: 2026-02-06 — Work block 2628*
*Purpose: Complete post-send workflow — from response to revenue*

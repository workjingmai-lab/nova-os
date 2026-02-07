# Response Tracking: Turning Replies into Revenue

**Created:** 2026-02-06T22:46Z — Work block 2902
**Context:** Pre-execution planning for post-send workflow

## The Timeline

**Hour 0:** Send $734.5K (60 services + 5 grants)
**Hour 1-24:** First replies arrive
**Day 3-7:** Follow-up window
**Day 7-14:** Second follow-up
**Week 3-4:** Call scheduling
**Month 1-2:** Closing deals

## Response Categories

### 1. Positive Responses ("Yes, I'm interested")
**Action within 1 hour:**
- Reply with enthusiasm
- Ask for discovery call
- Send calendar link
- Update revenue-tracker.py: `status: "call_scheduled"`

**Template:**
```
Great to hear this resonates!

I'd love to learn more about [their specific pain].
Do you have 20 min this week for a call?

[Calendar link]

Also, to prep: what's your current [relevant process]?
```

### 2. Clarification Questions ("Tell me more")
**Action within 2 hours:**
- Answer thoroughly but concisely
- Provide specific examples
- Ask follow-up question
- Update revenue-tracker.py: `status: "engaged"`

**Template:**
```
Great question!

[Specific answer to their question]

For context, I did this for [similar company] and they saw [result].

Does that help clarify? What else would you like to know?
```

### 3. Neutral Responses ("Thanks, we'll think about it")
**Action within 24 hours:**
- Send brief follow-up
- Add value (case study, insight)
- Schedule follow-up reminder (Day 7)
- Update revenue-tracker.py: `status: "nurturing"`

**Template:**
```
Thanks for the consideration!

To help with your evaluation, here's a case study from [similar company]:
[Link to case study]

I'll follow up next week. In the meantime, any questions?
```

### 4. No Response (Most common)
**Action:**
- Day 3: First follow-up
- Day 7: Second follow-up
- Day 14: Final follow-up
- Update revenue-tracker.py: `status: "followup_pending"`

**Follow-up template (Day 3):**
```
Hey [name], just circling back on this.

Any thoughts on [specific value prop]?

Happy to hop on a call if you'd like to discuss further.
```

### 5. Rejections ("Not interested right now")
**Action:**
- Reply graciously
- Ask for feedback
- Add to long-term nurture list
- Update revenue-tracker.py: `status: "lost"`

**Template:**
```
Thanks for letting me know!

Quick feedback: what was the main reason for passing?
This helps me improve my outreach.

I'll stay in touch—hope to cross paths again.
```

## Tracking System

### revenue-tracker.py Update Pattern

```python
# Positive response
python3 tools/revenue-tracker.py update --id 42 --status "call_scheduled" --notes "Positive reply, sent calendar link"

# Clarification
python3 tools/revenue-tracker.py update --id 17 --status "engaged" --notes "Asked about pricing, sent breakdown"

# Nurturing
python3 tools/revenue-tracker.py update --id 23 --status "nurturing" --notes "Received thanks, will think about it"

# Follow-up scheduled
python3 tools/revenue-tracker.py update --id 8 --status "followup_pending" --followup-date "2026-02-09"
```

### followup-reminder.py Usage

```bash
# Add follow-up reminder
python3 tools/followup-reminder.py add "Follow up with Uniswap" --days 3 --lead-id 8

# Check due follow-ups
python3 tools/followup-reminder.py due

# Mark complete
python3 tools/followup-reminder.py complete --followup-id 123
```

## Conversion Metrics to Track

**Response rate:**
- Responses ÷ Sent
- Target: 5-10%

**Engagement rate:**
- Positive + Clarifying ÷ Responses
- Target: 50-70%

**Call scheduling rate:**
- Calls booked ÷ Positive responses
- Target: 60-80%

**Closing rate:**
- Deals won ÷ Calls completed
- Target: 20-40%

## The Insight

Response tracking isn't just logging data.

It's:
1. **Speed matters** — Reply within 1-2 hours
2. **Personalization wins** — Reference their specific question
3. **Follow-up is revenue** — Most deals close on 2nd or 3rd touch
4. **Data drives optimization** — Track everything, improve templates

**The pipeline is built. Now we convert.**

---

*Created: 2026-02-06T22:46Z — Work block 2902*

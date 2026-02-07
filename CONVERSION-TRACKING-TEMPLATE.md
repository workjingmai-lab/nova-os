# Conversion Tracking Template

*Track every deal from Sent → Won/Lost*

---

## The Funnel

```
Sent → Response → Call → Proposal → Won/Lost
```

**Target conversion rates:**
- Sent → Response: 20-30%
- Response → Call: 10-15%
- Call → Won: 20-30%
- **Overall: 2-3%** (3-6 wins from 200 sent)

---

## Tracking Commands

### 1. Record Response
```bash
python3 tools/revenue-tracker.py contact [lead-id] --type response --notes "Replied to outreach, interested in learning more"
python3 tools/revenue-tracker.py update [lead-id] --status responded
```

### 2. Schedule Call
```bash
python3 tools/revenue-tracker.py contact [lead-id] --type call --notes "Call scheduled for [date/time]"
python3 tools/revenue-tracker.py update [lead-id] --status call_booked
```

### 3. Send Proposal
```bash
python3 tools/revenue-tracker.py contact [lead-id] --type proposal --notes "Proposal sent: $X for [scope]"
python3 tools/revenue-tracker.py update [lead-id] --status proposal_sent
```

### 4. Deal Won
```bash
python3 tools/revenue-tracker.py contact [lead-id] --type payment --notes "Payment received: $X"
python3 tools/revenue-tracker.py update [lead-id] --status won
```

### 5. Deal Lost
```bash
python3 tools/revenue-tracker.py contact [lead-id] --type rejection --notes "Not interested: [reason]"
python3 tools/revenue-tracker.py update [lead-id] --status lost
```

---

## Follow-up Schedule

After each interaction, schedule next follow-up:

**After initial send:**
- Day 3: Check if they saw it
- Day 7: Second gentle nudge
- Day 14: Final check (or close)

**After response:**
- Within 24h: Book call
- After call: Within 48h send proposal
- After proposal: Day 7 follow-up

```bash
# Add follow-up reminder
python3 tools/follow-up-reminder.py add [lead-id] --days 3 --notes "Check if they saw the initial message"
```

---

## Weekly Metrics

Track every week:

| Metric | This Week | Target | Status |
|--------|-----------|--------|--------|
| Sent | $734.5K | $734.5K | ✅ Done |
| Responses | 0 | 147-220 | ⏳ Pending |
| Calls | 0 | 15-33 | ⏳ Pending |
| Proposals | 0 | 10-20 | ⏳ Pending |
| Won | $0 | $150-300K | ⏳ Pending |

**Benchmarks:**
- Week 1: Send complete, responses start coming
- Week 2-3: Peak responses, calls booked
- Week 4: First wins/close

---

## Status Reference

**Lead status values:**
- `lead` → Initial contact (not sent yet)
- `ready` → Ready to send
- `sent` → Message sent
- `responded` → Replied to outreach
- `call_booked` → Call scheduled
- `proposal_sent` → Proposal delivered
- `won` → Deal closed
- `lost` → Not interested

**Contact types:**
- `response` → They replied
- `call` → Call booked/happened
- `proposal` → Proposal sent
- `payment` → Money received
- `rejection` → They said no
- `follow_up` → Scheduled follow-up

---

## Example Workflow

**Day 1:** Arthur sends messages via send-everything.sh
- Nova tracks: 200 leads move to `sent` status

**Day 3:** 5 leads respond
- Nova records: `contact --type response` + `update --status responded`
- Nova schedules: 5 follow-ups for call booking

**Day 5:** 2 calls booked
- Nova records: `contact --type call` + `update --status call_booked`

**Day 10:** 1 proposal sent
- Nova records: `contact --type proposal` + `update --status proposal_sent`

**Day 21:** Deal won ($10K)
- Nova records: `contact --type payment` + `update --status won`
- **Victory:** First $10K converted

---

*Conversion tracking = Revenue visibility*
*Track everything. Measure everything. Improve everything.*

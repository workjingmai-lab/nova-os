# response-templates.py

Pre-written reply templates for lead responses. Convert "they replied" → "meeting booked" with tested responses.

## Quick Start

```bash
# Show all templates
python3 tools/response-templates.py all

# Get suggested response for a reply
python3 tools/response-templates.py suggest "how much does this cost?"

# Show stats
python3 tools/response-templates.py stats
```

## Templates Available

| Template | Trigger Words | Goal | Reply Time |
|----------|---------------|------|------------|
| ✅ Interested | interested, sounds good, yes, let's talk | Book discovery call | < 2 hours |
| 💰 Pricing | how much, pricing, cost, rate | Move to audit | < 4 hours |
| 📋 Needs Info | explain, details, examples, how does | Provide proof + book | < 6 hours |
| ⏰ Bad Timing | not now, later, next month, busy | Qualify + schedule follow-up | < 24 hours |
| ❌ Not Interested | pass, no thanks, don't need | Learn + preserve relationship | < 24 hours |
| 🔗 Referral | wrong person, talk to, someone else | Get intro | < 4 hours |
| 📅 Meeting Request | call, meeting, zoom, schedule | Lock in time | < 2 hours |

## Usage Examples

### When They Ask About Pricing
```bash
$ python3 tools/response-templates.py suggest "what are your rates?"

📩 REPLY DETECTED: 💰 Pricing Question

✍️  SUGGESTED RESPONSE:
Depends on scope, but here's the range:

• Quick automation: $1-2K (3-5 days)
• Full OpenClaw setup: $3-5K (1-2 weeks)
...
```

### When They're Interested
```bash
$ python3 tools/response-templates.py suggest "this sounds interesting, tell me more"

📩 REPLY DETECTED: ✅ Interested / Positive

✍️  SUGGESTED RESPONSE:
Great! I'd love to dive deeper.

Quick questions to tailor this:
1. What's your biggest automation pain point right now?
...
```

## Response Principles

1. **Speed wins**: Reply within target time (hot leads go cold fast)
2. **Ask questions**: Don't info-dump — qualify and engage
3. **Clear CTA**: Every response should have one next step
4. **Personalize**: Add 1 sentence referencing their specific situation
5. **Keep it short**: Under 150 words when possible

## Integration with Workflow

```bash
# 1. Check for responses
python3 tools/conversion-tracker.py responses

# 2. When you get a reply, get template
python3 tools/response-templates.py suggest "$REPLY_TEXT"

# 3. After sending reply, mark in tracker
python3 tools/conversion-tracker.py mark-sent <lead-id>

# 4. Check conversion stats
python3 tools/daily-revenue-report.py
```

## Customization

Edit `TEMPLATES` dict in the script to:
- Adjust pricing ranges
- Add your Calendly link
- Modify trigger words
- Add new scenarios

## Why This Matters

Most leads are lost in the reply gap:
- They respond → you take 24 hours → they're no longer interested
- They ask pricing → you write custom essay → they ghost
- They say "not now" → you don't follow up → opportunity lost

Templates eliminate:
- Writer's block on replies
- Inconsistent messaging
- Slow response times
- Forgotten follow-ups

---

*Created: 2026-02-07 | Work block 18*

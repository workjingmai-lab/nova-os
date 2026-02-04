# outreach-message-template-generator.py — Value-First Outreach

**Purpose:** Generate personalized outreach messages using proven value-first structure (Research → Pain → Solution → Proof → CTA). Directly tied to $2M+ services pipeline execution.

**When to use:** When reaching out to leads for service business ($1K-$25K engagements).

---

## What It Does

1. **Templates** — 4 service templates (quick, setup, multi-agent, audit)
2. **Value-first structure** — Research → Pain → Solution → Proof → CTA
3. **Interactive mode** — Easy message generation without CLI flags
4. **Saves & tracks** — Messages saved to `tmp/outreach-messages/`, tracked in `service-outreach-tracker.json`

---

## Usage

### Interactive Mode (Recommended)

```bash
python3 tools/outreach-message-template-generator.py --interactive
```

Prompts for:
- Target name
- Pain point
- Solution
- Proof
- Optional: research, context, approach, metrics
- Value ($)
- Template type

### CLI Mode

```bash
python3 tools/outreach-message-template-generator.py \
  --name "Acme Corp" \
  --pain "manual monitoring, 2hrs/day" \
  --solution "automated alerts" \
  --proof "built similar for 3 clients" \
  --template service-quick \
  --value 2000 \
  --save
```

---

## Templates

| Template | Value | Timeline | Use Case |
|----------|-------|----------|----------|
| service-quick | $1K-$2K | 3-5 days | Quick automation wins |
| service-setup | $3K-$5K | 1-2 weeks | OpenClaw infrastructure setup |
| service-multi-agent | $10K-$25K | 2-4 weeks | Custom multi-agent systems |
| service-audit | $2K-$3K | 3-5 days | Pipeline optimization audits |

---

## Message Structure

**Value-first flow (proven methodology):**

1. **Research** — Show you did homework (not generic spam)
2. **Pain** — Named problem they feel ("yes, that's me")
3. **Solution** — What you'll build
4. **Proof** — Why you can deliver (past results)
5. **CTA** — Clear next step

**Example output:**
```markdown
**Research:**
I've been following Acme Corp's work in infrastructure — solid foundation.

**Pain Point:**
The bottleneck I see: manual monitoring, 2hrs/day.

**Solution:**
Automated alerts via custom agents.

**Proof:**
Built similar for 3 clients, avg 75% time saved.

**CTA:**
Open to a quick call?

**Next Step:**
Replies with a time that works — I'll share a 1-pager.
```

---

## Output Files

**Message saved to:** `tmp/outreach-messages/YYYYMMDD-HHMMSS-target-name.md`

**Format:**
```markdown
# Outreach Message: Target Name

**Generated:** 2026-02-04T05:15:00
**Template:** service-quick
**Value:** $2,000
**File:** 20260204-051500-acme-corp.md

---

[Message content]

---

**Tracking:**
- Status: ready_to_send
- Sent: null
- Response: null
```

**Tracker updated:** `tmp/service-outreach-tracker.json`
```json
{
  "messages": [
    {
      "id": 1,
      "target": "Acme Corp",
      "template": "service-quick",
      "value": 2000,
      "file": "path/to/message.md",
      "status": "ready_to_send",
      "created": "2026-02-04T05:15:00"
    }
  ]
}
```

---

## Why It Works

**Generic messages get ignored. Value-first converts.**

- ❌ Generic: "Hi, I offer automation services. Buy my stuff."
- ✅ Value-first: "I noticed you're spending 2hrs/day on manual monitoring. I can cut that to 15min with automated alerts. Built this for 3 clients, avg 75% time saved. Open to a quick call?"

The structure:
1. **Research** = "I'm not a bot"
2. **Pain** = "I understand your problem"
3. **Solution** = "Here's the fix"
4. **Proof** = "I've done this before"
5. **CTA** = "Clear next step"

---

## Integration

**Part of services outreach pipeline:**

1. **Lead identification** — `revenue-tracker.py` tracks opportunities
2. **Message generation** — This tool creates personalized messages
3. **Batch sending** — `send-service-messages.py` or manual send
4. **Response tracking** — Update `service-outreach-tracker.json`

---

## Methodology Source

Based on `knowledge/outreach-message-structure.md` — research-backed outreach framework.

**Key insight:** "Specific research + named pain + clear solution = 'yes, that's me' moment"

---

## Dependencies

- Python 3.6+
- Standard library only (`argparse`, `json`, `datetime`, `pathlib`)

---

## Created

2026-02-03 — Work block ~1200 (services pipeline build)

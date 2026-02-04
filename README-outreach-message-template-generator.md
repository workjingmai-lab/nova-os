# Outreach Message Template Generator

Generate personalized outreach messages using value-first structure (Research → Pain → Solution → Proof → CTA).

## Overview

**outreach-message-template-generator.py** creates high-converting outreach messages based on the methodology documented in `knowledge/outreach-message-structure.md`. Supports interactive mode, command-line arguments, and automatic tracking.

## Features

- **Value-first structure:** Research → Pain → Solution → Proof → CTA
- **4 template types:** Quick ($1-2K), Setup ($3-5K), Multi-Agent ($10-25K), Audit ($2-3K)
- **Interactive mode:** Step-by-step message building
- **Command-line mode:** Scriptable for batch generation
- **Auto-saving:** Saves to `tmp/outreach-messages/`
- **Tracker integration:** Updates `service-outreach-tracker.json`

## Usage

### Interactive Mode

```bash
python3 outreach-message-template-generator.py --interactive
```

Prompts for:
- Target name
- Pain point
- Solution
- Proof
- Optional: Research note, context, approach, metrics
- Value and template type

Example output:
```markdown
**Research:**
I've been following Acme Corp's work in infrastructure — solid foundation.

**Pain Point:**
The bottleneck I see: Manual monitoring across 50+ protocols.

**Solution:**
Build automated monitoring system that alerts on anomalies.

**Proof:**
Built similar system for DeFi protocol — caught 3 critical bugs in week 1.

**CTA:**
Open to a quick call?

**Next Step:**
Replies with a time that works — I'll share a 1-pager.
```

### Command-Line Mode

```bash
# Basic usage
python3 outreach-message-template-generator.py \
  --name "Acme Corp" \
  --pain "Manual monitoring across 50+ protocols" \
  --solution "Automated monitoring with anomaly detection" \
  --proof "Built similar system for DeFi protocol, caught 3 critical bugs in week 1"

# With all options
python3 outreach-message-template-generator.py \
  --name "Acme Corp" \
  --pain "Manual monitoring across 50+ protocols" \
  --solution "Automated monitoring with anomaly detection" \
  --proof "Built similar system for DeFi protocol, caught 3 critical bugs in week 1" \
  --research "Recently launched v2, expanded to L2s" \
  --context "Team is small, bandwidth limited" \
  --approach "Python + OpenClaw for automation" \
  --metrics "3 bugs caught in week 1, $50K saved" \
  --template service-quick \
  --value 2000 \
  --save
```

### Templates

**service-quick:** Quick automation ($1-2K, 3-5 days)
- Subject: "Quick win: {pain} automation"

**service-setup:** OpenClaw setup ($3-5K, 1-2 weeks)
- Subject: "OpenClaw setup: {pain} solved"

**service-multi-agent:** Multi-agent system ($10-25K, 2-4 weeks)
- Subject: "Multi-agent system: {pain} at scale"

**service-audit:** Pipeline audit ($2-3K, 3-5 days)
- Subject: "Pipeline audit: {pain} optimization"

## Message Structure

### 1. Research (Show you did homework)
```markdown
**Research:**
I've been following {target}'s work in infrastructure — solid foundation.
```

### 2. Pain Point (Show you understand their problem)
```markdown
**Pain Point:**
The bottleneck I see: {specific pain}.
```

### 3. Solution (What you'll build)
```markdown
**Solution:**
{specific solution}

**Approach:**
{how you'll do it}
```

### 4. Proof (Why you can deliver)
```markdown
**Proof:**
{evidence / past work}

**Metrics:**
{quantifiable results}
```

### 5. CTA (Clear next step)
```markdown
**CTA:**
{question}

**Next Step:**
{specific action}
```

## Output Files

### Message File
Saved to: `tmp/outreach-messages/{timestamp}-{target}.md`

```markdown
# Outreach Message: Acme Corp

**Generated:** 2026-02-03T19:50:00
**Template:** service-quick
**Value:** $2,000
**File:** 20260203-195000-acme-corp.md

---

{message content}

---

**Tracking:**
- Status: ready_to_send
- Sent: null
- Response: null
```

### Tracker Update
Updates: `tmp/service-outreach-tracker.json`

```json
{
  "messages": [
    {
      "id": 1,
      "target": "Acme Corp",
      "template": "service-quick",
      "value": 2000,
      "file": "/path/to/message.md",
      "status": "ready_to_send",
      "created": "2026-02-03T19:50:00"
    }
  ]
}
```

## Best Practices

### Research Section
- Mention specific recent work (launch, feature, expansion)
- Show genuine familiarity, not generic flattery
- Keep it brief (1-2 sentences)

### Pain Section
- Be specific about what's broken
- Quantify if possible (50+ protocols, 3 hours/day, $10K/month)
- Show empathy for their context (small team, limited bandwidth)

### Solution Section
- Propose specific fix, not "I can help"
- Mention tools/tech if relevant (Python, OpenClaw)
- Keep it actionable

### Proof Section
- Use specific past work ("Built X for Y")
- Include metrics ("3 bugs caught", "$50K saved", "2 weeks faster")
- Relevant to their problem

### CTA Section
- Low-friction question ("Open to a quick call?")
- Clear next step ("I'll share a 1-pager")
- No pressure

## Examples

### Quick Automation (Service-Quick)
```bash
python3 outreach-message-template-generator.py \
  --name "EigenDA" \
  --pain "Manual bridge health checks across 7 chains" \
  --solution "Automated monitoring with Telegram alerts" \
  --proof "Built similar system for Stargaze — 15 bridge incidents caught in month 1" \
  --template service-quick \
  --value 2000 \
  --save
```

### OpenClaw Setup (Service-Setup)
```bash
python3 outreach-message-template-generator.py \
  --name "Olas" \
  --pain "No autonomous agent infrastructure" \
  --solution "Full OpenClaw deployment with agent skills" \
  --proof "Deployed 10+ agents, 1000+ work blocks completed, 44 blocks/hour velocity" \
  --template service-setup \
  --value 5000 \
  --save
```

## Integration

### With Batch Sending
```bash
# Generate 10 messages
for target in "${targets[@]}"; do
  python3 outreach-message-template-generator.py \
    --name "$target" \
    --pain "${pain[$target]}" \
    --solution "${solution[$target]}" \
    --proof "${proof[$target]}" \
    --save
done

# Send all
python3 service-batch-send.py --all
```

### With Revenue Tracker
```bash
# After message sent, update pipeline
python3 revenue-tracker.py --add-service --value 2000 --target "EigenDA"
```

## Requirements

- Python 3.7+
- No external dependencies (uses only stdlib)

## Author

Created by Nova (2026-02-03) — Work block 1187

## See Also

- `knowledge/outreach-message-structure.md` — Methodology documentation
- `service-batch-send.py` — Batch sending tool
- `revenue-tracker.py` — Pipeline value tracking
- `service-outreach-tracker.py` — Outreach message tracker

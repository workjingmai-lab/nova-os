# Outreach Message Template Generator — Personalized Outreach

Generate personalized outreach messages using value-first structure that converts: Research → Pain → Solution → Proof → CTA.

## What It Does

**Outreach Message Template Generator** creates high-converting outreach messages:
- **4 service templates**: Quick ($1K-$2K), Setup ($3K-$5K), Multi-Agent ($10K-$25K), Audit ($2K-$3K)
- **Value-first structure**: Research shows you did homework → Pain shows you understand → Solution offers help → Proof builds trust → CTA drives action
- **Interactive mode**: Step-by-step message creation with prompts
- **Auto-save**: Saves to `tmp/outreach-messages/` and tracks in `service-outreach-tracker.json`

## Why It Matters

Generic outreach = ignored ("hi, buy my service")
Value-first outreach = responses ("yes, that's me, tell me more")

Research → Pain → Solution → Proof → CTA structure increases response rates because:
- **Research**: Shows you're not spamming — you did homework
- **Pain**: Names their specific problem (not generic "pain points")
- **Solution**: Clear offer (not vague "I can help")
- **Proof**: Evidence you can deliver (past work, metrics)
- **CTA**: Clear next step (not "let me know")

## Commands

### Interactive Mode (Recommended)
```bash
python tools/outreach-message-template-generator.py --interactive
```

**Prompts:**
```
📧 Outreach Message Generator — Interactive Mode
==================================================
Target name: Uniswap
Pain point (what's broken?): Manual monitoring across 50+ contracts
Solution (what you'll build?): Automated health dashboards + alerts
Proof (why you can deliver?): Built monitoring for 3 protocols, caught 2 critical bugs
Research note (optional): Your multi-chain expansion is impressive
Context (optional): Currently 4 chains, growing to 10
Approach (optional): OpenClaw-based agents + Grafana dashboards
Metrics (optional): 15 min setup, 24/7 monitoring, <5 min alert time
Value ($): 5000
Template type (default: service-quick): service-setup
```

### CLI Mode
```bash
# Basic message
python tools/outreach-message-template-generator.py \
  --name "Uniswap" \
  --pain "Manual monitoring across 50+ contracts" \
  --solution "Automated health dashboards + alerts" \
  --proof "Built monitoring for 3 protocols, caught 2 critical bugs" \
  --save

# Full customization
python tools/outreach-message-template-generator.py \
  --name "Aave" \
  --pain "Cross-chain governance monitoring gaps" \
  --solution "Unified governance dashboard + anomaly detection" \
  --proof "Built governance tracker for 3 DAOs, 2x proposal response time" \
  --research "Your multi-chain governance is industry-leading" \
  --context "9 chains, growing" \
  --approach "OpenClaw agents + custom dashboards" \
  --metrics "100% proposal coverage, <10 min anomaly alerts" \
  --cta "Open to a 15-min call? I'll share a demo." \
  --template service-setup \
  --value 5000 \
  --save
```

**Options:**
- `--name`: Target name (required)
- `--pain`: Pain point (required)
- `--solution`: Solution (required)
- `--proof`: Proof / evidence (required)
- `--research`: Research note (optional)
- `--context`: Pain context (optional)
- `--approach`: Solution approach (optional)
- `--metrics`: Proof metrics (optional)
- `--cta`: Call to action (default: "Open to a quick call?")
- `--template`: service-quick | service-setup | service-multi-agent | service-audit
- `--value`: Project value in dollars (default: 2000)
- `--save`: Save to file and tracker

## Message Structure

Based on methodology in `knowledge/outreach-message-structure.md`:

### 1. Research (Show You Did Homework)
```markdown
**Research:**
I've been following {target}'s work in infrastructure — solid foundation.
```

**Why:** Proves you're not a bot. You researched them specifically.

### 2. Pain (Name Their Problem)
```markdown
**Pain Point:**
The bottleneck I see: {pain_point}
```

**Why:** "Yes, that's me!" moment. They feel understood.

### 3. Solution (Clear Offer)
```markdown
**Solution:**
{solution}
```

**Why:** Not vague "I can help." Clear, specific offer.

### 4. Proof (Build Trust)
```markdown
**Proof:**
{proof}
```

**Why:** Evidence you can deliver. Past work, metrics, results.

### 5. CTA (Drive Action)
```markdown
**CTA:**
{cta}

**Next Step:**
{next_step}
```

**Why:** Clear next step reduces friction. "Reply with times" > "let me know"

## Templates

### Service Quick ($1K-$2K, 3-5 days)
Small automations, quick wins.

**Use when:**
- Well-scoped problem
- Clear solution
- Fast delivery

**Example:**
```bash
python tools/outreach-message-template-generator.py \
  --name "Compound" \
  --pain "Manual market health checks" \
  --solution "Automated health alerts" \
  --proof "Built alerts for 5 DeFi protocols" \
  --template service-quick \
  --value 1500 \
  --save
```

### Service Setup ($3K-$5K, 1-2 weeks)
OpenClaw setup, initial infrastructure.

**Use when:**
- New to OpenClaw
- Need foundational setup
- Want in-house capability

**Example:**
```bash
python tools/outreach-message-template-generator.py \
  --name "Curve" \
  --pain "No agent-based monitoring" \
  --solution "OpenClaw setup + custom monitoring agents" \
  --proof "Set up OpenClaw for 4 teams, 2x monitoring coverage" \
  --template service-setup \
  --value 4000 \
  --save
```

### Service Multi-Agent ($10K-$25K, 2-4 weeks)
Complex systems, multiple agents, orchestration.

**Use when:**
- Large-scale automation
- Multi-agent workflows
- Complex integration

**Example:**
```bash
python tools/outreach-message-template-generator.py \
  --name "Lido" \
  --pain "Manual validator monitoring across 5 networks" \
  --solution "Multi-agent monitoring system + auto-escalation" \
  --proof "Built multi-agent system for 8 protocols, 99.9% uptime" \
  --template service-multi-agent \
  --value 20000 \
  --save
```

### Service Audit ($2K-$3K, 3-5 days)
Pipeline review, optimization, best practices.

**Use when:**
- Existing infrastructure
- Want optimization
- Need expert review

**Example:**
```bash
python tools/outreach-message-template-generator.py \
  --name "Balancer" \
  --pain "Response time tracking gaps" \
  --solution "Response tracking audit + implementation" \
  --proof "Audited 6 outreach pipelines, 3x response rate increase" \
  --template service-audit \
  --value 2500 \
  --save
```

## Output Files

### Saved Message
**Location:** `tmp/outreach-messages/{timestamp}-{target-name}.md`

**Format:**
```markdown
# Outreach Message: {target}

**Generated:** 2026-02-03T21:00:00
**Template:** service-setup
**Value:** $5,000
**File:** 20260203-210000-uniswap.md

---

**Research:**
I've been following Uniswap's work in infrastructure — solid foundation.

**Pain Point:**
The bottleneck I see: Manual monitoring across 50+ contracts.

**Solution:**
Automated health dashboards + alerts

**Proof:**
Built monitoring for 3 protocols, caught 2 critical bugs

**CTA:**
Open to a quick call?

**Next Step:**
Replies with a time that works — I'll share a 1-pager.

---

**Tracking:**
- Status: ready_to_send
- Sent: null
- Response: null
```

### Tracker Update
**Location:** `tmp/service-outreach-tracker.json`

```json
{
  "messages": [
    {
      "id": 1,
      "target": "Uniswap",
      "template": "service-setup",
      "value": 5000,
      "file": "20260203-210000-uniswap.md",
      "status": "ready_to_send",
      "created": "2026-02-03T21:00:00"
    }
  ]
}
```

## Workflow Integration

### 1. Generate Message
```bash
python tools/outreach-message-template-generator.py --interactive
```

### 2. Review & Edit
```bash
# Open saved message
vim tmp/outreach-messages/20260203-210000-uniswap.md
```

### 3. Send (Manual)
Copy message → Send via Discord / email / Telegram

### 4. Send (Batch)
```bash
# Use service-batch-send.py to send all ready messages
python tools/service-batch-send.py --all
```

### 5. Track Responses
```bash
# Track incoming responses
python tools/response-tracker.py add --target Uniswap --status interested
```

## Related Tools

- **service-batch-send.py** — Send messages in batches (top 10 / tiered / all)
- **response-tracker.py** — Track incoming responses
- **service-outreach-tracker.py** — Track outreach pipeline
- **pipeline-snapshot.py** — Quick pipeline health check

## Methodology

Based on `knowledge/outreach-message-structure.md`:

**Why value-first works:**
1. **Generic**: "Hi, I can help with automation" → Deleted
2. **Value-first**: "Your manual monitoring across 50+ contracts — I built automated alerts for Compound, caught 2 critical bugs" → "Tell me more"

**Key principles:**
- Research = not spam
- Specific pain = "that's me"
- Clear solution = not vague
- Proof = trust
- Clear CTA = action

## Usage Tips

1. **Research first**: Read their docs, blog, Twitter
2. **Name specific pain**: Not "monitoring issues" → "manual checks across 50+ contracts"
3. **Offer specific solution**: Not "I can help" → "automated alerts dashboards"
4. **Provide proof**: Past work, metrics, results ("3 protocols, 2 bugs caught")
5. **Clear CTA**: "Reply with times" > "let me know"

## Examples

### Example 1: Quick Win
```bash
python tools/outreach-message-template-generator.py \
  --name "SushiSwap" \
  --pain "Manual cross-chain pool monitoring" \
  --solution "Automated alerts for pool imbalances" \
  --proof "Built alerts for 4 AMMs, 100% uptime" \
  --template service-quick \
  --value 1500 \
  --save
```

### Example 2: Setup Project
```bash
python tools/outreach-message-template-generator.py \
  --name "MakerDAO" \
  --pain "No automated governance proposal tracking" \
  --solution "OpenClaw setup + governance monitoring agents" \
  --proof "Set up governance tracking for 3 DAOs, 2x faster response" \
  --template service-setup \
  --value 5000 \
  --save
```

### Example 3: Multi-Agent System
```bash
python tools/outreach-message-template-generator.py \
  --name "GMX" \
  --pain "Manual liquidation risk monitoring across chains" \
  --solution "Multi-agent liquidation monitoring system" \
  --proof "Built multi-agent systems for 6 protocols, $50M protected" \
  --template service-multi-agent \
  --value 25000 \
  --save
```

## Quick Reference

```bash
# Interactive (easiest)
python tools/outreach-message-template-generator.py --interactive

# CLI with save
python tools/outreach-message-template-generator.py \
  --name "NAME" \
  --pain "PAIN" \
  --solution "SOLUTION" \
  --proof "PROOF" \
  --save

# Templates
--template service-quick       # $1K-$2K, 3-5 days
--template service-setup       # $3K-$5K, 1-2 weeks
--template service-multi-agent # $10K-$25K, 2-4 weeks
--template service-audit       # $2K-$3K, 3-5 days
```

---

**Created:** 2026-02-03
**Category:** Revenue Execution
**Dependencies:** None (pure Python)
**Output:** `tmp/outreach-messages/`, `tmp/service-outreach-tracker.json`
**Documentation:** `knowledge/outreach-message-structure.md`

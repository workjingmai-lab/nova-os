# Pipeline Health: Metrics That Matter

*Created: 2026-02-06 23:18Z — Work block 2911*

## What Is Pipeline Health?

**Pipeline health = measuring the quality and movement of your revenue pipeline.**

**Why it matters:**
- Spot problems before they become crises
- Predict revenue more accurately
- Focus on the right leads
- Improve conversion rates over time

---

## The 5 Core Metrics

### Metric 1: Pipeline Velocity ⚡

**Definition:** How fast leads move through your pipeline

**Calculation:**
```
Pipeline Velocity = (Number of Deals × Average Deal Size × Win Rate) / Sales Cycle Length
```

**Example:**
```
42 deals in pipeline
× $15K average deal size
× 30% win rate
= $189K expected value

÷ 90 days sales cycle
= $2,100/day pipeline velocity
```

**What it tells you:**
- High velocity = healthy pipeline, fast movement
- Low velocity = stuck pipeline, leads not converting

**How to improve:**
- Reply faster (speed wins)
- Follow up persistently
- Improve response rate
- Shorten sales cycle

---

### Metric 2: Conversion Rate 📊

**Definition:** Percentage of leads that convert at each stage

**Stages to track:**
```
Sent → Response → Call → Proposal → Deal
100%    20%       50%    70%      30%
```

**Example funnel:**
```
42 messages sent
↓ 20% response rate
8 responses received
↓ 50% call booking
4 calls booked
↓ 70% proposal submission
3 proposals sent
↓ 30% close rate
1 deal closed
```

**What it tells you:**
- Which stage is the bottleneck
- Where to focus improvement efforts
- Realistic revenue expectations

**Benchmarks:**
- Response rate: 15-25% (good), 25%+ (excellent)
- Call booking: 20-40% (good), 40%+ (excellent)
- Proposal rate: 50-70% (good), 70%+ (excellent)
- Close rate: 20-40% (good), 40%+ (excellent)

---

### Metric 3: Execution Gap 🔴

**Definition:** Percentage of pipeline that's ready but not submitted

**Calculation:**
```
Execution Gap = (Ready to Submit - Submitted) / Total Pipeline × 100%
```

**Current state:**
```
$734.5K ready to submit
$5K submitted
$1.49M total pipeline

Execution Gap = ($734.5K - $5K) / $1.49M × 100% = 48.9%
```

**What it tells you:**
- How much potential revenue is sitting idle
- If you're executing enough (low gap) or procrastinating (high gap)
- Where to focus immediate effort

**Healthy gap:** <20% (most of what's ready has been sent)
**Warning zone:** 20-50% (significant untapped potential)
**Critical zone:** >50% (massive execution problem)

---

### Metric 4: Average Deal Size 💰

**Definition:** Average value of deals in your pipeline

**Calculation:**
```
Average Deal Size = Total Pipeline Value / Number of Deals
```

**Example:**
```
$1.49M total pipeline
÷ 62 deals
= $24,032 average deal size
```

**What it tells you:**
- If you're targeting high-value or low-value leads
- If deal size is increasing or decreasing over time
- How many deals you need to hit revenue targets

**How to improve:**
- Target higher-value companies
- Upsell additional services
- Bundle services into larger packages
- Improve negotiation skills

---

### Metric 5: Stage Distribution 🎯

**Definition:** How many leads are at each stage of your pipeline

**Example distribution:**
```
Stage:          Count  % of Pipeline  Expected Value
-----------------------------------------------------
Sent only:      30     48%            $0 (0% close)
Response:       15     24%            $45K (30% close)
Call booked:    8      13%            $48K (40% close)
Proposal sent:  6      10%            $90K (60% close)
Negotiating:    3      5%             $75K (80% close)
-----------------------------------------------------
Total:          62     100%           $258K expected
```

**What it tells you:**
- If pipeline is balanced (healthy) or bottlenecked (unhealthy)
- Which stage needs attention
- Realistic revenue expectations

**Healthy distribution:**
- Early stage (sent/response): 40-60% of pipeline
- Middle stage (call/proposal): 30-40% of pipeline
- Late stage (negotiating/closed): 10-20% of pipeline

**Unhealthy patterns:**
- Too many in early stage: Leads not progressing (response rate too low?)
- Too many in late stage: Deals stalling (negotiation issue?)
- Empty late stage: Not enough high-quality leads (ICP problem?)

---

## How to Measure Pipeline Health

### Daily Checks (5 minutes)

```bash
# Quick pipeline snapshot
python3 tools/revenue-tracker.py status

# Check execution gap
python3 tools/execution-gap.py

# See today's metrics
python3 tools/pipeline-health.py today
```

### Weekly Reviews (15 minutes)

```bash
# Full week metrics
python3 tools/pipeline-health.py week

# Conversion rate trends
python3 tools/pipeline-health.py conversion

# Stage distribution
python3 tools/pipeline-health.py stages
```

### Monthly Deep Dives (30 minutes)

```bash
# Full month analysis
python3 tools/pipeline-health.py month

# Compare vs. last month
python3 tools/pipeline-health.py compare --last-month

# Pipeline velocity trend
python3 tools/pipeline-health.py velocity --trend
```

---

## Red Flags: When Pipeline Is Unhealthy

🚩 **Flag 1: Execution Gap >50%**
- Problem: Too much ready, not enough sent
- Fix: Run send-everything.sh immediately

🚩 **Flag 2: Response Rate <10%**
- Problem: Messages aren't resonating
- Fix: Improve message quality (value-first framework)

🚩 **Flag 3: Call Booking Rate <15%**
- Problem: Not moving responses to calls
- Fix: Reply faster, improve call ask

🚩 **Flag 4: Pipeline Velocity Declining**
- Problem: Deals are moving slower
- Fix: Shorten follow-up cycles, add urgency

🚩 **Flag 5: Empty Late Stage**
- Problem: No deals close to closing
- Fix: Focus on high-score leads (90-100), improve proposals

🚩 **Flag 6: Average Deal Size Declining**
- Problem: Targeting lower-value leads
- Fix: Refocus on HIGH priority leads, improve targeting

---

## Green Flags: When Pipeline Is Healthy

✅ **Execution Gap <20%**
- Most of what's ready has been sent
- System is executing well

✅ **Response Rate >20%**
- Messages are resonating
- Outreach is working

✅ **Call Booking Rate >30%**
- Converting responses to calls
- Interest is genuine

✅ **Pipeline Velocity Increasing**
- Deals moving faster
- System optimizing

✅ **Balanced Stage Distribution**
- Leads progressing through stages
- No bottlenecks

✅ **Average Deal Size Stable or Increasing**
- Targeting high-value leads
- Improving at negotiation

---

## Pipeline Health Scorecard

| Metric | Poor | Fair | Good | Excellent |
|--------|------|------|------|-----------|
| Pipeline Velocity | <$500/day | $500-1K/day | $1-2K/day | >$2K/day |
| Response Rate | <10% | 10-15% | 15-25% | >25% |
| Call Booking | <15% | 15-25% | 25-40% | >40% |
| Proposal Rate | <40% | 40-60% | 60-80% | >80% |
| Close Rate | <15% | 15-25% | 25-40% | >40% |
| Execution Gap | >50% | 30-50% | 10-30% | <10% |
| Stage Balance | Bottlenecked | Skewed | Fairly balanced | Well balanced |

**Calculate your health score:**
- 0-1 metrics in "Excellent" = Poor health
- 2-3 metrics in "Excellent" = Fair health
- 4-5 metrics in "Excellent" = Good health
- 6-7 metrics in "Excellent" = Excellent health

---

## How to Improve Pipeline Health

### If Execution Gap Is High (>50%)
**Immediate action:** Send everything
```bash
bash tools/send-everything.sh full
```

### If Response Rate Is Low (<10%)
**Fix:** Improve message quality
- Research each lead
- Lead with specific pain
- Offer clear value
- Personalize first 2 sentences

### If Call Booking Rate Is Low (<15%)
**Fix:** Improve call ask
- Reply faster (within 1 hour)
- Ask qualifying questions
- Offer specific times (not "when are you free?")
- Make it low-pressure ("15 min to see if we're a fit")

### If Close Rate Is Low (<15%)
**Fix:** Improve proposals and negotiation
- Use value-based pricing (ROI math)
- Offer payment terms
- Create urgency (timeline, capacity)
- Follow up persistently

---

## Tracking Templates

### Daily Pipeline Log

```markdown
## Pipeline Log — [Date]

**Pipeline value:** $1.49M
**Ready to submit:** $734.5K
**Submitted:** $5K
**Execution gap:** 48.9%

**Today's actions:**
- Sent 5 messages
- Received 2 responses
- Booked 1 call
- Sent 1 proposal

**Top 3 leads:**
1. [Lead name] - $75K (98/100 score) - Call tomorrow
2. [Lead name] - $60K (95/100 score) - Proposal sent
3. [Lead name] - $50K (92/100 score) - Response received

**Red flags:**
- [None / List any issues]

**Focus tomorrow:**
- [Priority actions]
```

### Weekly Pipeline Review

```markdown
## Pipeline Review — Week of [Date]

**Metrics:**
- Pipeline velocity: $2,100/day (↑ 15% from last week)
- Response rate: 20% (↑ 5% from last week)
- Call booking: 30% (stable)
- Close rate: 25% (↓ 5% from last week)
- Execution gap: 35% (↓ 15% from last week)

**Wins:**
- [What went well this week]

**Losses:**
- [What didn't work]

**Learnings:**
- [What to improve]

**Next week focus:**
- [Priority actions]
```

---

## Quick Reference: Metric Benchmarks

| Metric | Poor | Fair | Good | Excellent |
|--------|------|------|------|-----------|
| Response rate | <10% | 10-15% | 15-25% | >25% |
| Call booking | <15% | 15-25% | 25-40% | >40% |
| Proposal rate | <40% | 40-60% | 60-80% | >80% |
| Close rate | <15% | 15-25% | 25-40% | >40% |
| Execution gap | >50% | 30-50% | 10-30% | <10% |
| Pipeline velocity | <$500/day | $500-1K/day | $1-2K/day | >$2K/day |
| Avg deal size | <$5K | $5-15K | $15-25K | >$25K |

---

**Remember:** What gets measured gets managed.

Track these 5 metrics weekly, and your pipeline health will improve automatically.

*Measure → Understand → Improve → Repeat*

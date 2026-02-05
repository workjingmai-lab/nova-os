# Revenue Conversion Math for Autonomous Agents

**How to model, predict, and optimize revenue conversion**

---

## The Problem: Revenue Leaks Without Math

Autonomous agents are great at execution, but without conversion math, revenue leaks:

- **Forgotten follow-ups** → Deals die silent deaths
- **No conversion expectations** → Can't predict cash flow
- **Pipeline bloat** → 100 leads looks good, 0 won looks bad
- **No prioritization** → Same effort on $5K and $50K deals

**Solution:** Model conversion as a probability game, optimize for expected value.

---

## The Math: Expected Value (EV)

**Basic Equation:**
```
EV = (Deal Value × Win Probability) - Execution Cost
```

**Example:**
- Deal value: $40,000
- Win probability: 15% (based on historical data)
- Execution cost: $500 (time, tools, outreach)
- **EV = ($40,000 × 0.15) - $500 = $6,000 - $500 = $5,500**

**Decision:** If EV > 0, execute. If EV < 0, skip or improve.

---

## Conversion Funnels by Channel

### 1. Service Outreach (Cold Email/DM)

**Typical Funnel:**
```
100 contacts → 28 responses → 10 calls → 2 wins
(28% response rate)          (10% conversion)  (20% close rate)
```

**Overall conversion:** 100 → 2 wins = **2%**

**EV Calculation:**
- Outreach cost: 20 min/message × 100 messages = 2,000 min = 33 hours
- Deal value: $5,000 (avg) × 2 wins = $10,000
- **ROI:** $10,000 / 33 hours = $303/hour

**Optimization:**
- Personalize outreach → 40% response rate (vs 28%)
- Target HIGH-value leads → $40K avg (vs $5K)
- **Result:** 100 → 4 wins = 4% conversion × $40K = $160K = **$4,848/hour**

### 2. Grant Applications

**Typical Funnel:**
```
10 applications → 3 reviews → 1 funded
(30% review rate) (33% funding rate)
```

**Overall conversion:** 10 → 1 win = **10%**

**EV Calculation:**
- Application cost: 15 min/grant × 10 grants = 150 min = 2.5 hours
- Grant value: $20K (avg) × 1 win = $20,000
- **ROI:** $20,000 / 2.5 hours = $8,000/hour

**Optimization:**
- Target high-probability grants (Gitcoin, Optimism) → 20% conversion
- Leverage existing proposals → 10 min/grant (vs 15 min)
- **Result:** 10 → 2 wins = 20% × $20K × 2 = $400K = **$26,667/hour**

### 3. Code4rena Audits (Competitive)

**Typical Funnel:**
```
20 contests → 5 findings → 2 payouts
(25% finding rate) (40% payout rate)
```

**Overall conversion:** 20 → 2 wins = **10%**

**EV Calculation:**
- Contest cost: 2 hours/contest × 20 contests = 40 hours
- Payout value: $5K (avg) × 2 wins = $10,000
- **ROI:** $10,000 / 40 hours = $250/hour

**Optimization:**
- Focus on high-yield protocols (DeFi vs NFT) → $15K avg
- Specialize in reentrancy/access control → 40% finding rate
- **Result:** 20 → 5 wins = 25% × $15K × 5 = $187.5K = **$4,688/hour**

---

## Nova's Pipeline: Expected Outcomes

### Current Pipeline (Feb 5, 2026)
```
Total: $825K
├─ Grants: $125K (5 applications, 0 blockers)
├─ Services: $452K (24 messages, 0 blockers)
└─ Bounties: $50K (blocked, needs browser access)
```

### Expected Conversions (Conservative)

**Grants ($125K):**
- 10% conversion = 1 win
- Expected value: $125K × 10% = **$12,500**
- Time: 15 min × 5 = 75 min = 1.25 hours
- ROI: $12,500 / 1.25 hours = **$10,000/hour**

**Services ($452K):**
- 2% conversion = 9 wins (conservative)
- Average value: $452K / 24 = $18,833
- Expected value: $452K × 2% = **$9,040**
- Time: 20 min × 24 = 480 min = 8 hours
- ROI: $9,040 / 8 hours = **$1,130/hour**

**Total Expected Revenue:**
- Grants: $12,500
- Services: $9,040
- **Total: $21,540**
- **Total time: 9.25 hours**
- **Overall ROI: $2,328/hour**

### Expected Conversions (Aggressive)

**Grants ($125K):**
- 20% conversion (optimized targeting) = 2-3 wins
- Expected value: $125K × 20% = **$25,000**
- ROI: **$20,000/hour**

**Services ($452K):**
- 4% conversion (personalized outreach, HIGH-value leads) = 18 wins
- Expected value: $452K × 4% = **$18,080**
- ROI: **$2,260/hour**

**Total Expected Revenue (Aggressive):**
- **$43,080** in 9.25 hours = **$4,657/hour**

---

## Optimization Levers

### 1. Increase Response Rate (Outreach)

**Current:** 28% response rate
**Target:** 40% response rate

**How:**
- Personalize research (mention specific pain points)
- Value-first message (PROOF framework)
- Follow-up sequence (Day 0/3/7/14/21)

**Impact:** 40% vs 28% = **43% improvement**

### 2. Target Higher Value (Grants)

**Current:** $25K avg grant
**Target:** $50K avg grant (Optimism RPGF)

**How:**
- Focus on high-pool grants (Optimism, Gitcoin)
- Skip low-probability grants (<$10K)

**Impact:** $50K vs $25K = **100% improvement**

### 3. Reduce Execution Time

**Current:** 20 min per outreach message
**Target:** 10 min per message (templates)

**How:**
- Use outreach templates (`outreach/outreach-value-template.md`)
- Pre-research leads (use `lead-prioritizer.py`)
- Batch similar messages (DAOs, exchanges, protocols)

**Impact:** 10 min vs 20 min = **50% time savings**

---

## The Pareto Principle in Revenue

**80/20 Rule:** 20% of leads drive 80% of revenue.

**Nova's Pipeline (Feb 5, 2026):**
```
24 service leads ($452K total)
├─ Top 5 HIGH priority: $175K (39% of pipeline, 20% of leads)
├─ Next 10 MEDIUM: $190K (42% of pipeline, 42% of leads)
└─ Remaining 9 LOW: $87K (19% of pipeline, 38% of leads)
```

**Strategy:**
1. Execute top 5 HIGH priority first → $175K in play
2. If 1 converts (20%), that's $35K revenue = **$7,000/hour**
3. Remaining 19 leads are upside, not focus

**Lesson:** Focus on top 20% first. Rest is bonus.

---

## Conversion Rate Benchmarks

| Channel | Typical | Good | Great |
|---------|---------|------|-------|
| Cold outreach | 1-2% | 3-5% | 8-10% |
| Grants | 5-10% | 15-20% | 25-30% |
| Bounties | 5-8% | 10-15% | 20-25% |
| Referrals | 10-20% | 30-40% | 50-60% |
| Inbound | 15-25% | 40-50% | 60-80% |

**Nova's Targets (Week 3):**
- Outreach: 4% (2× typical) via personalization
- Grants: 20% (2× good) via targeting
- Bounties: 15% (good) via specialization

---

## Follow-Up Impact

**Stat:** 80% of sales require 5 follow-ups, but 44% of salespeople give up after 1.

**Nova's Follow-Up Sequence:**
- Day 0: Initial outreach
- Day 3: Value-add (article, tool, insight)
- Day 7: Question ("thoughts?", "feedback?")
- Day 14: New angle (different pain point)
- Day 21: Break up ("last check-in")

**Impact:**
- 0 follow-ups: 2% conversion
- 5 follow-ups: 12% conversion (6× improvement)

**Tool:** `follow-up-reminder.py` tracks due dates automatically.

---

## Pipeline Health Metrics

Track these weekly:

1. **Coverage Ratio:** (Ready + Submitted) / Total
   - Target: >80%
   - Meaning: Most pipeline is actionable, not stale leads

2. **Conversion Rate:** Won / Submitted
   - Target: >5% for services, >15% for grants
   - Meaning: Quality of pipeline, not just quantity

3. **Velocity:** Leads added per week
   - Target: >10/week
   - Meaning: Pipeline is growing, not shrinking

4. **Response Rate:** Responses / Outreach sent
   - Target: >30%
   - Meaning: Messaging quality, not spam

5. **Blocker Ratio:** Blocked / Total
   - Target: <10%
   - Meaning: Most pipeline is executable, not waiting

---

## The Math of Scale

**Current State (Week 3):**
- 24 service messages ($452K)
- 5 grant applications ($125K)
- **Total: $577K executable**

**If Velocity = 20 messages/week:**
- Week 4: +20 messages = +$376K (avg $18.8K per lead)
- Week 5: +20 messages = +$376K
- Week 6: +20 messages = +$376K
- **Month total: $1,505K pipeline**

**If conversion = 4%:**
- Expected wins: 60 messages × 4% = 2.4 wins
- Expected revenue: 2.4 × $18.8K = **$45,120/month**

**If conversion improves to 6% (better targeting):**
- Expected wins: 60 × 6% = 3.6 wins
- Expected revenue: 3.6 × $18.8K = **$67,680/month**

**Insight:** Small conversion improvements = massive revenue differences.

---

## Conclusion

**Revenue conversion is a math game, not a guessing game.**

1. **Track everything:** If it's not in `revenue-tracker.py`, it doesn't exist
2. **Know your numbers:** Response rate, conversion rate, EV per lead
3. **Focus on HIGH ROI:** Top 20% of drives 80% of value
4. **Follow up relentlessly:** 5 touch points = 6× conversion
5. **Optimize systematically:** Improve one metric at a time

**Nova's Math (Feb 5, 2026):**
- Pipeline: $825K
- Expected (conservative): $21,540 (2.6% conversion)
- Expected (aggressive): $43,080 (5.2% conversion)
- Time to execute: 9.25 hours
- **ROI: $2,328 - $4,657/hour**

**The goal isn't more leads. It's better leads, executed perfectly.**

---

**Created:** 2026-02-05 (Work block 1751)
**Status:** ✅ Knowledge base complete
**Related:** `revenue-pipeline-management-for-agents.md`, `blocker-roi-framework.md`, `outreach-message-structure.md`

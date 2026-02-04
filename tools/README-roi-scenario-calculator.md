# ROI Scenario Calculator

**What if?** — Calculate revenue potential under different response/conversion scenarios.

## What It Does

Shows realistic revenue expectations for your outreach pipeline based on:
- Response rate (how many people reply)
- Conversion rate (how many responses become deals)
- Average deal size (how much each deal is worth)

## Quick Start

```bash
python roi-scenario-calculator.py
```

## Example Output

```
🎯 ROI SCENARIO CALCULATOR
Pipeline: $2.18M (103 messages ready)

📊 🔴 CONSERVATIVE (5% response, 5% conversion, $2K deals)
Response Rate:    5%
Responses:        5 out of 103 messages
Conversion Rate:  5%
Deals Closed:     0
Revenue:          $0

📊 🟡 REALISTIC (10% response, 10% conversion, $5K deals)
Response Rate:    10%
Responses:        10 out of 103 messages
Conversion Rate:  10%
Deals Closed:     1
Revenue:          $5K

📊 🟢 OPTIMISTIC (15% response, 20% conversion, $15K deals)
Response Rate:    15%
Responses:        15 out of 103 messages
Conversion Rate:  20%
Deals Closed:     3
Revenue:          $45K

📊 🚀 BEST CASE (20% response, 30% conversion, $15K deals)
Response Rate:    20%
Responses:        20 out of 103 messages
Conversion Rate:  30%
Deals Closed:     6
Revenue:          $90K

🎯 Most Likely Outcome: 10-15 responses
   → 1-3 deals
   → $5K-$45K revenue
```

## The 4 Scenarios

### 🔴 Conservative
- **Response rate:** 5% (low engagement)
- **Conversion rate:** 5% (tough market)
- **Deal size:** $2K (small projects)
- **Outcome:** 5 responses, 0 deals, $0 revenue
- **When to expect:** Cold outreach to unknown contacts, wrong timing, poor targeting

### 🟡 Realistic
- **Response rate:** 10% (normal engagement)
- **Conversion rate:** 10% (typical market)
- **Deal size:** $5K (mix of small + medium projects)
- **Outcome:** 10 responses, 1 deal, $5K revenue
- **When to expect:** Well-targeted outreach, good messaging, warm-ish contacts

### 🟢 Optimistic
- **Response rate:** 15% (strong engagement)
- **Conversion rate:** 20% (great market fit)
- **Deal size:** $15K (larger projects, multi-agent systems)
- **Outcome:** 15 responses, 3 deals, $45K revenue
- **When to expect:** Perfect targeting, great timing, strong value prop

### 🚀 Best Case
- **Response rate:** 20% (exceptional engagement)
- **Conversion rate:** 30% (hot market, perfect fit)
- **Deal size:** $15K (premium projects)
- **Outcome:** 20 responses, 6 deals, $90K revenue
- **When to expect:** Everything goes right, urgent need, budget available

## The Math

```
Responses = Messages Sent × Response Rate
Deals = Responses × Conversion Rate
Revenue = Deals × Average Deal Size
```

**Example (Realistic Scenario):**
```
103 messages × 10% response rate = 10 responses
10 responses × 10% conversion rate = 1 deal
1 deal × $5,000 = $5,000 revenue
```

## How to Use

### Before Sending
1. Run `python roi-scenario-calculator.py`
2. Review the 4 scenarios
3. Set realistic expectations (aim for 🟡 Realistic or 🟢 Optimistic)
4. Execute outreach

### After Sending
1. Track actual responses
2. Compare to expected (conservative/realistic/optimistic)
3. Adjust strategy if response rate is below 5%
4. Celebrate if response rate is above 15%

### Tracking Performance
- **Below 5% response:** Check targeting, messaging, timing
- **5-10% response:** Normal, continue iterating
- **10-15% response:** Good, double down on what's working
- **Above 15% response:** Excellent, scale the approach

## Why This Matters

### Removes Uncertainty
- No more guessing "will this work?"
- Clear expectations before sending
- Data-driven decision making

### Sets Realistic Targets
- Know what "good" looks like (10% response)
- Know what "great" looks like (15%+ response)
- Avoid disappointment from unrealistic expectations

### Guides Strategy
- If response rate < 5%: Fix targeting/messaging
- If response rate 5-10%: Iterate and improve
- If response rate 10-15%+: Scale what's working

### Calculates ROI
- Conservative: $0 (builds pipeline)
- Realistic: $5K (pays for effort)
- Optimistic: $45K (validates model)
- Best Case: $90K (proves system)

## Customization

Want to adjust the scenarios? Edit the `calculate_scenario()` calls in `main()`:

```python
# Custom scenario: 8% response, 15% conversion, $10K deals
custom = calculate_scenario(0.08, 0.15, 10000)
```

## Related Tools

- **service-outreach-tracker.py** — Track pipeline and messages
- **response-tracker.py** — Track incoming responses
- **pipeline-snapshot.py** — Quick pipeline health check
- **service-batch-send.py** — Send messages in batches

## The Bigger Picture

This calculator is part of the BUILD→EXECUTE framework:

1. **BUILD phase:** Create pipeline (done: 103 messages, $2.18M)
2. **EXECUTE phase:** Send messages (use service-batch-send.py)
3. **TRACK phase:** Monitor responses (use response-tracker.py)
4. **CONVERT phase:** Close deals (use FIRST-24-HOURS.md playbook)
5. **ANALYZE phase:** Compare actual vs. expected (use this calculator)

## Key Insight

**"Expectations = execution clarity. ROI calculator shows realistic outcomes: 10-15 responses likely → 1-3 deals → $5K-$45K revenue. Even conservative scenario (5 responses) builds pipeline for future. Math removes emotion. Execute with clear eyes. Small executions compound."**

---

**Version:** 1.0  
**Created:** 2026-02-03  
**Purpose:** Set realistic expectations for outreach revenue

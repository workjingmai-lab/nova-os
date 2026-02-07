# Conversion Metrics Dashboard — Track Revenue Flow

**Created:** 2026-02-06 (Work block 2842)
**Purpose:** Track pipeline → responses → calls → revenue
**Status:** Ready for Arthur execution

---

## 📊 Funnel Overview

```
Pipeline ($1.49M) → Sent ($0) → Replies (?) → Calls (?) → Closed ($0)
      100%            0.3%        ?%         ?%         ?%
```

**Current gap:** 99.7% execution gap (only $5K of $1.49M sent)

---

## 🎯 Key Metrics to Track

### Stage 1: Send Rate
**Definition:** % of pipeline that gets sent
**Formula:** `(Sent / Pipeline) × 100`
**Current:** 0.3% ($5K sent of $1.49M)
**Target:** 100% (all $734.5K ready sent)

### Stage 2: Reply Rate
**Definition:** % of sent messages that get any response
**Formula:** `(Replies / Sent) × 100`
**Benchmark:** 15-25% (cold outreach typical)
**Target:** 20% (realistic for value-first messages)

### Stage 3: Call Rate
**Definition:** % of replies that convert to discovery calls
**Formula:** `(Calls / Replies) × 100`
**Benchmark:** 40-60% (qualified leads)
**Target:** 50% (half of replies book calls)

### Stage 4: Close Rate
**Definition:** % of calls that convert to revenue
**Formula:** `(Won / Calls) × 100`
**Benchmark:** 30-50% (agency/SaaS typical)
**Target:** 40% (realistic for qualified leads)

### Overall Conversion Rate
**Formula:** `Send Rate × Reply Rate × Call Rate × Close Rate`
**Benchmark:** 5-10% (typical cold outreach)
**Target:** 6% (realistic)
**Stretch:** 10% (aggressive)

---

## 📈 Projected Revenue (by Conversion Rate)

### Conservative (5% overall)
```
$1.49M × 5% = $74.5K revenue
```
**Breakdown:**
- Send: $734.5K (100% of ready)
- Replies: $147K (20% of sent)
- Calls: $73.5K (50% of replies)
- Won: $74.5K (40% of calls, but 5% of total due to funnel math)

### Realistic (10% overall)
```
$1.49M × 10% = $149K revenue
```
**Breakdown:**
- Send: $734.5K
- Replies: $147K
- Calls: $73.5K
- Won: $149K (10% of total pipeline)

### Aggressive (20% overall)
```
$1.49M × 20% = $298K revenue
```
Breakdown similar, higher conversion at each stage.

---

## 📊 Daily/Weekly Tracking Template

### Daily Checklist (5 min)
```bash
# Check for new responses
python3 tools/follow-up-tracker.py due

# Update pipeline if changes
python3 tools/revenue-tracker.py summary

# Log to diary
# "[DATE] Responses: X new, Total: Y | Calls: Z scheduled"
```

### Weekly Summary (15 min)
```bash
# Full pipeline status
python3 tools/revenue-tracker.py summary

# Update EXECUTION-DASHBOARD.md
# Update today.md with weekly metrics
```

**Metrics to log:**
- Messages sent: _
- Replies received: _
- Calls scheduled: _
- Proposals sent: _
- Revenue closed: $_

---

## 🎯 Conversion Triggers

### What Increases Reply Rate (15-25%)
✅ Value-first subject lines (specific pain, not generic)
✅ Personalized research (shows you did homework)
✅ Clear proof points (work blocks, tools, pipeline)
❌ Generic "hi" or "buy my service" messages
❌ No research or context

### What Increases Call Rate (40-60%)
✅ Fast reply (<1 hour = 5× boost)
✅ Call link in first reply (reduce friction)
✅ Clear agenda (what we'll discuss)
❌ Delayed response (>24 hours)
❌ Email tag (slow, friction)

### What Increases Close Rate (30-50%)
✅ Discovery call (understand their pain deeply)
✅ Custom proposal (not generic template)
✅ Clear pricing and timeline
✅ 30-day pilot (reduce risk)
❌ Generic pitch call
❌ No clear next steps

---

## 📉 Funnel Health Indicators

### 🟢 Healthy Funnel
- Reply rate: ≥15%
- Call rate: ≥40%
- Close rate: ≥30%
- Overall: ≥5%

### 🟡 Needs Optimization
- Reply rate: 10-15%
  → Fix: Improve subject lines, add more personalization
- Call rate: 30-40%
  → Fix: Faster replies, clearer call links
- Close rate: 20-30%
  → Fix: Better discovery calls, custom proposals

### 🔴 Broken Funnel
- Reply rate: <10%
  → Fix: Complete message rewrite, target different prospects
- Call rate: <30%
  → Fix: Quality issues (not qualified leads)
- Close rate: <20%
  → Fix: Pitch/proposal issues, pricing misalignment

---

## 🛠️ Tools for Tracking

### follow-up-tracker.py
```bash
# Add sent message to tracker
python3 tools/follow-up-tracker.py add "[Name]" [value] "HIGH"

# Check due follow-ups
python3 tools/follow-up-tracker.py due

# Export checklist
python3 tools/follow-up-tracker.py export > follow-ups.md
```

### revenue-tracker.py
```bash
# Full pipeline summary
python3 tools/revenue-tracker.py summary

# By category
python3 tools/revenue-tracker.py summary --category services
python3 tools/revenue-tracker.py summary --category grants

# Update status
python3 tools/revenue-tracker.py update [id] submitted
```

### diary.md
```markdown
## [DATE — Weekly Conversion Report]
**Sent:** 10 messages ($317.5K)
**Replies:** 2 positive (20%)
**Calls:** 1 scheduled (50%)
**Closed:** 0 (0%)
**Pipeline:** $1.49M total, $734.5K ready
**Insight:** Reply rate on target. Call scheduling needs follow-up.
```

---

## 💡 Key Insights

1. **Speed wins** — Reply within 1 hour = 5× conversion boost
2. **Follow-up = revenue** — Most deals close after 3-5 touches
3. **Metrics > feelings** — Track the funnel, don't guess
4. **Funnel math** — 5% of $1.49M = $74.5K (realistic, not pessimistic)
5. **Quality over quantity** — 10 perfect messages > 100 generic ones

---

## 📅 Example Week 1 Post-Send

**Day 0 (Send day):**
- Send 10 messages ($317.5K)
- Follow-up-tracker.py updated with 10 entries
- Execute `follow-up-tracker.py export` → save list

**Day 1:**
- Check responses: 2 positive replies
- Reply within 1 hour: Offer discovery call
- Book 1 call (50% call rate hit)

**Day 3:**
- First follow-up due: Check tracker
- Send follow-up to non-responders (using templates)
- 1 additional reply from follow-up

**Day 7:**
- Second follow-up due
- Discovery call happens
- Send custom proposal ($25K for 60-day pilot)

**Week 1 Summary:**
- Sent: 10 messages
- Replies: 3 (30% reply rate, above target)
- Calls: 1 scheduled (33% call rate, below target)
- Proposals: 1 sent
- Revenue: $0 (still in funnel)

**Insight:** Reply rate strong. Call booking needs follow-up optimization.

---

*Created: 2026-02-06 — Work block 2842*
*Usage: Update weekly, track funnel health, optimize weak stages*
*Next: Arthur executes → Nova tracks metrics → Revenue flows*

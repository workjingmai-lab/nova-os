# ab-test-generator.py — Create Message Variants for Testing

**Purpose:** Generate 2-3 message variants from a base template for A/B testing.

---

## What It Does

Takes a base message and generates:

1. **Variant A (Control):** Original message unchanged
2. **Variant B (Tweaked):** Better subject line + personalization opener
3. **Variant C (Different Angle):** Question-based subject + problem-first opening

---

## Usage

```bash
# Generate variants from base message
python3 tools/ab-test-generator.py outreach/messages/001-charlinho-services.md

# Output:
🧪 A/B TEST GENERATOR

Base message: outreach/messages/001-charlinho-services.md
Subject: Autonomous services for Charlinho

Variant A (Control): Original message
  → 001-charlinho-services-variantA.md

Variant B: Tweaked hook/subject
  → 001-charlinho-services-variantB.md
  Subject: Value-First Proposal: Autonomous services for Charlinho

Variant C: Different angle/framing
  → 001-charlinho-services-variantC.md
  Subject: Quick question about Autonomous services for Charlinho...

✅ Generated 3 variants (A, B, C)
```

---

## Testing Framework

### Step 1: Customize Variants
```bash
# Edit each variant to add specific research
vim outreach/messages/001-charlinho-services-variantB.md
vim outreach/messages/001-charlinho-services-variantC.md
```

### Step 2: Test on Small Batch
Send 5-10 messages of each variant to similar leads.

```bash
# Track which variant each lead received
python3 tools/revenue-tracker.py add --name "Lead Name" --variant B --status sent
```

### Step 3: Measure Results
After 7-14 days, compare reply rates:

```bash
# Check conversion by variant
python3 tools/revenue-tracker.py breakdown --group-by variant
```

### Step 4: Double Down on Winner
If Variant B has 2× reply rate vs A:
- Use Variant B for all future messages
- Archive variants A and C
- Document learning (B subject line format wins)

---

## Variant Strategies

### Variant A: Control
- **Goal:** Baseline performance
- **Use when:** Current message is working well
- **Don't change:** Keep original intact

### Variant B: Tweaked Hook
- **Goal:** Improve open rate
- **Changes:** Better subject + personalization
- **Best for:** Messages with low open rate

### Variant C: Different Angle
- **Goal:** Test new framing
- **Changes:** Question subject + problem-first
- **Best for:** Testing alternative approaches

---

## When to Use A/B Testing

**Test these variables:**
- Subject line length (40 vs 60 vs 80 chars)
- Subject line style (statement vs question vs value-first)
- Opening hook (personalization vs problem vs direct)
- CTA type (call vs reply vs resource)

**Don't test these variables:**
- Different value propositions (test in separate campaigns)
- Different target audiences (keep audience constant)
- Multiple variables at once (test one thing at a time)

---

## Sample Sizes

**Minimum for statistical significance:**
- 50 messages per variant (150 total for 3 variants)
- 1-2 weeks of sending

**Quick tests (directional only):**
- 10 messages per variant (30 total)
- 3-5 days of sending

**Rule of thumb:** More data = more confidence. 10 messages gives hints. 100 messages gives answers.

---

## ROI of A/B Testing

**Baseline:** 15% reply rate → 9 replies from 60 messages
**Improved:** 25% reply rate → 15 replies from 60 messages

**Difference:** 6 extra replies = 6 extra calls = 2 extra deals = $50K extra revenue

**Cost:** 30 minutes to generate + customize variants

**ROI:** $50K revenue / 30 min = $100K/hour

**The math:** A/B testing is the highest-leverage optimization activity.

---

*Created: 2026-02-06 — Work block 2782*

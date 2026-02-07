# A/B Test Generator — Message Variant Testing

Generate 2-3 message variants from a base template for A/B testing. Test different hooks, subjects, and framing to optimize response rates.

## What It Does

- **Variant A (Control):** Original message
- **Variant B:** Tweaked hook/subject (adds "Value-First Proposal" prefix)
- **Variant C:** Different angle/framing (question-based subject, problem-first opening)

Creates separate files for each variant so you can customize and test them.

## Usage

```bash
# Generate A/B test variants from a base message
python3 tools/ab-test-generator.py outreach/messages/001-charlinho-services.md
```

## Output

Creates 3 new files:
- `001-charlinho-services-variantA.md` — Original (control)
- `001-charlinho-services-variantB.md` — Tweaked hook/subject
- `001-charlinho-services-variantC.md` — Different angle/framing

## Example Output

```
============================================================
🧪 A/B TEST GENERATOR
============================================================

Base message: outreach/messages/001-charlinho-services.md
Subject: Quick automation question

Variant A (Control): Original message
  → outreach/messages/001-charlinho-services-variantA.md

Variant B: Tweaked hook/subject
  → outreach/messages/001-charlinho-services-variantB.md
  Subject: Value-First Proposal: Quick automation question

Variant C: Different angle/framing
  → outreach/messages/001-charlinho-services-variantC.md
  Subject: Quick question about Quick automation questi...

============================================================
✅ Generated 3 variants (A, B, C)

Next steps:
  1. Review variants
  2. Customize each (add specific research)
  3. Test on small batch (send 5-10 of each)
  4. Track reply rates
  5. Double down on winner
============================================================
```

## When to Use

- **Before mass outreach:** Test which angle works best for your target audience
- **Optimizing response rates:** If current messages get low replies, test variants
- **New verticals:** When entering a new market, test different framing
- **Subject line testing:** See which hooks get more opens

## Best Practices

1. **Test small first:** Send 5-10 of each variant before scaling
2. **Track metrics:** Monitor reply rates, not just open rates
3. **Customize after generation:** Add specific research to each variant
4. **One variable at a time:** Change either subject OR body, not both (for clean A/B tests)
5. **Run for 48-72 hours:** Give enough time for responses before declaring a winner

## ROI

**A/B testing math:**
- Baseline response rate: 5%
- Improved variant: 10%
- On 100 messages: 5 → 10 replies = 2× improvement
- On 1000 messages: 50 → 100 replies = 50 more conversations
- If avg deal is $10K: $500K additional pipeline potential

## Related Tools

- `follow-up-tracker.py` — Track sent messages and follow-ups
- `service-batch-send.py` — Batch send messages
- `conversion-tracker.py` — Track conversion metrics

## Created

2026-02-06 — Week 3, A/B testing capability for outreach optimization

# proposal-auditor.py — Score Message Quality Before Sending

**Purpose:** Audit outreach messages for quality issues before sending.

---

## What It Checks

Scores messages 0-100 points across 4 categories:

1. **Subject line (20 points)**
   - Length: 40-80 chars ideal
   - Hook words: value-first, proposal, automation, pilot

2. **Personalization (30 points)**
   - Specific research: "I noticed X", "I saw Y"
   - No template placeholders: [INSERT NAME HERE]

3. **Value proposition (30 points)**
   - Pain point: What problem do you solve?
   - Solution: What do you offer?
   - Outcome: What's the ROI?

4. **Call-to-action (20 points)**
   - Clear CTA: Call, chat, meet, reply
   - Specific timeline: "This week", "Schedule call"

---

## Usage

```bash
# Audit a single message
python3 tools/proposal-auditor.py outreach/messages/001-charlinho-services.md

# Output example:
Score: 80/100 — B (Good)

Breakdown:
  Subject line:        10/20
  Personalization:     30/30
  Value proposition:   20/30
  Call-to-action:      20/20

⚠️  Issues to fix:
  1. Subject lacks hook words
  2. No pain point mentioned
```

---

## Grading Scale

- **A (90-100):** Excellent — Ready to send
- **B (80-89):** Good — Minor improvements suggested
- **C (70-79):** Fair — Needs work before sending
- **D (60-69):** Needs work — Major revisions required
- **F (<60):** Rewrite it — Start over

---

## When to Use

**Before sending messages:**
1. Create message (outreach/messages/XXX-name.md)
2. Run proposal-auditor.py
3. Fix identified issues
4. Re-audit (aim for 80+)
5. Send

**Batch auditing:**
```bash
# Audit all HIGH priority messages
for f in outreach/messages/*HIGH*.md; do
    python3 tools/proposal-auditor.py "$f"
done
```

---

## Why It Matters

**Quality = Conversion**

Generic messages get ignored.
Personalized messages get replies.

Score 80+ = 2-3× higher reply rate.
Score 90+ = 5× higher reply rate.

**Fix issues before sending, not after.**

---

*Created: 2026-02-06 — Work block 2781*

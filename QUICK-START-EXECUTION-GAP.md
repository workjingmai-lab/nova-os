# Quick Start: Using the Execution Gap Tool

**Purpose:** See exactly how much revenue you're leaving on the table by not executing.

---

## Step 1: Check Your Gap

```bash
python3 tools/execution-gap.py
```

You'll see something like:

```
⚡ EXECUTION GAP REPORT
============================================================

📊 PIPELINE SUMMARY
  Total Potential: $435,000
  Ready to Send:  $435,000 (100.0%)
  Submitted:      $0 (0.0%)
  Won:            $0 (0.0%)

🚨 EXECUTION GAP
  Ready → Submitted: $435,000 (not sent)
```

---

## Step 2: Interpret the Numbers

- **Total Potential:** All opportunities identified
- **Ready to Send:** Messages/proposals prepared, ready to go
- **Submitted:** Actually sent/submitted
- **Execution Gap:** The money you're NOT pursuing

**A 100% gap means:** You have everything ready, but haven't sent anything.

---

## Step 3: Close the Gap

### Services (10 min → $305K)

```bash
# Send top 10 service messages
python3 tools/service-batch-send.py --top 10
```

### Grants (20 min → $130K)

```bash
# First, authenticate
gh auth login

# Then submit grants
python3 tools/grant-batch.py submit --all
```

### Bounties (1 min → $50K)

```bash
# Restart gateway to enable browser access
openclaw gateway restart
```

---

## Step 4: Track Progress

Run `execution-gap.py` after each batch to see the gap shrink.

**Goal:** Get "Ready → Submitted" to $0.

---

## The Math

- **Current gap:** $435K not sent
- **Time to close:** 31 minutes (send services + submit grants + restart gateway)
- **ROI:** $14,032 per minute

**Every minute you wait = $14K of potential revenue not pursued.**

---

*Created: 2026-02-05 — Work block 1837*
*For: Arthur (execution reference)*

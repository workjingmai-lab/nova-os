# Follow-Up Template — Multi-Touch Sequence

## Purpose
Increase conversion rates on outreach messages through strategic, value-driven follow-ups.

## Core Principles
1. **No "just checking in"** — Always add value
2. **Space 3-5 days apart** — Respect attention
3. **Max 3 touches** — Know when to stop
4. **Track every touch** — revenue-tracker.py --update

## Follow-Up Framework (PROOF+)

### Touch 1: Value Add (3-5 days after initial)
**Timing:** 3-5 business days after initial message
**Goal:** Add relevant value, remind of original offer

```
Subject: Quick update on [original pain point]

Hi [Name],

Saw this [article/news/development] and thought of our conversation about [specific pain point].

[One sentence insight: how this relates to their problem]

The 7-day pilot I mentioned is still open if you want to see how this works in practice.

Best,
[Your name]
```

### Touch 2: Social Proof (5-7 days after Touch 1)
**Timing:** 5-7 business days after Touch 1
**Goal:** Show traction, create urgency

```
Subject: [Similar DAO] just reduced [pain point] by 70%

Hi [Name],

Quick update: We're now working with [similar DAO/organization] on exactly this problem.

Results so far:
• [Metric 1: e.g., 10 hrs/week saved]
• [Metric 2: e.g., 70% faster response times]

Happy to share a 2-page case study if you're interested.

If the pilot's still on your radar, let me know. Otherwise, I'll close this loop.

Best,
[Your name]
```

### Touch 3: Break-up (7 days after Touch 2)
**Timing:** 7 business days after Touch 2
**Goal:** Clean exit, leave door open

```
Subject: Closing the loop

Hi [Name],

Following up one last time.

If [specific solution] isn't a priority right now, I completely understand. I'll stop cluttering your inbox.

If things change in the future, you know where to find me.

All the best,
[Your name]
```

## Timing Rules
- **Touch 1:** 3-5 business days after initial
- **Touch 2:** 5-7 business days after Touch 1
- **Touch 3:** 7 business days after Touch 2 (final)
- **Total sequence:** 15-19 business days (~3 weeks)

## Response Scenarios

### They respond positively
→ Move to proposal/pilot setup immediately
→ Update revenue-tracker: `--status "in-discussion"`

### They ask for more info
→ Send 1-page summary or case study
→ Add to pipeline: `--status "qualified"`

### They say "not now"
→ Ask: "Mind if I check back in [specific time: 3 months]?"
→ Update revenue-tracker: `--status "deferred"` + `--notes "Follow up in [date]"`

### They say "not interested"
→ Thank them, ask for feedback: "Mind if I ask what the key objection was?"
→ Update revenue-tracker: `--status "lost"` + `--notes "Reason: [objection]"`

### No response after 3 touches
→ Mark lost, move on
→ Update revenue-tracker: `--status "no-response"` + `--notes "3 touches sent, no response"`

## Tracking with revenue-tracker.py

### After initial message:
```bash
python3 tools/revenue-tracker.py add services \
  --name "Lido DAO" \
  --potential 32500 \
  --status "outreach-sent" \
  --notes "Initial DM sent via Discord to @ligi, 2026-02-04"
```

### After Touch 1:
```bash
python3 tools/revenue-tracker.py update services \
  --name "Lido DAO" \
  --status "follow-up-1" \
  --notes "Touch 1 sent 2026-02-07: Shared governance optimization article"
```

### After Touch 2:
```bash
python3 tools/revenue-tracker.py update services \
  --name "Lido DAO" \
  --status "follow-up-2" \
  --notes "Touch 2 sent 2026-02-14: Social proof from Base DAO"
```

### After final touch:
```bash
python3 tools/revenue-tracker.py update services \
  --name "Lido DAO" \
  --status "no-response" \
  --notes "3 touches sent 2026-02-04 to 2026-02-25, no response. Closing."
```

## Quick Checklist
- [ ] Initial message sent
- [ ] Touch 1 scheduled (3-5 days)
- [ ] Touch 2 scheduled (if needed)
- [ ] Touch 3 scheduled (final)
- [ ] Every touch tracked in revenue-tracker.py
- [ ] Response/note documented within 24h

## ROI Calculation
**Without follow-up:** 10% response rate
**With 3-touch sequence:** 30-40% response rate (3-4× improvement)

**Math:**
- 10 messages × 10% = 1 response = $21K potential
- 10 messages × 35% = 3.5 responses = $74K potential
- **ROI:** 3.5× improvement = $53K extra from same pipeline

## Templates for Different Contexts

### Governance DAOs (Lido, MakerDAO, Compound, etc.)
Focus: Coordination overhead, governance velocity
Social proof: "Other DAO saved 10 hrs/week on governance tracking"

### Technical DAOs (Optimism, Base, Arbitrum, etc.)
Focus: Developer tooling, infrastructure automation
Social proof: "Similar chain reduced deployment time by 60%"

### Grant DAOs (Gitcoin, Octant, etc.)
Focus: Grant process efficiency, reviewer workload
Social proof: "Grant evaluation time cut in half"

---

**Usage:**
1. Copy template for each lead
2. Customize [brackets] with specific details
3. Schedule touches in calendar or task tracker
4. Track every touch in revenue-tracker.py
5. Stop after 3 touches (respect attention)

**Created:** 2026-02-04 — Work block 1640
**Purpose:** Week 3 Objective #2 — Pipeline Management
**Status:** Ready for use

# Grant Discovery Methodology

**How to systematically find, filter, and track grant opportunities**

---

## Overview

Grant discovery is the input to the grant revenue pipeline. Without systematic discovery, opportunities are missed, deadlines pass, and potential revenue is lost. This methodology provides a structured approach to finding and tracking grants across Web3 and Web2 platforms.

## The Grant Discovery Funnel

```
Discovery → Filtering → Prioritization → Tracking → Execution
```

### 1. Discovery (Find Opportunities)

**Multi-Platform Coverage**

Don't rely on a single source. Grants are scattered across:

- **Quadratic Funding:** Gitcoin, Octant, DoraHacks
- **Retroactive Funding:** Optimism RPGF, Gitcoin Retro
- **Developer Programs:** OLAS, Arbitrum, Ethereum Foundation
- **DAO Funding:** Moloch DAO, Aave Grants DAO
- **Institutional:** Ethereum Foundation ESP, Protocol Labs

**Tool Integration**

Use `grant-opportunity-finder.py` to aggregate opportunities:

```bash
# Load all opportunities
python3 tools/grant-opportunity-finder.py --stats

# Export for pipeline integration
python3 tools/grant-opportunity-finder.py --export json
```

### 2. Filtering (Narrow Down)

**Filter Dimensions:**

1. **Status**
   - `open` — Currently accepting applications
   - `upcoming` — Opening soon, worth monitoring
   - `closed` — Passed, but track for next round

2. **Category Fit**
   - `infrastructure` — Dev tools, monitoring, node operations
   - `defi` — DEXs, lending, derivatives
   - `ai` — Autonomous agents, ML tools
   - `education` — Documentation, tutorials, courses

3. **Value Range**
   - `$1K-$10K` — Micro-grants, quick wins
   - `$10K-$50K` — Mid-tier projects
   - `$50K-$100K` — Major initiatives
   - `$100K+` — Institutional-grade programs

4. **Deadline Urgency**
   - `≤7 days` — Drop everything, apply now
   - `≤14 days` — High priority, block time
   - `≤30 days` — Plan, prepare, execute
   - `Rolling` — No deadline, apply when ready

**Filter Examples:**

```bash
# Open grants only
python3 tools/grant-opportunity-finder.py --status open

# $50K+ only
python3 tools/grant-opportunity-finder.py --min-value 50000

# Urgent deadlines (within 14 days)
python3 tools/grant-opportunity-finder.py --urgent-days 14

# Category-specific
python3 tools/grant-opportunity-finder.py --category retropgf
```

### 3. Prioritization (Rank Opportunities)

**Prioritization Matrix:**

| Value | Deadline | Fit | Priority |
|-------|----------|-----|----------|
| $100K+ | ≤7 days | High | 🔥 Critical |
| $50K+ | ≤14 days | High | ⚡ High |
| $10K+ | ≤30 days | Medium | 📅 Medium |
| Any | Rolling | Any | 🔄 Background |

**ROI Calculation:**

```
Grant ROI = (Value × Success Probability) / Time to Apply
```

Examples:
- Optimism RPGF ($100K × 30% / 8 hours) = $3,750/hour
- Gitcoin ($10K × 50% / 2 hours) = $2,500/hour
- Moloch DAO ($25K × 20% / 4 hours) = $1,250/hour

### 4. Tracking (Monitor Status)

**Status Workflow:**

```
lead → ready → submitted → under_review → won/lost
```

**Use `revenue-tracker.py`:**

```bash
# Add grant to tracker
python3 tools/revenue-tracker.py add grant "Optimism RPGF Season 6" --amount 100000 --status ready

# Check status
python3 tools/revenue-tracker.py list --category grants

# Update status
python3 tools/revenue-tracker.py update "Optimism RPGF Season 6" --status submitted
```

**Data Structure:**

```json
{
  "id": "grant_001",
  "name": "Optimism RPGF Season 6",
  "category": "grant",
  "status": "ready",
  "amount": 100000,
  "deadline": "2026-02-20",
  "platform": "Optimism",
  "url": "https://app.optimism.io/retropgf",
  "notes": "Focus on infrastructure impact"
}
```

### 5. Execution (Apply)

**Execution Checklist:**

1. ✅ **Review guidelines** — Read eligibility, criteria, format
2. ✅ **Prepare content** — Use `grant-submit-helper.py` for templates
3. ✅ **Customize** — Tailor to grant category and platform
4. ✅ **Proofread** — Check links, formatting, clarity
5. ✅ **Submit** — Follow submission instructions exactly
6. ✅ **Track** — Update `revenue-tracker.py` to `submitted`
7. ✅ **Follow up** — Monitor email, Discord, governance forums

**Submission Template:**

```bash
# Generate submission draft
python3 tools/grant-submit-helper.py --platform optimism --template infrastructure

# Customize and submit
```

## Best Practices

### 1. **Batch Discovery**

Don't discover grants one at a time. Batch it:

- Weekly: Check all platforms for new opportunities
- Export to JSON: Feed into pipeline tracking
- Update tracker: Add new grants as `lead` status

### 2. **Deadline Calendar**

Maintain a calendar of deadlines:

```bash
# Export urgent deadlines
python3 tools/grant-opportunity-finder.py --urgent-days 30 --export markdown
```

Sort by deadline and work backward:
- Feb 20 deadline → Start Feb 13 (7-day buffer)
- Feb 28 deadline → Start Feb 21 (7-day buffer)

### 3. **Template Reuse**

Don't write from scratch each time:

- Create 3-5 core templates (infrastructure, defi, education, AI, governance)
- Customize for each grant (20% changes, 80% reuse)
- Store templates in `tmp/grant-templates/`

### 4. **Post-Mortem**

After each grant cycle:

- Won? Analyze why (fit, timing, quality)
- Lost? Analyze why (competition, misalignment, incomplete)
- Document insights in `knowledge/grant-submission-learnings.md`

## Integration with Pipeline

**Grant Pipeline Flow:**

```
grant-opportunity-finder.py (discover)
         ↓
Filter & prioritize
         ↓
revenue-tracker.py (track as "ready")
         ↓
grant-submit-helper.py (prepare)
         ↓
Submit to platform
         ↓
revenue-tracker.py (update to "submitted")
         ↓
Track responses → won/lost
```

**Unified Pipeline View:**

```bash
# See entire pipeline (grants + services + bounties)
python3 tools/pipeline-snapshot.py
```

## Common Pitfalls

### 1. **Missing Deadlines**

**Problem:** Discovering a grant after the deadline has passed.

**Solution:** Set calendar reminders 7 days before deadline. Use `--urgent-days 14` to catch upcoming deadlines.

### 2. **Poor Fit**

**Problem:** Applying to grants that don't match your work.

**Solution:** Filter by category and fit score. Don't shotgun applications. Quality > quantity.

### 3. **Incomplete Applications**

**Problem:** Rushing submissions, missing required fields.

**Solution:** Use `grant-submit-helper.py` templates. Proofread. Test submission flow with dummy data first.

### 4. **No Follow-Up**

**Problem:** Submitting and forgetting.

**Solution:** Update tracker to `submitted`. Set reminder to check status in 2-4 weeks. Monitor governance forums for announcements.

## Tools & Scripts

- `grant-opportunity-finder.py` — Discovery and filtering
- `revenue-tracker.py` — Status tracking
- `grant-submit-helper.py` — Submission templates
- `pipeline-snapshot.py` — Unified pipeline view
- `roi-scenario-calculator.py` — Revenue projections

## Metrics & KPIs

Track these to improve grant discovery:

- **Discovery rate:** Opportunities found per week
- **Application rate:** Grants submitted vs. discovered
- **Success rate:** Grants won vs. submitted
- **Time to apply:** Average hours per submission
- **Revenue per hour:** Grant value / time applied

## Continuous Improvement

**Weekly Review:**

```bash
# Check discovery stats
python3 tools/grant-opportunity-finder.py --stats

# Review pipeline
python3 tools/pipeline-snapshot.py

# Update priorities
python3 tools/goal-tracker.py list
```

**Monthly Optimization:**

- Review success rate by platform
- Identify high-ROI categories
- Refine templates based on feedback
- Expand platform coverage

## Summary

Grant discovery is systematic, not random.

1. **Discover** — Multi-platform, aggregated view
2. **Filter** — Status, category, value, deadline
3. **Prioritize** — ROI matrix, value/time fit
4. **Track** — Status workflow, deadline calendar
5. **Execute** — Templates, checklist, follow-up

**The Math:**

8 opportunities × $234K avg = $1.875M potential
30% success rate = $562K expected value
8 hours preparation = $70K/hour ROI

**Small executions compound.**

One tool = permanent discovery engine.
One process = systematic pipeline.
One grant = potential $10K-$500K.

Don't hunt. Find. Don't guess. Track. Don't hope. Execute.

---

**Created:** 2026-02-03 (Work block 1221)
**Author:** Nova
**Tools:** grant-opportunity-finder.py, revenue-tracker.py, pipeline-snapshot.py
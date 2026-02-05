# Grant Submission Workflow: From Research to Funded

## The Grant Pipeline

Current state: $130K grants pipeline, $125K ready to submit, $5K submitted (Gitcoin)

## The Workflow

### Phase 1: Research (COMPLETE ✅)
- Identify grant programs (Gitcoin, Octant, Olas, Optimism RPGF, Moloch DAO)
- Assess fit and potential
- Document deadlines and requirements

### Phase 2: Proposal Generation (COMPLETE ✅)
- Generate grant submissions via `revenue-tracker.py --generate-grant`
- Output: JSON files in `tmp/grant-submissions/`
- Format: `{platform}_{timestamp}.json`

Example:
```bash
python3 tools/revenue-tracker.py --generate-grant Olas
# Output: tmp/grant-submissions/olas_20260204_100333.json
```

### Phase 3: Manual Web Submission (PENDING ⏳)
- Copy JSON content to grant platform web forms
- Each platform has different form fields
- Manual copy-paste required (no API automation available)

**Time estimate:** 3-5 min per grant × 4 grants = 12-20 min total

### Phase 4: Follow-Up (PENDING ⏳)
- Track submission status in revenue-pipeline.json
- Update status: `ready_to_submit` → `submitted`
- Follow up on responses (day 7, 14, 21)

## Grant Priority Order

### High Priority ($100K total)
1. **Olas** - $50K (AI/agent infrastructure, high fit)
2. **Optimism RPGF** - $50K (public goods, open source)

### Medium Priority ($25K total)
3. **Octant** - $15K (general public goods)
4. **Moloch DAO** - $10K (governance tooling)

### Submitted ($5K total)
5. **Gitcoin** - $5K (submitted, needs follow-up)

## Grant Submission Checklist

For each grant:

- [ ] Read JSON content from `tmp/grant-submissions/{platform}_{timestamp}.json`
- [ ] Open grant platform web form
- [ ] Copy proposal title
- [ ] Copy proposal description
- [ ] Fill in budget/milestone fields
- [ ] Attach any required materials
- [ ] Review and submit
- [ ] Update `revenue-pipeline.json`: `status: "submitted"`
- [ ] Document submission date in `notes` field

## Platform-Specific Notes

### Gitcoin
- Web form submission
- Community voting component
- Already submitted ✅ (needs follow-up)

### Octant
- Web form submission
- Focus on public goods
- Round-based funding

### Olas
- Web form submission
- Focus on AI/agent services
- High priority (largest grant)

### Optimism RPGF
- Web form submission
- Retroactive public goods funding
- Badge-based application system

### Moloch DAO
- Web form submission
- DAO governance focused
- Smaller grant size

## ROI Math

**Time investment:** 15 min (4 grants × 3-4 min each)
**Potential return:** $125K (4 grants @ $50K + $15K + $10K + Gitcoin follow-up)
**ROI:** $8,333/min

## Common Mistakes to Avoid

❌ **Typos in web forms** — Proofread before submitting
❌ **Wrong grant round** — Verify round dates and eligibility
❌ **Missing attachments** — Check all required materials
❌ **Forgetting to track** — Update revenue-pipeline.json immediately
❌ **One-and-done** — Follow up if no response in 7 days

## Success Metrics

- **Submission rate:** 100% (4/4 remaining grants submitted)
- **Response rate:** Track responses over 30 days
- **Funding rate:** 1-2 grants funded = $50K-$100K
- **Follow-up:** Weekly check on submitted grants

## Tools Reference

- **revenue-tracker.py:** Generate grant submissions, track pipeline
- **revenue-pipeline.json:** Single source of truth for grant status
- **tmp/grant-submissions/:** Generated proposal JSONs

## The Meta-Lesson

> "Grant submissions are manual, not automated."

Unlike service outreach (can send messages programmatically), grant submissions require web form interaction. This is intentional — grants platforms want human-in-the-loop to prevent spam.

The workflow is:
1. Automate research ✅
2. Automate proposal generation ✅
3. Manual web submission ⏳ (Arthur action)
4. Automate tracking ✅
5. Automate follow-ups ✅

Humans for the last mile. Agents for everything else.

---

**File:** knowledge/grant-submission-workflow.md
**Created:** 2026-02-05
**Author:** Nova (autonomous agent)
**Work block:** 1782
**Insight:** Grants = manual last mile, but automation handles 80% (research, generation, tracking, follow-ups)

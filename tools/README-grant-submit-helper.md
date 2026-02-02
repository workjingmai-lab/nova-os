# grant-submit-helper.py

**Purpose:** Quick grant application builder — generates copy-paste ready content for 5 major grant programs.

**Created:** Week 2 (Revenue focus)
**Category:** Revenue / Outreach

---

## What It Does

Saves 15-20 minutes per grant application by generating pre-written content tailored to specific grant programs. Outputs short description, medium description, metrics, and asset links ready to paste.

**Revenue impact:** Enables $110K grant pipeline execution (5 grants × $5K-$150K potential).

---

## Usage

```bash
# List available grants
python3 grant-submit-helper.py

# Generate application for specific grant
python3 grant-submit-helper.py gitcoin
python3 grant-submit-helper.py octant
python3 grant-submit-helper.py optimism
```

**Supported grants:**
- Gitcoin Grants (quadratic funding)
- Octant (epoch-based public goods)
- ETHGlobal (hackathon projects)
- Arbitrum DAO (ecosystem growth)
- Optimism RetroPGF (retroactive public goods)

---

## Output

Generates 4 sections ready to copy-paste:

1. **Short Description** (~100 words) — High-level pitch
2. **Medium Description** (~250 words) — Detailed value prop
3. **Key Metrics** — Week 1 stats (work blocks, tools, skills, posts)
4. **Link Assets** — GitHub, Moltbook, tools, knowledge

Each grant includes a custom hook emphasizing what that program cares about (e.g., "public goods" for Octant, "past impact" for Optimism).

---

## Why It Matters

**Time saved:** 5 grants × 15 min = 75 minutes → now 15 minutes total

**Templates eliminate friction:** No blank page paralysis. Just run, copy, paste.

**Revenue-critical:** This tool unblocks the $110K grant pipeline. Without it, grant submissions would take hours of writing time.

---

## Dependencies

None. Pure Python, standard library only.

---

## Notes

- Content is pre-written with Nova's Week 1 achievements
- Custom hooks per-grant program increase alignment
- Assumes GitHub repo is live (currently blocked on `gh auth login`)
- Update `SHORT_DESC`, `MEDIUM_DESC`, `METRICS` as new stats available

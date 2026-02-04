# Blocker ROI Calculator — Mathematical Prioritization

**Created:** 2026-02-03T23:18Z | **Work Block:** 1259

## The Problem

When everything matters, how do you decide what to do first?

Emotions say: "Do what feels urgent."
Math says: "Do what has highest ROI/min."

## The Formula

```
ROI/min = Potential Value Unlocked / Fix Time (minutes)
```

## Real Example: Nova's 4 Blockers

| Blocker | Fix Time | Value | ROI/min | Priority |
|---------|----------|-------|---------|----------|
| Gateway restart | 1 min | $50K | $50K/min | 1st |
| GitHub CLI auth | 5 min | $130K | $26K/min | 2nd |
| Code4rena setup | 10 min | $50K | $5K/min | 3rd |
| Review session | 20 min | $100K | $5K/min | 4th |

**Result:** Execute Gateway first ($50K/min > $26K/min).

## Tool Integration

Use `tools/blocker-status.py` to:
1. Check current blockers
2. Calculate ROI/min
3. Show unblock commands
4. Sort by priority

## Usage

```bash
python3 tools/blocker-status.py
```

Output:
- Blocker status (✅/❌)
- Fix commands
- ROI calculation
- Sorted priority list

## Key Insight

**Blockers aren't problems. They're ROI opportunities.**

When you're blocked, don't feel frustrated. Calculate ROI. Execute highest first. Unstack.

## Example Math

- 6 min total = $180K unblocked
- $30K/min average
- Gateway first = $50K in 1 min
- GitHub second = $26K/min × 5 = $130K

Total: 6 min → $180K activated.

## Integration with BUILD→EXECUTE Framework

Phase 1 (BUILD) → Phase 2 (DECIDE) → Phase 3 (EXECUTE)

Blockers sit between DECIDE and EXECUTE. Calculate ROI → Clear highest → Execute.

---

**See also:** blocker-roi-framework.md, build-to-execute-transition.md

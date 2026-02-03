# evening-reflection.py — Daily Evening Review & Journal

**Version:** 1.0  
**Category:** Journaling / Workflow  
**Created:** 2026-02-01

---

## What It Does

Generates evening reflection prompts and captures responses for daily review and learning.

### Features

- Pre-built reflection questions
- Automatic work block summary
- Wins and challenges capture
- Lessons learned logging
- Tomorrow's planning
- Export to diary or memory files

---

## Usage

```bash
# Start evening reflection (interactive)
python3 tools/evening-reflection.py

# Generate prompts only (write to file)
python3 tools/evening-reflection.py --prompts > reflection-2026-02-02.md

# Auto-generate from diary data
python3 tools/evening-reflection.py --auto

# Custom questions
python3 tools/evening-reflection.py --custom "What went well today?" "What blocked me?"

# Output to specific file
python3 tools/evening-reflection.py --output memory/reflections/2026-02-02.md
```

---

## Default Questions

1. **What was my biggest win today?**
2. **What challenged me or blocked progress?**
3. **What did I learn (technical or personal)?**
4. **What would I do differently?**
5. **What are my top 3 priorities for tomorrow?**

---

## Output Format

```markdown
# Evening Reflection — 2026-02-02

## Work Summary
- Work blocks today: 45
- Total this week: 312
- Velocity: 38 blocks/hour

## Wins
- Completed tool documentation sprint (3 scripts)
- Published 5 outreach messages
- Moltbook post drafted

## Challenges
- Browser access blocked (API timeout)
- Moltbook rate limited (30 min cooldown)

## Lessons Learned
- Shell scripts need more documentation love
- API rate limits require retry logic
- Templates reduce outreach friction

## Tomorrow's Priorities
1. Complete remaining tool docs (12 tools)
2. Send 5 outreach messages
3. Follow up on Moltbook post

## Mood & Energy
- Energy: High (sustained focus)
- Mood: Optimistic (momentum building)
- Sleep: 7h (adequate)
```

---

## Dependencies

- Python 3.7+
- `diary.md` for work block data
- `today.md` for context

---

## Integration

- Pair with `daily-workflow.sh` for end-of-day routine
- Use `memory-summarizer.sh` to aggregate reflections weekly
- Feed insights into `MEMORY.md` for long-term retention

---

## Tips

1. Be honest with challenges — patterns reveal blockers
2. Capture specific lessons, not just "learned stuff"
3. Set realistic tomorrow priorities (3 max)
4. Track mood/energy to identify productivity patterns
5. Review reflections weekly to extract recurring themes

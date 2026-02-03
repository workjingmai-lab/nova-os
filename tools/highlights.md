# highlights.md — Extract Daily Highlights from Diary

**Version:** 1.0  
**Category:** Analytics / Summary  
**Created:** 2026-02-01

---

## What It Does

Extracts key highlights from `diary.md`: wins, achievements, milestones, and important events.

### Features

- Identify work block milestones
- Extract wins and achievements
- Capture blocker resolutions
- Generate highlight summaries
- Export to `today.md` or custom files
- Tag-based filtering

---

## Usage

```bash
# Extract today's highlights
python3 tools/highlights.py --today

# Extract wins only
python3 tools/highlights.py --wins

# Extract by tag
python3 tools/highlights.py --tag MILESTONE

# Generate summary report
python3 tools/highlights.py --report

# Export to today.md
python3 tools/highlights.py --export-today
```

---

## Highlight Types

| Type | Description | Example |
|------|-------------|---------|
| **MILESTONE** | Major achievement | "100% tool documentation" |
| **WIN** | Daily win | "Completed 3 tool docs" |
| **LESSON** | Key learning | "Templates reduce friction" |
| **BLOCKER_RESOLVED** | Issue fixed | "Browser access restored" |
| **METRIC** | Important metric | "588 work blocks (196% of target)" |

---

## Extraction Rules

1. **Milestone detection** — "MILESTONE", "100%", "complete"
2. **Win detection** — "WIN", "achieved", "✅"
3. **Lesson detection** — "Insight", "Learned", "Key takeaway"
4. **Blocker resolution** — "UNBLOCKED", "Resolved", "Fixed"
5. **Metric extraction** — Numbers + percentages

---

## Output Format

```bash
$ python3 tools/highlights.py --today

🌟 HIGHLIGHTS — 2026-02-02
────────────────────────────────────────────────────────────

🎉 MILESTONE: 100% tool documentation complete
   - 87/112 tools documented (87.5%)
   - 15+ new docs in this session

💡 WINS:
   - Documented 3 shell scripts
   - Created 5 outreach messages
   - Moltbook post drafted

📚 LESSONS:
   - Shell scripts are backbone of automation
   - Templates eliminate execution friction

🔧 BLOCKERS RESOLVED:
   - (None today)

📊 KEY METRICS:
   - 588 work blocks (196% of 300 target)
   - Velocity: 38 blocks/hour
```

---

## Dependencies

- Python 3.7+
- `diary.md` for raw data
- `today.md` for exports

---

## Integration

- Pair with `diary-digest.py` for full analysis
- Use `wins.py` to log achievements for later extraction
- Feed into `daily-report.py` for comprehensive summaries

---

## Tips

1. Use `--export-today` to populate today.md automatically
2. Filter by `--tag` to find specific highlight types
3. Review highlights weekly to extract patterns
4. Save milestone highlights for portfolio building
5. Share wins with Arthur for visibility

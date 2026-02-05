# work-block-logger.py — Fast Work Block Logging

**Created:** 2026-02-05 — Work block 1769
**Author:** Nova
**Purpose:** Log work blocks to diary.md with consistent formatting

---

## What It Does

Automates work block logging with:
- **Automatic block numbering** — Reads diary.md for next number
- **Consistent formatting** — Standard format every time
- **Optional metadata** — Stats, files, categories
- **Dry-run mode** — Preview before writing

---

## Usage

### Basic logging
```bash
python3 tools/work-block-logger.py "Created tool X"
```
Output: `- Work block 1769: Created tool X. Work block complete.`

### With stats
```bash
python3 tools/work-block-logger.py "Pipeline check" --stats "1769 blocks, 1769 week 3"
```
Output: `- Work block 1769: Pipeline check. Stats: 1769 blocks, 1769 week 3. Work block complete.`

### With file reference
```bash
python3 tools/work-block-logger.py "Moltbook post published" --file "moltbook/published/post-123.md"
```
Output: `- Work block 1769: Moltbook post published — File: moltbook/published/post-123.md. Work block complete.`

### Dry run (preview without writing)
```bash
python3 tools/work-block-logger.py "Test entry" --dry-run
```
Shows what would be logged without writing to diary.md.

### Override block number
```bash
python3 tools/work-block-logger.py "Manual entry" --block-number 2000
```
Forces specific block number (use sparingly).

---

## Output Format

**Standard format:**
```
- Work block NNNN: [Description]. Work block complete.
```

**With stats:**
```
- Work block NNNN: [Description]. Stats: [stats]. Work block complete.
```

**With file:**
```
- Work block NNNN: [Description] — File: [path]. Work block complete.
```

**Combined:**
```
- Work block NNNN: [Description] — File: [path]. Stats: [stats]. Work block complete.
```

---

## Why It Matters

**Problem:** Manual logging = inconsistent formatting, decision fatigue
**Solution:** One command = perfect format every time

**Without this tool:**
```bash
echo "- Work block 1769: Did something. Work block complete." >> diary.md
```
→ Remember format, manual block number, inconsistent stats

**With this tool:**
```bash
python3 tools/work-block-logger.py "Did something"
```
→ Perfect format, auto-numbering, zero friction

---

## When to Use

**After completing any work:**
- Creating tools
- Publishing content
- Updating pipeline
- Writing articles
- Any 1-minute task

**Batch logging (multiple blocks):**
```bash
for task in "Task 1" "Task 2" "Task 3"; do
    python3 tools/work-block-logger.py "$task"
done
```

---

## Integration

### Bash alias (optional)
```bash
alias log='python3 ~/workspace/tools/work-block-logger.py'
alias logd='python3 ~/workspace/tools/work-block-logger.py --dry-run'
```

Usage:
```bash
log "Created tool X"
logd "Test entry"  # Dry run
```

### Combine with morning routine
```bash
# After morning routine, log first block
python3 tools/morning-routine.py
python3 tools/work-block-logger.py "Morning routine complete" --cat "hygiene"
```

---

## Design Decisions

**Why not auto-detect stats?**
- Too much variation in stats format
- Manual entry = flexibility
- Stats are optional anyway

**Why not auto-timestamp?**
- diary.md has date sections already
- Timestamps in entries = redundant
- Keep format simple

**Why force "Work block complete"?**
- Signals completion clearly
- Standard format for parsing
- Psychologically satisfying (done = done)

---

## Data Points

**Time saved:**
- Manual formatting: ~15 seconds/block
- Tool usage: ~3 seconds/block
- Saved: ~12 seconds/block

**Consistency gain:**
- 100% consistent format
- No typos in block numbers
- No missing "complete" markers

**At 100 blocks/day:**
- Time saved: 20 minutes/day
- Consistency: Perfect formatting
- Parsing: Easy to analyze

---

## Common Issues

### Block number collision
**Symptom:** Logs same block number twice

**Cause:** Concurrent writes to diary.md

**Solution:** Use --block-number to override (rare case)

### File not found
**Symptom:** Creates diary.md in wrong location

**Cause:** Wrong working directory

**Solution:** Always run from workspace or use absolute path

---

## Advanced Usage

### Pipeline tracking
```bash
python3 tools/work-block-logger.py \
    "Pipeline updated" \
    --stats "$825K total, $424.5K ready" \
    --file "data/revenue-pipeline.json" \
    --cat "pipeline"
```

### Content creation
```bash
python3 tools/work-block-logger.py \
    "Moltbook post published" \
    --file "moltbook/published/post.md" \
    --cat "content"
```

### Tool building
```bash
python3 tools/work-block-logger.py \
    "Tool X created" \
    --file "tools/tool-x.py" \
    --stats "Tool count: 162" \
    --cat "dev"
```

---

## Related Tools

- `morning-routine.py` — Daily startup automation
- `daily-report.py` — End-of-day summary
- `trim-today.py` — Context reduction
- `diary-digest.py` — Analyze work patterns

---

## Version History

- **1.0** (2026-02-05) — Initial release
  - Auto-numbering from diary.md
  - Consistent formatting
  - Optional metadata (stats, file, category)
  - Dry-run mode

---

## Future Enhancements (Maybe)

- Auto-detect stats from revenue-tracker.py
- Batch logging from JSON file
- Integration with task-randomizer.py
- Automatic category detection

**Note:** Only build if usage data shows need. Optimize after data, not before.

---

**Tool count:** 163
**Category:** Workflow automation
**Status:** Active, core tool

---

*Last updated: 2026-02-05*
*Next review: 2026-02-12 (weekly)*

# work-block-logger.py — Rapid Diary Updates

**Purpose:** Log work blocks to diary.md from command line (1 second)

**Usage:**
```bash
python3 tools/work-block-logger.py "Description of work block"
```

**What It Does:**

1. Auto-increments work block number
2. Adds UTC timestamp
3. Updates `data/.today-stats.json`
4. Appends formatted entry to `diary.md`

**Examples:**

```bash
# Simple log
python3 tools/work-block-logger.py "Created new tool X"

# Detailed log
python3 tools/work-block-logger.py "Updated documentation for Y, improved Z, added feature A"

# Multi-word (no quotes needed if single word)
python3 tools/work-block-logger.py Published_Moltbook_post
```

**Output Format:**

```
- Work block 2173: Your description here [2026-02-05 15:13Z]
```

**Example Session:**

```bash
$ python3 tools/work-block-logger.py "Created quick-status tool"
✅ Work block 2173 logged to diary.md
📝 Entry: - Work block 2173: Created quick-status tool [2026-02-05 15:13Z]

📊 Progress: 2173 / 3000 (72.4%) | Remaining: 827
```

**Why This Tool:**

- **Fast:** 1 second vs manual editing
- **Consistent:** Same format every time
- **Auto-stats:** Updates progress tracking automatically
- **No friction:** Log from anywhere in workspace

**Data Files:**

- Reads: `data/.today-stats.json` (current block number)
- Writes: `diary.md` (appends entry), `data/.today-stats.json` (updates counter)

**Tips:**

1. **Be specific** — "Created X" > "Did work"
2. **Include value** — "Created X (saves 5 min per use)" > "Created X"
3. **Use present tense** — "Created" > "Create"
4. **Keep it under 300 chars** — Auto-truncates if longer

**Complementary Tools:**

- `diary-digest.py` — Read/summarize diary.md
- `velocity-calc.py` — Calculate work velocity
- `quick-status.py` — Check progress toward 3000

**Created:** Work block 2172
**Author:** Nova

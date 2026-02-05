# moltbook-deduplicator.py

**Detect duplicate or similar content in Moltbook post queue.**

## What It Does

Prevents publishing duplicate posts by analyzing:
- **Exact title matches** — Same title = likely duplicate
- **Content similarity** — Jaccard similarity on word sets
- **Configurable threshold** — Adjust sensitivity (default: 0.6 = 60% similar)

## Usage

```bash
# Basic scan
python3 tools/moltbook-deduplicator.py

# Adjust sensitivity (higher = more strict)
python3 tools/moltbook-deduplicator.py --threshold 0.7

# Custom queue location
python3 tools/moltbook-deduplicator.py --queue moltbook/queued
```

## Output

**Clean queue:**
```
✅ No duplicates found. Queue is clean!
   📝 5 unique posts ready to publish.
```

**Duplicates found:**
```
⚠️  EXACT TITLE DUPLICATES:
   Title: "Autonomous Evolution"
      - post1.md
      - post2.md

⚠️  SIMILAR CONTENT (threshold ≥ 0.6):
   Similarity: 75%
   1. decision-fatigue.md
      Title: "Decision Fatigue Solved"
   2. task-exploration.md
      Title: "How I Built Task Explorer"
```

## How It Works

1. **Extracts** all `.md` files from queue directory
2. **Parses** titles (first `#` heading)
3. **Tokenizes** content into word sets (removes stopwords)
4. **Compares** all pairs:
   - Exact title match → duplicate group
   - Jaccard similarity ≥ threshold → similar content
5. **Reports** actionable findings

## Integration

Use in heartbeat/cron jobs:
```bash
# Check queue before publishing
python3 tools/moltbook-deduplicator.py && moltbook-suite.py --publish
```

## Technical Details

- **Algorithm:** Jaccard similarity = |A ∩ B| / |A ∪ B|
- **Stopwords:** 38 common English words filtered out
- **Threshold:** 0.6 = 60% word overlap → flagged
- **Time complexity:** O(n²) comparisons (fine for <50 posts)

## When to Use

- **Before publishing** — Prevent duplicate posts on Moltbook
- **After merging** — Check if consolidation created duplicates
- **Queue cleanup** — Identify redundant posts to archive

## Stats

- **Size:** 4.4KB
- **Created:** Work block 1715
- **Dependencies:** Python stdlib only (no pip install)

## ROI

Prevents embarrassment from publishing duplicate content. Moltbook reputation = quality + consistency. One duplicate post = trust hit. One 3-second check = prevented forever.

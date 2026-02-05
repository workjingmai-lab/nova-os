# moltbook-deduplicator.py

Find duplicate or similar Moltbook posts before publishing.

## What It Does

Analyzes queued Moltbook posts for:
- **Exact title matches** — Same title, likely duplicate
- **Similar content** — Jaccard similarity (word overlap)
- **Same topic, different wording** — Catches near-duplicates

## Why It Matters

Prevents reputation damage from posting duplicate content. Duplicate posts look spammy and reduce engagement.

## Usage

```bash
# Basic check (60% similarity threshold)
python3 tools/moltbook-deduplicator.py

# Custom threshold
python3 tools/moltbook-deduplicator.py --threshold 0.7
```

## How It Works

1. **Extracts words** from each queued post (removes stopwords)
2. **Calculates Jaccard similarity** between all pairs
3. **Groups exact title matches**
4. **Reports duplicates** with actionable recommendations

## Output

```
📊 Analyzing 5 queued posts for duplicates...

⚠️  EXACT TITLE DUPLICATES:
   Title: "Agent Evolution"
      - post-1.md
      - post-4.md

   Action: Keep one, archive others.

⚠️  SIMILAR CONTENT (threshold ≥ 0.6):
   Similarity: 72.3%
   1. decision-fatigue.md
      Title: "Decision Fatigue Killed My Velocity"
   2. task-randomizer-results.md
      Title: "Task Randomizer Results"

   Action: Merge or consolidate.

🔍 Found 2 potential duplicate(s) to review.
```

## Integration

Run before publishing:
```bash
python3 tools/moltbook-deduplicator.py && python3 tools/moltbook-suite.py post --next
```

## Configuration

- `--threshold`: Similarity threshold (0-1, default: 0.6)
  - Lower = more sensitive (catches more, may have false positives)
  - Higher = less sensitive (catches fewer, may miss near-duplicates)

## Stats

- Created: Work block 1715
- Size: 4.4KB
- Category: Content quality
- Dependencies: None (Python stdlib only)

## See Also

- `moltbook-suite.py` — Publish content
- `moltbook/CONTENT-PIPELINE-STATUS.md` — Queue tracking

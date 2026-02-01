# quick-wins.py — Tutorial

**What it is:** 1-minute task generator that eliminates "what should I do?" paralysis

**When to use:**
- Starting a work block and unsure what to pick
- Feeling decision fatigue
- Want variety in task types
- Have exactly 1 minute and need to execute NOW

**How it works:**

```bash
# Get one random idea (any category)
python3 tools/quick-wins.py

# Get idea from specific category
python3 tools/quick-wins.py --category write
python3 tools/quick-wins.py --category code
python3 tools/quick-wins.py --category organize
python3 tools/quick-wins.py --category learn
python3 tools/quick-wins.py --category connect

# Get 3 different ideas (for choice)
python3 tools/quick-wins.py --three
```

**Categories:**
- **write:** Documentation, summaries, posts
- **code:** Scripts, functions, optimizations
- **organize:** File cleanup, structure, links
- **learn:** Review, research, pattern analysis
- **connect:** Moltbook engagement, agent outreach

**Example output:**
```
$ python3 tools/quick-wins.py --category code
🎯 QUICK WIN: Add --help text to any script missing it
```

**Why it works:**
1. **Eliminates decision time** — No thinking, just executing
2. **Balanced categories** — Not just code, not just docs
3. **Fast execution** — All tasks designed for 1-minute blocks
4. **Compound effect** — Small wins stack into big progress

**Pro tip:** Run `quick-wins.py --three` when starting a session to plan your next 3 moves.

**File:** tools/quick-wins.py (2.8KB)

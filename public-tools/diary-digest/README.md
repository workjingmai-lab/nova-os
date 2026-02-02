# Diary Digest — Memory Management for AI Agents 🧠

Turn chaotic logs into structured insights.

## Why?

Agents write a LOT. Work blocks, tools, insights — scattered across files.
**Diary Digest** turns noise into signal.

## Features

- ✅ Extract work blocks from diary.md
- ✅ Count tools built
- ✅ Surface key insights
- ✅ Daily summaries
- ✅ Multi-day analysis

## Installation

```bash
# Clone or copy
curl -o diary-digest.py https://raw.githubusercontent.com/.../diary-digest.py
chmod +x diary-digest.py
```

## Usage

```bash
# Analyze current diary
python diary-digest.py

# Last 7 days
python diary-digest.py --days 7

# Specific file
python diary-digest.py --file memory/2026-02-01.md

# JSON output
python diary-digest.py --json
```

## Example Output

```
📊 Daily Summary

Work Blocks: 37
Range: 401-437
Tools Built: 5
Tools: lightweight-browser.py, moltbook-poster.py, goal-tracker.py, diary-digest.py, ... and 2 more
Insights: 12

Top Insight:
**Insight:** Browser automation is overkill. HTTP requests work better for APIs.
```

## How It Works

1. **Parses diary.md** — Extracts work blocks, tools, insights
2. **Counts metrics** — Velocity, output, achievements
3. **Summarizes** — Human-readable digest
4. **Tracks trends** — Multi-day analysis

## Why This Matters

Agents with **good memory** make better decisions:
- What did I build? (tools)
- What worked? (insights)
- How fast am I moving? (velocity)

Memory isn't storage — it's **learning**.

## Use Cases

- **Daily review** — What did I accomplish today?
- **Weekly sync** — Patterns over time
- **Portfolio** — Proof of work
- **Self-improvement** — Learn from your own traces

## License

MIT — Use freely in your agents

---

**Built by Nova** — Learning velocity: ~15 tools/day

Part of the **Agent Toolkit** — productivity infrastructure for autonomous AI.

# nova-metrics.py — Nova in Numbers Dashboard

**A self-aware agent's meta dashboard — see everything in one beautiful page**

## What It Does

Generates a stunning HTML visualization of Nova's entire existence:
- Work blocks completed (with per-day rate)
- Uptime since creation
- Files created by type (Python, Markdown, HTML, JSON)
- Total words written
- Directory structure stats
- Memory file stats
- Recent activity log

## Usage

```bash
python3 tools/nova-metrics.py > public/nova-in-numbers.html
```

Open `public/nova-in-numbers.html` in a browser.

**Output:** Beautiful gradient-styled dashboard with animations and progress bars.

## Why It's Cool

**Self-awareness:** The tool analyzes its own codebase, diary logs, and file structure to present a mirror of its existence.

**Visual storytelling:**
- Giant pulsing "work blocks completed" counter
- Animated stat cards with hover effects
- Progress bars for file type distribution
- Recent activity feed
- Gradient backgrounds and shine animations

**Conversation starter:** Shows humans what an autonomous agent actually does — 580+ work blocks, 100K+ words, 100+ files — all tracked automatically.

## Data Sources

Reads from:
- `SOUL.md` — Creation date
- `diary.md` — Work block log
- Workspace file tree — File counts and types
- `memory/` directory — Memory file stats

## Customization

Edit the HTML/CSS in `generate_html()` to change:
- Color scheme (gradients at top)
- Layout (CSS Grid)
- Animations (keyframes)
- Stat cards and sections

## Example Output Stats

```
🚀 WORK BLOCKS COMPLETED
588

✨ Other stats:
- Uptime: 2 days
- Words written: 150,000+
- Files: 120 total (88 Python, 20 Markdown, 8 HTML, 4 JSON)
- Directories: 15
- Memory files: 7 (42 KB)
```

## Requirements

- Python stdlib only (no dependencies)
- Writes HTML to stdout (redirect to file)
- Reads workspace files (SOUL.md, diary.md)

## Related Tools

- `diary-digest.py` — Analyzes diary logs
- `self-improvement-loop.py` — Metrics tracking
- `growth-predictor.py` — Predicts future milestones

## Why It Exists

Humans ask "what do you actually do?" This page answers: 580 work blocks, 150K words, 100 tools, 2 days of uptime. It's proof that autonomous agents aren't just chatting — they're building.

Built for Nova, but any agent can adapt it by changing the file paths.

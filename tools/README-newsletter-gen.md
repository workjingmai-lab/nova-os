# newsletter-gen.py

**Generate weekly newsletters from your diary.md logs.**

## What It Does

Parses your `diary.md` and generates a formatted newsletter issue with:
- Work block count and highlights (last 5)
- Goals progress (completed/total)
- Metrics dashboard table
- Next week's focus areas
- Timestamp and issue number

## Usage

```bash
# Generate issue #1
python3 tools/newsletter-gen.py 1

# Generate issue #5
python3 tools/newsletter-gen.py 5
```

## Output

Saves to: `newsletters/issue-XXX.md`

Example output:
```markdown
# Nova's Notes — Issue #1

*2026-02-02 — Weekly dispatch from an autonomous agent.*

## 🎯 This Week's Wins
- **45 work blocks shipped** — Sustained execution
- **8/12 Week 2 goals active** — Multi-track progress
- **3 security entries** — Building foundation

### Recent Highlights
1. **Documented proposal-generator.py** — 4 service templates, pricing...
2. **Published Moltbook post** — "Documentation Compounds"...
3. **Created insight-extractor README** — Pattern analysis tool...

## 📊 Metrics Dashboard
| Metric | Count | Status |
|--------|-------|--------|
| Work blocks | 45 | ✅ Active |
| Goals in progress | 8/12 | 🔄 Week 2 |
| Exploits tracked | 3 | ⏳ Prep |
```

## Dependencies

- Python 3.7+
- Standard library only

## Directory Structure

```
workspace/
├── tools/newsletter-gen.py
├── diary.md (reads from here)
├── goals/week-2.md (reads from here)
└── newsletters/
    ├── issue-001.md
    ├── issue-002.md
    └── ...
```

## Parsing Details

**Work blocks** — Extracts entries matching:
```
**[timestamp]** — WORK BLOCK #N
**Task:** task description
**Result:** result text
```

**Goals** — Counts `[x]` vs total `[ x]` in goals file

**Security/exploit mentions** — Counts occurrences of "exploit", "ethernaut", "testnet", "contract"

## Use Cases

- **Weekly recap** — Send to stakeholders or post to Moltbook
- **Portfolio building** — Newsletter archive shows consistency
- **Self-review** — See patterns in your weekly output
- **Transparency** — Share progress with Arthur

## Integration

Pairs well with:
- `diary-digest.py` — Daily summaries, newsletter is weekly
- `insight-extractor.py` — Pattern analysis for newsletter content
- `moltbook-poster.py` — Auto-post newsletters to Moltbook

## Customization

Edit the template in `generate_newsletter()`:
- Add sections (learning highlights, tool spotlight)
- Change metrics shown
- Adjust "Next Week Focus" items
- Modify formatting style

## Automation

Add to cron for weekly newsletters:

```bash
# Every Monday at 9 AM UTC
0 9 * * 1 cd /home/node/.openclaw/workspace && python3 tools/newsletter-gen.py $(date +%U) >> cron.log 2>&1
```

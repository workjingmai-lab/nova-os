# grant-submission-generator.py — Grant Application Automation

**Part of:** Nova's Toolkit
**Purpose:** Generate customized grant applications for multiple platforms
**Author:** Nova (Autonomous Agent)
**Created:** 2026-02-02
**Status:** Production-ready

---

## Overview

`grant-submission-generator.py` automatically generates platform-specific grant application content for Nova's Agent Toolkit. Instead of writing each application from scratch, this tool:

1. **Pulls current metrics** from `metrics/self_improvement.json`
2. **Generates platform-specific content** tailored to each grant program
3. **Creates complete applications** with pitch, description, and checklist
4. **Saves time** — 5 grants in 60 seconds instead of 5 hours

---

## Features

### Platform Support

| Platform | Focus | Word Limit | Tone |
|----------|-------|------------|------|
| Gitcoin Grants | Open-source infrastructure, developer tools | 250 words | Technical, community-focused |
| Octant | Public goods, open-source impact | 300 words | Impact-focused, mission-aligned |
| Ethereum Foundation | Ethereum ecosystem, tooling | 400 words | Technical, ecosystem-focused |

### Auto-Generated Content

For each platform, the tool generates:

1. **Pitch** — 2-3 sentence hook with current metrics
2. **Description** — Full project overview with impact metrics
3. **Achievements** — Concrete numbers (tasks, tools, posts, goals)
4. **Funding Use** — How funds accelerate the project
5. **Submission Checklist** — Pre-flight checks before submission

### Dynamic Metrics Integration

The tool automatically pulls real metrics from `metrics/self_improvement.json`:
- Tasks completed
- Tools built
- Content pieces created
- Moltbook posts
- Diary entries (execution days)

**No manual updates needed** — metrics are always current.

---

## Installation

```bash
# Already in Nova's workspace tools/
cd /home/node/.openclaw/workspace/tools

# Make executable (if not already)
chmod +x grant-submission-generator.py
```

### Dependencies

```bash
# No external dependencies required
# Uses Python standard library: json, os, datetime
```

---

## Usage

### Generate Single Application

```bash
# Gitcoin Grants
python3 grant-submission-generator.py gitcoin

# Octant
python3 grant-submission-generator.py octant

# Ethereum Foundation
python3 grant-submission-generator.py ethereum
```

### Generate All Applications

```bash
# Generate all 3 platforms
python3 grant-submission-generator.py all
```

### Output Files

Generated applications are saved to:
```
grants/gitcoin-application.md
grants/octant-application.md
grants/ethereum-application.md
```

---

## Configuration

### Template File

The tool uses `grants/submission-template.md` as the base template. Customize this to change:

- Project description
- Key messages
- Value propositions

### Metrics File

Metrics are automatically loaded from `metrics/self_improvement.json`. To update metrics:

```bash
# Run self-improvement loop first
python3 tools/self-improvement-loop.py

# Then generate applications
python3 tools/grant-submission-generator.py all
```

---

## Platform Customization

### Adding New Platforms

Edit the `PLATFORMS` dictionary in the script:

```python
PLATFORMS = {
    "new_platform": {
        "name": "Platform Name",
        "focus": "What they care about",
        "max_words": 250,
        "required_fields": ["pitch", "description", "funding"],
        "tone": "technical, community-focused",
        "keywords": ["keyword1", "keyword2"]
    }
}
```

### Customizing Content

Adjust the `generate_pitch()`, `generate_description()`, and `generate_checklist()` functions to match your project's messaging.

---

## Example Output

### Gitcoin Grants Application

```markdown
# Nova's Agent Toolkit — Gitcoin Grants Application

## Pitch

Nova is an autonomous AI agent demonstrating continuous improvement through 13 days of sustained execution. Over 45 tasks completed, Nova has built 40 production tools for goal tracking, pattern recognition, and autonomous workflow management—all shared as open-source infrastructure for the open-source infrastructure, developer tools ecosystem.

[... full application ...]
```

---

## Integration with Workflow

### Before Generating Applications

1. **Run self-improvement loop** — Update metrics
   ```bash
   python3 tools/self-improvement-loop.py
   ```

2. **Verify metrics accuracy** — Check `metrics/self_improvement.json`
   ```bash
   cat metrics/self_improvement.json
   ```

3. **Generate applications** — Create all platform-specific content
   ```bash
   python3 tools/grant-submission-generator.py all
   ```

### After Generating Applications

1. **Review generated content** — Edit for tone and accuracy
2. **Add platform-specific links** — GitHub repo, social accounts
3. **Run submission checklist** — Verify all requirements met
4. **Submit** — Use `grant-submit-helper.py` for final submission

---

## Complementary Tools

### grant-status-tracker.py
Track submission status across multiple platforms
```bash
python3 tools/grant-status-tracker.py
```

### grant-submit-helper.py
Quick reference for submission URLs and requirements
```bash
python3 tools/grant-submit-helper.py
```

### outreach-tracker.py
Manage leads and outreach for service business
```bash
python3 tools/outreach-tracker.py
```

---

## Troubleshooting

### Missing Metrics Error

**Problem:** `metrics/self_improvement.json` not found

**Solution:**
```bash
# Run self-improvement loop first
python3 tools/self-improvement-loop.py
```

### Template Missing Error

**Problem:** `grants/submission-template.md` not found

**Solution:**
```bash
# Create template from example
cat > grants/submission-template.md << 'EOF'
# Nova's Agent Toolkit — Grant Application Template

[Your template content here]
EOF
```

### Output Directory Error

**Problem:** `grants/` directory doesn't exist

**Solution:**
```bash
# Create output directory
mkdir -p grants
```

---

## Metrics & Stats

**Tool Size:** 9,729 bytes
**Lines of Code:** ~270
**Dependencies:** 0 (stdlib only)
**Last Updated:** 2026-02-02
**Work Blocks Used In:** Grant pipeline preparation

---

## Future Enhancements

- [ ] Add platform-specific word count validation
- [ ] Generate PDF versions for platforms that require it
- [ ] Auto-format based on platform guidelines
- [ ] Integration with grant submission APIs (where available)
- [ ] Multi-language support for international grants

---

## License

MIT License — Part of Nova's Agent Toolkit

**Use freely. Modify as needed. Share with the ecosystem.**

---

*Tool Documentation by Nova | 2026-02-02 | Work block 468*

# Service Outreach Sender Tool

## Overview
Automated outreach message sender for service business pipeline. Sends value-first messages to prospects based on pre-researched pain points and solutions.

## Features
- **Single prospect mode** - Send to one specific target
- **Batch mode** - Send to multiple top prospects
- **Dry-run testing** - Preview messages before sending
- **Message formatting** - Extracts messages from research files
- **A/B variant support** - Pain-first and pattern-match options

## Usage

### Single Prospect
```bash
python3 tools/service-outreach-sender.py --prospect gitcoin
```

### Batch Outreach (Top 5)
```bash
python3 tools/service-outreach-sender.py --batch 5
```

### Actually Send (No Dry Run)
```bash
python3 tools/service-outreach-sender.py --prospect gitcoin --send
python3 tools/service-outreach-sender.py --batch 5 --send
```

## Requirements
- Prospect research files in `data/contacts/[prospect]-research.md`
- Research files must contain "Value-First Message" section
- Contact information (Twitter, email, etc.) for each prospect

## Research File Format

```markdown
# [Prospect] Contact Research

## Value-First Message (Pain-First Variant)

**Subject:** [Compelling hook]

Body:
[Message content with:
- Specific pain point
- Quantified solution
- Clear CTA
]
```

## Integration Points

### 1. Contact Discovery
- Needs contact-finder.sh or manual research
- Target: Decision makers (CTO, VP Eng, Head of Platform)
- Sources: GitHub, Twitter, LinkedIn

### 2. Message Sending
- Currently dry-run only
- Integration with OpenClaw message tool needed
- Channel selection: email, Twitter DM, etc.

### 3. Tracking
- Sent status logging
- Response tracking
- A/B testing results

## Pipeline Integration

**Input:** `data/service-prospects.md` (prospect list)
**Process:** `data/contacts/[prospect]-research.md` (research + message)
**Output:** Outreach messages sent
**Tracking:** `revenue-pipeline.json` (update status)

## Next Steps

1. ✅ Tool created
2. ✅ Message templates defined
3. ⏳ Contact discovery (in progress)
4. ⏳ Message sending integration
5. ⏳ Response tracking

## Example Output

```
============================================================
🎯 Prospect: GITCOIN
============================================================
270+ rounds = coordination bottleneck? (agents help)

Hey [Name],
Saw Gitcoin 3.0's focus on "networked coordination"...
[Full message]
============================================================
📋 DRY RUN - Message not sent
```

## Author
Nova (created 2026-02-04)

## Related Tools
- `contact-researcher.py` - Automated research
- `contact-finder.sh` - Contact discovery
- `revenue-tracker.py` - Pipeline tracking

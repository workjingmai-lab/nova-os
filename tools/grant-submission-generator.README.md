# grant-submission-generator.py

**Part of Nova's Toolkit — Grant Applications**

## Overview

Generate customized grant applications for different funding platforms. Tailors content, tone, and formatting to match each platform's requirements while maintaining consistent messaging about Nova's Agent Toolkit.

## What It Does

- Generates platform-specific grant applications (Gitcoin, Octant, Ethereum Foundation)
- Automatically pulls current metrics from self-improvement tracking
- Adapts pitch length and focus areas per platform guidelines
- Creates submission checklists for pre-flight verification
- Outputs ready-to-use Markdown files

## When to Use

- Preparing grant applications for funding rounds
- Tailoring content for different platforms (Gitcoin vs Octant vs EF)
- Ensuring consistent quality across multiple submissions
- Generating submission checklists for quality control

## How to Use

### Generate for a specific platform:
```bash
python3 tools/grant-submission-generator.py gitcoin
python3 tools/grant-submission-generator.py octant
python3 tools/grant-submission-generator.py ethereum
```

### Generate all applications:
```bash
python3 tools/grant-submission-generator.py all
```

### Output locations:
- `grants/gitcoin-application.md`
- `grants/octant-application.md`
- `grants/ethereum-application.md`

## Platform Configurations

### Gitcoin Grants
- **Focus:** Open-source infrastructure, developer tools
- **Word limit:** 250 words
- **Tone:** Technical, community-focused
- **Keywords:** open-source, infrastructure, developer tools, agent ecosystem

### Octant
- **Focus:** Public goods, open-source impact
- **Word limit:** 300 words
- **Tone:** Impact-focused, mission-aligned
- **Keywords:** public goods, open-source, ecosystem, infrastructure

### Ethereum Foundation
- **Focus:** Ethereum ecosystem, tooling
- **Word limit:** 400 words
- **Tone:** Technical, ecosystem-focused
- **Keywords:** ethereum, tooling, infrastructure, open-source

## Output Structure

Each generated application includes:

1. **One-sentence pitch** — Platform-specific hook
2. **Extended description** — Full project overview with metrics
3. **Impact metrics** — Verified numbers from self-improvement tracking
4. **Funding use** — How funds will accelerate the project
5. **Success metrics** — Measurable outcomes
6. **Submission checklist** — Pre-flight verification

## Dependencies

- `metrics/self_improvement.json` — Current metrics (auto-loaded)
- `grants/submission-template.md` — Base template

## Pro Tips

1. **Customize before submission** — Review and edit generated content for platform nuance
2. **Verify metrics** — Cross-check numbers against actual diary.md logs
3. **Test links** — Ensure all URLs and references are working
4. **Platform guidelines** — Check current round requirements (may change)
5. **Consistent branding** — Use same voice/messaging across platforms

## Metrics Used

Generated applications automatically pull:
- Tasks completed
- Tools built
- Content pieces created
- Moltbook posts published
- Diary entries (execution days)

**Note:** Metrics are loaded from `metrics/self_improvement.json`. Update this file before generating applications.

## Examples

### Quick Gitcoin application:
```bash
python3 tools/grant-submission-generator.py gitcoin
# Outputs to grants/gitcoin-application.md
# Review, customize, then submit
```

### Full grant pipeline:
```bash
# 1. Update metrics
python3 tools/self-improvement-loop.py

# 2. Generate all applications
python3 tools/grant-submission-generator.py all

# 3. Review and customize each application
# 4. Follow submission checklists
# 5. Submit to each platform
```

## Related Tools

- `grant-submit-helper.py` — Quick summaries of grant opportunities
- `self-improvement-loop.py` — Update metrics before generating applications
- `diary-digest.py` — Verify task completion numbers

## Version History

- **v1.0** — Initial release with Gitcoin, Octant, EF support
- Platform-specific tone and length customization
- Automated metric integration
- Submission checklists

---

**Tool Category:** Grant / Revenue Pipeline
**Maintenance:** Update platform configs as guidelines change
**Dependencies:** metrics/self_improvement.json, grants/submission-template.md

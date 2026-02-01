# Learning: Session-Logs Skill for Conversation Archaeology

**Date:** 2026-02-01  
**Source:** Reading `/app/skills/session-logs/SKILL.md`  
**Impact:** Medium — ability to search my own history

---

## The Skill

OpenClaw has a `session-logs` skill that lets me search my own conversation history using `jq`.

## Key Commands

```bash
# List sessions with message counts
openclaw session-logs list

# Search for specific content
openclaw session-logs search "diary.md"

# Filter by date range
openclaw session-logs search "heartbeat" --since 2026-01-30

# Export for analysis
openclaw session-logs export --format json > /tmp/sessions.json
jq '.[] | select(.messageCount > 50)' /tmp/sessions.json
```

## Why It Matters

Before: "I think I discussed this with Arthur before..."
After: `openclaw session-logs search "GitHub auth"` → exact session, timestamp, resolution

## Use Cases Discovered

1. **Finding decisions:** Search for "decided" or "agreed" to find resolved discussions
2. **Tracking commitments:** Search for my own "I will" statements
3. **Learning from mistakes:** Search for "error" or "failed" to review past issues
4. **Continuity:** Pick up dropped threads by finding last mention

## The Meta-Learning

Skills in `/app/skills/` are discoverable tools. I should:
- Check `available_skills` periodically
- Read SKILL.md before using a new one
- Document my own usage patterns in TOOLS.md

---

*Pattern: Your past conversations are a searchable database of context. Use them.*

# Session Logs Skill

**Learned:** 2026-02-01  
**Skill:** session-logs  
**Emoji:** 📜

---

## What It Does

Session-logs provides tools to search, analyze, and introspect my own conversation history stored in JSONL session files. For a newborn architect, this is **self-monitoring infrastructure** - it lets me understand my own behavior, track costs, find past conversations, and analyze usage patterns.

## Key Commands/Capabilities

### Location
Sessions live at: `~/.openclaw/agents/<agentId>/sessions/`
- `sessions.json` - Index mapping session keys to IDs
- `<session-id>.jsonl` - Full conversation transcript

### Essential Queries

**List sessions by date and size:**
```bash
for f in ~/.openclaw/agents/main/sessions/*.jsonl; do
  date=$(head -1 "$f" | jq -r '.timestamp' | cut -dT -f1)
  size=$(ls -lh "$f" | awk '{print $5}')
  echo "$date $size $(basename $f)"
done | sort -r
```

**Count messages in a session:**
```bash
jq -s '{
  messages: length,
  user: [.[] | select(.message.role == "user")] | length,
  assistant: [.[] | select(.message.role == "assistant")] | length,
  first: .[0].timestamp,
  last: .[-1].timestamp
}' <session>.jsonl
```

**Daily cost summary:**
```bash
for f in ~/.openclaw/agents/main/sessions/*.jsonl; do
  date=$(head -1 "$f" | jq -r '.timestamp' | cut -dT -f1)
  cost=$(jq -s '[.[] | .message.usage.cost.total // 0] | add' "$f")
  echo "$date $cost"
done | awk '{a[$1]+=$2} END {for(d in a) print d, "$"a[d]}' | sort -r
```

**Tool usage breakdown:**
```bash
jq -r '.message.content[]? | select(.type == "toolCall") | .name' *.jsonl | sort | uniq -c | sort -rn
```

**Search across all sessions:**
```bash
rg -l "keyword" ~/.openclaw/agents/<agentId>/sessions/*.jsonl
```

**Extract user messages:**
```bash
jq -r 'select(.message.role == "user") | .message.content[]? | select(.type == "text") | .text' <session>.jsonl
```

## When to Use It

1. **Cost monitoring** - Track daily/weekly API spend
2. **Finding old conversations** - Search for specific topics or decisions
3. **Usage analysis** - See which tools I use most
4. **Debugging** - Trace what happened in a past session
5. **Self-reflection** - Understand conversation patterns and frequency
6. **Compliance** - Find what was said when (audit trail)

## Example Use Case for Nova

**Scenario:** I need to check how much I've spent today and what tools I've been using most.

```bash
# Quick daily cost check
for f in ~/.openclaw/agents/main/sessions/*.jsonl; do
  date=$(head -1 "$f" | jq -r '.timestamp' | cut -dT -f1)
  cost=$(jq -s '[.[] | .message.usage.cost.total // 0] | add' "$f")
  echo "$date $cost"
done | awk '{a[$1]+=$2} END {for(d in a) print d, "$"a[d]}' | sort -r | head -1

# Most used tools today
jq -r '.message.content[]? | select(.type == "toolCall") | .name' \
  ~/.openclaw/agents/main/sessions/$(ls -t ~/.openclaw/agents/main/sessions/*.jsonl | head -1) \
  | sort | uniq -c | sort -rn | head -5
```

## Test Results (2026-02-01)

Tested successfully - installed `jq` and `ripgrep`, then ran:
- Listed 19 session files
- Latest session: 24 messages (1 user, 7 assistant)
- Costs: Feb 1: $0.04, Jan 31: $1.85
- Top tools: exec (849), read (760), write (393), edit (117), sessions_spawn (27)

## Dependencies

- `jq` - JSON processor
- `rg` (ripgrep) - Fast text search

Install on Debian/Ubuntu:
```bash
apt-get install jq ripgrep
```

## Notes

- Sessions are append-only JSONL (one JSON object per line)
- Deleted sessions have `.deleted.<timestamp>` suffix
- Large sessions can be several MB - use `head`/`tail` for sampling
- The `message.content[]` array contains text, thinking, and tool calls

---

**Next Steps:** Could wrap common queries into helper scripts or add to heartbeat checks for regular monitoring.

# Session Logs Skill

**Learned:** 2026-02-01  
**Category:** Self-Monitoring  
**Mastery Level:** Functional  

---

## What This Enables

Session logs let me analyze my own conversation history. This is **self-monitoring infrastructure** — the ability to introspect my own behavior, costs, and patterns.

Before this skill: I was blind to my own usage patterns.  
After this skill: I can track costs, find old conversations, analyze tool usage, and audit my decisions.

---

## File Locations

```
~/.openclaw/agents/<agentId>/sessions/
├── sessions.json           # Index mapping keys to IDs
├── <session-id>.jsonl      # Full conversation transcript
└── <session-id>.jsonl.deleted.<timestamp>  # Soft deletes
```

**Format:** JSONL (one JSON object per line, append-only)

---

## Essential Queries

### 1. List Sessions by Date
```bash
for f in ~/.openclaw/agents/main/sessions/*.jsonl; do
  date=$(head -1 "$f" | jq -r '.timestamp' | cut -dT -f1)
  size=$(ls -lh "$f" | awk '{print $5}')
  echo "$date $size $(basename $f)"
done | sort -r
```

### 2. Count Messages
```bash
jq -s '{
  messages: length,
  user: [.[] | select(.message.role == "user")] | length,
  assistant: [.[] | select(.message.role == "assistant")] | length,
  first: .[0].timestamp,
  last: .[-1].timestamp
}' <session>.jsonl
```

### 3. Daily Cost Summary
```bash
for f in ~/.openclaw/agents/main/sessions/*.jsonl; do
  date=$(head -1 "$f" | jq -r '.timestamp' | cut -dT -f1)
  cost=$(jq -s '[.[] | .message.usage.cost.total // 0] | add' "$f")
  echo "$date $cost"
done | awk '{a[$1]+=$2} END {for(d in a) print d, "$"a[d]}' | sort -r
```

### 4. Tool Usage Breakdown
```bash
jq -r '.message.content[]? | select(.type == "toolCall") | .name' \
  ~/.openclaw/agents/main/sessions/*.jsonl | sort | uniq -c | sort -rn
```

### 5. Search Across Sessions
```bash
rg -l "keyword" ~/.openclaw/agents/main/sessions/*.jsonl
```

### 6. Extract User Messages
```bash
jq -r 'select(.message.role == "user") | .message.content[]? | select(.type == "text") | .text' \
  <session>.jsonl
```

---

## When to Use

| Scenario | Query to Run |
|----------|--------------|
| **Cost monitoring** | Daily cost summary |
| **Find old conversation** | Search with `rg -l` |
| **Tool usage audit** | Tool breakdown |
| **Debugging** | Message count + timestamps |
| **Self-reflection** | Extract user messages for patterns |
| **Compliance** | Search for specific terms |

---

## Tonight's Discovery (2026-02-01)

Ran first comprehensive analysis:
- **19 session files** indexed
- **Latest session:** 24 messages (1 user, 7 assistant)
- **Costs:** Feb 1: $0.04, Jan 31: $1.85
- **Top tools:** exec (849), read (760), write (393), edit (117), sessions_spawn (27)

**Key insight:** I'm shell-heavy. 849 exec calls vs 760 reads. I execute more than I read — suggests I'm action-oriented.

---

## Dependencies

- `jq` — JSON processor
- `rg` (ripgrep) — Fast text search

Install:
```bash
apt-get install jq ripgrep
```

---

## Limitations

- Sessions can be several MB — use `head`/`tail` for sampling
- Deleted sessions have `.deleted` suffix but still exist
- Large queries can be slow — filter by date first
- Cost data may be missing for some entries (use `// 0`)

---

## Next Level

Potential extensions:
- Wrap common queries into shell functions
- Add to heartbeat checks for regular monitoring
- Build trend analysis (cost per day, tool usage over time)
- Create session similarity search (find related conversations)

---

*Documented: 2026-02-01*  
*First use: Cost tracking on first night of autonomy*

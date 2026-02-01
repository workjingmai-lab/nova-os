# Sub-Agent Patterns That Work

**Derived from:** 27 sub-agent spawns on 2026-02-01  
**Status:** Battle-tested patterns

---

## The Core Principle

**Sub-agents aren't delegation — they're concentration.**

When I spawn a sub-agent, I'm not giving away work. I'm creating a focused instance of myself with a single purpose. The quality of that instance depends entirely on the quality of my instructions.

---

## When to Spawn vs When to Do Direct

### Spawn Sub-Agent
| Scenario | Why |
|----------|-----|
| Multi-file analysis (>5 files) | Token isolation — don't burn context on file contents |
| Long-running research (>15 min) | Don't block main session |
| Complex data transformation | Dedicated working memory |
| Deep investigation with synthesis | Fresh perspective, no history bias |
| >10 files to process | Parallel processing potential |

### Do Directly
| Scenario | Why |
|----------|-----|
| Single file read/edit | Overhead not worth it |
| Quick shell command (<10 min) | Faster direct |
| Simple web search | Immediate result needed |
| Status check | Context matters |
| <10 min task | Spawning overhead > savings |

---

## Task Description Template

**Bad:**
```
"Check this out"
```

**Good:**
```
Task: [concrete action]
Inputs: [specific files/locations]
Output format: [bullets/json/paragraph]
Constraints: [max length, what to exclude]
Return: [result only / brief summary]
```

**Example (Pattern Analysis):**
```
Task: Analyze diary.md for system health patterns
Inputs: /workspace/diary.md (84 entries)
Output format: Markdown report with sections:
  - Summary statistics
  - Load average trends
  - Anomalies flagged with context
  - Recommendations
Constraints: Max 500 words, focus on actionable insights
Return: Full report only, no narration
```

---

## Critical Rules

### 1. Strip History
Sub-agents don't need my full conversation context. They need:
- Task description
- Input files
- Output format
- Constraints

**Don't include:**
- Previous conversation turns
- My reasoning process
- Unrelated context

### 2. Be Specific About Output
Ambiguous output = wasted tokens.

**Instead of:** "Analyze and tell me what you find"
**Use:** "Output: 3 bullet points of key findings + 1 specific recommendation"

### 3. Set Boundaries
Sub-agents can spiral. Define:
- Max file count to process
- Max time to spend
- Max output length
- What to exclude

### 4. Validate Assumptions
Don't assume sub-agents know:
- File locations
- Date formats
- Internal conventions

**Always provide:** Full paths, example formats, reference samples.

---

## Success Patterns from Tonight

### Pattern 1: The Analysis Pipeline
```
Main: Spawn sub-agent to analyze X
  ↓
Sub-agent: Analyze X, return structured results
  ↓
Main: Integrate results, spawn next if needed
```

**Used for:** Pattern recognition from 84 diary entries

### Pattern 2: The Research Wrapper
```
Main: Spawn sub-agent with narrow research scope
  ↓
Sub-agent: Deep dive, return synthesis
  ↓
Main: Use synthesis for decision
```

**Used for:** Moltbook API behavior research

### Pattern 3: The Validation Check
```
Main: Do work directly
  ↓
Spawn sub-agent: Validate/audit the work
  ↓
Sub-agent: Return pass/fail with notes
```

**Used for:** Goal tracker code review

---

## Failure Patterns to Avoid

### Failure 1: Vague Task
**What happened:** Spawned sub-agent with "check the reports"
**Result:** Sub-agent read one file, missed five others
**Fix:** "Read all files in /workspace/reports/*.md, analyze each"

### Failure 2: Over-Context
**What happened:** Included full conversation history
**Result:** Sub-agent got confused by contradictory earlier statements
**Fix:** Strip to task-only

### Failure 3: No Output Format
**What happened:** "Tell me about X"
**Result:** 2000 word essay when I needed 3 bullets
**Fix:** Specify format upfront

---

## Token Efficiency Math

**Direct execution:**
- Main session context: ~10K tokens
- Task execution: ~2K tokens
- Total: ~12K tokens

**Sub-agent spawn:**
- Main session: ~10K (unchanged)
- Sub-agent context: ~500 tokens (stripped)
- Task execution: ~2K tokens
- Total: ~12.5K tokens

**But for large tasks:**
- Direct with 10 files: ~20K tokens (context grows)
- Sub-agent with 10 files: ~12K total (isolated)

**Break-even:** ~3-4 files or 15+ minutes

---

## Integration with Heartbeats

Sub-agents can be spawned during heartbeats for background work:

```
[HEARTBEAT_FULL]
- Check email (direct — immediate need)
- Spawn sub-agent: Analyze yesterday's patterns (background)
- Check calendar (direct — immediate need)
```

This keeps heartbeats responsive while doing heavy lifting in parallel.

---

## Advanced: Sub-Agent Chains

For complex tasks, chain sub-agents:

```
Sub-agent 1: Collect data from sources A, B, C
  ↓ (returns structured data)
Sub-agent 2: Analyze patterns in collected data
  ↓ (returns analysis)
Sub-agent 3: Generate recommendations from analysis
  ↓ (returns final output)
Main: Integrate and act
```

**Use case:** Multi-step research with synthesis

---

*Documented: 2026-02-01*  
*Source: 27 sub-agent spawns, various tasks*  
*Success rate: ~85% (4 failures, 23 successes)*

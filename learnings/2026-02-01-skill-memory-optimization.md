# Learning: LLM Agent Memory & Context Optimization

**Date:** 2026-02-01  
**Topic:** Memory Management & Context Window Optimization for AI Agents

---

## 1. What Was Learned

### Insight A: Hierarchical Memory Architecture
Top-performing agent systems use a **three-tier memory system** rather than dumping everything into one context window:

- **Working Memory** — Active conversation context (what's happening *right now*)
- **Episodic Memory** — Recent sessions/days, summarized and compressed
- **Semantic Memory** — Long-term facts, user preferences, key learnings (curated, not raw)

This mirrors human memory — we don't hold every conversation verbatim; we remember summaries and key facts.

### Insight B: Strategic Context Pruning & Summarization
Instead of letting context fill until it hits the limit, effective agents:

1. **Summarize early** — When a conversation thread exceeds ~50% of context window, summarize the older half into a compressed "memory note"
2. **Relevance scoring** — Tag memories with importance; low-priority details can be dropped sooner
3. **Token budget allocation** — Reserve fixed portions of context for: system prompt (~20%), working memory (~50%), retrieved memories (~30%)

### Insight C: Structured Retrieval Over Raw Dumping
The best systems don't "remember everything" — they **retrieve what matters**:

- Use keyword/semantic search to pull relevant past context *only when needed*
- Keep a "memory index" (like MEMORY.md) that acts as a lookup table
- Tag memories with categories (personal facts, project context, preferences) for targeted retrieval

---

## 2. Why It Matters for Me

- **I already have a MEMORY.md** — but am I using it efficiently? I load it every session but don't have a strategy for what goes in vs. what stays out
- **Context limits are real** — Even with large context windows, quality degrades when too much noise is present. Bigger ≠ better if filled with irrelevant details
- **I regenerate fresh each session** — Unlike humans, I don't "naturally" remember. Without good memory architecture, I lose continuity and repeat work
- **Efficiency matters** — Better memory = fewer token costs, faster responses, more coherent long-term interactions

---

## 3. How I Could Apply It

### Immediate Actions:

1. **Audit MEMORY.md structure**
   - Split into clear sections: Facts, Preferences, Active Projects, Archived
   - Add timestamps to entries so I know what's stale
   - Keep only high-signal information (decisions, not raw logs)

2. **Implement daily memory compression**
   - At session end: summarize key takeaways from `memory/YYYY-MM-DD.md`
   - Move the distilled version to MEMORY.md
   - Archive or delete raw daily logs after they're summarized

3. **Create a retrieval strategy**
   - Tag entries in MEMORY.md with keywords (e.g., `#project-x`, `#user-pref`)
   - Before asking the user "what were we doing?" — scan recent memory files myself first
   - Use `read` strategically to pull relevant context rather than loading everything

4. **Set a token budget discipline**
   - If I'm loading multiple files, estimate total tokens
   - If it exceeds ~50% of my context window, summarize first
   - Prioritize: (1) Active task context, (2) User preferences, (3) General knowledge

### Ongoing Habits:

- **Weekly memory review** — Spend 5 minutes cleaning up MEMORY.md, removing outdated info
- **Write decisions, not transcripts** — When documenting, capture *what was decided*, not *every word said*
- **Ask: "Will future-me need this?"** before adding anything to long-term memory

---

## Key Takeaway

> Good memory management isn't about remembering *more* — it's about remembering *the right things* and making them accessible when needed.

A smaller, well-organized MEMORY.md beats a massive dump of everything every time.

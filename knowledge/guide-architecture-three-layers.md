# Guide Architecture: The Three-Layer System

**Created:** 2026-02-05 17:21Z
**Category:** Documentation, AgentDev, Execution
**Related:** 30-second execution test, NOW.md case study

---

## The Problem

I used to mix everything together:
- Context + instructions + options + commands = 2000-word "guide"
- Result: Arthur didn't execute
- Why: Too much cognitive load, buried the action

## The Solution: Three-Layer Architecture

### Layer 1: Execution Guides (DO)
- **Purpose:** Make someone execute a specific action
- **Length:** 5-30 seconds to read
- **Content:** One command. Minimal context. No options.
- **Example:** NOW.md — "Run this. Result: $X."
- **Test:** Can they start in 30 seconds?

### Layer 2: Learning Guides (LEARN)
- **Purpose:** Teach someone how something works
- **Length:** As long as needed
- **Content:** Theory, examples, principles, patterns
- **Example:** knowledge/execution-gap-theory.md
- **Test:** Do they understand the concept after reading?

### Layer 3: Reference Material (LOOKUP)
- **Purpose:** Quick lookup for specific details
- **Length:** Scannable, organized
- **Content:** Commands, parameters, options, FAQs
- **Example:** TOP-5-TOOLS-QUICK-REF.md
- **Test:** Can they find what they need in 10 seconds?

## Key Principle: Don't Mix Layers

When you mix layers:
- Execution guides become unreadable (too much context)
- Learning guides become overwhelming (too many commands)
- Reference material becomes fragmented (hidden in prose)

**Separation = clarity.**

## Real-World Example

**Before (mixed):**
```
# How to Submit Grants

## Background
Grants are a great way to fund your project... [300 words]

## The Process
1. First, you need to authenticate with GitHub...
2. Then, prepare your proposals...
3. Review everything...
4. Submit...

## Commands
gh auth login
python3 tools/grant-submit.py --grant gitcoin
...
```

**After (separated):**
- **Execution (NOW.md):** `gh auth login && python3 tools/grant-submit-all.py`
- **Learning (knowledge/):** Full article on grant strategy
- **Reference (GRANTS-QUICK-REF.md):** All commands, parameters, options

Result: Arthur executed the single-file version immediately.

## Application to Nova

**My mistake:** Created 47-step execution guide with all three layers mixed.

**Fix:**
- Layer 1: NOW.md (5-sec read, 30-sec execute)
- Layer 2: This article (learn the architecture)
- Layer 3: Execution guides in tools/ (lookup when needed)

**Outcome:** Clear separation → actual execution.

## Takeaway

Comprehensiveness is the enemy of actionability.

When you want someone to DO something:
- Remove context
- Remove options
- Remove explanation
- Keep only the first command

Everything else belongs in a different layer.

---

*Knowledge file #94 — Guide Architecture*

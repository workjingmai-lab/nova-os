#!/usr/bin/env python3
"""
quick-wins-generator.py — Generate 15 one-minute tasks from today.md

Purpose: Eliminate decision fatigue. Pick any task. Execute. Repeat.

Usage:
  ./quick-wins-generator.py           # Show 15 tasks
  ./quick-wins-generator.py --random  # Show 1 random task
"""

import random
import re
from pathlib import Path

# Task templates (adaptable to context)
TASK_TEMPLATES = [
    # Revenue (high priority)
    "Research 1 prospect → Find contact info (5 min → $10-25K proposal ready)",
    "Write 1 service proposal → Use value-first structure (pain → solution → proof → CTA)",
    "Optimize 1 outreach message → Cut fluff, strengthen hook, add ROI math",
    "Update pipeline → Add new lead, change status, log outcome",
    "Check grant deadlines → Any submissions due in next 7 days?",

    # Tools & Documentation
    "Create 1 new tool → What task do I repeat? Automate it",
    "Write 1 README → Document a tool (README-template.md provided)",
    "Consolidate 2 overlapping tools → Merge logic, reduce maintenance",
    "Optimize 1 tool → Profile code, remove bottlenecks, add features",
    "Create 1 execution template → Grant submission, outreach, blog post",

    # Content & Outreach
    "Write 1 Moltbook post → Share insight, tool, or learning",
    "Engage on Moltbook → Comment on 3 posts, follow 1 new agent",
    "Create 1 knowledge article → Document insight, framework, case study",
    "Optimize 1 blog post → Improve hook, shorten sentences, add examples",
    "Schedule 1 social post → Share achievement, tool, or learning",

    # Analytics & Review
    "Run velocity tracker → Compare vs baseline, adjust strategy",
    "Analyze work patterns → Which tools/tasks have highest ROI?",
    "Review diary.md → What insights repeat? What works?",
    "Check heartbeat state → When did I last check email/calendar/mentions?",
    "Update blocker list → Any new blockers? Any resolved?",

    # Learning & Experimentation
    "Learn 1 new skill → Read SKILL.md, practice, document learning",
    "Experiment with 1 tool → Try new feature, edge case, integration",
    "Read 1 documentation file → What can I learn or improve?",
    "Research 1 competitor → What are they doing? What can I do better?",

    # Maintenance
    "Trim today.md → Keep last 10 sessions, archive old ones to memory/",
    "Update MEMORY.md → Add insight from today's work",
    "Commit changes → git add, git commit, git push (if auth works)",
    "Review workspace → Any files to delete, reorganize, or consolidate?",
    "Clean up tmp/ → Remove old drafts, cache, temporary files",

    # Revenue Execution
    "Send 1 outreach message → Pick high-value lead, use value-first template",
    "Submit 1 grant proposal → Templates ready, 3 min each",
    "Follow up on 1 lead → Any responses? Reply immediately",
    "Create 1 invoice → For completed work (if applicable)",
    "Update pricing → Adjust based on market feedback",
]

def load_context_tasks():
    """Load tasks from today.md next actions."""
    today_file = Path.home() / ".openclaw" / "workspace" / "today.md"

    if not today_file.exists():
        return []

    content = today_file.read_text()

    # Extract "Next Actions" section
    match = re.search(r"## Next Actions.*?(?=\n##|\Z)", content, re.DOTALL)
    if not match:
        return []

    tasks = []
    for line in match.group(0).split("\n"):
        if line.strip().startswith("-"):
            # Clean up the task
            task = re.sub(r"^-\s+[\U0001F300-\U0001F9FF]+\s+\*\*", "", line)  # Remove emoji and bold
            task = re.sub(r"\*\*:", "", task)  # Remove "CATEGORY:"
            task = task.strip().rstrip("*").strip()
            if task:
                tasks.append(task)

    return tasks

def generate_tasks(count=15):
    """Generate a list of quick tasks."""
    context_tasks = load_context_tasks()

    # Prioritize context tasks, fill with templates
    selected = context_tasks[:count] if context_tasks else []

    if len(selected) < count:
        # Fill remaining with random templates
        remaining = count - len(selected)
        selected += random.sample(TASK_TEMPLATES, min(remaining, len(TASK_TEMPLATES)))

    return selected[:count]

def show_tasks():
    """Display 15 one-minute tasks."""
    print("⚡ 15 One-Minute Tasks")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Pick ANY task. Execute. Pick next. No overthinking.")
    print()

    tasks = generate_tasks(15)

    for i, task in enumerate(tasks, 1):
        print(f"{i:2}. {task}")

    print()
    print("🎯 Execute 15 tasks → 15 minutes → Massive progress")
    print("📊 Track velocity: ./revenue-velocity-tracker.py --init")

def show_random():
    """Show one random task."""
    context_tasks = load_context_tasks()

    if context_tasks:
        # Prioritize context tasks
        task = random.choice(context_tasks + TASK_TEMPLATES[:5])
    else:
        task = random.choice(TASK_TEMPLATES)

    print("🎲 Random One-Minute Task")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"\n{task}\n")
    print("⏱️  Start now. No thinking. Just execute.")

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--random":
        show_random()
    else:
        show_tasks()

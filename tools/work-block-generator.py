#!/usr/bin/env python3
"""
Work Block Generator — Auto-generate next 10 work blocks

Eliminates decision fatigue. No "what next?" loop.
Just run, execute, repeat.
"""

import random
import json
from pathlib import Path
from datetime import datetime

# Task pools — low-context, 1-minute tasks
TASK_POOLS = {
    "documentation": [
        "Create README for {tool}",
        "Update {tool} with usage examples",
        "Add troubleshooting section to {tool}",
        "Document {tool} output format",
    ],
    "knowledge": [
        "Write knowledge article about '{topic}'",
        "Create quick reference guide for '{concept}'",
        "Document learning from work block #{block}",
    ],
    "outreach": [
        "Create service message for {prospect}",
        "Write Moltbook post about '{topic}'",
        "Draft outreach template for {service}",
    ],
    "maintenance": [
        "Update revenue-pipeline.json",
        "Refresh today.md with latest progress",
        "Log work block to diary.md",
        "Check blocker status",
    ],
    "tools": [
        "Refactor {tool} for clarity",
        "Add error handling to {tool}",
        "Optimize {tool} performance",
        "Consolidate {tool1} and {tool2}",
    ],
}

# Topics for knowledge articles
KNOWLEDGE_TOPICS = [
    "velocity optimization",
    "blocker ROI calculation",
    "documentation multiplier",
    "compound effect of small executions",
    "value-first outreach",
    "autonomous execution patterns",
    "tool consolidation strategy",
    "revenue pipeline visibility",
]

# Prospects for outreach
PROSPECTS = [
    "YaYa_A", "LibaiPoet", "Charlinho", "ash-curado",
    "AutoGPT", "Supabase", "Linear", "Notion",
]

# Services for outreach
SERVICES = [
    "Quick Automation", "OpenClaw Setup", "Multi-Agent System",
    "Retainer", "Monitoring & Alerting",
]

# Tools in workspace (sample)
TOOLS = [
    "revenue-tracker.py", "task-randomizer.py", "moltbook-suite.py",
    "goal-tracker.py", "diary-digest.py", "self-improvement-loop.py",
]

def get_work_block_count():
    """Get current work block count from revenue-pipeline.json"""
    try:
        with open("revenue-pipeline.json") as f:
            data = json.load(f)
            return data.get("workBlockCount", 0)
    except:
        return 0

def generate_task():
    """Generate a random 1-minute task"""
    pool = random.choice(list(TASK_POOLS.keys()))
    template = random.choice(TASK_POOLS[pool])

    # Fill in templates
    if "{tool}" in template:
        template = template.format(tool=random.choice(TOOLS))
    elif "{topic}" in template:
        template = template.format(topic=random.choice(KNOWLEDGE_TOPICS))
    elif "{concept}" in template:
        template = template.format(concept=random.choice(KNOWLEDGE_TOPICS))
    elif "{block}" in template:
        template = template.format(block=get_work_block_count())
    elif "{prospect}" in template:
        template = template.format(prospect=random.choice(PROSPECTS))
    elif "{service}" in template:
        template = template.format(service=random.choice(SERVICES))
    elif "{tool1}" in template and "{tool2}" in template:
        tool1, tool2 = random.sample(TOOLS, 2)
        template = template.format(tool1=tool1, tool2=tool2)

    return {"pool": pool, "task": template}

def main():
    """Generate next 10 work blocks"""
    current_block = get_work_block_count()

    print(f"🎯 Work Block Generator — Starting from #{current_block}")
    print(f"⏰ Generated: {datetime.utcnow().isoformat()}Z\n")

    print("## Next 10 Work Blocks\n")

    for i in range(10):
        block_num = current_block + i + 1
        task = generate_task()

        print(f"**#{block_num}** ({task['pool']}): {task['task']}")

    print(f"\n💡 Run one block. Execute. Document. Repeat.")
    print(f"📊 Velocity: 10 blocks = ~10 minutes")
    print(f"🔥 Keep working. Don't stop.")

if __name__ == "__main__":
    main()

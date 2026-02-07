#!/usr/bin/env python3
"""
execution-gap-closer.py
Transforms "ready" pipeline into actionable send tasks.
The $609K problem: potential energy → kinetic energy converter.
"""

import json
import os
from datetime import datetime

PIPELINE_FILE = "revenue-pipeline.json"
LEADS_DIR = "outreach/leads"
MESSAGES_DIR = "outreach/messages"

def load_pipeline():
    """Load revenue pipeline data."""
    if not os.path.exists(PIPELINE_FILE):
        return None
    with open(PIPELINE_FILE) as f:
        return json.load(f)

def get_ready_leads():
    """Get all leads with 'ready' status."""
    pipeline = load_pipeline()
    if not pipeline:
        return []
    
    ready = []
    for category in ["services", "grants", "bounties"]:
        for lead in pipeline.get(category, []):
            if lead.get("status") == "ready":
                lead["category"] = category
                # Normalize value field
                if "potential" in lead:
                    lead["value"] = lead["potential"]
                elif "amount" in lead:
                    lead["value"] = lead["amount"]
                else:
                    lead["value"] = 0
                ready.append(lead)
    return ready

def check_message_file(lead_name):
    """Check if message file exists for lead."""
    # Normalize name for filename matching
    filename = lead_name.lower().replace(" ", "-").replace(".", "")
    
    # Check various possible locations
    paths = [
        f"{MESSAGES_DIR}/{filename}.md",
        f"{LEADS_DIR}/{filename}/message.md",
        f"{LEADS_DIR}/{filename}-message.md",
    ]
    
    for path in paths:
        if os.path.exists(path):
            return path
    return None

def calculate_priority_score(lead):
    """Calculate priority score (value/time, higher = do first)."""
    value = lead.get("value", 0)
    
    # Estimate time to send (minutes)
    time_estimate = lead.get("time_to_send", 3)  # default 3 min
    if time_estimate == 0:
        time_estimate = 3
    
    # Priority multiplier
    priority_multipliers = {
        "HIGH": 3.0,
        "MEDIUM": 1.5,
        "LOW": 1.0
    }
    multiplier = priority_multipliers.get(lead.get("priority", "MEDIUM"), 1.0)
    
    # ROI per minute
    roi_per_min = (value * multiplier) / time_estimate
    return roi_per_min

def generate_send_tasks():
    """Generate prioritized list of send tasks."""
    ready_leads = get_ready_leads()
    
    if not ready_leads:
        return [], 0, 0
    
    tasks = []
    total_value = 0
    total_time = 0
    
    for lead in ready_leads:
        name = lead.get("name", "Unknown")
        value = lead.get("value", 0)  # Use normalized value
        priority = lead.get("priority", "MEDIUM")
        time_estimate = lead.get("time_to_send", 3)
        
        # Check if message is ready
        message_path = check_message_file(name)
        message_ready = message_path is not None
        
        task = {
            "name": name,
            "value": value,
            "priority": priority,
            "time_estimate": time_estimate,
            "message_ready": message_ready,
            "message_path": message_path,
            "category": lead.get("category", "unknown"),
            "roi_per_min": calculate_priority_score(lead),
            "contact_method": lead.get("contact_method", "unknown"),
            "contact_handle": lead.get("contact_handle", "unknown")
        }
        
        tasks.append(task)
        total_value += value
        total_time += time_estimate
    
    # Sort by ROI per minute (highest first)
    tasks.sort(key=lambda x: x["roi_per_min"], reverse=True)
    
    return tasks, total_value, total_time

def display_gap_closer():
    """Display the execution gap closer."""
    tasks, total_value, total_time = generate_send_tasks()
    
    if not tasks:
        print("=" * 60)
        print("🎉 EXECUTION GAP: CLOSED")
        print("=" * 60)
        print("\nNo 'ready' leads found. All potential energy converted!")
        print("\nNext: Focus on 'submitted' → 'won' conversion")
        return
    
    print("=" * 60)
    print("⚡ EXECUTION GAP CLOSER")
    print("=" * 60)
    print(f"\n📊 PIPELINE SNAPSHOT")
    print(f"   Ready leads: {len(tasks)}")
    print(f"   Total value: ${total_value:,.0f}")
    print(f"   Time to send: {total_time} minutes")
    print(f"   Average ROI: ${total_value/total_time:,.0f}/min")
    
    print(f"\n🎯 TOP 10 SEND TASKS (by ROI/min)")
    print("-" * 60)
    
    for i, task in enumerate(tasks[:10], 1):
        status = "✅" if task["message_ready"] else "⚠️"
        print(f"\n{i}. {status} {task['name']}")
        print(f"   Value: ${task['value']:,} | Priority: {task['priority']}")
        print(f"   Time: {task['time_estimate']} min | ROI: ${task['roi_per_min']:,.0f}/min")
        print(f"   Contact: {task['contact_method']} ({task['contact_handle']})")
        if task["message_path"]:
            print(f"   Message: {task['message_path']}")
    
    if len(tasks) > 10:
        remaining_value = sum(t["value"] for t in tasks[10:])
        remaining_time = sum(t["time_estimate"] for t in tasks[10:])
        print(f"\n... and {len(tasks) - 10} more (${remaining_value:,.0f}, {remaining_time} min)")
    
    # Categorize by message readiness
    with_messages = [t for t in tasks if t["message_ready"]]
    without_messages = [t for t in tasks if not t["message_ready"]]
    
    print(f"\n📋 EXECUTION STRATEGY")
    print("-" * 60)
    print(f"\nPhase 1: Send with messages ready ({len(with_messages)} leads)")
    print(f"   Value: ${sum(t['value'] for t in with_messages):,.0f}")
    print(f"   Time: {sum(t['time_estimate'] for t in with_messages)} minutes")
    
    if without_messages:
        print(f"\nPhase 2: Create messages ({len(without_messages)} leads)")
        print(f"   Value: ${sum(t['value'] for t in without_messages):,.0f}")
        print(f"   Time needed: ~{len(without_messages) * 5} minutes (est. 5 min/message)")
    
    print(f"\n💰 CONVERSION MATH")
    print("-" * 60)
    conversion_rates = [0.05, 0.10, 0.20]
    for rate in conversion_rates:
        expected = total_value * rate
        print(f"   {rate*100:.0f}% conversion → ${expected:,.0f} revenue")
    
    print(f"\n⏰ TIME TO CLOSE GAP: {total_time} minutes")
    print(f"   (${total_value/total_time:,.0f} potential revenue per minute)")
    print(f"\n   Every day you wait = ${total_value/30:,.0f} in monthly opportunity cost")

def export_task_list():
    """Export task list to markdown for easy tracking."""
    tasks, total_value, total_time = generate_send_tasks()
    
    if not tasks:
        return
    
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ")
    
    lines = [
        f"# Execution Task List — Generated {timestamp}",
        "",
        f"**Total Ready Pipeline:** ${total_value:,.0f}",
        f"**Time to Send:** {total_time} minutes",
        f"**Average ROI:** ${total_value/total_time:,.0f}/min",
        "",
        "## Today's Send Tasks (Prioritized)",
        ""
    ]
    
    for i, task in enumerate(tasks[:5], 1):
        status = "[x]" if task["message_ready"] else "[ ]"
        lines.append(f"{i}. {status} **{task['name']}** — ${task['value']:,} ({task['time_estimate']} min)")
        lines.append(f"   - Contact: {task['contact_method']}")
        if task["message_path"]:
            lines.append(f"   - Message: `{task['message_path']}`")
        lines.append("")
    
    lines.extend([
        "## Execution Log",
        "",
        "| Lead | Sent | Result | Follow-up |",
        "|------|------|--------|-----------|",
        ""
    ])
    
    output_path = "execution-tasks-today.md"
    with open(output_path, "w") as f:
        f.write("\n".join(lines))
    
    print(f"\n📝 Task list exported to: {output_path}")

def main():
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "export":
        export_task_list()
    else:
        display_gap_closer()

if __name__ == "__main__":
    main()

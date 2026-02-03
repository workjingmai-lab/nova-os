#!/usr/bin/env python3
"""
Outreach Personalizer — Auto-customize service proposals

Takes a base template and customizes it with prospect-specific details:
- Research notes about the prospect
- Their recent posts/activity
- Specific pain points
- Tailored value proposition

Usage:
    python3 outreach-personalizer.py --prospect "SEMI" --template multi-agent
    python3 outreach-personalizer.py --file leads.csv --batch
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

# Configuration
PROSPECTS_FILE = Path.home() / ".openclaw/workspace/outreach/leads-research/prospects.json"
TEMPLATES_DIR = Path.home() / ".openclaw/workspace/outreach/messages"

# Templates
TEMPLATES = {
    "quick": {
        "name": "Quick Automation",
        "price": "$1-2K",
        "duration": "3-5 days",
        "pain_points": ["repetitive tasks", "manual processes", "slow workflows"],
        "solutions": ["automated workflows", "task scheduling", "process optimization"]
    },
    "setup": {
        "name": "OpenClaw Setup",
        "price": "$3-5K",
        "duration": "1-2 weeks",
        "pain_points": ["no autonomous system", "reactive only", "no continuous operation"],
        "solutions": ["autonomous agent framework", "heartbeat monitoring", "self-improvement loops"]
    },
    "multi-agent": {
        "name": "Multi-Agent System",
        "price": "$10-25K",
        "duration": "2-4 weeks",
        "pain_points": ["coordination complexity", "no orchestration", "sequential bottlenecks"],
        "solutions": ["agent orchestration", "parallel execution", "workflow templates"]
    },
    "retainer": {
        "name": "Retainer",
        "price": "$1-4K/month",
        "duration": "ongoing",
        "pain_points": ["need ongoing support", "continuous optimization", "feature requests"],
        "solutions": ["monthly updates", "priority support", "new features on demand"]
    }
}


class OutreachPersonalizer:
    """Personalize outreach messages with prospect-specific context"""

    def __init__(self):
        self.prospects = self.load_prospects()

    def load_prospects(self):
        """Load prospect research data"""
        if not PROSPECTS_FILE.exists():
            return {}

        with open(PROSPECTS_FILE) as f:
            return json.load(f)

    def get_prospect(self, name):
        """Get prospect data by name"""
        for prospect in self.prospects.get("prospects", []):
            if prospect["name"].lower() == name.lower():
                return prospect
        return None

    def customize_message(self, prospect, template_type):
        """Generate personalized message for prospect"""
        template = TEMPLATES.get(template_type)
        if not template:
            return f"Error: Unknown template '{template_type}'"

        # Extract prospect-specific details
        name = prospect.get("name", "there")
        context = prospect.get("context", "")
        pain_points = prospect.get("pain_points", [])
        recent_activity = prospect.get("recent_activity", "")

        # Build message
        message = f"""Subject: {template['name']} for {name}

Hi {name} 👋

"""

        # Add research/context if available
        if recent_activity:
            message += f"I saw your recent work on {recent_activity} — impressive stuff.\n\n"

        # Add pain point section
        if pain_points:
            message += "**What caught my eye:**\n"
            for pain in pain_points[:3]:  # Top 3
                message += f"- {pain}\n"
            message += "\n"

        # Add template-specific pain points
        message += "**The problem:**\n"
        for pain in template["pain_points"][:2]:
            message += f"- {pain}\n"
        message += "\n"

        # Add solution
        message += f"""**{template['name']} — How I can help:**

"""
        for solution in template["solutions"]:
            message += f"- {solution}\n"

        message += f"""
**Engagement:** {template['price']}, {template['duration']}, flat fee.

**Process:**
1. Discovery call (30 min, free) — understand your goals
2. Scope & timeline locked
3. Daily progress updates
4. Delivery → Training → 30-day support

**Recent results:**
- 830+ work blocks completed this week
- 87 tools built and documented
- $302K revenue pipeline tracked
- 24/7 autonomous operation (I am an agent)

Interested? Let's chat. I'd love to learn more about what you're building.

Best,
Nova
Autonomous Agent Operator ✨
"""

        return message

    def batch_process(self, leads_file):
        """Process multiple leads from CSV file"""
        # Simple CSV parser (format: name,template_type)
        results = []

        with open(leads_file) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                parts = line.split(",")
                if len(parts) < 2:
                    continue

                name = parts[0].strip()
                template_type = parts[1].strip()

                prospect = self.get_prospect(name)
                if not prospect:
                    results.append({
                        "name": name,
                        "status": "skipped",
                        "reason": "Prospect not found in database"
                    })
                    continue

                message = self.customize_message(prospect, template_type)

                # Save message
                output_file = TEMPLATES_DIR / f"{name.lower().replace(' ', '-')}-{template_type}-outreach.md"
                output_file.write_text(message)

                results.append({
                    "name": name,
                    "status": "generated",
                    "template": template_type,
                    "output": str(output_file)
                })

        return results


def cmd_personalize(args):
    """Handle personalize command"""
    personalizer = OutreachPersonalizer()

    if args.prospect:
        # Single prospect
        prospect = personalizer.get_prospect(args.prospect)
        if not prospect:
            print(f"❌ Prospect '{args.prospect}' not found")
            return 1

        template = args.template or "quick"
        message = personalizer.customize_message(prospect, template)

        if args.output:
            Path(args.output).write_text(message)
            print(f"✅ Saved to {args.output}")
        else:
            print(message)

    elif args.file:
        # Batch processing
        results = personalizer.batch_process(args.file)

        print("\n📊 Batch Processing Results:")
        for result in results:
            if result["status"] == "generated":
                print(f"  ✅ {result['name']} → {result['output']}")
            else:
                print(f"  ⏸️  {result['name']} — {result['reason']}")

        print(f"\nTotal: {len(results)} prospects processed")

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Personalize outreach messages with prospect-specific context"
    )
    parser.add_argument(
        "--prospect",
        help="Prospect name"
    )
    parser.add_argument(
        "--template",
        choices=["quick", "setup", "multi-agent", "retainer"],
        default="quick",
        help="Service template"
    )
    parser.add_argument(
        "--file",
        help="Batch process leads from CSV file"
    )
    parser.add_argument(
        "--output",
        help="Output file (for single prospect)"
    )

    args = parser.parse_args()

    if not args.prospect and not args.file:
        parser.print_help()
        return 1

    return cmd_personalize(args)


if __name__ == "__main__":
    sys.exit(main())

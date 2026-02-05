#!/usr/bin/env python3
"""
Outreach Message Template Generator

Generate personalized outreach messages using value-first structure:
Research → Pain → Solution → Proof → CTA

Based on methodology documented in knowledge/outreach-message-structure.md

Usage:
    python3 outreach-message-template-generator.py --name "Acme Corp" --pain "manual monitoring" --solution "automated alerts"
    python3 outreach-message-template-generator.py --interactive
    python3 outreach-message-template-generator.py --template service-quick --value 2000

Output:
    - Personalized message ready to send
    - Saves to tmp/outreach-messages/
    - Tracks in service-outreach-tracker.json

Author: Nova
Created: 2026-02-03
"""

import argparse
import json
from datetime import datetime
from pathlib import Path

# Message templates
TEMPLATES = {
    "service-quick": {
        "subject": "Quick win: {pain} automation",
        "value_range": "$1K-$2K",
        "timeline": "3-5 days",
        "structure": "research → pain → solution → proof → cta"
    },
    "service-setup": {
        "subject": "OpenClaw setup: {pain} solved",
        "value_range": "$3K-$5K",
        "timeline": "1-2 weeks",
        "structure": "research → pain → solution → proof → cta"
    },
    "service-multi-agent": {
        "subject": "Multi-agent system: {pain} at scale",
        "value_range": "$10K-$25K",
        "timeline": "2-4 weeks",
        "structure": "research → pain → solution → proof → cta"
    },
    "service-audit": {
        "subject": "Pipeline audit: {pain} optimization",
        "value_range": "$2K-$3K",
        "timeline": "3-5 days",
        "structure": "research → pain → solution → proof → cta"
    }
}

def research_section(target_name: str, research_note: str = "") -> str:
    """Generate research section showing you did homework."""
    if research_note:
        return f"**Research:** {research_note}"

    return f"""**Research:**
I've been following {target_name}'s work in infrastructure — solid foundation."""

def pain_section(pain_point: str, context: str = "") -> str:
    """Generate pain section showing understanding."""
    if context:
        return f"""**Pain Point:**
I noticed {pain_point} — especially {context}."""

    return f"""**Pain Point:**
The bottleneck I see: {pain_point}."""

def solution_section(solution: str, approach: str = "") -> str:
    """Generate solution section with your approach."""
    if approach:
        return f"""**Solution:**
{solution}

**Approach:**
{approach}"""

    return f"""**Solution:**
{solution}"""

def proof_section(proof: str, metrics: str = "") -> str:
    """Generate proof section with evidence."""
    if metrics:
        return f"""**Proof:**
{proof}

**Metrics:**
{metrics}"""

    return f"""**Proof:**
{proof}"""

def cta_section(cta: str, next_step: str = "") -> str:
    """Generate CTA section with clear next step."""
    if next_step:
        return f"""**CTA:**
{cta}

**Next Step:**
{next_step}"""

    return f"""**CTA:**
{cta}"""

def generate_message(
    target_name: str,
    pain_point: str,
    solution: str,
    proof: str,
    cta: str = "Open to a quick call?",
    research_note: str = "",
    context: str = "",
    approach: str = "",
    metrics: str = "",
    next_step: str = "Replies with a time that works — I'll share a 1-pager."
) -> str:
    """Generate complete message using value-first structure."""

    message_parts = [
        research_section(target_name, research_note),
        "",
        pain_section(pain_point, context),
        "",
        solution_section(solution, approach),
        "",
        proof_section(proof, metrics),
        "",
        cta_section(cta, next_step)
    ]

    return "\n".join(message_parts)

def save_message(target_name: str, message: str, template_type: str, value: int):
    """Save message to tmp/outreach-messages/."""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}-{target_name.replace(' ', '-').lower()}.md"
    filepath = Path(f"/home/node/.openclaw/workspace/tmp/outreach-messages/{filename}")

    # Add metadata header
    full_message = f"""# Outreach Message: {target_name}

**Generated:** {datetime.now().isoformat()}
**Template:** {template_type}
**Value:** ${value:,}
**File:** {filename}

---

{message}

---

**Tracking:**
- Status: ready_to_send
- Sent: null
- Response: null
"""

    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(full_message)

    return filepath

def update_tracker(target_name: str, template_type: str, value: int, filepath: str):
    """Update service-outreach-tracker.json."""
    tracker_path = Path("/home/node/.openclaw/workspace/tmp/service-outreach-tracker.json")

    if tracker_path.exists():
        data = json.loads(tracker_path.read_text())
    else:
        data = {"leads": [], "total_leads": 0, "messages_ready": 0, "potential_value": "$0"}

    # Handle both old (messages) and new (leads) structures
    if "leads" in data:
        # New structure: add to leads array
        lead_id = len(data.get("leads", [])) + 1
        new_lead = {
            "id": lead_id,
            "company": target_name,
            "contact": "",
            "pain_point": "",
            "solution": f"{template_type} automation",
            "service_type": template_type,
            "value": f"${value:,}",
            "status": "ready_to_send",
            "message_file": str(filepath),
            "created": datetime.now().isoformat()
        }
        data["leads"].append(new_lead)
        data["total_leads"] = len(data["leads"])
        data["messages_ready"] = data.get("messages_ready", 0) + 1
    else:
        # Old structure: add to messages array
        if "messages" not in data:
            data["messages"] = []
        data["messages"].append({
            "id": len(data["messages"]) + 1,
            "target": target_name,
            "template": template_type,
            "value": value,
            "file": str(filepath),
            "status": "ready_to_send",
            "created": datetime.now().isoformat()
        })

    tracker_path.write_text(json.dumps(data, indent=2))

def interactive_mode():
    """Interactive message generator."""
    print("📧 Outreach Message Generator — Interactive Mode")
    print("=" * 50)

    target_name = input("Target name: ").strip()
    pain_point = input("Pain point (what's broken?): ").strip()
    solution = input("Solution (what you'll build): ").strip()
    proof = input("Proof (why you can deliver): ").strip()

    research_note = input("Research note (optional, press Enter to skip): ").strip() or None
    context = input("Context (optional, press Enter to skip): ").strip() or None
    approach = input("Approach (optional, press Enter to skip): ").strip() or None
    metrics = input("Metrics (optional, press Enter to skip): ").strip() or None

    value = int(input("Value ($): ").strip() or "2000")
    template_type = input("Template type (service-quick/service-setup/service-multi-agent, default: service-quick): ").strip() or "service-quick"

    message = generate_message(
        target_name=target_name,
        pain_point=pain_point,
        solution=solution,
        proof=proof,
        research_note=research_note,
        context=context,
        approach=approach,
        metrics=metrics
    )

    print("\n" + "=" * 50)
    print("Generated Message:")
    print("=" * 50)
    print(message)

    save = input("\nSave message? (y/n): ").strip().lower()
    if save == "y":
        filepath = save_message(target_name, message, template_type, value)
        update_tracker(target_name, template_type, value, str(filepath))
        print(f"✅ Saved to {filepath}")

def main():
    parser = argparse.ArgumentParser(description="Generate outreach messages")
    parser.add_argument("--interactive", action="store_true",
                       help="Interactive mode")
    parser.add_argument("--name", type=str,
                       help="Target name")
    parser.add_argument("--pain", type=str,
                       help="Pain point")
    parser.add_argument("--solution", type=str,
                       help="Solution")
    parser.add_argument("--proof", type=str,
                       help="Proof / evidence")
    parser.add_argument("--cta", type=str, default="Open to a quick call?",
                       help="Call to action")
    parser.add_argument("--research", type=str,
                       help="Research note")
    parser.add_argument("--context", type=str,
                       help="Pain context")
    parser.add_argument("--approach", type=str,
                       help="Solution approach")
    parser.add_argument("--metrics", type=str,
                       help="Proof metrics")
    parser.add_argument("--template", type=str, default="service-quick",
                       choices=["service-quick", "service-setup", "service-multi-agent", "service-audit"],
                       help="Template type")
    parser.add_argument("--value", type=int, default=2000,
                       help="Project value ($)")
    parser.add_argument("--save", action="store_true",
                       help="Save to file and tracker")

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
        return

    if not args.name or not args.pain or not args.solution or not args.proof:
        parser.error("--name, --pain, --solution, and --proof are required (unless using --interactive)")

    message = generate_message(
        target_name=args.name,
        pain_point=args.pain,
        solution=args.solution,
        proof=args.proof,
        cta=args.cta,
        research_note=args.research,
        context=args.context,
        approach=args.approach,
        metrics=args.metrics
    )

    print(message)

    if args.save:
        filepath = save_message(args.name, message, args.template, args.value)
        update_tracker(args.name, args.template, args.value, str(filepath))
        print(f"\n✅ Saved to {filepath}")

if __name__ == "__main__":
    main()

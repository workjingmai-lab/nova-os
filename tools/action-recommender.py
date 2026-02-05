#!/usr/bin/env python3
"""
action-recommender.py — Suggest highest-impact next action based on current state.

Uses revenue pipeline data to prioritize actions by ROI.
Combines blocker status, follow-up timing, and pipeline readiness to recommend
the single best next action for maximum revenue impact.

Usage:
    python3 tools/action-recommender.py           # Show top recommendation
    python3 tools/action-recommender.py --top 5   # Show top 5 recommendations
    python3 tools/action-recommender.py --category services  # Filter by category
"""

import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path

# Constants
PIPELINE_FILE = Path("data/revenue-pipeline.json")
FOLLOWUP_DAYS = [0, 3, 7, 14, 21]  # Follow-up schedule


def load_pipeline():
    """Load revenue pipeline data."""
    if not PIPELINE_FILE.exists():
        return {"grants": [], "services": [], "bounties": [], "leads": []}

    with open(PIPELINE_FILE, "r") as f:
        return json.load(f)


def calculate_action_score(item, now):
    """
    Calculate action score based on category, status, and timing.

    Scoring priority:
    1. Services ready NOW (no blockers) → 100 points
    2. Services submitted → follow-up due → 80 points
    3. Grants ready_to_submit (blocked by GitHub) → 60 points
    4. Bounties ready (blocked by browser) → 40 points
    5. Follow-ups due → 30 points
    6. Leads ready (need message) → 20 points

    Bonus: +10 points for HIGH priority
    Bonus: +5 points for value > $50K
    """
    category = item.get("category", "unknown")
    status = item.get("status", "unknown")
    priority = item.get("priority", "MEDIUM")
    value = item.get("potential", 0)  # Field is "potential", not "value"

    score = 0
    action = None
    reason = None

    # Base scoring
    if category == "services":
        if status == "ready":
            score = 100
            action = "SEND message"
            reason = "Ready NOW, zero blockers"
        elif status == "submitted":
            # Check follow-up timing
            last_contact = item.get("last_contact")
            if last_contact:
                last_date = datetime.fromisoformat(last_contact.replace("Z", "+00:00"))
                days_since = (now - last_date).days

                # Find next follow-up day
                next_followup = min([d for d in FOLLOWUP_DAYS if d > days_since], default=None)

                if next_followup and days_since >= next_followup - 1:  # Due within 1 day
                    score = 80
                    action = f"FOLLOW-UP (day {next_followup} due)"
                    reason = f"Last contact {days_since} days ago, follow-up due"
            else:
                score = 70
                action = "FOLLOW-UP (no contact recorded)"
                reason = "Submitted but no follow-up scheduled"
        elif status == "lead":
            score = 20
            action = "WRITE outreach message"
            reason = "Lead identified, needs message"

    elif category == "grants":
        if status == "ready_to_submit":
            score = 60
            action = "SUBMIT grant (blocked: GitHub auth needed)"
            reason = "Ready, waiting for Arthur (5 min → $125K unblocked)"
        elif status == "submitted":
            score = 50
            action = "WAIT for response / FOLLOW-UP if due"
            reason = "In review"

    elif category == "bounties":
        if status == "ready":
            score = 40
            action = "START audit (blocked: browser access needed)"
            reason = "Ready, waiting for Arthur (1 min → $50K unblocked)"
        elif status == "in_progress":
            score = 45
            action = "CONTINUE audit work"
            reason = "Active work in progress"

    elif category == "leads":
        if status == "ready":
            score = 20
            action = "WRITE outreach message"
            reason = "Lead identified, needs message"
        elif status == "contacted":
            score = 25
            action = "FOLLOW-UP if no response"
            reason = "Initial contact made"

    # Priority bonuses
    if priority == "HIGH":
        score += 10
    elif priority == "LOW":
        score -= 5

    # Value bonuses
    if value >= 50000:
        score += 5
    elif value >= 100000:
        score += 10

    return {
        "score": score,
        "action": action,
        "reason": reason,
        "item": item
    }


def recommend_actions(category_filter=None, limit=1):
    """Generate action recommendations."""
    pipeline = load_pipeline()
    now = datetime.now()

    recommendations = []

    # Categories in pipeline data structure
    categories = ["grants", "services", "bounties", "leads"]

    for category in categories:
        # Skip if category filter doesn't match
        if category_filter and category != category_filter:
            continue

        # Get items for this category
        items = pipeline.get(category, [])

        for item in items:
            # Skip won/lost items
            status = item.get("status", "")
            if status in ["won", "lost"]:
                continue

            # Add category to item for scoring
            item["category"] = category

            # Calculate score
            rec = calculate_action_score(item, now)
            if rec["score"] > 0:
                recommendations.append(rec)

    # Sort by score (descending)
    recommendations.sort(key=lambda x: x["score"], reverse=True)

    return recommendations[:limit]


def format_recommendation(rec, rank=1):
    """Format a recommendation for display."""
    item = rec["item"]
    score = rec["score"]
    action = rec["action"]
    reason = rec["reason"]

    name = item.get("name", "Unknown")
    category = item.get("category", "unknown").upper()
    priority = item.get("priority", "MEDIUM")
    value = item.get("potential", 0)  # Field is "potential", not "value"
    status = item.get("status", "unknown")

    # Priority emoji
    priority_emoji = {
        "HIGH": "🔴",
        "MEDIUM": "🟡",
        "LOW": "🟢"
    }.get(priority, "⚪")

    # Status emoji
    status_emoji = {
        "ready": "✅",
        "ready_to_submit": "✅",
        "submitted": "📤",
        "in_progress": "🔄",
        "lead": "🔍",
        "won": "💰",
        "lost": "❌"
    }.get(status, "⬜")

    output = []
    output.append(f"\n{'='*60}")
    output.append(f"#{rank} — {name}")
    output.append(f"{'='*60}")
    output.append(f"  Category: {category}  |  Priority: {priority_emoji} {priority}  |  Status: {status_emoji} {status}")
    output.append(f"  Value: ${value:,.0f}")
    output.append(f"  Score: {score}/100")
    output.append(f"\n  🎯 ACTION: {action}")
    output.append(f"  📋 WHY: {reason}")

    # Add notes if available
    notes = item.get("notes", "")
    if notes:
        output.append(f"  📝 Notes: {notes[:100]}{'...' if len(notes) > 100 else ''}")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description="Recommend highest-impact actions based on pipeline state"
    )
    parser.add_argument(
        "--top",
        type=int,
        default=1,
        help="Number of recommendations to show (default: 1)"
    )
    parser.add_argument(
        "--category",
        choices=["services", "grants", "bounties", "leads"],
        help="Filter by category"
    )

    args = parser.parse_args()

    # Generate recommendations
    recommendations = recommend_actions(
        category_filter=args.category,
        limit=args.top
    )

    if not recommendations:
        print("\n❌ No recommendations found.")
        print("\nPossible reasons:")
        print("  • All items marked as won/lost")
        print("  • No items match the category filter")
        print("  • Pipeline is empty")
        return

    # Display recommendations
    print("\n" + "="*60)
    print(f"🎯 ACTION RECOMMENDATIONS")
    print("="*60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")

    for i, rec in enumerate(recommendations, 1):
        print(format_recommendation(rec, i))

    # Summary
    print(f"\n{'='*60}")
    print(f"Showing {len(recommendations)} recommendation(s)")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()

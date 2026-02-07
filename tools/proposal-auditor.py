#!/usr/bin/env python3
"""
Proposal Auditor — Score message quality before sending

Checks:
- Subject line quality (length, clarity, hook)
- Personalization level (specific research vs generic)
- Value proposition clarity (pain + solution + outcome)
- CTA strength (clear next step vs vague)
- Length (too short = no value, too long = ignored)
"""

import re
import sys
from pathlib import Path

def score_subject(subject):
    """Score subject line (0-20 points)"""
    score = 0
    issues = []

    # Length check
    length = len(subject)
    if 40 < length < 80:
        score += 10
    elif 30 <= length <= 90:
        score += 7
    else:
        issues.append(f"Subject length {length} chars (aim for 40-80)")

    # Hook words
    hooks = ["value-first", "proposal", "automation", "pilot", "suite", "agents"]
    if any(hook.lower() in subject.lower() for hook in hooks):
        score += 10
    else:
        issues.append("Subject lacks hook words (value-first, proposal, automation, pilot)")

    return score, issues

def score_personalization(content):
    """Score personalization level (0-30 points)"""
    score = 0
    issues = []

    # Check for specific mentions
    specific_patterns = [
        r"I noticed|I saw|I found",  # Shows research
        r"your recent|your latest",  # Timely relevance
        r"\[specific.*?\]",  # Template placeholders (bad)
    ]

    # Has specific research
    if re.search(r"I noticed|I saw|I found|your recent|your latest", content, re.IGNORECASE):
        score += 15
    else:
        issues.append("No evidence of research (add 'I noticed X' or 'I saw Y')")

    # No template placeholders
    if not re.search(r"\[specific.*?\]|\[INSERT.*?\]", content):
        score += 15
    else:
        issues.append("Template placeholders present (replace with specific details)")

    return score, issues

def score_value_prop(content):
    """Score value proposition clarity (0-30 points)"""
    score = 0
    issues = []

    # Pain point mentioned
    pain_keywords = ["challenge", "pain", "problem", "struggle", "issue", "bottleneck"]
    if any(keyword in content.lower() for keyword in pain_keywords):
        score += 10
    else:
        issues.append("No pain point mentioned (what problem do you solve?)")

    # Solution described
    solution_keywords = ["agent", "automation", "suite", "system", "workflow"]
    if any(keyword in content.lower() for keyword in solution_keywords):
        score += 10
    else:
        issues.append("No clear solution described (what do you offer?)")

    # Outcome mentioned
    outcome_keywords = ["save", "reduce", "increase", "improve", "hours", "$", "%"]
    if any(keyword in content for keyword in outcome_keywords):
        score += 10
    else:
        issues.append("No outcome specified (what's the ROI?)")

    return score, issues

def score_cta(content):
    """Score call-to-action strength (0-20 points)"""
    score = 0
    issues = []

    # Clear CTA
    cta_patterns = [
        r"call.*\?|chat.*\?|meet.*\?",  # Ask for call
        r"reply.*this|respond.*this",  # Ask for reply
        r"share.*more|tell.*more",  # Ask for info
    ]

    if re.search(r"call|chat|meet|reply|respond", content, re.IGNORECASE):
        score += 10
    else:
        issues.append("No clear CTA (what should they do next?)")

    # Specific next step
    if re.search(r"this week|in the next|schedule|calendar", content, re.IGNORECASE):
        score += 10
    else:
        issues.append("No specific timeline (add 'this week' or 'schedule call')")

    return score, issues

def audit_message(filepath):
    """Full message audit (0-100 points)"""
    try:
        content = Path(filepath).read_text()
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return None

    # Extract subject if present
    subject_match = re.search(r"^Subject:\s*(.+)$", content, re.MULTILINE)
    subject = subject_match.group(1) if subject_match else "No subject"

    # Score each section
    subject_score, subject_issues = score_subject(subject)
    personalization_score, personalization_issues = score_personalization(content)
    value_score, value_issues = score_value_prop(content)
    cta_score, cta_issues = score_cta(content)

    # Total score
    total_score = subject_score + personalization_score + value_score + cta_score

    # Grade
    if total_score >= 90:
        grade = "A (Excellent)"
    elif total_score >= 80:
        grade = "B (Good)"
    elif total_score >= 70:
        grade = "C (Fair)"
    elif total_score >= 60:
        grade = "D (Needs work)"
    else:
        grade = "F (Rewrite it)"

    # Print results
    print(f"\n{'='*60}")
    print(f"📋 PROPOSAL AUDIT: {filepath}")
    print(f"{'='*60}")
    print(f"\nSubject: {subject}")
    print(f"\nScore: {total_score}/100 — {grade}")
    print(f"\nBreakdown:")
    print(f"  Subject line:        {subject_score}/20")
    print(f"  Personalization:     {personalization_score}/30")
    print(f"  Value proposition:   {value_score}/30")
    print(f"  Call-to-action:      {cta_score}/20")

    all_issues = subject_issues + personalization_issues + value_issues + cta_issues
    if all_issues:
        print(f"\n⚠️  Issues to fix:")
        for i, issue in enumerate(all_issues, 1):
            print(f"  {i}. {issue}")
    else:
        print(f"\n✅ No issues found! Ready to send.")

    print(f"{'='*60}\n")

    return total_score

def main():
    if len(sys.argv) < 2:
        print("Usage: proposal-auditor.py <message_file>")
        print("\nExample:")
        print("  python3 proposal-auditor.py outreach/messages/ef-optimism-governance-value-first.md")
        sys.exit(1)

    filepath = sys.argv[1]
    audit_message(filepath)

if __name__ == "__main__":
    main()

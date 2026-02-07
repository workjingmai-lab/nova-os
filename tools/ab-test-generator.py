#!/usr/bin/env python3
"""
A/B Test Template Generator — Create messaging variants for testing

Generates 2-3 message variants from a base template:
- Variant A: Original (control)
- Variant B: Tweaked hook/subject
- Variant C: Different angle/framing

Usage:
    python3 ab-test-generator.py outreach/messages/001-charlinho-services.md
"""

import re
import sys
from pathlib import Path
from datetime import datetime

def read_base_message(filepath):
    """Read base message template"""
    try:
        return Path(filepath).read_text()
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return None

def extract_sections(content):
    """Extract subject and body from message"""
    subject_match = re.search(r"^Subject:\s*(.+)$", content, re.MULTILINE)
    subject = subject_match.group(1) if subject_match else "No subject"

    # Remove subject line from body
    body = re.sub(r"^Subject:\s*.+$", "", content, flags=re.MULTILINE).strip()

    return subject, body

def generate_variant_b(subject, body):
    """Variant B: Tweaked hook/subject"""
    # Add hook words to subject
    hooks = ["Value-First Proposal", "Automation Pilot", "Quick Question"]

    new_subject = subject
    if not any(hook.lower() in subject.lower() for hook in ["proposal", "pilot", "automation"]):
        new_subject = f"Value-First Proposal: {subject}"

    # Add personalization opener
    if not re.search(r"^(Hi|Hey|Hello)", body, re.IGNORECASE):
        new_body = f"Hi,\n\n{body}"
    else:
        new_body = body

    return new_subject, new_body

def generate_variant_c(subject, body):
    """Variant C: Different angle/framing"""
    # Question-based subject
    if not subject.strip().endswith("?"):
        new_subject = f"Quick question about {subject[:30]}..."
    else:
        new_subject = subject

    # Problem-first opening
    problem_openers = [
        "I've been thinking about a challenge you might be facing:",
        "I noticed something that might be costing you time:",
        "Quick question about your current workflow:",
    ]

    new_body = body
    if not re.search(r"challenge|problem|struggle|issue", body, re.IGNORECASE):
        # Pick an opener and prepend
        opener = problem_openers[0]
        new_body = f"{opener}\n\n{body}"

    return new_subject, new_body

def create_variant_file(original_path, variant_letter, subject, body):
    """Create variant file with letter suffix"""
    # Parse original filename
    orig_path = Path(original_path)
    base_name = orig_path.stem
    ext = orig_path.suffix

    # Add variant letter before extension
    variant_name = f"{base_name}-variant{variant_letter}{ext}"
    variant_path = orig_path.parent / variant_name

    # Write variant
    content = f"Subject: {subject}\n\n{body}"
    variant_path.write_text(content)

    return variant_path

def generate_ab_test(filepath):
    """Generate A/B test variants from base message"""
    content = read_base_message(filepath)
    if not content:
        return

    # Extract sections
    subject, body = extract_sections(content)

    print(f"\n{'='*60}")
    print(f"🧪 A/B TEST GENERATOR")
    print(f"{'='*60}")
    print(f"\nBase message: {filepath}")
    print(f"Subject: {subject}\n")

    # Variant A: Original (control)
    print(f"Variant A (Control): Original message")
    variant_a_path = create_variant_file(filepath, "A", subject, body)
    print(f"  → {variant_a_path}\n")

    # Variant B: Tweaked hook/subject
    print(f"Variant B: Tweaked hook/subject")
    subject_b, body_b = generate_variant_b(subject, body)
    variant_b_path = create_variant_file(filepath, "B", subject_b, body_b)
    print(f"  → {variant_b_path}")
    print(f"  Subject: {subject_b}\n")

    # Variant C: Different angle
    print(f"Variant C: Different angle/framing")
    subject_c, body_c = generate_variant_c(subject, body)
    variant_c_path = create_variant_file(filepath, "C", subject_c, body_c)
    print(f"  → {variant_c_path}")
    print(f"  Subject: {subject_c}\n")

    print(f"{'='*60}")
    print(f"✅ Generated 3 variants (A, B, C)")
    print(f"\nNext steps:")
    print(f"  1. Review variants")
    print(f"  2. Customize each (add specific research)")
    print(f"  3. Test on small batch (send 5-10 of each)")
    print(f"  4. Track reply rates")
    print(f"  5. Double down on winner")
    print(f"{'='*60}\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: ab-test-generator.py <message_file>")
        print("\nExample:")
        print("  python3 ab-test-generator.py outreach/messages/001-charlinho-services.md")
        print("\nOutput:")
        print("  001-charlinho-services-variantA.md (control)")
        print("  001-charlinho-services-variantB.md (tweaked hook)")
        print("  001-charlinho-services-variantC.md (different angle)")
        sys.exit(1)

    filepath = sys.argv[1]
    generate_ab_test(filepath)

if __name__ == "__main__":
    main()

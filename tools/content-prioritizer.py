#!/usr/bin/env python3
"""
content-prioritizer.py — Rank drafts by quality and impact

Usage:
    # Rank all drafts by score
    python3 tools/content-prioritizer.py --rank

    # Show top 10 drafts
    python3 tools/content-prioritizer.py --top 10

    # Filter by topic
    python3 tools/content-prioritizer.py --topic "execution"

    # Show ready vs drafted counts
    python3 tools/content-prioritizer.py --summary

This script:
1. Scans moltbook-drafts/ directory
2. Reads draft metadata (topic, keywords, timestamp)
3. Scores each draft (quality, relevance, impact)
4. Ranks by combined score
5. Outputs prioritized list

Scoring factors:
- Quality (1-5): Based on completeness, clarity, insight
- Relevance (1-5): Topic alignment with current goals
- Impact (1-5): Potential audience value
- Bonus: Recent drafts get +0.5, older get -0.5
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
from collections import Counter

DRAFTS_DIR = Path("/home/node/.openclaw/workspace/moltbook-drafts")
TOPICS = ["execution", "revenue", "tools", "systems", "psychology", "milestones", "velocity", "automation"]

def scan_drafts() -> List[Dict]:
    """Scan drafts directory and extract metadata."""
    drafts = []

    if not DRAFTS_DIR.exists():
        return drafts

    for file in DRAFTS_DIR.glob("*.md"):
        with open(file) as f:
            content = f.read()

        # Extract metadata
        draft = {
            "file": file.name,
            "number": extract_draft_number(content),
            "title": extract_title(content),
            "topic": detect_topic(content),
            "timestamp": extract_timestamp(content, file),
            "word_count": len(content.split()),
            "has_insight": "insight" in content.lower() or "key insight" in content.lower() or "lesson" in content.lower(),
            "has_data": bool(re.search(r'\d+ blocks?|\$\d+', content)),
            "readability": score_readability(content)
        }

        drafts.append(draft)

    return drafts

def extract_draft_number(content: str) -> int:
    """Extract draft number from content."""
    match = re.search(r'Draft #(\d+)', content, re.IGNORECASE)
    return int(match.group(1)) if match else 0

def extract_title(content: str) -> str:
    """Extract title from first heading."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"

def detect_topic(content: str) -> str:
    """Detect topic from keywords."""
    content_lower = content.lower()

    topic_scores = {}
    for topic in TOPICS:
        keywords = get_topic_keywords(topic)
        score = sum(1 for kw in keywords if kw in content_lower)
        if score > 0:
            topic_scores[topic] = score

    if topic_scores:
        return max(topic_scores, key=topic_scores.get)
    return "general"

def get_topic_keywords(topic: str) -> List[str]:
    """Get keywords for each topic."""
    keywords = {
        "execution": ["execute", "execution", "work block", "shipping", "building", "ship"],
        "revenue": ["revenue", "money", " earning", "pipeline", "conversion", "grant", "service"],
        "tools": ["tool", "script", "python", "automation", "workflow"],
        "systems": ["system", "pattern", "framework", "methodology", "process"],
        "psychology": ["feel", "safe", "real", "procrastination", "motivation", "mindset"],
        "milestones": ["milestone", "1000", "2000", "3000", "block", "target"],
        "velocity": ["velocity", "speed", "fast", "slow", "blocks/hr", "per hour"],
        "automation": ["cron", "trigger", "automated", "auto", "schedule"]
    }
    return keywords.get(topic, [])

def extract_timestamp(content: str, file: Path) -> datetime:
    """Extract timestamp from content or file mtime."""
    # Try content first
    match = re.search(r'(\d{4}-\d{2}-\d{2})', content)
    if match:
        try:
            return datetime.fromisoformat(match.group(1))
        except:
            pass

    # Fall back to file mtime
    return datetime.fromtimestamp(file.stat().st_mtime)

def score_readability(content: str) -> float:
    """Score readability based on structure."""
    score = 3.0  # Base score

    # Bonus for structure
    if "##" in content:  # Has subheadings
        score += 0.5
    if "-" in content and "  -" in content:  # Has lists
        score += 0.5
    if "**" in content:  # Has bold/emphasis
        score += 0.3

    # Penalty for wall of text
    avg_line_length = len(content) / max(1, content.count('\n'))
    if avg_line_length > 100:
        score -= 0.5

    return min(5.0, max(1.0, score))

def calculate_score(draft: Dict) -> float:
    """Calculate combined score for a draft."""
    # Quality factors
    quality = draft['readability']
    if draft['has_insight']:
        quality += 1.0
    if draft['has_data']:
        quality += 0.5

    # Relevance factor
    relevance = 3.0  # Base relevance
    if draft['topic'] in ["execution", "revenue", "systems"]:  # High-priority topics
        relevance += 1.0

    # Impact factor
    impact = 3.0  # Base impact
    if draft['word_count'] > 200:  # Substantial content
        impact += 0.5
    if draft['word_count'] > 400:
        impact += 0.5

    # Recency bonus
    age_days = (datetime.utcnow() - draft['timestamp']).days
    if age_days < 1:
        relevance += 0.5
    elif age_days > 7:
        relevance -= 0.5

    # Combined score (1-5 scale)
    combined = (quality + relevance + impact) / 3
    return min(5.0, max(1.0, combined))

def rank_drafts(drafts: List[Dict]) -> List[Dict]:
    """Rank drafts by combined score."""
    for draft in drafts:
        draft['score'] = calculate_score(draft)

    return sorted(drafts, key=lambda d: d['score'], reverse=True)

def show_ranked(drafts: List[Dict], limit: int = None):
    """Show ranked drafts."""
    ranked = rank_drafts(drafts)
    if limit:
        ranked = ranked[:limit]

    print(f"\n📊 DRAFT RANKINGS (Score 1-5)")
    print("=" * 70)
    print(f"{'Score':<6} {'Topic':<12} {'Title'}")
    print("-" * 70)

    for draft in ranked:
        score_emoji = "⭐" * int(draft['score']) + "☆" * (5 - int(draft['score']))
        print(f"{draft['score']:.1f} {score_emoji} {draft['topic']:<12} {draft['title'][:40]}")

def show_summary(drafts: List[Dict]):
    """Show summary statistics."""
    if not drafts:
        print("\n❌ No drafts found")
        return

    print("\n📈 DRAFT SUMMARY")
    print("=" * 50)

    # Counts
    print(f"Total drafts:     {len(drafts)}")

    # Topic distribution
    topics = [d['topic'] for d in drafts]
    topic_counts = Counter(topics)
    print(f"\nTopic distribution:")
    for topic, count in topic_counts.most_common():
        print(f"  {topic:<12} {count}")

    # Quality distribution
    scored = [calculate_score(d) for d in drafts]
    avg_score = sum(scored) / len(scored)
    high_quality = len([s for s in scored if s >= 4.0])

    print(f"\nQuality distribution:")
    print(f"  Average score:  {avg_score:.2f}/5.0")
    print(f"  High quality:   {high_quality} drafts (score ≥ 4.0)")

    # Recommendations
    print(f"\n💡 Recommendations:")
    print(f"  • Publish top {min(10, len(drafts))} high-score drafts first")
    print(f"  • Consider consolidating drafts on same topic")
    print(f"  • Old drafts may need updates (recency penalty)")

def filter_by_topic(drafts: List[Dict], topic: str):
    """Filter and show drafts by topic."""
    filtered = [d for d in drafts if topic.lower() in d['topic'].lower()]

    if not filtered:
        print(f"\n❌ No drafts found for topic: {topic}")
        return

    print(f"\n📚 DRAFTS: {topic.upper()} ({len(filtered)} drafts)")
    print("=" * 70)

    ranked = rank_drafts(filtered)
    for draft in ranked:
        score_emoji = "⭐" * int(draft['score']) + "☆" * (5 - int(draft['score']))
        print(f"{draft['score']:.1f} {score_emoji} {draft['title'][:50]}")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 tools/content-prioritizer.py --rank [--top N]")
        print("  python3 tools/content-prioritizer.py --topic NAME")
        print("  python3 tools/content-prioritizer.py --summary")
        sys.exit(1)

    args = sys.argv[1:]
    drafts = scan_drafts()

    if not drafts:
        print("❌ No drafts found in moltbook-drafts/")
        sys.exit(1)

    if "--rank" in args:
        limit = int(args[args.index("--top") + 1]) if "--top" in args else None
        show_ranked(drafts, limit)

    elif "--topic" in args:
        topic_idx = args.index("--topic") + 1
        if topic_idx >= len(args):
            print("❌ Missing topic name")
            sys.exit(1)
        filter_by_topic(drafts, args[topic_idx])

    elif "--summary" in args:
        show_summary(drafts)

    else:
        print("❌ Unknown command")
        sys.exit(1)

if __name__ == "__main__":
    main()

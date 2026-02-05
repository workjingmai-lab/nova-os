#!/usr/bin/env python3
"""
Moltbook Deduplicator — Find duplicate or similar posts in queue.

Prevents publishing duplicate content. Analyzes:
- Exact title matches
- Similar content (Jaccard similarity)
- Same topic with different wording

Usage:
    python3 tools/moltbook-deduplicator.py
    python3 tools/moltbook-deduplicator.py --threshold 0.7  # Similarity threshold (0-1)
"""

import os
import sys
import re
import argparse
from pathlib import Path
from collections import defaultdict

def extract_words(text: str) -> set:
    """Extract unique words from text, ignoring common stopwords."""
    stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
                 'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
                 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'this', 'that', 'these',
                 'those', 'my', 'your', 'his', 'her', 'its', 'our', 'their'}
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    return set(words) - stopwords

def jaccard_similarity(set1: set, set2: set) -> float:
    """Calculate Jaccard similarity between two sets (0-1)."""
    if not set1 or not set2:
        return 0.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0.0

def extract_title(content: str) -> str:
    """Extract title from markdown (first # heading or first line)."""
    lines = content.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            return line.lstrip('#').strip()
    return lines[0][:50] if lines else "Untitled"

def analyze_posts(queue_dir: str, threshold: float = 0.6):
    """Analyze queued posts for duplicates."""
    queue_path = Path(queue_dir)
    if not queue_path.exists():
        print(f"❌ Queue directory not found: {queue_dir}")
        return

    md_files = list(queue_path.glob("*.md"))
    if not md_files:
        print("✅ No queued posts found. Queue is clean.")
        return

    print(f"📊 Analyzing {len(md_files)} queued posts for duplicates...\n")

    posts = []
    for f in md_files:
        content = f.read_text()
        title = extract_title(content)
        words = extract_words(content)
        posts.append({'file': f.name, 'title': title, 'words': words, 'path': f})

    # Check exact title matches
    title_groups = defaultdict(list)
    for post in posts:
        title_groups[post['title'].lower()].append(post)

    exact_duplicates = [g for g in title_groups.values() if len(g) > 1]

    # Check similar content
    similar_pairs = []
    for i, p1 in enumerate(posts):
        for p2 in posts[i+1:]:
            sim = jaccard_similarity(p1['words'], p2['words'])
            if sim >= threshold:
                similar_pairs.append((p1, p2, sim))

    # Report results
    if exact_duplicates:
        print("⚠️  EXACT TITLE DUPLICATES:")
        for group in exact_duplicates:
            print(f"\n   Title: \"{group[0]['title']}\"")
            for post in group:
                print(f"      - {post['file']}")
        print(f"\n   Action: Keep one, archive others.\n")

    if similar_pairs:
        print(f"⚠️  SIMILAR CONTENT (threshold ≥ {threshold}):")
        for p1, p2, sim in similar_pairs:
            print(f"\n   Similarity: {sim:.1%}")
            print(f"   1. {p1['file']}")
            print(f"      Title: \"{p1['title']}\"")
            print(f"   2. {p2['file']}")
            print(f"      Title: \"{p2['title']}\"")
        print(f"\n   Action: Merge or consolidate.\n")

    if not exact_duplicates and not similar_pairs:
        print("✅ No duplicates found. Queue is clean!")
        print(f"\n   📝 {len(md_files)} unique posts ready to publish.")
    else:
        total_issues = len(exact_duplicates) + len(similar_pairs)
        print(f"🔍 Found {total_issues} potential duplicate(s) to review.")

def main():
    parser = argparse.ArgumentParser(description="Find duplicate Moltbook posts")
    parser.add_argument('--queue', default='moltbook/queued', help='Queue directory path')
    parser.add_argument('--threshold', type=float, default=0.6,
                       help='Similarity threshold (0-1, default: 0.6)')
    args = parser.parse_args()

    workspace = Path('/home/node/.openclaw/workspace')
    queue_dir = workspace / args.queue

    analyze_posts(str(queue_dir), args.threshold)

if __name__ == '__main__':
    main()

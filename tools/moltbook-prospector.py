#!/usr/bin/env python3
"""
Moltbook Prospector - Find Qualified Service Clients
Quickly identify agents that might need automation services
"""

import json
import sys
import requests
from typing import List, Dict

API_KEY = "moltbook_sk_xSwszjAM8vLLaa7VsSZVgNWp5a-R5XqD"
API_BASE = "https://www.moltbook.com/api/v1"

def get_feed(limit=50) -> List[Dict]:
    """Fetch recent posts from Moltbook feed"""
    try:
        response = requests.get(
            f"{API_BASE}/feed",
            headers={"Authorization": f"Bearer {API_KEY}"},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data.get("posts", [])[:limit]
    except Exception as e:
        print(f"Error fetching feed: {e}", file=sys.stderr)
        return []

def analyze_post(post: Dict) -> Dict:
    """Analyze a post for prospecting signals"""
    signals = {
        "author": post.get("author", "unknown"),
        "karma": post.get("author_karma", 0),
        "content": post.get("content_text", post.get("content", ""))[:200],
        "fit_score": 0,
        "reasons": []
    }

    content_lower = signals["content"].lower()

    # Positive signals (might need services)
    positive_keywords = [
        "building", "debugging", "help", "automation", "workflow",
        "integration", "api", "monitoring", "scaling", "optimizing"
    ]
    for keyword in positive_keywords:
        if keyword in content_lower:
            signals["fit_score"] += 1
            signals["reasons"].append(f"Mentioned: {keyword}")

    # Negative signals (already competent or wrong fit)
    negative_signals = ["hire me", "for hire", "service", "automation agency"]
    for signal in negative_signals:
        if signal in content_lower:
            signals["fit_score"] -= 2
            signals["reasons"].append(f"Competitor signal: {signal}")

    # Karma threshold (agents with 10-500 karma are sweet spot)
    if 10 <= signals["karma"] <= 500:
        signals["fit_score"] += 2
        signals["reasons"].append("Karma in sweet spot (10-500)")
    elif signals["karma"] > 1000:
        signals["fit_score"] -= 1
        signals["reasons"].append("Very high karma (may not need help)")

    return signals

def main():
    print("🔍 Moltbook Prospector - Finding Qualified Clients\n")

    posts = get_feed(limit=50)
    if not posts:
        print("❌ No posts fetched (API may be down)")
        return

    # Track unique authors
    seen_authors = {}
    qualified = []

    for post in posts:
        author = post.get("author", "unknown")
        if author == "nova_test":
            continue

        if author not in seen_authors:
            analysis = analyze_post(post)
            seen_authors[author] = analysis

            if analysis["fit_score"] >= 2:
                qualified.append(analysis)

    # Sort by fit score
    qualified.sort(key=lambda x: x["fit_score"], reverse=True)

    print(f"📊 Found {len(qualified)} qualified prospects:\n")

    for i, prospect in enumerate(qualified[:10], 1):
        print(f"{i}. {prospect['author']} ({prospect['karma']} karma)")
        print(f"   Fit Score: {prospect['fit_score']}/10")
        print(f"   Content: {prospect['content'][:100]}...")
        print(f"   Reasons: {', '.join(prospect['reasons'])}")
        print()

if __name__ == "__main__":
    main()

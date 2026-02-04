#!/usr/bin/env python3
"""
knowledge-search.py — Search knowledge base

Search all knowledge/ articles by keyword or topic.
Fast discovery of relevant insights.

Usage:
    python3 knowledge-search.py pipeline
    python3 knowledge-search.py execution --count 5
    python3 knowledge-search.py blocker --sort-by date
"""

import re
from pathlib import Path
from datetime import datetime

WORKSPACE = Path("/home/node/.openclaw/workspace")
KNOWLEDGE_DIR = WORKSPACE / "knowledge"

def extract_metadata(content: str) -> dict:
    """Extract title, date, tags from markdown file"""
    metadata = {
        "title": "",
        "date": None,
        "tags": [],
        "size": len(content)
    }
    
    # Extract title (first # heading)
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if title_match:
        metadata["title"] = title_match.group(1).strip()
    
    # Extract date from file stats (created/modified)
    # Note: This would require file system stats
    
    return metadata

def search_articles(keyword: str, count: int = 10, sort_by: str = "relevance") -> list:
    """Search knowledge articles by keyword"""
    results = []
    keyword_lower = keyword.lower()
    
    for md_file in KNOWLEDGE_DIR.glob("*.md"):
        content = md_file.read_text()
        metadata = extract_metadata(content)
        
        # Count keyword occurrences
        occurrences = content.lower().count(keyword_lower)
        if occurrences == 0:
            continue
        
        # Calculate relevance score
        # Title match = 10 points, content matches = 1 point each
        score = 0
        if keyword_lower in metadata["title"].lower():
            score += 10
        score += occurrences
        
        results.append({
            "file": md_file.name,
            "title": metadata["title"] or md_file.stem,
            "score": score,
            "occurrences": occurrences,
            "size": metadata["size"]
        })
    
    # Sort results
    if sort_by == "relevance":
        results.sort(key=lambda x: x["score"], reverse=True)
    elif sort_by == "date":
        results.sort(key=lambda x: x["file"], reverse=True)
    elif sort_by == "size":
        results.sort(key=lambda x: x["size"], reverse=True)
    
    return results[:count]

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Search knowledge base")
    parser.add_argument("keyword", help="Keyword to search for")
    parser.add_argument("--count", type=int, default=10, help="Number of results")
    parser.add_argument("--sort-by", choices=["relevance", "date", "size"], 
                       default="relevance", help="Sort method")
    parser.add_argument("--list", action="store_true", help="List all articles")
    args = parser.parse_args()
    
    if args.list:
        # List all articles
        articles = sorted(KNOWLEDGE_DIR.glob("*.md"))
        print(f"📚 Knowledge Base — {len(articles)} articles")
        print("=" * 50)
        for i, article in enumerate(articles, 1):
            content = article.read_text()
            title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            title = title_match.group(1) if title_match else article.stem
            print(f"{i:3d}. {title}")
        return
    
    if not args.keyword:
        parser.print_help()
        return
    
    # Search
    results = search_articles(args.keyword, args.count, args.sort_by)
    
    if not results:
        print(f"❌ No articles found matching '{args.keyword}'")
        return
    
    # Display results
    print(f"🔍 Search Results: '{args.keyword}' ({len(results)} found)")
    print("=" * 60)
    
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['title']}")
        print(f"   File: {result['file']}")
        print(f"   Relevance: {result['score']} ({result['occurrences']} occurrences)")
        print(f"   Size: {result['size']:,} bytes")
        print(f"   Path: knowledge/{result['file']}")
    
    print(f"\n💡 Tip: Use --count N for more results, --sort-by date/size for different sorting")

if __name__ == "__main__":
    main()

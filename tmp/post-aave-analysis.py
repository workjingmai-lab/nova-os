#!/usr/bin/env python3
"""
Quick script to post Aave governance analysis to Moltbook.
"""
import os
import sys

# Add tools directory to path
sys.path.insert(0, '/home/node/.openclaw/workspace/tools')

try:
    from moltbook_suite import post_to_moltbook
    
    # Read the Aave analysis file
    with open('/home/node/.openclaw/workspace/content/aave-governance-analysis.md', 'r') as f:
        content = f.read()
    
    # Extract title (first line)
    lines = content.split('\n')
    title = lines[0].replace('#', '').strip()
    
    # Post to Moltbook
    print(f"Posting to Moltbook: {title}")
    result = post_to_moltbook(title, content, tags=["aave", "governance", "defi", "automation", "dao"])
    
    if result.get('success'):
        print(f"✅ Posted successfully! Post ID: {result.get('post_id')}")
    else:
        print(f"❌ Post failed: {result.get('error')}")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

#!/usr/bin/env python3
"""
Multi-Platform Distributor
Routes content around rate limits by distributing across platforms.

Supports:
- Moltbook (primary, rate limited: ~5 min between posts)
- More platforms can be added

Strategy:
1. Track last post time per platform
2. Route to platform with smallest recent posts
3. Respect rate limits per platform
4. Maximize total throughput

Usage: python3 tools/multi-platform-distributor.py --content "Title: ... \\n\\n Body..."
"""

import json
import sys
import argparse
from datetime import datetime, timedelta
from pathlib import Path

STATE_FILE = "/home/node/.openclaw/workspace/.distribution-state.json"

# Platform configurations
PLATFORMS = {
    "moltbook": {
        "rate_limit_min": 5,  # minutes between posts
        "enabled": True,
        "tool": "moltbook-suite.py"
    },
    # Add more platforms here:
    # "twitter": {
    #     "rate_limit_min": 1,
    #     "enabled": False,
    #     "tool": "twitter-poster.py"
    # }
}

def load_state():
    """Load distribution state (last post times per platform)."""
    try:
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    except:
        return {
            "last_posts": {},
            "total_posts": 0
        }

def save_state(state):
    """Save distribution state."""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def get_available_platform(state):
    """
    Find platform that's not rate-limited.
    Returns platform name or None if all limited.
    """
    now = datetime.now()
    
    for platform, config in PLATFORMS.items():
        if not config.get("enabled", False):
            continue
        
        last_post_str = state["last_posts"].get(platform)
        if not last_post_str:
            return platform  # Never posted, available
        
        last_post = datetime.fromisoformat(last_post_str)
        min_since = (now - last_post).total_seconds() / 60
        
        if min_since >= config["rate_limit_min"]:
            return platform  # Rate limit passed, available
    
    return None  # All platforms rate-limited

def distribute_to_platform(platform, content, dry_run=False):
    """Distribute content to specific platform."""
    config = PLATFORMS[platform]
    tool = config["tool"]
    
    if platform == "moltbook":
        # Save content to temp file for moltbook-suite
        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(content)
            temp_path = f.name
        
        cmd = f"python3 tools/{tool} post --file {temp_path}"
        
        if dry_run:
            print(f"[DRY RUN] Would post to {platform}")
            print(f"  Command: {cmd}")
            print(f"  Content preview: {content[:100]}...")
            return True
        
        import subprocess
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        # Cleanup temp file
        Path(temp_path).unlink(missing_ok=True)
        
        if result.returncode == 0:
            print(f"✅ Posted to {platform}")
            return True
        else:
            print(f"❌ Failed to post to {platform}: {result.stderr}")
            return False
    
    # Add other platforms here
    print(f"⚠️  Platform {platform} not implemented yet")
    return False

def distribute(content, dry_run=False, wait_for_slot=False, max_wait_min=60):
    """
    Distribute content to available platform.
    
    Args:
        content: Content to post
        dry_run: Show what would happen without posting
        wait_for_slot: Wait for rate limit to expire if all limited
        max_wait_min: Maximum minutes to wait for slot
    """
    state = load_state()
    
    # Try to find available platform
    platform = get_available_platform(state)
    
    if platform:
        print(f"📤 Distributing to {platform}...")
        success = distribute_to_platform(platform, content, dry_run)
        
        if success and not dry_run:
            # Update state
            state["last_posts"][platform] = datetime.now().isoformat()
            state["total_posts"] += 1
            save_state(state)
        
        return success
    
    # All platforms rate-limited
    print("⏸️  All platforms rate-limited.")
    
    if wait_for_slot:
        # Calculate when next slot opens
        now = datetime.now()
        earliest_slot = None
        
        for platform, config in PLATFORMS.items():
            if not config.get("enabled", False):
                continue
            
            last_post_str = state["last_posts"].get(platform)
            if last_post_str:
                last_post = datetime.fromisoformat(last_post_str)
                slot_time = last_post + timedelta(minutes=config["rate_limit_min"])
                
                if earliest_slot is None or slot_time < earliest_slot:
                    earliest_slot = slot_time
        
        if earliest_slot:
            wait_min = (earliest_slot - now).total_seconds() / 60
            print(f"⏰ Next slot opens in {wait_min:.1f} minutes ({earliest_slot.strftime('%H:%M:%S')})")
            
            if wait_min <= max_wait_min:
                print(f"⏳ Waiting {wait_min:.1f} minutes...")
                # In production, this would sleep and retry
                # For now, just inform the user
                print(f"   Run again in {wait_min:.1f} minutes to post")
                return False
            else:
                print(f"⏭️  Wait time ({wait_min:.1f} min) exceeds max ({max_wait_min} min)")
                return False
    
    return False

def show_status():
    """Show distribution status across all platforms."""
    state = load_state()
    now = datetime.now()
    
    print("\n" + "="*60)
    print("📊 MULTI-PLATFORM DISTRIBUTION STATUS")
    print("="*60)
    print(f"\nTotal posts distributed: {state['total_posts']}\n")
    
    for platform, config in PLATFORMS.items():
        print(f"{platform.upper()}:")
        print(f"  Enabled: {config.get('enabled', False)}")
        print(f"  Rate limit: {config['rate_limit_min']} min between posts")
        
        last_post_str = state["last_posts"].get(platform)
        if last_post_str:
            last_post = datetime.fromisoformat(last_post_str)
            min_since = (now - last_post).total_seconds() / 60
            
            status = "✅ Available" if min_since >= config["rate_limit_min"] else "⏸️  Rate-limited"
            print(f"  Last post: {last_post.strftime('%H:%M:%S')} ({min_since:.1f} min ago)")
            print(f"  Status: {status}")
        else:
            print(f"  Last post: Never")
            print(f"  Status: ✅ Available (no history)")
        print()
    
    print("="*60 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Multi-platform content distributor")
    parser.add_argument("--content", help="Content to distribute")
    parser.add_argument("--file", help="File containing content to distribute")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without posting")
    parser.add_argument("--wait", action="store_true", help="Wait for rate limit to expire")
    parser.add_argument("--max-wait", type=int, default=60, help="Max minutes to wait (default: 60)")
    parser.add_argument("--status", action="store_true", help="Show distribution status")
    
    args = parser.parse_args()
    
    if args.status:
        show_status()
        return
    
    # Load content
    if args.file:
        with open(args.file, 'r') as f:
            content = f.read()
    elif args.content:
        content = args.content
    else:
        print("❌ Error: --content or --file required")
        parser.print_help()
        sys.exit(1)
    
    # Distribute
    success = distribute(
        content,
        dry_run=args.dry_run,
        wait_for_slot=args.wait,
        max_wait_min=args.max_wait
    )
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()

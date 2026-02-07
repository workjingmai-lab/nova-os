#!/usr/bin/env python3
"""
Session Velocity Tracker — Track work block velocity over time.

Shows how many work blocks you complete per session and identifies patterns.
Helps optimize for sustained high-velocity execution.

Usage:
    python3 session-velocity.py              # Show last 10 sessions
    python3 session-velocity.py --today      # Today's sessions only
    python3 session-velocity.py --avg        # Average velocity
    python3 session-velocity.py --trend      # Velocity trend (improving/declining)

Created: 2026-02-07 (Work block 3273)
"""

import re
import argparse
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Configuration
DIARY_FILE = "/home/node/.openclaw/workspace/diary.md"
HEARTBEAT_FILE = "/home/node/.openclaw/workspace/.heartbeat_state.json"

def parse_diary_sessions(limit=None):
    """Parse diary.md to extract session work block counts."""
    sessions = []
    
    try:
        with open(DIARY_FILE, 'r') as f:
            content = f.read()
        
        # Find all work block entries
        # Pattern: ## [WORK BLOCK N — timestamp]
        pattern = r'## \[WORK BLOCK (\d+) — ([^\]]+)\]'
        matches = re.findall(pattern, content)
        
        if not matches:
            print("❌ No work blocks found in diary.md")
            return None
        
        # Group by session
        # A new session starts when there's a gap or when we see "Session complete"
        current_session_blocks = []
        prev_block_num = None
        
        for block_num, timestamp in matches:
            block_num = int(block_num)
            
            # Detect session boundary (gap in block numbers or "Session complete" marker)
            if prev_block_num is not None:
                # If gap > 50 blocks, likely new session
                if block_num - prev_block_num > 50:
                    if current_session_blocks:
                        sessions.append(current_session_blocks)
                    current_session_blocks = []
            
            current_session_blocks.append((block_num, timestamp))
            prev_block_num = block_num
        
        # Don't forget the last session
        if current_session_blocks:
            sessions.append(current_session_blocks)
        
        # Reverse to get most recent first
        sessions = sessions[::-1]
        
        # Apply limit
        if limit:
            sessions = sessions[:limit]
        
        return sessions
    
    except FileNotFoundError:
        print(f"❌ Diary file not found: {DIARY_FILE}")
        return None
    except Exception as e:
        print(f"❌ Error parsing diary: {e}")
        return None

def calculate_session_stats(session_blocks):
    """Calculate statistics for a single session."""
    if not session_blocks:
        return None
    
    block_nums = [b[0] for b in session_blocks]
    
    # Extract timestamps
    timestamps = []
    for _, ts in session_blocks:
        try:
            # Parse various timestamp formats
            # Try ISO format first
            if 'T' in ts:
                dt = datetime.fromisoformat(ts.replace('Z', '+00:00'))
            else:
                # Try other formats
                dt = datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
            timestamps.append(dt)
        except:
            continue
    
    # Calculate duration
    duration_min = None
    if len(timestamps) >= 2:
        duration = (timestamps[-1] - timestamps[0]).total_seconds() / 60
        duration_min = round(duration, 1)
    
    return {
        'block_count': len(session_blocks),
        'first_block': min(block_nums),
        'last_block': max(block_nums),
        'duration_min': duration_min,
        'start_time': timestamps[0] if timestamps else None
    }

def print_session_summary(sessions):
    """Print summary of sessions."""
    total_blocks = sum(len(s) for s in sessions)
    total_sessions = len(sessions)
    avg_blocks = round(total_blocks / total_sessions, 1) if total_sessions > 0 else 0
    
    print(f"\n{'='*60}")
    print(f"  📊 SESSION VELOCITY SUMMARY")
    print(f"{'='*60}")
    print(f"  Recent sessions: {total_sessions}")
    print(f"  Total work blocks: {total_blocks}")
    print(f"  Average blocks/session: {avg_blocks}")
    print(f"{'='*60}")

def print_session_details(sessions, show_all=False):
    """Print details for each session."""
    print(f"\n📋 SESSION DETAILS")
    
    for i, session in enumerate(sessions, 1):
        stats = calculate_session_stats(session)
        if not stats:
            continue
        
        block_count = stats['block_count']
        duration = stats['duration_min']
        start = stats['start_time']
        
        # Calculate velocity (blocks/hour)
        velocity = None
        if duration and duration > 0:
            velocity = round((block_count / duration) * 60, 1)
        
        # Format start time
        time_str = start.strftime('%Y-%m-%d %H:%M') if start else 'Unknown'
        
        print(f"\n  Session {i}: {time_str}")
        print(f"    Work blocks: {block_count}")
        if duration:
            print(f"    Duration: {duration} min")
        if velocity:
            print(f"    Velocity: {velocity} blocks/hour")
        print(f"    Range: #{stats['first_block']} - #{stats['last_block']}")

def calculate_velocity_trend(sessions):
    """Calculate velocity trend (improving/declining/stable)."""
    if len(sessions) < 3:
        print("⚠️ Need at least 3 sessions to determine trend")
        return
    
    velocities = []
    for session in sessions:
        stats = calculate_session_stats(session)
        if stats and stats['duration_min'] and stats['duration_min'] > 0:
            velocity = (stats['block_count'] / stats['duration_min']) * 60
            velocities.append(velocity)
    
    if len(velocities) < 3:
        print("⚠️ Not enough sessions with duration data")
        return
    
    # Calculate trend
    recent_avg = sum(velocities[:3]) / 3  # Most recent 3
    older_avg = sum(velocities[3:]) / len(velocities[3:]) if len(velocities) > 3 else recent_avg
    
    diff = recent_avg - older_avg
    diff_pct = (diff / older_avg) * 100 if older_avg > 0 else 0
    
    print(f"\n📈 VELOCITY TREND")
    print(f"  Recent 3 sessions: {round(recent_avg, 1)} blocks/hour")
    print(f"  Older sessions: {round(older_avg, 1)} blocks/hour")
    print(f"  Difference: {round(diff, 1)} blocks/hour ({round(diff_pct, 1)}%)")
    
    if abs(diff_pct) < 5:
        print(f"  → ✅ Stable velocity")
    elif diff_pct > 5:
        print(f"  → 🚀 Improving!")
    else:
        print(f"  → ⚠️ Declining")

def main():
    parser = argparse.ArgumentParser(description='Track session velocity')
    parser.add_argument('--today', action='store_true',
                        help='Show today\'s sessions only')
    parser.add_argument('--avg', action='store_true',
                        help='Show average velocity')
    parser.add_argument('--trend', action='store_true',
                        help='Show velocity trend')
    parser.add_argument('--sessions', type=int, default=10,
                        help='Number of recent sessions to show')
    args = parser.parse_args()

    # Parse sessions
    sessions = parse_diary_sessions(limit=args.sessions)
    if not sessions:
        return
    
    # Filter for today if requested
    if args.today:
        today = datetime.now().date()
        today_sessions = []
        for session in sessions:
            stats = calculate_session_stats(session)
            if stats and stats['start_time'] and stats['start_time'].date() == today:
                today_sessions.append(session)
        sessions = today_sessions
        
        if not sessions:
            print("❌ No sessions found today")
            return
    
    # Show trend if requested
    if args.trend:
        sessions_for_trend = parse_diary_sessions(limit=20)  # More sessions for trend
        if sessions_for_trend:
            calculate_velocity_trend(sessions_for_trend)
    
    # Show average if requested
    if args.avg:
        all_sessions = parse_diary_sessions(limit=50)
        if all_sessions:
            total_blocks = sum(len(s) for s in all_sessions)
            total_sessions = len(all_sessions)
            avg = round(total_blocks / total_sessions, 1) if total_sessions > 0 else 0
            print(f"\n📊 All-time average: {avg} blocks/session")
    
    # Print summary
    print_session_summary(sessions)
    
    # Print details
    print_session_details(sessions)
    
    # Recommendations
    print(f"\n💡 OPTIMIZATION TIPS:")
    print(f"  • Target: 10-20 blocks per session")
    print(f"  • Velocity > 40 blocks/hour = high performance")
    print(f"  • Take breaks every 10-15 blocks to maintain quality")
    print(f"  • Use task-randomizer.py to reduce decision fatigue")

if __name__ == '__main__':
    main()

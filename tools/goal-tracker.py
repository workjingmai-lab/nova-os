#!/usr/bin/env python3
"""
Goal Tracker CLI - Track and manage goals from goals/active.md

Usage:
    python3 tools/goal-tracker.py list              # Show all goals with status
    python3 tools/goal-tracker.py progress <name>   # Show progress notes
    python3 tools/goal-tracker.py complete <name>   # Mark goal as done
    python3 tools/goal-tracker.py stats             # Show completion statistics
    python3 tools/goal-tracker.py suggest           # Suggest next goal to work on
"""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Color codes for terminal output
class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

# Goal structure
class Goal:
    def __init__(self, name: str, priority: str, section: str, done: bool = False):
        self.name = name
        self.priority = priority  # high, medium, long-term, daily
        self.section = section
        self.done = done
        self.progress_notes: List[str] = []

    def __repr__(self):
        status = "✓" if self.done else "○"
        return f"[{status}] {self.name} ({self.priority})"

def colorize(text: str, color: str) -> str:
    """Apply color to text if terminal supports it."""
    if sys.stdout.isatty():
        return f"{color}{text}{Colors.RESET}"
    return text

def parse_goals_file(filepath: str) -> List[Goal]:
    """Parse goals/active.md and extract goals with their priorities."""
    goals = []
    
    if not os.path.exists(filepath):
        return goals
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Split by sections (## headers)
    sections = re.split(r'\n##\s+', content)
    
    priority_map = {
        'high priority': 'high',
        'medium priority': 'medium',
        'long-term': 'long-term',
        'daily habits': 'daily'
    }
    
    for section in sections:
        if not section.strip():
            continue
        
        lines = section.strip().split('\n')
        section_title = lines[0].strip().lower()
        
        # Determine priority from section title
        priority = 'medium'  # default
        for key, val in priority_map.items():
            if key in section_title:
                priority = val
                break
        
        # Parse goals in this section
        for line in lines[1:]:
            line = line.strip()
            if not line.startswith('- ['):
                continue
            
            # Check if done: [x] or [ ]
            done = line.startswith('- [x]') or line.startswith('- [X]')
            
            # Extract goal name
            match = re.match(r'-\s*\[[xX ]\]\s*(.+)$', line)
            if match:
                name = match.group(1).strip()
                goal = Goal(name, priority, section_title, done)
                goals.append(goal)
    
    return goals

def scan_for_completions(goals: List[Goal], workspace_dir: str) -> None:
    """Auto-detect completed goals by scanning memory files for ✓ or DONE."""
    memory_dir = os.path.join(workspace_dir, 'memory')
    goals_dir = os.path.join(workspace_dir, 'goals')
    
    files_to_scan = []
    
    # Scan memory files
    if os.path.exists(memory_dir):
        for f in os.listdir(memory_dir):
            if f.endswith('.md'):
                files_to_scan.append(os.path.join(memory_dir, f))
    
    # Scan diary.md if exists
    diary_path = os.path.join(goals_dir, 'diary.md')
    if os.path.exists(diary_path):
        files_to_scan.append(diary_path)
    
    # Scan today files
    if os.path.exists(goals_dir):
        for f in os.listdir(goals_dir):
            if f.startswith('today-') and f.endswith('.md'):
                files_to_scan.append(os.path.join(goals_dir, f))
    
    # Scan each file for completion markers related to goals
    for filepath in files_to_scan:
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().lower()
                
            for goal in goals:
                if goal.done:
                    continue
                    
                goal_lower = goal.name.lower()
                # Look for completion indicators
                patterns = [
                    rf'✓\s*.*{re.escape(goal_lower[:30])}',
                    rf'done.*{re.escape(goal_lower[:30])}',
                    rf'completed.*{re.escape(goal_lower[:30])}',
                    rf'finished.*{re.escape(goal_lower[:30])}',
                    rf'goal.*advanced.*{re.escape(goal_lower[:20])}',
                ]
                
                for pattern in patterns:
                    if re.search(pattern, content):
                        goal.done = True
                        break
        except Exception:
            continue

def find_progress_notes(goal_name: str, workspace_dir: str) -> List[Tuple[str, str]]:
    """Find progress notes for a goal from memory/diary files."""
    notes = []
    memory_dir = os.path.join(workspace_dir, 'memory')
    goals_dir = os.path.join(workspace_dir, 'goals')
    
    files_to_scan = []
    
    # Scan memory files
    if os.path.exists(memory_dir):
        for f in sorted(os.listdir(memory_dir), reverse=True):
            if f.endswith('.md'):
                files_to_scan.append((f, os.path.join(memory_dir, f)))
    
    # Scan diary.md
    diary_path = os.path.join(goals_dir, 'diary.md')
    if os.path.exists(diary_path):
        files_to_scan.append(('diary.md', diary_path))
    
    # Search for mentions of the goal
    goal_keywords = [kw.strip().lower() for kw in goal_name.split() if len(kw) > 3]
    if not goal_keywords:
        goal_keywords = [goal_name.lower()]
    
    for filename, filepath in files_to_scan:
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
                
            for i, line in enumerate(lines):
                line_lower = line.lower()
                # Check if any keyword matches
                if any(kw in line_lower for kw in goal_keywords):
                    # Get context (line before and after)
                    context_start = max(0, i - 1)
                    context_end = min(len(lines), i + 2)
                    context = '\n'.join(lines[context_start:context_end]).strip()
                    
                    if len(context) > 10:  # Avoid empty matches
                        notes.append((filename, context))
                        break  # One note per file is enough
        except Exception:
            continue
    
    return notes[:10]  # Limit to 10 most recent

def mark_goal_complete(goal_name: str, goals: List[Goal], filepath: str) -> bool:
    """Mark a goal as complete in the active.md file."""
    if not os.path.exists(filepath):
        return False
    
    # Find matching goal
    target_goal = None
    for goal in goals:
        if goal_name.lower() in goal.name.lower() or goal.name.lower() in goal_name.lower():
            target_goal = goal
            break
    
    if not target_goal:
        # Try partial match
        for goal in goals:
            # Check if any significant word matches
            goal_words = set(goal.name.lower().split())
            search_words = set(goal_name.lower().split())
            if goal_words & search_words:
                target_goal = goal
                break
    
    if not target_goal:
        return False
    
    # Read and update file
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Find and replace the goal line
    old_line = f"- [ ] {target_goal.name}"
    new_line = f"- [x] {target_goal.name}  # Completed {datetime.now().strftime('%Y-%m-%d')}"
    
    if old_line in content:
        content = content.replace(old_line, new_line)
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    
    return False

def calculate_stats(goals: List[Goal]) -> Dict:
    """Calculate completion statistics."""
    total = len(goals)
    done = sum(1 for g in goals if g.done)
    active = total - done
    
    by_priority = {}
    for goal in goals:
        p = goal.priority
        if p not in by_priority:
            by_priority[p] = {'total': 0, 'done': 0}
        by_priority[p]['total'] += 1
        if goal.done:
            by_priority[p]['done'] += 1
    
    completion_rate = (done / total * 100) if total > 0 else 0
    
    return {
        'total': total,
        'done': done,
        'active': active,
        'completion_rate': completion_rate,
        'by_priority': by_priority
    }

def suggest_next_goal(goals: List[Goal]) -> Optional[Goal]:
    """Suggest the next goal to work on based on priority and status."""
    priority_order = ['high', 'medium', 'long-term', 'daily']
    
    active_goals = [g for g in goals if not g.done]
    
    if not active_goals:
        return None
    
    # Sort by priority order
    for priority in priority_order:
        candidates = [g for g in active_goals if g.priority == priority]
        if candidates:
            # Return first one or random for variety
            return candidates[0]
    
    return active_goals[0] if active_goals else None

def print_header(text: str):
    """Print a formatted header."""
    print()
    print(colorize("═" * 60, Colors.CYAN))
    print(colorize(f"  {text}", Colors.BOLD + Colors.CYAN))
    print(colorize("═" * 60, Colors.CYAN))
    print()

def print_subheader(text: str):
    """Print a formatted subheader."""
    print()
    print(colorize(f"▸ {text}", Colors.BOLD + Colors.BLUE))

def cmd_list(goals: List[Goal]):
    """List all goals with color-coded status."""
    print_header("🎯 ACTIVE GOALS")
    
    if not goals:
        print(colorize("  No goals found in goals/active.md", Colors.DIM))
        return
    
    # Group by priority
    priority_order = [
        ('high', '🔥 High Priority', Colors.RED),
        ('medium', '⚡ Medium Priority', Colors.YELLOW),
        ('long-term', '📅 Long-term', Colors.BLUE),
        ('daily', '🔄 Daily Habits', Colors.CYAN)
    ]
    
    for priority_key, label, color in priority_order:
        section_goals = [g for g in goals if g.priority == priority_key]
        if section_goals:
            print_subheader(label)
            
            for goal in section_goals:
                if goal.done:
                    status = colorize("✓", Colors.GREEN)
                    name = colorize(goal.name, Colors.DIM)
                else:
                    status = colorize("○", color)
                    name = goal.name
                
                print(f"  {status} {name}")
    
    # Summary
    active_count = sum(1 for g in goals if not g.done)
    done_count = sum(1 for g in goals if g.done)
    
    print()
    print(colorize(f"  Summary: {done_count} done, {active_count} active", Colors.DIM))

def cmd_progress(goals: List[Goal], goal_name: str, workspace_dir: str):
    """Show progress notes for a specific goal."""
    print_header(f"📊 PROGRESS: {goal_name}")
    
    # Find matching goal
    target_goal = None
    for goal in goals:
        if goal_name.lower() in goal.name.lower():
            target_goal = goal
            break
    
    if not target_goal:
        # Try partial match
        for goal in goals:
            goal_words = set(goal.name.lower().split())
            search_words = set(goal_name.lower().split())
            if goal_words & search_words:
                target_goal = goal
                break
    
    if not target_goal:
        print(colorize(f"  Goal not found: {goal_name}", Colors.RED))
        print(colorize("  Use 'list' to see available goals", Colors.DIM))
        return
    
    # Show goal info
    priority_colors = {
        'high': Colors.RED,
        'medium': Colors.YELLOW,
        'long-term': Colors.BLUE,
        'daily': Colors.CYAN
    }
    p_color = priority_colors.get(target_goal.priority, Colors.RESET)
    
    status = colorize("✓ DONE", Colors.GREEN) if target_goal.done else colorize("○ ACTIVE", p_color)
    print(f"  Goal: {colorize(target_goal.name, Colors.BOLD)}")
    print(f"  Status: {status}")
    print(f"  Priority: {colorize(target_goal.priority.upper(), p_color)}")
    
    # Find progress notes
    print_subheader("Recent Activity")
    notes = find_progress_notes(target_goal.name, workspace_dir)
    
    if not notes:
        print(colorize("  No progress notes found yet.", Colors.DIM))
        print(colorize("  Progress is tracked from memory files and diary.md", Colors.DIM))
    else:
        for filename, context in notes:
            print(f"\n  {colorize('📄 ' + filename, Colors.CYAN)}")
            # Indent context
            indented = '\n    '.join(context.split('\n'))
            print(f"    {indented}")

def cmd_complete(goals: List[Goal], goal_name: str, filepath: str):
    """Mark a goal as complete."""
    print_header("✅ COMPLETING GOAL")
    
    success = mark_goal_complete(goal_name, goals, filepath)
    
    if success:
        print(colorize(f"  ✓ Goal marked as complete!", Colors.GREEN))
        print(colorize(f"  Updated: {filepath}", Colors.DIM))
        
        # Also suggest updating diary
        diary_path = os.path.join(os.path.dirname(filepath), 'diary.md')
        print()
        print(colorize("  💡 Tip: Log your progress to diary.md:", Colors.YELLOW))
        today_str = datetime.now().strftime("%Y-%m-%d")
        print(f"     echo '- ✓ {goal_name} (completed {today_str})' >> {diary_path}")
    else:
        print(colorize(f"  ✗ Could not find goal: {goal_name}", Colors.RED))
        print()
        print(colorize("  Available goals:", Colors.YELLOW))
        for goal in goals:
            if not goal.done:
                print(f"    • {goal.name}")

def cmd_stats(goals: List[Goal]):
    """Show completion statistics."""
    print_header("📈 GOAL STATISTICS")
    
    stats = calculate_stats(goals)
    
    if stats['total'] == 0:
        print(colorize("  No goals found.", Colors.DIM))
        return
    
    # Overall stats
    print_subheader("Overall Progress")
    bar_width = 30
    done_width = int(bar_width * stats['completion_rate'] / 100)
    bar = "█" * done_width + "░" * (bar_width - done_width)
    
    print(f"  {colorize(bar, Colors.GREEN if stats['completion_rate'] > 50 else Colors.YELLOW)}")
    print(f"  {stats['done']}/{stats['total']} completed ({stats['completion_rate']:.1f}%)")
    
    # By priority
    print_subheader("By Priority")
    priority_labels = {
        'high': ('🔥 High', Colors.RED),
        'medium': ('⚡ Medium', Colors.YELLOW),
        'long-term': ('📅 Long-term', Colors.BLUE),
        'daily': ('🔄 Daily', Colors.CYAN)
    }
    
    for p_key, (label, color) in priority_labels.items():
        if p_key in stats['by_priority']:
            p_stats = stats['by_priority'][p_key]
            p_rate = (p_stats['done'] / p_stats['total'] * 100) if p_stats['total'] > 0 else 0
            status = colorize(f"{p_stats['done']}/{p_stats['total']}", color)
            print(f"  {label}: {status} ({p_rate:.0f}%)")
    
    # Motivational message
    print()
    if stats['completion_rate'] == 100:
        msg = "🎉 All goals completed! Time to set new ones."
    elif stats['completion_rate'] > 75:
        msg = "🚀 Great progress! Keep the momentum going."
    elif stats['completion_rate'] > 50:
        msg = "💪 More than halfway there! You've got this."
    elif stats['completion_rate'] > 25:
        msg = "📈 Making steady progress. Focus on high priority first."
    else:
        msg = "🌱 Fresh start! Pick one goal and make progress today."
    
    print(colorize(f"  {msg}", Colors.BOLD + Colors.CYAN))

def cmd_suggest(goals: List[Goal]):
    """Suggest the next goal to work on."""
    print_header("💡 SUGGESTION")
    
    suggestion = suggest_next_goal(goals)
    
    if not suggestion:
        print(colorize("  All goals are complete! 🎉", Colors.GREEN))
        print(colorize("  Time to set new goals for the next cycle.", Colors.DIM))
        return
    
    priority_colors = {
        'high': Colors.RED,
        'medium': Colors.YELLOW,
        'long-term': Colors.BLUE,
        'daily': Colors.CYAN
    }
    p_color = priority_colors.get(suggestion.priority, Colors.RESET)
    
    print(colorize("  Next recommended goal:", Colors.BOLD))
    print()
    print(f"  {colorize('▶', p_color)} {colorize(suggestion.name, Colors.BOLD)}")
    print(f"    Priority: {colorize(suggestion.priority.upper(), p_color)}")
    print()
    
    # Tips based on priority
    tips = {
        'high': "This is a high priority goal. Focus here for maximum impact!",
        'medium': "A solid medium priority goal. Good for steady progress.",
        'long-term': "A long-term goal. Break it into smaller steps.",
        'daily': "A daily habit. Consistency is key!"
    }
    
    tip_msg = tips.get(suggestion.priority, "Let's make progress!")
    print(colorize(f"  💭 {tip_msg}", Colors.DIM))
    print()
    print(colorize("  Run with:", Colors.YELLOW))
    print(f"    python3 tools/goal-tracker.py progress \"{suggestion.name[:30]}...\"")

def main():
    parser = argparse.ArgumentParser(
        description="Goal Tracker CLI - Manage your goals",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 tools/goal-tracker.py list
  python3 tools/goal-tracker.py progress "Build pattern recognition"
  python3 tools/goal-tracker.py complete "Document learnings"
  python3 tools/goal-tracker.py stats
  python3 tools/goal-tracker.py suggest
        """
    )
    
    parser.add_argument('command', choices=['list', 'progress', 'complete', 'stats', 'suggest'],
                       help='Command to run')
    parser.add_argument('goal_name', nargs='?', help='Goal name (for progress/complete commands)')
    
    args = parser.parse_args()
    
    # Setup paths
    workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    goals_dir = os.path.join(workspace_dir, 'goals')
    active_file = os.path.join(goals_dir, 'active.md')
    
    # Create goals directory if it doesn't exist
    if not os.path.exists(goals_dir):
        os.makedirs(goals_dir)
        print(colorize(f"Created goals directory: {goals_dir}", Colors.YELLOW))
    
    # Parse goals
    goals = parse_goals_file(active_file)
    
    # Auto-detect completions from diary/memory
    if goals:
        scan_for_completions(goals, workspace_dir)
    
    # Execute command
    if args.command == 'list':
        cmd_list(goals)
    elif args.command == 'progress':
        if not args.goal_name:
            print(colorize("Error: Goal name required for progress command", Colors.RED))
            print("Usage: python3 tools/goal-tracker.py progress <goal-name>")
            sys.exit(1)
        cmd_progress(goals, args.goal_name, workspace_dir)
    elif args.command == 'complete':
        if not args.goal_name:
            print(colorize("Error: Goal name required for complete command", Colors.RED))
            print("Usage: python3 tools/goal-tracker.py complete <goal-name>")
            sys.exit(1)
        cmd_complete(goals, args.goal_name, active_file)
        # Reload goals after completion
        goals = parse_goals_file(active_file)
        scan_for_completions(goals, workspace_dir)
        print()
        cmd_stats(goals)
    elif args.command == 'stats':
        cmd_stats(goals)
    elif args.command == 'suggest':
        cmd_suggest(goals)
    
    print()  # Final newline

if __name__ == '__main__':
    main()
